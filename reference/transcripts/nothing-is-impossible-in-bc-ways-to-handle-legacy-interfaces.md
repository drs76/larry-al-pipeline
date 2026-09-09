# Nothing is impossible in BC - ways to handle legacy interfaces in Business Central

- **Source:** https://www.youtube.com/watch?v=22FGJbrCaaU
- **Video ID:** 22FGJbrCaaU
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 81m58s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

and welcome to my session about nothing
is impossible in business
Central just but first let me introduce
myself a little bit I'm Patrick Shiva
I'm from from Austria working for Cosmo
consult I'm a Microsoft MVP for business
Central and I'm a software engineer in
my daily work I normally work on Cosmo
albaka so B basically I'm not daily
working with business Central but I was
a business Central develop until a year
ago so I know a few things about
business Central
but what will I talk about today first
of all I will will talk about a little
just a little cimps history of Naf and
business Central
interoperability then we will access a
little bit of my Hardware from business
Central and we will access a little bit
of files so basically it's all about
this um some of the approaches I will
show you today will work for many many
things not only for Hardware or for
files so you will have find many ways
how you can use this what what I will
show you today so what is the motivation
behind this session so customers are
moving to S you don't can use your local
hardware anymore because your your
business Central is not running even in
your your environment
anymore
um it's not always possible to migrate
your third party software to newer
versions so I guess many of you will
have customers which have party software
which is relying on files or which is
just relying on a premise systems or you
also may have some Hardware in your
system which might not be migrated to
anything supporting an API or something
like that so you may have to access this
directly via some um dll or something
like
that and of course some customers need
access to to this machines so we might
have machines like a scale or product
machines or even printers are sometimes
a problem I know there are already some
solutions from business Central itself
for printing but sometimes they are not
enough
and um yeah of course there's there's
many many software and many partners
which are relying on files still because
they have 30 years old software running
on their system and they are not able to
migrate it to something new or not fast
enough to enough to migrate it to
something new so there for we still need
access to files but basically from
business Central perspective or from a
perspective we are not not possible to
we are not able to do
it so of and of course before I forget
it the universal code initiative which
is forcing us even on Prem to use uh
Cloud technology in business Central
which my opinion is a good idea because
everything is then cloud ready but for
some of you it might be a problem
migrating your your
software so before we start I have a
little Sur for
you who of you has still customers using
files of data exchange just raise your
hand
okay almost
everyone who of you still still doing
some
C uh see less hands but Al very much
hands um do have still some projects
which are not cloud ready yet
okay all also almost
everyone so let's start with a little
bit of a history in Na and business
Central um before na 299 we had the
thing which was called Automation and
ocx which is basically a Windows
technology to access your your DLS and
anything you have on on your system and
we could do almost everything I saw
people programming games enough I don't
know why they did it but they did it it
was possible
um and afterwards nav 29 R2 released
with the RTC and with the RTC we also
get dot net support so we could also use
net instead of
automation net has even got greater
abilities than than automation so the
abilities we had were even enhanced and
we also got tot net client Ed in which
we are also could use to enrich our
client
Cent then now 2015 was introduced they
removed s side automation oh then not
really removed it they just switched
over to 64 bit bit and most of the
automations are not supporting 64-bit so
you basically could not use it because
there was not another a
compatibility then na 2018 came and we
got the first version of a a it was a
little bit of strange version of a I
don't know if anyone is using it anymore
but if
you're using it you may know that you
cannot use the a extension from Visual
Studio code because uh you have to use
it the native version which is delivered
with with Naf
2018 but uh something changed with with
L it doesn't have any automation support
anymore but we got uh Native JavaScript
it maybe were were there before but at
least at now 2018 they were
here and then with bc15 we got some new
changes we got the removement of the C
and also the RTC was removed so web
client or the Windows app client was the
only thing we can use and the windows
web client the the Windows app client is
just basically the web client so you can
only use web technology
anymore and then
bc21 was released and we got the
universal code initiative which
basically forced us to set our app Chas
to um Target
Cloud so let's talk a little bit of
about the universal code initiative I
already said that uh we are forced to
use Target Cloud but what does it mean
um we are not able to use net
interoperability anymore or
interruptibility um
Technologies so basically Microsoft is
still doing it in Bas app but they have
some more rights than we have and uh we
can use the net classes which is
Microsoft um repping for us in the Bas
app but we cannot use our own
anymore we have we don't have any file
file access anymore so the the code unit
419 we will see later is set to Target
mostly set to Target on Prem and we
cannot use the functions in
there and of course if we don't have any
interoperability we cannot access
Hardware actually because the web client
is
in is isolated and cannot cannot escape
from the
isolation so let's start with our first
topic we want to access Hardware a
little bit and the easiest way would be
just as we have done it it in the past
we used just a little bit of net and
would look like this it's still possible
in in a but you have to set Target on
Prem and then you could for example read
your
printers but of course it's not s ready
and therefore it's not really a solution
for us
um but instead of using this we can just
jump over and use a middleware in the
shop or something like that
so basically if you're working with
middlewares you just have another
program uh which is developed in some
language I'm mostly use the because it's
very easy to to develop a web API or a
middle layer in theop and we can start
over in a few few minutes if we use it
and then we can call this API which we
have defined in our middle layer from a
directly and of course we need some
installation on our on Prem server
because the middle layer has to install
somewhere um but then from the middle
layer we have access to everything which
is on your network so you have access to
your your local machines you have access
to your local drive and you can
do almost everything I guess or maybe
you can do
everything
but let's not talk so much and let's
just have a look at it um I just jump
over to my
machine so
okay um first of all we already talked
about the net example I will just show
you here how it is used just to see the
difference so we have this net um
object and we can use it directly from
from a but to do this I had to change my
app Jason to Target on brem and if I
would change this to Cloud Target Cloud
um these two files will not compile
anymore so basically we cannot do it I
just switch it back that my so that my
demo is working
again but everything else I will show
you today is um working on on on S and
on on on Prem
so basically from uh Al perspective it's
very simple we have this object which
I've called middle layer printers and
here I'm just querying a API I'm using
the new rest client because it's a
better way to access apis than the hdtb
client you may have been in in AJ
koffman's session yesterday he has
described a lot about it and using that
we just get the response from a local
API and we can work with this response
just as a Chason file and query it so
before we jump into cop I will show you
that there is nearly no difference
between um net and
and exing that uh just have to start my
middle
layer so basically some thing about my
deos if you see a blue window it is the
shop if you see a gray window it is is
Al just to clarify for you I've changed
the colors here um just launching in it
now so the have have a
connection will take
some seconds to to
launch okay now the API is launched it
will be
ready in a few seconds okay so now when
I got to my demo page where I can I'm
calling this everything I can click on
get printers and I've get my printers um
and it's around 150
milliseconds and the same thing I can do
with the net thing it's a little bit
faster but uh that's of course we have a
little bit more overhead um we have
first of all we have the connection so
we have a network connection in between
which is doing some delay but not too
much and also we have this Chason
handling and everything you do on a text
base is really slow so you might have
imagined if you are passing huge files
uh it's very slow but there are
solutions to make it faster for example
the text Builder you might know if
you're using something like that um text
handling is uh very much faster so
basically from a use
perspective you do not get any
difference the only difference you have
here is that I have different printers
that's why um that's because the
business Central Middle tier is running
as an administrator and has only access
to the printers which are installed as
an administrator and the middle layer
which I've launched now is running in my
user context because I've started it and
in my user context I have some more
printers that's why there's a difference
but basically they are both accessing
the local
hardware so let's have a look at um the
C code which is also very easy so
basically you have a template from
Microsoft which look like this so when
you start with with u web API and cop um
you get a program CS which is the main
point you are you targeting in and here
you are adding your configuration but
mostly you can just leave it as it is so
if you don't want to change any Behavior
Uh you can leave it as it is and then
you have so-called controllers for
example I have a controller which is
called
printers and here I have a function and
when
we go back to the a code for net
basically it's the same code of course
there is a little bit of a difference in
the in the syntax but but basically it's
the same because in C we can access the
the same things um what also is very
nice in C is when you just have to copy
the port when you're using the the
default template you also have running
a a Swagger UI where your apis is
already documented so this is
automatically generated from the shop
and here you also can try out to your
your apis so basically it CES with
everything you need to to to start an
API also you have of course this swager
Chason for the open API definition which
can be used to generate code somewhere
at the moment not for Al but maybe in
the future there will be
a converter for Al so that you get Al
code out of this open
API so
um using this you can sew almost
everything um at least this middle layer
is mostly running on the server um so uh
yeah for on Prem you can easy access it
with via Local Host you don't need any
authentification because you are in your
network um you may add authentification
if you want um there are many many
examples on the internet how you add a
add authentification to such a middle
layer
and um yeah because you're on Prime you
don't need it anyway no one can access
it via the Internet you only can access
it via an local
network but for SAS it's a little bit
different it will work also for
SAS but uh at least you would have to to
uh publish a port to the internet and
you will have to add some security so
you need an authentification because
otherwise when we talk about m about my
printer example everyone can print on
your local printers and I think you
don't want to do it and although you
might uh think about Security vulner in
the internet so if you're not sure how
to um secure everything then maybe
that's not the right solution and that's
why I not recommend this solution for
for S there are better
Solutions so
basically we now had this BC server is
calling the middleware API and the
middleware layer is calling the local
hardware so one solution which is also
working for S is instead of the PC
server we're using our web client as I
said at the beginning our we web client
is capeable to
execute uh client uh JavaScript code so
basically um you can use JavaScript to
call your
API
and
um it's basically the same like you used
for the business Central but uh for the
business centrals here before but the
difference is that now the code is
executed on your client so even in SAS
you are in your local network and you
can use Local Host and again the
installation and the process in the shop
is the same
but just a call is is switched over from
a oh there is a mistake in here it
should should be call Api via JavaScript
um so we are calling it via the
client so let's also have a look at
this so when you're working with client
ents
you may have
um a new object type which is called
control addin and here you can Define
some JavaScript um script you want to
use and you can expose a function for a
so if you have a function in your
website in your client Ed in which is
called call Web Service uh a will be
possible to to call it so basically we
have a look at
JavaScript code it's very simple I
didn't add any error handling here of
course if you want to use it in
production you may add some error
handling here so for example if the the
web client if the API is not responding
you may react here in the JavaScript or
you're just passing the error back to
business Central and you to react in
business
Central so when I want to call this uh
basically just
include the user control to the page
where I want to use it and afterwards I
give it a name here afterwards I can
access it via current page do name do
function I want to
call um of course you will have to uh to
have a page so this will not work from a
code unit or something like that uh but
if you want to access some local hard
Ware uh which there are some use cases
for it my use case is for example a cash
drawer if you have a point of sales and
you have a cash drawer where your cash
is inside you may want to open this cash
drawer from the point of sale and
therefore you just can write an API
again I have done it in the same API
before um and of course I don't have a
cash drawer here that's why I don't have
any code to it directly but I just have
a a message here that we will see in a
few seconds
so
um this
one so this my client in demo as you can
see you can see nothing because I I
don't add any visuals to my my client in
you can do you can add any visuals but
in my case I just wanted to execute the
code and I don't need any visuals for it
because I just have an action here um
and when I call this open cat draw
action the API is responding so
basically if I would have a code inside
my my API to open the cash drawer it
will would be open now
um yeah but this is a local host so of
course it would work a local
host um but it will also work when we
jump over to my cloud
environment it will also work from here
so I'm now in a cloud environment I can
also access from my cloud environment U
my local machine and everything works
fine
so um this works fine if you want to
access client Hardware but if you have
installed your your Hardware devices on
a server or some something like that um
and you are in SS you might need a
different solution and there are always
solutions for for
anything and we now just add another
layer which is an Asia relay um Asia
relay is just a very small Asia resource
which can redirect uh your calls to a to
another um to another
location so this all is based on the BC
agent from Microsoft um it's an open
source example from Microsoft how you
can access local systems um I will show
you the repository in a few seconds um
but one thing about this repository it's
a sample repository and it is as it is
so Microsoft will not fix any bucks if
you have a bux there maybe they will if
you ask for but they don't have any any
support for it officially because they
are not meant for production you have to
change it maybe for
production and the Asia relay is secured
V key so you already have some basic
authentification of course you can add
more authentification
and um there is no public open port
needed uh
because when we go back
here my back button doesn't work on the
clicker for some reason okay when we can
go back here I just want to to clarify
the workflow from here so basically um
we are calling from the BC server we are
calling the Asia
relay and the Asia relay so the PC
server doesn't know anything about the
middleware and it's just calling the
Asia
relay and from the middleware we are
connected to the Asia relay and waiting
for for requests so B both systems are
just connected to this Asia relay and it
is in between and the middleware in cop
which is the BC agent basically um is
listening so it is poing if there
something you might want to to retrive
from the Asia
relay so that's uh how the repository
look but I will open it it's the akms
/bc te um there are many many examples
in there so if you want to have some
ideas what is all possible in in
business Central you might have a look
inside of this repository um you will
find a lot of information in there and
and the second thing we are using is the
Asia relay I will show you in a couple
of of moments how we we create an Asia
relay um and we will also talk a little
bit about pricing because every time I
talk about Asia um the first question is
how much does it cost and at least I can
tell you it doesn't cost very
much so let's go jump over to Asia
when we want to create an Asia resource
most of you or some of you may know you
just can enter the name of the resource
you want to
create in My Demo I want to create a
relay just click on create take some
couple of of time then you choose a
resource Group and you choose a
name Tex s
and then the relay in the background is
created so Microsoft is setting up
everything for you um it takes most of
the time around 10 seconds or maybe 30
seconds to to be provisionalized and
afterwards is it is ready to
use um and then some when it will pop up
here yeah it's already here go to
Resource and when we are here we have
two different entities
uh we are talking about the hybrid
connection today uh which is an just an
on on Prem s hybrid connection which is
supporting you um here we can also
create the
connection
and we can here choose if we want to use
client authorization or not so we can
use it here um I call it I call it my
relay and then I Al also create
my my hybrid connection and at the
moment there is stated that we have zero
listeners uh but we will connect our PC
agent in a few seconds um and what we
also have here is when we jump in it we
have a shared access policy which is
used to authentification we will use it
uh in a few
seconds um to authentification
business
Central but first let's jump over to
akms PC tech oh this also a very um a
very interesting akms BC all if you
don't know take a look at it there you
have all resources for business Central
it's a a very long list of resources
so you may have a look but I don't want
the akms PC all I want
akms PC
Tech it's pointing to a GitHub
repository it is public and yep as I've
said there are many many examples for
example we have app insides for tetri
here we opena here we have some
performance toolkit clock migration and
so on and so on um we have everything we
would need here and we also have this PC
agent thing there's also a documentation
from Microsoft how this thing works so
also the the basic workflow which I've
described you in my slide is here so you
may find informations how to use it here
but when I used it the first time it was
Al even if there is is a documentation
not so easy to use uh therefore I will
show you in how it
works okay then first of all let me show
you the
repository from Visual Studio code so we
can click through it a little bit
easier um what you have here is uh
three base um Technologies I would would
say uh we have the BC agent which is
doing the whole communication stuff and
we have a common library and we have a r
request dispatcher so basically most of
the time just leave it as it is um
you only have to change the connection
which is inside of the PC agent but most
of the time just leave it as it is and
then we have the plugins U we can write
plugins for it so I have again a plugin
for printer which is again almost the
same code so it differs not really we
only have here this Mark for plugin
method and that's the only thing we have
to do that it's available via the agent
via the the Asia Rel
so let's now connect
our um our PC agent to our freshly
created
relay so first of all I need the name of
the relay which is PC tag
session I've enter it
here
um I need the name of my
relay also here and then we have
something which is called the key key
name and key so therefore we already
talked about this shared access
policies um here I can create
um this policy and when I want to create
I have the three different options for
the permissions there is a manage
permission which will you give
possibility to also manage this resource
and create new keys and so on but we
have also send and listen um policies so
from a S perspective we are want to
listen so I create a key which is called
listen key or we can call it isap or you
can call it whatever you want the key
the key name doesn't
matter and then we have a key
here um and we can fill it in
here change dis
spelling uh just enter the key here
uh then launch the C
project and we see there is a connection
to I don't know what s SP is standing
for but we have a the connection to our
oh maybe it stands for service bus um to
our service bus Which is the technology
behind the relay so um
the connection is done and the the
different plugins I have created are
already here um
so of
course a and business Central still does
not know anything about this relay
therefore we jump back to our Al
code and be before we jump in my
implementation I just show you a library
so in this PC text samples which I
showed you before there's also El
library for accessing the service pass
relay so uh you don't have to take care
about the connection which is doing this
library for you and again there is no
support of Microsoft so if you have a
bug you may have to fix it
yourself um but the inside here we
have
um relay
setup
page we have here this service bus relay
setup page
uh which we can call uh from from
business Central then and we have one
code unit which we are using later which
is um connecting to the service bu so we
have here basically an initialized
function which is doing the the
authentification
and afterward we have a get function
which is getting the information from
our local
API so
I already published this app in my
business Central therefore I can just
jump over when we now go to settings and
to advanced settings then we have the
service
connections and the the app registered
inside of the service connection so we
here we have an Asia service bus relay
setup and here we
can uh connect our business Central we
take the same things
here we have our relay
name and we have a hybrid connection
then we have again a Shad access policy
we need to create and a sh access key so
I'm now creating a second key I'm not a
huge fan of having one key for send and
listen because uh if a key get
compromised you only have one side
compromised and not both sides and you
only have to change one side so
therefore I mostly create more than one
key so I call it now BC so that I have
the same my example and I allow it to
[Applause]
send and then I just paste the key
inside
here I don't want to encrypt my database
now and close
it so
um when we have a look
at the Asia relay now because we already
launched our C program we see there
there is one listener we can connect
more than one listeners um but basically
Asia decides which listen is executed so
it's just about load balancing if you
have a huge amount of calls maybe you
want to start one more than one listener
to to paraliz things a little bit but
when we talk about costs later I will
tell you that it might make a difference
if you have more than than one
listener so basically when we go back to
to our
example we now have the spec agent
implementation
also and first time takes a little
because it needs to start
up if I could execute it a few times it
will warm up and then um it will get
faster and just a little comparison we
have here 150 Mill seconds for the BC
agent and we
have almost the same time so it depends
between 100 milliseconds and 200
milliseconds uh in in both scenarios so
even when we now have an additional step
so we go to Asia and from Asia to the
local machine the performance is not
really differing um that's a question I
get really often how slow it is but um
you may not recognize any difference if
you're using the PC agents um the middle
layer from performance so at least if
you have a proper internet connection of
course if you have a bad internet
connection from your business Central
server
then you might get a difference
here okay so let's have a look at the AL
code for the the PC agent it's quite
simple
um I just have declared some some basics
in here so my my plug-in name and my
version and my my function which I want
to call and I'm using this code unit
which is called Asia service bus
relay um and again here I have a
function which is called get printers
it's um mostly the same code than we
have in the middle layer just to have a
comparison uh we have here the get
function and we also have here the get
function only only difference is we
using a different technology to get the
things um but basically um we have the
same
things um yeah this is a dry function so
you can also do something like
if to secure it a little bit so that you
don't get an error but maybe you also
want to to get the error um yeah so but
basically the Jason you're getting is
the same and the Jason handling is the
same so basically only the connection
differs a little
bit
um yeah I've already talked about
pricing um for every Asia resource you
have uh nice pricing
overview I should that
page to my favorites so then I don't
have to look it up every time so
basically a listener is costing 9 a
month
so um when you have more than one
listener you may also pay more than €9 a
month and you also have a 5 gab limit on
The Listener so if you're sending data
to the The Listener you uh May exceed
the 5 GB after afterwards the gigabytes
are are build separately with 90 Cent
per
gigabyte but to cope with it you can
also use for example an Asia FIA or Asia
plops um to send the data to through and
then just tell the listener where they
can find the data it's much cheaper it's
a little bit more more complicated more
complex but it's much cheaper if you
have much data then you might use
this um
yeah just jump back
here so let's compare this solutions a
little
bit um basically we have the first
solution um which is do net it's not s
ready um but every other solution I
showed you is s ready I would call the
middle layer a little bit limited sou
ready because you have this public Port
exposure but basically it is s ready um
there are difference where the code is
executed I've not mentioned it for the
net because the net is not really an
option
um but the middle layer and the the Asia
relay executed on the server or at least
the Asia Relay can execute it can be
executed on every computer in your in
your
environment and at the JavaScript on the
JavaScript side you on your client
machine so um you can do everything on
your client
machine there are also some differences
about the costs um you have additional
costs for the Asia relay but for the
other Solutions you don't have any
additional costs so uh basically if
you care a lot of costs then you might
not use the Asia relay but at least when
you think about a business Central
project what are N9 EUR a month um uh
business Central user is costing I don't
know the exact amount but it's up around
150 I guess a month and compared to that
uh €9 a month is nothing I guess you can
do it in almost every project without
even uh have to discuss a lot with your
customers because they will not
even uh recognize that that there is a a
change and then I have some opinion on
these Solutions um this is nothing which
is said but in my opinion I would never
do the. net because you may not upgrade
it to S and you may get problems with
the universal code initiative because
universal code initiative is also a
problem of a license you have to to use
an additional license to use the
universal code
initiative um then for the middle layer
where why sh I would prefer this for on
Prem Solutions so if you're on Prem then
I would go for this solution in my
opinion because it's the easiest way and
you don't have additional costs and you
can do the same things like you like you
can do with the BC
agent and if you want to access any
hardware on your your client computer so
like I've said a point of sale then go
for the JavaScript version
and in every other case or in SS
environments use the Asia
relay of course there are many many
other solutions to do this this just my
Solutions which I've used already
um I guess when you search in the
internet you will find other Solutions
there are maybe also ready to use middle
layers somewhere um but as I am a c
developer um
I'm doing it in the shop and just one
thing I want to show you uh how easy it
is to set up a a API in
C so I open up a
new Visual Studio
code when you go to the
terminal you just enter net new web API
and you give it an a name and you say
use controllers
BC text
session then you give it an output
directory so I just copy
this then in the background that the
template is loaded and when you jump
into this
directory you already have a ready to
use example uh with one controller and
when we go to WS code
so it's not blue now because I have had
to set up it in the workspace but this
is also
C uh when I launches I get the question
which protocol I want to
use it's starting up
and as I said you already get your
Swagger UI so you don't have to
configure anything and you're ready to
start with developing uh your your
middle
so that's about local hardware access um
I
guess you can do anything you want with
it
um but if the Asia relay is a solution
for everything we can also do other
things than local hardware access we can
of
course um
oh I have my demo here you can of course
for example access an SQL a SQL table so
I have created
an uh SQL table which I want to access
um therefore I also created just a
plugin in
cop um you can use it for writing or
reading a SQL data from an on- premise
system and you can also call procedures
or something like that what you might
not do you cannot access the business
Central SAS database because there is no
public availability of the the database
even if it's just an Asia SQL database
you're not able to do this but you can
access your on premise uh databases so
for example I have here my demo
environment and just to show you that
it's really live
I just enter a
few um more records when you jump back
it will work again and you're really
live on your SQL database um not showing
you the code for it now uh have a GitHub
repository for it so if you're
interested in the code you can have a
look at the GitHub repository after the
session I will give you the link um and
what we can also do using the the PC
agent we can also uh read a file by the
PC agent uh just have to make sure that
the file is there so where's my PC
agent
yeah of course you can pass a file name
uh but for my example I just
hardcoded that there is a file which is
called teot file uh and of course you
can use this PC agent to read a file it
works and you will can you can access
your local
system so maybe we are done for today
but if it would be that easy I wouldn't
have mentioned it on my agenda at the
beginning uh or maybe let's say there
are easier ways than using the PC agent
for for accessing file so for accessing
files the PC agent is a little bit of
too much
um and let's jump over to the file based
interfaces
so when we had C or we don't have the
universal code initiative we had us on
premise server which has directly access
to the files Al still was possible to to
access these files the code unit 419
still exists um you can look up it in in
the Bas app uh then we had some chop
cues maybe which were querying some
files on our local
machine but as I already said most of
the functions inside of the code unit
419 are for scope on Prem and therefore
we cannot use it anymore and it wouldn't
also make any sense in on S because then
you would write files on your SAS server
which uh you don't have access with
other systems so you can write could
maybe write files there but you then
then could not access this VI other
systems so therefore there are some
buil-in possibilities in s in business
Central um the first buil possibility is
already there since I don't know when it
was already there in CL maybe it was
already there in the first version of
nav Vis I don't know I haven't checked
it but you can use blops inside of
business Central databases and you can
use PC code to write
files but in my opinion don't do it I
will blow up your database uh your
database will get hu huge if you save
files directly in the database
therefore it's called database and not
file system um and even in SAS you will
get a problem with your storage because
in in SAS the storage is limited um so
this might not be a solution for you but
there are other built-in Solutions in
business Central we have um one drive we
have SharePoint we can use the Asia plop
storages and we can use the Asia file
share so basically we will talk mostly
about the Asia file chare because it's
in my opinion the easiest way
uh especially when you work with uh
local Legacy software which want to
access these files and this is the
easiest way so basically you have the BC
server you have an as file service API
and you have the Asia file share so
basically when you look up the the API
is is
very good
documented
uh so there's a documentation for this
whole stuff where you have
the operations on files for grade file
or for get file and so
on but uh uh fortunately we have also
something which is called another akms
link
akms PC apps which is basically the base
app of uh uh the system app of business
Central and some other apps are also
here and when we have a look at the
system application of business Central
we will find a lot of libraries so there
are libraries for a lot of things and
there are always new libraries in there
sometimes they even not mentioned in
release notes or something like that
because Microsoft is just using it for
their own implementations so what I do
is after every major release I have a
look at this or I go to to another
GitHub repository which is Stefan Maron
you may have seen it he has
the business center code
history uh where you can uh just compare
different PC versions back to I don't
know um and there you can do comparisons
between PC versions and there you will
see if there's something new added and
yeah two versions ago Microsoft added
the Asia file service API so they
implemented this whole API for us and we
don't have to implement it ourself
anymore um they also implemented plop uh
I guess plop was one of the first uh on
uh was one of the first open source
contributions before Microsoft even
started open
source
um they I think it was seon Fisher which
has created it and they took it from his
his own repository to the to the system
app and yeah then they started this this
open source initiative but we are using
the Asia file services today where we
have some code units to use it basically
we have this AFS file client and with
this AFS file client we can for example
also grade files read files write files
and so
on uh as I said it's a will play y API
we have this AFS file
client and we could also mount a file
share via uh a network drive so you use
it as a network drive and you caness is
VI Windows seamlessly so our upgrade
from a normal local file system to an
Asia file share is just seamless because
um your legacy software on your local
Windows machine will not even recognize
that it will work on S when you use an
Asia file
share so let's create an Asia file share
we again go back to
Asia there are something called storage
accounts there are different types of
storage accounts
so first of all we have um to create the
the main
account we have some different pricing
options but I just take the cheapest one
now uh you can look up the pricing again
and you can then just create
it and
yeah for my demo it's not relevant that
it it is performant it's just has to be
there and for most cases at our
customers we are also using the cheapest
version because uh the cheapest version
is even pretty uh fast but if you have
thousands of of rides hour or a minute
then you may get uh problems with the
cheapest versions and you may switch
over to a more expensive version and you
also have some options for security
for for GM D Storage and so on so when
we have our storage account we have
basically four different options here
only the first two are supported by
business Central we have the first one
which is the the Asia plop storage and
we have the second one which is a file
share um I just switch over to my
previous
create
uh yeah no it's not this
which yeah this one should it be um when
we go to our file
share uh we have here a
button which says connect and when I use
it I can show a script and then I get a
poell
script let's copy it and jump over to
the
Powershell uh execute it
just making a connection from my
computer when I now jump to my computer
I have a a drive set which is connected
to the Asia file just so when I create a
file for
example yeah I'm using this sem semic
uh syntax because I need it later um so
when I save a file here I can just jump
over to the Asia browser and see my file
also here uh so this is really live
connected it's not synchronized um when
you write to the the file system it it
triggers the API in the background and
uh it's really live so when we jump over
to business
Central I hope I have connected the same
here when I enter the name I can
also read this file and I have also a
connection to
it um so let's have a look at the the a
code code for
it um we have here a file demo so this
is my file demo page and here I have a
read functionality and it's quite easy
you just need the the so we start with
the file client it's a code unit you
just need to initialize this code unit
um you give a storage account a share
name and a SAS token SAS token can be
created in the the Asia file system in
the the Asia
portal and then you can
connect and uh afterwards you just can
get the files and you get such a
response which is called AFS response
using this you can all so check for
errors for example uh for example if I
would do something like
that and I can also check
if um if it's
working sometimes co-pilot is even
working uh helping you but at least in a
sometimes it does not do the cor the
right things at least in this scenario
it
does um so that's basically the code
behind this input uh we can do the same
for writing so this
is second
file I call it input two and write this
file and of course it's
here it's not a rocket science just a
little basic API from
Microsoft and you can use it you can
also get streams on your file so can you
can use it for XML ports or something
like that or for Exel puffer or for
anything else you have done previous in
in the days um so you can work with
these files probably like you've done
before
um
yeah this is nice I like
it um you can just access every of your
files you storing on this Asia files
here and it works like it worked before
only you're not using the the code unit
49 You're Now using this this AFS file
client and it's
also uh not so an expensive Asia
resource so you can still uh be very
cheap with this
solution but in my opinion I'm not a
huge fan of querying files so when you
would use this and you want to import
some files maybe you will have a a chop
Q which is clearing it so on testing if
there's a pile um so in my
opinion this is not a a nice solution
let's turn it
around we now want to react on on on
changes in the file system
and directly send the data to business
Central um and we are using a thing
which is called a file system Watcher
from net in our C program again and the
C program will read the file will pass
the Jason or we will pass this this
semicolon thing the Cs wi file and we
will then send it just to the business
Central API so instead of using files
inside of of of business Central we are
using the files outside of business
Central and dealing again with
apis and oh
let's have a look
at at
this
um again I have prepared something for
it using the the the file system buter
is Al very easy in the shop so basically
you create this
this object which is called file system
buter then to subscribe to an event in
cop and afterward you just say where you
want to
watch and then you start Rising your
events so to show you the demo I have
again to jump over to my cloud
environment because I haven't set up the
apis um for my local environment so just
open it in the browser
and log
in so I have here a small page where I
can import data via the
API um I just clear it so that we have a
clean
solution um and we launch our well first
of all we have to create our folder
where we want to watch it so I call it
watched and then we launch
again our net
application so file system which just
started
and when I place a file in
here
now file system watch is reacted on it
sending this file to
BC I
tries triy sometimes because there may
be a lock on the file but the file is
sent successfully when I go back to
business Central I have the data inside
here so basically now uh business
Central doesn't know anything about this
file but the data is still uh Landing in
business Central so you can also use
files without even using files in
business Central and um
it's from the business Central
perspective very easy you just have to
create uh let me have a look where I
have it you just have to create an API
page um you're defining your AP
publisher your API
Group um and then you have some
fields and from the business center from
the C perspective it's also very easy
so it's
here so basically you can ignore most of
the code here uh we have
just
and had the deay request message which
we are creating which is going to my
cloud container uh it's calling the uh
API with the publisher and the group and
the version and so on and I just create
a Json file out of it and send it to it
and basically we also have the HTTP
client here so basically the HTTP client
from from a is just the same as the net
HTTP client it uses in the background
the same things so we have the same
functionality in here and yeah using
this way we can automate our
files uh we can do it all also the other
way around so when you have an business
Central AP you want to write a file from
business Central you can also use the
web hooks Which business Central is
providing so business Central allows you
to to subscribe to apis I don't have a a
demo for it um but then you are cap able
to subscribe this API from cop and if
for example if a sales order is created
uh and you want to export this sales
order then you you can create hook to
the sales order API and when the sales
order is created you just create the
file from aop perspective so although
there are different ways how to do
it
um most of the time the first way which
I've showed you is the easiest way and
the way you want to go but I want to
show you also some different
things and when we have again
a look at this workflow so
basically we uh have a workflow
here uh where the file is going through
and we are reacting on on something and
I have written it in the shop but maybe
there are other things to automate
something maybe maybe even Microsoft
gives us something to to automate things
uh let's jump back some further ideas
where don't don't have a demo for it but
just to give you a idea what you can do
um for example you can use power
automate BC connector to get data from
business Central and there is something
called an on pre premise data gateway to
connect to your local file system so you
can even use power automate to Lo to
connect to your local file system and
then you can create a flow like this
it's of course it's not a full example
it's just giving you an idea
uh what you can do with power automate
um maybe I will create a whole example
on my blog but I've didn't did find out
this solution uh just two days ago so
that's why it's just on a slide and not
on a demo I didn't have the time to to
get a demo running for
it but of course you can also do this
the other way around you can also use
the the
on premise data Gateway for for power
automate to read files on your file
system and write it to the PC API so
basically we have the PC connector and
we also have this connector for the file
system and um we can also use it to
write files so we will just have a small
look at Power toate to give you a
glimpse what's possible uh
when we go
here okay take some
time we create a new flow and automated
flow I skip it and if I go to add
triggers I have this
file uh
triggers which is called file system and
there are basically two triggers from
the file system so I can react for
example um to when a file is created or
when a file is added or modified and as
it St States here you can connect it via
the on premise data Gateway you can then
set up here your connection for as it
says for a local file drive when you use
this solution you don't even need a Asia
file share you can just use it out of
the box just install the the Prime data
Gateway I don't want to use my clip
but um and we have some more options
using the the the file system
connector um yeah we have almost every
options you may have
uh with your local file system so you
can copy files you can create files you
can read files and so on and then
afterward you after you've read it you
can use the business Central
connector and here are also many options
you can do so you can create a record
based on on on the file in business
Central just by using the create record
connector when use the create Rec record
connector you can choose an environment
I cannot use my environments now but
because it's are the cosmo consulter
environments
um but as I said it's also possible the
other way around I just show you
the triggers for it so when we again go
to Power at made triggers we can again
have a look at business Central and we
have some triggers which can trigger a
flow for example when a record is
created or when a record is deleted and
so on and we have also this new business
event thing which is an event you can uh
trigger from from a and then react to it
from um from Power automate and you can
pass some par meters and so on and you
can work with it so maybe I use this one
now and again you can connect it to your
business Central
environment um
let's see if they are showing the events
also here so as you can see there are
all already some business events in
inside of the Bas app which you can use
out of the
box and then again you can add an an
action for the file system uh as I
showed you before we have this grade
file and so on there are also uh
connectors for other file systems so if
if you want to switch over to another
file system you can for example use the
connector for Asia file share you can
use a Dropbox connector uh data world
connection SharePoint one drive and many
many more I guess I haven't seen the
full list so you might find the correct
connector for you inside of this power
automate um
thing so before we come to an end here
are some res ources which you might want
to use um most of it are akm AMS links
so as I already told you the akms BC all
is a very huge source of BC business
Central resources you can find the
learning portals the
documentation examples there um and it's
linking to
everything then uh we have the two
repositories we have seen um then of
course my blog on my blog I've uh
documented some of the solutions which I
I showed you today and the last one is
the kup repository where the whole uh
example is in it and the qu code is
pointing to this GitHub
repository so one last thing of course
the answer to life the universe and
everything is apis and Asia so you can
um do and solve almost everything when
you're using uh apis and connect to your
apis
so um yeah we came to an end of our
session so now it's time for you
to ask some
questions
um
and I give this Cube to you uh please be
make sure that you speak directly into
it's on the floor the floor here oh it
fall
out um maybe one of the audio guys can
come down and fix the
cube yeah I think the audio guy is
already coming down
give me one second to put the F okay
this
T
okay okay it seems to work
now um I only wanted to know if it's
possible um to use JavaScript uh to use
a file access client side file access um
not really uh there are libraries for it
but the browser is isolated so you won't
get out of the LI of the browser but
JavaScript is not only used in the
browsers it's only also used for example
in vs code so vs code is basically
written in typescript which is another
version of of of JavaScript so there are
libraries for file access but you won't
use it in the web client because the web
client is running in the
browser okay good
question so you can pass the microphone
over
Clos okay I want to
know if we have a customer with two
houses and I had to print labels from
the
SAS uh I had to access to the local
printers but uh there are two local
printers one for a PC in the first
Warehouse and one in the second
Warehouse uh which solution is better
because I think that I had to install
two
mway um so you accessing files on you're
accessing systems on your client machine
or laptop or something or on your yes
the the client actually is on Prem but
we're uh trying to move to SAS okay but
do you still have a server on Prem then
or will will you have it on on the
client machine because if you have it on
it on the client machine then the the
JavaScript solution will be the better
way in my
opinion and if you're
running the connection on your your
server so it's a central thing which
everyone has to access um then you may
use your server and then the PC agent
would be the better solution so a server
with the two printers uh share the
server with the Asia relay and so on
would be if you were will go to sou
would be the better solution okay any
other
questions uh wouldn't you be able to um
call the middleware on uh server with
the JavaScript solution so not just call
Local Host but the server name of course
if you're running on Prem you can also
call a middleware on a server and even
from JavaScript you can call a
middleware which is running somewhere on
the server maybe also your your local
hardware is supporting apis already if
it's supporting apis already you can of
of course use just the apis which are
already there um and you can access
everything which you have on your local
network so it doesn't depend on Local
Host I've just showed Local Host in my
my examp
because it's an easy way how you can do
it but of course everything in your
network is open for
you
so I try
to throw
it but maybe you give it
back there one more last question maybe
we give it over to
here okay there's one in the back but we
have time for another question then
all right so my question is asking
around the a high share um what's the
difference between all the advantages of
that against the um uh share
points uh the advantage of the F against
SharePoint yes just the advantage which
I like the most is that we are just able
to connect
our um Windows machine directly to to
the the file yeah and that's not
possible for the for the SharePoint
because SharePoint has some syncing
mechanisms of course you can use it via
the one drive uh but um then you don't
have the the live view on the file you
have always a
thinking maybe give it also
back so I guess we have one question in
front of
here it was here
yes uh are there any connectors for SQL
Server databases from the cloud because
uh as far as I know you cannot access
this an on premises SQL Server system
you mean if the the power autate
triggers are available if you in Cloud
uh not with power alterate something
which is faster and which canor
something which is faster and which can
really handle lots of data and
throughput I'm not sure if I totally
understand your question um so you want
to use the power automate connectors so
what not with power automate is is it
possible with any sort of middleware to
connect the cloud system to SQL server
on premises database yeah of course you
can can connect your your local
middleware to to the cloud and you can
also run your middleware in the cloud if
you want so there always ways except
you're reaching it somewhere via an URL
uh you can do almost
everything
okay any other
questions then if there do we have
okay yeah so we had a client who has a
couple of
external SQL tables linked to the system
what would be the best can you please
talk a little bit more yeah sure can you
hear me now yeah all right so we have a
client who has external SQL tables
linked to the BC database and if he
would mate to Cloud solution what would
be the best way to upgrade that yeah so
you have a database which you're
thinking yeah a couple of databases
actually um there are different ways how
to do it um they're also built in
functionalities in in in in SQL Server
uh but in my opinion the easiest way is
to create also a middleware which is
just querying the whole uh SQL and send
it to the to the API so maybe uh it's
just a a chop on your local Windows
machine which is running uh every day or
something or whenever you want even
Windows also has has this this this task
scheder included so you can execute your
your local program every once in a while
whenever you want would this be
efficient for a larger amount of
data yeah
okay when there are no questions left
uh thank you for listening to me and I
wish you a great conference and uh safe
travel home okay afterward
