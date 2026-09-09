# Microsoft Presents: What is new in the Runtime

- **Source:** https://www.youtube.com/watch?v=dcxqC7T9des
- **Video ID:** dcxqC7T9des
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 44m52s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Ladies and gentlemen, please welcome
Jesper and Torben for what is new in the
runtime.
Yes, my name is Jesper Hellesø.  I work in
the so runime team together with Torben
and I mostly work on things database
related both querying and schema changes
and other runtime related things.
Yes my name is Torben Vind Mehof uh
started Microsoft 2005 so been doing
servers for 20 years.
We have some interesting things for you
guys today.  So beyond what you are going to
tell you, we are telling you the
things that you are seeing as visible
stuff.  I just thought we wanted to add
this slide to the screen.  So we are
actually the one behind the AL execution
the one time the database.
So we are part of when everyone else
calls the world class service and all
that kind of things.  We are the one
in the middle.  We are the one that
executes, taking care of your memory.
So beyond the features that you guys
see, we have a lot of other features
that we don't show today because they
are the internals of the machines that
but but this is the things that are
available for you guys and take it away
the first part.  Yes.  So we're going to talk
about a different some different topics.
It's gna be both what we released in the
most recent release but also the one
before it because it's been a year since
we were here last.  Øhm gna talk about a
runtime which is functionality exposed
to the AL language database search web
service tag and finally reporting.
Um, let's start out with the AL run
runtime.  So this is the
functionality exposed to the AL language
by the server but not the language
itself.  One of the first new things, the
first new thing is the new number
format.  So we probably know the existing
number formats.  They have been the same
since the seaside days.  Internally those
get translated into DNET format strings.
So we thought why not just expose the
DNET format strings directly.  So if you
use this format string here, you can put
in exactly what you would put into net
format and you would get that
in the UI.  Um today it only works for
tables, pages and reports but we're
planning to expose functionality to
format as well so you can use it as
well.  But for now it's only when you're
using pages, reports and tables.
This is more example if you want to
do special formatting for zero or
negative values.  That's very convenient.
Get URL supports the layout parameter,
meaning you can if you want to open a
page directly into analysis mode or some
other specific mode, then you can use
this parameter can also build the URL
but it's more convenient this way.  So if
you want to take the user directly to
the analysis view on a specific page,
you can do it that way.
Calculate only visible flow fields.
That's a I think seems like a very
requested feature.  So previously any
field even the field visibility was set
explicitly to false we would always
calculate it.  Now we have made a feature
key that you can opt into for now to get
the only calculate the fields that are
visible.  There are some fields that can
change dynamically back and forth
between visible and invisible after the page
has been opened still have to be
calculated.  But at least the ones that
are never shown, you don't have to pay
for the calculations anymore.  So that's
worth going and enabling it.  But be
aware if you have code that relies on
invisible fields being calculated, you
might need to adjust your code.
Set autocar fields.  So the record ref
actually just contains a record inside
but for historical reasons it has not
always followed the API of the record.
Now we have brought them more in line.
So you can now see autocalc fields on
records as well.
[Music]
So that you can get auto calculated
fields on records as well.  If you want
to write performance code using record
references that's the right way to do
it.
We have added session information.  Call
stack.  So I don't know if you knew but
the previous version was that you
threw an exception and you caught it
again and then you read the call stack
because that was the only way to get the
AL C stack before if you didn't have an
error.  So that's of course very
efficient to throw errors just to catch
them right after and then get the call
stack.  So we have now added a way to
just get the call stack.  No errors
involved.  You can just read it.  But it
still takes some resources.  So if you
plan to log it to telemetry then of
course get the call stack log it to
telemetry or show it in an error message
or show it to the user but if you're
just getting it and then deciding later
if you actually need it then
query for the cost deck if you need it
don't just get it always because it it
has some it has some costs
easy onopen company analysis so we added
more columns to the unopen company
telemetry so you can easier
troubleshoot like if you have a session
open company tag  correlate other
telemetry with that
in your telemetry analysis
and then we did some improvements to the
HTTP client before you could you have
always been able to send patch requests
but it was just the sent and then you
had to explicitly see the method.  Now
there's a dedicated patch method uh
meaning the better better readability of
your code and nicer to work with.  We
have also improved a lot of the error
messages on timeouts and other things so
that you can actually see what went
wrong.  Not just that it's a failure but
that what it exactly was that went
wrong with the HP client.
Um, we have added tool tips on queries
which is especially important now that
like queries are more used with
analysis view.  So then you can add these
tool tips to the query columns and they
can show up in the analysis view.  It also
means that if you have a query field
that query column that is bound directly
to a table field then we can inherit the
tool tips all the way from the table to
the to the query and then finally to the
UI in the analysis view
and then
list of of smaller changes we have added
the public IP address for you so you can
set it on the server meaning that if if
the server cannot figure out its own
public IP address itself then you can
set it up in the configuration file so
that the anything that needs to  expose
in make use of the public IP address can
create from the server settings.  We have
also added more to preview integration
meaning
you can get more detailed locks around
security related events such as user
changes or permission changes other
things that are important to look for
for security or compliance reasons.  So
we have added more to the list of
preview
events.  We have updated
companion table verification.  This is
like every time you install an extension
if it takes a long time.  It's it can of
course be your upgrade code but it can
also be some verification we need to do
to all your table extensions that exist
in your extension.  So this should now be
faster could still be better but it's
better now than it was at least.  And
then finally we have opened up for
moving fields and extensions.  This is
not a new feature but it was previously
not enabled in the cloud.  It was only
available on premise and for us but for
now we have now we have opened it up.  So
you can use the move fields
functionality to refactor your
extensions.  Move fields between
extensions ehm which I think is is
useful.  Um, I think we don't mention it
here, but we also added
for now on premise only, but the
capability to
obsolete fields and then later remove
them without requiring forcing.  So far
it's on premise only but you can uh yes,
but what are we then working on right
now in the AL run time for the next
release?  Ohm, a big topic right now is
that Torban mentioned is that we also
work on the behind the scene stuff that
is not directly g to be a new function
for you or a new API, but memory
improvements in situations where you
have a heavily customized system with
many extensions and maybe even many
tenants on the same box with the same
with many different extension applied on
top of the base app for example is
something we are looking at because then
you quickly get into this situation
where have many copies of metadata lying
around and this  is an area where we are
trying to improve things so that we only
keep the bare minimum metadata around so
you can like spend more memory on data
caches instead of metadata because
that's what makes the product faster for
you instead of we have to carry around
seven copies of the the metadata
then the data stack um
here what one of the changes we did
recently was the improvement of copy
company with large amounts of media so
we know that today if you copy a company
that has a larger amount of media, you
need to copy  all the media and then you
update all  the references because you
don't want to start editing the media in
company A and then company B's media
disappears or gets changed.  So that's
why when you copy company with lots of
media, we need to copy all the media,
update all the references and make sure
that that changes in company A don't
affect company B but in the most
efficient ways possible.  So it's faster
now when you have a lot of media, but
it's still not something you should do
in the middle of the working day if
you want to be nice to your users.
And the maybe not so popular feature is
the enforcement of the maximum number of
companies.  Um, so in the beginning we did
n't have an enforced limit.  We have
had a limit for a long time but that was
not enforced.  But now we are actually
enforcing that if you have 300 companies
you cannot create new companies in SAS.
And the reason is simply that uh
upgrade starts taking too long when
you have that many companies.  That's one
reason but another reason is that it
turns out to a lot of tables and sequel,
a lot of metadata and sequel.  So similar
to that that we need to spend a lot of
memory on our metadata.  Sequel also
needs to spend a lot of storage and
memory on their metadata.  So you're
spending memory on metadata
instead of the data you want to query.
So that's why it's good to stay below a
reasonable amount of companies.
Then we have added better insights into
database
missing indexes.  So the page has always
been there but maybe not so useful
because it would only say this index is
missing but it would not say how much
will it then help if I added and sequel
actually has the information so there
was no reason not to add it.  So what we
added is that now you can see how often
would that index then be used how much
would actually improve performance and
the combination of those two values ​​give
you an idea of ​​like then how how worthwi
is that index if if you multiply those
two values ​​so if you go into the UI you
can see here the the five new columns at
the end the first two says something
about how often is it used both for
scanning and seeking
the
uh Uh yes and the next two they say
something about what is the cost of the
query that would be improved by the
index and then how much improved would
it be and the final column is just a
combination of the first four columns
say something about like if it's if if
it's that frequent and that good of an
approval then the total benefit will
be this.  So it's an estimation but it's it
's useful root of th like okay this
index sounds like a good idea I'll add
that one.  Um then we add another
feature for unpremise.  As your sequel
this works out of the box but for
unpremise if you're running your own
high availability setup with sequel
server then it's a good idea to set this
setting to true because if you have a
fail over like the first sequel server
stops working and you want to switch to
the second one if you don't enable this
setting it can take a while before
sequel gives up on the first sequel
server it will try again and see maybe
itl come online again instead of quickly
switching to the new  replica.  So if you
enable this setting it will always every
time it needs to connect it will try to
connect to all sequel servers at the
same time and then the one that is first
to reply will get the the one that is
still alive will reply immediately
instead of having to try first the first
one then the second one then the third
one so this is this is for the unprem
guys that use high availability um
um then we are tr state locking is not
new um but the the state of things have
changed
en for everybody  and can no long back to
the old system small recap of rate
locking the previous solution was that
as soon as you did changes to a table
you would start running all your queries
with update lock on that table this is
how it used to work and has been working
for many years.  But with rate locking
included, you will instead just start
reading committed data.  So read all
queries will become read committed after
the first change to the table.  If you
then want to explicitly go to update log
on a table, you can either use read
isolation or you can call lock table.
that will still lock table works the
same but it's this implicit in the
middle locking stage where we previously
went to update lock where we will now
only go to
to recommitted so that should that means
that you only do keep a lock while
you're reading the data not while you it
doesn't persist for the duration of the
transaction
select latest version
this function has actually been the
product
forever I know uh it tells the the
server to say that the cashes that we
have that you have already populated
with  values ​​they are
they have a time stamp say this was
added to the cash five minutes ago or
this was added to the cash yesterday if
you call select latest version we don't
throw away the cashes we just say
anything that was cashed before this
date
don't don't use it stays in the cash but
you don't use it for your session
parameters
doing all
to this specific table I'm about to now
is the one I want to have the latest
version of now you can actually say for
this table I want the latest  version
small note is that we actually had this
in on  when you signed into the product
we call select ver latest version
without the parameter in the beginning
meaning every time you sign into the
product we said everything from before I
signed in I don't care about it.  We can
now do the right thing and just say this
specific table related to the login
process.  Don't disregard the cash for
that one.
Yes.  Then a new functionality for the
query objects.  Query objects already
have the save as CSV and save as XML
functionality.
Meaning you can directly stream your
data to CSV and XML.  But what is new now
is that you can stream it to Jason.  Um,
and the good part about using these
streaming operators is that you don't
build everything up into memory before
you have to put it into a stream.  You
don't have to pay for all the single
object J tokens and Js
individually before writing to the
stream.  You can make CSARP efficiently
stream it directly to to the disc or to
øhm HTP request or wherever you need to to
stream it to.  ehm meaning you use less
memory and it's simply more efficient.
There are some more details on how exactly
we do this in the in this slide.
But it's it's in general a good idea to
use this when you have a query to get
your data and you know that it's gna be
a lot of data.
So what are we then working on um
um right now?  One thing we're working on
I put it in I already mentioned that you
can now disregard calculating
flow fields for properties that are
invisible.  Another thing we are working
on that is actually going out in 27 is
that we will combine flow fields that
are using the same tables as source.  So
if you have can imagine credit debit
fields on the on ledger entries those
have exactly the same fields.  You just
one of them is summing the credit fields
one of them is summing the debit fields.
You can do that in the same query
whereas today we are doing one
subquery for the credit field, one
subcredit for the debit field, one for
the credit LCUI, one for the debit LCY.
So that's we're going to merge all of those
so it will cut down the size of
queries and the amount of data to go
through multiple times.
Then I mentioned we will talk about
search.  So what we already introduced is
the text search.  You have already seen
is from the client you will see this as the
as the modern search and you will
also see it in in lookup experience.  Ohm
it it is also used by the search and
company data.  is used directly by all you
can add it to your extensions.  What it
uses underneath is that it uses the
sequel full text search in feature.
So once you optimize a text field for
text search in your extension
we will underneath add a full text index
meaning that quies that would always be
forced to do a full table scan over all
your all your items or customers vendors
they now can use the fulltex index
instead
hm there's some things to be aware of
with this if if you very if if if you
very used to being able to search for
something anywhere in a string like in
this case we have the chair the green
chair of course chair and green and gre
chair  they work fine but the moment you
start with substrings or ends with
queries that does not work with
that does not work with fulltex search
so if you know you're gna search for
something that is at the end of a string
then
uh then you need to either switch back
to the legacy search or you can add your
wildcards yourself if you use modern
search
switch back and forth yourself adds
to your queries and then we will do the
most optimal thing
the moment you do that of course if we
have to  regress to the nonf text based
in search then  the performance will of
course be similar to what it was before
full text indexing but that gives you
the option to
If you need to do this in your app, so
we have added this to a lumber of our
tables, the big master data tables, for
example, items, customers, vendors.  If
you need to have if you have fields for
your own extension where you need this,
you can go in your table extensions
and optimize your own fields for this.
If if you have added them to the items
page for example, it makes sense to also
optimize the text fields that you want
to show on the item list to this so that
they also get in get searched in when
you're using modern search.  Um.   Yes
.
Um, you can also use this from AL.  So that
's what search and company data
does.  It's a new filter syntax where you
add it it might look a bit strange but
you add these double ampents to the
beginning of the filter
special full text wild card and then the
search will use full text index.  If we
detect that there's no optimized for
text search on the field you use
here we will just revert to the old old
way of searching.  So it's not like you
have to know that up front you can use
this syntax and then we do the right
thing.  If you know that it's there, but
maybe not in all versions of the app
you're depending on, then you can do it
this way.
What are we then working on in the next
version for search?  We are currently
working on semantic search for metadata.
Say like if you have a a specific report
you want to search but you know what
it's about but you don't know the exact
terms that are used in the in the title
or in the in the about text of the you
can use semantic metadata search that
will compute the meaning of what you're
searching and the meaning of the report
you have like what what is the report
really about and what is the query what
is it that you really want and it will
try to find reports that are similar and
meaning not necessarily in the exact
terms.
exp forilot chat experience for explorer
and tell me search where might be used
to know exactly what the report called
you can now search I want to do
something about some term and then even
if it's not written specifically in the
report title it will still show up
because the embedding models will figure
out that these terms are similar enough
that it's probably this you meant so we are
looking very much forward to to shipping
Yes.  Right.  Thank you.
On to the API stack.
Every day at Microsoft, we care about
security.  So we change things all the
time.  We have an initiative called SFI
running.
Sound okay Yes for h glims.
So every day we make security more
strict.  try to remove places where there
could be injections and similar kind of
things.  And this time it was on the HTTP
client calls where we will not accept uh
SSL certificates that is not valid
anymore.
You can in 27 26 you can up down on the
feature management page and get access
to using it or you can at the instance
level on a specific call even in 27 do
that also but we are going to turn off
API calls to the outside that is having
failing certificates
it's no it's something from the past
everyone on prem ran a lot of local host
services and other kind of things.  We
would like everyone to encourage to run
on secure stuff.
And if you guys in here, how many of
you guys are running telemetry?
Perfect.  All the others that didn't raise
their hands should go back and start using
telemetry because telemetry is
inside the server.  It is our primary
way to actually debug the issues.  So if
we get a ticket from you guys and it
comes into us, the first thing we do
is to do it into telemetry and look what
goes on, what are the exceptions and you
guys you know can turn on telemetry in
the admin center and get access to these
kind of things.  So do you actually have
APIs that are having these violations a
certificate that might be broken you
don't know of it but it will fail
somewhere in the future.  We are putting
these kind of things to telemetry.  So go
in and you will actually get these kind
of notifications from us telling you
guys that you have something to do
because you know in 27 it will be even
more strict and in 26 right now it will
actually fail as well.  So you have to go
into the feature management page at upd
soap.  Soap was one of the best features
back in the days.  I remember when we did
the big conversion from forms to two
pages and suddenly we made APIs for
every page any page you could just
enable by going to the web service page.
But the coolest part was because we did
n't have any APIs back then.  So this was
the APIs of the product and enabled you
to get started on almost anything.
But in the new world where we run
apps and we are upgrading you guys all
the time at least once a month if we can
get away with it unless you stopped us
that means that we would like not to
break you guys too often.  And if you
bind your APIs towards our screens it's
not a real public API and that means
that someone might break for you if we move
you to the newest version and we moved
controls around giving them new names and
these kind of things.  So we want you
guys not to use our pages as soap
endpoints.  So uh
we also put that to the feature
management page to enable and disable
it.  But later on it will be blocked.  You
can still use the OD data ones because
we want you to know to do this in some
transitional steps.  OD is also more
tolerant of fields.  You can ask for
fields.  You can select fields and other
kinds of things that were not present back
in the soap days.  But you can see this
on the web service page.  If it's turned
on, you don't get any soap UOLs on any
Microsoft page.  Your own pages that you
have added extensions will still get so
because it's up to you guys to turn them
on and off and decide if that was meant
to be an API page.  But you know change
your objects to API pages and use data
for the future.  Um,
and if
yes, if you see the blue band in the top,
then you can turn on and off and get
access to the feature management page.
And then if you turn it on, you'll see
soap again.
Similar to the first one also telemetry
is emitted.  If you do use any of our uh
pages, you also get that kind of
notification in your telemetry as well.
So I encourage everyone to turn on.
It's like bicycling with something next
to your eyes not running telemetry on
the service.
All right, over to reporting.  We did
quite a few changes on reporting.  A lot
of the things that is happening right
now is
electronic documents and we move from
just being a PDF file to have embedded
XML specific kind of funds passwords
added people need to get things into the
PDF after the rendering
so we added the PDF push processing
which is enabling us to do some of these
features I know specifically Germany is
hot topic on on getting
voicing added to all PDFs but happening
all over the place I think us is also
having a lot of new requirements for it
so this is enable  you to to touch the
PDF before it
to to set the set up set the state up
when when we do the rendering
all the way back to RDL and section
reports even back in seaside days all
the UI had like the USID in the corner
it had the company name, the data of the
rendering of the report, a lot of
standard stuff, you know, things that we
have on every report.
So when we are modernizing all the word
layouts now, we want to make sure that
the new data sets for the future are
actually slimmer because we don't need
that on the road level things that are,
you know, actually more than less
static.  So what we have done is we have
added two new data sets to the XML
reports sorry to the XML mapping in the
in the word reports where you have you
know the report ID the report name the
things that is you know the current
company they don't change.  So use the
new properties instead of the one from
the data set and remove them if you're
going away from RDL for your reports in
the future.
Excel um how many of you guys are using
Excel reports?
That's a lot of good things also to
catch up on there.  Also Excel gives you
a lot of new cool features.  You know,
instead of having the square data sets,
as we used to know from the RDLC side,
you can do, you know, like multiet so
get each of your tables out in the sheets
in in Excel.  And then it's much easier
to manipulate your data because you know
how many people today need PDFs over
actually just getting access to data.
Excel is, you know, a vital part of the
future on that one.  And the cool part is
that even though the provider of
the original report decided that it was
not a multisheet report.  Now you can in
an added layout actually go in and say
for this particular layout I would like
it to uh to be tab based.  So you don't
have to you know filter if you do pivots
and and other kind of lookups then you
get direct access to
the individual sheets instead of
having them joined.
Yes, something for the AL side we
allow you now to two tag layouts
in VS code so the obsolete taget state
obsolete reason.
So they will be present on the report
layouts page.  So you can tell customers
you know not to use this layout anymore.  I
would like the other one.  You might need
it for legacy reasons for a period for
upsolution and so on.  So
and similar report layout page also
shows deprecated and last modified by
and last modified so we can get
information on the page when the last
was changed.
other new features validate layout
especially about fund validation
a lot of funds is coming in right now
there a bit more on funds afterwards
also but you can you will validate that
the usages of funds is actually okay
with the machine that you are present on
right now if you make a new report you
need the xml injection you saw the two
new data sets before and then you need
the data set of the report itself you
can get the snipp it out if you want to
hand patch your uh new document you got
from somewhere and  now you need to embed
the developing part of adding a word
layout
and simpler if you can just get an empty
document also with all the XML added
directly into it and of course update
the existing data sets inside a document
so new new actions new helpers to make
it easier achievable to be successful
making word reports
and again telemetry uh Uh,
it's like change tracking you know
someone changed your layout your invoice
is now different weit now to telem when
the changes happened.  So of course the
last modified buy is there but you know
who did that before the last modified
buy telemetry is your choice.  you know
most often you know it's not a violent
user or someone that did something bad
but just helping someone telling them
that they did a mistake or they did
something you know and then help get get
your documents back layouts back if
someone changed it in in error
with the new electronic documents
sometimes you know when it's a PDF it
needs to be named something if it's a
special PDF based on data then you need
a different kind of name coming out
system instead of just you know
predicting names for you
en the ability  to attach to an event and
then you can manipulate the name of the
incoming document before sent to the file
handler.
It's useful in many places especially if
you need to have it to be a form number
for some government thing
other kind of scenarios you can
manipulate the name of printed reports.
Yes, we code small thing but
we added snippet helpers do you know the
snippet helpers when you're sitting at
coding I guess you do you know it's a
daily improver of how to you know get
your structures up in in the old days
you had a designer that helped you do
your structure but today we are copassed
and there's a lot of helpers at it and
this time it was the credent report
objects getting data link item helper
a few obsolutions
extensions methods more
used and now  the one you have to use
layout from inside your extension apps
now are depreciated not the one we are
going to use for the future market
pending and will disappear next time
new funds the world is changing all the
time and especially you know uh
we we are hosting your code now on the
services by running in the cloud.  That
means that you can't add funds.  So we
are listening to you know add specific
funds that make legal things.  Like in
the US uh
we have these address printing funds
added so people can do the correct
envelopes when they still do paperwork.
The US is doing more paperwork than Europe
in many cases, at least from what I know.
But we added
funds for that.  Actually one thing I
missed on this slide.  How many of you
guys have known the old good old word
alignment bug where you import export a
word layout and then suddenly it's left
aligned instead of right aligned
many people.  Well that one is gone now.
We finally have that fixed.  It took a few
years but it's
fixed now.  Yes.
But you know these special funds, you
know we can add more funds.  You know
oftentimes it's a matter of licenses and
other kinds of things.  If they are
specific and the general usage you know
then you know talk to us and then we
probably could get more of them in.  We
added aptos which is the office's new fund.
We don't use aptos in the product.  We do
n't use it in our reports but if you
make a new template from Word then most
probably it's on Aptos if it's coming
from Microsoft at least.  So we added
support for rendering of apps.  If we
changed it on our report it would be
because we would change it everywhere.
The product has you know a UX experience
and that's not based on Avat
Excel layouts also there a lot of with
all these new tabs and all these new
constructs it makes it also complicated
sometimes to know the right your right
lookups.  We added a lot of new macros.
So go to next time you make a new or
make an Excel layout.  Go look at the
macros that are inside
the report which is making many of your
lookups much much easier than there was
in the first version of Excel reports.
Yes.  New word ad in.  If you already have
one, go to the app store and get yours
updated.  There are new capabilities in it
and especially
the second one on the list.  I think is the
most important one the conditional
visibility
I think one of the limitations from the
beginning on word layouts was that it
was harder to do discount visibility in
in your tables doing other structural
behavioral patterns eh because that was
easy in RDLC because that was just a
matter of sitting a property on the
visibility expression eh but that's now
available with the new ad and you can
also add comments you know something
that is complicated in your report
render add
new
addin.
Alright when we started word reports
back in the days, we needed to support
multidocument rendering.  It's been a
behavior from good old seaside days
where you could go in and say these 10
invoices come in one spool to the
printer.  later on it was also for PDFs
but it meant that you always ended up
having one document in one transaction
and coming out of it.  So when we came to
work layout we need to figure out how
can we support that kind of thing and we
used the the sections to say this is the
split and the section we will split and
then we will you know do the rendering
on that one.  It had some consequence
that you couldn't use the section
features of course but with the new word
merge data item we don't care about
sections anymore.  So now you can
actually do your own section stuff.
Let's say you want to make a contract
where there's a page one to two and then
a section where there is another page
one to three.  You know one is you know
the going for the customer the one is
going for some archive and things like
that.  So we are free to use the word
features now
compared to in the past.
Yes more is coming on reporting also we
have the preprocessing.  We also found
out that the post processing would be
nice too.  that is coming in the coming
release and there even more things
coming on the word in data picker is
probably one of them you know these are
things not released so everything can
you know
I can't promise everything but that's
work going on on it to make everything
easier and don't forget all the
documentation added
go to I think
maybe forgot to get into this
presentation go to I think it's called
BC report CS
go to the learning website.  It just
got updated.  A lot of good information
coming from our PM Kenny that has spent
a lot of time on rewriting it.  Never over two
questions.  Just see what we in real
time we have six minutes.
Thank you.  for the word layout plugin is
it possible that you can we send an HTML
blob to the word layout and then it's
rendering and how we manage the page
break in future if we have some pictures
and we want to have nice document may
long tex
pictures HTML and page
What is the idea what coming
on the page
similar like on the printed document
pictures is already there like the
company logo and these things in a long
tax if you have an item and we putting
some long maybe an HL HTML blob and we
give it to the inlc we  can rendering it
but we also have the problem with the
page break so
let's catch up that one afterwards So I
think I need to get your complete
details on the scenario change
alri
[Laughter]
the auto format expressions will they
also become available for date time?
I heard that suggestion before.
They go through the same code pass.  So I
think we should should do it.  We haven't
started on it yet but I'll take the
suggestion with me.  You can use them
only
integer and kind useless.  Yes.
One there.  We have two only the two
first questions.  You don't want one.  Yes.
Now you have one th you can get one
my question is on filtering when we
filter on list pages for example ch
ofcoun i want to filter a range so at
present when i ch the first part of the
range and putد doudا after when i ch the
secondकप of the range it will be repeated
actally with the first
so how can i have you know comp to
filter
M so from the like on the advanced
filtering pain on the left side or yes
in the ch of accounts page I want to
filter a range of ch  ofcouns so I put
first part in my range and when I put
dou and when I select the second part it
replaces the first part okay that sounds
that sounds like a book maybe but it
sounds like it's something in the in the
front end but I can take the question
I'll need to take the question with me
see if I can put it in the Q&A
afterwards
for the session.  I can't answer right
now.  Thank you.
I was at some red carpet event a few
years back and it was promised that
there would be a system field on the
table that set company.  would be all
these company tables but I can see you
are already limiting this 300 companies
for the same reason I guess it's not
happening that has never been a promise.
That was part of
us trying to shard the database at a
certain point in time also but that was
it's never been a promise.  Okay.  It
sounded like that.
ten had
complicated so we actually did not we
have most of the code inside the server
still to do it we could do it for maybe
the small tables like the setup tables
and other ones but but it has some
complexity consequences but we never
promised I know for sure that that one
would be released do
[Laughter]
You can't sleep in these sessions if
these microphones are getting thrown
around.  Hello.  So what about
using QR codes and barcodes in word
layout like we need specific funds for
that right?
I think we have some of the back funds
already but
I don't know the exhaustive list that
will be in the documentation but I think
if you fail on getting it as a fund I
would create it as a bitmap on the
server and then send it up as a bitmap
we tried something like that but more
specifically like in the end that the
documentation that we needed some funds
imported Pram of course.  Yes.   Yes
.  Wed.  On pr you can do whatever you
would like.  Yes.  It's more it's more for
us because we need to legally have a
license for every server in the world if
we're doing it.  It's part for us is part of
the control plane to get funds out and
the templates.  Okay.  Thank you.
Never.  Any other questions?
Isn't that better?
Got a question about job queue the user
that is starting the job queue could you
make it the admin user
so the only admin that could start your
job queue so for example if you're a
consultant and you are starting a job
queue
for a client you want your name your
username to be visible in the job
should be the admin user starting job yes
the problem
Job job que behind the scenes of a job
queue is the task scheduler you know and
if an admin can impersonate me you know
then I can also you know do things as me
so a task  can ever only be scheduled by
the one that owns the context we don't
make sessions for anyone we make a task
that will make sure that you you're the
one as the one creating the task we can
pause it and then admin can start it so
so that is actually security feature
behind the scenes of how tas works.  You
can't just impersonate any user that
you know is a big security risk.  So it is
actually the one that hit the button is
the only one that can be executed as
Yes.
Never.  Any other questions?  I think we
are low on time also now.  Yes.  Let's do
the shift.
FKS
thanks a
[Applause]
