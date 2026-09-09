# Validate() - all tables / all fields / always

- **Source:** https://www.youtube.com/watch?v=EucBX5IYt6k
- **Video ID:** EucBX5IYt6k
- **Channel:** mibuso.com
- **Published:** 2024-06-16
- **Duration:** 89m25s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Thank you very much. It's actually quite
impressive to see that many people being
interested in a simple topic like
validate triggers. I mean,
um
that's really awesome. Okay.
Um
So, we're going to talk about validate
triggers. Uh as you can see from the
from the slide already, um we are quite
drastic in our opinion. And we want to
explain a little bit to you
um
what constraints come with this and how
we can get there to actually achieve
that goal that we put on the slide.
So, let's first introduce ourselves. Um
This is Christian. Um he started in BC
development in 2019 actually with NAV
still.
And um
he provided many ideas to me uh about
the LinterCop rules, the very first
starting of um
getting the idea into into place and
everything. Um in his daily work, he is
mostly concerned with or pretty much
concerned with DevOps and pipelines
building and therefore also PowerShell
stuff. He's
probably far better by now with
PowerShell than I am.
And he really likes to ask these
annoying kinds of questions. And he came
to me
um
and asked me, "Well, do you always
validate?" And I was like, "Well, you
cannot always validate, of course,
because there's like
certain situations where you have
obviously cannot. So, it depends." And
he talked to me about this more and
finally convinced me
that it's a good idea to always
validate. Um so, that's why we're here
today. If you want to reach out to him,
you can either do that through GitHub or
on uh the Discord BC professionals. If
you don't know about that, uh go check
it out. It's a really cool place to be
to uh discuss any kind of um
topics around Business Central.
All right, thank you. And uh with me is
Stefan Maron. You probably know him by
now.
He has a lot of stuff on GitHub, most
prominently probably the um code history
and the recently added uh code history
for sandboxes with nightly builds. You
can check out um changes on a daily
basis.
Um you can reach him on Twitter.
He
recently started doing live streams on
YouTube, Twitter, and
a bunch of other
platforms. Um
you probably want to catch that as well.
Okay.
Um
so let's look at the agenda first. Um
we thought that maybe it would be a good
idea to first get us all on the same
page what we're going to talk about when
we say validate trigger. Like, what is
good validate code? Um what
and and how you can structure that.
Um afterwards, we're going to look at a
long, very long list of concerns. We uh
we asked around on Twitter, in the
community, what you think about this
topic, and we picked up as much as we
could as we as we can,
and um
compiled that and gave you our opinion
on all of those concerns, if you want to
call them like that.
And then of course afterwards, there
always at least some
exceptions to the rule, so we're going
to cover those as well.
And at the very end, if we still have
some time,
we we might do a longer Q&A, let's see.
Um but if there is time left, we have
some related topics that somehow are in
the same scope, but not exactly cover
like not directly validate triggers.
So,
what is the definition of validate
itself? Like, what is
um what does a validate do? What What is
it all about? So, validate
triggers, like if if you call validate
on a on a record variable, this does
exactly two things. It checks like
validates the table relation if there is
one, and if it isn't turned off the
validation, and it does call a bunch of
code. There is five places in in total.
It's the validate trigger on the table
itself. Then around that, you have the
wrapper of the table extension with with
on before and on after validate. And
then around that, you have the event
subscribers. So that's actually like
what you see on the slides. This is the
the order of execution how how those
events get get executed. It does not
check
basically everything else.
Decimal places, min max value, chars
allowed, and I think there are more
properties that are that should be on
the list.
Um
But we didn't we didn't find anything
else that is actually
validated with the validate. Um so,
yeah.
This was a surprise to us as well. Um
we were going through this list of
decimal places, min max values, chars
allowed, and all, and um looked into
what really gets checked when we call a
validate, and it turns out really only
the table relation and the validate code
or the validate triggers.
Okay. And those other properties seem to
be only be valid for user interface
validation. So when a user enters
something on a page, then you get those
those checks as well, but from code,
they're not executed.
So now, what is our idea of good
validate code?
Um
Validate code itself should validate the
data. Like you you want to validate if
the the data that the user puts in or
that somehow gets in written into the
field is valid. Um
And then also like because we don't
really have a better place to put this,
read and populate related data. So,
imagine the customer number
on the sales header, if you put that in
just with assignment, that's all you
get. If you validate it, there is really
much data coming into the sales header
and populated from all sorts like from
the customer, of course, for from
default dimensions, from all places,
basically everything that relates to
this. So, that's that's also good thing
to do in validate triggers.
Yeah, because the validate trigger is
our most specific trigger when
trying to check whether value has
changed on a field.
Right.
Exactly. Um then also like you could do
Let's first look at the device.
Create, delete, modify records. I know
there are modifiers and I know there are
also creates in the base app,
especially when you look I think the the
most prominent example for this is the
dimension set entry.
And we're going to touch this later
again. Um but in general, starting right
transactions
when the caller of the the validate code
does not know about this, it's somewhere
hidden underneath and it could be like a
few levels deep under the validate,
um might not be a good idea. So, that
that might be a better place like to put
it on the in the modify trigger or or
somewhere else where you where the
caller knows that he's going to end up
in a right transaction.
And then also call web services. Um
I mean,
in general, if you if you only read data
like the VAT registration number for
example on the vendor card on the vendor
record,
it needs to call out to web service to
validate the data correctly. And that's
something you can do, but really do not
call out like write in different in
other people databases. So,
that's why we put the web services on
here as well.
Um
So,
Yeah, so this is what we're talking
about um
for the rest of the presentation. So,
we're talking about proper validate
code.
Um
or as we call it a maintain code.
There's always this uh legacy code with
a lot of stuff inside of these validate
triggers. And um
there might be exceptions for this where
you can't
just validate those fields, right?
So, we're talking about maintain code.
Yes.
And then and that's important.
Okay. Now,
why do we want now always call validate?
First of all, we always want valid data.
Um if the data we have in the
in our fields in the database is not
valid and we cannot rely on that it is
valid,
then
what what should we do with the data?
Um
And
the thing is
you don't know the definition of valid
for a given field in the current like in
nowadays.
Um because
you don't know what ex- extensions will
end up in a database. The customer could
go ahead and just install new
extensions. Well, they should test this.
They should talk about this, but they
don't always do. And also Microsoft
installs new extensions from time to
time without us noticing. So, the the
definition of valid for any given field
could change any any point in time. So,
you cannot rely on that that you know
that the data is valid just because you
think you know it is.
And then when you do not call the
validate trigger, that might break other
extensions because they might rely on
that their their validation code that
they hooked onto with the table
extension or or by an event is called to
validate the data their way and maybe
add extra validation. And we we're going
to see examples for this later.
Um
so that that extension might stop
working just because you insert records
in the in a base app table without
validation.
And that's I mean that's especially
valid for AppSource apps because once if
you if you push out a an extension to
AppSource and it really
I mean goes viral or just gets installed
a lot. Um
those are like it will end up in in in
environments with all sorts of
configurations, different um extensions
installed and
um yeah, you you never know the the
definition of value for a given field.
Um and that certainly changed when we
went from NAV to to Business Central to
AL from CL to AL because back in the
days when when you had uh your NAV
database, you knew what code was in
there and there was no way that there
were that were was code added without
you noticing because you needed to merge
it into the database. So if somebody
added validation code or some module, um
so to speak, if if you added that to the
database, you touched all the code
manually, hopefully.
So you knew about added validation code
and then you you at least had a chance
to react on this and adjust your code if
needed.
Right. And Stefan talked about a lot um
about valid data in this in this slide.
Um what is also very important is that
um
we subscribe to validate triggers not
only to validate well, then validate
data, but also to react on field changes
and that would be skipped as well.
Yeah.
So if you have any if you have any
business logic related to these
field changes,
you want to have that executed as well,
right?
Okay. Now
pages actually always do validate,
fortunately, because imagine users could
just decide to turn off validation.
Um
and I mean, with config packages, there
is a way, and I'm not sure if I want to
speak that out loud, if I want to
if anyone doesn't know this, probably
good thing. Um
But yeah, just imagine in the client,
they could do something like this.
Go to my settings, just turn off
validation for now, and just let me
enter the data because I keep getting
some weird errors, and I don't know what
this is all about. Just push in the data
because I know it's right.
I think this will be the reaction for
everyone. Now, why should developers be
able to do this
if
I at least I am very concerned about
users doing this stuff. So,
yeah. And I mean, pages even have more
additional additional validates code up
to five events more of validation code
that's being executed. So, there is even
more validation on the pages. So, we and
we need to remember this for the next
slides. I
some of the next slides as well.
Okay. Now, your concerns. As I said, we
collected some responses from Twitter.
And the order is not by accident. I put
the our like the one that
fits us the most on the front.
You should it should be the default
behavior to always validate.
But you cannot do it always. Now, that
not always should really be the
exception.
Um
I don't know if I don't I don't want to
name a percentage probably, but like
really, if nothing else works, then
there there is the exception. Um
But what does not always
actually mean?
Now, the concerns to start with. What if
performance is bad?
I think this was the
biggest one and therefore also the first
one we wanted to talk about. Um many of
you and other people out there, other
developers seem to be worried about bad
performance with calling validate
triggers.
Now, this was the first thing we had in
mind.
Um, speed versus accuracy.
And
there was the I mean that
popular meme, I think. Not
If you don't know it, take a time to
read it. Um
But the example I wanted to give you was
basically if if you imagine video
compression.
Um, if you have an uncompressed recorded
video in whatever higher resolution,
it's a really big thing.
Um, a big file you get and you can you
can reduce that by compressing the video
with minor loss of quality, but that
does not invalidate the video. You do
You do not end up with a video you
cannot understand anymore, you cannot
watch anymore, at least depending on the
compression, but you can you can really
reduce the file size.
Minor differences in ledgers,
I don't know. I mean, if if you increase
the performance of the whole
application, but you have sometimes have
a few cents of difference in the ledgers
and you can't explain why anymore
because
I mean, but it's faster. So,
not sure if that's the same case.
So, now
when
you skip validate triggers to make the
application faster, do you also do
something like this?
Um, and it's it's an abstract example,
but I think I saw something similar some
point in time in actual customer code
where some checks in the sales post were
turned off because there were some
errors. But I mean, it also increases
performance a lot potentially. Um
And I mean, also fixed some errors. So,
uh
I don't know.
But now, what what do you do
um, if
performance actually is bad
um
and you don't want to skip the
validation code.
Well, if this is actually an issue
or a bug, then you can report that
either to Microsoft if it's a Microsoft
code that's slow, or there are
third-party apps, but you can also open
a ticket, report that. Um,
and
chances are that it might not have been
discovered before. Like may maybe your
your situation in your extension is or
in your at your customer is different.
Maybe they don't know about this and
they're happy if if you report this.
And, um,
like every other performance problem or
any problem in general, you should
report that to anyone who owns the code,
um, so they can they can get better and
they can work on it.
It's like every other performance issue.
Um,
for example, if you,
um,
I'm sorry.
Okay. Um,
now, why should I call then a bunch of
empty validate triggers if I know they
don't do anything?
Um, assignment is much faster to type,
and as I am, probably many of you are
used to type the the assignment just out
of muscle memory, and then refactoring
that back to validate triggers
uh can be tedious.
And, uh, I mean all those events that
are that are raised, we saw there are
there are four events, and then
I mean, there has to be some overhead,
right?
Right. Let's take a look.
So, what I've got here is
Yeah.
It's probably not enough. Um,
I've created a or prepared a few tests
for that. Um,
three tests each, one for an empty
validate, and one for validating the
quantity on a sales line.
So, then if I run these,
it should take about a few seconds.
Maybe increase the size one.
Yeah.
All right, there we go.
Ah, and I think we can run it one more
time uh because 150 milliseconds
actually on the better like the worst
side of things.
Um
There we go.
That's better.
30 milliseconds for one validate
up to 7 seconds for 100,000 validates.
And for empty validate that's 7
milliseconds, which is still
kind of large because it's uh 3
milliseconds larger than 1,000 empty
validates.
And um
as you can see, most of that is actually
the overhead of the AL test tool.
Um
and when we take a could take a look at
the code actually.
So, the only thing we do here is
um call the validate on the quantity
with a static value.
And just to emphasize this, this is a
quantity validation on the sales line.
There is nothing turned off or anything.
I mean, there might be code path that
are not hit because of this scenario,
but this is not an empty validate.
Right. So, there's a lot of code you
probably have to scroll to find it all
and there are
procedure calls and everything in that.
And here we have an empty validate on a
field on a table I created.
So, there's
really no overhead for that.
And
as you can see,
maybe I run this test
isolated.
It doesn't change any anything. But 7
milliseconds is
on a real scenario when you are um
validating fields on a page for a user,
they probably won't notice 7
milliseconds. Even if you validate 10
fields, 70 milliseconds is still not
enough for user to
see and see a difference. And if you
look at the second test, even 1,000
validates for 4 milliseconds, there's
arguably no difference for the for the
user when considering empty validates or
just assigning
a value. Even if there is no apparent
code in that
validate trigger.
There might be
some event subscribers that
rely on that field being validated.
Yeah, and I mean, so the overhead of an
empty validate is probably not really
noticeable.
Um
then there could be a scenario where the
code is slow and it's a problem not
well, it turns out as a problem and it
is an issue like there is something
wrong with the code that's therefore
it's slow. But what if it's just if
there is nothing wrong, there's not much
to be improved
but it's still slow, then it's probably
just
doing much.
And that probably has a reason to be
there.
So.
All right, so this performance here for
an empty validate of one field isn't
even measurable really.
Okay.
Let's get to the next topic.
Chain or nested validates. So whenever
you
um
find yourself calling a validate which
calls a validate on another field which
calls another validate on another field
and you you
set loose this kind of chain reaction of
validates onto that that table and it's
really hard to control or foresee the
outcome of that.
Um
there's probably a good reason why it is
done that way. So
um
again there
when bad code is involved, that's a
different story, but if if everything is
okay, then there is a reason that it's
that it was designed that way. So,
um
there is also probably a way to validate
everything correctly, so it works. So,
sometimes it's important to to to
validate the field in the correct order
and not just um calling them in the
order of how they are added to the like
the the by field ID or something like
just from top to down.
Um
and
that might get complicated if if you
have a complicated scenario on a table
and um you need to find out the correct
way of
validating and filling all of those
fields. Um
and if that's your own extension, it
might be a good idea to add a function
to this
uh to the table to simplify this just
the number of parameters and then the
function will just uh do it in the way
it has to be. And that if your code
isn't closed, will also help other
developers to to read that code and find
out okay, well, this is this is how it
has to be. Otherwise,
um on pages, the fields are probably in
the order they the user has to enter
them because we learned on pages,
validate skipping validate is not an
option. So, there has to be a way
uh to do this correctly.
So, we've also also got a demo for that.
Um
Here we have a simple example of a unit
price, a unit price including that, a
line amount, and a discount.
And um the chained validate in this case
helps us keep the data coherent, right?
So, if we validate the unit price,
we also update the unit price including
that in in this case. There isn't even
any that added to that, but that's
Um and we also update the uh line
amount.
And the line amount has some calculation
in here um considering the the discount.
So,
if you have these four fields, you
really only need to validate the unit
price in this construct and the
discount.
Um but everyone using the table doesn't
necessarily know that.
So, the way I solved this was to create
a function.
So, this function
gets a
amount and a discount and validates
these two fields in the correct order.
I have added the two other fields, unit
price including VAT and the line amount
here as well, but they don't
need to be validated
um
because they are validated in the on
validate triggers of the unit price.
So, this is an example on um
what nested validates um are for, what
their purpose
could look like.
And um how to solve the issue of the
order of validation.
Okay.
Now,
what if I don't know what code will get
executed and like
I'm not sure how that actually like what
what happens and maybe as I as I
explained before the extension adding
more code and I'm I'm just not sure if
the customer even needs that all of that
happening and and I'm just concerned
that I I just don't know.
That's exactly why we're here.
Um
you don't know that
and therefore you need to execute it
because you can't control
um
all those extensions adding adding more
code more validation to this. And um
there is just this is this is more about
testing and I mean you can do automated
testing, you can do manually testing,
but you need to test. And the only way
you find out if if all of that is
working actually if you end like
populate the the records with your code
correctly is to test it. And you need to
test with all the extensions installed
because all of them could add stuff on
after validate on before validate and
um you need to need to account for all
of this.
Now when when it comes to AppSource it's
really hard to test your AppSource code
with all possible extensions installed.
So
um
that that that might be a challenge
there.
Um
but still
you need to do that and
that's especially the case for customer
environments if you if you um
check all the extensions today, there
might be new updates coming, new
extensions being installed tomorrow and
they might introduce new validation
code. So you really need to retest all
of that before it gets installed again.
And um
yes, um that might break stuff.
Um
but
you're not in it's not your
responsibility to test other extensions
of validation code.
It's just your responsibility to test
your code. So if you don't validate,
that also might break stuff.
And um that then actually is your
business because you broke the other
extensions by not calling the validates.
Right.
And also maybe you want to switch the
perspectives a little bit. You have
you've added some validate code,
whatever it might be, some business
logic, some other fields that need to be
populated. You want to add an event
subscriber to fill your own fields. That
is also possible scenario.
And um
then you install a
an app from the app source
and um
they just assign those fields without
calling a validate, then your logic
might get skipped and you need to
compensate for that.
Maybe you need to create an event
subscriber on after modify
and then you struggling with or is my
field being updated or is it any other
field and that leads to a whole bunch of
other issues.
As well, it's all
Let's take a look at the demo.
I did there's another demo. Huh.
Got quite a few demos.
But it's the same example as before.
Or
the same table as before but without any
validate triggers.
Um you've got the amount, the amount
including that.
Here it it is a discounted amount and a
discount.
And as you can see there are no validate
triggers on here.
And I've created a procedure same as
before.
Um update amounts
um which gets passed a new amount and a
new dis-
discount.
And I just uh
lazily assign a new primary key
um update the amount, update the amount
including that, the discounted amount
and the discount.
Um and there is
no validate trigger.
Right? So we there is no point in
validating this, right?
Well, actually I have a an event
subscriber, but it's not on the table,
but still in the same app.
And this event subscriber is it's very
simple.
Um if the discount is above 50, I just
get an
get a message that the
discount should probably not exceed 50%.
This might be a some type of
typo
or whatever, but this
illustrates how even in the same app
um at the first glance you might not
catch every validate trigger that's
being executed. All right, so you can
also have
table extensions on the same table in
the same app, which can also contain
validate code.
And
at this point
when you have a large app and a lot of
or you want to add um
validate code
to some field and you are in the habit
of um assigning those values
um it's get it gets difficult because
um if you want to like create an event
subscriber to that.
And all your places where you um assign
or where you want to change those values
get assigned, it's
it might be tough refactoring all of
that and ensuring that it's still
working, right? So, but if you validate
from the first time on
you don't run into these issues.
And there's no code in in there that can
break.
Because there's no code in there yet.
Okay. All right, let's move on. Let's
see the next topic.
So, what if I know what will get
executed, but I decided that I don't
want to? I don't want to have that
executed because it doesn't fit to for
my customer, it I it breaks my extension
because I need to replace it somehow or
I don't know.
It might be the several reasons for
this.
Um
and some of them might be like I don't I
don't see the value. Um
it's therefore an unnecessary
performance overhead if I just uh run
this and doesn't add anything or I'm not
using that part of the software, so I
don't need that code executed at all.
Well, the the simple
sentence for this is run it anyways.
Like it's not your decision to make. You
can if it's a whole module, you can
uninstall everything or use everything
like that. Um
if the the code owner didn't add a way
for you to turn that a piece of of of
code off of functionality,
then that might again be somewhat
considered a bug.
Um but if it's not, then it's probably
there is probably a reason for this to
be it's a that it's executed.
And then imagine somebody else would
just come along and just decide that
your code is not worth executing.
Um or a performance overhead or
something. So, um
yeah.
And um it's really hard to foresee what
consequences this might have, especially
down the road. A few months later, you
you end up with with data that's not
like unexpected for that extension. And
um that might break stuff.
And just to give an example again, the
customer number, just imagine if you
just assign this to the sales header,
then I think you won't be able to post
this
unless you really know what else to add.
And you might miss something that
Microsoft added not too long ago. You
weren't aware of that they added to uh
in that validation trigger. So, I think
this is a good example where everyone
agrees that this validation trigger has
to be executed because there is a lot of
code.
Um
and then the other one is
the code does not function correctly.
And that's again, congratulations, a
bug.
Um
Yeah, this might be an exception that
you actually find those kind of bugs.
Um
but if possible again, um try to
to report it. And if you if you need to
have it working directly, you can you
can try to implement a working solution
uh and validate that yourself somehow.
If there is no way to to skip the
individual code,
you might need to skip the validate
trigger in that specific example, but
you really should report that. You
should put it to do in your code that
you don't miss that place. And
eventually it will get fixed by
Microsoft. It's probably 6 months into
the future if you if it's if it's not
too critical. Otherwise, they will
deploy hotfix and you can move on pretty
quickly. And then afterwards, you can
revert to the normal validation if the
fix is in place.
Um
that was what we could think about
whether you wouldn't want to execute
code.
Um
then infinite loops.
I think everyone had an example or uh
touched an example where you would
validate a field that would validate
another field which would validate the
first field again and then you use
you're stuck in that kind of
uh validation loop.
Um
And those are typically those kind of
interdependencies and you really need to
assign values to both of those fields.
Um
but
multiple
um
I lost my train of thought.
Um Yeah, there are there are there are
different kind of issues
like different kind of scenarios which
raise different kind of issues.
Um
For example, the the start date end date
kind of thing where you want to make
sure that the start date is not after
the end date, but you cannot publish the
start date first because then it will
raise an error because the end date
still there and then will be before the
like those kind of of scenarios. There
you might be
um
it might help to just assign both fields
with an with an colon equal and then
afterwards call the validate on the
field without assigning a new value that
will then validate both of the the
values at once basically like after
another but without assigning or
changing those.
This example might be somewhat cons-
somewhat weird, but um we've got a demo
for that, too,
um really visualize how this how this
might work
or what the issue actually is.
Yeah.
So, I mean, we can we can switch to the
demo.
All right.
Take a look.
Um
we've got two examples. Um
the first example might be the obvious
infinite loop where I have a amount,
amount including that, and they update
each other, right? So, if I update the
amount, the amount including that
will be updated, in this case, with a
static 7%.
And when I validate the amount including
that,
the amount gets validated with that 7%
um
shuffled off.
So, what I did here is
calculate beforehand
if the amount including that
is the amount multiplied by 102 per- uh
1.07.
All right, so this way
I can check beforehand before validating
the field
if that field is already
updated or not. And the same goes for
the amount including that.
So, in this case, I just calculate
what I wanted the amount to be updated
to
and can just check if there is any
update occurred.
And we can take a look at
this in the web client. So, if I enter
an amount of 100,
the amount including that gets set to
107.
And if I update the amount including
that to 100,
it get the amount gets calculated to
some other number.
All right. So, the second example with
the start and ending date,
um we've got the start date and the end
date, and um
both of them
validate um
the start and end date to a point where
the end date must be prior to the start
date.
And when I um update both values, I've
created a procedure for that as well.
Where the start date gets updated and
then the end date, and afterwards um
validate is called without assigning a
new value. So, these validate triggers
are executed and
well, in this case no table relation,
but that would be checked as well.
Without causing any issues um
regarding the which field is being
updated first.
So, that I I don't need to worry about
that.
Right. So, um you need to be careful a
little bit with the with the second
example because sometimes validation
code also checks if the value was
actually changed. And in that if if
that's the case, then you cannot call
them like this because then in the
validation code they would not recognize
the change anymore since the um
assignment was done before. So, this is
uh just a little heads-up, but you
already get get the idea now what we're
like what the session is is about that
you really need to also look at the
validation code here, I think, so that
it is always callable.
Um because most like many of those
examples we now gave so far are just
um showing you how to how to write for
different scenarios, how to write the
validation code properly so it can be
called in all scenarios. So, if if there
are endless loops developed into an
extension, you're trying to validate
those fields and calling the validate
triggers and it doesn't work because
they did not care about those
interdependencies. Again, a bug.
Oh, yeah. Thank you.
All right. So, now what if I write data
just to my own fields? Like I have
button and extension, I want to write
data to those fields. Um
There There is really no dependency and
if there is a dependency, then they
didn't probably like this might be our
own extension as well. So, this is like
an internal button extension kind of
scope.
Um
And I'm pretty sure no one else like
outside of the company or outside of our
control um
can really access those fields. Um
Then what is about What about other
developers? Like if you're if you're
more than like one office of of
developers and you cannot speak to
everyone every day all the time and you
don't know what everyone else is doing
on the extension also depending of
course on the size of the extension or
the suite of extensions you might
um maintain.
There might be other developers who
don't necessarily know and they need to
need to work with your code as well. So,
this is also like an
dependency. Others are are using your
code. They're are not probably not
always aware. Sure, they'll probably be
able to read through your code, but then
again, this is an overhead. They need to
need to verify that everything's working
like they would expect this to work. And
and so on. And now if you if you do not
care about your colleagues, maybe you
care about your future self. Um
I'm not sure uh who
does know exactly what code they wrote 6
months ago. I don't. So, um
if I don't call validate in my code, I
will probably in the future be annoyed
because of that because I cannot use
like I cannot hook on to the validate or
cannot put code into the validation code
a trigger because I just don't call it
from somewhere else.
And this is a typical example of code
depth where you in 6 months you will
need to go back and check uh either do
some work around where you where you use
the on modify and then what Kristen
explained before um
find out if the field actually changed
if this is what I'm reacting to and then
find this some other cryptic way to to
get the job done.
Or you need to start refactoring your
previous code that might introduce new
bugs.
And so on and so on.
So maybe one day you or one of your
colleagues will need
to hook on to the on after validate
event or on validate event itself.
And um
that's why you still should call the
validate even if you if you just write
to your own field and there is no code.
There might be code added at some point
in time.
Temporary tables. I think uh this is
what many of you were waiting for. Um
and now we probably is slowly
approaching the exceptions kind of face
of the of the presentation.
Um
we have split this into two types.
First, the dedicated temporary table. So
whenever you set the table type to
temporary
you are like you you have an object in
front of you and a record table object
which knows about the fact that it's
used as a temporary table. It's designed
to be temporary. It will never be used
as a regular table.
That means
if there is any validation code on that
table, that validation code is aware of
the fact that it's on run on a temporary
table.
Therefore, call it. It's meant to be
called. It has like this is this is
correct.
So
that's the first thing, and I I would
say that it's the better part, like the
better usage of temporary tables. The
other one we call hijacked temporary
tables. So, these are tables, for
example, as headline, which are not
meant to be
used as a temporary table. I know there
are like many examples in the base up as
well where this happens all the time
because if there was no other way. Like
we usually we we got the table type
temporary. I I would need to look it up,
but wasn't too long ago.
Um and up until then we we just had
regular tables and we could use them as
temporary tables. So, there was not that
distinction. That wasn't even possible.
So,
I think as a good practice, it's a bad
idea to hijack tables as temporary
tables in general because that code is
most of the time not meant to be written
to be executed in
in in a temporary scope. And that's not
even not only true for validate
triggers, but also for all the other
code, like anything else.
Um there could be events all around the
place
and uh not know about the fact anymore
that it is
in a temporary scope. That for that
reason we have these temporary uh
variable on records. We can check that
and then exit or something, do
conditional stuff.
But I'm honest with you,
half of the time I probably forget that
this is there and do not account for
this in my code. So,
it's a tricky thing. And then when it
comes to a validate the validation
trigger code,
um for those hijack temporary tables, if
you really need to do that,
need to use them as as temporary tables,
regular tables, then um you should
probably decide on a um case-to-case
basis if you really need to call the
validate um
triggers. I would probably start off
with not validating them and then then
adding them in
slowly after time. so
So, I found a very innovative example of
uh use of high jack temporary tables the
sales line.
So, I
came across not too long ago like last
of
that week before
um someone used a temporary sales line
record
to calculate sales prices where they
just validate
quantity, the item number and extracted
the resulting um sales price out of
that, which um
did not go
too well
as you might imagine, but it's uh
somewhat illustrates why you shouldn't
do
uh shouldn't hijack tables as temporary.
And I've also got a demo for that.
So,
I've created a temporary table. This
might be an um
an example how you should not do this.
Um
and there are
like three fields on that, global
dimension one code, global dimension two
code, and the dimension set ID.
And when I validate the
um
yeah, like one of the dimension codes, I
want to get the um dimension set ID
back.
So, for that I have um
I use the dimension management code unit
with the procedure validate shortcut
dimension value.
This procedure gets um the shortcut
dimension code right here and the
dimension set ID by reference.
And this procedure validates or gets me
the dimension set based on the dimension
code I
give it. Which is base app code, I mean
you all probably recognize this. Right.
So, when I do this, the dimension set ID
um
gets updated. This is the field. And
afterwards, I can just validate this
field in order to
like uh call the validate triggers and
check if any um
table relations apply here.
But the issue with that is bear in mind
this is a temporary table.
This validate shortcut dimension values
creates a new dimension set ID
if it doesn't exist already.
In the dimension set entry table that I
mean
Right. So,
I'm working here on the temporary table.
And on the validate, if I validate one
of these these two fields, there might
be a case where other records are
created
um that I don't necessarily want to be
created when working with temporary
tables.
This might be a
somewhat easy example,
but think about what happens when um
more critical records get created.
For example, sales document when working
with
a
high jack temporary table.
That might be an issue.
Yeah, so yeah, I mean we all can live
with dimension set entries sitting
there, I think. They might get reused
later by other other tables, but this
was like to give a
a example you can
you you know already
um and you can imagine where this where
this potentially could go. And also one
other thing to mention here, um we pass
in the field dimension set ID by
reference into that function, so it gets
updated in that function, but that
function does not know any more about
the fact that this is a field, so it
cannot call the validate trigger. So,
you need to think about that as well if
you want to call the validate trigger
always.
Make sure that you either pass in a
variable and then afterwards assign it
to the field with validate or just like
Kristen did pass in the field and then
validate it afterwards
as a as a standalone drive. So this
scenario is still somewhat um
uh still present when working with uh
tables
uh in the base that have that some
records are just created and you don't
necessarily know that because this
validate shortcut done dimension values
function um
doesn't state that it's um that a new
record is being created.
Yeah.
So this is why we
um
say this shouldn't you shouldn't
validate on project temperature.
Okay, at least you really need to know
what you're doing.
Now data migration tables um
this is
those kind of tables where you when you
when you did data migrations or upgrades
or anything um in the past
I used them a lot.
Those tables where you just store the
data. In the old days we might have even
written those the data by SQL into those
tables and then write code units to put
them in the right places in in in the
system.
So those they might also be filled by
config packages for that matter and
they're just used to store data until
they're transferred to their real
destination. The tables might get
deleted after you finished.
You don't need to need to keep them in
the system.
Um they won't get extended anything.
They're just there during the migration
phase and then afterwards they're
they're just dumped.
Yeah, you can call the validate. There
is no code. You saw the overhead of 7
milliseconds. If your data migration is
that fast that the validates will make
it slow, just skip them.
Um really no need to
um to call them but you still can to
keep your code in in a in a clean
manner. If you validate everywhere and
you do not validate there, that just
breaks the optics. So, you might then
start thinking or others in code review
might start um
to to question well, why isn't you
validating here? Just out of automation.
And um so, yeah, just depends on you, I
think.
And then we put data transfer on here.
Um I think we are talking about this
later
uh again. But, data transfer, you need
to be aware it doesn't validate. It
actually doesn't call any triggers, but
it's also limited to upgrade code. So,
um yeah, just because this is an upgrade
scenario, we wanted to put this in here.
Um you might not use those as well to to
move uh data around in the database.
But, without validation.
Okay. Um
now the other part that goes along with
this. What if I do not load the data
into my migration table, as we called
it, but load it directly into the
destination tables?
Um so, that might be the those kind of
scenarios where you um
you want to you you migrate from a
previous system, you want to populate
the base app just to go live with a
customer.
And I hear that many times.
Well, I know that has been validated
because it was NAV 2016 and we're just
re-implementing and I know the customers
like this is all valid valid data.
Because it's just one by one just
transferring.
Well, the system is a new one. If you're
coming from NAV 2016, just to to name a
number,
BC, what what are we now? 24? The base
app changed
quite a bit. There might be new
extensions installed that all might add
new validation code, change existing
validation code.
Um
they might validate the data just
differently. So,
and I mean
frankly if you have any customer that or
you probably know that
you have a customer that says yeah our
data is
is valid
and you import that and there is just
a very
interesting scenarios of very
interesting data and that that
you can
really call valid data and I mean that's
just
happening.
Yes and I mean it's not only about
validating data it's also about
populating other tables just reacting on
on the the
assignment of that field. So there is a
lot going on potentially and without
that code being in place without it
being called even during initial load
the resulting system might not be
functional and that might not be
noticeable on the first glance again
you might notice that later on so
Yeah you
in our opinion you should really try to
simulate the user interaction with the
system and just automate it. So
calling all the validates doing the
proper way to fill the tables and then
just get everything else
populated alongside as if a user would
enter the data manually.
So you still might need to turn off the
validation on some fields and again this
is a case to case decision you need to
make but
you should try to start off with
validating the fields and then turning
them off as you need them.
If you're doing upgrades there might be
documentation on this kind of things
and then again at the end testing
everything to make sure it works
and then you should end up with a proper
initialization of the system.
Test code that's
an easy one, actually.
Do you want to test the validation code?
If yes, call the validate trigger. If
not,
then don't.
As easy as that. You might have been in
the session of vehicle
before about testing about unit tests.
You want to test exactly 100% of the
code you want to test and 0% of the code
you don't want to test. So, if you don't
want to test the validation code, just
don't call it from test code.
Yeah, and if you if you want to have
mock data or need mock data,
you only want to have like the fields
assigned you really need and
don't want to create any adjacent
records by validating any fields that
might not be the purpose of of your mock
data and
will slow down your tests.
So, that's something you you need need
to keep in mind.
Okay.
That was the list of concerns we
collected.
If you have other concerns,
keep that for the Q&A. We might get
we might have some responses for those
as well.
And we put together a little conclusion
for you. So,
the do's we came up with was
a validation trigger should validate
user input.
Um
it might read, calculate, populate data
from fields from other tables into the
same table.
Um
to help the user on the pages, of
course, because again,
on pages validation code is executed.
And also, you can leverage the same
thing from code if you're calling the
validation trigger. Just make it easier
to to collect everything that's needed.
Um
if there are complicated scenarios where
you really depend on the order of
execution of the validation code
triggers, um create helper functions for
your future self, for your colleagues,
for other people leveraging your
extension, having dependency on your
extension.
And
if there is any scenario where you would
have conditional code, like where you
would say, "Well, I could imagine that
this chunk of code might not be always
needed." Either put in control
possibilities on setup pages, where you
can just switch it off that way, or add
event subscribers, event publishers that
others can subscribe to with handle
pattern, use interfaces, whatever.
Just add control possibilities for those
for for others to turn off the optional
code as actually. Because
only that way they can actually still
call the validate trigger, but disable
your code individually. Otherwise, there
is no option left, and there is not
calling the validation code, which then
also might skip
number of other places and other code,
as well, alongside with this.
Now, the don'ts. That is a longer list.
Um
Database operations of any kind that are
not
um
reading.
So, you don't want to put the session
that is calling your validate triggers
into a write transaction without them
noticing.
And especially when you write data to
different kind of tables in in your
environment, when coming from temp
tables, that might really cause issues
because those were will get left over in
the database.
Um and then
yeah, might result in unwanted outcomes.
Um
testability.
Again, referring to the session, the
database access really slow. You want to
your your unit test to be blazing fast,
and database is a slow slow thing you
can do like as an individual command in
your tests. So, when you when you force
um
the code into the right transaction. If
you force access to the database from
your validate trigger,
um
that can make testing quite a bit
harder.
Um
Yeah, and again, as I said before, um
you the the the column might end up in a
right transaction without noticing this,
and then you get those funny errors
where you cannot run code units anymore
in in a condition you cannot run pages
in a condition you those those right
transaction errors. I'm sure everyone
has seen those.
Um
And then also, this might force order of
validation of the fields. In in an
optimal or an ideal world, the
validation code would only concern about
the would be only concerned about the
own field, like to validate the data
that has been put into the field. So,
Right. And also with um
with the right transactions in these
modifies and these validate triggers, um
someone wants
you shouldn't call any you invocation of
any UI.
But if that happens, if someone decides,
"Well, I need this page to be run modal,
or I want to run this code unit."
Um
I've lost my train of thought.
Yeah, in invocation of UIs, same thing.
Um
Right. This This will result in um
sooner or later in someone using
commits, and that will result in a whole
bunch of other problems. Then you
suddenly have like
one commit, multiple commits inside of
this of this code, because it's
somewhere or
some validation
uh trigger
um
calls like or sets you into right
transactions and another extension
depends on this transaction being
re-transaction in order to
um
Yeah, call a page.
This can get messy.
Yeah, definitely. And then I I think we
skipped that one, the other people's
databases.
Um aka web services. Then again, you you
you end up like
writing records somewhere where it
cannot get rolled back of narrow curves,
so that might run into issues. And then
I would mean we put a screenshot in
here. I'm not sure if anyone ever did
this. Like on the rec. Do a change
company. I wouldn't even imagine what
happens. So, um we just thought it was a
funny thing.
Inside of a validate trigger, of course.
Yes, I mean, and then also all the other
rec functions we listed there. If you
just do an insert in a in a validate
like this, if if the caller doesn't know
about this, not all the primary keys
might be filled. And then this runs
against the wall. And modifies for the
same thing. If you do not want to call
the modify until everything's filled,
then the validate triggers call the
modifies in between.
It doesn't make really much sense. And
then also like jumping to other records.
Just don't do that stuff.
This is uh especially an issue um
when we're talking about pages. When a
user is on a page and calls a validate
and inside of that validate trigger,
there's a find set find or find first
and then jumps to another record.
That might lead to a lot of support
tickets.
Mhm.
And then this was I think a last-minute
change, current field number in x rec.
Um I think we saw an x rec comparison in
in in the
keynote today.
So,
x rec is is a thing and this might this
could be a whole session on its own, Um,
but it doesn't really work well with uh
being called from code. It does work
well as same as the current field number
when executed from pages. So, then it
doesn't you don't notice any issues, but
called from code, it actually leads to
some weird behaviors. So, you really
want to be careful with this and really
test this before you um
put this into any kind of code.
Um
Yeah.
Then now there are a few exceptions.
And again, just
collecting what we already talked about.
So, test code, you do not really want to
call validation code unless you
explicitly want to test the code in the
validation trigger.
Um
For hijack temporary tables, you need to
really decide and check whether the code
works in a temporary scope. And that
might need to get retested if the
extension base changes. So, if any
updates get installed or anything,
because again, the code can could
change.
Yeah, and you really should um consider
whether or not you really need a
hijack temporary table or if a new
temporary table
uh one you create on your own
uh suffices in this scenario.
Because um
when you have a dedicated temporary
table for this,
you have all the
all the control over um
over how you want to use it, how um
what validate uh triggers are or
validate events are on this one.
Yeah. And then the last one, of course,
if the code is buggy and it just doesn't
work, you cannot execute it and that's a
no-brainer, but you really should think
about um
raising this, reporting this, and then
coming back to your code if it's fixed
and updated to get back on the
on the good side of things, on the
bright side.
Now, I think we we have enough of time
to cover those edge topics like the
additional topics and um
the pages actually also have an on
validate trigger.
Um
and the question is when when should I
put the code now on like if I write my
own extension, when should I put code on
the page validation trigger on in
opposite to the record?
Um
and one good example was
if you do calc fields, you could do calc
fields in on validation trigger if a
flow field depends on that field. So,
then the user enters the the data, the
flow field gets updated in in
immediately and the user sees direct
response.
Um and that
would actually be bad code on the table
because you do not want to calc field
random random flow fields
um that are maybe not even needed while
writing a record. So, that's typical
page code to improve the user's
experience
and that's not not needed for code only
execution.
Then any kind of UI UX logic, style
expression,
hiding or showing fields dynamically,
putting actions somewhere like all those
kind of things where you where you want
to modify something on the page like the
state or anything else,
um
that's typical stuff to do on the page.
And then the last thing
if you have if you use a variable to a
source expression for field on a page,
you have no option you if you need to
validate the user's input, you need to
do that on the page or just like
somewhere else in on the page, but I
think the validation code is there is
the best place to be there.
Um
there is no way to put that on the
table. So,
anything else I missed for the pages?
I think not. I think that was it.
Um
Now, we found something interesting
while playing around with this. And
that's actually the on lookup trigger on
the pages because that really um
is related to the validation uh on the
page itself.
So,
um it's pretty interesting because the
validation happens automatically and you
can you can write the lookup trigger on
pages in a way where it behaves as if
the user had entered the data directly
into the field.
Um
but you need to know that if
the table and the page both define the
lookup trigger, the page wins.
Um I'm not sure if that's intended or
why why it is that way, but um that's
what we found out. So, whenever you put
on lookup code on the page, the lookup
code on the table won't get executed.
And
on the table, it just works as you would
expect. There is the trigger, you put
code in there. It gets um it gets
executed when you click on the ellipsis.
And I think we can demo that as well,
right?
Yeah, we can.
So, let's take a look into VS Code.
I have a page
um with with a simple field on that.
This is the table for this.
So, I've got a primary key and a text
field.
And whenever I validate any anything
into this this field, a message pops up
um
which shows me um like the table on
validate message with value and then
I've got the value here.
Um and I've got this page for that.
Um this is like only this this one field
is added onto onto this page.
And whenever I click on the on lookup,
um page gets or the text that was
entered into that field gets passed via
this parameter.
And I just add
um page on lookup to that.
So, we can actually see how this
um
affects the user input.
So, if I go here
and type into that
like a 10, I get a message.
Okay.
Should be large enough.
Um I get a message table on validate
message with value 10.
All right, so the expected behavior. I
enter a value into that field and the
validate trigger
shows me
what this value is.
So, when I look when I click on this
ellipses,
um according to the code,
I should get
the page on lookup added to that.
And as you can see, there is no other
code in here.
So, in order for me to get that message,
I need to
have that field validated.
So, let's try it.
I think there is an exit missing,
actually.
Might be the
wrong page.
Okay.
Let me republish that.
Try exit true in the on lookup trigger.
Yeah, that's probably it.
Right. And there you go.
Simple as that.
So, I get the page on lookup added to my
to my value. And as you can see, um
this value gets added to the field.
And um
this only works
apparently
when you add a exit true for that.
So, if you
do an exit false, no value gets updated.
Yeah, and again, the reason why we
included this was because it really
interacts with the validation. Um
I didn't know that before we prepared
our session. So,
um
maybe somebody else still learned
something from this as well. So,
And now our probably our largest slides.
Um
Transfer fields modify all and we
already touched the data transfer
briefly. All of those do not execute any
validates.
Um
The transfer fields is mostly used for
transferring to posted tables.
Um and you might argue, well, you do not
you typically have any validation code
on posted tables.
But I still think that it might still be
reasonable
um place to put in extra validation code
or reacting on a field change to to do
extra stuff. Um there might be places in
the posting routines to add that code, I
know. But um
in my opinion, transfer fields is not
really a a thing you can use because
validation code is is skipped. And if
you just if if you
really
just do not do the typical examples from
the base app and just use the transfer
fields because, well, somehow the fields
map to each other, um then you might
break other people's extensions
depending on that or your colleagues.
Um
Now, the modify all
is the same thing, and I know I might
have said some people if I say you
shouldn't use modify all at all.
Um
Exactly that reaction.
But again, it doesn't it doesn't do the
validation. So, if you do modify all,
you need to be aware of that any
validation on that field is skipped. If
there is code, it won't get executed.
So, in and if if there are any modified
triggers
on modify code, it's already only the
like less code version because under the
hood it's still doing the the loopy loop
version.
To to run the modified triggers. So, I
would what I would really hope for if
we could get a third parameter to say,
well, if there is validation code, run
that please as well. If there is no and
the runtime should be aware of the fact
if there is validation code or not. If
there is no code, then of course, do the
do the SQL batch operation, make it
fast.
But yeah, we don't have that parameter,
at least not yet. I don't know if it's
coming. I think there is an idea, so
it might get voted enough so we can we
can get that. But again, if in favor of
calling the validation trigger, you can
really use the modify all.
It's
said but true.
So,
and then the data data transfer is the
same thing, but it's very limited
because you can only use it in upgrade
code.
It does not call any triggers, but
that's part of the definition of that
command because it's used really to to
do batch
shuffling of data from one table to a
different table.
So, there we would expect that. But
again, for the modify all, it's not
documented, somewhat hidden that it's
not doing that.
Pretty
sad, actually.
Okay.
Um
one last slide.
Start refactoring now.
Um it's actually not that hard.
There is a code action for that. You can
just
Um if you use the AL Code Actions
extension by David Feldhoff, you can
just
select whatever assignments you have and
refactor them into validates.
And um
yeah, get rid of those assignments.
Okay.
That's what we have prepared.
Now we are open for
any questions you might have.
And let's see if we can answer them.
Right.
I think it was a very relevant
presentation you did.
Very relevant subject. Um
and and actually when when when I do
code review,
I always re-
require that you explain if you're not
using validate
because of all the things you presented.
But when you when you have this subject,
what about you said that the user can't
pass
by the validate in the pages?
But what about the insert and the modify
triggers? Have you thought about those
too that you would say exactly the same
as with the validate?
Yes. Um
And that that you want the the quality
you you're talking about the quality of
the data.
So you want the validate to be run. But
what about the the triggers for insert
and modify? Isn't that the same?
Short answer, yes.
Same story. Um in our opinion, those
triggers should not be skipped either.
Um
and there are more ways where you can
actually execute it, but for at least
for the onModify, I'm not sure about the
onInsert actually, but the onModify,
there is a way to subscribe to them even
if they are not executed like if the if
the parameter is false, there's still an
event that's raised. So, there is at
least a way you can ensure your code is
executed. That's not the case for the
onValidates. So, that's why why that's
why our focus was on the onValidate for
this session, but you're absolutely
right. Yes, those should be executed as
well.
And I mean, you can you can
even argue that the code of code the
order of execution should always mimic
the the order the user needs to do. So,
you first do the init, then you primary
keys, you validate the primary keys, of
course, then you do the insert trigger,
then you do the rest, and then you do
the modify because that's exactly what
happens if the user enters data through
the page.
Right. So, if you mimic the user's
behavior, you probably can't get
wrong data or invalid data.
If it works on the page, I mean, it has
to work in code as well. If you do the
exact same thing, there shouldn't be
difference.
Yeah.
Right.
Any other? There There we go.
Uh if you're importing data from
external systems, sometimes you just
can't do validate because this data
may not uh correspond to your system,
but just the way it is. If the external
system is the leading system and BC is
just an external system which is used
for things the other system cannot do,
you have to take the data as it is.
And if you start validating it against
your uh other master data which you've
which you've taken from the external
system
at an earlier stage, sometimes it
doesn't work, so
you cannot validate. You have to live
with incomplete data and
Yeah, well, if if if that's the
scenario, what what is like in the
acceptable range of your solution if you
if you know the data cannot be valid and
you have designated fields for that or
whatever where you put the data in and
you know it's like it doesn't correspond
with the rest.
I mean it should be documented somewhere
for the for anyone else not familiar
with this to to read upon it and
not stumble across it, but yes, agree.
Look,
I had a question.
I second fully that it's a a great
overview. Thanks for the effort.
No, okay. Thank you.
I think there's one thing where we might
differ in in in the look. You say about
the user
perspective user input validation, but I
don't think code is always the same. In
the code we not always need to mimic
what the users are doing and that might
differ and you might know I shared my
blog post. I think in some instances you
first want to assign and only validate
one because it's going to call the
chain. And that one is more effective
than doing every field on its own. So, I
think it's not always the same, but
that's something to discuss.
In our opinion, the problem is with this
that you don't know who else might
subscribe to the fields that you skip.
Nobody in the end in that chain you
it will be a nested validate on all the
fields anyway, so they will be picked.
Yeah, so like the example I gave on the
general ledger or sorry, general journal
filling, you only need to fill in an
assign a number of fields and call one
of the validates and it will call
everything else. So, in that case I
think you need to study the code and
make it more efficient.
I mean we we can we can continue this
discussion for a long
I know. Just want to mention.
Okay.
Thanks so much.
Hi.
Could you please elaborate a bit on
Excuse me. There There was a quite huge
statement and no no validating test code
whatsoever. That's at least how I
understood it.
Could you please please elaborate? What
does this mean? Are you afraid that um
by doing on validate you would find out
something else before you come to the
point that you are actually testing
or more in the sense you you're talking
about mocking some data or preparing
some data
for for testing later? In which sense
and and
Both. I mean, first you need to prepare
the database
maybe. You need to write records. You
need to need to have something you you
can test with. And in that case
as well or
Um no, because you you want to control
100% of what data you're inserting.
You're inserting it in a way um
with assignments where what
to have the result where you need it.
And if you do validates, the code might
change. You might run into like
depending on the extensions and what
what code might change that is
subscribing to the validates and that
makes your your test unpredictable.
So in in when you're mocking data, you
if you somehow can just assign them to
make to have a reproducible
test case.
And then if you then need to test one
validate, you if that's the the
given when then
the when part, then you can call the
validation because that's the code you
want to test. And then you can execute
it, but if you're just preparing the
database to run your test against that
data, you typically don't want to
validate because you cannot 100% be sure
that that code will always be the same
and not modify your your givens under
the hood.
All right, thanks.
So, I think he was another question
somewhere.
Somewhere in the middle.
Can you pass that along?
Yes.
Uh are you planning to add a check for
this in the RuboCop?
I thought about this, yes. Um
I haven't gotten to it, but it's
certainly an idea, yes. To just have
maybe a disabled rule because not my not
everyone might get warnings on all the
assignments in all the code. Um
Uh but yes, you can so you can activate
it and then you get just reminders on
where there is still assignment in your
code. Um I need to think about this
because there might be exceptions and I
do not really like pragmas, so that
might also be another scenario where you
could just put in a code comment and
then the warning goes away or something
to explain the assignment. But yeah, I
thought about that already. That's an
idea.
Okay.
You can throw, maybe.
Thank you.
So,
can I throw?
Oh.
Slow again. Okay, short.
Okay, so about hi, hello. About infinite
loops.
Your solution was
I uh check if uh
a value is already on the other side.
Uh but what if the two values
um are numbers, decimals,
and calculations
um
may lead to
uh
like the third decimal to be different?
How would you handle such a a case
because the the the condition
would not uh
Mhm.
yeah.
I cannot talk in but I think I can I got
the
Yes,
that might I mean it's hard to wrap your
head around just by the description, but
I think that might also be an example
where you want to fall back to different
function handling the the exact steps
how you need to do that, how you need to
run the the validation code so it works.
Um but yeah, that that's certainly a
case where you need to need to think
have a look at your example and then get
creative to enable others to validate
the fields that um to catch that. And if
there is no way around um if it's not
possible to always call the validate
directly on the fields, then again
probably something you need to document
and say well, use this function and then
everything gets validated or executed
correctly.
Okay.
In the worst case scenario, you could
also you could always create a global
variable on the record
which you can set to true or false
depending on whether or not you have
updated this field already.
So, this way you can break out of
infinite loops.
all the time.
Yeah, I'm going to say something that
will make somebody angry, but I'm
thinking about some code
at my previous company. I didn't wrote
it.
I just had to maintain it. They actually
had a single instance to check whether
everything was already
in place.
The same idea. If you need the scope in
in global somewhere, then yeah, you need
to do single instance. Just need to be
careful to control the state.
And you just afterwards you can pick up
the trick.
Um
Yes, thank you. I I want to add
a don't um in from my practical view
because
when you use change company and after
that you do a validate, that's not a
good idea because
from this situation you do don't have
the in the validate if you use
other tables, then the change company uh
is not used.
The the change company only
works for the record you're calling it
on, and anything else that's running the
code, that will still run in the
original company's scope. So, yeah,
that's right. Absolutely correct.
Okay.
Some more questions? There we go.
Thank you.
So,
I have this scenario where you have five
different application, for example,
extending one
base application.
Mhm.
Right? And uh
you validate one field from this base
application in
uh all the applications. I mean,
uh which application wins? Uh
in case of
because they validate with different
values, which one is a winner, and how
to deal with that?
Um I think this is the the old topic of
event subscribers in the order of
execution for event subscribers in
general, and I think there is an
unofficial answer to that question,
which I won't tell you now, um because
the official one is you don't know.
Uh the code needs to be written in a way
where the order doesn't matter.
Um so, validation uh needs will run in
whatever order that you might hit, and
then um if one throws an error or
something, um
everything will will stop at that point,
or if you put like um populate other
fields, then that should also work, no
matter what order it get executed.
Otherwise, you will need to put like
some other
um construct in there to control the
order yourself.
So, basically, there's nothing you can
do about it.
No, the order of execution, you cannot
control that.
Thank you.
Some more questions? There's still Okay.
Still have 3 minutes.
Uh so, um
it's a good idea to to have a validation
on all the fields, but maybe it's also a
good idea to start talking about
validatability of the code. I mean, you
cannot insert whatever you want in a
validate trigger.
Yeah. And we we tried to cover this a
little bit.
Are there some principles or some
documentation about that? Some
methodology, I don't know.
Not that I'm aware of. I mean,
everything we we thought was important,
we put into the slides to really like if
you write validation code, care about
the value you're you're working with,
like that was put into the your field,
make sure that this is valid if you need
to check that, or populate other fields
based on that value. And everything
beyond that, basically, is really
something you wouldn't want to have in
the validation code for for various
reasons, write transactions, stuff like
that.
But I don't think there is any official
documentation
on what is like good in a validation
uh trigger and whatnot.
Okay. Thank you.
Okay.
I think we have time for one more
question.
That's not a question.
When you do the posting schema
Mhm.
from the sales line
to the item ledger entries, you go to
item journal. You don't validate the
fields then.
Why?
That's the rule.
Why?
Well, the the
Well, then I would call those validation
triggers being wrong. Um
Controversial topic, so
our idea is that if you should be able
to react on any field validation of all
the fields
because you might need to put your
custom logic which the extension author
cannot foresee. You need need to be able
to to attach that to the field
validation. Um
And we we did I mean, we can we can talk
about in detail about this, but I
couldn't think of anything any cases
where you couldn't write the validation
code in a way where you would enable the
callers to always validate this.
Given exceptions.
Okay, I think
that's it. Thank you very much for
joining.
