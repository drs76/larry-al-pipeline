# Microsoft Presents: What's new in AL language - Enhancing Your Development Experience

- **Source:** https://www.youtube.com/watch?v=cHfGSMWCRKI
- **Video ID:** cHfGSMWCRKI
- **Channel:** mibuso.com
- **Published:** 2025-10-02
- **Duration:** 48m36s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

So let's start on this second uh second
part of the presentation here about the
AL language. Uh I saw a lot of hands
when you saw the BCLE. So you most
likely saw me talk about all the
different things that we added. We are
going to scale a little bit down here.
Uh with me I again have Balash and we
also invited Espen. Uh so we're going to
talk a little bit about the changes to
the language.
Um the language changes that that we
introduce come from your ideas from BC
ideas and they come from the feedback we
get from the service on performance and
other things and get comes from the new
feature development that the the team is
doing. So we get a request from one of
the teams that want to introduce some
new language features.
One of these might be good, but it's
best when all three of these come
together when we try to solve a problem
you guys have and the service has and
the team has. So those are the kind of
the really good ones that come in and
sometimes getting ideas from all of
these different sources leads to
something completely different but
there's actually a better idea than each
one of them by themselves. Let's talk
about some of the things that has
happened in the last tech days. It's not
going to be a comprehensive walkthrough.
As I said, I'm talking a little bit
about some of the language constructs,
some of the enhancements for maybe
reducing the amount of code that you
have to write or making the code more
readable. For some, for others, it might
not be readable, but let's talk about
that. And then we're going to talk about
the the testing that we've added, the
ability to test using HTTP client
mocking. And finally, Espen is going to
take us behind the scenes of some of the
tooling that we're working on that we
might get in the future. Okay, let's get
started. So, I needed to create this
demo. So, naturally, I would use what I
would use copilot, right? So, I am using
the VS code agent functionality. And I
asked Claude, you might ask me why I use
Claude and not GBT40 or some of the
other models. Well, you try them out.
You figure out which one works for you.
And in this case, the cloud one was the
one that gave me the best result, the ro
result I actually wanted to present
today. So, I wanted to build a flight
manifest with some passenger
information, crew information, and so
forth and an example of it. And I love
to share my bad code. So, this is my
prompt.
Yeah, you don't need to read all of it.
It's in there somewhere that I want to
do a flight manifest. Um, the point here
is that it took a little while, but
actually it's not that big a prompt.
Some of the prompts that we see have
lots of meta descriptions and system
parts and all sorts of things. This was
just me tinkering around, right? Okay.
So, it gave me a lot of things as you
can see here. It spewed out files right
and left and it gave me a nice overview
of what it did. And me being me, I
wanted to see that in a different view.
So I asked it to create a class diagram
in Esiad, right? Old school. So you can
do a lot of things with this agent and
this co-pilot. It's a wonderful tool to
help you get overview and get structure
on on your next thing to do. So the
question is, did it work?
Who of you think I messed up and it
didn't work? Let's see it. Oh yeah,
you're so full of trust.
Okay. Okay. Well, actually, you're
right. It um it didn't work, right?
No, of course not. Of course not. No,
there was there was 12 errors.
That's not too bad, right? 12 errors.
Well, actually, I think it actually
worked cuz it gave me a head start. All
the things that I didn't have to do,
right? all the simple implementations,
all the finding the the property names
of all these things and setting the
methods and whatnot. It did all of that
for me. It gave me something to start
with. And I think it's quite cool that
if you use the wordings that are well
known like a builder pattern here could
be an iterator pattern, a mediator
pattern, a visitor pattern. If you use
those words,
the copilot will extract extrapolate
quite well to some code that is quite
nice to use in your applications.
Okay, so the outcome of all of this is
that yeah, we'll fix the errors in a
second. It's not going to be a big
problem. very few and minor errors.
Maybe I need to learn a little more
prompting. That might also be part of
it. Or if you can see the small blue
writing here, maybe I need to read up on
the co-pilot customization. So adding
some rules to my co-pilot experience
where I maybe put in some uh coding
guidelines or styling. Those of you
who've seen the BCLE probably recognize
that I am prone to using Pascal case
rather than some other casing. So maybe
I could put that in the the prompt rules
or the customization here. Okay, let's
see some code. Right,
let's go here. Okay, so this is my code.
Yes,
let's see if I can get to it.
No.
Yeah, same problem every time and I keep
forgetting. There we go. Okay, so this
is my code. These are the 12 errors I
have down here. All nice. It leads me to
the first problem, which is it's trying
to exit uh code unit manifest builder.
Okay, what does it want me to do? It
wants to return an instance of the
manifest builder code unit. So that
allows me to talk about the first
keyword that we introduced not too long
ago that this keyword. So the ability to
reference your own object yourself a
self reference. So I can actually use
this here instead of returning the code
unit. I can return this.
So let's do that right and just replace
everything here with this.
And voila,
we should be down to come on four
errors. Haha, this is easy. Coding is
easy, right? Okay, so the this keyword
is actually not only just for self-
reference. Well, that is what it is. But
you can use it in many other scenarios.
We can do
uh some scoping scenarios here. Let's
see if I look at some code like this
here where I have a parameter with a
variable and I have actually also a
global variable here. So the names are
the same. It's allowed. It's valid
syntax. There's nothing wrong with it.
And if I go and hover over here, I can
see okay, I'm assigning a parameter to a
parameter. Okay. I can also see here by
prefixing it with this I will actually
say well I'm using the global variable
instead of the parameter. So this is a
way to scope what I'm actually trying to
sign here. Okay I can do the same thing
for the the variable. I have a local
variable here local variables assigning
a global variable not very useful. I can
qualify it here by putting this in
front. So the global variable is going
to be assigned my local variable. Okay,
this is maybe a bit sought after, right?
Because who would name the local
variables the same as the global
variables?
Well, it happens, right? It's out there.
But I think the the most important thing
here is the ability to see from the code
that you're actually looking at a global
variable, especially if you have 50
lines of code. There you can see, well,
this assignment or this use is from a
global variable or a local variable.
That's quite powerful just from looking
at the code without knowing where it is.
Okay, I can use the this keyword in
other types like pages and tables and
whatnot. And I can use it for for
example referencing a global field in a
page field. Nice. And again inside this
page I can also use it to reference a
global global field in my procedures.
So, it's there to be used as a way to
make it more readable the code. And of
course, we saw before the self reference
in the manifest builder, right? So, why
did this AI generate the manifest
builder like this? Well, that's because
it actually writes the example like
this.
Some of you may easily recognize that
this is a well-known way of doing it in
other languages. So you dot your way
around when you do a builder. Others
might prefer
something that may look something like
this instead
where you specify the instance every
single time.
It's not going to change anything. It's
going to be the same thing. And in my
opinion,
this one up here is more readable.
Again, opinions. Okay, let's move on to
the next error. So down here at the
bottom we have some issues with some
date times for the departure time. Okay.
So this allows me to introduce another
enhancement we've done here to make code
easier to read. Instead of us trying to
convert this here we can actually do it
directly without getting the token
without getting the value. So we can
write JSON object.get
get and we can see we now have the
ability to get the type that we want
from this making it simpler to write
such code. So I can do get date time and
I can put in the date time here. Copilot
suggests me some that it may be right
but not quite.
So let's close that one. So that will
give me the departure time and then I
just need to put it into this. Let's
just write it. You all like when I spent
10 days on writing a simple statement.
So let's do that. Set departure date
time.
There we go.
So one liner here
means I can delete all of this, right?
Well, maybe not. So the first thing we
do in this line here is check whether
the property is even there in the data.
If I try to just use this one right now
without the data being there, it will
throw an exception. Right? So, we added
the ability to specify that you actually
want the default value for this data
type if we don't find the property.
So, just by setting this boolean flag, I
can now test that it's there
without testing that it's there.
So, I can now remove all of this. Yay.
Less code. You like that?
Okay. I could do that for all the other
ones. And let's go see if I did that
because I have so many versions of this
project.
Uh, so I did that here. So, you can see
instead of having all the if statements,
I just said it d and then we have read
the data.
Okay.
Let's see. We want to do something with
this work here. Let's see. I have my
example here and uh it's printing out
the totals at the end of the the
document or the end of the function
here. What if I want to know how many of
my passengers are actually employed by
the airline that has a special term?
Does anyone know what that term is?
I find it quite funny. It's called a
dead passenger.
I don't know why I find that funny, but
I do. So, it's called the deadhead
passenger. So, I could start by adding a
new file and a new interface maybe that
will implement the deadhead passenger.
And of course, I want all the
information from the passenger. So, I
would have to inherit
extend the passenger interface. So, we
added the ability to do that. And
actually what I did was I asked
co-pilot here say hey implement the
deadhead passenger
extending the passenger interface. Okay
and it actually did that. So that gave
me this file
and we can see it extends the passenger.
So you can use the extends functionality
to extend and add additional data to a
to an interface or maybe you want to
have a new version of the interface or
some other reason for having additional
methods on an interface. So you can do
that using the extends. Okay, I want to
use this. So, I'm going to go back to my
example here, and I'm going to
do another function that does Let's copy
this one
and say the dead head. I love that word.
It's a nice word. And we of course want
a new function for that. So, we want to
do a get dead head passengers,
right? So, all of that I'm just going to
implement. It's going to be nice and
easy. But let's uh let's take a look at
the code actually. So
and manifest here we go. Okay, here's my
implementation. And before you go into
details of it, let me take them one line
at a time, right? So the first thing is
I I named the return value just to make
it easier for me to to uh to use it. But
we'll see that we are able to return a
list of interfaces
which is quite nice. So we can actually
now support list and dictionaries of
complex objects like code units and
interfaces.
For those of you who have been working
with collections of interfaces or code
units, this has been difficult,
but now it's quite easy. So you can just
add a whole list of them. And of course
with a list, we want to do a simple for
statement. So we want to go for one to
whatever passengers we have. And the
first thing we want to do is figure out
whether this passenger is a dead head
passenger. And it is as simple as that.
You just ask is the current passenger in
this list a dead head passenger using
the new keyword is.
Those of you who've worked in other
languages might find that familiar. That
is the way you ask if something
implements an interface.
Okay. If I know it influence a dead head
interhead passenger interface and
I do not want those then I or I do not
want the ones that does not do it then I
can use the new keyword continue to skip
this item for this iteration. So for the
innermost loop that I'm doing here I can
skip. So it'll go back to the for
statement and take the next item in the
list. Anything below the continue
statement will not be executed. And
we'll go through it again and see if the
next passenger is a dead head passenger.
If it is, then I can actually use the
keyword as to do casting between the I
passenger interface that's in the list
and an I deadhead passenger that I have
extended.
And from that I can now get the dead
head reason and say that if you're in
training, you are not an employee yet.
So you cannot be counted here. Finally,
I add the deadhead passengers. So using
the is keyword, I can test if an object
implements the interface and using the
as keyword, I can cast that to the new
interface.
Okay. If you do not test whether an
object implements the interface you're
trying to cast to using the as
statement,
you will get an exception. So you need
to make sure that the thing that you're
trying to cast actually implements that
interface.
Okay. Now let's talk about sending this
data somewhere else. So the this
specific
this specific uh customer that I have
wants to send some data as JSON. Okay.
And I can go here and I can see that
we've built up a nice manifest here.
I need a little bit of water here.
And here I see that we have the
departure time formatted as 0, 9.
Everybody in here knows what that is.
Yeah. Oh yeah. Two people. Three, four,
five. Okay, that's good. I think
everybody knows. H I want to introduce a
simpler way of doing that. So I can do
two text. two text has been added for
most of the simple types allowing you to
easily convert the value you have into a
string. You can u you can use this as
just two text which is the normal
format. But if you want the 0.9 oops
if you want the 0.9 formatting you need
to use the invariant. So this is a
parameter here
invariant. So I put in boolean true
here. That would be exactly the same as
doing 0.9
or 0, 9. Again, doesn't change anything.
It can make code more readable. It can
make code different than what you used
to read. It's just a different way of
doing it. Okay. Now, I want to make sure
that whenever I send information out
about my passengers that the the
information about their name is
anonymized. Well, for some times I want
to send it out to some systems
anonymized, some systems it shouldn't be
anonymized. So, let's go and add that
ability. So, let me go and check this
guy here.
Yep. So, if just go back to this guy.
Yeah. And I'm trying to get back to it.
You see, I added a parameter allowing me
to anonymize the JSON that I'm grading
and I passed it on to the passenger
toJSON function.
So here, let's see if I can find that
button.
I need to add the anonymize. So do that.
And I can never spell to this.
There we go. Anonymize. Okay. Now for me
to anonymize the name it seems quite
simple. I can do an if statement here
saying if anonymize whatever then we do
something different than we used to do.
Maybe we put in redacted uh instead of
the actual name.
But what I can also do is use the new
turnary operator to just put it in here.
So I can say a boolean statement if that
is true then we'll return the redacted
and then colon as else we'll return the
get name.
So this is a very shorthand way of
writing if then else. The turnary
operator allows me to specify a boolean
expression. What happens if it's true?
What happens if it's false? Now, as with
great powers comes great responsibility.
Imagine you have the need for it to
return some cases first names, some
cases last names, some cases uh first
name first and last name last or the
other way around. If you use a turnary
operator for this kind of inline if
statement, well, you can guess it's
probably not going to be very readable.
So use with caution but it can be used
and you can format it in a way where it
actually looks like something you can
read. Okay, this uh this requirement
here also uh says that I need to change
the structure of the document that I'm
sending out to be a little more
complicated. Um I'm actually uh looking
at adding a little more data and adding
a little more different kind of objects.
I could use the the JSON object here to
build up that or I can actually just use
a a template. I can even build it into
my
into my function here using the verbatim
string the multi-line string. I can
build a string that starts with an at
and then the string begin and it ends
down here somewhere and everything in
between including line feeds and what
have you special characters will be
included in that string. This is quite
readable quite easy to to change if you
want to change it in the future. And
again I can just use replacement here
and that's how easy it could be. I could
also move it to the resources right
balas. Yeah could be doing that. So now
I'm ready to send it out to somebody
else. I want to test that integration.
So Balis, can you talk a little bit
about that? Sure thing. Thank you,
Stefan. Let's see if we can open this
up.
All right.
So
perfect.
Okay. So uh how many uh of you have had
to uh integrate with some kind of uh
external service in uh AL before?
Yep, quite a few. Uh great. So uh
testing these integrations before has
been uh quite a challenge at least uh
for us internally. Uh sometimes even
requiring setting up a mock service and
uh rerouting requests to be able to test
these integrations.
uh with the implementation uh with the
introduction of the HTTP client handler,
those challenges are all in the past. Uh
this new handler allows you to intercept
HTTP requests that are sent through any
HTTP client and uh mock the response for
these requests all within the AL
execution without ever leaving the AL
boundary. Um using this new feature uh
you can develop tests that do not rely
on uh on external services. You can uh
test the um how errorprone uh your code
is, how well it can handle different uh
response messages and uh it can allow
you to u make the test execution more
efficient by not having to invoke an
external service.
Um, also I reckon that most of you at
some point have had to deal with JSON
objects when working with web requests.
Uh, and we have also enhanced the
tooling around JSON objects uh to make
it simpler and more robust with a few
new utility methods as well as the
ability to embed secrets into JSON
objects.
uh to showa to showcase some of these
improvements and enhancements that we
have made around the test tooling I've
created a small demo application. It's a
bit simpler than Stefan's example. Uh
and it relies on an external service
that I am currently just hosting on my
local machine. Uh this external service
has two simple endpoints uh SL token
endpoint as well as a uh slash products
endpoint. The the token endpoint can be
used to fetch a token from this external
service and the products endpoint can be
used to get the list of products or one
specific product if we specify the name
query parameter. Then jumping into the
AI side which you can actually see on
the screen um
I have a product provider middleware
that calls into this external service
and respectively it has three methods.
one to fetch a token, one to list the
products and one to get a specific
product. And just for the sake of
visualization, I have also created a
list page that utilizes this product
provider
and it has the two actions to fetch a
token and to list the products. So first
we can fetch the token. It actually went
to the external endpoint and got a token
from it. And then using that token I can
go ahead and list the products. I can
see that uh the external service gave me
four uh products uh and information
about them. Specifically the name of the
product, the price of the product as
well as the category of the product. So
uh now let me go back into the code and
show you how you can test this uh
product provider middleware without ever
invoking uh this uh external API or
service.
Uh so first I want to go and test the
list products method for this. Um
yeah, I've created a test that just
invokes the provider uh and then uh
verifies that the result is correct. Um
to be able uh to uh intercept the
request and then mock the response for
it, we first have to create a handler
method. To implement it,
we have to define a procedure first
which has a test HTTP request message
and a test HTTP response message as
arguments
and then we have to decorate it with the
HTTP client handler attribute. As the
name suggests, the request contains
information about the intercepted
request and the response can be
populated with the desired values to
simulate any kind of response that you
want. Um, in the case of the list
products method, I want to attach the
list of products, the content, the JSON
content to the body of the response
message. For this, I can in a very ugly
way create this uh text variable that
contains all of the four products.
And in the end, I can just write it to
the response content.
To make sure that this handler is
actually used when running the test, I
now have to just add it uh using the
handler functions attribute to my
original test.
Um, so functionality wise this works,
but it's not the most beautiful. So to
make the code much cleaner,
I can go ahead and use the multi-line
string in combination with some of the
new JSON utility methods uh to make it
much cleaner and more readable. So first
things first uh just like Stefan did
before I've created a verbatim string
uh of the product template which uh
contains some placeholder values for the
name, price and category as opposed to
uh formatting it using the percentage
sign as we have seen earlier. then I can
convert it. I can read it into a JSON
object and then replace the name, price
and category properties of this JSON.
Finally using this template
I create the response message
uh I create the response body and uh
attach it to the to the response
message.
It is already much better. But we can
make our test even more datadriven
if we extract the product details into
some kind of structure structured
language format. For the sake of
variety, instead of using a JSON, I'm
going to be using YAML because now we
also support
reading from YAML format. So I can go
ahead define a JSON object uh and uh
read the product details from this
multi-line string that contains uh the
product details.
Finally, uh we know that this is going
to be a JSON array of multiple products.
We can use a for each to iterate this
list of products. uh use the previously
defined product template, replace all of
the placeholder values, and finally
attach it to the response content just
like we did before.
And as a very final improvement
that I've already talked about in the
previous session, we can move this YAML
and JSON resources out of the AI source
into their own resource files so that
they can be used across multiple files
and not just this specific test code
unit. Uh I'm not going to go into much
detail but you can see that instead of
having
the the two uh multi-line string in the
code I am reading it from my resource
folder the products.yaml
as well as the product template.json.
All right. Uh now that we have tested
the list products method I want to shift
our focus to how we can test fetching a
token. The biggest difference here is
that we have some sensitive information,
the token itself that we need to embed
in the uh body of the response message.
So I've created a template
for the token as well which looks
something like this. Um
it has a placeholder for when it expires
and for the token.
uh and in the handler I read this uh
read this resource just like before and
first I have to replace any values any
uh placeholder values that are not a
secret value like the uh expires
property I am replacing with the current
date time and using the two text that uh
Stefan also mentioned previously
and finally to uh put the actual value
of the token which is a secret value in
into uh the the JSON object. I can call
the write with secrets to method on this
JSON object. It will take the content of
the JSON as well as the secret value and
replace the in this case token pop
property with the actual secret text and
produce
a completely new secret text now with
the with the embedded token. Finally, I
can take this secret text
and uh write it to the response content
just like we did before. This way I can
make sure that the token is never
exposed even uh during debugging
sessions.
Um now that we have tested both the list
products and the fetch token methods
separately uh I want to combine them and
I want to test uh in one flow invoking
multiple different uh endpoints.
For this, I've created a test that first
fetches a token, verifies the token,
then uh fetches the gets the the banana
product and verifies that and then gets
the list of the product and verifies
that as well. In this case, because I
have multiple requests, I need a handler
that can manage multiple different
requests and can uh populate the
response accordingly and not just for
one specific request. In this case, we
can utilize the test HTTP request
message um which contains information
about the request type, the request path
as well as the query parameters of the
request.
So I note that all three requests um are
get requests. So first of all I can go
ahead and filter out any request that is
not a get request. In that case, I want
to simulate an error response, which I
can do by setting the HTTP status code
on the response object to 400. And I can
set the reason phrase to something like
can only handle get requests. Uh in case
it is actually a get request,
we can go ahead and check if the request
path is
pointing to the slash token endpoint. In
that case, I can populate the response
like we did before for the token and
return that mocked response.
In case it is targeting the SL products
endpoint, then I need to do some extra
checking if we want to get the list of
the products or if I want to get one
specific product. So, is the list
products uh method being invoked or the
get product for a specific product being
invoked? I can use the request.query
query parameters to check if the name
parameter is specified or not.
Let's go on the else case first. So if
it is not specified, I know that the
whole list of products is being
requested. So I can just populate the
response like I did before.
In case a specific product is being
queried, then I can try to get the
product from our uh YAML list that we
have seen before and if it exists,
I can write this content the details of
the product into the response and return
that. And otherwise, just like before, I
want to simulate an error response. In
this case, I set set the status code to
404 and the reason phrase to product not
found.
Um,
yep. So, that's been it and uh now let
me invite Espan onto the stage to give
you some behind thes scenes information.
Thank you, Bash. Take it away. Um,
welcome to the from the other labs
session. Not to be confused with the one
my manager Vincent uh provided this
morning. This session will be less AI
focused and a little more focused on
some old school useful things.
Um this is about tools for building apps
and how you how to hack the manifest
without changing the source. So this is
from one of our repos. We have a lot of
monor repos with a lots of AL projects
in it. In this case, it's the BC app
repo which is public and there are 230
from at least they are two days ago uh
app.json files in there and they all
share a number of common properties.
First of all, they have a version and
when we ship we have the same version on
all those app.json JSON files and
whenever we release a minor we increment
the minor version in all 230 files
and
our infrastructure team asked can we do
something about that it's a little bit
annoying we have to change all that and
of course they could have used co-pilot
to write some powershell script they
probably already did already did that
but that was not what they wanted would
like to have more an easier way of doing
some of Yes. So, let me
jump into some code. After all, that's
why we're here. Um, instead of fixing
the BC apps repo,
uh, I I picked another one and I chose
Stefan's uh, demo repo for Tech Days.
And um as you can see a lot have
happened since since 2024 to 2025.
Stefan got co-pilot. So he have um four
times as many files rather than just one
hello world. Um but what co-pilot didn't
do for him was to do anything about his
project files here. So it would be nice
if we somehow could get the same version
and all those and it would be easy to
have in a pipeline. So let me start to
do something up here
because if I start by
deleting the version number the compiler
will complain
should at least unless it's falling
asleep.
At least this should give a warning,
which it doesn't. Or
yes, good catch.
And now it won't get warning because I
actually have a special feature here.
But this one should
now get a warning saying you need a
version here.
But what now I can now do I can do this.
Put in a dollar sign parenthesis
version. And the reason why I can do
this is because we have looked at MS
build and directory props files where
they are using to do share common build
constants across many projects. So I
have in this repo in the root put in a
new file. We plan to support something
like this called directory app
props.json JSON that contains
information that will be shared across
all our
um all our uh projects and in this case
I have defined up here major minor build
revision I combined that into a variable
called version that glues them together
and that one I can use in all my
app.json JSON files. If I don't use it,
we'll just pick the normal version. You
will get anything everything like that.
But actually, if you look now, let's try
to see
I add a one to the minor and do a build
here. Oops.
Get into
like this.
So see what happened here is that I got
a
0.1 version built now because it picked
up the information from the directory
apps
file um app props.json file and stuck
that into the manifest while I was
building. This of course also works
if we are building from the command
line. So let me grab a terminal here.
And how many of you remember where LC is
tucked aside and when we install it's
something with a v6 and something with a
user directory right
we have done something else we have now
have a tools package it's in preview
it's a net tools package you can install
it's easy to install in pipelines
and that gives you an al command which
which maps to the AL tool we created um
which today lives in the V6 but we are
going to ship it as well this way. So I
can now do AL compile and point to the
project I'm in here
and it turns out it actually also
compiles and uses the same file for
getting all the common properties. So I
can both use it in a pipeline, but I can
also use it together with Visual Studio
Code without having anything
interfering.
So let's see if we can clean up the
app.json just a little bit more because
first of all, Steon has been a little
bit lazy, but I'll fix it. So you can
just I mean buy me a beer later or
something. No problem. Let's just fix
all these privacy statements and all
that. I mean
gone with those and the publisher. Yeah,
we want to have a common publisher,
right? Go back to the
to the file up here. There's another
section called properties. So I can put
a publisher in there and the properties
in there they are if if if the
corresponding property is absent in the
app.json file, it will pick it from
here. So what is happening here? I will
get a new publisher take the demon
ninjas and then I have up in the
variable section defined the base URL
which I can also use down here so I have
a common place to define that and when I
if I then build this let's just pick the
command line
let's build again let's see over here
yes we got the tech demo ninjas
because we cannot see the URLs
in the command line or in the in the in
the in the file name. But we can do
something else. We can do get package
manifest
and we'll take the latest one here.
Take this demo ninjas.
Run that one.
That's another command we have added to
the tool and also now to the command
here. It's just pulling out the um
manifest from the app file basically
printed out. And as you can see here, I
have my all my privacy statements and
the publisher. So the trick it does
essentially is that it replaces the
app.json information before we compile.
So when it hits the app file, everything
is resolved and everything is as it used
to be as if it was in the app.json file.
Installing the tool is easy. You can
install it, by the way, on Linux or
MacOSS or Windows. And apparently the
color of
No, you cannot see that color up there,
but it's actually very purple here like
the shirt. Um,
install it with this long command. net
tool install and then it's Microsoft
Dynamics Business Central developer
tools interactive global pre-release. It
will be in the slides. You can get it
there. Remember it's still a
pre-release. We plan to release it um at
some point maybe next release. And the
same for the property files. We are
going to try to uptake this file our own
and our own repos, our own pipelines. So
there may be changes to it depending on
feedback.
And now I show you one last thing you
can actually do.
We take this again
add the JSON here
can add
preprocessor symbols.
Then I could add something here called
configuration.
If you noticed here,
add a configuration here. Let's just
first compile it once
and then get the manifest.
And
there's nothing in here. It's because
the string is empty. So we throw it
away. No pre pre-process involved. But
it's actually possible to do something
like this.
Say we want to have a debug
configuration.
Try it again.
Get the manifest.
And now it actually ended up here. We
have some more ideas how we can make
this file more useful, improve it with
package information, something like
that.
But this is what is in there now. You
can play with it, but don't put it in
your pipelines yet because we may change
it. And I think we are more than out of
time. So, thank you all for listening
in.
Should be good.
So, we are one minute over time, but um
I'm just going to steal these and say
two quick questions. One over here.
Feel free to leave if you don't want to
be here. Y hi. Uh so about the HTTP
message handler, um is there any like
concrete advantages of using that over
the rest uh client code unit and the
interfaces that are surrounding it, you
know, like mocking those and using that
instead of the HTTP uh message handler.
Sorry, can you please repeat it? Yeah.
So there is uh the uh rest client code
unit and it has a lot of interfaces that
surround it. Uh so are there any
concrete advantages of using the HTTP
message handler instead of mocking those
interfaces and using them instead?
It's it's just a choice, right? These
are different options. So you don't need
the the rest client implementation if
you just use this handler here. But if
you find that is more useful for your
scenarios for making your test more
readable, more maintainable, then by all
means use that. This is a different
options. So there's no dependency when
you use the platform logic. Uh there is
a dependency when you use the the test
packages, but either way is fine.
There's choice. All right. Thank you. My
last one. Oh, we have one right here.
Wrong one.
Um I have a short question about the
pre-release thing you just said. What
was that? Uh just applying to the uh
thing that was shown showed last or was
it the whole thing with the JSON utility
methods? The the the pre-release is the
shipping as a net tool package. The
other one is currently in the in the
insider build of of the extension. Yeah.
So it's available there and there's some
I mean basically the pre-release
contains the same compiler. So, so it's
it's similar. If you ri it out one
place, it will change both. Um, but I
mean in some way or form we expect it to
ship the .NET tools package. I mean, we
have wanted to do this for a long time
and and the um the uh props file will
probably also ship because our own
infrastructure team would like to use
it. Okay, thank you very much. Yeah,
thank you.
So, thank you very much everyone. Have a
great conference. Enjoy.
