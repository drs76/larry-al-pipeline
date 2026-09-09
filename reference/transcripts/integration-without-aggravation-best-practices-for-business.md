# Integration Without Aggravation: Best Practices for Business Central

- **Source:** https://www.youtube.com/watch?v=r3wWbJ-gxsA
- **Video ID:** r3wWbJ-gxsA
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 85m02s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Ladies and gentlemen, welcome to today's
last session. Please put your hands
together for our next speakers, Vlat and
Taranga.
[Music]
Good afternoon everyone. I hope you guys
had a really great conference day two
days and uh surely we did. We had a
really great time.
Uh this is the third time I'm presenting
in tech days and it's always been like a
pleasure and a privilege and I'm truly
humble about being able to come here and
present.
Uh our session topic is integration
without aggravation best practice for
business central
for the next 90 minutes we'll be looking
into two paradigms of business central
integration. First part would be how we
going to do the traditional way of using
AI. The second part of the presentation
would be about how we going to do this
in a more modern way.
Before we jump into session, let me uh
introduce myself since we don't have any
AI kind of a things in our uh slide. I
put like I'm thought of about adding a
picture which created from AI at least
to relevant to the most of the topics
here. So I'm a lead technical consultant
at theta. Thea is based in New Zealand,
one of the largest uh business central
implementation companies in there.
As though even though I live in New
Zealand, Oakland, I'm originally from
Sri Lanka and I'm a co-organizer of
Business Central user group in Oakland
and I'm a ninetime MVP for the Business
Central as well.
I want to share something interesting.
So this our Oakland user group we run
this every month at Microsoft and we
started a few months ago and it's
growing really nicely and if any of you
this is open invitation if any of you
are traveling to New Zealand for
sightseeing and if you're specifically
in Oakland just buzz me and we'll have a
catch up and if you're lucky it might be
the day that we have in the user group
so I'll invite you to user group as
well. So today I have lot with me.
Yeah. So I seen that audience when you
start talking about New Zealand they say
expecting that you will get a tickets
like a free tickets here on the table
but not um yeah but we absolutely
welcome you guys um in in our mainland
and wherever you are there just catch up
and pink Tanga he will u absolutely will
help you. Uh so two years ago we've been
on this stage. Uh but like Tanga dropped
me. He didn't get a visa and I'm
actually making a big surprise for him.
So he's presenting by himself today.
Come on. Uh no it's it's a bad jokes but
okay. Uh my name is Vlad. I am working
with Tanga many many years probably 18
years in BC world. I always looking for
some challenges outside of BC. So, uh
actually if you guys touch in any kind
of technology outside of BC, ping me. I
will be absolutely keen to jump on and
try to contribute with you on your
GitHub projects on this. Um yeah, where
is
cool. So today's um we will try to
explore some
um integration scenario and our external
service would be like vet appointment
clinic. Um I recently get a dog first
time in my life. It's a shame like in 40
years old I I can get a dog.
So uh but uh I this kind of inspired us
to see how the daycare u the pet daycare
services works how they can uh manage
and communicate and specific challenge
is that like any uh like locally there
is plenty of different vet services
um and they had like different ways how
they wanted to communicate with you in
terms of the appointment for your pets.
Um, it's probably not like absolutely
real close to to to production scenario,
but like we've seen a lot of beer cases
and because we are not like big fans of
the beer, uh, we decide to go with this
one.
Go for it.
So if the integration is a puzzle
especially business central integration
is a puzzle I would see that this puzzle
is with the five pieces. Main five
pieces are setup trigger mapping request
and response. Once you have all these
pieces in place in the correct places in
a correct way you will have a complete
integration.
For the next part of the session, what
we're going to do is we're going to take
each of these pieces which is very
valuable for this integration to be
working and successful. So we're going
to take these pieces and analyze why
it's important and how we going to
implement that in BC.
So the first piece is setup.
In this piece we are mainly focusing on
collecting information from the admin
users or the power users.
In this piece, we are trying to to
collect information about the service
connections like the endpoint external
endpoint details or the authentication
details like what's the username, what's
the passwords and how we going to
authenticate, what are the types of
authentication methods. We want to
collect this. Not only just collecting
them, we want to validate them. We don't
want to run into a place where when we
try to do the integration, the
connection details or the username
authentications are not working. So, we
want to validate that part of it.
And then we want we don't want to build
an integration where we can't control
integration
when when to stop when to enable we want
to have that kind of mechanism as well.
So how we going to implement this in a
normal normal or the old fashioned way
what we normally do is we create a table
we create a setup table and then we put
those fields in there and then ask user
to go ahead and fill this information.
But that's the old way of doing it.
The recommended way or the best practice
would be using assisted setups. So that
user will be guided throughout the
process and relevant prompts will be
prompted and you can do the validations
on the run as well. So user won't miss
any details while they're filling out.
They will know exactly what needs to
enter and when they click next it will
ask the next question and they can do
that.
Now that part is correct. Now how about
managing these connections? I have seen
many partners including us in the past
we were building integrations and we
have different modules. Now different
modules have different endpoint details
and we have set up tables for all of
these and set up different set of pages.
Now the admin users has to memorize like
for this integration we want to go to
this page to enable the integration. For
this integration we need to go to this
page.
That's the old method. The correct
method would be to use the service
connection which is the centralized
place for external endpoints.
So you will have all the external
endpoints in one place and user doesn't
have to memorize it. You just open the
page all the endpoint details will be
there. You click it and then you can
open the page and you can go through the
process. So that's the beauty of the
service connections.
Yes. So the next big thing is triggers
and uh actually that's a biggest mistake
for for us. We had like this challenges
a lot and we had an interview with
Microsoft recently that said they that
the biggest mistake that partners are
doing in terms of integration is
actually trying to trigger and initiate
the code to external service when a
transaction is still open when there's
plenty of tables is locked and uh let's
say it's 95% of the the the cases like
this where this actually happens. So we
wanted to like focus on it specifically
because on this stage we wanted to do
few things. We wanted to understand
where is our data set uh on which state
of the business process we had enough
data set to communicate with external
service. We wanted to make sure that
this this data set is validated. So
there is everything is prepared for the
external service to to be called. So
even if we are not really building the
the whole body of the request or like
authentification, we just wanted to do
the validation side of it. Um and uh and
the last which is this important part is
make sure that any kind of business
transaction is completed
committed before we initiating anything
within the external service. That's a
two different systems. There is no way
you can like match them all together
into one single transaction. You start
something let's say if you are in the
middle of posting routine you subscribe
to on post warehouse shipment send a
call to your shipment provider made a
consignment with them get back the
response something happens back one
system in one state another system in
another state full stop and we make this
errors every day. So um to be able to um
in a in a best way to mitigate this is
build up uh your integration
using an instrumentation within the
business central that enables you to do
as in goals and we found that the job Q
is perfect instrument for it. So
wherever we want to in outside of the
business process to trigger something
that should be going outside we will be
scheduling job Q that's it we're making
sure that this job Q entry is in sync
with the business transaction. So if
everything will be rolled back the job Q
entry will be rolled back. So there is
no request potentially going anywhere
else.
And um that's can give you like a lot of
bonuses like uh you have an automatic
retries you can schedule them you can
like build some kind of queue so we
found that that's a perfect
instrumentation for it
uh yes okay so the next one is the
mapping mapping is basically you
transform and prepare the data set for
the integration so that you can call the
external party and pass this data set to
the external party. It's simple as that.
For that uh in business central we have
couple of uh helpers or rappers I would
say to support this and business central
support JSON and XML format and recently
Microsoft released really nice uh JSON
helpers which we can use
and uh the other option is leveraging
data exchange definition. This is mainly
if you want to give the users the
ability to change the payload. If you if
you think that users are capable of
doing this and also you feel that in the
down the line the integration might
change the payload might change and you
you don't want to make code changes then
you can use the data exchange definition
but
it comes with a price because
integration framework or the data
exchange definition framework cannot
do a full complex XML exports. So you
might have to write code again and it
might be tricky if you go down that
path. So make sure that you actually
think really well before you go into
that path.
And the third one is use interface to
manage versioning which means that
integration is actually agreement
between two parties saying that okay
this is the data set this is the payload
I'm expecting this is my endpoint and if
you want to call my endpoint you need to
make sure that it matches
but in the down the line the partner
might be saying that uh we want to
change some fields and we will have 3
months to do this and after that 3
months we're going to actually duplicate
the current ation. So how we going to
handle that? So the best practice would
be using interfaces in business central.
So we normally do is we wrap our
integration through a interface and we
have a version for that and then if the
partner comes back and says okay we want
to change something we said okay all
good. We don't touch the existing
integration. We create a different
implementation of the interface which
allows us to
move forward without breaking the
existing integration and allows us to
switch back and forth if you want to do
the testing or something like that. Yes.
So for the interfaces um few things. So
build up an interface for the high level
functionality of your client. Don't try
to like okay I will have an interface
just for a mapping. It's fine that you
will sometimes will have a duplicated
code but it will be like pain pain
really to to try to trace if you had
like a mapping versions but maybe the
URL is the same the version is the same
wrap the whole external service client
into an interface and then do the
implementation even if with a with a
copy copy code cases.
I wanted to add a little bit regarding
data exchange definition. uh we had a
like product in TA that we do
integrations and we it's it's partially
built on on the data exchange framework
and uh we had one customer that actually
going and actually modifying the schema
for his needs. Every everyone else as we
implemented it they're just sticking
with it and uh there real cases where
they actually the mapping is changing.
So I strongly recommend you will save
your effort, save your time for your
customer and money for your customer if
we just hardcoded it
using A. So in our case we we do um
build our demo one using interfaces as
well but it's really really easy one. So
you can see that I just had a simple
interface where I'm requesting an
appointment. It's everything that my
external service is doing and I'm pay
passing the record that okay that's
that's my parameter for this. I'm making
sure that it's as generic as possible.
I'm not trying to like build certain
specific parameters within this
interface. I'm allowing the record to be
interface. So then any kind of future
changes to it will allow me to pretty
much not touching the interface but
extend a sk the scope of parameters into
it.
So the next one is a request. Uh I think
that's me. Yeah, I think that's you.
Okay, cool. Uh yes. So um uh we do have
a lot of instrumentation in business
central uh to call the external
services. I actually know four. It would
be interesting like if someone else know
five.
That's that's for sure. Um so what we
wanted to say is that um it's absolutely
capable. It's covering 95% cases. Maybe
not 100% but uh we wanted to make sure
that you guys are using the right tool
for the job. You probably can see that
certain implementation takes more code
if you communicate with it. If you just
had a REST API, you can do it just in
one line. So you don't need to like uh
less code is less errors I was supposed
to
uh and of course we need to parse the
response where we get the stuff back.
Happily we can read different formats in
business central
um
and uh we it's it's not like uh
something special. I'm pretty sure that
most of you knows about it, but I
definitely seen some of the people and I
did seen the code reviews where people
like reading JSON as text and then start
like imagining some kind of parsing
techniques on their own. Uh it's gives
me a little bit of mental health after
it but okay. So with the new version of
Business Central, we now had a good
wrapper for the JSON objects that you
can directly access certain properties
with types.
Um, and again that's a big pain that was
in past. I think I did three wrappers in
three different extensions,
three different versions before this
happens. So it's actually very nice API
to to access properties directly.
uh
we you will have a cases for example if
you're taking like JSON where you're
looping through properties for each
fully support this and of course if you
wanted to you don't know which
properties you get in a file and you
want to for example loop through them
and get them individually u that's a
good uh way of doing this as well
so now uh over to Tranga for a little
bit of demo.
Okay. Uh I'm in BC obviously.
So we what we want to show is that how
this uh we build a small extension and
it's basically we have puppies and we
want to connect to a external web
service and schedule a appointment with
them. Now if you can remember we had a
five pieces. First piece was setup and I
recommend that we using we should use
the service connections. Now if I go to
service connections in here
it takes a little bit of time. I think
it is little bit slow today.
So we have service connection called web
deployment
and I go to web deployment and it
initially asks like what's the
integration type this is the interfaces
that we have been we have three
implementations of this for uh this
particular demo and for now for this
piece of the demo I'm going to use the
HTTP client
and uh then I'll be go to next
yeah there actually was supposed to be
a field there for asking for an endpoint
and a notification but probably someone
deploy some bad build. Oh, that's fine.
We don't need to ask we take you through
and then we finish that.
Now, if I go to this uh puppies, the new
one that we built any Formula 1 fans
here? Oh, I can see a few. And probably
you'll be able to make some connection
with these names and some of the birth
dates
reflect some memories as well. So I will
go with this first puppy
and I I feel that this puppy is not
behaving well. He's not up to his
standards. He's not doing well. So I
want to make a better appointment and
ask the vet why he's not behaving well
and why his behavior changed.
So if I show you the appointment
history, I don't have anything here.
It's blank.
Now when I click uh request wet
appointment, what it does is it will go
ahead and create a record on the show uh
appointment table and then it schedule a
job queue in the background and this job
q will trigger integration to the
external party.
So that's the triggering point for our
integration not the this action button
or the creating the record. the simply
the job queue.
So I will click request web deployment
and yeah request is sent. Now if I go
and check this
I already have this record. It's quite
fast. So that's why otherwise it should
have blank uh uh date and time and
integration will update it back. Yeah.
Actually on this point I wanted to
mention that uh because most of your
integration would need to be as
synchronous you need to make sure you
communicate back to user saying what's
happening right now. They will not get
an instant instant feedback. So good
practice is to do any kind of status
fields changing the visibility of the
button saying it's now engaged or having
something in effect box like in our case
that something is happen something is
scheduled
and the other thing I want to mention on
here is that we don't have any any logs
we don't have a way to trace back what's
happening in integration only thing we
can do is we can go back to uh job cues
and find out what happened in the job Q
there will be no job queue here it just
car on gone. Yeah. So, we can Yes. And
it's kind of frustrating because if this
works, it's fine. If it not, then we'll
be in a position that we'll have to
create sandboxes. We have to debug all
of those because there's no monitoring
in available with this approach. If you
want monitoring, we'll have to build
everything from the scratch. Yes. So,
there is certain telemetry of course
that will allow us to see any external
calls that happens to a system. But of
course, you don't see like the body of
the request. You just need see an end
point and uh when it happens
is it all. So with that uh yeah we have
VL I think it's you to talk about the
limitations. Yeah. Yeah. Um so awesome
and I think that you guys uh were uh
showing us in your feedback for the
question for this session that you like
AO integration that you think that it's
absolutely capable but it's certainly h
have certain limitation in terms of how
it can communicate
in in New Zealand we less have this
problem I heard here um in Europe you
definitely have some customers that
using def very old legacy systems
that have really strange formats and and
communication instrumentation. So yeah,
it's it's still limited in this point.
Uh but another uh area of limitation is
this scalability. When I'm saying
scalability is not like about the
volume. We can drop huge volumes with
business central cloud. Thank you
Microsoft for certain technical and
performance updates. But wherever we say
in scalabilities how this now affect the
organization
because in reality yes that's great it
can communicate with web appointment
service but in a real case scenario
organization wants to do something with
it they might want to like send an email
to someone else when this happens they
might want to trigger another process
within the organization uh that that
relates to this integration specifically
so this is where I'm saying the limit
limitation of this scalability you
implemented it in a the only job it do
is like one thing happen it goes to one
service that's it so uh yeah yeah yeah
so with those uh scalability limitations
it's kind of a deal breaker because when
you build integration you need it to be
scalable you will you should be able to
integrate more partners to into it and
connect to the more external endpoints
so is there any other possib possible
options available like any other
patterns that we can use which is
already available in business central
that we don't have to reinvent.
One of the options is web hook.
I know some of you think uh web hook
give us few minutes and we'll show you
how we can use this technique quite
well.
uh web hook is a real-time communication
mechanism that allows like system A to
announce something happened in the their
system to system B. So system B can
react to that.
This uh web hook is not real time. It's
closer to real time in the sense it's
not like 5 minutes delay. It's like a 1
second or 2 second delay that you get a
notification.
Second point I have listed is at reduce
resource consumption. How
in old integration method what we did
was we used polling method where the
system B let's say that system A and
system B have integration system A
generate those events
and system B has to come to system A and
ask knock on the door and ask like do
you have anything new for me sometimes
it has some most of the time it says no
I don't have it
system gets frustrated just the way that
You guys come to a conference, you go
home, you want to relax, but someone is
coming knocking the door and trying to
sell you something and then you get
frustrated. The same way the system gets
frustrated because it's using lot of
resources to answer these calls.
So the asynchronous me method is where
that uh these two happens in two
separate transaction scopes. When the
web hook method delivers the payload to
the system B and then it dumps the
payload there it it uh it will not wait
for the system B to process and give us
a feedback. It simply says hey something
happens take it. If you don't that's
fine. I'm going to move on with my life.
Yes. So from the synchronous
communication point of view, the stuff
that we discuss with you on a trigger
point, it's not something that you need
to enforce developers to make sure that
they always need to use job cues. It's
done there out of the box. So the way
how the web hook works is only triggers
if the transaction is committed. So um
this is how you don't need to follow
them and uh see how they actually
implementing any kind of communication
with external service. So another thing
is very important is this loosely
coupling thing. Um can you guys like the
light this if you know what is loosely
coupling is I think it's a buzz word or
not. So someone can explain there's two
people, three people in a room, four
people, but they don't have lights
probably. Um who can explain it? Um my
understanding of this is
um we had two different systems had two
different life cycles of systems. They
evolve independently.
Um whenever we talking about loosely
coupling we trying to make sure that we
are not tying two system together so
they can live separately and they can
mutate separately break separately and
uh marry hopefully after all this
where is my cool so I wanted to walk you
through how the web hook works in
general I hope that most of you knows
but that's a really basic principles any
web hook works the same Okay. So, oh
actually I had a lighter. Cool. So, we
had a which we call the consumer someone
who is interested in the stuff that
happens in our system. So, what consumer
do he's asking the web hook service to
say I'm interested in this if you have
something for me that like this is what
I'm interested about like this is type
of event that I'm interested. So if you
will happily have any of this event in
your system, please call me back and
this is my number which is like a
notification URL. So this web hook
service is had a catalog of all these
subscribers
and he actively maintaining this
catalog. So if in our source system or
event generator
something happens like in our case the
new appointment is requested
our web hook service takes care of
looking for where which parties are
interested in this event and in parallel
they're sending
this payload which is about certain
limited information about the event to
external body. Uh so that's in nutshell
how it works in business central we do
have few versions of implementation of
the web hook probably you heard about
web hooks since I think 200 three
versions before I think three versions
before okay and there was like this we
call it web hook version one the way how
it was u designed is that every time
when you as a developer creating pages
API
system registering the web hook for all
the record event for this page. You
probably didn't know about this before.
I actually didn't know that every time
when I'm creating API page, this is what
happens. And um but the rest of the
process looks similar as for the web
hook button. We had a oh sorry wrong
button.
We had a consumer. It sends a a request
to a subscription endpoint.
Um our business central web hook
creates a record in a API web hook
subscription table
can responding back yes I'm done with it
when something happened in the business
central like a new appointment that's
very interesting happen
every time on global insert modify or
delete what system do is for your
beautiful API page that you created and
you didn't know anything about it goes
reading this table and looking if
someone interested in your record change
and then probably in most cases it's not
but if it is this is where it creates a
new record in API web hook table web
hook notification table and then the
background job picks it up and actually
send this to the external service.
This model was great as a first
implementation
but it has limitations. But it has huge
limitations. Has huge limitations. One
of the main go back. Yep.
We clicking together. Yeah. Yep. So one
of the main limitation is only record
events get trigger uh become the webbook
events. As Vlad said every time you
create a page, it goes and registered
like okay this is something uh something
suitable for web book. Let's enable it.
And once that is enabled, every time
record insert, modified or delete, it
triggers it. It looks for a catalog for
things that is not available or things
that partner doesn't need to be
implemented.
And with that, then there comes the big
performance overhead on the global
triggers.
So if you have a extension or a solution
which has hundreds of API pages for
different entities that means you are
without knowing slowing down the tenant
and uh the other thing is work this can
be actually not the limitation this can
be a workaround you want the pages but
you don't want it to be enabled in the
web hook then you can make the uh O data
API key as the composite key. So then it
will not register it.
And the other thing is the first version
of this is every 3 days the subscription
expires. So the whoever subscribed to it
has to renew the subscription every
3day.
So this is going to be another problem.
Sometimes some of the implement
implementation doesn't have this kind of
a capability of redeeming the
subscription every 3 days. So they
wanted to leave it like subscribe then
leave it until they purposefully uh
expire the subscription.
There are a few other limitations uh on
the bottom of the page screen. Those are
like more of the technical one where we
can't use the system table for the APIs
and API. If you build the API pages as a
query object then this won't get
triggered as well. So that these are
limitations and also work around to stop
this uh global triggers getting uh
ringed every time something happens in
BC. So I would say that webbook version
1.0 do not buy it, do not use it uh for
any of implementations. Yeah. And this
is what Microsoft identified as well.
That's why they bring second version of
it. And uh I'm not sure if this is where
you guys seen it before. Um, that's a a
big change. The big change because it's
first of all, it's not defined by the
page APIs. It gives partners full
flexibility to create a um events in a
for the web hooks pretty much anywhere
within the business logic.
It doesn't have a limitation of the
performance overhead because it's not
technically tied to any kind of record
change. It's yes it's it's going within
the code but it's handled on a platform
level. As soon as the business event is
triggered on a platform it generates a
new record um on the web hook system to
actually send it to external service.
Uh another limitation that we bypassing
with this version is in first version we
just by was sending as a payload just
the primary key of the record. That's
it. Right now with the business event,
we do have options to support a little
bit more um uh payload within this
request.
Uh yeah, and actually it's as I said
like it's supporting a custom event so
any partners can can build them. I
wanted to show you how it works pretty
much the same as um the previous
implementation but we had another
endpoint to register this subscription.
It goes to different table when in
business send when when in business
central the business event is triggered
as a procedure. This is where this
happens on a platform level
to initiate this system will create
internal external event notification
record for all the
uh external event subscriptions. We
didn't find any code unit that execute
this. That's really like a the data is
presented for us to see what is
happening there, but actual whole
execution happens on the platform.
So that's that's a big difference. So
but that's the issue with this I would
see because it's still preview.
If you go to Microsoft learn website and
find out it still says preview and it
only has limited number of uh external
business events. Why is that? So we had
this question and we asked from
Microsoft actually the people who was
actually looking after this uh
implementation.
So the reason was this to be in preview
is Microsoft is currently looking for an
option or a solution to deprecate these
certain events without breaking the
integration agreements
which means that they planning to push
this forward. They they think that this
is going to be the future of how we
integrate with external systems but they
are currently looking for a proper
solution to uh uh proper solution. If
the partner was to duplicate one of
these events, how they going to do it?
So that's the part that they are
missing puzzle of that and why only few
events right now because Microsoft
doesn't want to go back and change this
uh when we go to GA in probably within
this year. So they have only added very
limited events which they think that
won't change in the for the foreseeable
future. But uh good thing is we are
allowed to do this. We are allowed to
add business events as a partners. So we
can easily add business events for that.
So that's what we're going to show you
how we going to do this.
If you remember that at the start of the
integration uh this session we had five
pieces of the puzzle setup uh trigger
mapping uh response and request. So now
I want to go back to that same uh
structure and see how we going to do
this. For the first one is setup. Do we
need a setup?
Uh no. How we doing do the
implementation? Only thing we need to do
is we need to make sure that permission
is there for the users who are
subscribing to the business events.
But if you go to Microsoft learn, you
will see like this kind of a lengthy
article about how you enable business
events. It's not required.
We tested it. We check with Microsoft
and they're going to they need to update
the documentation because none of these
are required to enable business events.
Yes. So to to make sure that this
virtual events of business event
working, you don't need to connect it to
a data versse. You can just be by
yourself in business central. So works
great. Yes.
And on the permission level there are
two things that you need to uh make
sure. One is the subscriber a user or a
service account should have external
event subscriber permission set assigned
otherwise you will get a permission uh
error message at the time of subscribing
saying that this particular user doesn't
have the permission required.
And the second one is the same
subscriber need to have read access to
external business event definition
table.
That's all you need to do. And as soon
as you uh complete that the setup part
of the business events is complete.
Now comes the trigger and Vlad's going
to talk about that. Yes. So from a
trigger perspective, right now we
finally need to implement business
events.
So um that's pretty much all we need to
do. Um
and because again it's basically by
nature it goes outside of the business
transaction. So let me share my screen.
I will show you how we're doing this if
this works.
So in our case
um
uh yeah where is our web hook
implementation?
Hook. Cool. Um, so, oh, actually I have
a slides for it, I think. Yeah. Yeah,
you can do the slides. Yes, it's much
easier. Sorry.
Uh, yes. So, you need to create a new um
event category for the business event.
So, you extend an event category to
bring your own. It's just a
categorization of the business events.
Probably for your app, you'll be using
this. Maybe for app and API level, you
will be using this. Um actually it's
probably would be only for the for the
app level.
Um the next thing you need to do is
actually
um define this business event and you're
doing this by creating a new procedure
in your extension
which has certain metadata that required
for the business event to be public. So
which is like a name of it. This exact
name is used by subscriber to subscribe
to this event.
Um you need like a meaningful name for
the users. This is more for u power
automate or some kind of external
solutions that potentially wanted to
read the definition of your event and
present it to a user that doing some low
code stuff or actually we can talk about
AI right now. your MSP server
potentially will be will be able to read
some of this. Um and a little bit of
description of course and our custom
event category.
Um one more thing that you need to do
here and it's quite interesting one is
this required permission. Uh Tango
already talked to you regarding what
permissions
the subscriber needs. But the way how
this works is very interesting. the
subscriber user send a call to business
central saying I wanted to subscribe to
um to this business event and what
system do in a moment of subscription
it's checking if this user which
subscribe to it do have
this permission
because after this moment Business
Central will happily deliver him all the
information that he subscribed to And
this is exact moment when uh from a
permission and security standpoint we
wanted to make sure that external
service really have an access to the
data that we are exposing we wanted to
expose to to a service.
Uh cool. So as soon as we have this of
course we need to call our business
event just a regular call as another any
other procedure from a best practice
point of view. The only thing is uh is
to join all your business event in a
separate code units. Uh so then you know
what is your business event in one place
and then you call in this code unit and
the procedures from pretty much anywhere
within the transaction. Doesn't matter.
It will act similar as the um as a job
q. Uh so it will only be triggering this
subscription sorry triggering this event
uh only if the transaction is committed.
If something will be rolled back there
will be no external service code.
Yeah I think that you pretty much
covered it. Yes pretty much covered.
Yeah. So over to Tanga. He wanted to
show you
how we can use an API for business
events. how we can subscribe it from
postman.
So this is my postman uh application and
I have authentication set up and I'm not
going to go into details about that.
So before I go into external events or
any event I want to find out what are
the endpoints that available to
subscribe or understand business events.
So I have the base URL tenant ID the
environment name API/ version 2.0 and
dollar mark. So once I do this
I get the payload back and I can see
there are two particular endpoints
available for the external events. One
is called external event subscription
and the second one called external
business event definitions. So what are
the difference? Let's find out.
So what I do is I want to find out
what's the external business event
definition means. So now the URL get a
little bit different.
I will have API Microsoft runtime
version 1.0 zero external business
definitions.
Everyone can see the screen right like
uh okay good.
Now once I do this once I make the call
I get a payload again here
this time it brings me all the business
events available within business central
whether it's a custom business event
added by partner doesn't matter it
brings all the events Microsoft and uh
partners so if I scroll further down
I think bottom of the page we have the
custom business event that we created in
here you have the app ID app ID means
the app that implement this particular
business event and the name of the event
event version payload what's the payload
will be look like display name
description the category which we
created with the extending enum and
what's our app name who's the app
publisher and the app version so it
brings all the information about the
business event and also the app
now uh
before we going into the business events
that custom business event that we
created. I want to focus on this
customer blocked one because that's the
easiest one to uh showcase you guys.
Now, if you remember, we had two
endpoints. One is the external business
event definition and the second one was
external event subscription. So, I'm
going to do a request to this and I can
see it's a blank doesn't have any
subscriptions yet. Now I want to go and
create a subscription.
Now I have this payload. So you can see
the endpoint uh URL is external event
subscription
and I'm passing the company name which
is the company that I'm interested in to
subscribe into. So if you if the tenant
database has multiple companies you can
simply and you are interested in all of
these companies then you can simply
remove this uh company name parameter
then it will subscribe to all the
companies but in my case I only want to
subscribe to one and then you can pass
the company ID, event name, app ID,
notification URL. Uh this is a dummy
endpoint that I have. This is the
endpoint that I created to monitor
what's my request would be look like.
And then clan status. Clan state is
basically a token that you can pass it
to the external system to validate.
Now let me send this.
Now I get error. It says user does not
have required permission for external
business even customer blocked. I'm
pretty sure I have all the permissions
there. I don't even have to check. I'm
100% sure. So what's the problem?
The problem is
business events. Even though your
payload is incorrect,
it does not give the error saying that
your payload is incorrect and your some
of the payload elements are missing. It
doesn't say that. It says the permission
uh issue. So what was missing was the
event version.
You can get this event version and all
this information with the uh business
events. So you have the event version
here. You need to get that and then put
it here.
Now I I think that my payload is all
good. Now I send the
subscription. Now I have all the
uh
information back to me with the
subscription details like when it was
created and who was created. All this
information is here now. Now my
subscription is created against the
customer.
Now now let me go back to business
central. I'll go to the customer
and then I'll pick this customer which I
was using for the testing as well. So I
don't want to change it in the middle of
the demo. So I will change this uh
customer status to invoice to ship
and I go out of the record.
Now if I go here you can see that I have
post request right now it's 12:19 a.m.
in New Zealand.
So if I go and inspect a little bit of
this the payload
uh header has lot of information. Now on
the body part of it, it has the company
name, company ID and the URL for the
exag uh record and the web plant URL and
what's happened with the status. It's
been now blocked for ship.
Now this gives me all the details I want
as a external system to react on it. If
I want I can call back business central
and get the full details about this
customer with this particular URL or if
I don't want I can simply ignore it as
well. Now that's the part of where we
creating the subscription.
Now let's say that we run the project
and we don't want to have the
subscription anymore. That means we want
to unsubscribe it.
For that uh you need two things. One is
the subscription ID. How do you get that
is like two uh there are two ways.
Either you run the list all subscription
details uh method or at the time of
registering it send you back the ID you
can store that or uh you can store that
and also you need to have a E tag for
this.
Now if I all have all of those
information I simply do is on the
endpoint uh URL external uh event
subscription open brackets and put the
ID and on the header I have if match and
the E tag
and then I click what about body?
Yes, good point. in the body you need to
pass a blank uh JSON object otherwise it
will give you an errors. Don't ask why.
That's probably why it's still in
preview.
Yes. So uh now I deleted the request and
it says 204 no content and let me go to
this one and run it again. So it's blank
again. So there's no subscription
available for this particular uh
database.
And that's basically how the web hook
works when you look into the the API
level. We'll be going into much more
details about this in a different uh
integration layer.
Yep. Cool. So thank you very much Ranga.
Uh so you ranga show us how to do like
this manually but potentially you are
talking about that this would be done by
from some kind of integration layer.
We we we love integration layers and I
think that um some of you guys who are
responding to our question what where
are you doing your integration business
logic and even like most of you talked
about AL we do see that there are a few
pro integrators in a room who's actually
doing Azure integration services I
actually wanted to rerun this poll now
because probably some of you not using
the app so can you light our And who is
doing AL only? AL only. Oo. Okay. No
lights anymore. But like I would say 30%
of the room. Yeah, makes sense. Cool.
Who doing all the integration of Power
Platform?
No. Not not good. Who is doing only
Azure integration services?
Cool. One. No. No field. There's a few
more there. Okay. Probably my
you need glasses.
Not the lights, just glasses. Yeah. Uh
what we see is um even if the customer
requirement starts to be small, every
time every new months they come up with
something new. So you're building your
integration within a and then like in
three months time they start to want
some more. they wanted to have another
system to communicate. They want to have
like some kind of guy who is main
managing this. So in most cases what we
are trying to do is to introduce
customer to like variety of options in
the integration space. uh in a in a
terms of this conference we will be more
like looking into Microsoft offering in
for the integration services and uh
that's probably would be part of our
demo but uh web hooks is absolutely
standard thing any integration layers do
support some forms of web hook and they
will support the way how business
central is doing this actually some of
our demo part is doing this on like uh
still in power automate but like using
the HTTP connectors. So you will see
that it's pretty much works in any uh
any any space like this.
So
that's was an interesting discussion
regarding where to use the power
automate in Azure application services.
I think you've seen some of these slides
for the last five years many many times.
or not like bring you some our
perspective on this but we did a lot of
integrations. I was a big fan of power
platform. I'm not
in terms of integration. I'm sure that
you like love it. We always had this
argument at uh our company that not
recommend uh power platform then I find
excuses to not to use power platform and
then uh we always go to Boston light
like we presenting our cases and most of
the time I think I won. Yeah you do.
Um what we found is like yeah there are
certain technical differences but um the
main thing is you who will be supporting
this and if the customer do have like a
small workflow they had really power
users they do wanted to use a power
platform they do have a person in the
room who's like yeah sure I will go to
this run I will rerun it this is where
probably you can um be within the uh
power platform
But anything else this is where Tanga is
definitely a winner and especially like
but most of the cases what happen is
blood the person who was saying that
okay I will do the rerun he's on the
leave when this things go south so then
someone else has to do this yeah we so
yes we charge customer to go and and
help them with it uh but like uh I do
see that um another aspect where the
most of our integration Now moving to
Azure integration services is because of
security. Um more and more our services
do require strong IP filtering the stuff
that you cannot do in a low code system
or serverless system. So that's
potentially like I think most of our
just like integration transition from
power platform to uh Azure integration
services happens because of security.
Cool. So, let's do a another demo. Demo.
Okay. So, that's me.
Yep. Works.
I don't need any of those now. And I
want to go to business. Oh, yeah. I
think it's my demo. Oh, that's fine.
I'll do it.
So uh in business central uh with the
business events we get a little bit of
what do you call uh monitoring
capabilities
not 100% but n I would say like it's
closer to
uh 80% or something like that. So in
business event uh you can find if you if
the search you will able to find it as
well but we put a actions here because
it's easy for us to navigate through the
demo. If you go and click on the
business event subscription, you will be
able to see all the subscriptions
currently available right now. We don't
have any subscriptions. So that's why
you don't have you don't see anything.
Now let me go to power automate and I I
have power automate flow and I'm going
to turn it on.
This is why I don't like power automate.
Now I click that but it doesn't show me
whether it's been turned on or not. It
is. It is. You just need to believe, you
know. Yes.
So, I need to do a hard refresh. Now, it
says turn on. That's okay. Now, if I go
and edit this one
and I if I open the This is changed.
What? This is changed. That's fine. Now,
just new designer. Yeah. Which everyone
hates, but okay. So, I'm going to go
back to the old one. That's the first
step that you do when you opening the
power to me. Okay, this looks much
better now. Old school. Yes. Now, if I
open the connector uh the trigger the
connector, I can see the environment
name. I can drill down. Come on.
I can see all the environment names that
I have. So, in this case, I'm using
tech. I can't use this one. This is my
wife's uh tenant. So she will get
furious if I play with that. Uh now it
will show me all the events here as
well. So this is really good if you are
like a low code user. This is really
good because it gives you all the
information. You don't have to memorize
or have to do anything other than
clicking this arrow button to drop down.
So you click the appointment and this is
something uh optional company name. If
you want to subscribe to all the
components in the uh database, you can
keep it uh blank. Otherwise, you can
select it at that also a drop down.
Actually, this is u was an interesting
point. Uh why it's in the preview. When
we were starting preparing this demo
like few weeks ago, there was no such
property. Now it's appears. So now you
finally from power automate at least you
can select the company that you are
subscribing to. So now I won't go to the
other parts of the power automate
because we will be coming back to this
particular flow again. Now if I go to
business central and refresh
if my connector works well I can I
should see a one particular
subscription.
Yes, it's there.
Now in this one we have user ID that who
created this subscription. So one of the
things that you notice is in the power
automate we are not with the power
automate and with the business central
connector we are not allowed to use
service to service authentication. So
that means we need to have a named user
for this. So in this case my user
account being used and this is my user
account details here. Yeah but we can
show you how to bypass it. Yes we'll
come back to that and then this
notification URL. This is the power
automate notification URL that it will
be getting called.
So yeah, that's how you simply enable
the power automate and then uh to the
subscription.
So let me go back to presentation.
Yes. So from mapping perspective because
you're sitting somewhere else you have a
plenty of option to map your data from
business central to um to your target
system hopefully not so complicated
legacy I don't know what was it EDI no
okay anyway um yes so but definitely you
will have way more options in this space
and u what we told you that business
event is triggered just with the data
that you define in the parameter. So
probably wherever your integration layer
is, you need to go back to business
central using the uh some kind of
reference from your uh business events
call back the business central API fetch
the data that you need for your
integration. So there is no mapping, no
nothing, no requirement for the data in
BC. This is something that the external
s service should take care of.
And uh from a communication point of
view, of course, wherever you want in
Power Platform and the Logic app, there
are like more than 1,400 connectors that
are able to communicate pretty much with
anything. Um that's not the topic of
this conversation, but we had a friend
who's like actually working on the team
for a logic apps and that's an
interesting challenge for me for him.
like every month that customer come up
and saying like oh you know let's do
this and it's like random file
drop uh process
um from a response perspective we using
our favorite business central APIs to
push the data back. So in case of our
demo we do create uh our web appointment
API where any external service can call
and update the information about the
appointment.
Cool. So let's go back to the demo.
Okay.
Now uh I showed you bits and pieces of
this web hook like how to create the
subscription and how the power automate
connector works. Now let me take you
through the end to end and then explain
you how these uh work in the power
automate. So for that first need to do
is go to service connections. If you can
remember that we had different
implementations of the integration. So
the first part of it we use the HTTP
uh but for this part of the demo we want
to use a web hooks.
So it's next and finish.
So now from this point onwards when we
create a new appointment we are not
using HTTP we will be using the web
hooks.
Now uh I'll go to my puppies.
This time we'll get a different puppy.
We I'm okay. We'll get the uh this one
different Formula One driver.
I I never thought that they hairy so
much. Okay. So for this one we we don't
have any appointment yet and what I will
do is I will click this one and then it
will initiate a
external BS event which will call the
power automate and power automate will
take it over from there. So request wet
appointment for this.
And now if I go to this
the uh the data has been updated.
Now let me see.
Can you show the business events
notification? Yes. Yeah.
So
data got updated.
And now if I go to business event
notifications in here
and sort it
you can see that at 12:35 exactly now
the notification has been sent
and yeah so you can see that there are
retry counter and this is basically the
platform exposing us an information how
it's execute the request to a external
service. Yeah this is where blood was
trying his best to make some demo work.
Yeah, it was interesting. Yeah. And uh
if you want to have a log of how the
subscription was subscribed,
unsubscribed and event notification, you
can go to business event log and it will
show you like whether the subscription
has been created, when it's been
unsubscribed, when the notification has
been sent. This is like a full picture
of it.
And now if I go to power automate, you
can see like 11 seconds ago a flow has
been run.
I'll go into that.
So what we'll do is we get uh details
like sandbox environment name the event
for the event we are just passing the uh
appointment system ID and then this is
the company ID
uh let me click download. This is the
how the payload looks like
and see on the body you can see all this
information. I can make it a little bit
bigger. Yeah.
Is there any payload? Yeah, this is the
Oh, cool. We had our appointment system
ID. Yes. Now, with this system ID, what
we do is we do a we use the the business
set connector actual get record. Since I
know already know the actual system ID,
I'm going in there passing the system ID
as a row ID and it takes the uh record
back to me like full business central
record.
So it has all the records. Now I do the
mapping part of it. So these the only
two parameters that required by the vet
appointment system. So I'm do the
mapping in the integration layer. Pass
it to the vet appointment endpoint
got the feedback saying that it's
scheduled and this is the appointment
date and time. Based on this information
I'm going to go back and pass the record
ID that I want to update. And then this
time I'm passing the date time. So now
the business center will get updated.
You obviously see that this is like a
for a demo. We don't have any error
handling or any other uh what do you
call mechanism to implement the
authentication. But this is to give you
update on how you can do this in the uh
integration layer.
But with this connector there are like
lot of limitations and Vlad is happy to
show that on his laptop. Oh yeah
buttons.
Uh cool. So limitations.
You want to break my flow? Okay. What?
Sorry. You're going to break my flow and
show it. Yeah, of course. So yeah, the
first limitation that we already
mentioned is there is no service to
service connection
like really we asked uh this question to
Microsoft multiple times and uh we're
they definitely said that their um
business business events will become GA.
uh but for the manage uh service
authentification there was nothing for
now. I think this is a probably a
slightly bigger change because business
central uh standard connector is widely
used um and um certain feature would be
harder to implement for them but and
there's a busy idea about the service to
service authentication and if you can
please go and vote for that and then
they will be able to put that into the
actual workload. Right now it's in the
backlog. Yep.
So another limitation that we see is um
as from a development standpoint it's a
little bit tricky because yes as um
Trunka showed you before you can use
this fancy dropdowns to select your
environment company and API but probably
in real time scenario you do need to uh
use like environment variables for all
this and for example when we're talking
about like an update record um connector
if I will start like changing something.
Let's say, okay, I actually want this to
be a dynamic content. Where is it? No,
this modern one. Should I switch to the
classic?
Yeah, as I said, starting point for
everything.
Change to classic.
Can you keep it classic?
No.
Come on.
Yes.
Let me try to change environment
and um I will put some environment
variable for this. You can type
something else. Just type it. That's
fine. Okay. Yeah. Oh my. That's
definitely something wrong. So we are
seeing this as Yes. It's for like a low
code guy who wants to do something for a
particular company. But if you wanted to
try to squeeze anything out of it
meaningful, you might have an issues
like this. Yeah. Especially uh
especially when you want to uh deploy
this uh power automate as a solution to
your environment. You can't parameterize
it because the the all the actions work
with with the connector uh connector
body. You can't actually write your
custom code or custom uh
parameterization with this. As soon as
you start doing that, the connector and
the actions goes out of shape
which is going to be a deal breaker for
most of the integrations. Yeah. So what
I wanted to show you is um we tried to
do the same thing but using standard um
HTTP and web hooks connections.
And the reason for it is we wanted to
use manage authentication. this
connection do support manage
notifications. We actually can declare
an app for this. Um and we don't have
this issues with mapping goes out of
shape weird errors. You just do the
mapping for HTTP call directly in your
body.
So first of all I want to show you
quickly we have this app
nice name not sure where you get it. um
that's represent um our flow
because of this web hook is so standard
it's fully supported with a standard
connector. So you can see um the
definition of this web hook trigger is
you need to define what is your
subscribe endpoint. In our case is this
external event subscription API.
We pass in the body the one that Tanga
was showing in the Postman.
um it has like a a generic variable from
the web hook trigger that basically when
you're enabling this is generates every
time a new callback URL
and then you do have an unsubscribe
parameters as well
where are they here so you define in the
endpoint and you actually even able to
extract this ID that you get when you
call the subscribe endpoint because the
way how it was working you send a call
it returns you back a response with an
ID of your subscription. So this
unsubscribe should get this id and in
power automate using this um connector
you do able to access this value to be
able to call and unsubscribe one
and um do all this weird thing with
delete passing this empty body to
unsubscribe
just works like this and of course this
is where you're actually able to
authenticate to this endpoint. points
using the manage um manage not managed
sorry
the the OS and the service to service
authentication.
Cool. So that's for the web hook
trigger. The rest is pretty
straightforward. Yeah, we do use uh our
puppy API
and the payload that we get from the web
hook. The slightly difference from what
you see in the connector is that um the
way it works
is
it's not sending you one event. If if it
can send you 20 events and the 20 event
happens in certain point in time, it
will send you all 20 events in the same
endpoint. So the data set that you get
um on your site is actually like array
of events. So that's why on my side I'm
looping through them. I'm getting that
appointment uh from business central
API. I'm sending this to my service
uh getting back my appointment date and
then calling business central API again
to update my data. So no limitations.
Yeah. So adding to that about the number
of calls uh if you trigger this
particular uh external business event
within like 20 times let's say take a
random number 20 times within a very
short period of time you will see in the
power automate flow if you use business
central connector that it has a 20 runs
but if you use this uh web hook method
you might only see one run and within
that one run you will have a body that
you have to loop through 20 times so
that's why blood had
for each loop. So you have to loop
through that.
Yep. Yes. So um as a reference for this
materials, we wanted to leave you with a
link to a business central um
documentation.
Be aware that you will see like this
long setup that not required at all. Uh
another strong takeaway is you can use
it in production even the business
events from Microsoft
they this is what they commit it's fully
working fully scalable we tried it
multiple times on a big scales it's all
deliver message as it promised
and yeah we are you oh you forgot to
publish the code publish the code yes so
the code for for the demo that we did is
on GitHub up. So, please go check it
out. Um, and u hopefully
um we we got the slightly help you to do
some integrations.
So, now the questions. Unfortunately, we
don't have the t-shirts because uh they
ran out.
Okay. Uh because I'm publishing the I'll
do that quickly. code is the same as the
first code.
Sorry. Oh, yeah. Both. Oh, sorry. Thank
you very much. Tanga, please fix any
questions that which one like a
question. The QR codes are the same.
Yeah, we we at least make one fail.
Oh,
the external business events. Um,
there's a protocol that you showed us.
Sorry, there's a protocol for the
external business events you showed us.
Protocol? Yeah, like how many retries
and if it was successfully or it failed?
Um, is there like a config or setup for
it so that we can define a maximum of
retries? Okay. uh we didn't experiment
with retries but I think that how many
of them was uh 19 times that that's the
maximum I have seen okay
but uh there is no setup for this and
there is no setup in definition of the
business event so it's just platform
thing okay thank you
no t-shirt sorry really we were said
about this as well
thank you Uh is there a way when you
make the event uh subscription to pass
along uh something to be used as a
header or something like a subscription
key that can be passed along in the call
back? Uh no unfortunately not basically
the subscription is um you just pass in
the notification URL but what you can do
is probably within your notification URL
it's accept any URL so you can encode
like in a query of the URL some
parameters. So then your back end will
get it with some metadata that's
specific for your subscription only.
That's kind of an option for these
parameters
for that. Uh client state is not passed
with an event. That was
yes.
Uh oh yeah that's John.
That's cheating.
kick him with a with a mic. Um I'm
wondering if the record that calls that
event can be traced back like do I have
a record ID of something in the
notification
like which exact record that you
inserted the appointment in example what
we did was we actually pass in the
system ID for of that record and then
also it in the URL H yes but it's inside
the body I want to see it yeah I I think
we we probably need to double check this
it's a really good
Um there should be because like every
notification that we get do have a
unique ID. So I'm expecting actually
that this would be in a in a payload as
well. Okay. So then you can trace it
back. But I will double check this and
probably after conference I will find
you. You can message me on teams.
Uh there was a question from that side I
think. Yeah. And
whoa. Sorry.
Almost there. You're not a football
player.
Why when you subscribe to the business
events, there is a version field for the
for the event? Yes. So my understanding
that the versions is this kind of
prototype of instrumentation for
Microsoft in future to to allow you to
have like multiple uh definitions of the
events. Yeah.
um we didn't see in the and I think we
didn't show this in the metadata
uh that we have that uh the version one
this is currently an optional parameter
so you're not like mandatory to do this
and you will get like the version as we
do like 0.0 zero but you will see that
Microsoft all day business when they do
have a version but not for the partners
yeah we can't we couldn't add the
versions but in Microsoft once they had
the version so we are not actually sure
how we can do that we might have to
check with Microsoft one I I thought
it's an optional parameter you it's not
yeah it's optional but when we're
creating the it's not creating the event
like when you're publishing the event to
the uh tenant we don't have option of
creating that this is the version two or
version Okay. Uh, so need to find out
what how they do it.
Cool. Uh, there was someone else.
Okay.
New Zealand is like well known about
like rugby players who can throw but not
we. We are. And uh what about consuming
um external system webbox from uh
business central because here uh this is
external system that consume business
central web but maybe we want business
central to interact with external web.
So how to publish uh aure area to to
send to this uh web hook. Yes. So if I
understand the question correctly,
you're talking about that mic uh the
business central is interested in some
web hook somewhere else and you wanted
to react on it.
That is not possible primarily because
all the API in business central has an
authentification. You can see this
notification endpoints they are
notification free. So there is no
anything that you can enforce
external service to like authentificate.
Again, if you're using the normal
subscription, of course, this is where
we're talking about some kind of layer
in the middle that can subscribe using
web hooks or wherever and then just use
a business central API to communicate
back this information to business
central.
Oh, can we pass it? Yeah. Yeah. Yeah.
Yeah. Go for it.
Um
so the web hook thing looked like a
oneway um one way thing to me. So what
happens um for example in power automate
we have an error. So how do we tell
business central we got an error here?
Yes. So you're done.
So the web hook the the the protocol is
defined in a way that you receive you
accept.
So you need to like whatever service
handling the web hook it needs to accept
as acknowledgement soal meaning that I
get it
how I get it it's not your problem and
the only thing what what business
central will do it will retry if you
will not return 200 it will start
bombating you with retries but it
doesn't care if like eventually you're
done like it doesn't care whether that
you handle it or not. It's simply
passing the payload saying that there's
something happened in my system. Take it
do whatever you want. If you fail in the
other system, Mr. Central doesn't need
to know about whether it's failed or
not.
Yeah. So this is from an architecture
point of view. You need to make sure
that this is two decoupled system. They
live independently.
you can say that okay I'm expecting
something from external service but uh
it's up to to them to handle it and
potentially you would need to have a
certain instrumentation maybe to follow
up on it or maybe external service can
go and inform a user something happens
some pattern that some of our teams
using is basically you you sometimes
send a notification that something is
done or again the error handling
instrumentation whatever you use is
reporting back that the integration is
failed.
Yep. We had
there. No, that's far. We actually Whoa.
Oh, that's nice. This is a guy who
definitely needs a ticket to New
Zealand. I can't.
So, regarding that, uh can we use
telemetry
on the power automate end to uh log
these these kind of things? So we can in
the same application insights uh space
so we can correlate these events better.
This is uh probably uh no for power
automate but yes for logica. Yeah
because logic app. Yes. Yeah, you do
have rarely limited access to actual
subscription u calls and even for this
one for this demo I like spend an hour
try to understand how to extract this
response ID from a subscription from a
subscribe call to unsubscribe
and like there's no documentation for
it. So uh hopefully thanks to certain
ideas from uh from Gemini and uh some
limited one I managed to get it but yeah
it's uh it's hard to trace especially
with a power automate absolutely
different story for the for the logic
up. Yeah you get the full control over
what are the telemetries that you want
to pass and then on top of that you can
do the monitoring as well. So it's
really good.
Cool. No more questions. questions.
Good. Thank you very much. Thank you for
being on a BC Tech Days. That's the last
session. Hopefully, you will be joining
the closing one. Thank you.
