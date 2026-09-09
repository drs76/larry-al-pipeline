# Http Communication Best Practices

- **Source:** https://www.youtube.com/watch?v=zj2VfeTl7OI
- **Video ID:** zj2VfeTl7OI
- **Channel:** mibuso.com
- **Published:** 2024-06-16
- **Duration:** 83m44s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

yeah welcome back well uh I had a
session in the same room this morning
together with valo and now on my own
completely different topic about HTTP
communication um yeah what can I say
there's actually a lot to tell about HTP
communication I seem to have this topic
uh around HTTP or web services and API
quite
sometimes um the purpose of this session
is to dive into the HTTP client and
everything around it number of best
practices how do they uh work uh have
some focus on well why do that just the
next one agenda the default pattern for
the HTTP client so how do we uh call and
how do we handle um the the exceptions
that can happen what is actually the
difference between a get post the patch
and send command because they are
different but why and how um I want to
dive into HTTP headers because I see a
lot of people struggling with setting
headers at a correct level um we can set
them at three different levels why do
you set them on the on the HTP client or
on the request message and what about
their content type header that is on the
content HTTP content why actually do we
need to remove the content type header
every time they want to change it why is
it there uh to begin with um I hope to
explain that um I want to talk a little
bit about performance with the HP client
it's a heavy object that takes really
some time to load um so what can we do
about it um then some best practices how
do we um design our code when we work
with the HTTP client what should you do
what should you not do we have the new
rest client module uh that was
introduced in uh version
23 um which actually takes away a lot of
the stuff that I talk about maybe I
should only talk about the rest client
and then uh probably uh just uh you can
skip a lot of the uh content that I have
before but at least then you understand
what's going behind the scenes and then
I'll end with uh if time permits with
the uh with some new developments that
I'm working on uh endpoint and O A
management that should actually extend
that rest client
module well that's the agenda little bit
uh challenging I have actually no idea
if I can manage that in 90 minutes maybe
I need more maybe maybe less only thing
I realize is that I'm between you and
the beer so I keep that in
mind okay so the default pattern for the
uh using the HTTP client
um actually um the commands that we have
on the HTTP client to get something or
post or put delete we have and the sent
um they return a bullion and a bullion
actually indicates if a response could
be
received um or was received the Boolean
does not mean that the response was
successful the Boolean D indicates did
you even get a response so maybe the URL
was incorrect or was no server at that
URL or maybe the URL could not trans be
translated into an IP address so the DNS
uh is not giving back an uh IP address
for that URL uh maybe the server is just
down could not be reached did not
respond whatever it could be many
reasons maybe it was blocked by a
firewall you don't know but he could now
reach that uh uh URL he did not get a
response so you should always test that
one always test did I get back something
now in case of um a false the meaning I
did not get back a response you should
also test the property on the response
message is blocked by environment the
little strange thing here is that there
is not even a response message at that
point I mean there's no content no
headers whatsoever on response message
you did not get a response but there is
blocked by environment that is a Boolean
that could have a value um and if that
is false you need to raise an error with
that uh error message is it blocked by
environment or well you did not just get
a response um whatsoever now that
blocked by environment is actually
something that um sometimes annoys
people first of all it only occurs in
sandboxes so um the idea behind it is
that you want to control the user needs
to control if an app really um is
allowed to make an outgoing call think
about a Sandbox that is a copy of a
production environment you do not want
your um uh sandbox then go out to um
real production environments make calls
to them and uh place maybe some orders
or whatsoever I mean this is a real
scenario that I've been in it's a long
time ago but someone was very proud of
the integration that they created uh
that we created um for automatic
ordering at a V with a vendor and they
ordered 100,000 pieces of this and
100,000 pieces of that and literally one
or two weeks later it was B at the uh
gate and the fendor was happily uh
delivering the order that was uh not
really intentional so uh you want to uh
prevent that so that's why uh in the
sandboxes uh even if if they're copied
from production then all apps are
Switched Off for uh external HTTP
requests now there is a record in the
table enough app settings and that is
controlling the allow HTTP client
request it's pretty much the only field
in that table um if there is no record
in that table then the user will be
prompted what do you want do you want to
allow always once or do you want to
block all always or block ones um if you
say allow block ones one of the once
options then that table will uh stay
empty will not be a record for the app
that is trying to uh make an HTTP
request and the next time you make a
request with the same app the user gets
the very same answer if you say uh
always either allow always or block
always then that table will uh get get a
record for the app and HTTP client
request allow HTP client request will be
set to true or false based on what you
do with allow and block now if that
record exists then the user will simply
not be prompted the user will uh just um
of the HTTP uh request will just be
blocked or um uh be granted allowed if
that record exists based on that
field now in case you say block once or
block always and that record is being
created with allow HTP client request
false then the HTTP response message is
blocked by environment will be set to
true so then you know hey I'm blocked by
the user and you can gently ask the user
hey please allow me because I cannot do
what I want to
do maybe that is on
purpose um yeah that is just how it
works now what you need to keep in mind
here is that this um record can be
opened from the extension management
page and when you do so then uh it will
automatically be created effect uh as an
effect you will not get that prompt
anymore it will just
block unless you say true in that page
uh when you copy a production to a
sendbox then uh the enough app settings
table will be cleared um and you can
also create that record yourself in your
code in your install code for example
just to self allow the app for doing
HTTP request there's also an option so
um let me quickly demonstrate
this um how that
works so
um going have
my this one no but that's not what I
want come
on this is the one I want to
open and I'm going to opening a
page for HTTP demo HTP request we will
spend some time in this page in this
session um
first of all I go to my extension
management
page and find my app it's over
here so this one is now allow for HTP
request I just pretend that it was brand
new so I delete this record do you want
to delete that record yeah I want to
delete it seems like I'm deleting an app
I'm just deleting the enough app
settings record that's fine and now if I
say hey uh send a request I get this
message and if I say um uh allow once
that's fine just going to work give me
something back and the next time I do
the same thing it's going to give me the
same
message and if I say um send
request um allow
always then I don't get the error
message
anymore just r works but now if I go to
that extension management
page then you see this one is existing
here and if I delete
it I'm back to the
beginning so I get that message again uh
that say allow one so it's not creating
that record but
now I open the page
one time meaning I do not allow here I
just have now the record created and
then it says sorry it's blocked by the
environment I don't get that arror Mage
anymore so this can be a little bit
confusing how this works but now you
have seen the internal mechanism of
that all right
[Music]
um so here we go on the next
slide um
okay and next
slide so the other thing is when you
receive a response from the HTTP client
then you should you should test the HTTP
status code any status in the 200 range
means success there could be 200 okay
2001 created 2004 no content anything in
a 200 range usually is successful
you can test that with um is sucess is
success status code or if you want to
test for a specific status because you
expect for example 2001 then of course
test for that on the HTTP status code
but is success status code test if it is
in the 200 range and if that is not
successful you want to show an error to
the uh to the user usually with the
status code and the reason
phrase now sometimes times uh people do
have a problem with remembering all the
um uh all the uh HTTP codes there are so
here is
um some reminder for
you you can remind them with
dogs if you want to so I mean HTP status
dogs and they tell you exactly what they
mean I don't think I have to explain
what 304 not modified means this one
here
or not found or whatever and if you are
more into
cats be my guest there is one for cats
too so for everybody some something okay
hey this was of course uh for a little
bit of fun but
okay there we go continue this one
so I just demonstrated you that basic uh
pattern and that is actually what you
see here on the screen as
well and then finally when you have a
successful uh response well you can get
the uh content out of the response
message the response message has a
Content property which is basically HTTP
content object and you can do a read as
and then read it as a uh text or read it
as um a uh a stream object if you have
binary
data now we have a number of
um uh methods on the HTTP client to get
the post to put and the send and all of
them are sending data now basically the
get the post and the put command are
basically rppers around the sent method
if you ever ask yourself why would I use
sent if I have a get or what is the best
option to use should I use the send or
should I use the get well then it may
help to know that the get is just a
wrapper around the scent what he
basically does is taking away some code
from you that you don't have to write so
here in the example you see method one
which is using the uh HTP client. poost
so it writes an HTTP content from the
request body and then post it and the
second method is using the HTP client.
send by creating um a message HTP
request message with the method post set
the request URI write the content and
then send it now if you look at the the
post
method behind the scenes it basically
does the same thing create a request
message and then call the method
send so it's just some sugar coating a
round descent making life a little bit
easier for
you but um when you start seriously
developing with the integrating with uh
web services you most probably end up
with using the send yourself I mean
that's what I find myself uh in most
cases
doing
um now that this is the basic pattern
let's look at HTTP headers
HTTP headers are used for additional
information with a request or response
and we have different header types and
you probably are uh already used to the
term request headers and response
headers but we Al we have also something
called representation headers and
payload headers that's actually the
official naming from uh the official
definition of headers I will come to
that of course explain what is the
difference and what are use them for and
you probably didn't say oh but
representation headers
is um you combine
headers um or you have as a set of
headers on a request or
response some of those headers can have
multiple values uh some of them cannot
have multiple values for example um you
can have an except language uh header
which can have multiple values so I
accept English or and German or whatever
you have as a language available for me
but the content type header can only
have one value because your content type
is just one type it cannot be two types
in your content So based on the header
it is allowed to have one or more values
and that is something that is defined
and actively checked when you set a
header value that is uh you try to add
another value to it it is checked is
this allowed for this header
type um if you want to see um or read
have a good read about headers I have a
link here headers for dummies at least
that help me a little bit uh better
understanding of headers or if something
is not clear I can refer to that uh page
it's actually pretty good uh read about
headers so uh request headers what do
they include they include um for example
I mean these are just examples there
could be more a user agent which uh
could uh or is used
for um indicating what is the HTTP
client actually what what application is
it is it a browser is it another
application what is the version of it
usually used for statistics uh sometimes
also used by a server to uh to know how
should the response look like but in
most cases just for keeping statistics
I'm uh the The Edge or the the Chrome
browser is used the most or um what all
browsers you have so that's it um but
also for versions so uh could for
example server could say sorry um you
are on an older version of a certain
application I cannot help you um the
host header is usually the header that
indicates the UR actually part of the
URL where are you sending this request
to except language and there are more uh
more accept uh headers uh used to uh
give an allowed or preferred format of
response so I um would prefer to have an
uh data in uh English uh or German or
whatever language um and I accept
encoding in gzip or deflate or whatever
authorization is also a header request
um that uh is going on the request of
course and authorization actually is the
wrong word here it's the header name is
authorization but in fact it contains
authentication credentials it does not
authorize you it authenticates you um
it's up to the server to give you
authorization based on your
authentication okay the header is called
Auto
iation it's what it is so these are
examples of request
headers we also have response headers um
usually we see a header with the server
name so is the server an Apache server
or maybe IIs server or well just the
name of the server that gives you the
response um there could be a location
header um usually location header is in
combination with status code 301 or 302
meaning hey I do not have this resource
anymore uh you are redirected to another
location and then the location header
defines where you should go to uh HTP
client is predefined to follow that
location in that case so it makes a new
request to the location we cannot switch
that off in HTP client in.net that would
be possible but not an Al code
um but we also see the location header
for example in um business Central apis
and we call a bound action it could
return a location header where we can
find uh the updated record that was
created with the bound action cookies
could be returned but yeah many uh
servers use that of course um and then
the IDE is that on the next request that
you make you uh also set the same cookie
so you have a kind of a session uh ID uh
that the server knows hey you made a
first request or a second request or I
know who you are it could be an
authentication value uh it could be
something uh that is used for
authorization it could be used for
transactional stuff it's up to the
server how he wants to implement uh the
cookies then we have the uh content
headers and that is actually what is
officially named as representation
headers representation headers are about
the content and they can both be in the
request and in the response of course
because you can send content you receive
content um just the content type header
the content encoding content language so
content type could be um application SL
Json or text/plain or application XML or
um uh PDF data all the mime types you
could have in there um how are they
encoded what's the language that is in
the content um but only part of the
request or the response if it really
contains
data um in most cases what we do from
our code is only set the content type we
do not really care about the content and
coding or language uh usually that is uh
not our concern um and that content type
as I will also demonstrate later is only
available on the HTTP content object if
you try to set this on the HTTP client
directly you will get an error message
not allowed HTTP uh content is the
object that you use to set the content
type header no uh other object except
the content type header that is not
because uh Al implements that is because
the net objects behind uh HTTP client
and the HTP objects are defined in that
way then we have the payload headers
actually also about the content but
that's more about the content length the
actual length um it maybe a range if you
if it's being sent or received in chunks
of um of data uh and some encoding about
the transfer we usually do not care
about about these is all uh calculated
automatically for us uh automatically
added by the HTTP client so we do not
care with uh about the um payload
headers now how do we work with the HTTP
headers we have an HTTP headers object
and we use that to add a name value
pair and the name value pair is used to
uh
create a new HTTP header if it does not
exist or if that header already exists
it tries to add the value to the
existing header so then we basically
create a header with multiple values but
some headers do not support that so in
that case you will get an error message
now that value that is usually a text
but it could be a secret text especially
when you're working with an
authorization header and you want to uh
add a token or uh use a password
combination then you should use a secret
text so it cannot be um at least not
it's not visible while you're debugging
now the point is that in the request
itself it will just be plain text the
request itself is not um secret text uh
you can sniff it you can see it as long
as you you have of course the SSL
certificate that is being used on https
communication never ever um use
HTTP without SSL uh when you are uh
exchanging authorization information
because then anybody else could sniff
the data and uh get access to tokens or
passwords or whatsoever now there is a
little bit strange thing going on with
the HTTP header object when it comes to
secret text we have an HTTP headers do
Keys which give you that name value the
list of all the names which um is both
text and secret text I mean the name
itself is not a secret text it is the
value so it gives you a list of all the
keys but if you try to get the values of
a certain name that is the third option
on the list then you ask for the values
of a specific header and because it
could be multiple you have to um request
for a list of
text if that um was a secret value then
get values is going to give you an error
message in that case you need to use get
secret values but there is
no function that says get me the secret
keys or the keys for the secret values
so the only thing that you need you can
do there is ask for contain secret and
then you know hey is this a secret or or
not little bit more information about
this too much maybe but just saying that
if you sometime want to read the header
object you may run into this and then
hopefully you remember this usually you
do not inspect the header's object
anyway on the request and on the
response it's always text how would uh
Al know
if a certain response header should be a
secret text or a normal text so response
headers are always normal
text how do we add a request headers now
and here's the confusing uh confusion
for many people we can add them on three
different levels we can add them on the
HTTP client we can add them on the
request message and we can add them on
the HTTP content and this is is also
related to if you are
using get and post or you are using the
send command because if you are using
get and post then you are not using HTTP
request message so you're not able to
set headers on the request itself you
can only set them on the client or on
the content in that
case but if you are using the send then
you're also using the HTTP request
message and then you can set them on all
three
levels so how do we set them on the HTTP
client that is the default request
headers uh function on the HTTP client
that returns an HTTP headers object and
the easiest way to use that is just say
HTTP client. default request heads. add
name
value when you do that the name default
request headers already have has it in
it that header will be added to every
single request you do with the same HTTP
client
instance you use that for static values
like a user agent or static credentials
like basic authentication so let's
switch to a small demo about
this um
go in
here so what I'm doing here in this
piece of code I have an HTTP
client and I set default request header
one time and then I do a first one HTTP
client. getet and a second one
httpclient doget uh just actually two
times the same request and then when we
ex uh inspect the uh request you will
see that they both will have the same
user agent so let
me uh find that demo
again
and I'm going to use this one as
my tester here I can actually see what
is coming in let me clear all the events
there we go and default request head us
the first
one filed together
response okay that's
funny why was
that of course usually always works and
now
today trust me it works I mean you
remember that
phrase why is he
oh there's no anything
here okay that's funny let
me quickly see if I can find what is
going on here because if this is not
working then nothing is
working let me quickly
check demo request
headers online 10 yeah okay
maybe I don't have an internet
connection it could be blocked but as
far as I know well let me check maybe
it's you are right on
that that will be the first thing to
check oh could be the case maybe it's as
simple as
that and now you know why it is
important to check is blocked by
environment because then I would
immediately know probably my code let me
check ah my code didn't have it I it was
on
purpose of course it
was okay there we
go it needs to wake up there we are and
here I have two requests coming in let
me uh check the headers here I have a
user agent on the first header business
Central version
24.1 and the second one has the same
header
and all because I set it one time as a
default request header so it is added to
the both of the
requests the next thing is adding it to
uh the request
message
and well only uh when you want want to
do this you need to use the get the post
sorry not you need to use the send and
not to get post or
put
um you can set the HTTP headers request
on sorry the header on the HTTP request
message not directly not in the same way
as you can do on the HTTP client on the
HTTP client you had that function uh get
default request headers and then you
could say do add there is not an HTTP
request message do headers do add
because somebody at Microsoft thought
what might be a good idea to have a get
headers function that returns to http
headers as a bivar variable byar
parameter I mean I don't know why uh it
returns a Boolean if it was successful
or not I never ever come across the
situation that the Boolean is false
anyway
so okay um it would be lovely if
Microsoft would just say hey give uh
we give you an HTP request message do
headers that actually returns headers
otherwise the code is a little bit more
clunky as we will see in the next demo
now headers that you add on the HP
request message will only be included
with that particular
request the next request will have an
empty set of headers only the default
request headers from the HP client will
be added so the HTP client actually
combines the headers from the default
request headers and the headers you set
on the request message they will just
combined to one list of headers now you
use the request headers um with expiring
tokens for example so you don't set them
as a default because yeah they can
expire so every time for every request
you need to see if you need to uh
specify in another token maybe um the
accept headers for this request I accept
uh a certain language or Json or XML
whatsoever but you cannot use it for the
content type header if you do that you
get that misused header name message I'm
sure many of you have seen this one and
then wonder why well the content type
header is not under request you will see
that uh when we talk about the HTTP
content itself so let me show you this
one as
well and that is this piece of
code here I still set that uh default
request
header and then I have a request number
one um I set a method to get I get the
request URL and then I get the headers
and on the headers I set four different
extra HTTP headers for this request I
said my uh accept the said the language
and I have a custom value not customer
oh always make that typo the custom
value one a custom value
to now um on the request number two I
clear the request message and then uh I
add um accept X XML and accept language
but not the custom
headers and that's it so let
me publish this
one and there we
go request message
headers so here's what we get from the
first one in the headers we have my
custom header now look at this one
custom value one and custom value two as
a as one
header you see my custom header is
actually add two values to it so it
comes in as
duplic as a as one header with two
values in it and I have my user agent as
the default request header and of course
my accept language and accept
application Json when I look at the next
request done with the same HTTP client
but with a different request I have
accept text XML language but I do not
have that custom header value
anymore so that is how we can can manage
the headers that are sent with every
request and the headers that are only
sent with a particular
request pretty simple isn't it you just
need to know
how all right so this is about getting
stuff let me
um get to the HTTP
content the HTTP content is is used to
transfer content either in the request
or get it back in the response you can
set the content in three different ways
you use write from a text variable or
write from a secret text and then write
from an instream so it could be an
instream from my temp blob for
example now the content type header that
one will always exist even before you
write any
content with a default value text
plane let's hardcode it simply hardcoded
now the question is why does it exist
because that is something that if you
understand why that actually happens it
makes your life a lot easier the HTTP
content when we look into net then for
those who know net uh not opening it
just telling you the HTTP content object
in net is an abstract object meaning
that that is an object that you cannot
instantiate you cannot create an HTTP
content object the only thing you can do
is create one of the derived types
derived types in net means an HTTP uh
string content or an HTTP stream or an
HTTP different types of HTTP
content if you create an in net an HTTP
string
content it will have a value text plane
on the content type Header by default
now this is what happens behind the
scenes because in AO we do not
instantiate net objects we do not
instantiate those um repper objects that
are actually. net behind the scenes HTTP
content is just net HTTP content with a
wepper layer around it we do not
instantiate objects in Al code we do not
so for that reason the AL code behind it
like the net code behind Al has to
instantiate that object for us but you
cannot instantiate HTTP content so
they're intiating the string content
with text plane as the default header so
as soon as you define HTTP content now
you know that in the background you
actually have an HTTP string
content with header text plane that is
why it happens now as soon as you um
have uh do do I write from text or a
write from Secret text that means that
you're actually creating another string
comp content actually he does that for
you in the background creates a new HTTP
string content object resetting the
header to text plane even if you changed
it before the write
from it will be changed back to text
plane meaning that you
always need to set the content first and
then set the header uh content type not
the other way around because then you
may be in
trouble so first do the right from then
set the content type but hey if we set
the content
type we're actually adding it the value
to the already existing content type
that is not possible because the content
type can only have one
value so you first need to remove it
and then add it again so that's why just
what happens behind the
scenes Let me switch to a
demo some
code
um so here we have the correct order I
do I write from response text then get
headers into a object HTTP content
headers then I remove content type it is
always there if you want to be 100% or
110% safe you do a if uh HP headers do
contains content
type then uh remove the content type I
mean that would be 110% safe but you are
already safe with this piece of code
anyway and then you add it if I for
forget about this this line is going to
give me an error message so let me
quickly show that error message so we
remember that
one H come
on did I
actually that's funny oh sending content
uh of course I'm trying to do the
send yeah
yeah oh I actually did not let me try it
again no probably
H did I not
publish I thought I published
it I probably did something to the code
anyway you will get an error message
that's your
ID again
I I don't don't understand what you
say you think it is demo 5 let me check
otherwise we just
continue oh that's yeah a course I was
just freaking on the wrong demo sorry
for that uh cannot add the value because
content type does not support multiple
values that's actually message thank you
I don't have T-shirts at the moment
hopefully they will come in before the
end you you you really I owe you
t-shirt anyway so this is the message
and the way we solve it is by clicking
on a different demo no on the just
remove that content type header
first okay so now it
works
um the funny thing with this code is
always that I have to think about it I
do have I do a get headers HTP content
headers and then I set on the headers I
do some actions on the headers I'm not
doing a set
headers that's not
required it's like I I get an object out
of HTTP content I do
some stuff on it and then uh I don't
have to push it back into the HTTP
content that is because of net and
reference objects Etc I'm not going into
the det details but it's not needed it
does um not require
it
um okay that was that
one let
me
next something about
performance creating a new HTTP client
instance is not 90% slower comparing to
reusing an HTTP client
instance what do I mean with an HTTP
client instance a variable of type HTTP
client as soon as you define that
variable you run the code um if you have
it as a local variable in a function the
moment you call that function the HTTP
client will be
instantiated and what I did is I just
compared the code with a local
function sorry yeah a a function with
the HP client as a local variable and
then setting the default request
header
versus a global variable with HTTP
client in the same code unit and then
calling a function that only sets the
request
header and the time it took was just
90%
less for working with the global
variable
so does that mean that you always should
use an HB client as a global variable no
that's not what I'm saying what I want
to say because even if it takes it is
90% slower I had to run it about a
10,000 times to even get into something
measurable like 7 Seconds versus uh half
a second or something like
that the point is that that if you are
going to do a 10,000 times an an a call
to an external web service maybe because
you want to singr onize something then
the cost to create HTTP client instense
for every single request is measurable
but at the other hand the request itself
is considerably slower and will probably
um you will probably not get any faster
on and better performance because it's
the request itself that takes um
probably 500 milliseconds or maybe more
to complete so for the performance of
your process it does not make a lot of
difference
however HTTP client instances in net are
meant to be long lived that is how they
are
designed there is actually another
reason and if you are from the net world
you probably uh know about this and
maybe have wondered how does that work
in Al
code the expensive part of the htttp
client is something that is internal in
the HTTP client that is called the HTTP
message Handler you never seen that one
in Al you will not but in net it is
definitely a thing the HTTP message
Handler is handling the active is
actually handling the transport the um
sending the request now the point is
that every HTTP client in um with that
HTP message lender is keeping a
connection pool and the connection pool
is let's say an open port to an outside
server now if we think about net the
problem in net is is that if we
instantiate an HTTP client for every
single request and we do not even think
further then he will open another port
and another port and another port to the
outside web server and that Port will
not be closed when the HTTP client goes
out of memory when the HTP client is
disposed because that HTP message
Handler in the background lives
longer it keeps the port open open in a
connection pool for four
minutes and that is four minutes because
it's defined in the official HTTP
specification or
TCP so because of that definition and
four minutes open port that means if you
run that a 10,000 times in a minute you
end up with 10,000 open ports on the
server now imagine that a couple of
users do that and you suddenly have a 30
or 40,000 open ports at the same
time you see what every one is going at
some point you run out of available
outgoing ports because there are is not
unlimited it's about a
65,000 ports outgoing ports so you run
out of ports and that is known as Port
exhaustion in the net world the h P
client import exhaustion is definitely a
thing and if you Google on that you will
find a lot of information about it so
how does that work in in Al it is
managed for us it is in the net you can
work with the HTTP client Factory HTP
client Factory creates a new HTTP client
for you but pulls or caches the HTP
message Handler with those open
connections so it can be reused every
time and that HTTP client is meant to be
shortlived because it's the message
Handler
itself that actually takes the time to
instantiate that has the connection pool
and Al handles all of that for
us why I'm telling this to you because
if you are comparing net if you are into
the net world if you have maybe read
about it you may Wonder Hey how does
this work in Al do I have this problem
in Al and actually you do not because
the team of uh business Central already
figured it out that their service would
pretty fast run out of EX of of outgoing
ports if they didn't do anything about
it so there was probably a matter of
teaching all Al developers to do it in a
proper way or do it themselves well
luckily they chose to do it and manage
it
themselves so internally there's an HTTP
client Factory and in case you wonder in
case you have um U you know more about
this it they are using a delegating
delegating Handler behind the scenes not
going into details just saying so that
short lift that means
something because does that mean that we
can just instantiate the HTTP client
every time so have it as a local
variable
in our functions I just said even if it
is slower compared to having a global
variable the request itself is probably
taking more time so it's not really
measurable when you make external
requests so what is the better option so
let's look at some best practices
here every instantiated HTTP client
requires in
initialization um with some default
request headers or authorization headers
Etc now it is okay this my
recommendation it is okay to create a
new HTTP client for occasional requests
so requests that just happen every now
and then like you do an HTTP request to
check um I know a license every uh hour
or something like that um but if you
have a loop for example to synchronize
data to send multiple records you should
rather have a code unit with a global
variable for a HTTP client in it and
then call initialize it one time and
then make the request multiple times and
then let the code unit
go you could even put it into a single
instance code unit but then you may run
into another problem because that HTP
client will be sitting there with its
HTTP message Handler and it will not
when has made a connection it knows the
URL it knows the IP address it will
never ever pick up a DNS change unless
the user lcks out and locks in again and
DNS changes oh they happen so if the
server is sitting at a different IP
address suddenly for whatever reason
then hey uh HP client is not picking it
up um and in net you can set a
connection lifetime pulled connection
life after this uh period of time you
need to refresh your DNS St we cannot do
that in Al so how does that look like in
code this
recommendation me go into this one here
this is actually what I usually do I
have an HTTP client in a normal code
unit as a global variable so not a
single instance code unit then I have a
function for for example send s
request and in the function itself which
I actually could also put in the send
request but anyway I have an initialize
function and then in the initialize I do
onetime initialization of the default
request headers and then every other
request that is sent through the same
code unit will have those headers um but
it does not have to instantiate the HTTP
and initialize the HTP client again by
doing so I mean you're not really
gaining a lot of performance for your
requests but at least you put the server
at ease because otherwise the server has
to do the heavy lifting of creating that
HP client every and every time again so
we actually relieving the business
Central server in that case and if we
all want to be good neighbors especially
in the SAS world we should just follow
this best practice so this is how I us
work with the HTTP client again Global
variable multiple functions in
it uh to Center
requests
okay
then I showed you a lot of
code around sending
requests now uh in version 23 the rest
client module was released as a
community
contribution I wrote it and this one is
uh meant for encapsulating the HTTP
client and all the other HTTP objects
you can call web services with just one
line of code and the whole stuff about
is it successful uh is it blocked by
environment all these lines of code are
inside that rest
client so here are some examples uh um
getting text basically press client.
getet and then um on that get we get
back an HTTP content code
unit get content and I can say s
text that's it posting text is as simple
as posting to a URL and then call on the
HTTP content object a create with the
text and applications as Json in this
case for for the content type so we have
don't have to set a content type header
ourselves and we can then do get content
as text or if we want to work with
Json get as
Json returns adjacent token so only
thing I have to do is say as object and
get back adjacent object
directly or post as Json pass in ajason
object we don't even have have to create
HTTP content that will be handled for
you and it returns ajacent token that
could be an array that could be an
object that's up to you you know what's
going on there um and then you get can
cast it into an object again
alternatively what we can also do if we
want to have the text you post it as a
Json with the Json object and then
because we get back a Jason token we can
write it directly to the response text
so
turning it into a textt rather than Json
can store it directly to a field I don't
know
whatever uh another alternative would be
this one post HTP content create as the
J object so here we see HTTP content
create with a text here we see an HTP
content create with a J object you don't
have to think about the content type
because it knows this is an an object so
the cont content type is going to be
application Json
automatically and then get the content
as a Json as an object while you see
post as Json is actually doing that get
content for you returns actually get
content as Json for you we can also have
binary data we can get uh content as
blob and returns a temp blop code unit
or the other way around post it as a
temp blop and and then say hey there's
an PDF that I want to post
there so it makes life a lot
easier so a lot of objects in there we
have the rest client itself it actually
is then the replacement for HTTP client
we HTTP request message and response
message code Unit A content code unit we
have a method enum and we have a client
Handler I will focus on the client
Handler um in a minute and we have also
an authentication interface for basic
for o client credentials and I'm working
on extending that to all o or
types so the rest client is part of the
system
application that also means that if you
are using the rest
client you will get a
question do you allow the system
application to make an request to an
external
server that's maybe not what you wanted
because the system application should
not get Global permission imagine you
have multiple
apps making use of the rest client and
app number one is making external
request and you say yes system
application may make that request then
app number two com comes
in but because the system application
where the rest client is in has already
the permission to make external request
app number two is allowed
automatically that is a little bit of a
horror right you don't want that what is
more Telemetry will not be sent to your
um appin sites because it will be sent
to Microsoft because it's the system
application that sends the request so
that rest client I'm going to
demonstrate this um needs to be a little
bit
smarter so let me go in
here and show you the rest
client you see here extension system
application that is actually what he's
now asking and if I say yes I open it
for any app that is using the rest
client
do not use it in this way actually maybe
I should just remove this
option and not let the system client do
the actual request if you agree tell
me there's one person at
least okay can I get a hand who agrees
that I should remove
this that's not everybody so wait a
second I'm going to demonstrate you how
to solve this and and what you the
pattern that everybody use in their apps
and if you are then still agree I may
suggest to Microsoft remove it it's
probably not going to happen because
it's a a um breaking change then so um
what is the point let's see if that was
actually on the
slide
yeah what you should do is you should
use the HTTP client Handler
HTTP client Handler implements the
interface HTTP client Handler and you
use that one to initialize your rest
client so here on this code this is my
code unit and that code unit has one uh
function in the interface HTTP client
hand has one function interface and it
is sent and it provide you with the HTTP
client the request message that need to
be sent and the response message that
needs to be returned and it only needs
to have two lines of code HTTP client.
send returning the response message and
then pass that response
message into the code
unit this is all you
need but now it is your code that is
performing the HTTP client docent your
code and this makes it so powerful
because now your app will be asked if
want to uh allow uh outgoing uh requests
and tel3 is going to your app and not
Microsoft and what you need to do is on
the rest client initialize it with that
client Handler that's all so you define
that one one time and use it on
initialize so let me do
that do I
have come
on now I have nothing on my
screen oh this is not what I was looking
for
so technician what can I
do
okay I'm
I'm going to do like this come on I can
watch that the big screen over
there and take that one so this single
line here just going
to and uncomment
it and then go
here
whoa and then do it once
again and no comment no ask no question
so let me really verify that is my app
that is doing
this exchanger
management go SL
down delete
it do it again there we
are so this proves that by uh passing in
that client
Handler it's my app that actually makes
the
call so this is something we
should all use
um instead
of um well just using the rest client
out of the box so again the question do
you agree we should force everybody to
use
this not n there's not everybody here
still
okay I discuss that with Microsoft if
that was just a good idea or not
this client Handler also allows you to
test without making the actual call
because you can mock the results so here
is the same HTP client Handler
implementation but now I call it my test
HP client Handler and instead of making
the call doing HP client. send I just
set the status code the response phrase
um the Jon op object that I want to pass
in and say success is
true so I've completely faked the
response and with this way I could say
this is a positive one maybe I want to
have a negative one as well how do you
react how does my code react to a status
404 or to an object that is invalid or
whatever there's a lot easier to test
your um integration with external
services
then actually makinging the request and
then make sure that that external server
is replying in um a correct way in an
incorrect way with an error message with
an invalid object Etc you just fake it
because your test test your code not the
external server right so this message
Handler or client Handler is not only to
get everything into your app it is also
also the way to have proper tests for
your external Services
Integrations all
right do you like this rest
client good thank
you it's it's so lot easier now okay
um there is more I mean I can talk maybe
for half an hour about this rest client
but that's not what I want to do um
final couple of minutes uh I want to
talk about the next piece that I'm
working on and I that is actually
combination of endpoint and o
or um it's under construction and the
idea is that um we can have an endpoint
configuration can also do it completely
from code but an endpoint configuration
in business Central where we set up
everything kind of similar to the
registration in Azure but now the client
side part and and then the only thing we
need to do in the code is to say hey uh
rest client this is the endpoint and it
configures it completely with everything
that you
need let me see if I still have a black
screen yeah I still have a black screen
okay um not really funny this but um
trying to get my way through
it where is my mouse I'm happy to have
big screens there so this is um how it
works from a code
perspective um I have a rest client that
I need to initialize let me go down
um where is it it's here initialize with
an HTTP endpoint code and then what what
I do is I call this one HTP endpoint
doget rest client the bind subscription
around it is to pass in the uh client
Handler that I just demonstrated but
this get rest client that's actually
what you need and when we do that we get
all the
settings that we need so let me
open the
endpoint definition
so here um I'm going to call business
Central from this
endpoint
um this is my base URL and I specify
that I want to use oo
authentication and I tell him that my o
authentication is using Microsoft entra
ID that my o old application is the BC
let
me go into to app
registrations here's my BC
definition it does have a client
ID um it allows multiple organizations
meaning it is multi-tenant could also be
single tenant and in this case is not
having any secrets I'm using a
certificate code and a certificate
code um oh let me just do the drop down
here
F
list is this
one um that was not what I
wanted select from
fullest yeah should show have the card
page
anyway Andra certificates there we are
so this is my certificate I could even
create a certificate from this uh code
so if I go into azure
entra uh ID and I create an app
registration that you can choose between
secret or
certificate for the authentication part
secrets are used for test and
development certificate should be used
for um for production environments but
how do you get that certificate you
don't have to buy it you just um well
this code is actually creating that
certificate you can download it from
here you get the public key the private
key stays in business Central never
leaves business Central because it's
only used to sign the request not to
trans be transferred to Azure and the
public certificate you upload that to
Azure and that's it and you can see that
this one expires on
2099 well that's quite a long time maybe
it's not the best option but Secrets
expire at least every two years
certificates have an expiry date that
you can set and it is safe to have that
10 years or 20 years because it never
ever leaves the application it is not
transferred over the Internet
anyway I'm not going into the code how
to create a certificate that is
different topic actually so I have my um
AB registration here with the client ID
and instead of a secret I'm using a the
CER ific and a redirect URI which is
different from the standard URI that
Microsoft is using different story not
going into that and here on my endpoint
definition I tell him uh which um entra
ID I really want to use and if I want to
use client credentials or authorization
code I stay with client credentials for
here and I tell him the Scopes you
probably remember that one also for your
app registrations in entra client
credentials always require this scope
the sl.
default so how does that work after you
have set it up again if you have done
Azure app registrations you will
recognize all of this so let
me open my test
page and tell him that I want to make
the
request on that BC
Endo let me see do I get something here
no oh it's not even making a request
now oh that's
funny oh might might be blocked it might
be blocked
yeah um
hold on a sec I need maybe I because I
published everything just not really
working as I like
to yeah it might be the blocking issue
here so let me go into extension
management I actually should get an
error message about uh blocking but let
us
check it is
allowed so that cannot be the
issue okay so somehow it worked when I
tested this yesterday but trust me I
would have a list of companies here so
let's not fix that on stage um if you
will be interested you can contact me
um the idea was I crap it should have
worked anyway I'll stop this demo here
and switch back to
my
slide so endpoint configuration oh one
more thing on this because this is all
configured in the client you can
also do it in code completely and you
would have code like this um or old
client application set a client to D set
client secret or a certificate um set a
redirect U add some
Scopes uh initialize your um Grand flow
is it authorization called Grand flow or
client credentials and then initialize
it and then well you can get a rest
client with that so just you can do all
of this from code this part is under
under construction
honestly so you think this this make
sense then also let me
know there was actually the last
slide so 10 minutes left for questions
again I don't see any t-shirts that were
not delivered sorry for
that maybe somebody's bringing them now
but there are no t-shirts no sorry for
that but here you
go sorry Milan yes uh yeah in the
beginning you spoke about the uh
sessions being blocked and yeah we have
seen multiple occasions of that but I've
seen multiple times when I triy to use
the HTTP client on Docker that it
doesn't work uh I don't know why but I
realized just by uh restarting the
docker itly work works again so is that
something you have experienced
it it could be a Docker issue because
Docker and networks uh and blocked by
firewalls maybe um that could be an
issue yeah it depends on how you create
your Docker if you add it to a uh
internal Network or I mean these things
can happen that yeah it's not usual
actually I never run into that what you
were saying I I have had it on multiple
occasions during different times of year
and so on so that could be a tip just
trying reboot Cas you should actually
look into how you create a Docker um
containers I
think y
right oh
a you not do that um my question is with
the addition of the rest client yes is
there any purpose for the HTTP client
still uh what do you mean with purpose
for the HTP client is is there anything
I can't do with the rest client that I
still so I still need to use the H HTTP
client yeah it is using internally HTTP
client and at this at this moment um the
rest client is not supporting the
cookies so that needs to be
added but as far as I know that's the
only part that you cannot use the RIS
client for I see so the I'm sticking
with the rest C for now yeah you can use
the rest C for pretty much everything
there was a question over here
yeah is the rest client uh limited to
cloud or is also on premise on premise
well okay yeah
absolutely do I see more
questions uh so with your last demo on
the uh entra ID apps and stuff so that's
you do plan to make that as an open
contri open source contribution yes
that's idea um authen authentication
types en
extensible yes perfect thank you yeah
absolutely so um and interfaces around
it yeah so it is under construction so
that's my excuse that it doesn't work it
did work yesterday when I checked
everything sorry for that if you stay
around for a few more minutes try fix it
right after to make sure yeah if
somebody wants to see it but um yeah
it's under construction so that's my
excuse any other
questions uh I actually had a question
about that poor Postman new show you
used for tests is there any plan to make
it as an app because there's something
that many non-technical people asked for
test and so on and is it possible to
make it similar to the real Postman
somehow I is why I named it my poor
Postman it is actually just an um uh a
viewer
controller in where I can show Json and
XML and whatever um right into the
client so yeah a custom control D that
one with the code lines the and it is it
is the a editor um and yeah I can um
make that available of course it's quite
powerful
but I I think I should create um a small
uh oh
let go maybe I should make a small blog
post about that uh separately and then
uh give um the source code away on uh my
giab I put it on my
list is it possible to add loging to the
rest client can I hook into the
interface somewhere that I want well
looking uh yes because that client
Handler is every giving you everything
yeah so you could use that for loging if
you want to um in the first edition that
I created I had a logger actually but
then somebody told me that might not be
a good idea because of uh gdpr rules or
um uh yeah you could expose data that
you want don't want to expose so you
have Telemetry of course with have
outgoing request everything is there
reducted for um private
information but for debuging reasons I
could see this happening um so yeah
definitely possible okay
more
questions no
more well in that case um I have one
final
slide thank you
