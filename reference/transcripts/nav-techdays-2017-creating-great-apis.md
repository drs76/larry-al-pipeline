# NAV TechDays 2017: Creating great API’s

- **Source:** https://www.youtube.com/watch?v=d9jMAnYB6qk
- **Video ID:** d9jMAnYB6qk
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 97m03s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Thank you. First of all, welcome to all
of you. It is wonderful to see so many
people in this room that want to hear
about creating great APIs.
Just a practical, this session is
scheduled to last 90 minutes. We will
try to reserve the last 15 minutes for
questions, in case you have questions.
And then we'll also be available after
watching, in case you have some
follow-up question.
And you can hunt us down tomorrow as
well.
But we being my myself, my name is
Anders. I'm a developer from Microsoft.
I actually got my CAL license back in
'93.
And that will mean next year I can call
myself senior developer having 25 years
of experience.
With me I have Nikola.
So hi everyone. My name is Nikola and
I'm also developer from Microsoft and
I've been working with NAV for the last
10 years.
And this is basically my fifth TechDays
conference, so it's a double
anniversary.
Yeah.
And so we should start with the session
because we have prepared a lot of
content for you today.
So on the previous TechDays and few
years back as well, we were showing you
this slide and this slide is summarizing
all of the external web services that
the NAV is integrating with.
And you could have seen in the previous
past years that we have been increasing
the number of services that we have been
integrated to.
And this year we are basically flipping
this picture around. So instead of
integrating to the other web services,
we would like to be able to offer to the
other web services to integrate to us.
So basically we have managed to turn the
NAV into a back-end that you can
integrate to.
So if this is NAV and we are hosting it
in the cloud,
in the last year we have built a set of
APIs on top that you can use to
integrate your solutions to.
So now I want to open question to all of
you. What is the difference between a
web service and an API?
So, what is the thing that makes an API
different than the web service?
And an answer to this question is
basically two two ways.
So, every API is a web service in the
end, but the API should serve as a
shield.
So, the first requirement that a good
API needs to fulfill is that there must
be no breaking changes. So, once you
deliver the API to the general public,
you must not do any breaking changes in
it.
Otherwise, it shouldn't be called API.
And the second important consideration
is that it needs to be very simple to
use.
And this consideration goes together
hand in hand with the consideration
number one. Because if you make a
complicated API,
it's going to be really hard not to
introduce any breaking changes, right?
Um
so,
we got our first users, and the office
has integrated to us. So, right now we
are serving as back end to the office.
There is a solution that just went live.
It's called Business Central that we
will briefly demo today.
And tomorrow we will be There will be a
session that is going to demo it and
explain it in a very high level of
details.
Then we have also managed to integrate
the QuickBooks desktop through the
microservice with our cloud offering.
So, we are able to pull the data from
the QuickBooks desktop into NAV, and
vice versa from the NAV to push the data
into QuickBooks desktop solution.
And lastly, we have managed to build a
lot of cross app scenarios. So, for
example, you are able to create from
your calendar
an invoice via web services.
And we have also started to write native
apps like
Android and iOS apps that are using NAV
as a back end
through the APIs.
And basically, this is where you come
into the picture because these APIs are
also intended for all of you to build
your integrations on top.
So, we would like you to write your own
microservices, your own apps, and your
own UIs.
And one thing that is great about this
conference is that every year when I
meet all of you guys and talk about the
different solutions that you do,
I'm really amazed with the way how
you're using our platform. So, that's
really truly amazing.
Now, uh everything that you write on top
of the API stack is going to work for
both on-prem and on SaaS.
So, you just need to change the
endpoint, and your solution should
continue to work,
which is really a good offering that we
can give.
And because, as I said, there are no
breaking changes, there should be no
code merge and no upgrades that you need
to do in your own solution.
Uh since these are all web services that
have been around for quite a while, uh
you can use any language to code against
this. So, you can use C#, JavaScript,
CIL if you're efficient with it. We have
wrote a lot of wrappers, and also the
modern
development environment that was shown
today is also supporting invoking web
services.
And pre- While preparing for this
session, I have learned that it's even
possible to code in COBOL.
So, all of the languages are basically
supported. Yeah.
And so, we would like you to leave this
session today
by If you don't know OData and the REST
API, we are going to do a basic
introduction so you can follow.
And then I'm going to show you some
advanced concepts and some new
capabilities that we got in OData V4.
Then, Anish is going to demo to you the
currently available APIs that we are
shipping out of the box.
Then, we would like you to understand
how the different endpoints are working.
So, what is graph, what each endpoints
are available in SaaS,
and how can you connect it with on-prem
solution?
And we will end with building your own
APIs. We can also sneak in a design
patterns subject.
And we will also talk about future
plans. So, what are we planning to build
on top?
So, with this, I'm going to turn it over
to Hannes
to do an introduction.
Thank you, Nikolai.
So, I will introduce you to REST and
OData.
REST was defined and introduced back in
year 2000 by Roy Fielding, where he made
a doctor disputes, where he introduced
that concept. And since that, REST had
been taken up by every service almost.
And they have implemented REST-based
call using more or less their own
interpretation, but still have the
common way of doing that. The most
important thing to know about REST-based
call is that they are stateless, unlike
the old
service we had, the SOAP service that we
have, where you could preserve state.
Microsoft,
we have our definition and
interpretation of REST. It is called
Open Data Protocol.
That work started back in 2007, and
currently we are on version four.
In this presentation, we have some
links. I will, of course, not go to all
of them. I think those three links are
some of the best, especially if you are
brand new and a bit uncertain about what
OData and all
that is, please take
click on link number two. And the good
thing about TechDays is actually
presentations are available afterwards.
So, you can take them, and you can
click.
But, what is OData in practice? It is
get, post, patch, and delete.
It had been nice if we just called it
read, insert, and
modify the lead, but get, post, patch,
and delete. It's very simple.
So, here is a short example of how you
can see a JSON
of getting the the company entity for
our endpoint.
An ID, a system version, the name and
display name, and the business profile
ID that we're exposing here.
Now, before we go into the APIs, I will
talk more into the endpoints, the URL we
have.
We have two set.
The one we have in our SaaS offering,
and the one we have on on prem. So, in
SaaS,
you can call API invoicingoffice.net
and version 1.0, and that version is
referring to the version of the
endpoint.
Then, follow I want to have API.
Then, we have beta and the concrete
entity. I will in the next slide talk
more into versioning of the APIs.
Similar for invoicing as Nicolai
introduced that we have the business
center that is calling us because we are
the back end for office.
If you want to call a tenant directly,
you just add the tenant name in front of
it.
On prem,
it also works on prem.
It is just machine name, whatever port
you're using, Dynamics NAV, uh sorry,
the instance name, of course, API/uh
beta, and then the entity that you are
asking for.
We will also talk more into later on how
you enable
APIs on prem and what kind of
authentication that are available with
the different endpoints that we are
showing here.
As I said, I will return on the
versioning. We are currently in what we
call beta
with our APIs.
I will guess it is very unlikely that
we'll break them. I'm quite convinced if
we break them, and I will be called in
the middle of the night, and we don't
like that.
But we will soon get on official version
one. So, Microsoft is a big company, and
we have processes, and we need to have
that version in draft,
and we just have to wait until we can
flip it to version one. But hopefully
soon, we've been promised.
When we have the versioning in place,
then whenever we
do It's a breaking change, or when we
create a new version of of of an entity
API, that will not be compatible with
the previous one, then of course we'll
create a new version and maintain that.
And then previous version will work
normally until you update your code.
Now we come into getting some of the
data now that we know what endpoint to
call.
It is get This I have API invoicing
office.net, but it will also be
dynamics financials.dynamics.net.
The API, the beta, and then there's
something a long thing. It's a good.
It's a unique ID,
and we want the the keys to be
canonical, and therefore they must never
change they must because they must never
change.
Inside the app, we actually keep track
of those ID even if you delete the
entity. For instance, delete a customer,
we just keep track of that ID used to
belong to that customer.
Yeah, again, most keys are represented
here as good.
So, here you are another important
thing. if you are fetching a large
larger set of of data,
then of course
we have a limitation that you will only
get in a set at least we have set that
up 2,000. You go going to get the first
thousand road and if you want more you
just need to to fire a content
contention set link
to get the rest of that set.
Here I have some example on how you can
get uh
how you can get a list of invoices, a
specific invoice.
Get the nested record. So, normally an
invoice is actually only interesting if
that invoice also contains some lines
and that is a nested set.
We also, if you want to get an entity
using a more complex key or alternate
key.
I will, after those few slices here,
switch over to Postman where I'll just
fire a few Postman scripts so you can
see how it fits data.
When you are posting
creating data
you need to specify that the content
type type is application JSON in the
header.
Do whatever authentication that you're
planning to do.
And then in the body you specify the
fields that you want
to to create the customer with in this
example here.
If you also just took take a short look
at the URL, you can see that every
entities are entities under the company.
It's obvious that when you as a user log
in to your company, then you will see
the customers for that company and you
can have several companies. The same
logic is replicated here in the APIs.
If you want to modify or delete data,
oh, we also have a very, very long
strong there at
text here.
An e-tag.
So,
normally when you are developed towards
traditional navigation, we keep the
server keep track of version of the
record that you are working on. So, if
somebody else changed the the customer
while I'm working on that, you will get
this conflict.
We are enabling that for the for the
external developers by supplying a e-tag
whenever they get a data,
and they must preferable use a match on
that when patching or deleting an
entity.
If you're just playing with the API, you
can just do if matched asterisk. I don't
care if other have changed them, and
that's easier.
But, it is good practice to to take
versioning into consideration when
building an app.
So, now I'll just shortly switch over
here to
if I manage to do this. Oh,
this key.
Come on.
No.
Do you want to switch here? Yeah, just
switch that.
Yeah.
So, here I'm using the tenant specific
endpoint.
So, you can see
M365, whatever. That's the name of a
tenant I'm working on, and it is in SAS,
so it's financials.dynamics.com.
I specified the port, and then MS for
for Microsoft here.
API beta and companies.
And it is the companies that I want to
see, so I just
And here you can see I have two
companies on that tenant.
Exactly just like building a page inside
NAV and run it and see what's inside.
And again,
here you see the ID.
So if I want to get a specific ID, uh
sorry, specific company,
then I just in parentheses put that key.
And if I try to send this,
you will see now I'll only get that com-
a company I requested.
And then here another example of get me
give me all the customers under certain
company.
And then you will see this long list of
customers.
Later we'll talk into that there aren't
that many fields that you normally see
on the customer inside NAV.
Post.
The only thing that is slightly
different here is that I in my request
header I need to say that I am sending
this as JSON.
And here I have the body where I can
specify a display name let me see the
world of 44.
Whatever that means.
And
here you can see the result that is
coming back the response.
If you want to patch,
I will only here say that it is the
header that is important that you
specify whether you care about
versioning or not.
And similar, you can do you can do um
request for getting invoices and built
on top of that. For that invoice, I also
want to have the invoice lines.
Let me see if this work.
Ah.
Mhm.
The presentation is not running.
All right.
Let's see if I can get
Mhm.
There we are. Sorry.
Oh, and with this I will give over to
Nikola.
Thanks.
So, let's look a bit deeper in what is
available out of the box. So, in the
last version, we have really enriched
our OData V4 endpoint. And we have added
a lot of new functionality to it.
So, for this part, I'm going to start
with explaining the authentication to
all of you guys, because without this
one, we cannot start.
Then, I will show you how you can
understand what the capabilities of the
services are by reading the metadata.
And we will briefly go over the data
structures that are available.
And then, basically, we are going to go
through all of the new functionality
that we have added, dollar expand, deep
inserts. We will briefly touch up on the
batching.
Filtering, we have added actions. The
actions are especially cool because this
was the main limitation that we had on
OData compared to SOAP, because before
it wasn't possible to invoke the
actions.
And then, we will go through the error
handling and selecting a language.
So,
for the authentication, uh you have only
two ways of authenticating against our
web services. And the first one is the
web service access key, and the second
one is user bearer token.
And an important thing to know is that
the API is always running as a user.
So, both of these authentication methods
are connected to the user.
So,
the API call is going to have exactly
the same permissions as the user has.
And as well, if you're doing any logging
on the username, then
depending on the credentials of the
user, we are going to store that in D N
A V.
So, the first way of authenticating is
the web service access key, and this one
is the easiest to set up. So, I'm going
to just to show you briefly how you can
do that.
So, if I switch here, and here I have my
cloud instance.
So, if you just navigate to users card,
and you open the user,
here you're going to get a web service
access key. So,
if you want to expire it, you can just
open it, and you can also
change it and update it to a new
new value, right?
So, how to use the web access key? It's
very easy. So, I'm going to copy it.
And the second tool that we are using in
general is Fiddler. It's similar to
Postman, but some people would say it's
a bit more geeky.
So, yeah. I prefer it because I've been
using it more than I have been using
Postman, so it's more like a preference.
And the cool thing that we have here is
a text wizard. So, in order to use the
authentication token, I have to be
64-encoded.
So, I'm going to type admin colon and a
web access key.
An important consideration is that you
shouldn't have any new lines or any
spaces, because you see how it is
changing.
So, if you have a return line or a
space, the web service is going to
reject
the
access key.
So, if I go back,
okay, I have to close this one.
And I just provide here the web access
key.
And now I'm able to call this tenant. A
big limitation with web access keys is
that you have to hit the URL exactly.
So, I have to know what is the address
of this tenant before I can communicate
with it.
So, if I execute the request, I'm
getting the companies back. So, the
service has allowed me to interact with
it.
Now,
for the second way
of
authenticating is basically bearer
tokens. And this is also rather simple
to use, but it requires a bit more
setup. And the tokens are superior to
the web access keys because they're
containing information about the user.
I'll demo this one quite shortly.
So, in order to get the token running,
you need to get four pieces of
information. And this is the hardest
part.
So, get obtaining these four points,
that's the hardest part with using the
tokens.
And this is the example of C# how you
can actually generate the token. And as
you can see, it's only two lines.
Um on the bottom of the slide, we have
put some excellent article. If you would
like to get started, we really recommend
that you just read it after this
presentation from the slides itself.
So, basically to show you how you can
generate the bearer tokens,
I have wrote a PowerShell helper that
I'm usually using.
And it's rather hacky because I just
like the things that work. I didn't
polish the code.
So, in order to get the token, it's the
same code as we have in the C#.
So, we need the user's credentials. We
need under which authority we're
authenticating.
And then we are just invoking the same
functionality as the C# does.
I have also implemented that it copies
it to the clipboard because that's what
I'm using when I'm developing. So, it's
very easy to paste it back in the
fiddler.
So, if I just
get the token for the user number one.
And if I go back to the fiddler
in this
text wizard, and if I put the token here
and now I say please transform it from
base 64, you can see all of the
information that it's sending to the
service.
And right here, you can see under which
account the
token is going to authenticate against.
And this is really enabling us to know
which tenant you want to provision,
which credentials it has, so we can know
a lot of things by using a bearer token.
So, we can provide additional
functionality for you.
So,
if I would like to use the same thing
here
then I would just need to change this
basic to bearer
and paste the token.
And then if I
execute the same web response request,
oops, it doesn't work.
So, let's try here.
Let's see if it will work.
Yep.
So, basically we were able to get the
same response for the tenant.
And you can see that here we don't know
the tenant name, so we're hitting the
forwarding service which is based on the
information obtained from the token
directing the call to the proper server.
So, back to the slides.
So,
as I said, the tokens
have a simpler uh authentication. If the
user is logged in, you can just reuse
the credentials. You don't need to store
the web access keys and update them and
do this kind of manipulation, so it's
easier to manage.
Then you can use the single endpoint
with the tokens. And the cool thing that
we have enabled with the single endpoint
is that if you don't have a tenant, we
are going to automatically provision one
for you within 40 seconds.
So, an API call is going to lock, and
when it returns, you will get the tenant
set up.
So, it's very important when you're
specializing specifying the URL, are you
going to say invoicing on financials
because that's the tenant that you're
getting in the end. So, we'll either
provision on financials
or invoicing
tenant for you.
And each token has an expiration time,
so it is easier to manage. If you revoke
user's permissions, you don't need to go
into the user part and then do the
management of the tokens.
And web access keys in general are quite
good for prototyping. So, it's as you
saw, it's just a few clicks. So, if you
would just like to get up and running
fast,
you should be using these.
Then, the second important concept that
we're going to go into today is
metadata, and this definition is pretty
good. If you would like to learn about
the service capabilities, there are two
ways of doing this.
One is is docu- reading the
documentation, and the second one is
dollar metadata.
And dollar metadata is better because it
is always up-to-date, right? It is based
on the code that is currently running,
and
you can even see something that we have
recently implemented that haven't been
documented yet.
So, if you invoke the call like this, as
I did,
we are going to return you what are the
capabilities of this tenant here.
And the metadata is being returned as an
XML.
I have a nicer view here.
So, if you take a look here, you can see
that we are having some complex types,
and nullable means that it can not be
specified.
Also, you can see the data types,
maximum length, and
which entities we have here,
navigational properties,
and various different stuff about the
service. We will also tell you which
fields are read-only,
on which services you can insert, on
which services you can modify
and additional information like this.
So, it is quite useful.
And yep, this is how it is looking like
and this is the URL that you should use
to obtain the metadata.
Now, as you saw in the metadata, we are
giving you which data types we have
enabled. And in short, they can be
categorized into three groups.
Entities, subentities, and complex
types.
And entities are main records like sales
invoices, customers, and vendors. So,
that's where the main data is.
Subentities are the dependent records
and they cannot live without the main
records. In NAV, that would be a sales
invoice line or dimensions.
And as you can see, we can reuse one of
the subentity
on multiple APIs, which is really nice.
And then the complex type is just a
struct, which is reusable.
And the cool thing about it is that, for
example, we when we have an address, we
can have the same address format on the
sales invoice, on the customer, and on
the vendor because in the end it's the
same information.
Now, for a design question, which is
constantly arising, when should you use
the subentity and when the complex type?
So,
there is a performance impact when
you're using complex types because
they're always loaded. You cannot easily
exclude them from the response.
And subentities can be accessed directly
if needed. So, you can just navigate to
the subentity without accessing the main
entity.
But the complex type cannot because it
just lives on the main entity itself.
Uh now, complex type is updated in a
single transaction. So,
if something fails, we'll roll back the
transactions. While for the entities,
you need to do a different request if
you would like to patch it.
Yep. Um a new capability that we have
also added are navigational properties.
And
in NAV terms these would be payment
terms, units of measure, or currencies
that we could have on the sales invoices
or on the customers.
And they can be inserted or they can be
expanded with the dollar expand.
So, I'll briefly demo these.
So, the dollar expand is going to return
your value
from the related records. So, if we go
back to the fiddler
and this is the new functionality that
we have introduced.
So, and if we say dollar expand
so, and I need to paste the token here.
And if we would go here and if I just
fetch the sales invoices like this
and if I do this expand lines
so, here you can see that there are no
lines in the response. So, I'm not
getting them
as related data.
But with the dollar expand
they are included in the response. So,
you can fetch the invoice and the lines
together.
And basically you can chain up as many
navigational properties that you would
like. You can get
currencies, payment terms, and
everything else that is specified
in the metadata.
Then for the next concept that we have
Oops, sorry.
That's deep inserts and deep inserts are
also a data V4 functionality that we
have recently added and this allows you
to insert in a single call
the main entity and all of the
navigational properties that it has.
And the really cool thing is that it
runs as a single transaction. So, if
something fails, we will roll back
everything. So, you don't need to manage
the state.
So, for the example we are going to
insert the sales invoice with the lines.
So, if I I go back here
and I would go to my deep insert demo.
And paste the token again.
So, you can see that here I'm inserting
a sales invoice. I have specified the
customer and I have specified the line.
So, if I execute this request, I'm going
to create an invoice together with the
line.
And this invoice now can be posted,
which I will do a bit later.
And then if I
Mhm.
If I try to do an invalid deep insert,
nothing is going to be created and I'm
going to get 404.
Which is really a benefit if you would
try to first insert the header and then
the lines and then you would have to
delete the lines that didn't succeed and
header and mess with the data itself.
And the side effects that it could have
created.
Uh
Many people like the deep inserts a lot
and then they asked us, "Can we get a
deep modify?" And the answer is no
because it is not supported by the
standard.
And deep modify supports not really
work. Uh the reason why is because you
need to specify concurrency token.
So, what if the concurrency is off for a
single record that you're trying to
modify, right?
And you're not changing the latest
version. It would really be complicated.
And that should be fixed by the dollar
batch. And with the dollar batch, as you
can see,
you can batch multiple requests and
submit it to the service.
And then service is going to take it one
by one and process them.
Unfortunately, with the current version,
we only support a single write
transaction
within the change set.
So, the change set itself, it should be
transactional.
And but unfortunately, we are not able
to support this from the back end
because we cannot guarantee that we will
revert.
Since you know, in C L, you can hit
multiple commit statements
and then we would have to lock the data
while the operation is running, which
would impact the availability of the
service. So, it is a rather hard
problem. So, we have allowed it to only
to do a single right within a
change set and I would advise you not to
do the multiple rights in the multiple
changes in the dollar batch because then
it's really hard
to control what happened if something
fails.
So, you can batch a single right and
multiple reads.
That would be a recommendation if you
need to do that.
Then we have a dollar filter, which is a
cool functionality. So, basically it
behaves exactly the same as UI filter.
And you can filter on the APIs.
Since it is behaving the same as the UI
filter, the same limitations are
applying as in UI.
Namely, you cannot filter on the
calculated fields. That's going to be
ignored. Also, on the global variables.
That's also going to be ignored.
And the no unions are supported. So, you
can say give me everything that has a
price of 100 or price of 200,
but you cannot say give me everything
that has a price of 100 or is being sold
in pieces
because that request is going to be
rejected.
So, to show you an example of
filtering.
So,
here I have my own request and I'm
trying to get all of the invoices that
are in draft states and are worth more
than 100
including tax.
So, if I specify the bearer token and I
execute it,
I will receive back the
filtered list.
And this is really cool if you're trying
to build any kind of a UI or just fetch
a single entity.
Then, for the next thing that we have
added is that now we are allowing you to
read binary content. So, you can fetch
the invoices printed, you can fetch the
images,
and other things.
And just recently, few days ago, we have
also implemented writing the binaries.
So, but we will not demo it today.
But basically, now you will be able to
push the binary content to the service
itself
by using the same approach.
So, to switch to the demo to show you
this one.
Now, if I go to the composer,
and
I ask for the company information here,
and I give my token, of course,
and I execute it.
It looks like I clicked twice. So,
and and I'm getting Now, I received the
company information back. And here you
can see that I have a picture. And the
picture has a link.
So, if I just go up and I change this
URL and I paste the picture,
and I delete this media link before,
and I execute the request,
and if I say like raw,
no, image view,
you can see that I got my company logo.
And you can use this API for getting
items or customer pictures or anything
else.
Then, we also have this functionality
that you can get the PDF. I just need to
get my token back.
And if I replace this token
here,
and I do execute,
and this one is basically returning a
PDF. So, I need to right-click it and
say save response
response body,
and I'll put it on the desktop.
Uh-huh.
Did it save it?
What?
Did you use a folder?
I use a folder. Okay, thanks.
Uh-huh. And here it is, invoice.
And thank you for being awake.
Thanks. Yes. And you can see that I got
the invoice from my company with my
company logo.
Which is pretty cool.
Now.
And basically, this is the best edition,
in my opinion, that we did in the latest
OData stack. So, we have enabled you to
use actions.
And uh this was the biggest limitation
comparing our OData stack with the SOAP,
because in the past you were not able to
invoke the action.
And the first concept is bound actions,
and they are bound because they are
running on a single entity.
And the metadata will tell you on which
entity does the action belongs.
So, it has to run on a record.
And to use it is very simple. I'll demo
it in a minute, because you just need to
invoke a post request without a body.
And the name space is
microsoft.net.nab.post,
and you shouldn't specify content type.
And this is going to invoke an action.
Uh the limitation on this one is that no
parameters are possible, and it can only
return an entity back in form of the
URL.
So, I'll show you this one in the demo.
So, if we go back, and I go back to the
fiddler,
and if I go here,
and
So, just let me find the I'm going to
deep insert insert in French make an
invoice metadata.
So basically, let's just post the sales
quote here.
And here I'm going to say
sales quote lines.
And I need to get a token again.
Because yeah.
And I specified here.
And I
Whoop.
So, this is a good thing that it
occurred.
So, we I got an error.
So, let's see what happened.
And the Uh-huh, okay. So,
I did
I selected here. So, let's try now.
So, the quote got created.
And now I need the ID of the quote in
order to be able to invoke the action on
it.
So, if I go back and I access this quote
like this.
And at the end, I will say Microsoft.
dot NAV.
make invoice.
So, I'm going to convert this one into
the invoice. I need to delete this one
and I need to delete the body.
And I'm going to execute it. And now
this quote has been turned into an
invoice.
And here you can see that I got in the
response the location of the invoice
that I have just created.
So, if I copy the invoice itself,
I can put it in the URL here.
And
just a second so I don't make any
mistakes. And I delete this location.
And I go to the end and I go here.
And now if I do a post request,
yep, I'm I'm clicking it twice.
Now this invoice got posted.
And I get the updated request.
So you can see it's very easy to build
these flows. You can just simply go from
the quote into an invoice just by The
service is going to lead it
lead you by itself.
The next
uh yep, so I have done with this one.
And the next concept that we have are
unbound actions.
So this is the second concept that we
have introduced. And the unbound actions
are running
as as aesthetic. And you should think
about it that it shouldn't run on the
record and it's global for the entire
service.
And unlike unbound actions, it can take
parameters in and it can return your
simple value back.
And you can see this in the metadata, it
is listed on the bottom.
Unfortunately, these are not supported
by the APIs. This is only OData V4
concept. So you can use it from your own
extensions. You can simply publish a
code unit as a web service and it's
going to pop up as an unbound action.
And the interactions with the unbound
actions are the same as they are with
the bound actions.
Now big question that we got when we
were developing these APIs was when
should you use an action and when should
you patch, right?
And
we some developers implemented some
things wrongly to go back and undo it.
So a question for all of you guys,
should this interaction be an action or
should we just simply modify a record
through the patch?
So the first interaction is posting an
invoice.
And the second interaction is accepting
a quote. And if you're not familiar with
this functionality, it's going to flip
the accepted field to true and it will
set the accepted date.
And the answers to these are that the
first one should be an action and the
second one should be just a patch
request.
And the guidance for this is that you
should use patch whenever you can simply
patch the entity back.
If you cannot patch the entity back, you
should use the action to notify the
developer that this change might be
irreversible.
Also, patch shouldn't modify the other
entities within the same request.
While the action can modify as many
entities as it wants.
So, for these reasons, posting an
invoice is an action and patching the
quote is not.
If you introduce an action where you
should use patch, you're basically
introducing additional complexity, which
is not really needed
for these kind of scenarios.
Now, also very important question is the
error handling and this error is the
best internal web server error.
If you're not familiar, this means that
service cannot really tell you what went
wrong, right?
So.
Uh we improved the error handling in the
latest release and to tell you a story
around this one, we were working
together with the Office devs and every
Office developer is going to start the
integration
story with, "Please give us the list of
the errors that the service can return."
And we tell them we tell them that the
NAV can potentially raise 1,000 errors
and that you guys through the extensions
can add even more, they are really
puzzled. And then the next question is,
"Okay, but which ones are occurring most
oftenly, right?" And then we have to
tell them we don't really know, right?
Because that's really hard to tell.
So, in order to fix this one, we have
categorized them and we have introduced
the following categories. The bad
request means that you are doing
something wrong. The request that you
are forming is not valid.
And then you're going to get the message
why.
Authentication is means that you didn't
specify the authentication well.
Authorization is
means that basically you don't have
correct permissions.
Internal means that um
we got some unexpected errors on the
service. It may be valid or it may be
invalid.
And application means that you have hit
AL errors.
Uh
please don't read this slide. You can
come back to it after the presentation
if you download the slides.
These are user-friendly error codes that
we recommend that you can take straight
from the error message and show directly
to the user, which is the same thing
that we have recommended to the Office
Devs to do.
So, if you get this error code back,
you can just simply reflect it in the
error message. Otherwise, show a message
"An error has occurred. Please try again
later." or whatever the correct wording
is.
Um on this topic, we have a full list of
error codes. I think there is around 40
or 50. So, if you would like to look at
look into it, you can
after the presentation.
Now, a really cool thing that we also
got is selecting a language. So, if you
would like to flip the language under
which the web service call is running,
it's very simple. You just need to
decorate it with accept language in the
header and specify valid language. And
then it behaves exactly the same as any
videos. If we have this language, we
will return you the text into this
language, otherwise we'll just use
English.
And this is equal to the AL word which
says global language and then you put an
ID.
So,
and it is only during an API call. After
the API call, it's going to be rolled
back.
So, for the demo,
I can show you this one
as well. So, if I go here
and I want an error in French
and I paste a token. Nope.
I don't have a token.
Give me token.
Yep.
Bearer
And I got an error back.
It's a nice thing in demo when you're
trying to invoke an error, right?
So, you can see that we got this code
internal invalid table relation, and
then I got a message in French.
So, this is really enabling you to reuse
the error messages and text.
If I would try to print a report, the
report that I would get back could be in
French as well.
So, and there are differences between
the API and OData V4 endpoints. And why
is this is because API is being exposed
to graph, while OData V4 is being
exposed to all of the existing
developers.
And also OData V4 was the first thing
that we implemented, so we had a lot of
dependencies that we couldn't easily
change. So, there are slight differences
between the APIs, and you can expect
that in the future as well, it can
behave a bit different.
So, APIs are auto published, and you
cannot change it with the extensions. It
is written in stone more or less.
You can do OData V4 extensions.
URLs are a bit different. In OData V4,
we call it company, that's the main URL.
In API, it's companies.
And there is a slight difference in
response on these APIs.
As I said, on board actions are only on
OData V4.
And for the name spaces in OData V4, we
use NAV.something
for legacy reasons.
And for API, it's Microsoft in front.
And this is important because we need to
integrate to graph itself.
So, to show you a two quick demos.
So,
for the first demo,
I'm going to show you
uh an integration that the Office team
did. So, you can see these APIs in
in practice.
So, if I go to the Office site and I
need to log in.
Let's hope that I didn't make a mistake.
Let's see.
No.
So, what happened with this tenant?
Aha, okay. I got to different site,
sorry.
And if I click on this Business Central
so, when it loads
I will be able to demo you which parts
of the Business Central are using APIs.
So, Business Central is a solution that
was developed with Office, which is
which is supporting you to do multiple
things like invoicing, bookings,
connections.
And there will be a session tomorrow
about it, which will cover it in
details. So, I'm not going to too much
details.
And it's the last session of the day.
So, if you're interested, join that one.
And here
this uh totals are actually coming from
invoicing through the API call.
And as you can see, if you're using this
solution, you're going to be quite
successful. This customer has made a lot
of money, right?
So.
Also, these pages that we have built
here, invoices, they don't look anything
like any of the pages and they're also
being run on the API stack.
And unfortunately, I cannot demo this
one to you if you don't have invoicing
already. When you get to this page, it's
going to ask you if you would like to
get to the tenant. And then if you click
a button through the API call, they're
going to provision a tenant for you
within 40 seconds.
So, if you would like to try it out, you
could see the full experience itself.
And for the second demo
that I have prepared, So, let's see if
this one
how this one will work.
Is that here in the invoicing app
which will also be done with tomorrow in
a high level of details.
Let's see.
Yep. So, let me just log in.
Nope.
So, while we're waiting to log in
here basically I have written a
really quick script to transfer the
customers from one tenant to another.
So, it is very simple in
in PowerShell. So, if I have a payload
from one customer, I can just use the
invoke rest methods to post it.
So, you see this is a brand new tenant
here.
Whoop.
I got the wrong URL. So, I need to fix
it.
So, what's happening?
Ah.
So, just
uh sorry.
This shouldn't happen. This is usually
happening during the demos, right?
So, if I take this thing
and
I take the URL and then I take chess
gifts.
And since I'm already logged in, it
should automatically forward me to the
correct one.
Yep. And it's trying to do a guided
setup. I'm not interested in this. And
you can see the tenant is completely
blank. It has no customers in it.
So, if I invoke my PowerShell script
and this one is now going to start
running.
So, let's see if it will be successful.
Yep.
I managed to transfer a customer.
And I have a bug in the script itself.
So, I need to delete it, right? This was
for testing purposes.
So, let's try it again.
And now this customer list should start
growing.
As you can see, I can automatically
script the things around by using APIs.
We are using these a lot by providing a
specific setup. So, if we would like to
create a demo environment or to generate
a large amount of data, it's very easy
to write these kind of scripts.
And I also have a script that I'm using
to check the health of the test tenants
that we are developing because it is
also very easy to automate
through the PowerShell.
Okay. So, that was all of the demos that
I had for today.
So, I'm going to hand it over to Anders
to show you which APIs we are shipping
out of the box.
Good. Thank you, Nikolai.
So, the APIs that we are shipping out of
the box
we have for long period of time wanted
to have a set of pages and APIs that can
be exposed by external services. And
finally, we got the chance to build that
stack for this release.
So, when we start
figuring out what we want to build and
what what what
deep and brief we need to build, we of
course do what everybody else do, we
look at what our competitors are doing.
So, there's a lot of big American online
services, uh Zero, Sage, uh Sage. We
also have a lot in Denmark. We also
looked at some of the one in Holland,
and I think
two in Germany and one in Belgium to see
what they are offering off the page.
And many of those competitors, they are
in the smaller market segment.
So, that will mean the only
customization model they have, that is
the API stack.
So, we saw what they need to build to
for for other services to be able to
connect to to their ERP system, and we
have cry try to build the same ourself.
So, we are part of the Microsoft bigger
Microsoft group, and and and we are
working on APIs. We'll later talk
shortly into graphs. So, of course, we
also have to do some unifying around
namings.
I think there are also sessions here
around CDS and CDM. This have nothing to
do with this. This is just purely API
here.
And and so, we we need to align the
names. We need to have the set of
entities that our competitors have or
similar.
And then, some of those NAV internal
fields, we need to not expose them for
now.
So, that is also being able to have and
maintain APIs. If you start by filling
in the whole stack, there's a risk that
you do something wrong.
And and and by all all the fields, and
thereby, you need when you fixing that,
you do a breaking change. It is way
easier as they get requested to add
additional fields here.
And of course, we will balance that
expe- expansion against uh with with
simplicity.
Another thing that is important for
being simplicity is
imagine that if you're doing uh
payroll or whatever, you're not an
expert on developing a payroll system,
and now you want to hand back some
finance transactions to an ERP system.
You don't want to read a long book. You
just need to see where are they Where's
the door? How do I kick in the pack and
slam it again and say goodbye? Because
my focus on developing a great payroll
experience, for instance.
So again, we are in beta with our APIs.
We do take the versioning very serious,
even though we are in beta. We are just
waiting for flipping the flag to be 1.0.
When an API get a version, it will stay
like this, and we will support it
forever.
Nobody will say forever in software, but
for a long period of time, and if we are
need to duplicate some, we'll give
heads-up with all the normal policy we
have here.
Another important thing is, now we are
in Europe, so you know
we release NAV in different versions,
but we also release them, should we say,
in a different flavor. So, if you take a
French data schema and compare that to a
Belgian's, I know that at least there is
one field that is different. That thing
there
enterprise number in Belgium,
where is in the rest of countries, we
only have VAT registration numbers.
All those local flavors we have and kind
of figured out how we're going to nail
this out.
Nail this down right now. And we will
see if we need to do it. The advantage
of having this common common API is,
again, if I do payroll in Denmark, then
if I can do it in Germany as well, I
don't have to think about if that
customer is located in Denmark
or Germany when I integrate, I just use
the same set of APIs.
Right. now it's not possible to modify
and extend the the APIs, the standard
APIs, but if you need to, you can
develop all the APIs you want to have
for integrating to a special service
that you have that will grow the
business together with you.
So, if I give some more details on how
that uh for instance, the customer API,
I looked it up the other evening, I
think in W1 we have 89 normal fields in
the customer tables.
We definitely not have that many fields
in our APIs.
We have, I think, around 15 or 20.
A few things that is where that that's
important to be aware of. We do not use
abbreviation in our APIs, so that means
that in no
is number, spelled out.
And then we have to align to Microsoft
naming, so when we see a name,
it is a display name property in a in an
app built by somebody else.
All the complexity that many of you are
deep expert in, like dealing with
with the posting group, invoice discount
code, and whatever and whatnot we don't
we have on the customer table,
we don't expose this.
We will, however, have some templating
behind our customer APIs, so when you
create an API, the bookkeeper can
control when what what default values
various field will get there.
So, here is the set
that is pending to get version one in
the graph.
I will not go into
of the individual APIs, you know,
actually when I learned Navision then I
learned Navision the hard way. Here you
have the customer, here you have all the
fields, here you have the item, here you
have all the fields.
You are clever, you can look it up, so
if you need to.
But I think some of the important thing
that are some of the most important APIs
there is actually something as simple as
the journal and the journal line.
Imagine that you are doing a
an app where you do something again like
payroll or outsourcing
for instance web service uh sorry
warehouse and all that and you just from
time to time from that uh software need
to report things back to the ERP system
to keep the books up to date.
That's very important, so you can just
call the API, flush it in and if you
give that
uh
permissions to that user, they can also
post it using a bound action.
A little thing that we haven't had
advocate that must, we have also exposed
the employee, that's a very old entity
we have there and the only reason why I
want to talk into now is that we have
also make it possible
for posting against
uh employee inside NAV, so if I have
some expenses and that will end up the
company will owe me $200.
You can register that in the journal and
you can see that under the employee.
So that is also some of the things we
have been doing while we have developed
the APIs.
Documentation
or metadata, you know, trust code.
And of course a hint
we are not using na- na- namespacing
inside NAV yet. We are not completely
modern there but our classic development
experience, but the object range it is
there for reference.
The graph
I will briefly talk into it.
The graph is invented by Office and
Office are not shy. They have the end
points to rule them all.
There is a link here to get started
with the graph.
Imagine that a user, Susan, have access
to the Office online and there's a lot
of product.
Now also
she's most likely employed uh hired in a
company and she's working with contact
customers uh items and invoice and so
on. Imagine if you want to build an app
exposing those resources that uh Susan
have created using the other
apps inside the Office family.
It would be nice if there's one end
point where you can fetch them all.
That is available. So, we have the graph
single end point.
Please notice in the bottom of the name
spacing here. I think we have if you
call it with financials,
it will redirect you to our single end
point for the SaaS offering.
And again, if you have logged in and uh
sign in using uh OAuth
uh AAD authentication, sorry.
It will of course pick up the right
tenant and find all the details that uh
you want to fetch from that tenant.
Or from Office or from CRM if they have
exposed those entity.
This is a slide for reference. Please,
the important thing to notice here is
the difference amongst end point and the
fact that when you go home, get
hopefully now 2018 soon, install that,
APIs are disabled out of the box. Nico
will talk into how we enable it. It's
rather simple.
But it was
uh this is decision we took. So, don't
expose a company's data to API unless
they give consent.
They the endpoint are also slightly
different
but besides from that it more or less
work the same.
And I also think
we will try to improve that experience
for the on-prem and access
the endpoint.
in the near future
time frame.
Oh, yeah.
So, our APIs the naming display name for
instance we are in review with the graph
team. We go to every field explaining
what it do and we talk about how it
should be named.
Oh.
Were you talking to enabling endpoint on
Yes, thanks
so.
Basically
for enabling APIs on prem as you already
heard the API is disabled by default.
There was a lot of discussion should it
be enabled or disabled but we felt that
it wouldn't be right that we enable
something out of the box so users might
be sharing more than they wanted.
Because this list of the data that we
share is quite long.
And
it's very easy to set up the APIs on
prem so you just need to enable the all
data web services
and then in the administration console
or in the config you just need to change
the enable API services checkbox.
There is an action in UI that you need
to run to make sure that all the data is
set up and you need to set up templates.
So, these are the four steps that you
need to do it.
So, I'm going to demo how to do this.
So
in short in the server config here which
is this is more geeky way of doing this.
You just need to flip this value
to true.
And now I would need to reset the
server.
Oops.
So, let's go to the services.
And if I find Microsoft Dynamics
NAV server, so I just need to reset it.
And while that one is happening,
I will just start the
Windows client that I have on my box.
Oh.
Yes.
It's still working.
It is.
Cool.
And now the server is cold, so it will
take some time to load.
And uh really good thing about the
Mhm.
So, it looks like I haven't saved the
URL, so I'll have to wait until it
loads.
I did I No, I didn't.
So, let's just wait until the client
loads.
Do do do do do do.
Hopefully, this will warm up the server.
And now if I go to the API setup
page, and it's here.
And this is the page that you need to
use for setting up the APIs.
Uh the first action that you should run
is this one, which is called integrate
APIs. And this action is going to go in
the background and generate a lot of
integration records, fixed references,
and navigational properties. So, it
might be a quite lengthy action to run.
So, don't do it during the office hours,
definitely, because it is also locking
some records in the tables.
And the second thing that you might want
to do is that you might want to set up
templates.
And here you can see the
uh rule pattern that we have applied.
So, if you would like to specify how the
customer templates should be applied, we
are going to follow the order. So, when
you give a JSON to us, we'll look which
fields you have specified in the JSON.
And then we are going to iterate through
templates one by one trying to find the
first one that matches the criteria.
So, here you can see that I'm applying
the foreign template for everybody who
has a currency code different than UK.
This is definitely wrong. It should be a
country code.
Otherwise, I'm applying a domestic
template to the customer.
And now just to like because we have
enabled it,
to get the URL, you just go for the web
services.
And we wait for this one to load.
Come on.
And here you just take any URL.
And then you just delete a lot of stuff
here.
All the way up to the NST, you type API
beta, companies.
Yep.
And because we're running on prom, you
can delete all of this stuff.
Since this tenant is configured to use
the
Windows authentication, so I don't need
to specify anything. And if I just
execute this request,
it should return soon.
Yep.
So, this is the quickest way to get up
and running. So, if you just install
your
box and you flip this Boolean and use
Windows authentication, you can use all
the APIs. As you can see, I managed to
get the companies back.
And if I just fetch one of the company
here,
And I do a post request.
And I just provide a display name here.
And I execute it.
Yep, it was successful.
So, just under which company did I run
this?
I picked first this Cronus Canada.
It's important to pick the company
because otherwise then it's going to end
up in a different place.
And if I filter here for the name,
you can see that my
customer got created.
And you can also see here that the
template should have been applied.
So, you see we got payment terms code
and everything else automatically
applied from the template.
And because we have a cool templating
system in the background, even the
dimensions were transferred. Oh,
actually they were not. Sorry.
They should have been transferred as
well.
So, I have a bug in the set.
Sorry for that.
Yep. So,
Annes is going to take over from here
and to show you how you can develop your
own APIs.
Perhaps I should take this one here.
So, I'll just take a small sample on how
you can build or how we have built some
of the API pages,
what property you need to set on the
pages, talk
a bit into complex type, and give you a
short example of how you can make a
bound action.
And to do that, I will use
a box with my favorite
tool on.
I have it here. Yes, mhm.
There we are.
Yes.
And let's see.
So, I prepared a little
example here trying to build
a bank entity.
Not rich on field, but
again,
and isn't it just cool that we got this
feature in so you can see it both what
I've changed from default, so it's
pretty simple to see here.
A name, a caption,
a page type,
reference to a source table,
and of course, we need to delay insert
because we get the full record and
therefore we do need to have that
property set.
And then just specify what is the
external OData key that we are using.
So, that will be the primary key from
the external from calling the API.
I have exposed here
the standard field number and name. Ah,
I should have written display name,
sorry.
And I have what I call here an address
JSON.
And if I go into the code,
so I need to do when I get it when I get
my record, I just need to fill in this
complex type and luckily
we have components size and have a way
to do that using a library here.
So, you get the address, address to CD,
county, country region, postcode.
Put into a JSON in the standard format
we agreed on. I'll show to you later
shortly.
Of course,
this is when getting.
If we also need to
Damn, it wasn't down here.
We should not play the round.
Set.
So, you can set it or you can get it.
So, here if we need to update it, so if
the user have made a post request,
it is almost similar. We have a little
helper function where we pack it into a
JSON and then we can show it in the
response and we are good there.
One thing to be aware of however, if
you're using those complex type
that you need to specify on the field
a OData EDM type.
We have a few available out of the box.
Yep.
Uh EDM any part.
Yep.
But, you can also build your own.
Oops.
Did you warm up the server for me?
Yes.
Thank you.
So, actually if search for this page to
see the predefined EDM type that
available.
And down here I have the
the post address.
And
you can see here how it packs it up and
make this normal this beautiful street
address
county country
as an example.
The bound actions
they are equally simple to create.
I have it up here.
You need to create a function.
I think this is the one that it's right
here.
It just need to be visible and also have
set service enabled to true.
Nothing magical there.
So, in this little sample I will not run
the code here in interest of time.
I when I wrote this in action I flipped
the phone number to something else. Do a
wrong do a modify of my record.
And then I set the response
to this here with the action context and
I actually have it there
where I say the key the number
and the page. I should have used page
colon colon bank account for the beauty
nest, but again, just it is not magical
or complex to make to make to implement
bound actions. It's just slightly
different. And the good example inside
our NAV 2018, you can just look up the
the quote or the invoice where you can
do a make make an invoice based on the
code and post an invoice.
Cool.
So, let's flip over here, too.
Thanks, Anders.
So, the last topic that we have for
today is our design patterns, and we
have very little time left on clock. So,
my apologies, but I'm going to go a bit
quicker through them. Rapid. So, we
prepared four of them, and we will also
be discussing commonly made mistakes.
So, when you see this logo, it's a
tripping point where many developers
have tripped.
So, an open question for you all of you
guys. How do you measure code quality?
So, most likely you have heard many
metrics like cyclomatic complexity,
churn per line of code, but the only
measure that really really matters
is the WTF per minute. And you measure
it like this. You get the developers in
the code. You give them a code flow, and
you measure how many times they're going
to say like, "WTF?"
Right? And the good code generates a
little.
A bad code generates a lot.
And this picture is so good that we're
using it for the second time.
And there are multiple levels of WTF.
The first one is what? The second is
why? It's component level. And the
ultimate level is when you're so
outraged that you're going to spend your
time to figure out who wrote it, right?
That's the ultimate level. So, we can
introduce the couple of WTFs with the
OData stack. As you saw, Anders showed
you that it's quite
quick to implement an API, but the devil
is in the details. So, when you hit some
APIs,
it's going to become hard.
So, the first pattern is the shadow
table, and this table is physically
aggregating two tables into one.
So, for all of the sales headers and
sales invoice headers, we have
duplicated them into the sales invoice
header aggregate.
And basically, the problem that we are
facing is the data is split into two
tables. And this would force us to split
it into two APIs, like draft sales
invoices and sales invoices.
But, the flow would be horrible. So,
first you would have to check if it is
in the drafts or is it in the invoices.
And if it's not, you should guess it got
deleted, right?
And basically, all of the non-NAV
developers would say, "WTF does right?"
Because no service in the world is doing
this.
And yeah.
Then, you guys, when you would start to
use this API, you would think it sucks
as well. And everybody would agree on
that.
So, simply, it was a no-go to split it.
First thing that people say when they
hear this problem is, "Let's base it on
the temp table."
And this is really a horrible idea.
It's really a horrible idea.
Why?
Because you're going to end up in a
world of pain if you do that.
So, never ever base an API call on a
temporary table if it can return a large
number of data.
And we all know that you can have
300,000 invoices in the system.
Why? Because of performance. You have to
load all the records no matter what. If
they are filtering, you have to load all
the records.
Then, continuation tokens, like paging,
is going to be really problematic. And
filtering together with the continuation
tokens is going to be a nightmare.
So, don't do this.
For the sales invoices, it is not okay
to base it on the temp on something
which returns a small number of records,
like tax setup.
It is okay to base it on the temporary
table.
So, we have pre-computed all the values,
and we have stored it in the shadow
table. And this is has also helped us
with the performance because
calculations are expensive. 30
milliseconds thousand times thousand
invoices, it's 30 seconds in the best
case.
And you know, like if you're having a
bad day, it's going to be 40 or 50
seconds, and no user is going to wait
for the API to return.
So, and the graph is forcing us to
return within 200 milliseconds in most
cases, otherwise they will fall move us
to the asynchronous API.
And you don't want to be in the
asynchronous API, according to them.
Uh they said it to me in such a way that
I didn't dare to ask why, right? So,
we're really aiming not to be over 200
milliseconds.
The shadow table works with the global
subscribers. So, each time that a change
happens to the sales header or related
records, we just duplicate it into a
table that is in the NAV.
When you're inserting a record from the
API, we are propagating the inserts to
the main table, and we are exiting with
false because we don't want to end up in
the loops. We always force the main
table to update the aggregate itself.
And for the fields, all of the aggregate
specific fields are having numbers
larger than 9,000. And this is really
cool, because now we're not growing SQL
row size, which would hit you with your
implementations, right? Then you would
have to either choose are you going to
implement LS Retail or APIs. So, we're
putting all of the API specific fields
in a separate table.
Yep, so I managed to say this, and be
very careful to enforce read
permissions, because aggregate is
exposing two tables. So, on open page,
filter it out.
Yep, so consistent data is duplicated.
Read permissions are hard, we get
performance not increasing the row size,
and we can change the flow from the
proxy. So, that's really cool.
Then the next pattern that we can
introduce is a register field set. And
just explain it briefly, here on the
left I'm trying to create a non-taxable
customer, and on the right I'm trying to
create any customer.
But the problem is that it ends up with
the same data set, right?
And then the insert trigger will set
taxable to both.
Because it doesn't know what have you
specified. And in the first case it's
wrong because I wanted a non-taxable
customer.
And in the second case it is correct.
So, we couldn't fix this one generically
because in some cases we should throw an
error, in some cases we should auto
validate, and in some cases we should
enforce the set value. So, we need to
code.
And order of the feed fields on the API
page is very important because they get
validated in this order. This is not
like a regular page.
And the solution is that we decorate all
the fields with register field set, and
then we try to set them back if you have
specified it in the request. We had a
code review meeting, we all agreed it's
a hack, so we are going to get a proper
platform solution for this one.
The next pattern, which is not really
that good, is the integration IDs. This
is a system which is 3 years old. It's
been used for the first CRM integration.
And in the integration table we are
storing all of the integration record
IDs.
So, all of these IDs that you saw in the
demos are coming from this table.
You can search in the object designer
and they're being used for all of the
APIs and all of the integrations that we
have.
And
uh this is not really a good solution.
And if you'd like to see how it runs,
the source point is the code unit one.
And child entities, they don't have an
integration ID. They just update the
parent. So, a sales line will never get
an integration ID, the sales record will
have an integration ID. And when the
record is deleted, we blank the record
ID on the table.
Never delete the integration records,
you're deleting the history because when
you ask the API, we will give you that
the record was deleted. And also when
you ask for the deltas, we'll use the
integration table to tell you which
records got deleted in the meantime. So,
never ever delete the integration
records. That's also a mistake that
people make.
The biggest problem with this system is
very fragile. So, if somebody deletes
the integration records, we have lost
the data and this is not the way to do
it. We are also causing locks on the
tables, which is harming the
performance.
So, we need to get a proper platform
solution for this one and it's in the
queue.
And for the last pattern, we have these
temporary tables.
So,
uh basically, if you have few records,
you should use temporary table because
it is way simple to modify.
And this is an important consideration.
You will see this that we have coded on
find record
and you're probably going to be thinking
like WTF.
And the reason for this is that the web
service pages are behaving differently
than the regular pages.
And currently, the page used to close
after on open trigger. So, if you would
load it on open page trigger,
the page would close and reopen, so we
would lose everything that we have
loaded on temp.
But it doesn't close on find record, so
we have coded it there.
So, yeah. Uh also, it is in the plans to
fix this so we don't open close the page
multiple times.
The OData page can behave differently
than the regular page in the future and
maybe by design because they're serving
two different purposes and the different
code gets executed.
Yep. And the cons for this approach is
that you have to transfer data yourself
to the physical tables and you have to
make sure that the data set is small.
Yep.
So, honestly, should I take this one
quickly
or William?
Yeah, let's take it quickly. Oh, I can
just
So, I think Nicola earlier said that
media right is going into the depot as
we speak, so to speak. It will not be in
NAV 2018, but in
in Tenerife or so. Delta support,
imagine you you have fetched all the
customers from the service and now you
just want to see give me what have
changed since the last time. That is
also being worked on. Webhook advanced
filtering, extensibility
of the APIs, the standard APIs, and the
capabilities of not only have our
namespace API, but have a namespace
called API custom. So, you can have your
own custom namespace.
And then we will add a few APIs, perhaps
something around incoming document going
on if that can please you a bit.
With that being said, I think we should
jump directly as we skip the last 100
slices.
So, yeah, we can skip this. The only
slide I would like to show is the last
before the end.
So, yeah. Basically, this is very easy
to learn. So, start using it. If you
don't have I would really recommend that
you learn this.
So, if you the next steps, you can get
this is a link to get started with the
APIs. And we are really looking for your
feedback. So, so far we have been
proactive. Now, we are switching to
reactive mode, and all of the APIs and
the addition that we do are going to be
based on your feedback. We already got
the feedback that on the sales invoice
we didn't expose the external document,
and it's mandatory in many cases. So, we
just quickly fixed it.
So, if you would like any fields or
bound actions, make a request and we'll
start doing it. We are not adding
anything without a specific request.
And start building connected apps.
Yep. So, questions?
Yippee. Here you are.
Is there a good question?
Um
Yep.
Yes.
Can we expect to get a base 64
conversion field
in the user card
below the current one because you
converted this with your tool
to base 64?
yeah, that would be a nice to have
thing, right?
Yeah.
Yeah, sure. Sure. We could do that, too.
because otherwise I always have to copy
Yes, we could do that. That's that's a
good suggestion. Yes.
Yep.
Thank you.
Yep.
Next question.
Yeah, up here.
What?
I have seen you down there.
Yes.
Hello.
Thank you.
Um
We have one in the queue up.
I was wondering if there's going to be
enough 2018 in December. Then on the
road map, there's also enough 2018 R2.
And after that, there was Tenerife for
on-premise.
Is the API also going to be available in
one of these earlier versions or is it
only
on Tenerife?
The list that you saw here of APIs
available, that's 2018.
Okay.
Yes.
So, in December we can enable the check
mark.
Yes. So,
That's and we have a question there and
then one in behind here.
Yes, sir.
Yeah.
One is
like will you going to keep supporting
sub protocol?
Yes.
And
another one is like when you post
when you use the post command, are you
going to record the
user ID?
Are you going to so?
Record the user ID who posted that
invoice.
Yes. I mean
if the air logic is doing that, that is
going to happen. And if you override it,
then no.
like if you use a
web key,
Mhm.
then how can you record that who posted
that particular user?
APIs running as the user, right? So, if
you are doing any logging, it's going to
automatically run. If you're not doing
any logging, it's not going to be logged
and it's simple as that.
Okay.
Yeah.
So.
Yeah.
So.
That's the benefits of running it as a
user, right?
But it also has its flaws.
Yep.
Then we have a question there and
to ask what will happen now if I
create page in modern development
environment with Visual Studio Code and
use that type API
You cannot do that. It will not compile.
I okay. Thank
Because like if we would allow you to do
this, then you would have to keep the
same SLA as we do and you would have to
go through the graph review. But that's
why we are considering introducing a
custom endpoint where you could publish
your own API pages.
So, in the future it will be possible.
Yes, because we are looking into two
extension points. One is the custom
endpoint, and the second extension point
is open complex types. Open types,
sorry.
With open types, you can just attach any
data to the generic API. So, you like
you could post anything.
And then maybe in the subscriber you
could handle it through the extension.
Thank you.
Yep.
And then we
Will all the new functionalities like
batching also be available
features.
Sorry. Okay. Patching? Patching?
The batch processing will it be
available on the on-prem version as well
or only in the API that you are exposing
on the cloud?
Everything will be available both
on-prem and in SaaS. The only thing that
differently that's the endpoint of
indication and that stuff. So.
Okay. And one other question.
Yes.
Um if we deactivate the API version, uh
the API functionality, will the tables
that you have, the aggregation table and
the unique ID table still run or will
they just be deactivated because we
don't need them?
So, the question was when you enable the
API settings, will everything run? I
think you if you follow those steps that
that Nikola explained here, you will be
you will be safe there.
Okay. No, but if we deactivate it, it
will not run, right?
Like if you wanted to save system
resources and we don't need the API, can
we deactivate it and then not have the
the tables run, the aggregation table
for example?
If you activate it and all that, the
table will run and they will be
maintained.
You have to do something to turn them
off.
Which you can with a little key.
Uh sorry, but we'll also take the Q&A
afterwards. So, yes, question.
Yeah. So, my question is about the post
post web services.
So, when we want to write something to
the database, like create a record
or modify a record,
we need to do it field by field or how
how exactly? For example, if you
You just specify. That's a good
question, basically. So, if you would
like to modify multiple fields, you just
include them in the JSON and you push
all together to the web service.
Okay. Is it going to do the validate for
all the fields or
Yes. So, all the fields that you specify
in the payload are going to be validated
in the order that they are appearing on
the page.
So, that's why the order of the page on
the web service, the fields, is
important. So, when you're coding your
own OData V4 service, make sure that the
order of the fields is correct.
It is the same as you have a user
experience inside NAV. You normally on
the order validate from left to right
because otherwise we screwed up earlier.
We control this now, but that was the
user experience.
Yes.
So,
one more question. For example,
I want to I want to call my I want to
create my own function, action,
Okay.
and I want to call it, but I want to
pass some parameter to it.
Yes, it has to be unbound.
Sorry?
It It will have to be an unbound action.
So, it has to be a code unit.
Yes, correct.
And to the code unit I can pass a
parameter.
Yes, you publish the code units. So,
basically, if you would like to see how
the unbound actions look like, we didn't
demo them because of the time. You can
just simply go to the web services page,
see the exposed code unit, and just go
into the C side and see it. It's just
global functions
Mhm.
with the variables on top.
So, in the function itself, you define
the variables, you define the return
type, and it gets published as such.
And as many functions you have, as many
methods you will have exposed.
There's a lot of opportunities. You can
also create your magic table and you fit
certain
set of values inside that. You run this
code based on the parameters that was
given. So,
Okay.
it is only imagination that
This is available only in all data for
Yes.
Only on data before.
And all data for is available only in
NAV 2017.
So, this is available only on NAV 2018.
Okay.
Yes. Because you have to take into the
consideration when was the platform
functionality implemented, right?
Oh, damn.
Did you something?
Oh, sorry.
Yep.
So, we have a question here.
So,
Yeah, we have one.
The question was
is it
dependent on the JSON, the direction of
the parameters, or on the page?
On the page.
You can specify whatever you want in the
JSON.
Okay.
So, it doesn't matter.
Yep.
So, one more question and then just
approach us and then we'll answer
everything.
Um yeah, you showed the
the the downloading of the binary data
and you got as a result result you get
the media link. Is this a dynamically
generated link for every uh
No, you can you can just go to it. I'm
not sure if you saw the structure,
but the structure is always the same.
Okay, so if I if I
if I have a request for a two requests
for the same picture, I get
You don't you don't need to do that.
Yeah, if you do the two requests for the
same picture, you'll get the same
picture.
So, if you know how to construct the URL
by yourself,
Okay.
you can by all means do that and go
straight to the picture.
And you showed the the the invoice, the
PDF. So, is it was it the actual PDF
that was printed when posting?
So, the the PDF is the one that we
generate. So, under this API we will
generate it.
But basically because we don't store it,
so it's the same as clicking print from
the posted invoice, right?
Yeah, but then the the the the the the
the media link is just temporary because
if you just
Uh but the URL is always the same,
right?
Okay.
So, you're safe on that.
Yep.
So,
One more question. Okay.
new material, is there any plan to put
together an overall documentation
package that's got everything in it,
even if it's just online?
So, yeah, basically we have
shown you two links today. So, there is
the first one which is called
aka.getstarted.
Mhm.
And there is also generic graph
documentation that we have. So, around
all of the APIs that we publish. And
there are many articles as well that are
covering the getting started, too.
But is it all I mean like the old days
used to have these manuals and it
I don't know if we have the equivalent
of that online where we have it all
together and everything just kind of go
through and
It It should be like that. Yes.
All right.
Yep. It should be like that. And provide
feedback if it is not good enough.
Okay.
Yes.
Thanks.
That's very impressive.
Thank you.
So, thank you all.
Thank you.
And if you have more questions, just
come down. Yeah.
