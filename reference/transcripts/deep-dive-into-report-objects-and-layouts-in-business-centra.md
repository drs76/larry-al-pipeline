# Deep Dive into Report Objects and Layouts in Business Central

- **Source:** https://www.youtube.com/watch?v=FZkAnXlLPog
- **Video ID:** FZkAnXlLPog
- **Channel:** mibuso.com
- **Published:** 2025-10-02
- **Duration:** 97m39s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

All right, welcome everyone to this uh
session deep dive into report objects
and layouts for business central. My
name is uh Steven. I work for a company
in Belgium called Platan, part of
Companion uh where uh we do uh training
around business central. We have
learning journeys also around a few
other uh subjects.
I'm available on uh social uh media blue
sky uh LinkedIn uh if you would like to
contact me or ask some questions after
the uh session. All right.
Today I'm going to talk about report
objects and um all the ins and outs and
how to prepare to create great uh uh
reports and I'm going to do that in a
number of different uh subjects or
topics. going to start to talk about
analytics in uh organizations or the
analytical needs, how to prepare, how to
think about uh getting started to create
reports. Then we'll dive into a number
of different uh subjects. We'll start
with the data analysis uh one of the
let's say more later additions regarding
reporting in business central and how we
can use that what is also coming in in
the future.
Uh besides that of course we are going
to dive into report uh objects. First
we're going to have a look at creating
the data sets and preparing the data
model. Any kind of report you would like
to create. Is it a business central
report a PowerBI report data modeling is
the most important thing. If you get
that right then the layout should be
easier to uh to create. And we'll also
of course dive into the different
layouts with advantages disadvantages.
Um, I've also included a few topics on
uh PowerBI because we cannot leave that
out when you're thinking about reporting
needs in an organization and we'll also
see uh why that is the case. And last
but not least, a few best practices
takeaways have also uh foresee.
All right, let's dive into it. Before
you open any kind of development tool or
create reports, you need to consider the
analytical needs in organizations based
on uh for example personas or who
requires a report. And I'm really
thankful that Kenny from Microsoft also
included this diagram in the official
documentation because it can really help
and guide you in preparing uh um the
data model of the report the layout
choosing uh what you will need. So the
model is based on who in an organization
you are building the report uh for. On
the one hand we see aggregation or data
aggregation which has to do with how
detailed the data needs to be. Then on
the other hand the hierarchy within the
organization or the person for whom
you're developing the reports. You could
say that the higher in the hierarchy,
the more the data needs to be aggregated
and the lower in the hierarchy or more
operational uh persons need more details
and depending on that you're going to
try to figure out what might be the best
solution or the best uh reports and
remember data aggregation. one of the
most important concepts when you're
going to develop uh reports.
I have the same kind of diagram here. Uh
and then by the level of aggregation I
have also plotted the solutions that
that we have within report objects
within PowerBI uh within other uh tools.
All right. Now, aggregating data means
providing totals subtotals. So it's
never a really really really good idea
to send all of the little details all of
the ledger entries into a report or a
report layout even though users
typically u request these things for
performance for manageability uh for
scaling it's never a good idea. So you
need to aggregate uh data. Aggregating
data means grouping it, creating totals,
subtotals so that the data model of your
report is exactly what's required in the
layout. Performance- wise, that's also
always a good idea. This means you also
need to understand where the data comes
from and to be able to provide these uh
insights. Now, data aggregation is a
concept. Data granularity is also an
important concept. So aggregation is a
process of combining multiple pieces of
information.
Summarizing it with a certain level of
of detail and granularity is kind of an
indicator of that level of of detail. If
you are going to aggregate the data, the
more you're going to aggregate the data,
the less detail and that you're going to
provide. So the smaller the granularity
will uh will be. one of these concepts
that uh comes out of the BI uh world
that I also used quite a lot when
creating PowerBI reports. But if you
think about it uh for normal report
objects, any kind of data set or
semantic model, it's important to think
about what is the exact level of
granularity in which I need to offer the
information in a report keeping in mind
scalability and of course also app
performance.
All right.
When you ever you asked to create a
report, you need to ask a few questions
to get the scope uh right and to also
help you determine uh which type of
layout uh might be best suited for this
certain uh request. And to give you a
small example, when I was a junior um I
came into Dina Vision world and I was
kind of a reporting and not really
expert but had some experience in that.
One of the first reports I was asked to
create for a customer was Stephen H can
you visualize uh the uh availability
that we have about our items uh in
different uh locations
told to the customer of course no
problem took me a few hours to create
that uh report presented it and the
feedback was well it looks really nice
but it's absolutely not what we need
what what we wanted. actually expected
something else. Then I started asking a
few questions. Okay, what do you expect?
Then basically inventory was supposed to
be availability.
I didn't really know how to calculate
availability. The locations were not the
warehouse locations but basically the
customer sites uh where the inventory
was also sometimes stored. So to avoid
losing all of that uh time, ask these
questions before uh you begin. Few
questions uh that can help uh is what
needs to be in the report. So what data
that needs to be in there? Where does
the data come from? Where do we find it
currently in business central? Uh you
can use the um control alt f1 on any
page to try and figure out where data
comes uh from. Users might not be able
to answer these questions directly. So
simply asking them where you have the
data right now, where in BC is it. I can
help you figure out whether the tables
the relations between the tables and how
to build that into your data uh model.
Then how do you want to use the reports
and do you want to simply be able to
look at it? How recent does the data
need to be? Is it a problem if that data
is uh 5 minutes old, one hour old, the
data from uh yesterday? And are you
going to print the report or you going
to use it in some other uh way that is
usually going to determine which type of
layout might be best suited. Then very
important what level of detail is uh
required. Now if you ask uh the question
the first answer usually is well we need
all the details then the negotiation is
going to start yes but h do you really
need these details in the report because
you have them in business central. If
you want to look at the details uh go
and look there and so what level of
granularity what level of detail is uh
required
how to visualize the data are also
important and because depending on the
layout type that uh that we have we
might not have the possibility to do
certain visualizations especially in
PowerBI where uh there are lots of
visualization possibilities always ask
the question how the data needs to be
visualized because even though PowerBI
has a lot of capabilities
uh it might not have exactly those uh
visualizations and then you might opt
for another format.
A question I also almost always get is
um can we export this to Excel? You can
create the best report with the best uh
layout. Uh one of the first questions
will will always be yes but we also want
that in Excel. So ask that if the qu if
the answer is yes then you need to
support have have a layout of course
that uh supports that you also need to
ask are you going to need to print the
report share the report email uh the
report or some uh data from it or you
going to do that within uh the
organization that's sharing or do you
also need to share information outside
uh the organization and for example
PowerBI has great possibilities to share
But usually within an organization
sharing outside is not impossible but uh
might require a little bit of of
thinking especially also about the
security uh of that uh data.
Last but not least once you have the
report you want to be able to make some
changes uh yourself. Usually uh that
goes hand in hand with can we export it
to uh to Excel because they want to be
able to make these changes. But ask that
question also in the context of why do
you want to be able to make these uh
changes? Um the reason might be there is
a problem in the process. If a report
that is created always needs to be
modified and it means that the all of
the data in there is not correct. The
data comes out of the system. So the
process that generates that data there
is usually a problem in there. You can't
fix that in the report. The data in a
report always shows what is happening.
If the data in the report is not showing
uh what you would like it to show, then
don't change the report. Change the
data, change the the process. It's very
easy to get stuck uh in these requests
and try to fix that in the layout.
That's sometimes uh impossible. Now to
give you small example, a long time ago
I was asked to create a sales invoice uh
layout RDLC.
Uh usually that takes a few hours for a
report to modify or create from scratch.
Now that particular report took me 20
days to uh to create and the reason was
that every time I showed it uh to the
customer they wanted some uh changes.
Did you think about this exception? Did
you think about that case? No, you
didn't tell me when I asked you. Okay, I
can build it in. Do you have any other
exceptions? No, no, we don't have any
other exceptions. And that went going on
uh for a whole number of uh of days. Of
course, I was lucky this was not not a
fixed price uh project. Now the reason
for all of these change requests was
that in the old system all of the flaws
and issues in uh the process of
invoicing were fixed in uh the layout
but there were a few problems that
needed to be fixed in that uh that flow.
So always ask these questions and this
can get you ready to decide what layouts
and what type of report might be more
interesting. Voila. That was a a small
introduction but not an important in
business central with a few tools
available. Uh one of the newest let's
say kits on the blog is the data
analysis or analyze list page data or
query uh data and it fits in the uh
lower part of this chart here. Uh we
have less aggregated uh data but we have
some possibilities to aggregate. It's in
the client. It's an operational uh
report that we very quickly can create
on uh screen. So before we're going to
look into the details, there are also a
few permissions you can set on that. So
we have this permission set which you
can give to someone to use it or deny h
to not use this functionality. And also
developers also have the possibility on
pages to use a property analysis model
enabled and to enable or disable that
functionality on uh pages because there
might be a few pages where you don't
want to uh enable uh that to go into the
analysis model you need to find the
button and simply click on it on most
list pages it will be available then you
can get uh started
I have the screenshot again of that
button and uh the permission set that
you can use. If you're going to dive
into the analysis model, you get a
window. Uh it has a few um areas on it.
We have the data area where you can see
the data. We have a summary uh bar. Uh
we have columns and uh filters and
that's basically how it looks like. Uh
right now in the data area you're going
to see the the actual data uh that you
are working with. At the bottom for our
numerical columns, we're going to see a
few totals.
Uh in the data area, you might have some
buttons, you might have some rightclick
possibilities. It also depends a little
bit on the version of Business Central
that you have on my slides. I have a few
features which uh might not be available
yet or might become available in 26 or
26.12
or one of the next uh uh versions.
Microsoft is heavily investing in this
technology.
interesting at the bottom is that you
have a summary bar uh where you see some
totals, some aggregates and these are
always very interesting in my PowerBI
reports. also try to incorporate them
because they can help you check if what
you're looking at is correct. uh in
these uh pages normally uh it should be
correct but in PowerBI a total m might
not match for example what you see in
the uh details
we can select uh columns you can do
clicky clicky draggy droppy in here uh
you can select the columns you would
like to uh to see you can put them in
the row groups you can select some
values to summarize or to aggregate and
there is a top and you can create
multiple tops in there to create
multiple uh views you and double click
on the top to rename it. It's really
nice to uh to play with. And there's
also possibility to go into private uh
mode.
Um when you right click uh there is or
there is going to be also a possibility
real soon not only to look at the data
which is currently in uh the page which
might be standard fields or custom
fields that you have been added via page
extensions.
Then in the future we'll also get that
possibility to find data from related uh
tables. So here I'm starting from uh
customers and I can also go to locations
responsibility centers uh or other uh
sources and if you click on the other uh
sources might get some other tables that
are uh related and you can also use
these fields in your analysis. Uh this
is a preview. It's coming uh real uh
soon.
All right. There's also a filter pane
that you can use to filter on a number
of fields. For certain fields, you will
also get some aggregates for date fields
and you get the year, the quarter, the
months and so on that you can also use
these things or add it in there
automatically.
Once you create uh your views, they will
remain in uh the client when you reopen
the page. Go to the analysis uh views or
they will be there. But you can also
export them and right click share and
you can send a link to someone within
the organization and to directly go to
these uh views.
These data analysis uh views are
interesting if you would like an ad hoc
uh report directly in uh uh the client.
You don't want an an extra object. You
want to see it directly in a list page.
It's kind of an Excel private table view
uh on list pages that you can create uh
that you can uh customize quite uh quite
quickly
within uh business central
once the feature was introduced and that
was it. But now Microsoft has also uh on
certain pages added a few default of
these uh views. Have a small overview uh
right here in the presentation uh which
is also going to be shared. I added
quite a lot of links. You can click on
those, go to docs and there you can see
some more details and screenshots and
where you can find all of these uh
builtin data analysis uh lists.
All right, time for a short uh demo.
So I will go to my uh business central
here and you can typically go uh to a
page uh and then when once the page uh
opens we have that button right here. I
zoom in. right
on which we can uh click.
Then we get the uh analysis uh view on
the right side. You can select which
columns you would like uh to uh use. We
drag and drop them in the row groups if
you would like to. Then some numerical
values on the customer list. I'm simply
seeing a few totals by customer. But if
I for example would go to uh items,
we can get some more uh information. Um
I have an analysis here uh that I
already uh prepared uh where we
basically are seeing uh the inventory by
uh item and there's also an availability
column uh that I added in here. This is
not a standard column uh on this uh page
but a custom column that I created via
simple page extension.
And if I go into the let me try and see
if I can find that page extension.
Um,
I should have remembered where it is.
Let me have a look.
Here it is. So, I have a small page
extension for the uh item list which I'm
adding an availability uh field. Um, and
it's a very complex uh uh calculation.
So basically my availability is the
inventory plus whatever is on purchase
orders minus what is on sales orders. A
simple example we can make it more
complex later.
Uh within our page uh we can see the
availability. If you go to the analysis
model we also have that field to play
with with totals and subtotals that can
be created. So uh think about that. Uh
if you're looking at the number of pages
you can add calculated fields to make
these also more interesting.
Once you see your analysis view, you can
also jump to a private uh model where a
few non-numerical fields will then be uh
removed that looks more like a private
uh table.
Here I'm also looking at my items per uh
unit of measure. Um and I can also jump
to private mode to see some details. So
in almost any list page uh you can uh
use this functionality and add a few uh
uh views and for example items by
location by uh um availability.
We can also go go and find ledger entry
pages also enable it on uh uh there.
All right. Usually that limits us to the
data which is in the source table of
that page or a few related uh tables.
But you can also uh prepare your data
sets especially for data analysis model
and and there are a few gains here.
Basically you can create a query objects
and if you give a query objects a usage
category that means you can find it in
the client. If you click on it then in
the results of the search it will also
open in analysis mode. So for any query
that you develop you have that
possibility. So this is an API query as
you can see where I've also added that
property. So whenever I'm going to
create an API query for example for
PowerBI reports or for something else by
simply adding this property in it and in
the client we can also uh use it in the
analysis uh mold uh which can be
interesting even though queries
sometimes have a few uh limitations it
gives you a few more uh possibilities.
So let's have a quick look at uh that.
Let me go back to Visual Studio Cold.
I have my data analysis items uh query
uh here. Few properties usage uh
category is also in there.
Let me copy it for the time being. Makes
it easier to find. Again
in my query I'm starting from the item
uh data item selecting a few fields
which I think that might be interesting
then I'm going to the ledger entries
interesting about the query object is
that you can use the SQL join that you
would like to use left join inner join
and uh others from the item ledger
entries I'm selecting a few fields which
I think might be uh interesting
then from the item ledger entries I will
go to the uh value uh entries. So do and
joining a actually these three uh
tables. Interesting about a query object
uh is that you can use methods on a
numerical uh field to aggregate your
data also on date fields to add the year
the month and the day level. If you do
that you automatically get a group by on
all of the other uh columns. So okay
this might be a query or an API that we
have developed for PowerBI or
specifically for our uh users and
because of that property you can quickly
find it in the uh client and if you run
it it opens automatically in analysis uh
molder I have all of the fields uh
available from uh my query and the
related uh tables and you can start uh
to also create your uh little private
table with totals and uh subtotals.
that I find is really really really
interesting. Um, so
remember that whenever you're going to
create uh APIs that they might also need
to be used in that analysis model though
there's also going to be a small
difference. If I'm going to create APIs
for PowerBI not going to join too many
tables and if I'm going to create APIs
for data analysis model joining data is
quite interesting.
Normally in my session I was not really
going to talk a lot about copilot or AI.
I think there might be quite a lot of
other sessions uh that dive into that.
However, uh in data analysis model there
was also a copilot button on which you
can click. You can type in a simple
question uh on that item list. Show me
the items by type and unit of measure
and it will simply generate that uh
view. Usually creating the view yourself
is almost as fast than asking the
question. Uh but this might uh help if
you have quite a lot of fields on that
uh page. Not going to demo it right now.
It's very easy uh to do. Uh and a few
tips uh are also that uh for your
prompts uh you need to be uh uh precise.
Uh so be concise. Use the field names as
they're known in the application. You
might not need to say um inventory. You
might need to say quantity on hand. that
helps uh it uh natural language common
keywords are also recognized
some sort by group by this by that and
so on and you can also provide some
followup uh instructions in your prompt
to get a better uh result
uppercase doesn't really uh uh matter
so that's a nice uh a nice feature
all right so data analysis uh remember
that uh it's something that we have in
the client to quickly be able to
aggregate and summarize some data.
Next topic I would like to talk about
are uh report uh objects. Going to spend
some time here. First in the data model
then uh the different uh layouts with
advantages uh disadvantages.
Last but not least testing is also
important. I don't have any specific
slides on uh testing but whenever you
create a report please test it and
foresee the time uh to test that you
need to uh print or preview the report
look at the results are they uh the same
exported in the desired formats
especially uh with our DLC there might
be a few uh different ways on how
margins are calculated and you might end
up with blank pages between pages with
uh uh data. So these things you might
need to test. Printer settings are also
taken into account. Usually the PDF
preview uh is uh what it's going to look
like uh but might be worthwhile testing
it. Uh anyway
for reports creating the data model is
uh very important. So there might be two
let's say kind of situations on how you
might want to create a report. On the
one hand you might be a developer and
then you have your hands on how the data
model is created. On the other hand, you
might be a consultant. Then you have to
work with the data as it is provided.
But it's important that you understand
how the data model is built and because
that will make it easier or less easy in
the word layout and RDLC layouts and so
on. So I've foreseen a few examples that
I would like to quickly look at in the
data model list one table. If you have
multiple tables or data items, how to do
a union, how to do a join and a report,
left, outer join, inner join, cross uh
uh join using a query, the data model
that we typically have in uh documents
and why that is the case. Using an
integer, what might be the advantage of
doing that? A buffer table. And then a
simple example of being able to quickly
dynamic encoder switch the current
layout of a uh report.
All right. So I'm going to have a look
in Visual Studio Colder. I have prepared
a few uh reports for that.
All right. When we start with
a list report, I typically mean a very
simple data model, one uh data item with
a few fields. There might be also some
numerical fields on uh there.
That's it. We then also have the
possibility to add layouts in the
rendering uh section. Usually um I will
have one RDLC word and Excel yard, but
you can have multiple uh ones. And as a
developer of the data set, you also say
uh what is going to be the default uh
one.
All right. If I'm going to run this uh
report in the uh client, let me quickly
do that.
Even before you create uh the layout, it
might be very interesting to simply send
it to Excel uh data only to have a look
at what is the data set at runtime and
what is the data set at design time. How
did I organize my uh data uh items and
we simply uh will then see the resulting
data coming in via one table uh with a
little bit of data. Creating a layout
for that is uh quite uh simple. Uh once
we have our rendering sections uh
defined the empty files will be created.
Uh I can go to uh RDL open it with
report builder or visual studio uh
coder. Uh, Report Builder 2016 is what
you need to install. Um, if you would
like to work with Visual Studio, that's
also possible in the documentation in
docs. It's talking about Visual Studio
2019 with a certain plugin. But if you
install the latest version of Visual
Studio 2022, it will also uh work. Uh,
then you can also find that VSZX file to
be able to render the uh the RDL
in the layout. uh we get a few uh fields
as you can uh see uh right uh here
fields in the data set for numerical
fields there's also going to be a format
called in here and then I can simp
simply insert a table and then uh add a
few fields in there voila and uh that's
it very simple to uh to do
in the word layout uh if I would like to
create a simple uh list
uh then we are simply going to open word
And in Word, the first thing that you
might need to find is the developer uh
pane.
If you don't have that developer pane,
you can simply rightclick anywhere,
customize the ribbon, and then here,
enable developer. From then on, it will
be in uh there. All right.
I will go to the mapping pane. That's
where I will see my data sets. Uh it
still has the name Dynamics NAV but I
can see my data item in here uh which is
a customer.
Microsoft also recently added a default
data item for the word layouts uh with
some meta data that you might want to uh
use uh to all right to put this data in
here. Typically in word I'm going to
insert a uh table.
Um it will have a header row it will
have a detail So I select the detail row
and make that a repeater uh for the uh
data item that I would like to uh repeat
it in here. And I add the fields uh in
here. There is no clicky clicky draggy
droppy. That would be too easy. You have
to right click and then select the
content control that you would like to
uh to use for your fields. There might
be some plug hints from other companies
that allow you to do drag and drop. All
right. Simple data sets. uh so one uh
data item at one ticket it then really
matters what kind of layout that you
want to create.
Second example is how to do a union. So
as a report developer uh what we are
going to do is we're simply going to add
two data items right below one another
and it's then at runtime going to create
kind of a union result sets not
completely the same that how a union
works in SQL in SQL and you have to have
the same column names we have one uh uh
result set with in this case uh three or
four columns here what will happen is
that the first data item will be
processed then the second data item
and the result set of both are kind of
glued uh together. So I'm quickly going
to also have a look at that uh result
sets
and it's important to always check that
and because you need to know where the
data is in the runtime result sets to be
able to consume it uh correctly in the
uh layouts.
So I have my uh customer uh data in uh
here and I have the uh vendor data.
While it's processing the customers, you
will have annual values for the uh
vendors and in the layout. You might
need to filter those uh out.
I've also provided a few let's say URLs
in here or email addresses. You can use
them uh interestingly in the words uh
layout for example. Right? That's the
data set uh to create the uh layouts for
a union in uh RDL RDL or RDLC.
That will be a little bit more work
because in the data set we always have
one data set. Uh the name is always uh
the same uh in the RDLC layout. It's
called data set results
and I see the columns uh of uh customer.
I see the columns of uh vendor. And the
difficult thing is for example being
able to split these into two uh tables
and not show the empty rows uh in there
construct. What we then typically do is
filtering or hiding on the left side I
have a table where in the table uh
properties
I have added a uh filter and the field
that I'm filtering on is basically the
uh customer number. If the customer
number is empty, you don't want to show
uh the data. Uh but trust me, it works
better if you first convert it into a
string because customer uh in business
central is a call data type. Here I am
in VBR. So to really uh do the matching
correctly, you need to use the CS2
function to convert this. Then I'm going
to say this value needs to be bigger
than the empty value between double
quotes uh in uh here. And uh you can
choose uh different from and and so on.
But also trust me it works better if you
say bigger than than if you say
different from. Don't know why but
that's basically uh my experience.
And that way I am uh able to filter out
data in this table
and to fetch the data in the data set
that comes from the customer data item.
So in RDLC that requires some
manipulation. Another way of doing that
is by for example adding a visibility uh
rule on the detail uh row and we'll go
here to the row visibility I can create
an expression for when the row needs to
be visualized or uh not
voila I'm saying that uh if the vendor
is empty hide uh the row uh in this
vendor uh table these are usually the
two ways uh that you can do that and I'm
showing both ways because For example,
in the document layouts or DLC layouts,
uh sometimes they use the filtering way,
sometimes they use the hiding uh way
depending on who developed the reports.
So in RDLC that might require a little
bit of manipulation and knowing that um
VBIA uh language
in words and that's what I was really
happy about when the word layout was uh
introduced. We don't really need to do
that in the word layout. Um it is as
simple as looking in your uh data model
and in the work layouts you're only
going to see one uh but you're going to
see the two tables. You can quickly see
uh that they are on the same level. So
this is basically a union happening
and I'm going to create a table insert a
repeater for customer another table
insert a repeater for vendor and these
tables will be automatically filtered to
that data item. So don't need to provide
any other filters.
That's a fun thing about words. Um all
right so if you have uh unions somewhere
in your data set what you need to
remember is that a word layout might be
uh easier or if you want to create a
word layout union your data sets
a join of course that's also a
possibility
I'm joining here customers with uh
customer ledger entries you need to
provide data item uh link uh to do that
and uh sometimes uh uh um sorting. The
reason why I do the sorting is not
because I want to sort and but because I
don't want to have the second ledger
entry data item pop up in the request uh
page and by sorting uh you can uh then
remove that.
If you do not specify a data item link
and you also do not specify print only
of detail, you get a cross join which is
the cartisian product of the two tables.
All records will be uh connected.
If you provide a data item link
and you do not provide print only of
detail then you get a left order join.
If there are customers without ledgers
they will still be in the data set. And
if you do a print only of detail in here
you get the in uh uh join. You can
define that as a developer hardcoded
using the properties. However, there's
also a print only of detail methods that
you can use if you want to run the
report by caller using a report variable
where you can disable or enable that
print only if detail property
dynamically. So you don't need to create
multiple reports. If one time you would
like to run at the left order join, the
next time an inner uh join.
If you're going to join data, you will
kind of get an aggregated data set which
works best then in the RDL uh layout. Um
the advantage of the RDL is that we can
create a table.
Let me zoom in here. And then in that uh
table also a few uh groups.
Um I start with the details and I'm
going to create a few parents uh uh
groups. So the little trick here is to
simply start with a table.
put the numerical data in here or the
details that you would like to see and
then remove all of the other uh columns
for example the amount
starting from here I'm then going to add
uh parent uh groups
and I'm going to say okay I would like
to see the amount by customer I would
like to see a total so I select customer
and we can add a header and or a footer
Voila. Then uh I have a group in my
table. I will see uh each and every
ledger entry I will see the summary by
customer. To see that summary by
customer, I'm also going to add the
amount field in here. Click right click
and then uh summarize uh for example and
calculate the uh sum.
All right. The scope will automatically
be the group. So we'll get a subtotal by
customer. You repeat that uh process and
you can also group by any of the other
fields and within the RDLC layout we can
very easily create and aggregate or uh
data which is a big you could say
advantage.
So if you have joined uh uh data items
the RDLC layout seems to be a nice one
uh to uh to use because you can also
aggregate and group and visualize that
data. the word layouts
not actually the best layouts uh for
when you are joining data but not
impossible uh to do. So if we go into
our data set uh quickly um and you can
also very easily see that these two data
items are joined ledgers belong to a
customer and what I'm then typically
going to do is I will start by inserting
a table head row uh and then the
repeating uh row um for the repeating
row I will insert a repeater for the
customer data item I typically also
leave a tell uh blank or some room uh in
there. Um here I will then add another
uh table and for that table I will
create a repeater for the legendary uh
data item. So you can have nested
repeaters in the words uh uh layout and
that is possible.
All right. If we do that and we are then
going to run our uh report in the RDLC
layout, it's going to look quite uh nice
within the word layout
even though we have the nested uh
tables. Let me quickly change layouts.
It is going to display that uh data. I'm
seeing my customer information and for
that customer the ledger entries and
they are uh correct and then the next uh
oops customer my mouse is a little bit
fast today. The next customer but then
the other uh ledger uh entries. All
right.
The problem uh with the RDLC uh uh uh
with the uh word layout is that we can
see the details but we cannot really
calculate these uh sub uh totals.
So it's something we can't really do in
that uh layout.
All right.
Next example is using a uh query.
The reason is performance and a
aggregation. So here I have a simple
query uh called customer uh ledgers
fetching information from the customer
table also doing a join with the
customer ledgers. Uh you can then
specify the exact joint type app you
would like to have the fields and then
also the uh methods uh per year per
month. I would like a subtotal of the uh
amount
this query I can once I have that use it
uh to build the data set of a uh report.
It's not very difficult uh to do and you
create your query uh variable. from the
query uh variable. You simply add a few
fields in the data set coming from uh
the query. Really easy. Then a few lines
of code. Of course, you need to have
your query uh variable in here. And um
as a data item, I'm going to use my
integer data item. I'm not going to
filter it in the properties, but I'm
simply going to break it when there is
no more data to process. So I'm open the
query. uh open runs a query leaves a
data set on the server but doesn't
return any data uh yet and then in the
un get record that will read record
until there are no more records that I'm
going to uh break so a few lines of code
and you can kind of use almost any query
in the data set of a report advantage is
performance performance of queries will
be a lot faster than simply joined uh
data items uh a second advantage is uh
let's say the aggregation possibilities
of queries to calculate calcate these
subtotals.
So you will have the data that you need
in the data set a lot faster and usually
smaller uh data sets. So also very easy
to uh do a disadvantage uh of this
approach
is that in a query uh you could say
unfortunately we can't really do any
programming can't define a record
variable and calculate availability in
our L code. uh that's not uh not
allowed. Um basically,
so if you that's something you would
like to do uh then a buffer uh table uh
might be a better uh example.
Uh let me also show that open to the
sides. So a buffer table I've created
table in here a customer buffer which
I'm going to use as a temp table in my
report in the data set with a few fields
uh customer number customer name and the
uh sales amount
that's a table and that I've created and
uh what I'm then going to do is the the
idea here is to create a top 10 uh
report. Now in RDLC you can say it's
very easy to do a top 10 filtering as a
property for that but then you might
have a very big data set and only show
these 10 customers. The idea is to have
the 10 already in the data set. No more
no less. That's best for performance.
Um so I am first going to process my uh
customers. I'm going to loop over all of
my customers to be able to uh identify
the top 10 ones that I would like to
have. going to clear my uh buffer table
and in the on after get records. I'm
basically going to insert
a record in my temp table and also get
the total sales amount for that uh
customer. Um voila, that's it. And then
I have a second uh data item using a
integer which is going to fetch the data
from the buffer table and display it
here. Top 10 uh buffer uh in the uh
results.
little bit of gold uh uh in here and the
play data item
to sort maybe to rank uh your uh
information. Um right now I have this
top 10 hardcoded in here but you can
also make that quite uh dynamic. So a
little bit of coding but uh then you can
programmatically calculate a few things
add them in your uh temp table. you have
the integer data item which is the
resulting uh one and that you can then
consume in your layout word and or RDLC.
So that's kind of the the the workaround
for the word layouts. You can calculate
stuff in the data sets using buffer
tables or other techniques and then uh
once you have that data item you can
simply link it to a table in uh the
words uh uh layout.
That's buffer.
Uh another data tip design data design
tip actually is working with integer. Uh
what I see quite a lot in uh reports
from developers but also some out of the
box reports is that we have the data
set. Then we also would like to include
a company name, company picture and all
of these things. We simply add them in a
connected uh or joint uh data item. If
you do that, the problem is that all of
these comp logos will be repeated on
every line in the data set which is
let's say suboptimal for performance. So
it's much better and that you for
example add a top level uh data item or
one at the end of your data set using
the integer table to fetch one row to
add one row in the data set and there
the all of the information you only need
uh once.
This adds one row in the data sets with
that uh information.
Very simple to do with an enormous
performance improvement.
Interestingly is that then in the word
layout it makes it even easier uh
because you will have a data item
customer uh with the data that you need
and another data item header text uh
which you can also put in another table
uh with with that data company logo. uh
for example
also for the RDLC layout uh more
interesting because we have a more
performance uh report but if you create
a table in the RDLC layout where you
show information in this case customers
don't forget to filter out that one line
from the integer uh data uh item
all right
in a document
and we also have a few uh things that
are uh important. So I try to recreate
data set of a document which is
typically a join between a header and a
line uh data item uh with a few fields
and a few options. What is important uh
there? Well, typically a document needs
to be generated in the language of the
recipient uh not the language of the
user running the reports. So uh we are
going to add field captions only for the
fields that need to be multil- language
not for all of them. And typically in
the on after get records we get the
language code of the header uh which is
typically the language coder of the
build to customer to switch language in
the uh report and to create a data set
with the labels in the language of that
recipient for that invoice. For example,
if you want some company information in
there, we also have a separate data
item. Here we have the integer in the
end instead of in the uh beginning.
All right.
What else are we going to do? Um
I can provide a few layouts. It might be
interesting
to uh skip the execution of the report
if the user did not filter in the
request page to not accidentally print
all uh uh invoices. This folder by the
way is in report 1306 by default.
And then you can create a layout. Now
creating a layout for this report in
RDLC is not going to be really uh uh
difficult depending on what you want uh
to do. Uh uh of course
let's uh jump uh in there. Uh what I
typically have in here uh is a table
and uh in the table I might have some
grouping. I have some header
information. I have some uh details.
Simply going to create a few uh groups.
If you would like, for example, every
invoice to start on a new page, then I
can highly recommend you to put that
table in a list. So, typically in RDLC,
we're first going to put a list
container in there. All of the other
tables go in there, too.
In that list, in the details, you might
want to add a group, for example, on the
document uh number. And when you add
that uh group, uh you simply click on
the page break uh property to get a new
page break invoice.
And this you do on the list and not on
the table. And typically in that list
you might have multiple tables that show
how you control your uh page breaks
in the word layout.
Uh let's have a look here.
I have one from Microsoft here.
Uh for the more complex data sets. Uh
you can also have all of your fields uh
there. And what you're going to notice
is that
we have that more complex data set. We
have the header with all of the fields.
We have the lines. We have all of the
other data items. And then uh what
you're typically going to do is add a
few fields need to be on top of the
document picture. Then for example uh a
table with or without some groupings and
or subtotals. So like we have done
actually uh uh before uh to be able to
have that new page uh per uh document.
It is then important in your uh data set
uh that you specify the word merge data
item property and put it on the header
and that will then basically take care
of of that.
So don't forget uh that is very
important for the words uh layout.
All right. So these are a few examples
of how to create a data set union uh
join and or a combination which is what
will typically happen in um
a documents.
All right then because I'm going to talk
about layouts a little bit later. Well,
last one I wanted to show you is uh this
report item list. That's a report where
I have for example two layouts.
I have uh two work layouts, an orange
one and a blue one. And a question is
sometimes okay in the RDLC layouts uh we
can use conditional formatting. We can
dynamically hide or show something. So
one layout can serve multiple purposes.
We don't have these expressions in the
word layout but for example you can
simply create two different uh layouts
with two different controls. You can say
which one is the default and when the
user runs the report in the request page
they can always switch uh very easily.
However, uh if I'm going to uh run this
report,
I always have to switch in the request
page. So, what have I done?
I have created another page uh that will
run my uh report. Let me go in there.
If I run this report, I will get its
default uh orange uh layout.
But uh if I run it, update it, it will
by default come with the uh blue uh uh
layout. So you can programmatically
control and change the default layout of
a report. Now I'm not the most amazing
programmer,
but I found a little bit of colder uh
online on Yammer to help me uh uh do
that. So basically in the colder of that
button, I'm changing which is the
default layout currently for this
report. I set it to orange and here I'm
setting it to uh blue. And basically
what you need uh to do
is uh work uh with the uh report uh
layout uh list uh table and there change
uh the default uh layout. Uh you can do
it per company uh also also per user if
you would like uh to do that. Here you
quickly uh change that. So instead of
creating all of these expressions in an
RDLC layout, you can simply create
multiple work layouts and dynamically
include the switch and determine which
one needs to be uh run and depending on
certain uh conditions.
All right,
these were a few things I wanted to show
about data set uh uh design uh or or
using data items. I can talk about it a
lot longer, but it's important to
remember that if you're going to join
and another DA might be easier as a
layout. If you're going to have unions,
that's very good for the word layout. Or
if you need to use a word layout, try to
work with unions. All right, features of
the different layouts are also
important. Uh the word layout, you can
uh print it, you can export it to a PDF,
you can email it, and the advantage is
that you can have the report as an
attachment in an email, but also in the
body of that mail. That's a reason
sometimes to create multiple word
layouts for the same report. One for
attachment, one in the body which is a
little bit summarized. We can't use
expressions. However, there's an add-on
which I'm also going to cover which is
going to simulate a few things that in
the future might might hopefully uh give
us um conditional formatting and some
expressions in the word uh layout RDLC.
Okay. Uh we can export to PDF. You can
email it as an attachment but not in the
body. Uh it supports expressions which
is nice but performance-wise not always
that great. In theory you can do pixel
perfect editing uh but um I think that's
mostly theory. Okay, you can position uh
text boxes uh but it's not always that
easy uh to do. And the reason why
Microsoft is not recommending to use
RDLC anymore in the performance
guidelines is not because RDLC has a bad
performance but the way that it's
executed in RDL you can use expressions
in these expressions that could be net
interrop that you are using and net
interrop is not allowed in business
central it's not safe so to guarantee
the safety whenever you run a report
with an RDLC layout it is sent to a
separate standalone sandbox and there
the report is executed uted uh and then
the result is fetched back into the
client. That takes time and resources uh
uh to do and so that's why it's a little
bit uh slower.
Excel layouts interesting. We're also
going to have a look at those in a few
moments. We can't really print them yet
directly from code. You can download the
Excel file, but you can use private
tables. You can use uh uh um slicers,
all of your Excel skills, Excel
formulas, power query, and also uh power
uh private.
All right. So, if we dive a little bit
deeper into the different layouts, we
have the words uh uh layouts.
Word layouts typically need to be
printed. If you're not a developer, we
typically go into the report layouts uh
page and there we can create new ones
based on an existing uh data set. that I
have the steps uh laid out right here.
Um and we have some buttons. If you
would like to create a new layout, you
first run and export an existing one and
then we can use that as the basis for uh
for the new one. And same also basically
with our DLC.
In the word layouts, uh you have your
mapping pane and you typically create a
repeater for the data item in a table
row where you would like the data to be
uh repeated. And then you can use your
word design uh skills uh to design a
reports. Um there might be quite a big
difference between looking at the report
in design time at runtime. So a lot of
testing and trial and error might be uh
required. But still uh there are quite
some options uh available.
Um, besides creating a simple uh layout,
there is also some very good
documentation online that explains how
to use all of these uh things, headers
and footers, how to use tables, how to
create lists, how to use sections uh and
so on. And these are a few tips and
tricks I would like you to take away uh
uh or use when you're going to design
word layouts. So I have foreseen a few
uh bits and pieces about that. So in
words, what is really interesting is
that we can use headers and footers. You
can have different headers and footers
for the first page uh or for other uh
pages. Um you can put the break uh also
in there if you would like to to do some
testing but then don't remember to
remove that break. So headers and
footers with formatting is um is
possible. NLC say we also have headers
and footers but they are a little bit uh
limited.
Then if you're going to put fields in a
word layout
um you don't want to repeat anything but
fields or images you can simply add them
in there or add them in tables. So one
tip I would like to give is put these in
uh tables at runtimes you will not see
these tables but tables help to align
fields more uh easily even uh images.
Here I have an example uh of company
name a company name and a picture in one
table. But for a picture you could also
say I'm going to use a one-on-one table
only the picture in there. And it can
also control alignment but also growth
of images in word uh layouts. At design
time you can also enable grid lines.
There's a button for that. I have it
marked right here to see where something
is positioned. uh don't remember to uh
uncheck that. Then afterwards
with pictures, you can also use tables
to control how they are going to fit
that not going to over uh flow within uh
uh the cell of that table where you put
the picture in. There are also a few
properties to adjust spacing
and you can also disable the via
property the behavior of the cell to
automatically uh resize. So that's might
be interesting to do. Uh something else
performance-wise uh for pictures which
is also important is uh compressing. So
in a picture in the word uh layout you
can go to the picture format top and you
can click on compress uh picture uh
which will then at runtime compress the
data will which will make it smaller
layout and a faster uh report. Simple
property uh uh to click that's all that
you need to do.
So in the word layouts I'm going to use
uh tables not only for header and
repeaters but to basically kind of uh
position elements. If you have a table
you can put a repeater in there can be
multiple uh nested repeaters as I've
shown you with the join uh report. In
the uh documentation it says as many uh
nested repeaters as you would like to
but I usually don't do more than two or
uh three uh to be honest.
All right. Um lists uh is also
interesting to uh use if you like a
bulleted list or a numbered list with
some data in uh there you can start by
creating a list uh in uh word and then
also put a repeater in there. It doesn't
always have to be a table. Uh so that's
also interesting to uh to do and the
details I also have have here.
With nested uh uh repeaters, it can
sometimes be difficult to see where is
uh what. Uh so don't go too many levels
uh deep. But I basically have showed
this uh uh before with a small
screenshot on the slide to uh emphasize.
If you work in tables, you can also
resize columns and try to position a
little bit where data uh needs to end
up. But uh should be honest, it's not
always the most fun to do in the word uh
layout.
Regarding totals and subtotals, well, we
can't aggregate in the word layout. So
basically the idea there is to use a
buffer table or to have a data item in
the data set that has the detailed data
and another data item that has the
totals or the summarized or the
aggregated data. And these two separate
data items you can then bind to
different tables in the work layout. And
that's also how it's done in the
workload of the sales uh invoice.
Same for conditional formatting. We
don't have those limit those
possibilities right now. A few other
things. If you're going to use styles
for tables and you can right click on a
style and you can select a default which
is uh applied on any table that you will
have in your words uh layout.
Hyperlinks that's also something that
you can uh use. So if for example you
have a data set customer where you have
an email address where you have um a URL
you simply have those fields in the data
set you put them in a table in the work
layout and automatically at runtime you
can click on those and you can navigate
to the website and also if you uh save
these as a as a PDF you don't have to do
anything special just have the email
address in the data set and u u the
links an RDLC you can also do that with
an RDLC you have to go to the textbox
properties and enable the hyperlink uh
uh property
sections. That might be the best tip to
use in the word layout. Um in a word
layout, you can create different
sections which have different uh
properties formatting uh paper uh size.
Uh for example, you can have sections
start on the next page but also in the
same page you can create multiple uh uh
sections and you have more control uh on
what happens. For example,
click. Um, this is also a one uh report
where the first page is uh portrait and
the second page is landscape by simply
using sections and changing that on uh
uh there. So that might be interesting
to uh to do
fonts. There are quite some fonts that
uh you can use. The whole list is also
available on uh docs. These are
pre-installed and available by default.
Don't think you can add any or extra
fonts.
Also in tables go to the in the word
layout in a table go to the properties
and there are table properties. There
are row properties, column properties
and cell properties that you can play
with to try to align uh the data uh
which is uh in there. You can do that
relatively but also uh absolutely. I
also have an example of that in a few
moments. So for a table uh for example
you can go into the table properties you
can set the text wrapping to around. If
you set the text mapping to around the
positioning button becomes enabled. You
can click on it and then you can go for
an absolute positioning uh of that uh
table if that's what you would like to
uh to do. So that can be um also
interesting to uh to remember.
All right. So the work layout it has a
few limitations. and cannot do a few
things that the RDLCO can do. However,
Microsoft is working on that and if you
need to be convinced to stop doing RDLC
and to move over completely to words, we
need some extra bells and whistles in
the word layout and there's an addin for
that that Microsoft has created. It
currently has these functionalities, but
more is coming. And what might come in
the future, I really hope that uh is
conditional uh uh formatting and also
being able to have conditional
visibility of controls in a layout. That
would already be uh a great step
forwards. Currently, it's heights, a
field, a row, a column, and adding some
comments in there. The first thing that
you need to do is in the word layout, uh
you go to home, get add-ins, and you
look for the uh business central word uh
addin. You install that and then you
will have it available in the word
layout under a new top called business
central h with then a button uh in here.
Once you have created a table uh in
there you can select for example the
table say height if empty. You can
select a row in there and say height if
empty uh and so on. You can also insert
comments uh in your word layout which
might be interesting uh to do some
versioning of uh of layouts. So I have
an example in here of a comments um and
at design time you're going to see these
comments set. This is a customer table.
This is vendor table. And for example at
the bottom I have a inserted a table
with some versioning information. Who
designed this layout or might made which
change at which moment and so on
versioning table at design time nice to
have but if I'm going to run the report
h these things are not going to be
visible.
Another example is to mimic blank zero
and blank uh numbers. Uh uh we can also
use these uh heights. If empties on the
left side, if an amount is zero uh you
will see it on the right side. You're
not uh seeing that. Amazing. But okay,
it's something that we were unable to do
and that we can do right right now. If
you don't have that addin, this is also
something you can simulate in the data
set because if in the data set a field
does not have a value, it will not be
rendered in the word layout. So you can
programmatically can also make something
empty, clear it and it will also not be
rendered in the layout.
All right. So for the words uh layouts
uh I think I have already demolded most
of these if I remember uh correctly one
thing that might be interesting and that
can serve as inspiration is this
um if you would like to be convinced on
what you can do with the words layout it
might be interesting
uh to look at this reports
or one of its siblings. This is a clone
of 1306, a standard sales uh uh invoice
where Microsoft redesigned the data set,
optimized it for the words uh uh layout
and there's also interesting layouts
that you can have a look at. You can get
this out of the uh base up
and you can have a look at the uh data
set quite some fields in here. Um what
is interesting is that the way that the
data set is changed is that all of the
fields have been given uh quite good
names data items too. So that if you
look at those in the word uh layout h
that you by using the name of the table
kind of know what is uh in uh there and
if you also look at that data set have
to scroll down a little bit uh we have
the typical data set of a documents then
at a certain point you're going to see
quite some other data items coming in
with uh unions of uh data uh work line
uh description v amount lines uh with or
without uh details uh unionions with
header information, footer information,
vit clauses and so on. Um report totals,
report header left side, report header
right side and so on. All of these data
items are unions. And the reason why
this is done in the data sets is that uh
in the work layout that makes it a lot
easier to uh visualize.
So in the word layout of course we have
our table uh with the uh uh details uh
but we also have other separate tables
with uh totals uh uh in here coming from
uh the new data items or the redesign of
these uh data items.
All right, here it is. You can see the
header and if I scroll to the bottom and
you can see all of the other uh data
items and for example we have buffer
tables or integer tables calculating
information especially for the work
layout
and the idea is that you get different
tables in the work layout which you can
then map to tables in the layout itself.
So different data items to tables.
All right.
What you can also do when you create uh
a word layout is to create more
professional looking reports. One
possibility would be the following.
You start with words
and then okay in words file new actually
and you can use for example some uh
templates. So if you would like to
create an invoice
uh report it might seem silly but you
might want to look around for one of
these standard invoice nice looking uh
uh reports. If you say okay this is a
layout I would like to use in business
central and you create a word file with
that nice looking uh layout and then you
need to strip it a little bit so
basically if there is a table in there
I'm going to remove all uh rows except
uh one
delete cells delete entire row
um until I have something uh which is
looking uh nicely what I can then do is
file save and then also save it in the
folder where the report is and in visual
studio cooler do a control shift B to
have the data set in the word layout and
then you can go to the XML mapping pane
and for this row for example add a
repeater and then simply replace a few
of the fields in here with some fields
of the data set that's something uh
interesting uh to or interesting way to
get started
another way to get started is maybe to
convert an RDL layout to a word layout
or to start from an existing documents
Okay, these are a few uh tips uh that
you can do an RDL layout. You can run it
in the request page. You can send it to
a word file
and then you have a word file and you
can start with you can script it. You
can put the data set in there and so on.
So that's something uh might be a way uh
uh to work. However, I wouldn't really
really recommend that because the word
layout of an RDLC file that's not always
that uh that great, but it's one of the
possibilities.
Another way to get started is that you
get an existing invoice from your
customer in a PDF format. You open words
in word file, open PDF, PDF converted to
a word file and you have something also
uh to get started with which you can
strip put the data set in there and
continue. So there are a few ways on how
to get started uh uh there if you want
better looking uh layouts.
All right. So you can use the word
layout also in the body of the email. Uh
you can also do that on u customers and
vendors to have customers specific
vendor specific uh exceptions.
This email uh looks like but that's not
really new functionality. It has been in
here for a long time. But if there's
something that you would like to do,
then the word layout might also be very
advantageous uh to use.
All right, have about 20 minutes left
and few things uh to to show. No worry,
I'm still on on schedule. RDLC layouts.
Um that's an alternative for the word
layouts. The advantage is that we can do
some uh scripting in uh there and we can
use our triangle detailed information
but also the possibility to summarize
aggregates uh and so on and uh I can
talk for a real long time about RDLC
layouts but why do that? Why go to RDLC
if you could drink a coffee and enjoy
life go for a walk with text my dog?
Um the reason I have this slide in here
is that if you're already using RDLC,
fine continue uh to do so. If you are
not yet using RDLC, no is not a good
moment to start.
Uh because in the future
maybe, who knows, we might not have RDLC
anymore or might become limited or more
expensive to uh to use. The reason is
that um RDLC technology comes from SQL
server reporting services was introduced
in the year 2000 and the latest
officially supported release was in
2016.
There is no support on it anymore. So
basically that means that if someone
finds a security book in RDLC, Microsoft
is going to have to stop using that in
SAS immediately. So if they will find
it, they need to stop with that. So
there might be thinking about phasing
this out because it's basically not
supported anymore. It's not in the hands
of the business central team. It's a SQL
team uh that simply don't support that
because they have a new version of RDLC
in uh PowerBI.
If you still would like to get started
learning RDLC, there are some great
resources online and there's also an
amazing book that you can have a a look
at uh with some guidelines and some
examples. It's based on the vision. Uh
but if you go to my blog and my GitHub,
github.comsrrendx/blog,
I tried to convert a few of the examples
in my book based on uh cases uh to that
might also get you up and running and
lots of tips and tricks on working with
um tables and groupings and a matrix and
different kinds of layouts and and
formatting and place and bottom and and
all of these uh these features.
All right.
A lot of the um interactive features of
the RDLC layout no longer work in
business central. Why? Because in a
vision we would render a report RDLC
layout in the report viewer which was
the HTML version which was interactive.
In BC we get a PDF export. So that's not
always interactive.
Okay. If you would like to know a few
things about RDLC, then for example, it
might be interesting to also take the
standard
sales invoice as an example.
This one I usually prefer to edit in
Visual uh Studio.
All right. And what we typically see is
that here we're also going to use tables
uh uh to position information. Big
difference between 1306 and 206 a long
time ago is that header information is
now in a table at the top of the body
and it used uh to be in the header.
Okay. An advantage of being able to put
something in uh the header is that you
can have it repeated on every page. You
can use expressions to determine when or
not to show it. But to get data from the
data set in the header, you have to use
these nice uh workarounds like get data
set data. And there are also better ways
of of doing that. You might remember
these from a long time ago, a galaxy far
array. Um but in 1306, no trace of that
anymore. It's all in the header. Easier
to read, easier to maintain. Only one
little problem. The table at the top of
the body is only visible on the first
page and not on the second or third and
so on. That's the RDLC out with a few
workarounds that are still uh still in
here. Can always go a little bit deeper
uh in this or if you might have some
detailed questions after the session,
come and find me. I will always be happy
to go a little bit deeper in uh RDLC
layouts. advantage is that we can use
expression, we can dynamically show and
hide uh uh things like conditional
formatting, conditional visibility, but
I'm pretty sure we'll also get that in
the future in the um word layout.
So, RDLC layouts, if you ask a customer,
hey, how do you want the layout to look
like? Do you need grouping? Do you need
something special in the body and the
footer and maybe on different pages,
different information in body or footer?
Do you want to uh visualize data in a
table matrix or other visuals? Okay,
these are all things we can do with
RDLC.
We can't really do that in the words uh
uh layout. All right, Excel layouts.
That's also interesting to uh look at.
Um I'm going a little bit faster because
I'm really out of time. Uh but no
problem. Um
you can create good data sets and also
an Excel layout around it. And basically
let's say our DLC goes away and then if
you have union data items will go to the
word layout. If you have join data items
and Excel layout is really interesting
to uh use. Even though I'm not using
these very much in real life they have a
few advantages. Some links to official
documentation
how to add comments how to do all of
these things nobody ever does but there
is some documentation about that. But
what's a big advantage of using the
Excel uh layout? It is that you can have
multiple views on the same data. But
there is a contract. So if you generate
an RDL an Excel uh layout, you get a
data sheet. Don't rename it. Don't
delete it. In that data sheet, there is
a data table. Don't rename it. Don't
delete it. And that's the contract with
the layout. You can move it, but you
cannot uh rename or delete it. You will
also get some presentation sheets that
you can create. And there's also a meta
data sheet that if you would like to,
you can uh delete. You get some extra
options in there, translated captions
and so on. So you can also indeed do
multi- language uh Excel uh layouts in
business central and that's where you
can see the big advantage. Microsoft as
also added some Excel layouts for some
reports used to only have RDLC or a work
layout to make them a lot more
interesting. age accounts receivable.
You can see the data, but there are a
few slicers uh in there and some other
reports also. I've just taken a few but
actually quite a lot of these that now
have an Excel uh layout.
If I look at the Excel layout
all right
then I have here an item availability
data set.
Start with the item table. go to the
ledger entries and also include sales
lines and purchase to be able to
calculate availability. Going to add all
of that in my uh data sets and then I'm
going to create an Excel uh layout to
visualize that information.
It takes a few seconds to uh load.
Uh now what do you typically do? Uh uh
you uh run the reports. There you have
the layouts that you can generate save
into the same folder and then you can
open it in Visual Studio Cool. They have
some data to play with and what I have
right here is a table a table uh with
some a private table with some
information also private charts uh below
that and some other uh charts and the
possibility uh to slice and dice or to
filter uh for example using Excel uh
slicers.
That's all very nice. These are all
options that Excel
uh has. You can work with all of these
visualizations in Excel. What you need
to be aware of is that you have your
data sheet,
excuse me, this is the one
where all of the data is from the
different data items. Using that to
create this report will be challenging.
So um what do I typically do for Excel
layouts? And you can provide information
in your data items uh joints uh items
and then ledger entries, sales lines and
so on uh unions and then in Excel it can
be interesting to go to the uh data top
and based on the information in the data
table to create a data model in power
private.
So you can open that table in power
pivots. What then happens is that you
have the original table with all of the
information. We can then split it into
multiple tables in power private. So
based on the information in the data top
split that into new tables, one with
only item information, one with ledgers,
one with purchases, one with sales. So
we split that out in different tables.
And then there's also a possibility to
create a data model uh in here. So I
split out in multiple tables. Then the
item table I linked it one to many with
purchases, sales and ledgers.
That's you. And then uh what you can
also uh do is go back into the uh data
view and there's also a possibility uh
to define a few measures uh in here if
you know ducks. All of these things we
can do in in Excel. So starting from a
flat data
uh table uh you can create kind of a
star snowflake model in Excel in bore
private save it and then also use that
uh to generate
uh private uh tables. So that's a big
advantage. You can use all of these
features of Excel. There are a lot more
features of course also uh available.
The advantage is that okay you have your
data sets uh and then a user can create
that Excel uh layout and uh uh consume
it.
Um but there are other ways of working
and because for this to work you need a
developer that creates that data set for
you. Um
a few properties uh in Excel Excel lay
out multiple data sheets. If you don't
want to have one top with the data but
one per data uh uh item uh then uh you
can do that. That's also uh quite uh
interesting especially with union uh
data items. All right, there's a new
report explorer uh where you can find
all of the reports report extensions.
Also wanted to mention that
with the report extension you can add uh
or change something in the data set of
an existing uh report if something is
missing and you can add columns, you can
add data items and so on. But what I
would like to say basically is be
careful because this can also happen on
the left side. If that is the let's say
data set of the current report you want
to extend, you might not want to extend
it. So make sure the current data set is
stable and extendable.
The middle example I will go into more
details that can happen with a report
extension. You might be extending it but
might end up in the wrong place. And
then uh a report can be extended many
many many many times but it will not
make it a more betterl looking uh data
set. That's the example at the right
side. So be careful with that especially
developers. So for example I have a
report in here two data items customer
vendor and basically what I would like
to do is add uh more uh information in
here like uh contacts
um and I'm going to add that after uh
the vendor data item. one of the first
report extensions I created.
And when I ran the report, something
strange was happening because even
though I had a lot more contacts than
vendors at runtime, I would always have
exactly uh uh the same amount of
contacts than vendors. When I looked at
the data set, I found out, okay,
something is wrong. And
what is wrong? Well, I made a small
mistake. This should not be at last, but
at after.
So, be careful uh with that. check uh
your data before you add any layout uh
to it. But the key uh for the rest I
think it can be really interesting to uh
u uh to use.
All right. The main focus of my
presentation uh was on the report
layouts. I also have a little bit of
PowerBI in here. Not will I will not go
into complete uh detail. That's not the
objective of this session. But I added
that in my PowerPoints because if you
have it then you have the full uh uh
picture. And for reporting that's also
really important. Why? Because I see
developers and partners and companies
spending a lot of time in developing
report objects and data sets.
They can't really reuse uh those. So
PowerBI might also be really interesting
to have a look at and it can do
everything. It can show detailed
information. It can also so show highly
aggregated uh uh uh information.
There is a lot of documentation uh
available uh online how to create and
get started with PowerBI uh reports.
Ronaldo and I have also given a lot of
sessions about that. You can always come
and ask us. We have some great learning
journeys too at Platan Companion. But
what I would like to show about PowerBI
reports is that using PowerBI desktop
can connect to uh queries or web sources
but queries are usually better. PowerBI
desktop is free. You build your report
in PowerBI desktop. You send it to the
service uh online and there you can
distribute and uh share a lot of
visualization possibilities based on
APIs because these are usually faster
than uh web services. In PowerBI desktop
get data you connect directly to
Business Central. You have all of your
data sets in there and you can get
started. Another way to get started is
online in the service by creating a data
flow gen one uh or one of the older ones
and the difference is that in PowerBI
desktop
I will uh have all the data in my one uh
report build the data model and have
have the report available. If you're
going to use data flows or a data lake
or something else then basically you're
going to fetch the data from business
central into a central repository which
can be consumed in PowerBI reports but
also Excel and other uh tools.
A few slides on that
onrem is also a possibility for uh
PowerBI
uh but okay if you would like PowerBI
desktop and the service online to be
able to find your onrem data it needs to
find a way to the server. So you might
need to install and configure that uh
PowerBI uh gateway
any kind of data model in PowerBI use
star or snowflake uh performance-wise
scaling and that's always the most uh
interesting thing to do the fact table
in the middle dimensional tables around
it if you need links in your dimensional
tables uh that's also possible data
model design part science part uh arts
and I can continue uh with some best
practices tips and tricks and so on and
I can create some really great looking
uh reports. Okay. Um we go to PowerBI
uh we can create reports like uh about
item availability
uh with the possibility to slice and
dice and drill down see some high level
information uh some uh trends
and some real details uh that they can
also have a look at and filtering the
simple reports that I have created. Um
what can we also do? We can create a
dashboard. Dashboard is like a
helicopter view uh on one or multiple
visuals from one or multiple uh reports.
So you can start with some high level uh
uh uh information
and if you click on one of these visuals
you will then be redirected to the
report where it's coming from. Um this
can then be also added into an app that
you can very easily share and
distribute. And then PowerBI can also
work with the scorecards. So simply
would like to highlight there are a lot
of elements available in PowerBI, lots
of different visualizations
and usually they remain in PowerBI. Of
course, we can embed those in business
central and there we see quite a lot of
enhancements uh uh uh coming in because
for example on the RO center or any
other page you can have multiple PowerBI
parts now linked to different uh uh
reports and there's also possibility
to not show a report but for example one
visual of a report a scorecard and also
a dashboard this can also be embedded uh
uh in here.
Now, if you would like to work with
Excel layouts or send the data to Excel,
interesting to know is that you can
export this uh into Excel.
However, uh if you have a report which
has an Excel uh layout,
uh you can simply open uh Excel and from
that Excel uh layout there's also
possibility to go into the data top and
get and select data from uh your uh
power platform for a PowerBI data sets
and so on. That's the reason I also
wanted to include this in this
presentation.
Okay, don't want to go too deep, but I
have some detailed information on uh the
slides. Uh but that was normally out of
the scope of this uh session, but you
can have some nice vis visuals in there
too. Uh last but not least, Microsoft is
also heavily investing in PowerBI. There
are a few out of the box uh apps that
you can also uh install. Uh these
include APIs, these include the reports
and also a setup that uh that you can
do.
All right to conclude um tips, tricks
and best practices. If there is one
thing I would like you to remember then
it is think about data aggregation and
data granularity. What level of detail
is required and based on that select the
best uh uh tool. So it's a fight uh
between the user wanting the details and
not having them in uh your uh reports.
Uh give power to the users. Think about
all of the different possibilities that
you have, all of the ways to consume uh
data coming from Business Central, but
maybe also from other uh applications.
There are a few online places where you
can find more information uh like uh
learn uh uh aka.ms/bc
reporting and aka.ms/b
uh for some more uh uh yeah detailed
examples. All right, I have one or two
minutes left. Any questions? Uh go
ahead. I'll give you the microphone.
Hi. Uh you mentioned that uh Microsoft
might have to drop
layouts if any security issues or
something arises. So in your opinion,
should we remake our uh let's say sales
invoice layout to use board and
sacrifice some conditional formatting or
is it fine to wait for? I think at the
moment is indeed come to stop investing
in RDLC and try to do it in the word
layout. The word layout is less
flexible. So that might require to put
that flexibility in a code instead of in
the uh the layouts. Yeah, these are
things I I highly recommend you to start
investigating so that whenever you might
have to do the move from our state to
something else that you are ready.
Thank you. Give you a t-shirt in a
moment.
Hello. Uh my my question is I guess a
bit of a addition to the question the
colleague asks here. Um, should we uh
recommend our clients that have like
more of a you know more of a higher
standard of security to completely not
use the custom layouts that they can uh
add themselves to the uh system because
well you can in fact add a custom layout
yourself into the business central you
you can still use them. Uh so um um in
the report layouts page and you can
start from an existing layout and create
a new based on RDLC based on the word
ones. You can still use those. I'm not
saying you should stop completely with
RDLC right now. Only I guess we should
at least limit Yeah, you should be
prepared for someday in the future maybe
not being able to use it anymore. I see.
So start your journey right now into
learning more about the word layout and
try to have the word layout replace the
the RDL. seems seems a little bit sad
for me at least personally for the DLC
like isn't wouldn't it be just possible
to just fix the port builder? Yeah, but
I think I think the problem is there
it's not not in the hands of the
business central team it's server team
and it's like old obsoluted technology
and and for them it's game over.
Hello Steven. Uh so uh my question is
also again in the same thread uh certain
things if we look at uh for example
sales invoice word layout it's more the
simplified version it's not as complex
as the RDLC yes so in future uh do we
look forward to Microsoft to having all
those features in word layout and second
question in the same thread is uh
certain requirements such as you know
having QR code in layout would that be
possible with uh the word layout codes
in RDLC we could also do HTML formatting
within the cell will we have those
features in word layout very good
questions and I will say right now it
can be very let's say challenging doing
everything in word what is possible at
ncia because word has many limitations
that's the reason I think why there is
no the word adden uh uh control which is
being added by Microsoft currently with
limited functionality however Kenny from
Microsoft is highly actively
communicating about that on the a Yammer
group and there recently he asked
feedback from everyone about what do you
need to be in the word layout what you
currently do in RDLC to be able to start
moving completely and based on all of
that feedback I think they will add all
of these features in that plugin I think
the end goal or ID is giving words via
that adden all of the things that you
need to be able to have them fully
replace the RDLC layout that's the idea
can come and fetch your your t-shirt was
um yeah so uh up till now I personally
used for uh I never used the data model
in in Excel but I used the power query y
so what's your thought about that what's
what's better or or is that a personal
taste or well I I like poor query a lot
because the pork query you have in Excel
is the same that you have in PowerBI
desktop and you can do ETL extract
transform data and then load it in
there. So with power query you get some
some great features in Excel. So what I
also frequently do is the data in the
data tab that comes in loaded into power
query do some calculated columns uh
clean up the data uh change the data
types uh so I highly recommend you to
use it. However, um when you generate
that uh uh the report, you might have to
click on that refresh button for
everything to to load or to reload. When
the Excel opens, normally it should go
automatically, but I notice it's not
always the uh the case. Uh Power Private
is also something you can use in Excel,
but I don't do it that frequently
because you can also create all of the
data models, for example, in PowerBI.
So, you can create a PowerBI report with
only a data model, all of the
relationships and the measures and the
calculations.
publish it to the service and then in an
Excel layout it also connect to that and
the advantage is that not only um you
have all of the power query from the
PowerBI report coming in but also the
complete data model and the
relationships.
