# NAV TechDays 2016: Migrating to Events

- **Source:** https://www.youtube.com/watch?v=qiZaWRA11hs
- **Video ID:** qiZaWRA11hs
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 94m39s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Hello good people,
welcome. This session is about migrating
to events. So if you are planning to go
to the cool session, you're in the wrong
room.
But I will be talking about the events
that Microsoft ships with the product
and how to use them.
This is me in my
winter
shape. I'm from Iceland, so you have to
have two faces. You might see this one
sometimes. You might see that one right
here. It's good to have, you know, the
both
versions. I am an employee of Advanaia
in Iceland. Uh, one of the biggest IT
companies up there.
I'm also a blogger on Dynamics and an
NAV
MVP.
Last spring, I got the chance to be
certified and I took that chance. So, I
am also a credentialized professional
for
Dynamics. Now, this is what we will be
focusing on
today. Four goals.
First, we'll be looking at the events
that Microsoft is shipping with Dynamics
NE
2017 and Dynamics 365 for
financials. Then we will dig a little
deeper
into when events are executed and when
they are executed, what data is
available at that given time.
We will spend probably most of the time
looking at this
one. Our third goal will then be to show
you a few
examples of how we can modify what we
have usually done with
customizations using
events. And then finally because this is
a developer
conference and I'm going to show you a
little bit of uh a few things that
interest me in the NAV and the new
platform. So first
goal what events are shipped with NOV
and Dynamics 365 for financials.
These are the event types directly from
Microsoft. We have business events and
integration
events which are dedicated functions in
any NEV object and they are by
properties changed to be a
publisher. A publisher cannot have any
code by itself. It cannot have a
response value.
But you can put as many parameters and
variables in as in a normal
function. Then we have the global
events. The global events are in fact
integration events but they are in code
one the application management.
What differs global events with the
other ones is that the platform itself
actually executes the methods in
coordinate one. Which means
that catching the global events will
allow you to actually change how the
platform is working.
Then in the end we have those system
events and system events are
automatically created created for every
table and every
page. So the user or the developer
doesn't need to do anything in code to
activate the triggers or the events that
are fired for those two object types.
So then we ask us how do we find these
events? Well, Microsoft does
not have any public list of events on
the
websites. So I suggest these two
options. One is just to go into a code
unit, create new
function, mark it as a
subscriber, tell the function which
object you want to subscribe to and then
list whatever publisher are
available. I said go into a code unit
and that's an important part. A
subscriber to an event can only be a
function in a code unit.
And it should be a local
function. You should not have a function
in a code unit that is a subscriber and
you are also using that function for
something else. So a dedicated
subscriber function local in a code unit
is the way we
recommend. Now Waldo had has spent some
time on figuring out the list of events
in the application. So he exported all
the objects in a text format and run
them through PowerShell scripts to get a
list of all the integration and business
events in the
application. And you will find that on
his website.
He recently published the whole list of
events in the release version of NE
2017. Now, how do we catch an
event? Well, let's me switch to the demo
machine.
We are in a code
unit and we go ahead and we
create a
function. Function name as
usual
local. And we go to
properties. Is this well visible in the
back? Possibly
not.
Hey.
So, we can Let's see if we can make this
happen.
Here we change
this to
be a
subscriber. So, what would you like to
subscribe to? Where would you like
to catch an event in the system? And as
a demo here, I'm going to
catch an event in the global or in the
code unit one. So I will go for
C1.
And what am I going to catch? I'm going
to catch after company open which means
that after NEV has opened the company
it's going to fire my
event. This
question always pops
up. Do we want to make sure that all the
variables in your function matches the
event that is
fired? And the question is yes, you do
want
this.
So there are a few cases where you might
not want it, but I suggest that you when
you haven't digging deeper into it, just
answer
yes. Now these two questions are also an
option. If the customer license doesn't
have permission in the object in this
coordinate that I'm creating, what
should happen? Should
we display an
error or should we just skip the
subscriber? And I usually change this to
skip just to make sure that even if I'm
have the code in there, if it's not
licensed, I don't want to use
it. Then the second one
is this object. This code init 50,000 is
in the customer license, but the current
user doesn't have permission to use it.
So what do we want to do then? It's more
likely that we would like to raise an
error in that
case. So we have our subscriber
ready and we can start writing
code. Let's do a simple
message. This should always be the first
code to write on a session, isn't it?
This is my first session at any tech
day. So, this must be the first
code. Save it. Save this one.
And let's reopen the
company. And it should say hello
world.
Happy. Pretty simple.
So back to the
demo. This was a simple first goal just
with the
basics. Our second goal is um a bit
tougher.
We will be asking the question when are
events executed and when they are
executed what data is
available and to answer that question I
created a set of a small set of code to
log what's happening when the events are
executed. I will show you the code
behind it but start by showing it the
functionality and looking at what is
really
happening. So this is the event
publisher log page. So here I will see a
list of the events that are
fired and my first
test is I want to create a temporary
customer. I want to modify the temporary
customer and I want to delete it. And
these are the events that was were
fired in that
process. And I can see if I look close
into the details, this is a JSON format
which will tell me every data that is
available when that trigger was
fired. So we will see that the
record is temporary. We see that the
trigger which means the trigger in the
table did not
execute and we can see all the data for
the
record. If you go a little bit further
down we can see that there's an
after insert trigger as well. We have a
before and an after trigger for every
table events.
If we look at the
modify, what we want to do there is just
add the
name and it's going to add the name. Now
let's look a little bit further
down and we can see the XRE. This is the
the previous version of the record as we
are used to having it. But we can see if
we look at this one, the XRE also has
the testing
which tells
us we cannot
detect changes made in code to the
customer if we
just look at the XRE and the rack in
this
instance and it's these are valuable
information we need to know what data is
available at any given
time we look at
same for all the steps. Look at all the
data in there and we will see it. It's
very similar. Now let's go and do the
same
thing but
now with a database
record. This is very
similar but we have two or we have this
one.
system event also
firing. So we create the uh customer and
we can see in the details that we are
doing the same thing. We are doing a
test customer. The is temporary flag is
false. So this is going to do something
for us.
And in between before and after we see
that the system event is
triggered and in this event the actual
database right
is triggered. So and we can also look at
the
details in here. This is going to give
us exactly the same
information. But the interesting part is
we see the
same if we look at the before modify we
can see that we still have our testing
as the name both in rack and
extre. If we look at the system
trigger, that's going to tell us we are
doing testing in this record and the
XRE is the real X
record. So this gives us another
opportunity then
to use this global event if we want to
track how our customer is modified.
There's one important thing to
know. After customer modify really means
after the con has been modified. That is
the record in the database has been
modified.
If we look closer to the details all the
way down here, I'm also
locking well not in
here. Let's go down
here. I'm in this case I'm locking the
record. I'm locking the X record and I'm
also looking what's really in the
database.
So after customer modify we can see that
the modification is already in the
database. So the modification has been
done which really means that if if you
want to affect the data that has been
written when you do a modify
insert you have to do it only before
trigger or you have to use the system
event. The after triggers in the
tables is for things to be
done after the fact.
There is really no interesting thing
here in the delete trigger. It's all as
you
expect. Now, let's complex things a
little
bit. Let's go to my customer
cart and
let's change the
name. Pretty simple
function, but a lot of events.
So here we can look at what's happening
for each of those
events and try to figure out where do I
want to hook in and make my
modifications. And we can see how the
events are ordered. After we have our
customer on the
page and we try to modify the name, the
first
trigger is done in the in the uh table.
So
before the modification code on the page
is executed, the modification code or
the validation code on the table is
executed.
if this is the correct order or not.
That's I guess not my place to say. But
we can also look at the the data that we
have in here. This
is I'm changing the customer
name. And if I look
at the previous record, I can see that
now XR has the same or the correct
information. So doing this from a
page means that the previous record is
correct and I can
also look at what's actually in the
database.
So we need to study all those events
when we want to make a modification to
our application or if we want to make an
extension to our application.
What's I felt was very interesting
here is we actually
have
three database modifications for this
one change we did in the
pages. So how is that going to affect
our subscriber? We're going to have
three execution of events for a single
modification. And we also see that we
have from the customer point of view, we
have three
modifications.
And I don't know if this is by design,
but this is exactly how it is. If we
look at the
data, the
trigger in on modify on the customer
table is executed after you change the
name exactly as you would
expect. But then
again few moments
later this trigger is executed again.
Well, but
without running the code in the
table.
So I would then say it's very important
to actually know what is
executed and when and what data we have
to work with at that given moment.
Now let's go to the
next test. Delete these records and
let's post an invoice, a sales
invoice. We'll sell our
usual bike.
and
pushed. And here is what
happened. And here things also start to
get
interesting
because affecting the way that we move
data in a customer or a sales invoice
posting is something a lot of companies
need to do.
So where do you want to plug in? We can
see that in the object name called sales
post the code unit at we all love we
have four isn't it sales post one here
one here and one here these
events this one
is well we are not seeing the yeah we
are seeing this one here this one is
actually fired before anything is done
in cot which means If you want to test
for your field, make
extra test near test far procedures, you
will hook into this event. And we can
also see here how
exactly or what exactly this event is
going to give us in data. So we will get
the sales
header with this trigger here.
This postcommit sales talk gives us the
exact same data
except if you know code unit 80 you will
know that the first part of code unit 80
is to actually get the documents or the
number series for the posted document.
So we will see the posting number series
and we will see the posting number in
the data. So we we know
that when the posting will be executed,
this will be the number of the invoice
or the credit memo if that is the other
way
around. Which means that at this moment
we have a lot of information but the
process hasn't really
started. So keep that in mind.
Then we are inserting ourselves in voice
header. We are of course having our
global trigger also firing for that one
and we can of of course study all the
data that is put in there. We have the
after and then we have our customer led
entry
created. We can we can also see that
after the customer ledger entry has been
created, the sales inwards header is
updated and the actual number of the
customer led entry is stamped on the
posted sales invoice. And the same thing
goes with all the posted documents in
sales and purchases.
And then finally after the document has
been
posted we have another event telling us
it has been posted and we get a few
parameters. We get the sales header with
all the information. The sales header
that usually will be
deleted and we can look at the other
parameters that we have. We have the
shipment number that was created and the
sales invoice number that was created.
So we have the possibility
to do additional data
modification on this trigger here.
This trigger here also
includes the general posting journal but
so that we can actually add things to
the posting of the sales invoice at this
point.
So the next question
is where should you go? Which one should
you
use? And before we go
there, let me talk a little bit
about that one.
So what we learned from
this in this
uh slide that we just looked
at the publisher
functions are executed quite frequently.
We have a start events before events. We
have an after events and we have a
global events. So there's a lot of
places that we need to look at when we
have to decide where we want to put our
subscribers.
That's let's see how the locking demo
that I created is done. So we will now
dive a little bit into CL.
So a simple
table, an entry table where we can log
the objects, the
publisher and we save our detailed
information in a blob
file. So this is nothing new here.
The code unit that we use to manage
this
is has those few public functions. It's
going to start
logging. So we need to we create a new
locking entry and we give it information
on where which object which method and
which content we are running it in.
Then we can log any
variable to the details we have and we
lock it with a variable name and a
variable
value. Then we can also log a record and
it will find all those fields in the
record loop through them and give us the
value.
So this function here will go through
all the fields in the given record and
lock the value of it to the
JSON and when it when we end locking we
will simply insert the record with the
details. So the basic code unit here is
pretty
simple and the fact that whatever you
want to log you will need to create your
own code unit with
subscribers to do the actual logging. So
if I want to
log changes on the customer or events in
the customer table, I will need to
create a code unit for that and I will
need
to
subscribe to
every events there are in the customer
table.
So I will create a subscriber for every
single event there are in
here and a function for each of them and
for each of them I will log the data
that I'm interested in. So I can log the
record and call it wreck. I can
log the XRE as I do here and I can log
the datab database record simply by
passing the record
ID and
that's that's the power of varants in
this case you can easily
pass whatever record you have you can
pass the record reference or you can
pass the record ID and you will always
get the same
result. If you look at how
we log the sales posting events, it's
similar. We hook up to all the events in
code 80 and we log what is going on.
So a little bit recap of what we just
did. We created the temporary customer
and we saw how the events were
fired. We created a real customer and we
saw the all the events.
The surprise was when we updated the
customer during a
page, we got a lot more events that we
expected and then
we posted and created our sales invoice.
So now
let's look at some of the examples of
how we can change
customization over to
events. First thing the rail roll
center. There are a few scenes that I
decided to show you guys.
Uh first thing is the question about the
role
center. This is my role center
in my Windows
client. And what if I want to have
another role center when I log in
through the web
client or even through the phone
client? So I'm using my business manager
role center in here.
And if we if we like to use the events,
we can actually create a user profile
selection where we can have different
profiles based on the client
types. There is a global event that's
that is asking for the profile ID when
you log in. But there are two things you
need to be aware of to make that event
execute. You cannot have any default
profile and you cannot have a profile ID
in the user customization table. So if
you clear that
out, this event will fire and you will
be able to do whatever you want.
And as an
example, this is the web
client. This has a totally different RO
center than we had in the Windows
client. The phone client has yet
another RO
center and the tablet client yet another
one.
This could be a pretty powerful thing
because users have different roles when
they sit at their desk or when they look
at the
phone. So, you you should be able to
expect a totally different
experience based on the device you are
holding in your
hand. And let's look at how this is
done.
Let's see. Here we
are. The code here is pretty simple. We
hook
up to an event, a global
event. Let's see how that
is. And that's a global event in
coordinate one called on after get
default RO center.
So that event will fire
and we will use our new table where we
can select the profile based on the
client type and we
will answer with the default RO center
and everything is as it should
be. Pretty easy code, pretty easy event,
but a very very powerful one and no
changes to the standard
code. The next thing I would like to
show you
is something I believe that a lot
of clients are
doing. They are adding a field to the
customer list.
entry. So we add a new code field to the
customer led entry and we add that same
field to the
page. So if we look at our
customer and we look at our
entries, we see our new field right
here. However, you should also know that
a field in a ledger entry tables is not
an editable
field. But still, in some cases, you
would like it to be editable. For
example, you can change the due date in
here, but you cannot change any amounts
or currencies. So, I want to have this
editable.
The edit function is done in the
standard through code
103 and this is an issue that we will
sometime find that there is there isn't
any way to hook into this code. So we
have to find another way to catch an
event and do that
modification. And in our
case and sometimes we need to just
accept that we need to
create let's
see almost a copy of the code in the
code we saw
earlier. So we need to use the the code
cloning that
we usually like to avoid, but now we
actually need to use it to update just
this one field both in the currency in
the customer ledger entries and in the
detail customer ledger
entries and we are
subscribing to that field on that page.
So we are subscribing to what happens
when we change the value of the field on
the
page. So after the data is validated on
the page, we go ahead and run this code
to
update the uh protected tables, which
also means that we have to have our
permissions in hand.
now responsibility centers is another
A lot of
companies, bigger companies like to
segregate their business or divide their
personnel depending on responsibility
centers. It might be a process. It might
be a
location. But you might want to have the
system set up so that the person working
on this responsibility center has a
limited view of what belongs to that
location and the other one has a limited
view to what belongs to that one. So,
and the other thing that comes along
with having different locations is of
course we have different
printers. You have one printer in
location A and you have one printer in
location B. And you guys who know the
standard printer selection, we can only
select printers by user. So now we would
also like to be able to to select a
printer based on the responsibility
center. And instead of going into the
printer selection table, adding the
responsibility and changing the primary
key, which I believe you cannot do with
an extension, you need to add your own
printer selection based on
responsibility
centers. And this would be an example of
that.
And what event would you like to use to
activate this
one? Here's the
example. We
have a function here.
Sorry function
here that is catching the global event
on find printer and that global event is
going to give us the user and it's going
to give us the report that it's going to
it's
printing and we have to ask ourselves
does this user belong to
uh responsibility center if that user
does belong to to a responsibility
center. We will go ahead and find the
printer name for that responsibility
center and return
it. But if that user has already
specified printer in the standard
printer selection, we would not like to
override that one.
So this is an
easy example of how you can apply or
change the filter or change the uh
behavior on the in the find printer
function. The other code that you see in
here regards to the customer list and
the customer page. You're all well you
have probably seen it in the open page
trigger in the sales documents that the
list of sales documents can be on is
filtered by the responsibility center of
the
user in the standard system. This is not
done in the customer list and you might
also want to do that. Make sure that
this responsibility center has this set
of a customer and the other
responsibility center has another set of
a
customer. So in that case we can easily
hook
up to the onopen page trigger
in the customer list and the customer
cart and apply the filter in the same
methods. So we are applying the filter
both to the customer list and to the
customer card. But we also need to make
sure that when we create a new customer,
that customer will get the
responsibility center code for that user
to stay in the scope of the
filter. Now, let's step it up a little
bit.
that code field that I
created in the general in the customer
led letter entry. I now also want it to
be in the sales
header. And when I post that sales
header, I need to have that code
transferred to the customer ledger
entry. And as we saw earlier, we have a
few possibilities of doing this.
We see here for
example, let's go ahead and sell to our
customer the
usual
bike. And we put in
here some code.
And we need to make sure that that code
is
delivered to the customer ledger entry
when we do our
posting. I have here four examples of
how this could be done. Two of them I'm
going to show you.
Now, this one is going to catch the
event that happens
after the invoice has been posted.
So if we have an sales invoice header
number, we will get that
invoice and that invoice will have
information about the customer ledger
entry number that was
created. If we have a sales credit memo
info, the same thing goes. We will have
the customer relation entry
number and we would like to update this
field in the customer entry number with
the field that we did in our sales
invoice. But since
we have already done our code unit to
update this, we can simply call that one
in the end and it will update this code
both in the customer list entries and in
the detail entries that were
created. Now we should always
see does it
work. So, we will take our sales invoice
and post
it. We'll look at the
customer. Hold it. Hold it. Hold
it. And the
entries. And we have that quote in here.
Did you notice something new when I
opened the entries in
2017? There is something new
here. The newest invoice is on the
top. Have you noticed that? That's in
the customer letter entries, GL entries,
vendor letter entries, and so
on. So, you don't have to do that for
the customers anymore. They always ask
for it. So now it's built in. The newest
is on the top. That's what you're
looking
for. Now let's look at the other way or
way number two to do
this. Doing that method means that we of
course have to update a record that has
already been inserted. It's an extra
database operation.
The same thing actually is done here,
but instead of hooking to the coachet 80
that does the posting, we hook up to the
modification of the sales invoice.
So after the sales invoice is modified
and the current customer led your entry
number is updated, we will get that
customer led
entry, update it with our reference
number and call the same code
again. And just for demonstrational
purposes, we of course need to make sure
that this is working.
And now we can go yet another way to
find these
things. There's always more than one way
in any way.
And we can show that we got our code as
well this
way. So which one is the better one?
Which was the right one? Are they
both the wrong way to do it? I will
suggest two more options just a little
later.
Just you should be able to see that we
have more than one option of doing
things.
So how do you want to do this?
First thing you have to map all the
events that are executed in the process
that you need to change or
modify. You have to be really creative
in figuring out how that old code
modification or the whole old code
customization can be updated and
changed.
We of course need to think about
different client types and the cloud. We
need to really understand that some
functions are valid in the Windows
client but not in the web client.
For example,
the question we had about the
printer, it's not really valid for a
Windows
client
or sorry, it's valid for a Windows
client but not for a web
client. If you have a process that you
need to hook into and you can't find
your event, no matter how creative you
are, you can go into connect into
Microsoft connect and suggest that they
add an integration event event into the
code.
And some say this doesn't work, some say
this works. My experience is
that if you are building an extension
for Dynamics 365 for financials and you
need an integration event to make that
extension work, Microsoft is very likely
to listen to what you have to
offer. And the last box here is saying
that we are going to have to do some
code
cloning. It is necessary. We
cannot modify the functions that we have
in the system. We might need to do
exactly the same thing that Microsoft is
doing just a little bit differently in
our own code.
And we might even need to update the
same record that Microsoft just updated
again because we have our
own changes we need to
apply. So there are things you need to
live with. You need to make sure that
all the code that you create is
independent of all the other ones. It
has to be able to survive if everything
else changes. That's the thinking of the
Microsoft extension model. Whatever you
create, it needs to be independent of
other things. It needs to be able to
survive even if other things are
updated.
Now I would like to spend a few some
time talking about things that I find
interesting about
development which will include
those two more options for
the sales posting.
Now we have some changes in
our environment that we are setting up
different to what we used to have in our
own classic client in 2009 and older. We
have something called the server
cache and the server is caching a lot of
data which means that when we are asking
the server to read something it can be
extremely
fast because it doesn't have to ask the
SQL server about that
data. Some places in the code and you
probably recognize this and have used it
yourself.
We
are use something called gl setup.get.
We are fetching our GL setup and we also
have a boolean variable that tells us oh
we have already gotten that GL setup so
we don't need to do it
again. And we are when we did it this
way we were trying to save the traffic
between our NAV and the SQL
server. And now this is not
needed. It
is the same doing GL setup multiple
times as using this option. The GL setup
is in the server memory in the server C
and it's just like picking it up from
the
memory. Also, if
you're thinking about
performance, you should be using
queries.
Queries are extremely fast in
reading. And if you have to read data
for more than one table, combining them
in a query is the fastest way to do it.
So if you're not a have not been using
queries, I suggest that you look really
close into that. What's also important
about queries is
that the NAV server will only ask the
SQL server about the columns that are
included in the queries.
So instead of reading the whole customer
record, it might read only three or four
fields from it, which also means much
higher performance.
Temporary tables that are now stored in
the memory of the
server are really useful.
And try as well as you can to use those
temporary tables for all the heavy
lifting, for all the
processing to create the final result
before you actually go ahead and publish
them to the SQL server or create the
actual
records. And finally, I want to talk
about single instance code
units. They are like a memory bank.
You can put things into a single
instance code unit and it will survive
as long as the client is
running. So put things into a single
industry code unit is like putting it in
a shelf somewhere and then you can pick
it out somewhere
later. In the keynote here earlier, we
saw that they are using this method in
the notification
framework, Thomas did put two entries or
two values into a single instance memory
bank in the
notification framework and then later he
was able to pick it out of that same
memory bank. So what I'm showing you
here is nothing that they are not using
themselves. And let's look at the single
instance. I have here three single
instance code units.
one with the net object dictionary which
is my shelves. So I can put things into
a shelf and I can label that shelf with
the variable name and I have unlimited
number of shelves that I can put stuff
into.
Then I also want to be able to store a
record and just keep that in memory to
be used somewhere sometimes
later. And then the third one is about
keeping one set of a temporary record in
memory where I can use the same
temporary instance from different
objects.
Let me dive a little
bit into that one. The dictionary just
to show you how that is
done. Zoom in a little
bit. This is the net object
dictionary and it can handle any type of
data. So when I want to add something to
my dictionary or to my shelf, I call
this function with a variable name and a
variable value. And that is just add it
to the
dictionary. And then when I want to get
something from the dictionary, I ask
does it contain this shelf or this
variable? And I return it if it does.
And the same thing when I'm clearing I
ask first does it exist and then remove
it because a cleanup is always a good
practice. And then I added one function
which does both. It both gets that value
and clears when it's
done. If we are
using when we are using this from code
it is really useful to have a dedicated
get function for each of the or of the
simple types that we are using. So it's
useful to have a get text get code get
decimal and a get
integer. The code unit
itself in properties is set to be a
single
instance and but I would I also like to
make it clear in the name of the code
unit that it is a single instance code
unit. Now if we look at the option
number three we had for posting a sales
invoice. This is using my
dictionary. Bit too small, isn't
it? So this is the
event in the sales posting that is
triggered after you have created or
after you have done the number service
and you know which number the final
invoice will be posted under. So you
know the document
number. So I'm going to save this
posting number here into one
shelf. Then I'm going to
put my code field into another
shelf. And these are the variable names.
The variable names are defined in
functions in the button. It's very
important not to use a text code for a
variable names in every instance you
want to use them. If you put this behind
a function, you can be pretty sure that
a spelling error will not affect your
code.
And then what we want to do is we want
to
catch the event before the customer is
inserted. And when the
customer is being inserted, we simply
ask our
dictionary, do you have something for
this document number?
Or let's say what is your document
number that you are storing? If that is
the document that I am
posting, I
will
stamp the tech code into the customer
list
entry. And let's do the same for the
detailed entries.
Make sure that the other ones I had
tested were
disabled. And let's prove the point that
it actually
works. Selling the same item once
again. And post
So we have our value in there. And what
does this do for
us? We do not need to do another get
statement to find the custom military
entry that we created. We do not have to
do another
modify to modify the record that we
already created.
Just by asking a question before the
process starts and saving the answer for
that question, we are able to use that
answer anywhere in the process after
that. So this is a very powerful tool if
you want to use this.
The same
idea is in my option number
four except there I'm using the record
storage. So this storage here I can put
any record into
it
and it will remember that it has a
record and it will remember the number
or the table number of that record. So
when I
ask for a record for my table, I will
either be answered yes, this is the
record that I'm keeping on myself or
not. And I must say this is one of my
favorite functions in the whole system.
You can throw a variant into a code unit
code 701 and you will get the record
ref as an answer. So you can throw a
record in there, you can throw a record
reference in there or you can throw a
record ID in there and you will always
get your record
back. So this is yeah pretty simple one.
We can save any record or we can save
our record by record ID if we like. And
this is what we would do in example
number four. So in the same spot that we
did before, we are now saving our sales
header. Not just the one field, the
whole sales
header. And
then when we insert or before we insert
our
data, we are going
to
get the
code if this belongs if this is the
record or the document number that we
are posting and that single instance
record storage code is right here. get
me the record reference for the sales
header. So
even if I have no link to the actual
sales header responsible for this
process, if I ask for it before I begin
and keep it in my storage, I can always
access it later in the process from
totally different object and use it
right there.
And again, just to prove a
point, I Are you starting to believe
that this
works? Let's
see. Now I'm getting lazy.
So this leads to the same result. So we
have now seen four possible ways of
catching an event and doing what we need
to
do
and what to choose what to do. You
probably would like to make sure that
the method that you choose works on
all client
types. and you want to make
sure that you have the best performance
possible. So I will disable this one
again. I'm also using
this as an
example in the in the user interface.
So, I go ahead and I want
to create the sales invoice for the
Canon group. And you notice that the
Canon group has ship to
addresses. And I find out that the Canon
group has ship to addresses. I'm likely
to want to use one of those in my sales
invoice. So, I'm asking a question of
the user,
which ship to address do you want to
use?
I want to use this one. Okay. And it's I
applied to the
invoice. The thing is
here if you do this on a
normal event after you have notified or
after you have validated the customer,
you will not be able to pop up a page to
ask a question. You will be in the
middle of a transaction.
So you have
to start by figuring
out if the question needs to be asked.
So let's look
at this code.
So before we validate the sell to
customer, I'm going to check if that
customer has shift to
addresses. Then I'm going to filter on
it and I'm going to run the
page and if the user selects one of the
addresses, I'm just going to store it on
my
shelf because I know I need to use it
later. I cannot apply it now because we
have three or four validation codes
coming after this one that will
overwrite my
selection. So let's keep it here until
the
end. And we have two two ways of
creating creating or applying a customer
to a sales
invoice. We can also be doing it
directly from the customer card. So we
will need to catch a before insert
trigger. So if the filter is applied on
the sales cell to customer number in in
here we are also creating an invoice for
that customer. And we also like to ask
the
question
before. And
then after the sales invoice has been
inserted, we make sure that we clear the
value from our shell from our dictionary
to make sure that it doesn't interfere
with the next invoice being created.
And then after some digging using the
event logging, I found out that it was
best to go after the location has been
validated and update my ship to address
information.
So after that has been validated and I
have something on my shelf in my
dictionary, I
can apply the sales or the shipment
address to the sales header. And this is
also in this case done with code
cloning. I'm not validating the ship to
address in the sales header.
So then again we need to live with code
cloning and we need to ask the question
before the transaction actually
starts. Now we have one
more one more example of
this single instance
dictionary. Let's see that I have now
created that invoice
here and I'm doing a post and
send
and I'm now catching the action of the
user pressing the post and send
button
and I
have a question
here. Will this invoice be sent to a
printer? And if that is
true, just select the printer name you
want to print this invoice to. So I'm
asking yet again asking the question
before the actual posting starts. You
know all that after
posting the invoice will be
printed and it will be printed according
to the printer selection or our
responsibility center printer selection.
So I can just select the printer before
this process starts. I want it to be
printed to
PDF. It's
posted and it's printed to a PDF. So I
again ask a question before the process
and then I catch the find printer the
same event I did
earlier and then I apply whatever I had
in my dictionary.
So there are various cases that this
dictionary can be used
at.
The last single instance dictionary is
about a temporary
tables and I told you you should be
using temporary tables as much as you
can and the fact is you can have many
instances of the same temporary table.
Let's say here for example we have a
page which has a
record in here and then we have fact
boxes and how do you get
access how is it best to make sure that
you can from the fact boxes or actually
from any other object directly affect
what's in your main page. So, how would
you do something like
this? And I'm doing this
by sharing the same temporary record
between all those
pages.
So in my pause items table, I have a
function that accepts
my temp pause line. And I use the copy
here to make sure that I have the same
instance. And by using copy true you
copy the temporary table instance to
your new
variable. And that al that means that if
I
press the number
button the code to add an item to the
temporary table is this easy and it just
works. The same
idea you can apply to a fact box. Let's
say here for example
I go and I
create a sales invoice for my usual
customer and I want to add a link which
is just some
files. Let's put in a train ticket.
So I have created a link for my sales
invoice. I've hooked up an event to make
sure that when I create a
link, I am looking for the master record
behind the link. So I have a secondary
link in my record link table which says
that if I add things to a sales
document, I want a secondary link to my
customer. And the secondary link is a
record
ID. And how would you on the customer
card link a record ID from the customer
to the fact
box? Another
challenge. So here we also need to be
creative.
And this is an example of how I use a
single
instance code unit to save a temporary
or host a temporary instance of the
record link
table. So when I open the fact
box on the side of the customer card, I
initialize a temporary record in a
single instance code unit.
So that one now is deleted, cleared and
I copy the instance between the single
instance code unit and my fact box. So
now I have the same table in both
places, the same
instance. Then when I have the current
record of the customer and this is
catching the
event from my customer
page after get current record. So now I
know which customer I have on my
page and that record ID of that customer
I will use that to
filter the temporary table or exactly to
filter the record link and replace the
values in the temporary table so that
the temporary table will now have all
record links that have secondary link to
my
customer and I don't need to do anything
for the factbox because the factbox has
the same record. So it will just
automatically be updated with the
temporary record in there. So let's see
how that one
looks. Here I
have my source table here
is well sorry my source table here is my
record link.
It's going to match my temporary
table. But in my code, I'm gonna want to
clone my temporary record link with
what's in the memory. And when I find
the next, I'm going to search my
temporary table instead of the actual
table. So that means that you can now
put a fact box on any record. it doesn't
have any direct relation with that
record. Even if you cannot add the
factbox link and make that work
correctly, you always have another
methods of doing
it. So that's why I really like to use a
shared temporary
tables. Now to my
final demo.
I am taking a list of customers and I
want to group them by the posting group.
So I want to count how many customers I
have for each posting group. And
I'm suggesting four possible ways to do
this. We can loop through the customer
with our record and we can add and
modify the grouping record as we go
along.
This is directly database records which
we will be using in the first
method. The second method, the one to
the right, I create a query. The query
gives me account of
record and for each for each customer
group very first
one. The third one is going to loop
through the customers and the grouping
table instead of being a database table
is a temporary table. So I'm going to
create and update the temporary table as
we go
along. And the fourth example is what I
called a skip test and I actually
managed to use that in my workshop
yesterday.
So
for so I'm sorting the
customers by the field that I'm grouping
and I find the first one count them all
and then I find the last one. So I'm
going to see show you the the code
behind this and how it's
performing. So let's go again to the
demo
machine.
Here I have
my grouping test page and I'm starting
the test and we can see that the query
or perhaps we cannot see
it. The query test is pretty
fast. It's a matter of milliseconds.
the temporary test where I group things
in
memory that is pretty
slow. I'm reading through all my
customers looking at
the the U
result
and
seeing or counting the kids. Now look at
the skip and contest. It doesn't even
register. It's so fast.
So, and then we look at the legacy test
where everything is in
database. It's so slow. 23
seconds each
one. So, which way would you
go? When do you want to use this the
query and when can you use that skip and
count methods?
So let's look at the
code between them all. This is the
legacy
code. It's just looping through the
customers, inserting or updating the
grouping
record. You could say this is the way we
used to do it. So that's why I call it
the legacy
method. But no longer do we do it this
way. The difference between the legacy
method and the temporary is that the
grouping record is now a temporary thing
which means we are mostly reading from
the
database and updating our temporary
grouping table. And in the end we write
our temporary grouping table to the
database. I suggest or I think that a
lot of you are actually doing things
this
way. Now if we have a
query it's pretty simple. The query
delivers customers customer group and
the count. So it's just call the query
and insert the grouping table. That's
it. But the skip test is a little
different. We sort the customer by the
posting group. We find the
first we go into a repeat look and we
filter all the customers based on this
posting group. And then we just count
them.
After we have counted them, we find the
last one and release the filter. So the
next one in a repeat loop will be the
next posting
group. So this is the least number of
reads we can do to create this grouping.
I believe Microsoft is using this in one
or two places, but it's a very fast way
of grouping data or making sure that you
do something only for this set of
records. Now, that was my last demo. So
now we have time for questions and we
have t-shirts.
There we have one. Hi
there. Is that possible? The question
was when we create more and more
subscribers, is there a way to see the
list of
subscribers? The answer is yes. There is
a page in the RO client. Let's switch
over to that one.
that you can
start from the debugger here in the
tool. It's called the event subscription
and it will give you the list of all the
subscribers you have in your system
today.
It is possible to have an inactive
subscribers which means
that you think they work but they don't
and I suggest that you look at the
session at Waldo tomorrow to see how to
manage those
problems. And we have a t-shirt.
If you have more than one subscriber to
one publisher, is it possible to change
the sorting? Which one will be executed
first?
Okay. The question was, you have more
than one subscriber to the same
publisher. Can you in any way affect the
way that they are
executed? And that question is no, you
cannot. They are executed in the order
of the ids of the code
units. Which means that if you have
complete control, you know in which way
they will be executed. But as soon as
someone else adds a subscriber in a code
unit with a lower number than yours,
then you have no control anymore.
So, but there is a pattern called handle
pattern which you will find on the Viki
page for NAV which actually says that if
you have multiple subscribers you can
say boolean flag for handled and if it's
handled by this one the other one are
supposed to leave it alone or leave it
alone and that's all what we call a
gentleman's agreement. Please do not
touch it because I've already done it.
When you when you use uh the third
approach with uh using dictionary and
you start posting two documents
simultaneously, can they get can values
get mixed and first document get the
value from the second document in the
end? All
right. The question was if the
dictionary can be mixed if you post two
documents at the same time. The single
instance objects that I was showing they
belong to a session which means that
another user in another session has
another set of dictionary. So the the
data will never be mixed between more
than between users or between sessions
and a single user cannot possibly post
two invoices at the same time in the
same session.
So I can't see any problems using that
method.
Yeah, you it's just you will get the
record blocking. So it's no way to do it
anyway. It's no way to post two
documents in the same same session.
Okay. Sorry.
Yeah. Hello. Okay. Oh, you sorry. It's
back there somewhere here. Oh, there. I
sorry. I was just wondering the you're
talking a lot about using single instant
code unit storing data as a as a shelf
and area to put it in. It adds quite a
lot of complexity to the code and the
the person developing has to be very
conscious of what they're doing. a
second developer comes in, they have to
make sure that they're using that same
method and not doing it differently. So,
you're adding a layer of complexity that
could cause issues with um stability of
the code or with the consistency. Have
you done any significant performance
test to see if this really is a
significant advantage? Uh, in other
words, is it really worth doing all
that? It seems a lot of complexity and I
just don't see in my head where you're
getting a major performance advantage
from doing that.
Well, do we get any major performance
advantages from using the single
instance? Kind of depends on the
customer. If the customer is a big
customer, you will probably see a lot of
performance. If you can
skip 7,000 rightes into the ledger
entry, perhaps you will see a lot of
performance increases. But for smaller
customers, I can't really see that it's
any problem just doing another modify on
the customer ledger entry in like in
this case. I'm not worried about big
customers. Yeah. So, I'm not saying that
in those between those four examples
that you should use the single instance
one. It's all on you to pick which one
is the one that pass then the one that
you really like. But any product is a
complex one. So, you always you you will
always have to
uh dig a little deeper into it, but
yeah. All right. I'll throw the catch
box. It's like a Pokemon. So, there's
one two hands
there. You can speak into the microphone
now. Speak into the box, Steve. Yes. Oh,
do you see a way to uh share temporary
objects between sessions so that two
users can use uh the same temporary
object?
Well, you could do that with net and the
single and the singleton pattern using a
net
object, but not within CL. You will then
have to use uh a real table, a database
table if you want to do it between
sessions. The singleton, you can put a
singleton DL on your server machine
which will have the
same information for all users on that
service
tier. So that's single instance
dictionary. You can find that on my blog
if you
like. There's one here. If you if you
use temporary records in your single
instance code units to store data and to
modify or insert them afterwards to
increase performance, isn't there a huge
risk when several users try to change
the same data or how do you deal with
this? Well, if we have the data in the
single instance dictionary, then that
means that that data is isolated for
that session. Exactly. So you will not
have more than one user trying to work
on the same temporary table. It's always
that's correct. But someone else might
retrieve the record in a database before
it is stored back. Yeah. But that's
that's the same issue we have any time.
You have to make sure with that you have
the current record of the database
before you update. You have to use the
the find method for example to make sure
they have the actual okay record to work
with. And that's fast.
Is there a time where you wouldn't use
uh the
events? Any rules for when not to use
events or would you always use
it? Well, when Microsoft brings us the
solution up, then perhaps we can do a
little bit more. But at the moment,
that's the only way we can do things if
we want to have things in an extension
format.
So if you are building your own
customization which you can call
solution app which is the foundation or
your localization then you probably need
to go beyond that but then you have to
have the perfect control of the
code but I would call that the solution
app and that's it. Yeah, I will ask one
more. All right, I'm sorry. Can I ask
one
more? Event publisher has property to
pass global variables. I understand that
this is not used anywhere in standard
and is it something bad or
it's integration events can do this
business event
cannot. Uh yes, this well it it can
include globals. It's never used in
standard. It was pushed in by Microsoft
because of a pressure I believe. I don't
think you should use it. If you need
something of the variables from the
center object, you should just add it to
the publisher function as a local. So it
is there. I don't recommend that you use
it. So that's it. Thank you all. It's
been up.
