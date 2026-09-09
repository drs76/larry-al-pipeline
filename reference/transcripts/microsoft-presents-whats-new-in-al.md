# Microsoft presents: What's new in AL

- **Source:** https://www.youtube.com/watch?v=7YQrZQgFb9Q
- **Video ID:** 7YQrZQgFb9Q
- **Channel:** mibuso.com
- **Published:** 2026-07-02
- **Duration:** 89m38s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Welcome everyone. Uh my name is Peter.
You might know me. I am not a product
manager just to set that straight.
So in this session we're going to talk
about what's new in uh in AL but as you
have seen in the keynote hopefully this
morning uh then the experience of
building software solutions not just for
business central but in in general is
evolving fast. So we see less time spent
by developers to actually write code. We
see more opportunities for
non-developers like consultants, uh,
power users, makers, etc. to contribute.
And with AI and natural language and
agents used consistently across those
personas to increase productivity and to
lower the bar of entry uh for all
stakeholders.
So um let's try first to see get an
overview of sort of the landscape of
those different uh experiences. Uh we
have um something that might not be that
familiar to developers but because that
the no code experience and you've seen a
rise in those platforms like lovable or
uh or repit or other platforms. I think
I'm going to ask a couple of questions
during at least my part by raise of
hand. So I'm curious how many in the
audience
have used a platform like lovable
specifically lovable
and replet.
So actually not a lot just to double
check that you are developers raise of
hand who are developers.
Good good okay okay. uh to this no code
um category also goes uh in product uh
customization capabilities that are
actually already in BC. I mean you can
do layout, you can do personalization,
there's the designer mode. Uh I'm going
to talk in a moment about data vers
field mapping. You also saw in the
keynote Espin showed some of the
opportunities going forward to do more
modifications directly inside of the
client.
Then you have uh what you probably you
know at least the last I don't know 10
15 years have been working in uh which
is a coding IDE right sort of more a
graphical experience uh where we have
visual studio code we have um branches
like cursor and windsurf I'm curious
raise of hand how many have used cursor
windsurf
other similar IDE [snorts] than that
okay so mostly cursor but not that many.
Then you have uh the interactive command
line uh interface. Uh we have uh the
GitHub code CLI we have things like
clock codeex others raise of hand again
how many used uh github CLI
and clock code so by far more clock code
uh others that I didn't mention
not a lot okay so cloud code super thank
you and then uh we have these more
automated pipelines right so things
running in in GitHub we also saw that uh
today uh in the keynote
uh and then obviously you have different
models underneath there um driving the
the LLMs and and we believe in the same
underlying foundation powering all of
these experiences. Uh of course our
focus is a little bit different. We
don't focus on sort of third party no
code experiences. We focus on the BC
experience. uh we focus mainly on uh or
on VS code from an IDO point of view and
GitHub copilot CLI uh and GitHub itself
and from the models it's mainly GPT and
the anthropic models right but there is
some uh variance in this and you can use
these tools outside of that as well but
that's our focus
that also means that uh this sort of
regular session we have with what's new
in AL isn't just about the language and
the developer of Visual Studio Code
environment anymore more um while the
language is still there uh we have had
to evolve and expose the development uh
platform capabilities to support the
increased experience surface across
these things like command line like uh
pipelines etc and the personas involved
um
and and that means that today we are
going to talk a little bit about the
capabilities uh sort of in the product a
no code experience I'm going to show to
database data data versse field mapping.
Uh then we're going to hear Stephan talk
about uh language enhancements and we're
going to see uh how we can teach or have
agents actually write code and know
better about AL how we can now test uh
AL code from within VS code and also
from the command line uh and having peak
and those uh command line uh tools AL
tools and LMC and then also
troubleshooting MCP which is I think
quite interesting just to see where
those fit in. This is all about us uh
basically teaching these experiences how
to work with AL because there's not that
much about AL out there of course
because the models have been trained on
AL but we need to improve the accuracy
of those. You saw that in the keynote
how when we invest in tools when we
invest in um docs and insights etc. We
when we evaluate we improve the accuracy
uh for AL. So our investments around the
agent um skills, the BC quality effort,
uh the tools uh that we will see today,
the testing uh the troubleshooting, they
all help on this. Uh and as I said, we
evaluate that with BC bench, but we're
not going to talk about that in this
session. That's a separate session uh on
that. But let's start somewhere else. Uh
let's start with a new uh no code
ability to customize BC uh within the
client. So uh how many of you have
worked with data verse integrations
where you had to do mapping to BC? Okay.
So maybe not that many 10 10% or so. So
typically administrators have to uh keep
business central and data versse uh
aligned as the data versse schemas
evolve or maybe extensions are being
installed in BC. And previously if you
wanted to expose uh a new or existing
custom data versse field you would have
to actually have a developer build a
PTE. There's some tools for for creating
uh um uh creating that but you would
have to deploy that uh as an extension
and so now you can actually map directly
within the uh business central client
without creating these table extensions
or writing code. So it's much easier to
do these configurations and it's much
faster to do that and you don't have to
be involved in that as a developer but
an admin can do that. How many are aware
of this new feature which is some months
old? So not many. Okay. So uh the way it
works is that when a new field is added
in data versse or vice versa I mean we
support birectional here. So it doesn't
matter whether it's it's to pull
something in from data versse or to pull
something in for business center to data
versse but you could uh then have a a
custom field for example in the in the
dynamics 365 sales and now you can map
that field directly uh to a BC field
inside of the BC client you can refresh
in the BC client uh the list of fields
from the data versse uh field list and
then you can create the table mapping uh
you can then define the synchronization
and it then runs uh as you are are used
to that. Um and that as I said makes it
a lot easier to uh to do these things.
We have support for multiple different
data types. We have uh support for
transformation rules and we also come
with some uh builtin configuration
templates uh for these different
records. Let's try to uh do a demo and
let's see if I can figure this switching
out.
>> [snorts]
>> Yeah, super. So, um it can go both both
ways, right? But let's just pretend here
that we have something installed from an
ISV solution, a new field that I want to
sync to data versse. Uh I lack
imagination as a product manager. So, I
put in shoe size here um that we just
track on uh the uh the item that we have
here, which is an essence desk. Those of
you familiar with the data versse
integration will know that basically we
need to have a coupling uh per record.
So it's already set up to actually sync
between the record here in PC and the
record in the corresponding data versse
record here. But from a field
perspective we do not have the shoe size
uh built in yet.
So if we jump to um the data versse and
the table schema, the corresponding
thing to uh to map the item to is the
product in here. And so on the product
itself, we can add a new field
um
or new column.
I have various uh types um available for
me, numbers and text, etc.
I'm going to just use the text here.
I'll I think that'll work. We'll see
what happens. Uh because it's actually
an integer in BC. But let's just for the
fun of it look at this. Uh let me see.
It's probably not shown here yet.
So it's just because it's out of bound.
Let's just hide a few of this. So shoe
size came in here. And we see that for
the Athens desk, we don't have shoe size
at the moment. And so we have to set up
this mapping, right? And the way we set
up mapping is that in Business Central,
we go to the integration table mappings
page. Uh we have the item product
mapping set up. So we can go under
mapping and select the fields to map.
And oops, that was the wrong one I
picked.
I'm pretty sure I had highlighted that
one, but let's see it now. So we have
the item product mapping. We shouldn't
have shoe size here now, but it shows
all of the fields currently mapped. we
can create a new field mapping.
So we select on the BC side
what is it that I want to sort of map on
the BC side. So we select the shoe size.
Then on the data versse side we will now
look up directly in data versse and
hopefully it's already picked that up.
So we have the shoe size we created in
data versse. We can set up the direction
whether it's one way or or the other way
or birectional. We can have
transformation rules. Oh, one thing I I
missed showing is that you can see that
there's also a tab here for actually now
it's showing shoe name. Let me just find
that again.
Shoe. You can see it says is runtime
over here. And that's because it's
actually one of these dynamic fields
that we created like this. I'll talk
more about that in a second. But now we
set up the mapping.
It's not enabled by default. So
we'll finish the wizard here.
[snorts]
And it's disabled. So let's go and edit
the list and just enable this
integration
like that. And that is hopefully it. So
let's see. So we'll go to uh our essence
desk. Yeah, I have a Microsoft noise. I
hear that. We'll do I don't know 44 in
shoe size
and that. So I can trigger the
synchronization um manually but it
should pick up this. So let me just go
to uh data versse and refresh this and
we'll see what happens.
So hopefully this is better for the
remaining 30 seconds of my stage
presence
or maybe a little longer because it
doesn't show up. [snorts]
We'll do once more.
And uh
probably I should have set it to
integer, not a text. Let's just do a
synchronization here.
[snorts]
There is a synchronization lock as well
where I can see if it failed. I think
you understand uh that it's supposed to
put in the 42.
I have a video of this as well because I
came prepared after the keynote. But
okay, so now here you have 44 at last,
right? So that basically shows how you
can do the data verse integration or
sync without involving code and it took
like five minutes or so, right? You can
for now do it only for sort of the
existing table uh mappings. We can't add
a new table uh sync yet, only the
fields.
Let me switch back to
presentation.
Yeah.
So you saw the demo. Um the way it works
is that um it's actually one of the
things that we are looking into from
this kind of no code approach where
things happen behind the scenes. So
we're not really creating an extension
as such. We we connect to the data
versse uh to get the fields uh from data
versse live. You saw that when I looked
up the fields. Um then we actually store
these mappings as data in the
environment and at runtime we uh we then
take uh that delta and apply it right so
it's a like a dynamic uh application or
resolving of that and that also means
that we don't have any deployment uh on
this we configure it directly in UI in
production and it's working like that
and this just like adding analysis views
with related fields how many of you have
actually tried that it's more an enduser
consultant feature but yeah but that
works a a little bit the same that you
can actually go and put in um you
basically create a query at runtime in
production behind the scenes, right? And
these are examples of how we are um
empowering uh users to customize PCs
themselves uh involving typically
natural language AI etc. Not so much
here but in general we're doing that uh
because um AI is helping us move faster
towards that goal in the future. Again,
you saw the better call in the keynote
today, which is from the lab's idea on
that. But let's slow down and uh and
let's get back to the actual uh coding
experience uh itself. Uh we had a launch
event on what's new in AL which cover
some of the topics from the rest of this
session. How many of you have watched
that launch event session from a month
ago? Okay. So you will see some
familiarity with the topic but it's
still only about 10% of you. Um so let's
bring in Stefan for that.
[applause]
>> See if we can get this one up and
running.
So what better way to start this than
continue with some UI, right? Uh my
favorite UI.
There we go. you can all read this. So,
um I'm going to walk through some of the
language changes that we have done since
the last time we were here. Uh it's not
going to be all of them. It's going to
be some of them. Uh as you can see here,
I have a very well-prepared structured
demo. Well, okay. I have collected some
some code here that we can talk about.
And if you're curious if it compiles, it
does compile and we can actually go
check it out. I mean, what uh beautiful
UI we have here. Maybe we can refresh
it. That would work. Um, it has very
nicely
constructed actions and fields. So, it
works. It can compile at least. So, so
far so good, right? Okay. Let's start
with some code here. The first thing I
want to talk about is the allowing
customization. uh we added that some
time ago uh for you to help hide things
that are in a table that you don't want
users to add to pages in the
customization experiences. Uh we needed
a little more fine grained u capability
here. So we added the as read write
option for that. So you can now add uh
the value add read as read write meaning
that when a user drags that onto the the
page itself it will actually be writable
and not just read only as it used to be.
You can still put the classification
here on the the the page or the table
the object itself and we added the to be
classified to understand the difference
between I did not look at this and I'm
not done yet. Right? So you have now
that option also and as you can see you
can still put in on the individual
fields that some of them should be of a
certain classification here to be
allowed in the customization. So this is
when users drag fields that are not on a
page to the page. Right.
Something different in the UI also is
the new property called mask type. The
mask type is different from the extended
data type masked in the way that you can
recall the data anytime you like. So
here you would see data that looks like
it's masked, but the icon on the side
will then give you the option to open up
and see what's the data behind it. In
the extended data type mask, you would
normally only see the data while you're
editing it. As soon as you left it, it's
kind of masked. So here you can have
account number, social security numbers,
and other important details that you
don't want to be visible at the
beginning and then you can show them
when you need it.
Another interesting uh extended data
type we added is the extended data type
document. This is for media fields where
you want to show show a preview of the
media and you want to make sure that
it's aligned in a certain way the the
portrait mode so it shows as a document.
So if you have a fact box or something
like that, you can now tell the code
here that this is supposed to be
rendered as a document and it will
render it in a portrait mode.
You might see uh the auto format type
has been added many places in the code.
It's not new. It's not something that uh
we just added to the language. It's
actually been there for some time
helping you describe how the numbers
should look in the page here or in the
in the table. What we've added here is
more rules uh that will allow us to help
developers remember to put these things
in. And we do that no not only because
developers need to understand what the
the code is is about and what is the
data in this field but also for the L&Ms
that reads the code. Now they understand
the format this data is supposed to be
in. Right?
Okay. Let's move on to something
interesting also data related. Sometimes
when we're working a lot with a lot of
data like log entries and stuff like
that we need to clear out the data fast.
And today or before we added this new
method, you had to do for each and
delete all the records or do some of
these things. Now you can use the
truncate method. The truncate method
does what it says. It truncates. So it
does everything in one single go and
deletes all the records that you have
within your filter.
This needs to be used with some some
caution. As you can imagine, when we no
longer run triggers and all the other
things that are in the product in the
code, then we need to be careful what we
delete. So use that with some caution.
Another interesting u scenario here is
that when we add a lot of data,
sometimes if we use [snorts] guid
identifiers, we will mess up the
indexes. We will fragment the indexes.
uh quite significantly and that can be a
challenge. So we introduced a create
sequential GUID function which allows
you to create GUIDs that keeps running
in a very sequential way and that will
help uh not fragment the indexes as
fast. Yeah.
And inserting or doing anything with
data can sometime mean that you need to
lock. So to give you a little more
control of the lock timeouts, we've
added this lock timeout duration method
that you can use to specify how long
you're willing to wait for a lock. And
sometimes you want to exit fast and then
come back when there's more time to do
things. Other times you want to make
sure that your your code can run for
longer before it bails out. So use this
also with some caution because it
applies until you start a new session or
you set the original or some other lock
timeout. Right?
So let's go not to that one. Let's go to
number three. Here we go. So lots of
data. Keep talking about data. We've
done some improvements to the data
transfer. Uh one thing we've added here
is the ability to use the destination
filter.
So imagine you're running data transfer
again and again and again for every
upgrade or maybe many times doing an
upgrade. You want to make sure that you
only update the records that have not
been upgraded already. So you can use
the destination filter to only target
certain records.
We've also added the ability to use the
update audit fields in cloud scope. uh
it was there before for onrem but now
it's also open for uh for the cloud
meaning that you can set it to false now
and keep the audit fields as they were
in the data and not be updated.
Okay, let's move on to the next one
here.
Name spaces. Everybody loves namespaces
here. So we've done a lot to kind of
make namespaces a bigger part of the the
language and make it something you can
actually depend on and use. The first
thing we we started doing was adding
namespaces to the metadata. So now you
can query and find all objects in a
certain namespace. You can maybe find
all objects that are related to sales or
find all objects in a certain company or
a certain uh subp part of a namespace if
that's something you need in your
product.
We've also uh exposed the fully
qualified name as a property on records
and record refs. This gives you the
opportunity to save that data if you
want to get back to it at some point. Um
instead of using the table ID, for
example, you can use the fully qualified
name. And why is that interesting? Well,
because you can now also use the fully
qualified name to run a code unit,
to run a page or a report.
So now you don't need to know the ID of
the the object. You can just use the
fully qualified name. And of course you
can also open record refs using the
fully qualified name as you would
expect.
When we work with the record refs, we
work a lot with record IDs also. And of
course here we also added the fully
qualified name. So that you can see here
you can format a a um a record ID using
the classic way where you get the table
name or the caption if you want that.
But now you can also use the agnostic
one where we put in the fully qualified
name of that object. So if we look at
the data this would produce it would be
something like these three examples down
here where you have the name of the
table and the caption of the table. And
here's the fully qualified name. Right?
So name spaces are infused everywhere.
And of course when you want to go back
from a a string that has the record ID
to the actual record ID, the evaluation
also works for that.
So we saw Peter talking about analysis
views. Let's just see if we can find one
here. I had one open. So let's try
again. The analysis views are a quite
powerful query generation tool in the
product where you can generate your
queries and you can add columns from
related tables like the unit of measure
the vendors in this case for items. It's
quite powerful for users to build up
their own queries and have them show the
data that they need for their job. But
up until recently we haven't been able
to ship that in the extension. We could
create the queries, we can create pages,
but ship these analysis views was not
possible. So now we made that possible
and the syntax for it is super simple.
So it looks like this. That's all it
takes, right? Well, of course, we need
the analysis. And the way we do that is
that we export it from the client. So we
build the analysis view in the client
the way we want it to to work and then
we export it. So if we can do this, we
can say we want to export the definition
and that downloads a file analysis file.
I take that file and I put it into my
solution. It looks something like this
which I recommend not editing directly.
Go back into the client, change the
view, export it again, get it to what
you want. And once you've done that, uh,
you can put a reference to that file
here in the definition file and give it
a nice caption. And once you publish
that, it will be just like this for
example. Right?
So now this analysis view comes from my
extension. It's not something specific
to this user, but it comes from my
extension. And you can see that it
doesn't have all the details. You can't
edit it. You can't do a lot of things
here. Uh if a customer wants a special
version of this, of course they can just
go and duplicate it, right? And then
they can start changing whatever they
need, right?
So
how many of you have used summaries on
pages?
Like a nobody. Fair [laughter] enough.
Do you all know what summaries are?
You do, right? So over here,
well, yeah, I turned it off, so it's
[laughter] not there. That is the whole
demo, right? So now you can turn it off
if you don't need it. So we can say
true. And then we can publish this one.
Let's see.
And that doesn't work. Fair enough.
Anyhoo, so on list pages, sorry, on cut
pages and and other document pages, you
have the summaries. I think we can
actually just pick one of the others.
Did we have one here?
Let me just go and find a customer
because nobody knows what summaries are
and I feel obliged to tell you. So
summaries is what we have over here.
It's now synthesized on all these card
pages meaning that it is present and you
can reference it on all cart pages.
Imagine a user wants to use it. they can
just start summarizing and co-pilot will
help generate an overview about this
customer for what it's on the the page
itself but also related data. So
hopefully in a second we should see some
information about this customer like a
balance, outstanding orders, payment
received totals and so forth. But this
just doesn't make sense on all pages. So
having this summary function there and
having users click that summary function
doesn't make sense. So now we can turn
it off uh in our extension if we want
to.
Right. So last thing I want to mention
is some uh some small additions to the
language just because we have time and I
can uh JSON has been added to the
language some time ago and we've keep
extending it making it more and more
powerful. The last thing we added here
is the ability to do uh some JSON path
queries into the data which can be
extremely powerful. So you don't have to
iterate over all the items in a JSON
object like here we want to find some
>> [snorts]
>> uh origins within routes or we want to
find some uh routes here for these
flight details that are more than 700
units long. So this gives us the
capability to filter into the JSON
objects and and get more details out of
it without having to loop through things
which is very powerful.
And part of the whole uh referencing by
name, we also added the ability to
reference fields by name. Uh so instead
of having to just figure out if a field
exists and then find the ID and then get
the field value by ID, you can now just
get the the value by name if you want
to.
And of course we continuously improve
and react to the feedback uh that we
get. We added two text and added more
text functionality to the text types
some time ago. Uh but we forgot text
constants. So you guys gave us some good
feedback and we added the string methods
to to text also.
So this was a lot about the the language
uh all the the details we've been
adding. There's plenty more. Go check
the change log for all the details on
the the additions to the language. Now
let's talk about the tool set. So let's
invite Thomas up here to talk about
that.
[applause] Yeah.
Right,
perfect. Right, so we've all seen that
agents are now more powerful than ever
at writing code,
but they still need a little bit of
help. We
give them the tools um to actually do
some useful AL development here. And out
the box um with the AL extension, we are
giving them the opportunity to build um
our um our AL projects. Um they can find
symbols not only inside the code, but
they're also able to download symbols
from your um system tenant. Um they are
also able to publish uh your projects.
they can run test on it and we have
troubleshooting capabilities as well
[snorts]
um for for the agents to use. All of
this is inside the V studio code
experience but these are also available
outside if you were to use the uh MCP
connection um
yeah for your CLI interface.
Right. So, let me warm up my machine
again here
and jump to it. Perfect. Oh,
wonderful.
Let me Yeah. [snorts]
So, here I have V Studio Code. Um, and
we can see I have a a little uh
diagnostic down here telling me that u
the customer is missing. So let's say
that we need to uh download symbols and
make sure the project builds.
[snorts]
So without setting up any MTP
connection, without doing anything else
but installing the AL extension, um the
agents are now able to go in and
hopefully uh fulfill my request here.
So [snorts]
if we take a look at the set of skills
that I have or a set of tools I have
available, there is nothing else but the
built-in ones and the uh the extension.
And we see down here that it's been
downloading symbols and now it's
starting to compile the project and it
all works out. All is good.
Perfect. and it keeps going.
What you'll maybe notice right away is
that there doesn't seem to be any
troubleshooting um tools available at
the moment right here. Um all of these
will be available as soon as you go into
a debugging session. Um and it will get
access to get all the the stack trace,
the variables, uh set break points, all
that um will be available there.
So these are the set of tools that we
have provided inside V studio code for
the agent.
And
if we take a look at our next um
improvements that we have done, it's
around our testability stories.
So
back again at my uh my machine here,
[snorts]
we have added support for the uh the
test explorer and uh right here and none
of my test has been running. Um but
luckily we have added support for not
only running your tests but also
debugging your tests and running your
tests and collect uh code coverage
information um for these ones. So let's
start out by running the test and see
how it goes for them.
Here we are publishing and running. And
uh
give it a minute.
Of course.
[snorts]
Oh, the demo today.
Let's stop it for a second here. Let me
do a quick reload and let's give it one
more try here. [snorts]
So we are loading up the workspace
and load up the tests and let's go back
in here again.
[snorts]
So what we're seeing here is that it is
uh not only publishing but also running
the tests. Um and that's because
specifically for run of your uh your
tests, we have added these two profiles
where you can decide if you want to
publish every single time that you're
running your test or if you want to just
run them um once in a while. [snorts]
So if we take a look at some of the
tests here then we can see they're using
the subtype test and there will be no
mentioning of AL test runners uh right
here because they are not used when
running the the test explorer um but
instead for covering our um test
isolation uh needs from the test runners
we have added a new property for it. So
in here you can specify if you need to
roll back your transaction after every
single uh test method at the code unit
or if you never like to ever need to do
it um for your tests.
Besides that there is the uh test type
property that's been added uh on uh test
code units. And the purpose of this one
is not to modify the execution of the
test in any way. This is just a signal
for you and I and our agents that these
are a specific scope for our our test
here. So we can tell that it's a unit
test or integration test or this is a
test that is working on AI
functionality. And from this you can
imagine running a subset of your test
depending on on this test type. Um
whatever you need to
All right. So going from here, let's
have a look at the the code coverage.
So if we take a look again and we try to
run all the tests
[snorts] with code coverage,
then
we can now go back again into our uh our
code here
and we got a new code lens element.
This code lens uh element will indicate
if
um or it will tell us how many tests we
have executed this function right here
and how many of them has been passing um
on it. So if we take a look for instance
at this uh overdue function right here
we can see that five test has been
passing out of the five that has been
touching this one.
So if we were to have a few failing
ones, then we could click on it
and now they're running. So this is a
way for you to narrow in on which tests
you actually need to run and they might
be scattered all over your test
solutions, but this will uh now give you
a good starting point on this.
And lastly, um, for for the these three,
uh, musketeers up here, you're also able
to debug. And the good thing about here
is that you no longer have to track down
a session ID or go into the web client
to test your it's all captured inside
your developer experience here. So what
you can do is simply right click on the
test that you want to debug and let's
put in a break point that actually stops
somewhere
and then we go debugging
and we are publishing the extension once
again to make sure that we have the same
set of codes uh running that you are
seeing in your uh uh in V studio code
here and we are now hit a break point
and from here you can easily do whatever
you are used to do when you're debugging
right so step over find all your
variables whatever you need to do um
[snorts] all of it is uh available right
here
and uh I think that will be it for our
testing solution um this time around so
now I'll hand it over to Stefan to talk
more about our uh our tools
I'll be back. Thank you, Thomas. Thank
you, Thomas.
So, let's see.
So, I want to come back to the AL tool
that we talked about this morning. Um,
how many of you have been using AL tool?
Do you know what it is?
Well, a few. Yeah. Awesome. You are my
friends. [laughter]
So, this started with with a simple
challenge. uh where do I find the
compiler when I need to compile some
code in a in whatever setting that is
outside of VS Code and the answer
previously has been that we have to find
where the V6 is installed and we need to
go in there and find the the XFile ALC.X
X and take it out and put it in uh some
infrastructure pipelines and stuff,
right? It's not been easy. So, we
introduced a a new package uh for
shipping the compiler outside of the the
language extension and all was well,
right? We came to a point that was
great, right? But then there was other
tools that we wanted to ship like AL doc
and then other tools. So we put them in
the same package and then we kind of
came to a conclusion well there's a nice
um way of shipping these tools uh that's
called the net tools and that allows us
to have a simple infrastructure for for
installing and for showing what the
tools are and also to upgrading tools
and so we changed the tools to that. We
have now on the Nougat site the
development tools package which you can
download. There are also platform
specific versions of it Linux and Mac OS
for those few tools that require
platform specific binaries. Uh but for
most of them uh especially the compiler
and all the things related to that it's
agnostic of the platform. So, you can
get it all in one package. And as I
mentioned this morning, using the
pre-release, you can try out uh all the
new things that we can think of. Uh
figure and try out if the new version
works for you before you even upgrade
your language extension.
So, it's available everywhere because
it's easy to use. You can install it on
a client that doesn't have the language
extension. You can install in one that
has the language extension. You can mix
and match what you like. You can put it
in pipelines, you can put it in in
GitHub agents and so forth. Um, that's
pretty cool. And as I said, it's
language agnostic or OS agnostic, sorry.
Uh, meaning that it actually runs on
Linux also. It runs on Mac OS. Uh, so uh
you can use the tools there if you
prefer those OSS.
The tool set today is
expanding. It's pretty good right now.
We have lots of tools. the original
tool, the compile. Uh where is my ALC?
It's right there in the AL tool. So you
can use the AL compile if you want. Then
you get everything for free there. And
we have many more uh tools by now. Uh we
have been looking at expanding this
towards usage in pipelines. So that's
why we need to understand what kind of
package type it is. It's a simple
runtime package and so forth. And of
course the new ALMCP is in there. Uh so
you can use this tool set to launch the
MCP server locally and that is great and
wonderful and the preview has the new
LSP server also saw this this morning.
Now if you add the .NET tools to GitHub
you get more stuff and it's quite simple
to add the AL.NET net tools to GitHub,
you can just add a config file to your
repo and that makes GitHub aware that
you're using a .NET tool and when you
download that repo, when you clone that
repo, you can just write in your in your
command line there restore. It will find
that config file and restore those tools
for you. So now you don't even need to
install them up front. you can just have
them configured maybe a separate version
or maybe more tools in one repo versus
another repo and so forth. So it's
pretty easy to work with. And on the
right side, so on the right side here,
you can see this is just an example and
and to be fair, it doesn't work. But I
just want to tell you that just by
putting that config file in there, no
additional instructions, no nothing, the
agents in uh GitHub, the cloud agents
there will detect that this tool is
available and try to use it if it knows
it's an AL project you're working on.
Now from the box here, it's not really
usable by the agent yet. Maybe we can
work a bit on on the documentation for
the AL tool to make it more usable. But
with a few instructions in your in your
your agent for GitHub, you can make it
use this tool quite easily because you
don't need to tell it where to install
it. You don't need to tell it about what
how to use it because it knows .NET
tools by itself.
So
what else can we do that are fun things
on GitHub?
Well,
how many of you have used code spaces?
One guy. Two. Awesome.
So, code spaces is a I think it's a
really powerful feature. It's really
nice for a developer who works on many
repos or somebody who doesn't want to
have all the tools installed locally.
Maybe you're working for one customer
one day and another customer another
day, different tool sets, different
versions and so forth. Code spaces are a
way to have Visual Studio Code in a
browser with all the tools available and
I want to I want to show that.
So it's pretty simple to configure. Um
we go to GitHub and let me see if I can
find GitHub.
Yep,
there's GitHub. We all know that.
So uh here I have my config file. You
can see it right here. There it is the
config file. The net tools.
Awesome. So now when I clone this repo I
have this available. But I also have a
folder called dev container. Inside here
I have a file called dev container. This
is the configuration of a code. So here
I set up how I want my code to look. In
this case I want to use a Linux
distribution.
Yeah, vuntu. I want it to be one where
that has the net 10 installed. Pretty
nice. I want it to have powershell and
some other things. But I can also have a
postcreate command here which is when
it's done creating this this uh code
space, it will execute something. And in
this case, I want it to restore the
tools. So they're ready for me if I want
to use them in this code space. But I
can do even more. So I can configure VS
code in here. Also, I can tell it to use
the AL language extension. So, when my
code is created, it will install that
language extension. In this case, I'll
also use the pre-release because I'm
cutting edge right there on the front
line. Right? So, I'll have it do that
and I'll have it install some other ones
that will help me be productive in this
repo. I'll also have the ability to set
some settings like what code analyzers
to use in this. maybe even background
code analysis,
right? And so forth. Incremental build.
I can use all the settings that I have
available in VS Code. I can set here in
this configuration file and then it will
be ready for me when I start up, right?
I can even configure MCP servers for
this uh code space. I know I have the
MCP JSON here in the repo, but maybe
there are some MCP servers that I only
want when I'm in a code space inside VS
Code in in a code space. I can do that
here.
So, the next thing you would do once you
have this is go back to your repo. See
if I can do that. There we go. And then
you go here and you say, I want to
create a new options that I want to do
that to show you all the different
settings you can have. You can choose
which branch you want to work on. You
can choose which container
you want to have, which configuration.
So you can have different configuration
depending on what you're doing. Maybe
you're doing one configuration for older
versions, another configuration for
newer versions, and so forth, right? And
of course, where you want it to be,
latency and all the things, and of
course, what kind of machine you want,
how much you want to pay for it
essentially, right? And then you create
it. It takes a little bit to start up,
but once it's started up and yeah, of
course, [laughter]
once it's started up, let's try to start
up. So, what happens when you create a
new workspace or a new code base here is
that it will install all the extensions.
It will install the net 10 and it will
restore the net tools and get all of
that ready. Uh, the second time you
start it up like here, it it doesn't
take that long. it it's a little bit
faster, but essentially what you get
here is the same as you would expect on
your local machine. It's a VS Code. It
has the chat, so you can run some stuff
over here. Uh ask the the chat about
some things. Um and while it's loading
here, we can check the
the extensions maybe. Come on.
There we go. We can see that it has some
uh some extensions installed. It should
say in a second at least.
Come on. Yeah. Well, you see the MCP
that I configured that's there.
And come on.
Not having much luck today. Let's try
again.
See, it's loading the workspace. That
means that the AL extension is
installed. You can see it because it
actually shows the dialogue there to
load the workspace. And uh even though
this button over here didn't seem to
work,
not today. But the extension is
installed. And we can of course use what
Thomas showed here. Uh if I load that
workspace with the tests. Come on.
Let's load that workspace. There we go.
And we can see that the tests are there.
So I have the same kind of capabilities
as I have locally but now just in a
browser and I don't have to install
anything on my own box.
Uh that brings me to small feature that
we also added which is sometimes you you
build solutions without having a server
and maybe
you need the symbols to compile your
solution without having a server
available. So we added a new function to
download symbols from a global source.
So this uh gives you the ability to
download symbols from base app and
others uh other dependencies that uh
that exist on a certain version without
even having a server connection. Right?
So here I can download them and I can
say I want a specific country version or
the W1 version and I'm just going to do
it this one time. I'm not going to save
this uh in my workspace. So I can
actually connect it to a right
environment later on. Uh and it should
be downloading here. You see it
downloads from from Nougat feeds the the
different dependencies.
So once you connect it to a real
environment, it doesn't really make
sense anymore because you have real
symbols from a real environment with the
actual versions and stuff that's on that
environment. But sometimes it's faster
to just iterate on small uh features,
especially in aentic development without
having a connection to an actual server.
So you can download symbols from Nougat
instead. Back to tools. So I said it did
net restore here, which means I can
actually go to a terminal and write ale,
right? That's what I said. No, that
doesn't work. Why doesn't it work? Well,
this is a Linux box, right? So I write
net tools tools. want to do net tool run
al
now it works okay so there's some
differences between the different
operating systems and the way we install
things that just you guys who work in
Linux boxes know all about this for sure
and know probably a lot more than I do
so teach me because this is fun um but
uh you can access the tool here and you
can do the the is simple only launch MCP
here and and connect MCP to whatever
sessions you So you have the same tools
available everywhere.
But let's uh hear more about this uh AL
tool. Estim
got the good name for a C code spaces
glorious winner. That sounds good. Um I
need to get my glasses
and
Damn.
So,
a couple of months ago, our
infrastructure team, they came to us in
the tools department and asked them to
help them with one of their repos
because it's growing and you probably
all know it. it uh it's BC apps and um
at that point in time there were 230
30 files in there uh app.json JSON files
which means projects and it took
a long time to um compile them and
whenever they create a new version a new
build they had to update all of those to
the same build and that was time
consuming. So they asked us could we do
something smarter
and what we came up with was a new file
called
directory
um app.json
which is a file that allows you to
specify properties to be shared across
all that.json JSON files
and the format is like this. It has a
variable se section where you can define
variables
give them a value and they are they are
replaced into the um [clears throat]
dollar sign parenthesis blocks. So in
this case if you look here I define a
major minor build and revision which is
1.0.0.0
zero and then I create a version
variable which is actually combining all
the others. So I get an actual version I
can use.
And in the other half of this file there
are properties and those properties are
properties that be be used if the
property is missing in the app.json JSON
file, which means that
with a setup like this, I can remove
publisher from all of my app.json files
in the entire repo and they will all be
replaced with fabricam.
I can remove all the version um
uh properties [clears throat] in the
app.json files and they will all now get
the same version which make managing
huge repos like this much easier.
specific error at least if you want to
have the same version and the same
publisher for all but often that's what
you want
and the the way this file is found is
that the compiler is looking upwards
against the root to find the first
instance of the directory props.apps
app.props props.json file
picks the first one and uses those
values and it also works from within
Visual Studio Code. So if you have this
file, you can also use Visual Studio
Code in the language extension with
those properties removed and have a
centralized way of using them.
So yeah, here's the it's found by name
searched upwards works for both loaded
once and um it's [clears throat]
expanded into the uh into the installed
packages. So when a package isn't is
actually compiled and generated there's
no difference. So it's completely
transparent from from that point of
view. And there are currently 15
properties which are supported.
So let's try that out
and let let me do it in a combination
with demoing another new tool feature.
So I have a small project here and as
you can see over here there's a base
there's a dashboard and inventory and
sales and there's this directory that
directory approps.json
file and it has only one property
defined in there which is runtime 16
which is the one I want to apply to all
my packages.
But let's start down here. I have
already installed the the new tools
package because that makes my life a lot
easier.
And I I don't have a workspace in here
yet, but I would like to have one.
So,
let me create one. I will create a new
workspace called Kontoso. And I will do
it from this directory. And what this
command now does is that it
goes down to all the subdirectories.
looks for app.json JSON and create me a
new workspace with all of those
and warming up
and it found exactly four projects as I
hoped for and you can see in here
is all four base consoor base conso
dashboard
so but I mean from here I cannot see how
the dependencies actually are for those.
But there's another
option for the workspace here.
Workspace map pointing to the workspace
file. And that actually creates a
markdown file up here
that I can show. And as far as I
remember, we have a new option here
directly to do that.
And
for some reason
that doesn't work as well.
Yeah. Uh if you're really quick, you can
see it actually draws a graph. And I'm
not sure what's wrong with my extension
here. Um, but it creates a mermaid
diagram in the markdown that allows you
to see the the structure of these
projects.
And the structure is dashboard depends
on inventory and sales that depends on
base
which means that
at that I have two projects which are
independent of each other which are
sales and inventory.
which also means that if I could compile
them in parallel, I would actually be
able to compile a little bit faster. So,
one of the things that we added to this
command as well is a compile
that can compile the workspace.
And what it does is that it finds and
and creates the optimal compilation
graph so it can parallelize as much as
possible while compiling. So let's fire
that up. And this is a small status bar
down here saying it's currently working
on one
two waiting. Those two are now compiled
in parallel and one is left. And now I
got all four compiled.
that feature in the BC apps repo when
our compilation that to go down was 75%
which quite a lot there's a lot of files
that could be compiled in parallel there
um and some of you probably have repos
with similar issues that can be
optimized like that
remember I talked about the directory
apps.props.json JSON file runtime here
that actually means that if we
let me pick one of them just the base
here in here there's no mentioning of
the runtime but what I can do here I can
use another command
get manifest from the base app
and it simply just outputs the generated
man manifest in the app file. But what
you can see here is that the runtime
is set to version 16 and that
information come from the app file uh
from the [clears throat]
props file and is put in there.
That is that feature I think that's for
you to come back Stephanie
>> back to you. Yeah,
>> I'll be back. Yep. Uh,
let's see. What should we talk about
now?
>> Yeah.
>> What could we talk about?
>> I'm just going to skip all your slides
here. Is that okay?
>> Yes.
>> Troubleshooting. Should we talk about
>> Let's talk about troubleshooting. Right.
So Thomas talked about the
troubleshooting MCP which is inside of
um of the AL language extension allowing
you to use our tool set to do more than
just adding code but also to
troubleshoot code and I want to see if
we can get it to work. Are you guys up
with that? Could that be fun? Yeah.
Yeah. Troubleshooting, right? Yes.
Exactly. Love that energy in here.
Right. So let me see if I can get my
solution back up and running here.
And we go here.
So as we discussed earlier or at least I
disclosed is that um this project is the
best solution ever not absolutely not
just designed for this demo. So I have
some high value code in here somewhere
that is really really difficult to
debug.
Let's see if we can get it up and
running.
Um,
in the keynote I talked about uh using
the set def breakpoint or get the the
agent to find the breakpoint that I
need. Sometimes you know that there's an
issue and you know exactly where to put
it. But when you get into that debugging
state, it's not that obvious what
happened here, right? Sometimes the the
the information that you're actually
looking for is in the data. So you need
to figure out what are the variables,
how do they get here, like what's the
flow of the code and all these kind of
things. And that's kind of what we tried
to to add tools for with the debugger
MCP. So let me see. I have a a very
important function here. I actually have
three. You see very important functions.
And I want to invoke one of them and see
if we can debug it. So the first thing
we need to do is attach the session. So
I'm going to find my session ID if I
can. Where is it? Uh not there. It's
here. Help and support. I go find my
session ID.
There we go. I go into my launch config
and I have neatly prepared one.
Paste the session ID in here and then
we'll debug that
if we can. Let's see.
Come on.
I messed it up.
Come on.
>> Okay.
>> Did you bring a video?
>> I know. It's It's really a good idea to
bring one.
>> Yeah. Well, this might help. I somehow
uh disabled the configurations.
Okay, let's try again. There we go. I'm
going to attach to the cloud sandbox. I
I do things every now and then.
[laughter]
Yeah, let's see. It's going to see if I
can connect to the actual session. It's
connected to my sessions here. Okay. So,
I'm going to run my very important
function, right? Go back and then run
this very important
deep call stack analysis. Very important
business function.
Hopefully, the debugger will break
because it found an error somewhere. I
made this easy for me. I don't need to
set a break point because it's just
easier with it failing on an exception,
right? So do that. Like everybody here
can see that this is most likely a
division by zero ex exception, right?
But let's let's ask the agent and I
prepared a small query here that says
let's use the AL debugging tools
to inspect where are we like we want to
know what's the call stack what's the
variables all these kind of things and
tell me where the division by zero is
happening right these are the questions
I would ask myself as a developer when
I'm troubleshooting this so let's try
and see what happens here um
agent should now used the get call stack
and all these tools that we added um to
get the information not from a local
source but actually go to the server ask
the server give me the call stack that
we actually in right now give me the
variables that I can see in this call
stack so this frame here and uh from
that try to reason over that data to
figure out where are we why are we here
and what happened right agents are
brilliant at deducing these kind of
things from that kind of context and
giving it this context through the tools
makes it super easy for the agent to
work with with it here. Right. So it
find here that there's a bug and like we
can go up here and find all the
explanations. So we have a division by
zero. Yes. And if we look at the call
stack we can see how we got there. Uh we
can see here what's the variables and
why five valid routes were counted. The
the invalid count is zero. Right. Okay.
So there are no invalid routes found but
uh we have some zero here and we can go
check here and see okay we set the the
invalid count to
to the variable and it even gives me
navigation hints so I can click on it
and see what happen see what we get
there and then we get a division by
zero. So using the troubleshooting
tools, the agent can help me get an
overview that would normally take me
some more clicks and understanding and
trying to figure out and looking at call
stacks and kind of navigating the code.
So this is next a tool for you guys.
When you're out there trying to debug
something really complicated, try using
these tools. They will be a benefit, I'm
sure.
That's the main part of this. So now
let's talk about something more
interesting, the future, right?
>> Yeah. Yeah. Yeah.
>> Yeah.
>> Or at least a possible future.
>> Go back to the
>> Yep. This one here. Uh for some reason
the last part of the uh keynote today
got a little bit rushed. Um
and the part I didn't get to talk about
was a part of uh bite code. the last
part of by code. How we actually
implemented this um
and what what we have built is that we
have created a um virtual machine which
is outside the server which is also what
made it possible for us
to take that virtual machine and move it
into the AL extension and run it there
as well as a test runner. And that gave
us some new capabilities
like very fast testing on a mock. Um,
of course it's known nowhere near ready
for prime time because there was all
there was a number of bugs in there
because platform functionality that's
not implemented.
But it on command line it runs the 800
test in 2.5 seconds and that would take
around 40 seconds to publish and deploy
on a real server. So there's a huge
potential for fast feedback on those um
and that will benefit developers and
agents and um
speed things up a lot.
Um [clears throat]
it's not something that will be coming
right now, but we hope that we can use
that in future to to improve that.
Yeah, I don't have a lot more, but maybe
there's a lot of questions around some
of that for
this the keynote, maybe some of the
other things we have shown.
So, we have about 15 20 minutes to go
through some questions. If you guys have
questions for this, we are really fast
today. I can see we have t-shirts here.
>> One here. Yeah.
um on the shared properties what you
showed is there the pre-pro prep
pre-processors
um things also supported so that I can
make the um
my checks in that the the checks in the
code also triggered like the clean for
the clean clean 28 or something like
that
>> that you can add to the command line
during compilation or in you cannot you
cannot add them into the Actually
that I think you can.
>> And the second question the the you
showed the um online thing with the
referencing the nu get packages only. Is
it um am I limited or can I also add my
own or like reference nu get packages
from other extensions on this one
>> if they are.
>> So for code spaces is that the base app
>> codes configuration is is all yours.
It's in your repo. You can add whatever
you want. If you have your own uh VS
code extensions, you can add them there.
If you use Waldoros or some of other the
extensions out there, I mean just add
them as as entries in that list for the
configuration and you can do that. You
can add startup scripts. You can yeah do
a lot of things there. It's very
powerful, very flexible.
>> Yeah. You can make make personal
configuration and you can make uh
company configuration and project
configurations depending on what you
need. Yeah.
>> Yes. Uh you mentioned name spaces in the
beginning.
>> Yes.
>> I would just like to know will name
spaces ever be mandatory?
>> So I
>> have a slide for that.
>> I I actually
so glad you asked. So we have had a talk
about this for many years. So I have
asked co-pilot. [laughter]
So the short answer is not right now.
But we know based on our own experience
inside the base app inside u the the
project that we work for work on that
this helps us organize better the code.
It helps us design the code better. It
helps us figure out what belongs to what
manage dependencies figure out if we
have code smell in our code by looking
at the number of using statements. And
all of you have seen the huge list of
using statements in the base app. That's
a huge code smell, right? It has
branches everywhere. So, as we refactor
things, we use namespaces as a way for
us to help have these conversations,
help us discuss whether this is a good
design for the new module or a bad
design for the new model. So, from that
point of view, we are really into
namespaces.
>> Yes.
>> Yeah. And also the um some of the tools
that we have added the simple suit
search is actually often using name
space spaces to hone in on specific
areas of the base app. For instance, if
you mention something from sales, it
will start searching in what object are
in the sales name space and use those as
a starting point for figuring out what
to do. So it actually also helps agents
a lot. And just to round that discussion
off, um our dream is to use namespaces
as a way to get rid of affixes to have
clearer names and better names and not
having to have this registration of
affixes because namespaces themselves
should be unique enough. We are piloting
ways to do that, but we're not ready yet
because the runtime still needs more
work in order for us to support
namespaces everywhere. But as you can
see in today's presentation, we are
continuing down that road relentlessly.
So at some point, yes, namespaces is a
key part of the language.
>> Yes.
>> So a quick followup. Yeah.
>> Will there be a path for us as an ISV
not using namespaces right now, but some
of the apps that depend on us are using
namespaces?
we will not be able to introduce
namespaces without making a breaking
change for all of them as it is right
now.
>> True.
>> Will there be a path for that?
>> So there is a path. They uptake
namespaces for your from your code,
right? And there's code actions to help
you do that. That's the the the easy
answer to that. And and I mean we've
improved the diagnostics messages as
part of our work with agents and trying
to to uh improve how they react. So we
worked a lot on the the responses from
the compiler
>> to make sure that when the compiler gets
an error like I can't find this symbol.
It has a little more context
>> and it knows what to search for and I
mean in in very a lot of a lot of cases
I won't say 100% of the cases but a lot
of cases uh it's going to do that for
you. So you don't have to do any work or
your your collaboration partners will
not have to do much work just uptake it.
So I don't think there's going to be I'm
not going to speak for everyone but at
least personally I don't think there's
going to be a solution where when you
add namespaces and your your consumers
are adding namespaces that we will then
have some kind of global mapping or
secret function to make that happen
seamlessly. Uh but again we we are just
beginning to get people on boarded that
are not using aixes and really into
namespaces but still a bit unclear how
that would look but we we appreciate any
feedback of course on that transition.
Yes.
>> Okay. Um we're wondering if there's any
plans for perhaps in the future to be
able to debug production environments.
So uh right now you can debug but only
using snapshot right. So we cannot halt
our execution in production
environments. We do not see a future
where that is possible. I don't know if
the VM at some point will help do that.
I don't know.
>> No, I think it will be the same
challenge as as
>> stopping execution in production is
really not an option.
>> Sorry. [laughter]
Let's catch one in the wing.
So we were trying to set up the MCP
troubleshooting that you have shown us
today but we found an issue for us that
we are using the delegated admin
accounts
>> and it doesn't work with that right
>> so are you planning to add that support
or do we have to create accounts for
every our customer because we don't have
accounts for every our customer
>> so I should just say they should create
more more users right
>> no [laughter]
if it doesn't work in let's say a couple
of weeks. Give me a hole.
>> All right.
>> Get it prioritized. Yeah.
>> I don't know how far it is at this
point. So,
>> oh, I think I saw one up here.
>> Of course. Yeah.
>> Hi. Uh
there you go.
>> Yes.
>> Uh you showed data vers and about the
dynamic mapping.
>> Yes.
>> And is it also available for the onrem
version? Ah yes it would be right. Yeah
it is it is because data versse is
supported on prem as far as I know
>> and the connector. So what what happens
behind the scenes is that it uses the
connection that you have set up inside
business central to connect to the data
versse instance. Right? So it it's not
something new. There's no new
connections. There's no new uh
functionality in the connection between
data versse and business central. What
we did was take the the the the code
that we had in AL code and made it
possible to do that inside the product
itself. So it's the BC side that has
changed, right? So if you can set up a
connection in in uh in on-prem for data
versse, then this would also work there.
>> Okay. Thank you.
>> You're welcome.
>> Here we go. No more t-shirts, so the
rest of the questions are free.
[laughter]
>> Anyway, thanks. Uh I've tried to
implement the feature that you showed
about uh props JSON but it works only
locally. Do you have any plans to add
processing of this feature in pipelines
i go or bc container helper?
>> That surprised me because it that's what
we use it for. We use it for pipelines.
So we need to talk more details on what
you guys are doing because uh it this is
what it's used for. This is why we built
it because we needed our pipelines to be
more efficient.
These lights are super bright.
[laughter]
>> A short followup question on the name
spaces.
>> Yeah.
>> Uh long time ago you started to
reorganize your base application how you
store files by folders.
>> Yeah.
>> Uh and inside folders even subfolders
like the financial management and so on.
Uh my question is uh is it related to
agentic development? Does it give any
benefits to agentic developments? Um,
and would you recommend an extensive
folder structure for other solutions as
well?
>> I I think if if you're dealing with
something like our base app with I don't
know 6 8,000 objects, a folder structure
is a is a good choice. And I think it
makes sense to to use the name space as
a as organization for it anyway. Um, so
for me, yeah, that made sense. And I
they I don't think that the agents care
a lot about the folder structure.
Actually, they probably work more of the
name space itself.
Um, although they could consider
folders, but I think namespaces is the
primary part of it. and and with the
additions of tools we have made that
actually are able to to read uh and use
the name spaces for searching it's it's
it it adds a lot of benefit for those in
in large um apps
>> one more
two sorry
>> so I have two questions so one is
related to datavas. So the first one is
that uh I made the connection with the
database and the business central and I
was not able to identify that where the
integration is getting failed. So I want
to know that if uh I want to verify
which system is not picking up the ID or
the key correctly. So how I can identify
that because I want to know that like
it's the synchronization and both
systems should need to have a key uh
some kind of key or integration mapping.
So how I can figure it out?
>> So it's in it's in the integration
mappings the whole mapping between the
two tables.
>> So from the business center side I know
that there will be the system ID will be
going there. But from the uh database
side which
>> it's always the system ID on on database
side. That's uh that's how records are
are referenced in database.
>> Okay. And the second one is related with
the mask data type.
>> Yeah.
>> So
I save the credential of the user and uh
once uh user is user is going to uh get
the information and I need to verify the
user is putting the credentials or not.
So how how I'm going to prepare that uh
compare that user is providing the
correct value or not.
>> So I would encrypted
>> yeah I would not use masked for that.
>> Okay.
>> If masked is there to help you recall
the information later right? So like a
social security number some people need
access to it. A password on the other
hand is something you enter once then
you have to take it away and save it
somewhere else a hash of it and then you
can verify the hash of the repeat for
example also. So don't don't use uh the
the mask for for passwords. That's
that's not the intention. Use the the
extended data type instead.
>> Okay. Thank you.
>> Yeah.
>> Thank you.
>> Is it working? Oh yeah. Uh I have a
question about bite code compilation.
>> Yeah. um because you said that you
wanted to move to to that possibly in
the future and does that also mean
moving away from the net and all the net
addins etc for al
>> awesome question yes potentially it will
yeah um we we would like to get rid of
the net interrupt feature at some point
but
I mean it's not this year but maybe in
the future because it really doesn't fit
the cloud.
>> Already today we we recommend well you
can't use .NET your own.net in the cloud
at all. Right. And for on premises we
recommend that you go to a cloud
compatible model and don't use uh net
directly in the product but infer it in
some kind of service you have next to it
that can be accessible using HTTP uh
maybe an ashure function or something
like that. Right? So take it out of the
product. That's what our recommendation
today and there is absolutely a path
forward wheren net is not a part of our
of our tool set.
>> Yeah. All right.
>> Thanks. Firstly, uh thank you for adding
FTP support natively. Um can you now add
native support for importing PDF files
so we can extract the information out of
them?
>> Love that idea. Love that idea. So you
saw in the keynote that uh the agents
can actually do that using the AI tools.
So that is a
most likely coming very soon.
>> Yeah.
>> Perfect. Any more questions?
>> I think the BSS one is right. Sorry.
>> One about the better call L demo that
you showed. Um,
generally speaking in the the web
application and so world, it seems to me
like the whole VIP coding idea is great
for prototyping, but you can also see a
lot of people shooting themselves in the
foot with VIP coding.
>> Oh, yeah.
>> Now you're opening this up in our EOP
world where it's even easier to shoot
yourself in the foot. So maybe it's just
the grumpy old guy seeing that others
can now do what what I used to be able
to do in the past exclusively. And and
I'm I'm scared of that. But I I really
am scared about people doing things they
really shouldn't be doing and then
getting back to us and complaining why
is this even possible. Um so
>> I I'm a bit scared. I understand it's
technically fascinating but I'm not sure
this is the direction I want to see the
product go. Do you share those concerns
or how do we see
>> I I I share and understand them. Um it's
definitely something that we are also
considering how to handle um in these
demo.
>> I mean first of all
>> that yeah
>> it is a it is a prototype um an early
one uh but we also see some potential in
being able to make changes for yourself
in these scenarios um and maybe even a
little more
uh than that.
>> Yeah. So one of one of the purposes of
showing it is to get feedback, right?
And the whole life cycle operation of
having these extensions is a super
interesting point. How do you manage it?
How do you get support for it? How do
you understand when it's broken? When it
breaks something else like in in example
here, we're working off a sandbox. So
anything is possible. Who cares, right?
It's just a sandbox. But in production,
I mean, the rules are different.
>> Yeah,
>> we need to figure out how that works.
>> And maybe there's a different way of
doing this. Maybe we can have we talked
about the the limiting version of of
this that could do designer experiences
or other things. So absolutely a huge
topic around how can we control manage
and support this in in a real scenario.
Right. Yeah.
>> But that that said we also think that
this is a natural way forward for end
users to do some changes.
>> Yeah.
maybe probably a little more than hiding
moving fields around because that's
that's not a lot. Um, but
>> for the the the personalization design
story, we already kind of have that. So,
just to have another interface to do the
same thing. I mean, that that doesn't
make it too much more complicated.
>> I think we can do more.
>> Yeah, I think we would like to do more.
>> Just the like the the analysis view that
I just showed here is a great example.
uh why do I need a developer to put that
or share that with others today I need
to export import and all these things
why can't they just put in an extension
for example like these kind of things
could be things we consider like how can
we promote personalization to
customization how can we share with
others how can we yeah add a whole new
page that collects information that I
want to see based maybe on analysis view
or query or something I create we talk
about the data on demand I want to see
these top 10 customers by region
whatever and then we get that page. I
mean, I would love to at least see some
controls for partners then so that we
could for our customers then maybe say,
"Okay, this is
>> we whitelist you to do personalization
and maybe add a page, but everything
else is blacklisted because I
>> I really don't see us supporting that
for customers. That's really
>> we have to figure that out together,
right?
>> It's a it's a discussion to open up
scenarios
plus who, right? Who's the make a
persona at the customer? Is it an admin?
Is it a power user is it the end users
what are the different scenarios that
they could do right
>> you can I I at least could imagine users
themselves move things around adding
things like we already have the add a
field uh thing where it's an existing
field but I could also see customers
adding a field for example as a make a
story a new field maybe to do data
versus integration but it maybe not the
user doing it but somebody being an
admin doing it potentially in a sandbox
that we provision super simple
So you can test it out in a sandbox
before you move it to production. So we
get back to this life cycle thing. I
think it's a that the from the labs is
more like an inspiration of where things
could go, but we definitely have to have
a discussion about what are the safe
scenarios
>> for whom and the life cycle between
sandbox and production, right? Because
absolutely
>> we want to, you know, we want to protect
production as well. Just like we had the
question before about debugging in
production, right? That's why we make it
hard to do things like that in
production. But but we world is also
moving towards the empowerment uh for
the customers.
>> Yeah, we are out of time now. Y
>> so thank you all for staying. You
[laughter]
>> have a great conference.
