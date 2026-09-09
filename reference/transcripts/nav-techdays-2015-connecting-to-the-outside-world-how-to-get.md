# NAV TechDays 2015: Connecting to the outside world How to get the best out of web services

- **Source:** https://www.youtube.com/watch?v=FLFc_U3oQlA
- **Video ID:** FLFc_U3oQlA
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 89m36s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Marty!
You've got TO COME BACK WITH ME.
WHERE?
BACK TO THE FUTURE.
WAIT A MINUTE. WHAT ARE YOU DOING, DOC?
I NEED FUEL.
Go ahead. Quick, get in the car.
No, no, no, no, Doc. I just got here,
okay? Jennifer's here. We're going to
take the new truck for a spin.
Well, bring her along.
This concerns her, too.
Wait a minute, Doc. What What are you
talking about? What happens to us in the
future? Do we become or
something?
No, no, no, no, no, Marty. Both you and
Jennifer turn out fine. It's your kids,
Marty. Something has got to be done
about your kids.
Hey, Doc, we better back up. We don't
have enough road to get up to 88.
Roads?
Well, where we're going, we don't need
roads.
Good morning, everyone.
I thought we were in a movie theater, so
why not watch a movie and why not watch
a really old classic? Everyone is old
enough as me as watched this movie when
they were a boy, so
always good to do to do something like
that.
Uh how do you like NVT days this year?
Come on.
Very good.
So, where we're going, we don't need
soap.
Um this is a session about web services.
Uh we're going to talk about web
services. And sometimes uh I I know web
services feels a little bit like 1985.
But um a lot has happened since then.
So, it is now uh 2015. So, uh we're
going to talk about uh what has happened
with web services since it was
introduced in NAV uh a couple of years
ago.
Ah.
I was switching.
Yes.
And it was uh back in 2001 uh the tech
at in Barcelona.
Um I was there.
And this is Don Box sitting in a bathtub
um introducing soap.
As you can see, he is totally into the
soap. And that was his message.
Uh he was doing this for an audience of
5,000 people.
Telling that DCOM uh has vanished away
and that soap was coming in.
Well, how many of you do know what DCOM
is?
A couple.
Not many.
Well, this guy was telling
here we have soap
in his bathtub
but also with XML calling
other systems using XML streams.
It was very nice, but
we are not going to do soap today. We're
not going to do this kind of
performance. There's no bathtub here.
We're not sitting in a bathtub. I'm
sorry for that. You can't handle that.
So, we tried to get a bathtub here, but
we couldn't get it to work.
So, I would like to introduce Arjan.
Arjan is a fellow MVP from from Holland.
Uh he started with as a as a global
developer.
Uh been doing NAV since 2002.
Um he's the co-founder of the Experior
Group. He is a he's a blogger and he is
uh my partner in crime. He's doing all
the heavy lifting and all the demos uh
today for you.
And if I don't get it, it is Mark.
Because if it fails, it is his failure,
of course.
Blame me.
Everyone blames me.
You should blame him.
Uh so this is Mark.
You all should know him because he wrote
some books and he is a an MVP for
uh couple of years now.
Um next year 10 years celebration or
this year 10? Yeah, 10 years celebration
now.
So um
maybe you was the first MVP for Dynamics
NAV, I guess.
No, no, no, no. That was Luke and and uh
Eric.
A few MVPs here in front. So if we don't
know it, they know.
Um Marcus in the Netherlands as well as
me like me and we have worked together
on web services couple of years ago with
a customer.
Oh, yeah.
And we sit
next to each other and our desk was
maybe sitting sitting like this.
And we sit like this.
The entire day.
web services. So makes sense to be here
to talk about web services.
So let's have a look at the um
agenda for uh today. First we're going
to give you a status update on web
services, what has happened with web
services
uh in the last couple of years. We're
going to talk about different types of
web services.
Then uh Arjan is going to do all of his
uh cool demos, uh how to consume web
services in NAV uh based on rest and uh
managed APIs. And then hopefully at the
end we'll have some uh time for Q&A.
Arjan has been programming on the demos.
Uh
I think he still is.
No, no. I finished. We we finished.
Didn't work.
So let's start with the uh with the
status update.
So, where are we today? We have about a
decade of of web services. So, what is
the the status of the web services
today?
Uh why are we using web services? Where
does it come from?
Uh when I started to do NAV and
Navision, it was a very closed system.
Uh the only way to get data in and out
was with flat files. Um then for a short
while, we had the option of doing ODBC.
We could get data into the database
directly.
Uh we can do that with with SQL Server
as well. Uh but we all know that if we
write to the database base directly,
we're not executing any business logic.
We're not validating anything. So,
that's not really a good practice.
Um then from a file perspective, we went
from
flat files to XML.
Uh XML introduced metadata inside files,
allowing us to do file descriptions
inside the files. And web services was
supporting the XML. It was basically if
you send a SOAP web service, you're
sending
an XML file
over the web service.
Then recently, we have JSON. And JSON is
also a new file
that we introduced and that we use with
web services. And it's changing the way
that we do web services as well. And I
think most of the things that Darin is
going to show today is is based on JSON.
So, if we look at integration and if we
look at the way that
we do things today,
we've all been working with web services
for the last couple of years. And web
services really changed the way that we
think about software development. Um
It's basically like NAV solutions on
steroids. Um if there is a web service
out there,
why would you reinvent the wheel?
Connect connecting to web services
is very easy. For example,
um
why would you write C L code to convert
from Celsius to Fahrenheit if there is a
web service that does that for you?
So, web services are also becoming more
and more standardized
and common to use and they're also
better known by NAV developers.
I still remember that 10 years ago
um
we had a web call with the MVPs about
web services and I had to actually use
Google and Wikipedia to find out what
web services were. So, we've come come a
long way since then.
When was that?
Sorry?
When was that?
That was when Navision 5 was still
supposed to be the role tailor client.
Okay, that was before we we said okay.
ago. That was a long time ago. Yes.
Um
So, when web services were introduced,
um
Microsoft paid a lot of attention to
exposing pages as web services. Every
page was potentially a web service. I
think many partners discovered that just
exposing page 42 as a web service is not
really a good thing. It doesn't make
life very easy for for
developers. You get a lot of garbage in
your web service. So, we've all learned
a lot about best practices on how to
expose web services.
Um I think if you expose an XML port or
a query, you get a much cleaner web
service than exposing a page as a soap
web service.
Um NAV out of the box
when we got web services for the first
time, it exposes soap with XML.
Um I think there is really a trend the
rest of the world moving to to rest and
JSON and today we're going to talk about
how that reflects to NAV.
How does rest work with NAV and what
does OData do with with rest as well.
Um
So, let's uh dive into the different
types of web services. Uh what do we
have today? Uh and how does it reflect
to NAV as well?
Um I like to think of of web services
like this uh triangle. Uh the basic
foundation of web services is SOAP. Uh
there are still a lot of legacy uh web
services out there that work on SOAP.
Um but I think we can see that um
people are moving to rest. Rest is
simplified. It's easier to work with
rest services than it is it's to work
with uh with with with SOAP. And OData
is basically a standardization for uh
rest. And on top of that, we have XML
and JSON
um and and how that works with with web
services.
Uh so, SOAP is the way with that we
traditionally were working with uh with
web services. SOAP stands for simple
object
access protocol. Uh it's a generic
object model. It's really flexible.
Uh you can put a lot of methods and a
lot of files into one WSDL. Uh one web
service can actually do a lot of things,
but it can also become uh very complex.
It's uh it's supported by NAV. If we
think about web services in NAV, the
first thing that we think of is SOAP
because that was introduced by Microsoft
um when we got web services for the
first time.
Um if you have a SOAP web service, you
have a WSDL that describes the objects
um and that you can use to look at the
web service and see what it uh what it
does.
Um
If you use rest rest web services, rest
is standardized. If you if you go to
Wikipedia and you look at the
description for uh rest, then Wikipedia
says that
um
rest is where design patterns go into uh
web services. Um I like that. I'm a big
fan of design patterns, you will know
that. Um, I'm not quite sure if I
completely agree with that. Uh, because
with a REST web service, you can also
make a big mess if you want. Um, it's
actually, uh, also a lot more flexible
because, uh, wherein, uh, SOAP, you have
the object model in the WSDL describing
exactly what you're doing. REST is much
more flexible. You're just sending files
back and forth. Um, and you have to have
a description about the web service to
see, uh, what it can do. Uh, REST is
based on standard HTTP protocol. Uh, you
have get, post, uh, put, and delete
methods.
Um, and the standard, HTTP methods
basically define what you do. And with
the SOAP web service, you have to create
your own methods. Uh, SOAP is just using
the post post HTTP protocol. And, uh,
you can basically do whatever you want
inside your, uh, your WSDL. You can
have, uh,
a hundred methods in one uh, web service
if if you want.
Um, REST is not something that we
typically think of when we have NAV, uh,
but, uh, OData is based on REST. It's a
standardized version of REST. And right
now, we have queries and pages that we
can expose as OData, and that's actually
a REST web service.
Um, OData is based on REST. It's, uh, a
Microsoft attempt or a Microsoft project
to standardize, uh, REST. Uh, they
started with OData in 2007.
So, you have to realize that, uh, people
were already moving to OData when we got
NAV with web services in 2009. So, we
actually got something that was already
old.
Um,
OData is very powerful because it
includes a query language. Uh, I think
we all know that if you go to Amazon or
another web shop, uh, your, uh, URL is
full of these question marks. Uh, these
question marks are actually a query
language that you can say, I expose the
customer page and I do question mark
where number is, uh, 10,000 and then you
get one of our favorite Cronus, uh,
customers. So, OData is very powerful
because it it has this query language.
Uh, so that makes it a lot more
flexible. It is supported by NAV, both
read and write. Um, and, uh, with OData,
uh, the HTTP protocol is also, uh,
extended with the patch command. And the
patch command allows caching. And that's
actually what, uh, BI, Power BI is
using, uh, for, uh, for performance as
well. Power BI is completely based on,
uh, on OData web services with, uh, with
JSON.
So, XML and JSON, how do they, uh,
reflect? I think we all know, uh, good
old XML. Uh, we have a lot of metadata.
We have more metadata than data.
Um, if you go to websites that describe,
uh, XML versus JSON, then you have a
couple of websites that are really huge
fans of JSON and say everything should
be JSON. It's faster and more
intelligent and
that's actually not true. Um, people say
that JSON is faster because it contains
less data. Um, well, XML, you can just
leave out the second tag and then it's
exactly the same size. And if we send
back and forth, uh, XML or JSON on the
internet, it's always compressed. And if
you compress data, uh, the metadata will
be compressed most. So, from a
performance perspective, it doesn't
really make a lot of difference if you
do XML or JSON. It's a different
notation. JSON is actually something
that the makes the most sense in
JavaScript because JavaScript allows
creating objects from JSON like, uh,
Wiebe talked about yesterday in his
session.
So, let's go to, uh, Arend Jan. You've
heard me talk about the theory enough.
Uh, let's do some really cool stuff.
This is NAV TechDays. So, Arend Jan is
going to, uh, show you how easy it is
and how powerful
uh, REST web services are in combination
with an AV.
So, let's uh
try to see if this switch thing is
working.
This one.
Yep. Now, you're
the same screen. How smart is that?
You want the clicker?
Can we switch? Yes.
Yeah, we can switch this to clicker.
It's a more manual switch, but we can do
it.
Yeah.
This is playing with the demo gods,
guys. This is This is really really
really dangerous.
Never do this at home.
You can try if you have this one.
So, um
well, let's see if this going to work.
Yes.
It does.
Wonderful technique.
So, SOAP versus REST.
So, you got a an introduction from Mark
about SOAP. So, this is a a recap. Um
REST and SOAP web services
um there is a difference in between.
They both are web services, but uh the
difference between them is
um not that you should um
always choose for a REST web service
always go for a SOAP web service.
Um
it is a different task that I do.
For the SOAP web service,
it is like calling another system a
method in another system. Like
while REST is more or less like exposing
data. It is more like a resource.
So, that is a different task between
REST and SOAP.
Um with REST, you have predefined
commands like get, post, put, and
delete. While SOAP exposes an operation,
and it is the SOAP API that uh defines
which operations uh it
exposes. So, with SOAP you use HTTP POST
or you can even use SMTP or message
queue to send SOAP messages.
The REST web services is a
point-to-point communication over HTTP.
SOAP is more a loosely coupled
distributed messaging. But, I'm not
going to do explain exactly what that
means, but it is loosely coupled.
Imagine that you have SMTP
as an asynchronous
call, of course.
I never used it, but it is possible to
have SOAP over SMTP, believe me.
REST is stateless communication.
REST means
you just issue command, get data,
and after you get the data,
the server at the other side is
forgetting about you. It's not
uh
saving any session, normally.
Well, SOAP
is can be stateless, but also can be
stateful. You can send several SOAP
commands
while the server in the back is
remembering you the next time that you
send a SOAP message.
With SOAP, it's only XML.
SOAP only accepts XML, an XML envelope,
an XML
message in it, etc.
With REST, you have the JSON that XML
and text but Mark already explained.
And
what I have seen from between these two
is that
using REST web services is far more easy
than using SOAP web services.
Um and today, the most of the web
services out there in outside world are
REST. I saw a
investigation uh
How do you say that? A list of web
services that was,
um, published maybe 2012
and they, uh, made a comparison with,
um,
maybe 2010, 2008.
And the number of web services,
uh, using REST and SOAP, or using REST
and and JSON, etc., was growing, was
increasing to maybe 75%
and maybe it may
today it's even more.
So,
how are we going to call them?
Well,
if you want to call
I'm I'm talking about calling them from
C A L code, of course.
From Dynamics NAV, directly from a code
unit. If you want to call REST SOAP
service without any external component,
well, that is possible.
You're going to do all the message
message plumbing yourself.
You call the web service with a .NET
component, a HTTP web request. You
handle the web response
and there's no strong typing. So, you
get an XML message, you have to dig into
the XML or you get a JSON file back as a
long string and you have to pull out all
the data in it.
If you look in at code units at 1294,
97, 99 in,
uh, NAV 2016, you see a lot of code that
is working in this way.
If you
want to use external components, it's
getting easy.
For REST,
you can have, uh, with JSON, you can
have strong type objects with Visual
Studio, which means that you can
transfer, convert the JSON message that
you get back as a long string into a
strong type object, into an object that
you can work with like, uh, my
response.values,
my response my value of the response
value.name. Whatever.
That is what I mean with a strong type
object. And you can create I can use
Visual Studio to create these strong
type objects based on the JSON response.
And I'm going to demonstrate that of
course.
You can use the HTTP web request, HTTP
web response, but what is a better way
is to use HTTP client and HTTP response
message.
And I will go into that in the next
slide.
If you will want to use SOAP, you can
create a proxy DLL with Visual Studio.
You then you have automatically strong
typing.
You still need to do some plumbing with
the .NET binding and endpoint
components.
Now in the demos
that I prepared
I really tried to find a SOAP web
services that is useful.
And I couldn't find any.
So the only demos that I have for you
today is based on REST web services.
I have a couple of them.
Five, six demos.
Um
I have to be honest, four demos are on
REST web services, two are on SOAP web
services actually.
But you are not seeing that it is SOAP.
So service calling is made easy. You see
the cartoon.
Well
yesterday it was Wednesday. So yesterday
maybe
the lower picture would work.
Um but there's a difference between
between REST and SOAP. So the command
from REST is just cat me coffee.
That's it.
SOAP is
much larger request.
Telling very polite that you are asking
something that is a request for coffee
request
etc.
So, first HTTP client
Here you see
code
and this code snippet
is all you need
to call any REST web service.
Only this code.
So, if you look at code unit 1294 97
whatever
and you see this lines of code. Forget
about it. Don't use them.
Go with this code.
The HTTP client is available from .NET
framework I think four or 4.5 I'm not
sure, but it is available in the .NET
framework where Dynamics NAV 2015 and
2016 is based on.
It supports the get, post, put, and
delete commands.
Um and it is designed as an easy-to-use
alternative for the HTTP web request.
The HTTP web request is a .NET component
that is used by NAV 2016 in these code
units for sending out data to the OCR
service etc.
So, oh just here .NET framework 4.5.
Well 4.5 that is starting with 4.5 as a
D read as a easy-to-use component for
HTTP web request. Um
all the demos that I'm doing today is
using this snippet of code.
Nothing more.
The HTTP client
is working asynchronous.
That means
um it has a method that is not
uh possible to use that in C L code.
But putting dot result at the end of it
makes the call synchronous.
So, you always get a response message in
this way. You see that NCL success
status code which means basically it's a
checking for an HTTP 200
return code. So that the status code
the status is 200 means successful.
Any other
code like 301, 400, whatever will fail
in this
stage. So
maybe this could be a try function.
And then the result is just a string.
Or an object or whatever because it can
be
an image. The result can be
a binary data, whatever.
And I'm going to show you both in the
demonstrations.
The next one is the strong typing.
So then you have that big JSON response.
And I will going to dig into the
response trying to found out all the
values.
I know there is a way to do this
generic in a generic way finding out
what is in the JSON
and yes if you have a very short very
easy structured JSON you can go with
that.
But if you have a more complex JSON
response
it is very easy to use Visual Studio to
create a strong type class for it.
Using paste special paste JSON as class.
It will create a class for you.
You just have to compile it.
Throw it into your add-ins folder.
And then you can use the JSON converter.
The Newton soft JSON DLL
must be in your add-ins folder only
design time.
That's because of the
compiler looking for that
that DLL.
but run time it is already available for
you in the service folder in the yes in
the service folder itself.
So.
Um.
I'm also going to demonstrate this one
I'm going to demonstrate it right now.
How this is working.
So let me see if I can switch the
screen.
This.
Is an API
rest API.
Can you read it? I guess you can read it
too small.
This is a rest API to find out about the
weather.
And this is the result.
Only thing we need to do is.
We copy it.
Start Visual Studio.
Create a new.
Class library.
I call it
the the enough weather.
Remove this class.
Say edit.
Paste special JSON as class. And there
we go.
That's all.
Build solution.
Succeeded.
Go to the folder.
In debug and here I have my DLL.
Throw this DLL into your into your
add-ins folder.
But you can you guys probably already
did that
for the demo, of course.
So,
I'm going to show you that it is there.
Here I have my
Open Weather Map DLL.
And
this one is just
working right like call the REST web
service
on this
URL.
This is the command, weather.
I give it an ID, which is Antwerp.
I got an API ID because
I signed up for an account.
I get a result.
Based on the HTTP response message, I
can say, "Give me the content. Read it
as a string."
Then, this result
is deserialized by using JSON convert.
The result
and I want to deserialize it into this
object.
And then,
the weather is just the weather root
object {dot} weather {dot} get value
this cuz it is an array.
So, let's see
what the weather is today.
It says broken clouds.
This is just live
getting the data out from
a web service.
This
call REST web service
is basically
this one
what you saw before
on the slide. This this code. No more,
no less.
If you look at code unit
HTTP web request management
you have this lot of code.
A lot of plumbing in there.
So,
we had
HTTP client code
creating strong type classes with Visual
Studio.
And then the next
um
possibility is managed APIs.
A couple of web services out there are
complex, very complex.
Complex web services
can be used with SOAP, can probably be
used with REST web services, but there
are companies who are creating a managed
API. And a managed API hides the
complexity for you.
So, they provide a couple of DLLs, a
couple of classes that you just can call
from straight from your CAL code,
straight from C# code, whatever.
And it hides all the complexity, it
hides all the calling of the SOAP or
maybe REST web services for you.
It is as if
just exactly the same as if it was
an other system just sitting next to you
on your own computer.
Your client code only needs to use that
API, that downloaded DLL.
So, all web service calls are done
already by a DLL that you can download.
It is extremely useful with complex web
services, and I have two demos today to
show you how easy that is.
So,
I want to show you a couple of demos.
And why
a couple of demos? This is
to give you an idea what web services
are available outside
to
prevent you
from reinventing the wheel.
Because web services are there at your
service.
They are servicing you with
operations, with tasks that maybe are
hard for you to complete because they
know exactly what's going on behind the
scenes
and you only have to call them.
So, very easy.
Verify email address. You might think
that you can do this yourself.
And of course,
you can validate if an email address is
valid formed.
So, does it contain a domain name? Does
it contain the ad sign ad sign etc.
But what if you want to know if an
well-formed email address is really
valid, if there is really an inbox
behind it?
There's only one way to know that.
To send an email to that email address
and see what happens.
And maybe
you get a response that it does not
exist. But what if you don't get a
response?
Does that mean that the inbox is
existing?
Or does it mean that the email server at
the other side is just throwing it away?
You won't know.
This web service is checking it for you.
This web service is checking the
mail server
if the mail server exists,
if the mail server
accepts
mail messages sent to an email address.
And it is a very easy web service to
use.
And I'm going to demonstrate this in
code, of course.
So, let me first
demonstrate it.
I'm going to
customer.
This is the customer card.
And I change
the email address.
Communication.
Email address.
Whatever.
It says the mail address syntax check
passed. The mail address domain part is
empty.
Oh, wait.
I mistyped probably something.
Then
I say domain.
Now it say the mail address is not a
role address. Domain part is not an IP
address. Domain part is not fully
qualified. Whatever. A couple of
messages. It is not okay.
So, now I have a well-formed email
address.
Now it says
that an MX record for the domain has
been found, but the SMTP address
validation result failed.
So, this means
and I did I did not
grab the message and
form it well for you, because I guess
you can read for a couple of years right
now. So,
this message is now telling us that the
email address does not exist at email
server.
So,
let me type in
a valid email address.
No message anymore. Just accept it.
So, how does this work behind the
scenes?
Go down to the
code units.
Verify email address.
I have a couple of event subscribers
here.
I just sent it 16 of course, so
I didn't want to change code unit 18 for
table 18 etc.
Here is the code.
I call a REST web service on this
address.
This is the
API {slash} verify. This is the command.
I give it a parameter.
I give it an API key. The API key that I
got from this uh from this guys. It is
an evaluation there, so you can copy it,
but
uh
you should go and get your own key, of
course.
I get a result.
Then I have an API result object.
And in this API result object, which I
converted with using the JSON convert,
um
if the status
isn't 200, 207, 215. How do I know that?
Well, this because of the um
documentation that is behind.
On
this
site,
you get all the information.
There's an online API.
How does it work?
And
here it says
you have a couple of API result codes.
207, the mail address is valid.
207,
215, whatever.
So, a web service
with a site that describes how it works.
Even with some
um example code.
So, I look carefully at this example
so that I could know
how to handle the result.
Which resulted
in this simple lines of code.
Verifying email address.
I'm not doing myself checking an MX
server. I'm not going to verify that if
the email address is valid, whatever.
Just call this web service.
Easy, isn't it?
Next demonstration.
Barcodes.
Now, some
people may respond, "Barcoding? I don't
need a web service for that. I can use a
font."
That's true if you print it with a
report. But what if you want to have
your barcode as an image?
So that you can scan it on a screen or
so that you can set it on a website?
On a on a on a web shop, for example.
Well, this barcodes um
web service gives you just an image.
So, this is a web service that is not
returning a JSON.
It is returning an image.
So, let me show the website.
We enter
a code.
We say, "Give me this."
And here we have a barcode.
That's it.
Include text, not include text.
Well, that didn't work.
I I think it's
an error on their website.
We can give it a different height.
Whatever.
And there is a web service behind this.
Well, not really a web service. It's
just an URL.
A URL
that is
{slash} barcode
{slash} C39
for the type of code of barcode
mycode
{dot} png
and some
parameters like width, height, and is
text drawn.
I'm going to demonstrate this one as
well.
I go to an item.
And I just took
the item number to create a barcode.
The barcode type
C39 and there we go.
Include text.
We have the text behind it.
We want a different one?
No problem.
That's quite simple.
How was this done in code?
I hide the event subscribers again.
This is for the change of the code. I I
have an option file of an option field.
And well, I want to
just have an event subscriber on it. So,
no code behind.
Um the the fields.
And then here I have my generate
barcode.
I must know my type based on the option
field.
It's just C39
etc.
Then I call the REST web service.
Again, on this address.
This is the command barcode {slash} item
number. Oh, this is the type/item
number.
I give it a command get because I just
want to get something.
And then the result
is an image stream.
It's just a stream.
And I put this into a barcode which is a
blob field on the item table.
That's it.
It's that easy.
And now you can print this on paper
on a
page or whatever.
So, very simple,
easy to use.
If you use, of course,
again,
this code
which is behind.
It's the only code you need to call a
REST web service, again.
Next demonstration.
SMS.
Bulk SMS.
It's one of the sponsors of NAV Tech
Days.
I don't know what they are sponsoring,
but I they are one of the sponsors.
Bulk SMS
is a web service that you
can use to send
You can send SMS to
a mobile.
So, imagine what
makes it uh possible.
If you have, uh let's say, an SMS code
an SMS text that you send to a customer,
uh hey, your package is being shipped.
Your order is being shipped right now.
Or you send an SMS to some guy in a
warehouse, you should pick this order or
whatever.
Or maybe you can send an SMS to the CEO
telling him that that uh
whatever the the the the turnover there
this new order that is um making
uh a lot of profit.
You can do a lot of things with bulk
SMS.
Well,
bulk SMS, let's go to the website.
It's asking you to sign up.
I signed up for an evaluation
account. Gives me 1,000 per day.
Um
And there's an API behind.
And there's a very easy API.
Well, not that easy as the other ones.
And the reason is that this API is not
based on the get command, but on a post
command.
Because you have to send data to it, a
large message probably.
Together with an
your API key, together with your
the the phone number that you want to
send the text message to.
So,
let's first demonstrate how this works.
I have a bulk SMS setup.
A username and a password for my
account.
By the way,
this one
is using
a password key,
which is a good.
If you ever have to store passwords in
F2016,
you should do it in this way.
Set password,
and then use the service password table
to save the password.
Because this one will encrypt your
password.
So, save the password as encrypted in
your database.
It is a pattern.
A very small one. You can use it
to have your password saved in database
encrypted.
So, go back.
Oh, come on.
Close this one.
Send an SMS message.
Now, I'm going to
Let's see if I can get my
SMS over here.
Come on.
Freezing.
Ah, there we go.
Yes.
So, this is my phone.
I'm typing in
a number.
Send SMS.
And hopefully,
well, there it is.
It This is really my phone
receiving this message.
So, let's go to the code.
So, now you all have my
phone number. Okay.
Don't SMS me right now.
Looking into the send SMS code,
there are a couple of things going on
here.
I have to send some data.
And
if you look at the SMS API, I'm I'm not
going to open it here, but
it is done a little bit different
from the documentation.
The reason is that
if I followed the documentation of Bulk
SMS literally,
I had a problem with NAV 2016. The .NET
interoperability did not allow me to
follow all the rules that Bulk SMS has
in his API.
But basically,
posting
to a REST web service is exactly the
same as posting an HTML form.
Posting an HTML form means you have that
HTML form, type in some data in some
fields, press post, press okay, press
whatever, login, whatever button there
is, and then behind the scenes there's
an HTTP post.
HTTP posting form data.
And this is exactly what I did here. I
composed exactly the same data that
would
go in if you use HTTP post on forms, on
an HTML form.
And
this one is telling
the data that it is your form URL
encoded.
So, now I use post
together with the string content.
Well, and then I get the response
message.
What can you do with SMS further than
only sending an SMS out to somebody
telling that his server that his order
is being shipped?
I just want to demonstrate another
possibility.
I go to user setup.
And I allow use two-factor
authentication.
Say okay.
Close Dynamics NAV.
Opening
the SMS here.
Now I start Dynamics NAV.
And here says, "Enter the code you
received by SMS."
You saw what coming in here.
So I just type in the code.
That is here and to demonstrate that
this is really working,
put an X behind it, say okay.
Not allowing me.
I have to type in
exactly
this code. It was generated and sent by
SMS, waiting for me
to enter this.
So here you will have your two-factor
authentication in Dynamics NAV 2016
using Bulk SMS.
What are you waiting for?
Okay.
Two demos left.
The next one,
DocuSign.
I'm not sure who of you who know what
DocuSign is.
A few.
DocuSign is a service that let you
digitally sign a document.
You can send a PDF file
to the DocuSign service
and telling the DocuSign service that
somebody
needs to sign this.
Then the other person will get an email.
That email will lead him to the PDF
giving him the possibility to review the
PDF
and then digitally sign which literally
means that the gets that that PDF gets a
kind of of signing a of writing
on top of the PDF.
And then you get back that signed PDF
and that means that it is well kind of
legal.
So DocuSign could be used
to let customers
for example um sign an order
confirmation.
And this is what I'm going to show you
today.
I will send out an order confirmation to
DocuSign telling that another customer
the customer needs to sign the order
confirmation before I'm going to release
the order.
So
let's first open the mailbox
where the DocuSign message is come
coming in.
So that you can see that I'm nothing
faking here.
No emails in this mailbox.
There will flow in a new email in a
minute.
I go
to my sales orders.
I set up customer 30,000 with the email
address the correct email address.
And I say email confirmation.
And just a small thing here send with
DocuSign. I did not
uh put together a button send with
DocuSign whatever. I just pick up the
PDF.
I say send to DocuSign.
It is sending.
And now hopefully
Well, here it already it is.
I got an email.
Please sign sales order.
Review document sends me to
the DocuSign site.
I have to sign that I I agree to use
electronic records and signatures.
So, I now I am the customer.
Here is the PDF
coming from
Dynamics NAV.
I can sign here.
I can even select a style.
I can type in my complete name.
There it is.
And I say here change style.
So,
if there is a different writing that I
like,
I can choose it.
So, let's pick one.
This does not completely match my
writing, but okay.
I say adopt and sign.
Here you see it.
I press finish.
And then the customer gets the question,
"Do you also want to use this?" I say,
"No, thanks."
And now I get an email. The customer
gets an email
that with the sale
the signed sales order. So, for his
records so that he can save the the
signed part.
And also the sender gets an email with
the the signed document.
And as you can imagine, there is also
the possibility to get it directly into
Dynamics NAV saying that this one was
signed, saving the file in in a blob,
etc.
I did not make it that far.
It's just to get you
on the idea that these types are
possible. So, how is this done?
Here is the code.
Nothing to do with REST web services. As
you can imagine,
this is a lot more complex.
So, what DocuSign did is they created a
DLL.
They created a managed API.
You have to get that DLL. The DLL is
available on NuGet.
Who knows NuGet?
Ah.
It's more than
uh
the previous question.
So,
I just want to show you how to get this
file on my system.
Um
if you go to this page,
then you see here
to install the DocuSign.net client, run
the following command in the package
manager console. So, what the heck is
the package package manager console?
Well, something in Visual Studio.
Because they do not think about Dynamics
NAV, of course. They only know Visual
Studio and other development
environments. Um but this is something
that you can run in Visual Studio.
Then you get the download, the DLL.
And then you can copy that DLL to the
add-ins folder and for Dynamics NAV. No
other things to do in Visual Studio.
We're not even to compile something in
Visual Studio, whatever. I just create
an empty project
because I have to um
to have I have a
an empty project that I Visual Studio
don't need it before it can download a
package. So, I just have a console
application and I call this one temp
DocuSign.
Okay, oh well, I used it one already
before. DocuSign too.
Now I need to open the package
manager console. It is in a view
all the windows
package manager console.
I paste this command.
It's coming from here.
Press enter.
And I will download the DLL.
I will go to the folder
of the project.
I have a packages folder.
And here's my DLL.
And I just copy this DLL to my services
add-in.
Well, it's already here. DocuSign this
DLL
in
program files services
uh Dynamics NAV 90 service add-ins etc.
So then I can start writing my code.
Well, I'm not walking you through all
the code here.
But it's basically you're um
telling the web service who you are.
Your username, your password, your
integrator key.
I have a demonstration account. Um
which means that you can send any
numbers uh of document, any number of
documents, but there will be some red
text on top of it that this is a
developer account with a demo key.
Um
don't copy the key because you have my
don't have my password.
You create an envelope.
And then you create a tab. This
this tab is to position
on the PDF
where the customer must sign. So here
with this a code you can position
somewhere on the page
where the the customer
will place his sign.
Then
I have a signer.
This which is the recipient email,
recipient name.
Well, that is added to the envelope.
Then
I give it the status sent. Before I send
it, I give it the status sent. Well, I
don't get that, but you can also say
created, which basically means um that
you can
um
create it and then go to the website of
DocuSign and then modify it further.
And then I get that PDF file that comes
in
that was created by printing the PDF
printing the order confirmation and I
send it with envelope.create.
And that's it.
How did I get that PDF? Well, just by
going to
document mailing.
Here the you have that email file
email file from sales header.
And here I have that confirmation sent
with DocuSign, you saw before.
And then I call this file this function
DocuSign file with the attachment file
path, etc. and some more information
about the customer itself.
Um
And here I compile some information
about that PDF file, but in the end it
is calling the request sign with a send
tool
uh email address and name, the file path
from the created PDF file on the server
and the file name, and that's it.
This integration
in this code unit
that you see here
was created
just before my session at
Directions in Mannheim.
It was created in just an hour.
It's not because I'm that smart.
It's because this is so easy to use.
So, if it takes me 1 hour, well, okay, I
have some experience with web services.
But if it takes me 1 hour,
maybe you have 1 hour and 50 minutes to
complete this.
It's that easy.
You don't believe? It is.
All right.
Next demonstration.
Synchronize an Office 365 inbox
including attachments.
Imagine that you have an inbox
Office 365.
It receives emails with, for example,
these PDF files that you want to OCR.
Instead of downloading them
or automatically forwarding them to the
OCR service, you can also get them at
first in Dynamics NAV,
storing them in a blob,
maybe previewing them,
and then with a press of a button send
them to the OCR service, or maybe
automatically send them to the OCR
service.
So, what I'm going to show you to
demonstrate is how easy it is to get all
the contents of an Office 365 email
inbox.
And it's also a managed API.
and get your mail
uh ready
because I'm asking you in a few minutes
to send mail to this inbox because I
want to prove that this is working, of
course.
So, here is the the site getting started
with
Exchange Web Services Managed API.
A lot of documentation here. I'm not
going to walk through. You can read for
yourself.
But, basically, it is exactly the same
as the DocuSign part. You have to
download a DLL. You have to install uh a
package.
And
the package can be found here.
And here you have the same thing.
Install the package Microsoft Exchange
Web Services. This gives you two
DLLs.
These two DLLs are also available
already in F2016.
But,
I choose to download them for myself,
put them together with my solution so
that I
can that my solution cannot be broken by
a new version that is being used by
uh by Microsoft in F2016.
So,
in fact, it's duplicated, this DLL.
I'm going to
demonstrate this.
Um first, going to open
the the inbox that I'm reading.
Sign out from this one.
Sign into this new
email box.
This one is empty.
I'm going to
the in online inbox.
And here
in this
part
it will show the incoming emails.
So, now I'm going to ask you
send an email
including an attachment
to finance@cronus.company.
I will type it for you.
finance@
cronus
.company.
I can hear
emails
coming in.
Already?
A lot of emails.
So, let's see what's happening
in Dynamics NAV.
Well, here you see them
flowing in directly into NAV.
Total of eight items.
Two are unread.
And this thing this page is
synchronizing every 10 seconds.
And of course this can be done using uh
a NAS server that is running it
uh each minute or each 5 minutes or
whatever you want.
So, to prove that this is working
I pick one
that is uh
including an attachment.
This one has an attachment.
I open this one.
Here we go.
You see?
Just coming in.
I'm not faking this.
It's synchronizing right now.
So, it freezes.
I should take this one, Alin is telling
me.
I'm not sure if I want to.
I'm I'm brave. I'm just trying it.
Don't have a wrong picture.
Oh, okay. Well, we can handle this one.
Just send in.
So,
a lot of emails are flowing in right
now. I'm going to close this one.
So, what's going on behind the scenes?
How does this code look like?
First of all, I have that
um
that page over here.
Oh, it's synchronizing for the next
I have that here. Total items 33, unread
items one.
This is because I have this get inbox
count.
This is a
a call from the page.
I test if I have a service URL.
This was created by auto discovery.
Then, I ask
to uh create Exchange Web Services
credentials.
Let's go to that one.
I have an Exchange account username.
I must have a Exchange account password
key.
And then I create web credentials or web
credentials, which is basically a .NET
component.
Then
I do a folder.bind
based on the well-known folder
name.inbox.
There's also
a class coming from that DLL.
I can tell you there were a lot of
.NET variables going on here.
And then I simply can set folder.unread
count, folder.total count.
That's it.
It's that easy.
Then how to synchronize the inbox?
Again
I do this thing with folder.bind.
And then I have a small wrapper.
This is because I had a problem with the
.NET interoperability
using the web service synchronization.
So
I'm switching to Visual Studio.
I open the
nav
sync wrapper.
There's a little code here.
That much.
But basically it is about the sync
folder items.
It gets the Exchange service.
It gets the folder ID and the sync
state.
And then the sync folder items
gives me, based on the synchronization
state, what are the new items in the
inbox.
So I'm not reading the inbox like give
me all the messages and then I'm
checking if I already read that
messages. I leave this for
Office 365
based on the synchronization state that
I save in the database, which is a large
text
basically. Um and this key now is is
then recognized by Office 365, so it
knows at what time you had that
synchronization, so it can determine
which emails were new.
Then
I want to have normal items.
No
um
uh things like uh scheduling for agenda
or whatever.
And then I get
this one, a change collection.
And the problem with change collection
was that I could not create an instance
of change collection in C A L code
because change collection is a generic
item, a generic class, and generics are
not supported by C A L currently.
Maybe in the future, so I can get rid of
this one.
But because
uh of um
that that that C A L code does not
support the generic classes, I had to
create this Visual Studio wrapper.
Uh it's a C# wrapper around the change
collection, which is basically uh in I
IEnumerable. So, the only thing then I
can
uh need to return the synchronization
state just to save that one in the
database. I give it return a count, I
don't even use it in my code.
Um if there are more changes available
because it only gives you the next 10 or
20 or 50 items that are new in the in
the inbox.
Um so, and with this Boolean you can
find out if there are any more.
Um,
and this one is the most important
thing. I have an I enumerator.
This I enumerator that I return based on
uh with this function get enumerator
is used
in
um, my code here
with this for each command which is new
in F 2016.
So,
this is the NAV
EWS sync wrapper.
And the for each command
automatically gets for me
this
I enumerator get enumerator.
This is because I
inherited from I enumerable.
And then I can
look into my item change
which is basically
a class coming from the DLL that I
downloaded.
Then I can look into the change type and
see if it was a change type create,
update, delete,
or the read flag change.
So, with this demonstration I only use
the create which means basically this is
a new email.
But you can also have uh
an updated
uh well, maybe not an updated email, but
you can have an updated uh
scheduling item or an agenda item,
whatever.
You can also see this uh agenda items
with this uh code.
If it is de- being deleted from the
inbox, you also get the message that it
was deleted. And if the read flag was
changed, you can
uh also track that down.
Then,
if that one was created,
I just say, "Okay."
If it was an email message,
then bind to the email message.
Each email message in Office 365 has a
unique ID.
You can just bind directly to the email
message. You don't need to have that
inbox
uh ID or whatever. You can just directly
grab an email by binding it using its
item ID.
So, here I have that
item change dot item ID.
Bind
the email message,
which is
some code here. Bind email message. And
here I set some properties. I want to
have my first class properties like
sender, receiver, subject.
I want to have a normal body.
And also want to include attachments. If
you don't include attachments here,
you'll have to get them later with an
extra call of your code.
And then here I have that email message
dot bind on this service with this ID
with my property set.
And then I return the message.
And then here
I can just say my email item from
the two recipients, the
copy recipients, etc.
And put them
write them into my database.
If my email message has attachments,
then for each attachment in the
attachments,
and then I say, "Okay, if my attachment
is not in line, it's really attached.
It's not that picture in embedded in a
mail message, I'm going to save it in a
blob."
So, I'm not going to walk through each
line, but this is basically what's
behind the scenes.
And then I
change the email message to read.
And if there's a read re- receipt
requested, I say suppress that one. I
hate them.
I don't want to let the other person
know that I have read a message
because maybe I don't want to reply and
then I get the that message from, "Hey,
I saw you read that one. Why don't you
not replying?"
All right.
So, this is the final demo.
Um
if you want to have more
useful web services, here are some
ideas.
Azure file storage,
complete API.
So, you can
um send, store files on Azure directly
from C A L code.
EAN search, which is basically a
database filled with item information
filled by uh the um vendors who
uh can
uh
s- who sell these items.
And the programmable programmable web
web site contains tons of web services
that are available. It's just a
directory of web services that are
available.
So, I have a call to action for you.
First of all, learn .NET
interoperability.
There was a lot .NET DLLs
behind all this code.
If you don't know how to use .NET
interoperability, start with it right
now.
Yeah.
And I can really second that. Uh on the
project that I did with Arjan, I think
it was the project where I learned the
most about .NET and C sharp and uh
really start deep diving into this stuff
because it's really important and makes
your life easier. We are living in a
connected world, even though Arjan broke
the cloud. I think Azure is now We had
broken clouds, remember?
Yeah. We had broken clouds.
the cloud.
Yes, there was a better today.
Yes.
So, no more Azure, guys. Sorry.
So, learn C#
if your .NET uh DLLs that you can
download uh cannot be used in CIL code,
you probably have to write a wrapper. Uh
uh and and well, then you have to to
type C# write C# code yourself.
Think simple.
Choose your battle wisely.
Do not try to reinvent the wheel.
If there is a web service available out
there for that task that you are uh
trying to to use to do,
go and use that web service. It is
or it can be for free or you pay a few
bucks per month to to use a web service.
So, that's it.
We open up for Q&A. So, let me ask the
first uh question. I think Arjan did a
really great job, guys, with all these
demo. It was really really impressive.
This was This was really my easiest
presentation at NAV Tech Days ever. Um
my first question to Arjan would be, is
this going to be available on your blog,
Arjan?
I got this question
multiple times after Mannheim, after uh
Directions Orlando, and the answer was
yes.
It will be available after Tech Days.
But I have to have some spare time
to write my blogs.
That's my uh challenge to find time to
write blogs. But okay, I will post this
code. No support,
of course.
But you have his phone number.
And even you have some email addresses
as well, but I'm not looking in these
inboxes for any support questions.
And this this session is recorded, so it
will be on Mibuso, and I find it very
useful for those sessions if you
attended that uh I know that Arjan said
something, but I don't really remember
so you can go on maybe so download the
video download the slides and then you
can you can look at the details again.
We have 6 and a half minutes left for
questions and good questions get
t-shirts.
We have got
five of them so who wants to get a
t-shirt?
I think we have a question over there.
You have to ask a question for that. You
have a microphone where's the microphone
over there? There's a microphone over
there.
I was just curious
maybe not quite as knowledgeable but
security issues regarding calling these
web services
what should you be looking for?
You mean security issues with calling
web services?
Viruses
problems getting from a foreign web
server coming back to you somehow.
Um
there are some security issues that you
should think about.
Calling a web service you of course you
should
trust that web service.
So any free web service
is probably something that you should
carefully investigate if you can't trust
that web service that is first. If it is
a paid web service then it's probably
also
coming with some kind of support so you
can ask that question.
The next thing is if you going to store
any username and password in the
database
basically means that you trust your NAV
application to store this username and
password.
Any user who is using that application
is theoretically
capable of using this username and
password to call that web service. So
imagine that Office 365 inbox part
if you are storing username and
passwords of end users in the database
to let them know that there is an email
coming in in their inbox from NAV
gives the possibility to other users
to read his colleague's inbox.
Should not do that.
The only way
to do this kind of synchronization
is to use the consent framework.
By you let the end user trust the
application
on his machine
to read his inbox.
It's a totally different part and I
decided to not go into the consent
framework here because it's more
complex. But never
uh store personal email box credentials
in NAV.
That's not the thing you should do.
Next question.
Uh
you got a t-shirt?
Yeah, yeah. I
Okay, you go on.
I'm your lovely assistant. I do that
stuff for
That's why I have the pony tail.
I have a question about the
documentation. How do you figure out how
to take care of all these pieces of
code?
Just use the API documentation that
uh the web service providers
uh providing or go and search online
with Bing, Google, whatever search
machine you want to use.
Do you have any recommenda-
recommendations on uh starting those uh
learning about .NET interop
I I always first start with the
site of the web service
and then I look for
I look for um
C# API documentation, how to use that
API with C#, because that one comes the
closest to how you can use it from C/AL
code.
Yeah.
That's the one how I I do it.
And that's why it's important to if you
don't want to program C#, at least learn
how to read it.
Because reading reading C# makes your
life a lot easier as an NAV developer.
And if you have to use some .NET
framework DLLs, like you have to use an
array
.NET array or .NET convert or whatever,
and you don't know how to get it, just
Google on C#
convert and you will get an MSDN
article where you can see where that
class is, in which DLL it is. So, and
then you can go to your code, pick that
DLL, pick that class.
Next question.
Uh do RESTful web services support
transport and or message security?
Uh message security, you say?
Yes, like uh signing and encrypting uh
the HTTP request.
With SSL certificates or
basic authentication?
Hm?
Yes, for example.
Of course, because um
it is the URL that is um
defining if it is
um uh
secured with an SSL certificate.
And what I didn't show here, but I will
try to post on my blog as well, is how
to add basic authentication to it.
Um
the thing is that
um
all these demos
uh accept a username password in the
URL.
Or in the data that is being posted.
But you also can have some um REST
APIs that accept basic authentication.
OData from Dynamics NAV is doing that.
And then you have to add an
authorization header.
Well, that's different stuff.
And that was the part I was trying to
create when we started here this
morning.
But I didn't get through it that fast.
So, I will try to figure out how to add
authorization headers and post it on my
blog as well.
What's with the guy behind you?
What are
If if you're exposing the web services
instead of consuming them, what are the
license implications?
I mean, if you're only um
living in a couple of tables
more than the the simple user.
License implication of exposing web
services from Dynamics NAV, you mean?
Exactly.
Yeah.
Um
If you are exposing web services
from Dynamics NAV
and they are used by
the customer of your customer
you can use them for free.
You have a web service user that you can
create
together with a web service key
which basically serves as the password
for the web service user.
This password then
cannot be used to log in into the
client.
But as soon as you expose web services
that are used by your
the employees
of the company, then you have to have a
user in the license.
So, that is the difference between.
You got a t-shirt?
All right.
Okay, we have
I have one t-shirt left.
time, but we have one one t-shirt left.
Just throw it in.
30 36 uh seconds over time.
I want to throw a t-shirt myself.
question. You want to have a t-shirt
yourself?
I I want to throw one.
You want to throw a t-shirt?
I also want to throw one.
But that's the furthest one away, so you
have to really throw.
Yeah, we we we've been having some
problems with web service APIs that
they're using the OAuth protocol. Do you
know of any libraries that we can make
our life easier in this way?
It's hard to get a question. Did you get
a question right, Mark?
Uh no.
It It's hard for me to to hear you what
you
We've been trying to use some APIs that
use OAuth
as the
OAuth?
OAuth.
Yes?
Yeah, protocol.
Uh I I'm not using OAuth, so it's
something new to me.
All right, okay.
Okay, so
So
Who Who knows OAuth from you?
Two or three.
It's a So I'm not the only one who
It's It's a It's a security
authentication protocol that's quite
complicated. I wonder if you had any
experience of any
come across
libraries. Okay.
I basically want the same thing.
Okay.
What's the same question?
Wasn't it
No, what are questions?
Just
But
hello.
Uh my question is
I'm pretty sure it's a gun now.
Okay, never mind. Uh could some of these
demos be be done with new data data
exchange framework we used for currency
exchange update?
Yes, I guess so.
Yeah?
Yes.
Some of them, not all of them, but some
can be done using exchange framework.
Is that easier? Maybe?
For some of them, yes, probably. Yes,
that could be easier.
Okay.
Okay, thanks everyone.
Have a nice
and happy tech days.
