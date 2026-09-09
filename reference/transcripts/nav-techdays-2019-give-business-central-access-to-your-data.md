# NAV TechDays 2019 - Give Business Central access to your data files

- **Source:** https://www.youtube.com/watch?v=5jdwO6d_UEQ
- **Video ID:** 5jdwO6d_UEQ
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 79m06s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Today we will be talking about files
and
a little history
perhaps still the current story.
In our companies we used to have and may
still have our own file servers.
We are storing our files, we're taking
care of our own backups.
We have a way to bring the files into
our organization.
It may be automatic, we may have our own
FTP server.
They may be delivered through emails. We
may even give them get them manually.
And we have through the years
in the older releases
figured out a way to get them imported
into our business ERP system.
Now
most of us would have wanted to
implement the job queue
and have the import automatic.
Depending on where the files are
located, it might be possible, perhaps
not.
I have seen cases where customers have
needed to use .NET on client and running
the Windows client in order to get
access to the files just to be able to
automatically import them from there.
And of course the manual
is always the safe way and a lot of
companies are using that today.
And also
whatever file format you are getting
we are used to writing our own code to
handle that file and get that file into
our documents or our tables, wherever
they need to end up.
So, file shares
drive SSH, whatever
we could mount file shares from
wherever.
And this is our current story.
I believe that
most of you should be able to relate to
having your local organized C drive. You
have a folder called work. Under that
you have the customer. Under that you
have whatever. So you have your own
structure. You feel comfortable with
what you're doing. And you know where to
pick up the file whenever you need that
file.
Now, and this is perfectly good and all
working for Business Central and NAV
on prem.
But we are going not just into the SaaS
world where we can get access to
Business Central
in the in Microsoft cloud.
We are also going to the world where we
have a hosting partner that is hosting
our Business Central.
Not necessarily Microsoft, perhaps
someone else.
But in the same story, we do not have
access to their file system and they do
not have access to ours.
So how do we bridge that gap?
First let's
introduce myself. My name is Gunnar
Gestsson.
That Thor in the middle.
I know there are some Icelanders up here
which can help me with that. This is the
same name you see in the Avengers movie.
This is the lightning
the god of lightnings. So this is Thor.
I don't know why the presenter did not
choose to use that.
Here you can see my information. This is
my own little company back in Iceland.
I have been uh
uh working in this business since 1994.
And have been an MVP for 7 years now.
Uh
been on stage here before and it's
always a challenge.
Big screen behind me.
A lot of people up there.
And it's great.
We all need to do this at least once,
right?
So today
I'm going to be talking about these
topics.
And we cannot talk about files without
talking about the data exchange
framework.
So
one question.
Are you using the data exchange
framework in your current version? Can I
have show of hands?
Exactly. That's why I'm going to talk
about it.
How about the job queue? All of you are
using the job queue?
That's much better.
Any incoming documents?
It's almost the same as the data
exchange. So
this is why I wanted to pick on these
topics for this session.
The data exchange framework is something
that Microsoft delivered first in 2013
R2, if I remember correctly.
And the idea between the data exchange
framework is that you have a destination
where you need to bring your data.
In their first example, I think we had
bank account statement.
But you may have
different banks, different file types,
different APIs to talk to.
But and that's why they
introduced the data exchange framework.
In that framework, you can
customize the flow of data
from the start to the beginning.
From the start to the end. That's it.
Okay.
Now the job queue has now in later
releases uh
been built on top of the new task
scheduler.
I will talk a little bit about that.
Incoming documents is kind of the inbox
for Business Central and NAV. This is
where files are being dropped and then
processed.
Uh
I'm going to show you a few demos on
file services.
Just uh there are here four demos that
I'm going to do. There are more.
And then in the end I'm going to
uh talk a little bit about document
scanning cuz that's kind of a new story
now.
Now, let's start with the data exchange.
So, what is data exchange framework?
This is a process definition
of importing and exporting files.
You define the process
both for import and for export and you
define the lines and the columns of your
data.
And
bring between the data and your actual
database or your tables, you need to map
field by field.
When we are importing data, we might
want to
transform the data.
And that's why we have transformation
rules. So, you bring in a text and that
text need to be transformed in some way
in order for Business Central to
understand what it's about.
An example of that would be
I'm importing my credit card statement
into my ERP.
And
a part of the amount field is ISK, which
is the Icelandic krona.
And of course, I cannot evaluate that
into a decimal. So, I need to
cut out the ISK before I can evaluate
that as a decimal and that's one of the
things that the transformation rules can
do.
And then I'm going to spend a few
moments
uh demoing how to extend or a way that
we can extend the data exchange
framework.
So,
first about the process definition.
This is uh as you could should be able
to see the
the title name of the page. This is data
exchange definitions.
And these are the definitions you will
see in Cronus International today.
Mostly about importing invoices into our
purchases,
UBL invoices in the Europe.
And what we also have
a bank statement import, and we have a
definition for our currency exchange
service.
If you look little closer
at this fact,
the process goes from right to left
depending on if you're importing or
exporting.
So,
data import begins on the right.
You execute the feedback code unit, and
then you move to the left. And when you
get
when you finish the track on the left
side, you go into the mapping process.
If you're exporting, you start with the
mapping process, and then you go to the
right until you end up in the feedback
process.
And the feedback process is all about
the user.
So, feedback process you use when you're
doing things manually.
So, you can ask for an authentication if
you need an API call,
or you can ask for a confirmation that
you want to start things, and the same
thing in the other end if you're
exporting. You can notify that user that
the the export has been finished, or the
import has been finished.
Now, this code unit here, this one takes
care of reading the actual file.
That is, taking that piece of blob that
is the file and putting that into a
table in NAV
or Business Central.
And this is the table it's going to be
in.
We have this data exchange table.
There's a value
uh file content blob value field and
this field will contain your file. And
it doesn't matter if the file is
imported from your file system, uh if
you download that file from an API or
whatever, this is where the file will be
stored and this is our first task when
we're importing file. If we are
exporting, this is where the file will
be
brought from and exported or uploaded to
your destination.
Third step is to actually read the
content of that file.
And
that content is being read into fields
into a table called data exchange
fields. And here we are utilizing the
column definitions and the line
definitions.
And the other way around, if we are
exporting data, this is where we
take the data that we have in those
fields and create a document layout, an
XML layout for example, using an XML
port.
And the arrow here that is pointing
between that code unit and the XML port
is because it's always the code unit
that is executed, but there is a code
unit that actually executes that XML
port.
So,
you are never using both of them. It's
either or.
And this would be the file
the fields table.
And you can see that the data that we
bring in or the data that we're bringing
out will be in this
value field, which is currently
250 characters.
And that might be an issue for us.
Because we will
find our
find the examples where we need more
than 250 characters in a field.
And
what they did now in version 14, I
believe, is we now have a value blob as
well in this table.
So, we have a function to set value and
we have a function to get value. If the
value is too big to fit into this text,
it will be stored in the blob.
And if you need that in your older
versions, just take a look at how it's
done in that version.
This is a screenshot of the
line and column definitions. So, for
each line definition, you have this
specific layout of the data.
If you have an Excel file, then you
might read this is the header line and
this is the
details line. The same thing goes with
the XML file. You have this node, which
is the header information, and then you
have another node that is the line
definitions. And this is an example of
the
uh
of the UBL format.
And
we have the headers and we have
the lines.
And each of those has its own set of
columns.
In the columns, we can define this
column number, this one is this XPath,
or is this string between this and that,
or if we have a variable
delimited file, we can say this is
column 1, 2, 3, and so on.
So, we have pretty good control over
defining our fields
uh
from the imported data and as well to
the exported data.
The validation code unit, we can use
that just to validate the content in the
fields table.
As you can see, Microsoft is not using
that here in these examples, And I I
even believe that their standard process
is not even
executing this code unit if it is there.
But that's its main purpose with this
code unit. That's validate the field
content.
Now, finally
in this process
we have a data handling code unit. And
this code unit is always
1214 if we are
using the data handling functionality.
So, what is the data handling part here?
In the data handling, we are copying the
data that we have in the data exchange
field over to another table that has
another layout, a little different
structure. And that table is called
intermediate data import.
So, if we are using intermediate data
import, we need to specify code unit
in this place.
And let's take a little bit into that.
This would be the layout, well, the
first fields on the intermediate data
import.
And the value
in this table is structured a little
different than the values in the field
table.
So, let's scroll back a little bit.
Here we have the fields table.
And as you can see this the data here is
by
lines, by record, and by field as the
line definition specifies.
You can see that See that on the first
fields.
If you go forward again
into our intermediate data import the
data here is structured by the
destination table. So, it's the table ID
in our Business Central, it's the field
ID in our Business Central.
So, the data is kind of moved in a way
so that we can easily handle that
from our business central point of view.
We do have a problem here though in this
record
we have no space for a value blob.
We will need to figure out a way to
get the data through this process if we
have a big
big value. We might even have a base 64
encoded PDF document in our XML file
that we need to be able to handle.
Here we go into field mappings.
This is
from the line definitions. Each line
definition can have one or more field
mapping. It's not requirement. It can
have one or more field mapping.
And we will have different field mapping
based on the target. Are we going to
Is the field mapping directly into a
destination table or is it into the data
or into the intermediate data import
table?
And let's see the difference between
those two.
This would be the currency service
import.
And this one is automatically created
when you configure your currency service
import.
Table 330, that's the
currency exchange table. So, we are
importing data directly into that table
using a mapping like that.
And you can see that there is a flag
there specifying if this is
an intermediate data
table or not.
And look at the columns that we have
to set up the destination.
We have the columns from our column
definitions.
We have the name from there and we can
specify which field in our table 330 the
data will end up in.
And we have this optional field which
specifies that
well, we might get a an XML file that
sometimes has this value and sometimes
it's blank.
So, if we if we get data that
sometimes has value and sometimes not,
we need to
to mark this as an optional.
And then we also have the possibility to
add a transformation rule.
If we look at the other way, well, this
first Is there any way for you in the
back to see this code?
I don't think so. Well, you will get the
slides. It's going to be on me booster.
So, you will have to believe me when I
tell you what's there.
So, this is a code that is importing
using a field mapping from directly from
data exchange field into the target
table.
And this one is using record references
and field references. So, this is kind
of a universal code that you should to
be able to use more or less in whatever
process you need.
However, this code is currently inside a
bank statement import procedure. So, you
will need to bring that out and you will
need to create your own
field mapping code unit to handle your
code. You might find a way to do a
generic one.
But in some cases, you will need to
create a specific field mapping for a
specific
But this is the skeleton you would use
in almost all cases.
So, this one is looping through all the
records being imported based on the line
and column definitions. And then it's
going to pick up the
field mapping and insert the data with
validation into the target table.
So, this is gives you the flexibility to
get whatever data
and whatever mapping into whatever
table.
Next we look at the
uh mapping into the intermediate.
And there we see this is table 1214.
And this is always table 1214. This is
the same number as the code unit that we
saw. So, 1214 is a number that you will
remember from now on.
Because this is what we will be needing
to use in our daily work.
The difference in there is in the lines.
You see that each line has now different
set of columns than it had before.
We not only specify the column or the
field number that we are importing into,
we also can specify different tables.
So, by this structure the data is
formatted into the import data or the
data Yeah, import intermediate data
import table.
And we also have that uh
optional field there, which is
which is uh well, might be hidden. We
have the transformation rule, and we
have something called the validate only.
The validate only is is uh
thought exactly as I said, we are not
going to use that data as an import
data, but we would like to validate that
the data in there is whatever we are
thinking about or whatever we need. For
example, we can see that the GLN number
is validate only. That's because if we
get an invoice, we would like to match
that the incoming GLN number matches the
GLN number for a company. We are not
going to accept an invoice for another
company in our data.
In this mapping, we can also see we have
option for three mapping code units.
Uh we can put in logic that happens
before we actually map stuff.
And what we do there is
like in this example here,
we are mapping that description to a GL
account. We are searching for the vendor
and we can do all kind of modifications
to the data that we have in the
intermediate table before we actually
execute the mapping part that is in
1218.
1218 as the mapping code unit, it is
required. You need to specify a mapping
code unit. The pre and post, they are
optional.
And
the code to actually
apply the data from the intermediate
data into the
tables
is that simple.
It basically loops through the
intermediate data
for a this specific table and then it
initiates a record and applies the data.
Now
the transformation rules, we have a
table in Business Central with
predefined transformation rules that can
do a lot of things.
And we have these types.
Replace, we have regex, we have
daytime formatting, which means that we
can specify our
our local settings for the date. We can
import the US dates,
Danish dates, Icelandic dates, whatever.
And we also have this if you look at the
bottom there, we have a custom,
which means that we can write our own
code unit,
shove it in with an extension and if if
we do that correctly, it will be
discovered as a transformation rule and
we can use that in our code.
And that one in the bottom there, the
Unix timestamp, this is an example of a
code unit that is
a single code unit that is a
transformation rule.
Do we have any idea what's a Unix Unix
timestamp is?
Yeah, we do.
Seconds since Jan- January 1st, 1970 or
something like that.
So, it's just a big integer number that
can be converted into a date. And the
type helper, of course, in Business
Central has a way to do that.
So, let's look at the extending part.
This code unit 1240,
this is the code unit that's supposed to
bring the file into Business Central.
And let's look if we if you look at the
code,
in Business Central, they have added
an event
into that code. This used to be just a
file picker and nothing else. Now, we
have an event, so we can actually do
something before
the code unit pops up a file picker for
the user.
So, this gives us
new possibilities.
Let's also look into
an example where we can extend this one.
And what I like to point out here
is this new code unit that you see
in the bottom.
There's a code unit called Temp Blob.
And this is one of the breaking changes
between version 14 15.
Uh
I believe that Temp Blob table was the
table that I used the most.
So, now I'm switching to that Temp Blob
code unit, and you will have to do that
same if you're not already there.
Temp Blob is these intended storage for
a binary or a big data,
and you can pass things around with that
code unit like it was a
like it was a record, yeah.
Behind that code unit, there actually is
a table.
So, what this code unit does is I have
the possibility to use that set
procedure to inject data into that code
unit, and then it will subscribe to that
event
and deliver that data into that 1240
code unit.
But, there's one thing that I would also
like to point out here.
And this is something that I believe all
of us need to know a little better.
That's the first line there called an
event subscription equals manual.
We have been using the eventing model
for few years now.
There's something that happens, 1240
triggers an event, and we have a lot of
code unit answering that call.
But,
we should be trying to control who is
answering the call and who is not
answering that call.
And what we what we do is we put
this
property on the code unit that's
supposed to answer the call.
And then we enable this in our code, and
we
disable this in our code. That's why
That's how we make sure that we are not
calling something initiating a code unit
if we don't need it.
And how do we do this?
This example here is
the bank statement import. When we
import a bank statement,
we use this format, we call code unit
1270.
And that code triggers that data
exchange framework flow
from back to finish, and we should have
a data in our bank statement.
We can, of course, replace this code
unit with our own.
And this could be an example of our own.
We have here a code unit that
that's just doing some preparation work
and then it's calling
and it's returning. So, and the
preparation work here,
if we look closely,
we are downloading a file.
We are putting that file into that code
unit that I showed you earlier.
And we are using what's called a bind
subscription.
So, what we do with this bind
subscription is that we
activate
the subscription in that specific
instance of that specific code unit. So,
so not just any code unit will answer,
not just any instance of that code unit
will answer, but the just this specific
one.
So, if we have the normal subscription
model, if we have a normal
uh code unit that's answering an event,
that means that when the event is
executed,
a new instance of that code unit will be
created and that will answer that call.
But that new instance
will of course be blank. It will not
have any data.
So, how can we make sure that the one
that's is answering the code actually
has some data to deliver?
And that's by doing it that way.
We put in the data, we bind the
subscription,
then we answer that call, and then we
unbind that subscription in the end.
If you want to look close
a little closer into how this is done in
this standard application, you can look
at the posting preview functionality.
This This is exactly what they're doing
there.
Now,
that's it with the uh
data framework. We'll
show you a little bit about that in the
demo.
So, now I want to switch over to the
job queue.
The job queue
is a background task and it has been
available for quite some time.
Uh
Microsoft is using it more and more with
it with each version and they have even
now added something called a page
background task which is also giving us
a lot of possibilities but that's not in
the scope here.
So, this is about automating tasks or
offloading them to a back from session
so that the user doesn't need to wait
for it.
I upgraded my own ERP
I believe a year ago or something like
that and I used to send out
invoices through PDF in the email.
I used to do post and send and then I
would wait 10 seconds and it would be
gone.
Well, I upgraded that system. I did the
same thing. I did my invoice. I pushed
press and send and boop.
Nothing happened. Well, it kind of
looked like that.
So, I really needed to dig into it. What
actually happened was Microsoft decided
they would not want the user to wait
these 10 seconds.
Instead, what happened when I pressed
the post and send
it actually scheduled a new entry in the
job queue.
So, that background session was
executing for 10 seconds and did the
same job.
This
is happening
more and more in uh the
the uh Microsoft solution. We are seeing
data upgrades being pushed to the
background session and this is of course
something that
all partners writing their software
should utilize as well. We do not want
customers waiting
for their
ERP system to answer.
We can also use this technology if we
want to create an asynchronous API. If
you want for example an API that will
post sales order, we may not want the
other end to wait while that post is
executed. So, we could trigger it.
It will that trigger will schedule the
posting part, and then they can just
ask, "Are you done?"
So, back before
2017, we had something called Navision
application server.
Back in the days, this was our Fin SQL
without UI.
Basically, with nothing else.
And this NAS is still there in the
product.
But, it's not used by the job queue
anymore.
So, what NAS does, if we activate that
on the service tier, it's it fires up a
service. It fires up a session that does
a specific job. It used to
uh
loop through the database
in the job queue and see, is there
something I need to do?
And that means that the instance was
talking to the SQL server every 2
seconds asking, is there something I
need to do?
And guess what happens when Microsoft
brought their solution to the cloud,
and their solution was asking Azure SQL
every 2 seconds, is there something I
need to do?
Well, of course, they got a huge bill
from Microsoft.
So, that was one of the great things
with that
uh cloud implementation from Microsoft.
We actually are getting a better system
out of it.
And they figured, well, we need to find
a different way than to ask the database
every 2 seconds
if we need to do something.
So, they built the task scheduler. It's
based on the same technology that we see
in our operating system.
We schedule a task, and the instance
will just start that task when the time
comes.
And there's a table in the database to
keep track of all our tasks so that if
the instance is restarted, it will read
that table and reschedule that task. And
it's a lot more stable. It doesn't take
out all the resources.
And it's a better solution for us.
We have a configuration.
We used to be able to create a lot of
job queues
to have multiple sessions going at the
same time. Now we have a configuration
in the service instance which specifies
how many of those tasks can be executing
at the same time.
10 is the default one.
I believe that's the same even if you
have 100 tenants
hooked to your application. So you might
need to configure this based on the
amount of power that you have in your
machine.
But we have always had problems with the
task scheduler.
There are problems with handling errors.
We will have errors
when we're scheduling tasks.
Some tasks just don't start and some
tasks just don't complete.
So we will need to figure out a way or
workarounds
to at least manage these things.
And I'm here suggesting three
options. The first one,
make sure that the user will know if
something is failing.
The second one, make sure that you have
a task that cannot fail.
That is responsible for all other tasks.
The third one,
create an error handling, some smart
code that can actually look into what's
going on and fix or restart,
notify or something else if something is
failing.
A simple
way for the UI, add a queue box on the
UI with a number of
failing jobs.
So, at least the user has the
possibility to do something about it.
The second here,
and this is the exactly the code that
I'm going to be
demoing or in the demo.
This is the code that is running every
X minute.
And this code shouldn't be able to fail
because the only thing this code does is
actually spin off new tasks.
And since the task scheduler and
everything about the job queue is
designed in a way so this shouldn't be
able to fail. This should always be
executing.
Even if all the sub tasks are failing,
this should be running.
The same thing goes for the monitor. You
maybe saw that, maybe not. The second
task this handler is starting is
actually the monitor, the error monitor.
So, it will spin up the error monitor.
The it will take a quick look at the
status and then finish.
And what the error monitor does in this
case, it checks four different code
units, if they have error,
it's going to tell someone about it,
update the status somewhere, write in
the activity log,
and it's going to restart that
service.
Of course, in some cases, you might need
to put some
smart logic into this and figure out,
okay, it's now stopped 10 times, let's
not restart it, let's do something else.
And of course, when you're starting
jobs, you shouldn't
be starting jobs that are already there.
So, just verify that you have a job that
code unit running for that record,
and you don't want to start it unless
unless there is a missing one.
So, that's it with Job Queue.
I said that incoming documents is the
entry point or the inbox for documents
into NAV.
This is the place where we get documents
that are supposed to be converted into
purchases, sales,
and GL journals. Of course, we could
utilize this to do our own formatting as
we want.
And for each incoming document, we have
a set of attachments.
Uh one The one attachment that is the
main attachment is always the XML file.
And that file is used to process that
incoming document into our purchases,
sales, and so on.
There may be a binary document, and we
have built-in OCR service,
or at least we can use a utilize a
built-in code in Business Central to
send our binary document to an OCR
service, which will deliver an XML
document, which will then be the main
document.
And we can have multiple supplemental
attachments as well.
So, we could have a PDF document that
is, for example,
with the original UBL invoice as a
supplemental attachment.
And when we use this process of posting
or creating a document and posting a
document that originates in the incoming
document, we will have the full
traceability throughout the system.
So, in our GL entries, in our customer
entries, in our vendor entries,
we will be able to see the original
incoming document with one click.
So, this is the This is the place that
Microsoft intended for us to bring our
document into the into the system.
Of course, this is and should be
available from the
role center.
This would be we have here 12 incoming
documents. And the incoming documents
are with their own status.
And the status, of course, can be new
and then all the way up to be posted.
There's also a flag in incoming
documents specifying if it's handled or
not.
And if the document is handled, it's not
going to show up in the role center
anymore.
And we have multiple ways to get
data into our incoming documents. The
standard one
is the manual one. We just click this
button and we import whatever file in
there.
If you open Business Central up in your
phone or or tablet or use the universal
app, you will see import from camera.
From my point of view, you should not be
using that. And the simplest reason is
that image that you take from your
camera will be in full resolution in
your incoming document. So, it's going
to be a huge image.
At least for the modern phones, they're
going to make huge images.
For our goal here
is to create these incoming documents
automatically.
So, they should just appear
as we go along.
Tradeshift is doing that already if we
are using Tradeshift in our Business
Central. So, Tradeshift will
download our UBL documents and put them
into incoming documents.
We could, of course, do our own custom
data flow.
Or we could even attach a document
scanning feature to this one. So, you
can say new incoming document from
scanner and put your document into your
scanner next to you.
So, this it doesn't really matter how
the data is created in there.
But, how is it processed? And that's
that's kind of a mystery for a lot of
people. There is something called
data exchange types. And this is a list
of possible types that you want to be
able to process from the incoming
documents into your system.
And these four types, OCR debit credit
and UBL debit credit, these are the ones
that we
we have with the
uh with the solution.
And this basically is just a link
between the incoming documents and the
data exchange framework.
You can see that the third column there,
this is the data exchange framework
code, the definition code from the data
exchange framework.
So, if the incoming document has that
type, that specific data exchange
framework is going to execute this
logic.
And there is a code in Business Central
that actually is executed whenever there
is a main document.
And what this code does, it tries with
all those, in this case, four methods,
it tries to read that file.
And that file
must be an XML file. It must end up in
the intermediate data import because
this one here is just going to count the
number of records in that intermediate
data import table.
And whatever import generates the most
of the records in the intermediate data,
that's the one that's going to be
selected and stamped on this incoming
document.
So, you can create your own readers,
your own process, and your own data
types, just as long as they will create
better results than the ones that are
already in there, then they will be
automatically picked as the one you
would like to use.
So, we could get all these file types
into our incoming documents through the
data exchange framework.
Or we could even
do that manually, but we must be able to
convert those files into XML to have
that main document. That's kind of the
the thing that you need to remember if
you want to process incoming documents,
they must be an XML file.
All right.
The user processes this with just this
click of a button.
Create a document. This is not enabled
unless there is an XML
main document in the incoming documents.
So, fast
and
brief
introduction to these
systems. So, let's look at the file
systems
or the file services.
There are of course a lot of services
out there.
Dropbox was probably the one first of
them. Can I see show of hands how do you
are you using Dropbox?
Not not that much.
Is there someone here who actually knows
what RushFiles is?
One, two. Okay.
Cuz I needed to create an connection
with RushFiles because they had
uh a customer was using them.
I guess I'm doing an an advertisement
for them now.
What?
Of course, we have OneDrive. We have
OneDrive in
both in the old classical way linked to
our live ID. We also have OneDrive in in
our office now, OneDrive for business
which is based of SharePoint.
And we have these Azure blobs and the
Azure files.
Of course, there are more.
Google
Apple and so on.
But what we really need to be able to
use these guys is an API.
And all of these, they have APIs.
So, Business Central will use that API
to talk to these guys.
Here is a
few slides just with a list. Of course,
you should be able to bring that up from
me booster as well.
If you want to use Dropbox, this is the
client. This is the URL. And most of
all, there is something there called an
app console.
So, every user can create an app in
Dropbox and that app is accessible by an
API.
I will demo that a little later.
RushFiles
The same thing goes there. We have a
reseller, we have a company, and we have
a token to authenticate to RushFiles so
we can do the same things there.
OneDrive is part of SharePoint.
Uh we can download that OneDrive client
to synchronize the data.
Uh
The API is through Microsoft Graph.
So, we need to be able to authenticate
to Microsoft Graph through Azure AD in
order to use the endpoints for OneDrive
for business.
There is a new playground that we can
use
to play along with play with that
OneDrive for business.
And then again, with any
Microsoft Graph endpoint which will now
include the
Business Central in SaaS environment.
And I encourage you to look at this
this uh
Graph Explorer
in Microsoft and see what you can do
with it.
Now, Azure Blob has been there a long
time.
And this is a probably the cheapest
storage you can find
for any kind of files.
And it's fast and it's easy to integrate
whatever with Azure Blobs.
What I for example, when I started to
use Azure Blob,
I decided that I didn't want to save or
store my binary files inside Business
Central.
So, when I dropped a
a TIFF image or a PDF file into incoming
document, instead of storing that in the
database, I pushed it up to Azure Blob.
And Azure Blob gave me a URL and that
URL is the only thing that I stored in
the database.
So, I like to push the binary data out
of the database and just shove it into
Azure Blob.
There are
a storage explorer for Microsoft where
we can use to
just look at what is in our Azure Blob.
We can upload, download, delete, and
whatever.
Uh I found one software there called the
GoodSync.
That's one can synchronize between A and
B. I think this is a paid version. I
just wanted to put something up there.
So, but I could was able to set up a
synchronization between a folder and
Azure Blob with very very little effort
using that tool.
The API information is there on the
Microsoft Docs.
And the authentic- authentication part
perhaps is the most complex one, but we
now have uh
you will have you will have examples
both from Microsoft and from my
repository, so you can easily grab the
code that you need to authenticate to
your Azure Blob.
And you manage this through the Azure
storage account in your Azure portal.
Azure files,
it's almost the same thing as Azure
blobs. The difference between Azure
files
and Azure blobs
is basically you can mount Azure files
as a drive.
And you can
install a
software from Microsoft to synchronize
data from your server
into Azure files.
And it has a very similar API. So, if
you can talk to Azure blob, you should
be able to talk to Azure files as well.
And it's managed on the same site. It
has the same storage account. It can
have the same access key.
And we will now let's take a look at
that.
This is a I just wanted to put it in
here. You will It has no meaning here,
but you can use the letter. This is the
PowerShell script that's used to map
Azure
files on your computer, whatever that
is.
Now, let's do a little
demo.
Uh I'm here in a machine somewhere in
the cloud.
And this is the storage explorer that
I'm running.
And I have here a blob container
called session, and there is nothing in
this container.
If I switch over to my browser,
I can see that I have containers here on
the portal.
And we can create as many containers as
we want, as many storage accounts as we
want. And we can place them in a
whatever region we want.
When we have created our container,
what we need is the access key for the
container.
So, we need to know the storage account
name, the container name,
and the access key, which is here.
Similar things go with Azure files. This
is the same
uh storage account.
It's just shares instead of files.
So, if we go to the overview here on the
storage account, we see that we can
create containers, and we can create
file shares, and
tables and queries, which is not in the
scope here,
in the same storage account.
And in this demo, I'm just using the
same account, which means that I'm using
the same access key.
If I go back into the storage account,
and this is my session blob,
I can just simply upload files through
here,
and uh
let's just browse for them,
because we need to have uh
we need to have uh Business Central
being able to
see some files.
So, uploading them into the container
should be just like that, and we should
be able to verify that
in our container in the portal.
So, in our session container,
we should now have files.
There is an upload and a download
functionality in here on the web as
well.
So, while we are doing this,
doing development and testing things, we
can of course verify everything just
through the website.
Uh
the PowerShell script
that I used to map the Azure files
results in a drive on my laptop, or on
my computer.
So, here I have a drive called S and
this is my
files on Azure drive.
And of course, we need to put some files
in there as well.
Let's do that.
This would be
Yeah, let's go
to the desktop.
Here I have the demo files.
I want to copy some of them
any any one of them to my
S drive.
So, proof of concept.
Now we have files in Azure files and we
can verify that as well
in our portal.
If we look at Dropbox,
we used the app console to create the
app.
And when we have done our app,
which is here in this example is an app
folder,
we used this generate access token here
to create the access token that we
actually use when we link to this API.
And what happens in our Dropbox,
if we have one example here,
is that in our Dropbox, we will get the
apps folder and inside the apps folder,
we will have all our apps.
And we let's drag some files into our
Dropbox as well.
More demo files.
Now we have files in our Dropbox.
But of course,
we should be able to have files locally
as well.
We might have our solution on prem. So,
this is my local
drive
from the container point of view
because I'm running Business Central in
a container.
And let's just copy a few files
in there as well.
So,
I have files now all over the place.
Let's look at my PC. Hey, I also have
the rush files here.
So, that is also a drive and in my home
folder
in my import, I also have some files.
So, I've now placed files
manually into a lot of places.
So, how about document scanning?
We have been used to creating a
solutions that
utilizes our twin scanner. We have
bought a solutions from partners to do
that.
Uh
not to try and
get you to return those products, but
a document scanning is a feature that we
have in almost every on any equipment
that we find.
We have document scanning in our phones.
We have document scanner on our in our
offices. And if we have file services,
we should be
it should be both both fast and easy to
scan a document.
This is the Office Lens app from
Microsoft on
on your phone probably already.
It's quite easy to scan
a receipt and invoice with Office Lens.
You can actually crop it and and and fix
it up and then you save it as a PDF in
your OneDrive.
And that should just end up in your
incoming documents.
This is the solution that I'm using
myself.
So, I'm
I have my Dropbox app linked to my
incoming documents.
So, if I
go somewhere and spend some money
as a company, I need to make sure that I
scan that receipt or that invoice into
my app. And you can all see the name of
the app of the app. The app name is two
NAV.
So, it's quite easy. Whatever I put in
there
will be in NAV.
And if you have your office already set
up with
an equipment that can scan,
then of course that one can scan your
invoices and your attachments
to an email,
to a file,
and wherever.
Just hook that up to your file services.
There's one else here, one one more
thing that I want to point out.
Microsoft Flow is also a great way to
pick up these attachments, these
invoices, and put them into either a
file service or even directly into your
incoming documents.
And Arjan is going to demo that for you
tomorrow.
He's actually going to show you how he
can send or I think he's going to ask
you to send him an email, and that's
going to end up in his incoming document
by using Flow.
But it's the same general idea here.
And if you get
invoices in your email,
just drop them into the
file API that's being linked. That's
what I do. I just drag them into my Tuna
folder in my Dropbox and they will be in
the incoming documents pretty soon.
Now, because we want to use the data
exchange flow, we need to create a code
that can grab whatever we put into the
file content
and just put that into incoming
document.
This is an example of a code that does
that.
And just to make sure
I will give or I will give you all
access to that demo code and that code
that I have been showing here today so
you can all
clone that one from Git and see what's
happening.
And you can see there in the bottom that
if I have my OCR service active,
we will actually send that binary
attachment to the OCR service using the
job queue.
So,
more demo.
First,
this is the Git repository.
It's in DevOps.
And if you
go to this
repository, you will get access to all
this code.
And there's a lot of code there. This
code is just a proof of concept. This is
not a product.
Uh but that means you should be able to
find in there some useful
uh procedures, some useful
uh
well, code examples.
And
if you need, use it as whatever you
want. It's just It's just there for you
to use it.
Now, let's look at that product that I'm
talking about.
I need a password.
The code has two
uh
apps.
We have two apps in the workspace. We
have an AL app
and we have a test app.
It's broken down into
functional areas.
So, the code will have a dedicated set
of files
that handle Azure blob, another set that
handles your handle Azure files. The
idea here is here is that I have a
framework
and then I want to be able to add
interfaces to that framework. One
interface being Azure blob, another
being Azure files,
rush files, server file system, and so
on.
So, if we figure out more APIs that we
can hook up,
then we can just add that to that
framework and it should work. The
general idea here
is that the user should always expect
the same constant environment.
So, what we have up here
is we have something called a file
providers.
And here
in the interface will self-register,
we can have our local server environment
and then we can have all those file
services that I have already hooked up.
For each of them, we have some kind of a
setup.
We have set up for our local drive.
If we go into the Dropbox setup, we can
see that we put in the Azure
Sorry, the access token.
And we have a verification that this is
the correct app that we are talking to.
In
Azure blob,
we need to specify the account,
the container, and put in the access key
that I showed you earlier.
And you can even do this now if you got
a picture of the access key.
The same thing goes with Azure files.
Just the share, the container, sorry,
the share, the account name, and the
access key.
So, it's quite easy for the user to
configure this and and make it work.
I'm not going to go into the rush files
demo.
But
this page that I have open here, this is
a page I call import setup.
And I can configure a more than one
import setup for each provider. So, I
let's say that I have
I would like to see all XML files from
this Azure files. I should be able to
configure something like that, and I can
go into process and just verify that I
can see the files that I just copied
into the environment.
And this is the list of files. I can go
into all of those, and I will prob- I
would be seeing the same
results.
And this is the same UI talking to
different interfaces, to different
services.
So, what I also put in here is a data
exchange definition code.
Cuz when I bring that file into
Business Central, I just The only thing
that this import part is about
bring that file into a content, and then
the data exchange takes care of the
rest.
And let's do a a short example here.
We have files
on the server. We can see what files
there are.
These are the files that I copied into
my container directory.
And I can decide that I want to create
what I call import entries.
And creating import entries basically
importing the directory, so I can see
the whatever I put in
my folder is now represented here.
And these This is something I need to
do. I need to import these things. And I
can go through the steps.
I can import the content of the file
into the data exchange.
And I can also process that with data
exchange to
my incoming document. And when I've done
that, I can navigate to the processed
entry.
And I should be able to see the incoming
document that I did. And based on the
data exchange flow that we create,
the destination may not may be something
different than the incoming document.
So, the data exchange flow just decides
where will this document end up? Is this
going to be a sales order? That's very
well possible.
But of course, I'm not into doing things
manually.
So, what I can do here is I can actually
go ahead and
start
each one of those
with a job queue.
So, let's enable these guys.
Let's do it fast.
So, I've now enabled uh
five job queues. I should be able to see
job queue entries just to verify that.
And as specified,
the job queue entry that start is just
the handler, the one that case takes
care of spinning up other tasks.
So, now I have the job queue running and
these guys should be imported
automatically
every minute now.
It may have started. It may have
Yeah, we are already getting files for
each of those import setup into our
system. They start by being new and then
they will be processed and imported.
So, this is the This is the
functionality that's in that app and
this is the functionality that you can
get from that Git repository.
Uh
Of course, being a Git means that you
can create a pull request, you can fix
things and uh
do things a little better.
There is one more thing that I would
like to show you because we have some
time.
Uh there is something that was on the
agenda that's I have not talked about.
That is uh
called centralized setup data.
So, some of you might have uh the
necess- necessity to create a master
data of some type.
Posting setup, GL account, customer.
Do you ever need to do that?
Yeah, yeah, yeah.
And copy to 800 companies.
Exactly.
So,
a simple way
could be to use
a solution that's in there which well, a
proof of concept as well.
We can use something called a data
package setup.
And let's say for example, we are
we want to use the customer table and
for every
insert or modify or
rename of that customer table,
we would like to push that change
somewhere.
And but where would we put that change?
We of course we need some kind of a
destination.
So, let's
let's find a data package destination.
And let's create one.
This is
company one.
And
company two.
And
the only thing we need to do actually is
to link
that to a
import setup.
So, let's see that I want this company
to be or the data for this company to be
created in this
in my server and that one I want on my
Dropbox.
And let's
unblock that one. So, now they
destination should be set up and ready.
The job queue that's that will handle
this in the background is not
operational.
But let's
still try and uh
prove that this works.
So, we have a way to go into the
customer
through sales into a customer. Let's
find a customer and
do some changes to that one.
And
we should now have
a document in our system
describing the change that we did.
So, if we look at the code that it was
actually executed,
there is a
code unit in the platform that's called
global triggers.
And that global triggers will fire and
ask,
"Do we need to do something whenever we
update a record in the database?"
And by using that one and specifying
that I want to do something when I
insert, modify, delete, or rename a
record,
these events will be executed
accordingly.
So, I will have something called a data
package because I modified the customer.
I called that create data package
function,
which is down here.
And if we see there's if you look at the
results, let's look at the data
packages.
This kind of surprised me first. I just
didn't want change, but it's still four
packages
because we got the modify
trigger executed four times.
And we can
Of course, this uh the the layout that
we see
for this XML file, which is describing
the change,
of course, this is something that you
could create your own and decide if that
is
what fits you. This is the layout I
structured and decided that this would
be enough to describe that this is a
modification for a customer and I pass
all the selected values with an XML
file.
And since we have hooked up the
destination to our drive, that means
that the this XML file will be delivered
to that destination.
And
if you look at company 102, they just
import these files and apply them with
the same rules.
If we need this to happen instantly, we
could use or or look into that
that Azure functionality that Dimitri
and Trangala actually demoing right now
in another session.
But you could look at that video
probably later.
So that's the thing that I wanted to
talk to you about.
We have
15 minutes or so for
for questions, suggestions,
or whatever and I have a catch box for
you.
Someone have Someone have any question?
Let's try it.
There we go.
Hello.
Yeah. Um in regards to the job queues,
is there a
good if even at all is it possible way
to prioritize different job queues or
different job queue entries? If for
example, you have 50 jobs and you insert
another one that is much more important.
Or is it just sequentially?
No, in in the in the current release,
there is not.
You just need to make sure you have
enough background sessions available to
execute your job queue. The priority
field that was in the table, it has been
obsolete. It's not used anymore. So the
default job queue does not have that
option.
Okay, thank you.
So I have t-shirts.
Oh, almost there.
Using data exchange framework in
combination with XML files.
Yeah.
You also mentioned CSV files. Can it
also import other file types than that?
It can
So that the the code unit that's you put
in as the reader code unit
Mhm.
You put that code unit
depending on the file type that you
have.
There is a reader code unit for flat
files, for variable files, for XML
files, for JSON files, and you can
create your own
reader. I for example created a reader
that reads Excel files.
Okay. And you have not had any situation
that you could not map
into the data exchange framework yet?
No, I have, but I have needed to extend
the data exchange framework a little
bit.
But I have I've done that to be able to
handle all the different file types that
I have needed to use. So yeah, I have
been able to push things to there in
every case.
Thank you.
Um
Which cases would you prefer to use the
XML port instead of the data exchange
framework?
You mean which cases would I skip the
data exchange framework?
Yeah.
Okay. So
If I might skip the data exchange
framework in order to get the data
directly into incoming documents.
And then from the incoming documents I
would always use the data exchange
framework from there on.
In my example here, I'm actually using
the data exchange framework first to
create the incoming document, and then
again treat the data from the incoming
document.
So that example that Arjan has where he
receives
an an PDF attachments for that invoice
at contoso.com email and puts that
directly into the incoming document,
that's perfectly valid as well.
Okay. So.
But it's I I like to have the
possibility to push it through incoming
documents because it could be a
different type of document that I want
to be able to handle.
Okay.
All right.
Do we have more questions?
Over this side.
Um
All your for your examples and the
framework, is it already on cloud ready
or is the dependency on premises?
Because of example, the file management
has dropped some functions due to
to the problem.
The
This framework has the server file
system
in there as well. If you cut that out,
the rest should be SAS ready.
Okay.
So.
Azure the Azure blob, the Dropbox part,
the Azure files, that will all work up
in SAS.
It's using It's using functions already
in the base app for the authentication
part.
Sorry.
So.
Yeah, it's SAS ready.
So, what is your experience with rapidly
executing tasks where you basically
export files to one of these file
systems?
How many files can they take for
example? What what what's your
experience at what point would you
recommend looking for a different
solution?
So So what I do normally is if I have
like in my example, I had a folder
called Tunaf in my Dropbox.
Uh what I do when I import the file, I
always remove it from that
directory. I can archive it to somewhere
else.
Uh
I in that setup data service example I
had, I exported all the customers
to a file service.
I think that took about a minute.
So it's It is pretty fast. Azure blob is
fast.
Thank you very much.
There was someone over there?
To the left.
Thank you.
Uh data package question.
Uh I just want to ask if you have some
experience with
uh creation, for example, you said the
customers creation of documents for the
changes on the customers.
In that case that you are changing a lot
of records,
I mean I mean for example
the thousands records.
From the perspective performance and
looking of the tables.
I don't think I've tried it with that
many tables, but uh from my point of
view, if if if if the uh change doesn't
need to be instant,
Mhm.
then the the job queue will finish this
Mhm.
in uh just a few minutes.
It is uh
It hasn't been any issue with that from
my point of view.
The thing that I also do with this uh
when you serialize data to an XML,
Mhm.
you can actually be using that yourself
to move data manually from one setup to
another.
You could actually pack up the whole
setup data tables into one XML and just
import it on the other side.
That's what uh we have been doing for
several years now with with Advaniya.
Okay, thank you.
Is there one up there?
It's done. Okay.
That is it then. Thank you everyone
everyone for attending and and
have a nice conference.
