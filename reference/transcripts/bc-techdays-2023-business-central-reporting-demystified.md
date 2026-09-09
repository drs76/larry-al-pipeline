# BC TechDays 2023 - Business Central Reporting demystified

- **Source:** https://www.youtube.com/watch?v=aOJhUcNjeF0
- **Video ID:** aOJhUcNjeF0
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 94m50s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Uh, good afternoon everyone, and thank
you for joining to last session in room
number eight before closing.
Uh, my name is Renato, and I'm coming
from Croatia. I'm a business central
consultant and power platform consultant
plus F&O product owner.
Uh, also I'm a Microsoft MVP for almost
5 years and Microsoft certified trainer.
And today I will try to show you how you
can also use reporting
from, uh, let's say consultancy, uh,
point of view.
And while with me is Steven today.
Right. Thank you, Renato. My name is,
uh, Steven, Steven Renders from, uh,
from Belgium.
I'm still the MVP. I've been working
with, uh, reports for a long time.
And today we'll try to demystify
everything available in Business Central
regarding, uh, reporting. I will take
the more technical subjects, Renato the
more functional subjects. And we hope to
give you a a good overview.
Yeah.
Regarding our agenda today, what we are
going to show you is what are the
overall capabilities for reporting in
Business Central from, uh, some, uh,
basic things in, uh, Business Central to
some advanced in Power BI, uh, some
ideas and concepts. We will also show
you how one, uh, process of building and
report when I'm working with Steven
goes, so from an idea to the report.
Financial reporting, we all know that we
have this for a while in Business
Central and NAV.
And after that we are going to, uh, more
deep dive into coding of new reports,
extending existing one using data flows,
Power BIs, and so on.
At the end we are going to tackle a
little bit Power Platform.
So, how we can, uh, integrate Business
Central with Power Platform, with Power
BI, and embed those reports, uh, in into
different Power Platform components.
And last but not least, telemetry always
has a
interesting topic and hot topic. We are
going to show you what and where we can
find some, uh, telemetry for reports
that we are that we have in Business
Central.
So,
as a start, reporting capabilities. And
this slide is getting bigger and bigger
every time when I
show it.
So, we remember that in NAV back then we
had RDLC report layout that was
primarily built by developers
and usually it has a lot of ping-ponging
between
developers and consultants on how to
build a perfect layout for our
customers.
After that,
we received a Word layout in NAV as
well. It was like start of the Word
layout where we were able as a
consultant use Word to build some
layouts for our customers or for example
go on site and build it together with
our customers.
Latest layout that we have is Excel
layout that we are also going to show
you today where you can export your uh
uh data set to Excel and build powerful
reports like uh analysis of your top 10
customers and and so on.
If this three is not enough for you uh
using the Power BI uh using the
report object, you can use Power BI,
build queries, build data flows on power
uh in Power BI and analyze your data in
Power BI.
The newest uh topic that we have, of
course, and you already saw it in some
Microsoft presentations uh yesterday, is
data analysis
uh in list pages. So, where you can use
some uh analytics on uh list pages to uh
analyze your data and so on.
And last but not least is financial
reports that we have in uh Business
Central or previously known as
accounting schedules
uh in NAV.
So,
uh what is I would say idea and how we
are building a report. So, usually when
a customer is coming to us or
I have some an idea, of course,
I gather all requirements how I want
that this report looks like. And we will
show you today, for example, some
inventory by location, very simple
object.
After that, I sit with Steven and we are
developing data set. So, we are checking
what tables we need, which fields we
want to to use. Because, of course, you
don't want to
put a lot of fields in a in a data set
if you don't need it in your report.
After that, as a consultant, I'm going
and developing a layout
for
that report that we developed. And, of
course, then I'm choosing either I'm
going to Excel if it's some tabular or I
need it for some analytics later on
or it is some printout of our Excel
sales invoice or sales quote that then I
will have a in a Word or RDLC.
And at the end, as a key user or
consultant, I can configure layouts
in
a report layout selection in
BC.
So, that's like overall idea. And when
we are speaking about some financial
reporting,
we know that we have
a
concept or functionality called in
Business Central financial reporting
that is previously known as accounting
schedule.
And here we still don't need a developer
to build some
powerful reports based on general ledger
entries or budget budget entries. Users
or consultants will utilize their
knowledge of building rows or columns.
And then, they can
print those reports either in
PDF and so on.
Of course,
what some advanced users can use is
publish this data set as a web service
and consume it in Power BI.
Because we have our columns, we have our
rows, we can publish this data set to to
the Power BI
and build same report in Power BI.
And what we also have possibility is to
consume standard
uh Microsoft APIs
uh in
uh Power BI.
So, to build the same report without
needing to go to uh Business Central.
And this is actually what I will I will
show you now in my demo.
It's how to use uh financial reporting
in Business Central.
Okay. Uh um
My screen is on. Perfect.
Okay. When I navigate to Business
Central
and I go to my search and I'll find
financial reporting
or financial reports.
Uh
you will see a lot of predefined already
uh
financial reports that we can use
uh in Business Central as a consultant
or end user.
And as I said, each of those uh reports
uh consists of some rows and some
columns.
Uh okay, if I go to the definition, I
can
design my rows, so how they will look
like in
my printout. So, here I'm uh
I'm choosing my accounting categories
and subcategories and then I'm totaling
totaling them. And of course, I have to
specify what is the row type, net
change, balance, and date, and so on.
And of course, I can have column
definition where I'm tracking uh some
column information like current period
and and so on.
Okay. And that's pretty much simple
way how you can uh
define some report and then I will
calculate my figures.
Fine.
And I will print this.
Close.
Okay, and I see here that I received a
RDL C layout for my
for my report that I can now download
and send via via email to my colleagues.
Okay, so this is
the first thing that I wanted to show
you about financial reports.
The second one is publishing this as a
web service.
So, if I go to find
financial report
I will see here financial report KPI web
service setup.
Where I can specify details about my
report, so
for which period I'm
taking data.
Do I want to aggregate them by month or
whatever?
And at the end I'm specifying my row
definition. So, similar as I had in
my financial report definition
and I will publish this as a web
service.
I already did this for the sake of our
demo.
And now I will open my Power BI.
Okay, and here I will go to get the
data.
And when I find my Business Central
I will connect to my Business Central
online.
In a few seconds when I choose my
environment
Okay.
I will choose my company.
Under the web services a legacy one, I
will find
my Power BI finance web service.
And here I can now build for my
financial reports in Power BI. So, I
don't need to go to Business Central
and run reports from there.
If I scroll down, it will be some data
there.
But as we see here, we have some mark
that these web services are legacy and
then we want maybe to switch to
something new and advanced.
And if you are familiar, Microsoft is
building a lot of APIs to support
financial reporting.
And here under the Microsoft reports
uh reports finance beta, we can find
standard Microsoft APIs that will give
us the same possibility like we have
with financial reports, but just
consuming new APIs uh inside the Power
BI.
And also
You don't have to set up anything in
Business Central. They're they are out
of the box. Yeah. You have your master
data, transactions. You can build your
model in Power BI. A lot better than the
out of the box web services.
So, for example, I will select my
general ledger accounts,
GL entries, and I'll load those.
Just a simple report based on my general
ledger accounts.
Okay.
Go fast.
Okay, I will connect those two tables.
Account number, account number.
Perfect. One-to-many. Yeah, that's what
I want.
And here I can see then
account name.
And maybe amount.
Yeah. And I have my Power BI report in a
few seconds available.
Available for use inside the
based on the APIs developed by Microsoft
in my Power BI.
Okay.
That was all about financial reports.
So, Steven, now to you.
Yep. I'm ready to to take over for a
little bit to talk about the the report
uh object. And we need to mention it.
It's a reporting session, and sometimes
we still develop reports in Business
Central.
And when I deliver trainings about
reports, I always say that you need to
focus on creating the data set of a
report. That's really important. Besides
the data set, we now have also the
possibility to create and add not one,
two, three, but multiple layouts of
different types. But always start by
thinking about the data model before you
create the layout or the layouts.
And then last but not least, whatever
you would like to do with your report,
print it, email it, anything else, test
that, especially printing, margins, and
so on. It's also really important.
Right now, we have the possibility to
add three types of layouts. We have the
Word layouts, we have the RDLC layouts,
and we have the Excel layout. All of
them have their advantages and
disadvantages. And we're going to talk
about that, but we'll we'll come back
about that later in in this session.
Remember that you need to be a developer
or in the development environment to
create the data sets.
The rest you can leave over to someone
else. As a developer, of course, you can
also create
some layouts.
Besides creating reports from scratch,
we can also extend them, but
let me come back to that later.
Um all right.
Very quick demo.
Going to go here in my Visual Studio
Code, and we can very easily create a
few reports.
Let's have a look. They should be at the
top.
So, as a developer, what we typically do
is we start to create
the report from scratch using other
tools.
Um very important is that you think
about creating the data set. You can
have one data item, multiple data items,
you can do a join, a union, a
combination of both.
Uh whatever you do, test it, run the
report until you see the request page,
export the data to Excel,
so you can have a look at what the
report actually does. And here we have a
simple example, GL accounts and GL
entries. Don't forget the data item
link. You will only forget it once.
And you can very easily create a view
uh
or get some data.
Then, lately, uh small change is that we
now have a rendering section where you
can add multiple layouts, uh type Excel,
Word, or RDLC.
You give them uh very nice description
because that's what you will also notice
and see inside with a central when the
report has been published. And for
example, someone would like to add a new
or another layout.
Here, I'm keeping it to Excel layouts.
But also have created a few other
reports with different types of of
layouts. And here we have Excel and
RDLC.
And choosing the type of layouts is
actually not that easy. Depends on a
number of things.
Um
and
it goes in both ways. So, on the one
hand, you start to create your report,
you create the data set, and based on
that, the layouts. But if you know in
advance that you're going to create, for
example, an Excel layout, you might want
to create a data set in a different way.
So, depending on the layout of the
layouts that you would like to create,
um the data set might need to be
modified a little bit.
Then I also have another example, a
report,
some shipment information
where I'll have a also a Word layout.
We're not going to spend a ton of time
diving into how to creating these these
layouts, but I can show you exactly how
to create a simple RDL or RDLC layout. I
can dive into document reports and talk
for hours about get data, set data, and
why that's so much fun to maintain.
Uh I think we all know
that. But it's important to know that
you can now have multiple uh layouts in
one uh reports.
All right.
Um creating the Word layouts, I can show
that.
Because if you have to choose, for
example, in the future
uh to go, let's say, RDL
RDL say or Word layouts, then
most of us would recommend to go uh for
the Word uh layout. So, I think it's
quite important to know how that works.
So, you create a Word layout
and the data set. You add a Word layout,
the Word file is created and um you can
very easily
uh open it.
Now, I was never really a big fan of
using Word to design anything.
Uh I remember that from when I was uh
studying in school and had to do my uh
my thesis in Word.
And every time I changed something,
um well,
the layout was was not how I saved it
previously. So, when Microsoft started
using the Word layout, I was not that
enthusiastic, but there are a number of
advantages.
You can see your data set here to the
right side.
In Word, what you typically do is you
create an element. For example, you go
and insert
a table. You have to know a little bit
in advance how much columns and rows you
would like to to use. Keep one row for
the the labels. Keep one row for the
data that needs to be repeated.
And then, uh you select the row that
needs to be repeated. And for example,
for the data the item would like to
connect to it, you can simply add a
repeating.
So, there is no clicky clicky draggy
droppy in the Word layout, but it's not
that extremely difficult to uh to
create. And what is actually very
interesting
is that, that's what I wanted to
emphasize in this demo, is that if you
have another data item,
right now we have the sales lines joined
with customers, but imagine below that I
have something else, uh vendors or or
company uh information in a separate
data item, then I can put that separate
data item
very easily in a separate table in the
layout without the need to apply a
filter. That happens automatically in
the word layout.
In RDLC, we can also create two tables,
link it to two data items, but then you
have to start to apply filters, which
makes it quite complex. So, quickly
wanted to demo that.
Now, once you have your reports,
you have defined them as a developer,
and you publish them into Business
Central, then users can go and also
change
and add layouts. I'm going to do my demo
that a little bit later. So, I'm not
going to do it right now.
After a while, you might notice that
users might want extra fields in certain
reports for the layouts they would like
to to add.
And that's something a user cannot do. A
user is not able
to
add fields to the data set of of a
report.
So, Microsoft created recently the
possibility to add a report extension
object that you can use to add fields to
existing data items.
That's why I would recommend you to to
use it.
Now, you can add columns to existing
data items. You can add new data items.
You can also add code in certain
triggers. You can make modifications or
add stuff in the request page, and you
can also add a report layout.
How does that work? Well,
I think the idea is very good.
The implementation of it has a little
bit room for improvement, but okay.
So,
I have a report here, very simple data
set, customer sales,
uh with information from the customer
table, I have data item customer uh
ledger entry.
Quite simple. And I have another one
here, customers and vendors. So, two
data sets, my examples of a join, and
second one here, uh uh union.
We can very easily extend these uh
reports by creating
a report extension uh object. The report
ext, uh you create one, and then in the
data set, you can say what you would
like to uh to do.
For example,
here I'm adding
a field uh city to the customer data
item and currency code to the customer
ledger entry data item.
Nice and simple. I can then deploy this
uh object uh even without a a layout.
And uh the fields will be added in the
data set of the original uh report, and
users can then start to use them uh when
they create their own uh layouts.
If I would like to, then I can also add
uh a layout myself. Okay, here I'm using
the layout properties. I could also use
the rendering uh section, of course.
Customers and vendors here,
I'm doing something uh special.
Um
let's also have a look at the original
reports.
Customers and vendors here it is.
So, in the original report, we simply
have a union of the customer and the
vendor uh data item.
Here in the customer data item, I'm
adding city. Vendor, I'm adding city.
And then,
after vendor, I'm also adding a new data
item because they also also wanted to
have contacts in there.
So, what what I would then expect to
happen is that in the data set, another
union, a new data item will uh will come
in. Well,
that will happen, but maybe not as you
uh expect.
Let me go to Business Central. I have
already deployed that report.
If I go to the report layouts,
let's have a look at my
report extension customers and vendors.
The original, I'm quickly going to run
it.
Actually, no.
This one.
And then send the data to Excel.
A very nice feature if you check the
data set at runtime. I can only
recommend to use that.
Although I should have selected
the one without
the layout.
Voilà, data only.
Let's open the Excel file. All right.
So, what we basically see here
is the original data item. So, I have
the customer data item.
And then I have the vendor, oops, data
item.
So, that's, all right.
And let's say vendors start about here.
That's typically what happens when there
is a union of two data items. Now, via
the report extension, I also added
the contact data item. So, I was
thinking that, okay, the contact data
item, new columns, the data will be
filled in at the end. But, um, it is
not.
So, as you can see, the contact data
item is added in the data set, but at
the same level where you have vendors
because I did at last to to the vendor.
So, that might not be the data set that
you expected.
So, be careful about that.
Now, another situation where report
extensions can be interesting is, for
example, to extend document reports. So,
here I have a small example of how you
could extend the sales invoice report
because a customer might ask you, "Okay,
I would like to be able to see the order
number of the invoice on the documents
will be printed out."
Very simple. You add
something to the line data item, in this
case the order number label and the
Boolean to decide if you
would like to display that in the layout
yes or no.
In the request page,
Boolean, voila, that's it.
I can publish this. The field will be
added to your data set of the original
report, fine, and we can use it.
However,
that's why I see some room for
improvements.
Um if I now also would like to myself as
a developer add the new layout, um how
can I get the original layout and add my
fields to it? If I simply add the
property here on the report, do control
shift B, repackage, the layout will be
created for me, but completely empty.
And I don't want to recreate that
invoice layout from from scratch.
So, if you'd like to reuse the existing
layout,
add your fields to it, what's the
process right now? Well, you have to go
inside Business Central.
You have to go to the report layouts or
the report layout selection page, but
that page will disappear.
And there you have to look for the
existing report. So, in this case,
1306.
You select, for example, the original
layout. It can be a the RDL layout, can
be the Word layout.
And from here, you need to export that
layout file.
So, we get the RDLC or the Word layout
you exported. Okay, you know where it's
saved, you copy it to your Visual Studio
uh code folder, you rename it, and have
the original layout. Then
you do a control shift B to add the new
fields in the original layout that you
copied, and then you can modify it and
add it in the in the layout itself how
you would like to. And then you
republish.
So, a report extension to add fields
to an existing data set, okay, but with
a layout, uh the process is quite quite
cumbersome. It can can be done.
So, there are some advantages and
disadvantages about report extensions.
However, you need to be careful what
you're doing because this can and will
happen.
Um
you need to know which report you are
extending. Uh host like you see here on
the left adding stuff on top and on top
and on the sides,
uh it might work in the end, but not
produce the results that that you
desire.
Adding data items the wrong location,
you might not be able to use them.
And even if everything works, uh the
host at the right, okay, it works, might
not be uh very pleasant to to live in.
So, be careful with report extensions.
You need to know what you're extending
and how that data set looks looks like.
Personally, in many cases, I think you
might get a better result if you simply
recreate, clone the original report, and
work with that.
All right.
I have the contacts, for example.
Okay.
Perfect.
Now, um
the reports and the layouts. I talked a
little bit about the Word layouts.
You already have the Excel layout, and
we're really going to dive into that. I
can if I would if I want to, but might
not be that relevant relevant anymore in
in the future.
So, what I'm going to do is I'm going to
uh provide you with a link with some
extra information, aka.ms/bcreporting.
Some very good documentation that
Microsoft assembled to learn everything
there is to know about about reports.
But I would like to spend some time on
the Excel layout. And for that, we're
going to switch back to Renato.
Thank you, Steven.
Okay, so we have our data set ready, and
we can build now Excel layouts. An Excel
layout is something that came recently
to Business Central
Business Central world, where which is
the third option how you can use layouts
with current and or existing
uh reporting capabilities. So, once
Steven built the data set, I can use his
data set and build various
Excel layouts uh on top of this.
What is very interesting is that you can
combine
uh data set from uh report object with
external data sources. So, for example,
if I want to connect to SharePoint list,
or I want to extend report that I
already have with some APIs from
Business Central, I can easily do this
in a in Excel.
Uh when I have my data set ready,
I can build Power Pivot tables and
charts and so on, and do analytics
inside the inside the Excel.
And of course, I can use it for some
post-processing
uh like forecasting, analyzing my data
set with standard Excel features.
And of course,
telemetry here goes into hand as well,
where you can track what uh reports your
clients and customers are using
uh
in Excel layout, so you can maybe uh
some improve some
give them some improvements and so on.
So, here I will then jump to to my demo,
where I will show you how you can
use Excel layouts in inside the Business
Central.
Okay, so let me go to BC.
Okay, and uh here under the Business
Central, I will go to report layouts.
And I can see all my report layouts that
uh Steven already built.
Uh and we have a Microsoft one and I
have my filter already ready. And here I
can see a lot of
uh reports that are already uh enabled
uh within our extension.
And on the right side I find Excel
layout. And for example, if I choose
this item availability data only,
I can run this report.
And as you can see, one of the
uh
changes or differences from Word or RDL
C layout is that you cannot preview our
data or you cannot print it.
So, you just need to first download your
report.
And then here you will get your
uh
item availability report
within the
Excel.
Okay, it's already here.
So, and here I can see my data sheet
with contract. So, uh this table is
called contract, where you can see uh
data uh from from data set
of the report.
I'm sorry to interrupt you,
Renato.
As a developer, I can also do that. So,
when I create my data set, then add an
an Excel layout to it. As a developer,
you can repackage. The Excel file will
be created, but it will be empty. There
will be a data sheet in there with the
columns, but no data. So, then the
developer I'm kind of stuck to to
continue. But then the application you
can get the data.
Here on the right side when I return to
the Business Central, I will see from
which extension or base app this report
is coming.
And for example, this uh
item availability that's coming from uh
extension,
I have problem and I will not be able to
delete it. So, I can only delete user
created
layouts or that are in the Business
Central.
Okay, but I will return now to my Excel.
And as I said, here I can do whatever uh
I want uh with
So,
I will just insert pivot table. Where it
is?
Sorry, I don't like this
tables, pivot table.
Data and the new worksheet. I can
My Excel doesn't like me today.
Okay, so let me see if I can search for
the fields.
It is item description and quantity.
It will not open this.
Okay, so what I can do, I will now show
you on one of the examples that I
already prepared for you.
So, in extension, we have some charts
here and I will run this report.
And I can click download.
Okay.
I will get my item availability, but now
with some
charts and already prepared
pivot tables and pivot charts in the
Excel.
So,
again, here I have my contract and I
have different sheets within the Excel
workbook with information about my
my data.
So, this is a layout that was developed
from scratch by my developer. But if I
want to extend, for example, existing
reports, such as I don't know, customer
top 10
list, I can do this as well within
as a as a consultant or as a developer.
I can see that here I have only RDLC
report, but what I can do is
send to
and send data only to to the Excel.
I will click
And now I'll get my top 10
customers.
Okay, I'll click enable editing.
And now I see here that I have report
metadata, which I don't
And I have a lot of columns that as well
I don't need in my my report when I'm
using
Excel layout. So, for example, I will
just keep number of customer number,
name, sales and balance. And all these I
can delete.
So, I have my
data contract now here.
I will save this. And what I can do now
is also enrich this report with some
with some APIs.
Which what?
Be careful, Renato. You can delete
columns, no problem, but you cannot
rename existing columns or start to move
them around because then you might break
the at the contract.
Okay, I removed. And now I will just add
some OData feed.
And I here here I have one of the
APIs for my customers.
And in a seconds I will get my customer
information, customer details
inside my
Excel. I can transform this data.
Okay, and I have customer details.
And then I'm loading this into my
workbook.
Okay.
Okay, now I have my OData query. I can
do refresh if I want and so on.
Or I can build
query
Now if I'll
be able to see
to move it.
Now just a second, data
from table,
from table range.
So, I will get now my customer details.
So, this is my API and this is my
uh data set from Excel layout.
And I can merge those two queries
into new one.
So, I'll save my customer
customer details.
Okay.
You know this.
And then I'll be good.
Okay.
No, it doesn't work.
Okay.
It says that uh it must be the same uh
column type. So, this means that I can
convert this to uh text and then combine
those two
uh
tables, join them, and uh use them in my
uh Excel layout.
Okay. Uh I'll just delete this.
Now, when I save my
Excel, I want to consume this inside the
Business Central.
I click close.
And then I can go to my
report layouts page. I'm already here.
I will find my report. It is somewhere
around 100 and
11.
And I'll click create a new layout.
Okay, I will use customer
top
10.
API.
Okay.
And then I will choose my customer top
10.
Okay, and now I have my new layout for
uh my customer top 10. If I run it,
and I click download,
Come on.
So, actually, if I would like extra data
in an existing report and it has an
Excel layout, you need a report
extension. You just need an API or web
service. And in the Excel layout, you
use Power Query, connect the data.
What we can also specify is that on each
Odata we can have automatic refresh once
we open the Excel. So you don't need to
go to a manual refresh inside the
inside the Excel.
Good.
Uh
that was the Excel layouts.
The next step that uh is Excel look like
is data analysis on the list pages in
Business Central.
So the new feature inside the Business
Central where you can interact with your
data on
um
and have a report like like in Excel.
Uh you can group your data, filter data
based on the available fields in uh in
Business Central, or set some filters.
And what is also very nice and cool
feature is that you can uh
pivot and uh save those views for
another reuse.
Also as a client we can track this in
Power BI uh in in telemetry to see if
our users are using uh
data analysis on the list pages.
Uh how this uh we can enable and use
inside the Business Central, I will show
in my demo.
Uh when I navigate here in my
Contoso USA into feature management.
Here I will see uh feature preview
analysis mode quickly. Analyze the data
directly in Business Central and you can
enable it
for for your users.
Once it is enabled,
I'll just switch to another company
where I have more data to show you.
I will have possibility to analyze on
any list pages.
Come on.
Okay. For example, I will go to my item
ledger entries
where I have a
lot of entries.
And here, when I turn it on,
I receive a little bit new view,
and in a few seconds, my analysis will
be ready to to use.
Uh I see that here I have some
on the right side
uh columns from my table.
I have my location code, and I have my
my values as well here.
I can always remove this
and have it
item number here,
and then see all my uh
detail ledger entries for quantity,
or I can add some new,
for example, remaining quantity. Oh, it
is already there.
So, here you can also have multiple
fields that are summing up our
values.
Okay, and now I have also my remaining
quantity as well.
Good. Uh if I want, I can turn on pivot
mode and have a little bit different
overview on my data, so I can have my
rows items, values are my remaining
quantity, and I want I'm interested in
my inventory per location,
where I can see uh what is the quantity
and remaining quantity per my
warehouse.
Uh
after that,
uh I can
copy this data, I can export to CSV or
Excel.
I can rename it, duplicate this view,
and then uh do some another
modifications, and so on, or I can move
or left.
Uh
I can specify filters, so if I'm only
interested in current year or previous
year, and what I like to use is that, of
course, that we have also drill down to
month, quarter, or
year as well here.
Good. This is the analysis in Excel uh
in list pages.
And now I'll return
presentation and we can go to Power BI.
All right.
Now the analysis view on these pages, I
think it's really cool. Now we have the
Excel layouts. Now we also have analysis
view on uh uh in list pages.
Um and it's only in preview, as it will
be coming a lot more. Maybe also even
the possibility to export to uh to
Excel. Yeah, that might be coming.
All right.
Now also I'll talk a little bit about uh
Power BI. That's one of the other tools
tools that uh we have available to
create some some reports. So um we have
a few topics that uh or scenarios we're
going to cover.
First,
how to get data into Power BI. Uh what
do we need? Uh then
some nice things we can do uh with Power
BI. You can do multi-company,
multi-environment, multi-fact.
Data flows are interesting.
Getting the data back in Excel from uh
Power BI.
A little bit of an information about
what's coming. Uh Fabric uh and Copilot
in Power BI. Then incremental refresh,
which is usually kind of uh
an interesting feature to investigate.
And then how to embed Power BI reports
back into Business Central.
Now to get data in Power BI, we need
data or a way from Business Central uh
to uh expose that. Currently, we have
like two possibilities of data uh web
services and APIs. Both are based on
query objects and page objects.
There was a a poll, which we'll come
back to uh later uh on this session,
where I asked uh what you guys were
using
uh as data sources in uh Power BI. And
well, the answers weren't always as I as
I expected.
But personally, I always prefer to work
with API uh queries. They should give
you the best uh performance.
API pages are also uh okay. But I would
recommend not to use web services uh
anymore.
All right. Now, if you'd like to know
which APIs are available, there's a link
in here. You click on it, you go to the
Microsoft documentation. On the left
side, you can see the the list. Now, out
of the box, we have some very good APIs.
Most of the master data is there. The
transactional data, posted, non-posted.
Some model data, but there might also be
a few things missing. And for example,
last time I checked, I don't think there
were any available out of the box APIs
about manufacturing or production data.
On top of that,
um you can also have a look on GitHub,
like Christof explained yesterday in his
session. Have a look at the original
code, which is being used to create
these these APIs. And you're going to
notice that most of them are all page
APIs.
Now, in real life, when the standard web
services or APIs aren't sufficient for
Power BI, then you have to create new
new ones because the existing APIs
cannot be extended. So, it requires a
little bit of development. I imagine a
situation, you have added the shoe size
on the customer card.
You also want that in Power BI, but with
the existing APIs, you won't be able to
do that. So, you have to create a few
new APIs.
So, let's quickly see
how that works.
Go to the correct project.
I have a project here called the Power
BI APIs.
I have a few of these APIs that I
created, which I divided into master
data and transactional data.
Now, before you even start to create
these APIs, APIs are so very similar to
a data set of a report. So, if you know
how to work with data items, you can
create APIs very very easily. But, you
should know
what you want.
And in reporting, that's always very
difficult.
You can create APIs
um especially or designed for the
reports in Power BI that you would like
to create. So, for example, if I would
like a sales uh dashboard
in Power BI, I can create one query and
that gets all of the data in Business
Central, groups it, aggregates it, and
makes it available for that Power BI uh
reports. The next report I would then
like to create, okay, I can do the same
thing over and over and over again.
I don't like that.
I do it the other way. I first create a
whole bunch of smaller uh API queries,
which are like little blocks of Lego
that I can consume in every Power BI
report that I'm creating. Usually, the
difference between two Power BI reports
is the fact table. Uh the other tables
in the data model are usually the the
same.
So, right here I have a few very simple
uh queries, an item query which fetches
item information. Why did I create this
one? Well, because the out-of-the-box
item query uh didn't have all of the
fields that that I needed. So, it's
really not rocket science to uh do this.
The difference between a normal query
and an API query uh is basically uh the
bunch of properties uh that you see here
at the uh top.
What you define there
is also will define where we can find
these if you're importing in uh Power
BI.
One thing I would like to emphasize
is this property.
If you're creating a query,
then your goal is basically to read data
from Business Central. Well, indicate it
with data access intent to read only
because then your query, when executed
in Business Central, will go to a
replica of the production database, not
the production database.
And the replica of the production
database is kept in sync. It might be a
few milliseconds behind. Then your Power
BI reports will not be blocked by any
locks that might be in the production
database. And also, while the Power BI
report is refreshing, you will not block
any other users.
You can do this
for all APIs, query APIs that you can
create, but also for reports, for
example.
Should be some real performance
improvement.
Besides that,
I highly recommend to think about the
granularity of the data that you need in
Power BI.
Um usually when you fetch data from
ledger entry tables, you're going to
import it into Power BI, then group by
this and group by that and calculate
subtotals. So, why not do that in the
query?
Simply implement some method or another
kind of method on your numerical fields,
and automatically you will get a group
by all of the other columns, which
basically is going to reduce the size of
the data set coming out of BC and going
to Power BI.
It will improve the refresh times. What
What I see also quite a lot is people
fetching all of the data without any
grouping in the query, importing in
Power BI, and then grouping there, which
in my opinion makes no sense.
One thing I've also seen at the customer
is that if you do this
and you do not notice any performance
improvements, it's usually because
someone added the entry number in here.
If you group by the primary key, you
will not get any aggregations.
So, you can create a whole bunch of
different queries. I have a few master
data queries, there are some other
queries that I might might need. And you
can simply publish them. You can do some
joins in here and interestingly is that
in a query
you can define the SQL join type you
would like to have.
For example, I'm not going to
change it here, but there are a few join
types we can choose from. We cannot yet
do that in reports.
All right.
So, I have my project. I simply publish
it. I make sure all of my APIs are in
same API group and I can find them quite
easily. You can also version your APIs
so that in the future if you would like
to make a change, don't want to break
any existing reports, you simply create
one with another version.
What should you create? Query APIs or
page APIs? I prefer query APIs because
of the grouping.
In page APIs, you can also join tables
if you work with the subparts, but
that's a little bit more difficult to
create and grouping aggregating isn't
really possible. That's why I personally
always prefer to work with a query APIs
because you only need to read data.
Existing page APIs are fine, but in the
existing page APIs are there's also a
lot of code foreseen
in case when they're used by Power Apps
or Power Automate and they're inserting
and modifying data. For Power BI, we
don't really need all of that overhead.
So, less is better for Power BI.
Once we have our APIs, we can very
quickly go to Power BI and start
importing data.
So, let me do that.
By launching a new
Power BI Desktop.
I already have a few open, so
All right.
Now, in Power BI Desktop, there was this
get data button that you can use if you
work with Power BI, you already know it.
You go to more online services.
That is Business Central.
For BC SAS, I usually use this connector
for BC on prem. I tend to use the OData
connector. It depends a little bit.
You connect to your environment. Inside
your environment, you will see your
companies. Inside the companies, you
will see what you have available to
connect to.
I will take the Cronus USA company.
And then my Sorry.
Custom APIs that I have developed are
available here in advanced.
Without the Solutize ones,
and I can see them.
Not going to build a whole report. I
have already done that, but let me take
one of these and then hit the transform
button to import the data in Power
Query.
In Power Query, I can see my items. I
can do a few transformations if I would
like to.
However, my goal was to talk about
multi-company and multi-environment. So,
how can I turn this into a multi-company
multi-environment query?
Well, you might notice in Power Query
that there are two steps that were
executed by default to import the data
in Power BI, and we can simply go back a
step.
And here we see
the environments. So, can we do
something with that? Of course, we can.
I'm going to delete the second step.
And then
I'm going to keep the first two columns
and remove the other ones. So, I have
now my environment name and a data pane
that I can expand.
Going to do that.
And wait a few seconds. Now I see
something else, which is interesting, my
companies. So, I have all of the
environments, have all of the companies,
and still I have the
rest somewhere here in the top. I can
expand the data top. So, again,
I'm going to select these three columns
with control, remove the rest.
Here I can say
this is environment.
You can type in the demo key, and here
it is company.
Voilà.
Before I continue, I'm going to filter
out my company. Or maybe other
evaluation companies, because that's an
empty company, and from no one that will
give errors in Power BI or in Power
Query.
Voilà.
I can now expand the data top again.
And then I will need to do a few more
conversions, and suddenly I will see all
of my web services, advanced APIs, and
standard APIs appearing. But then in a
multi-company, multi-environment
way.
We have my environment, now company. I
can see the type of API.
And data. Going to remove the rest once
more.
Voilà.
So, I can choose choose standard APIs,
web services, advanced APIs. Let me go
for the advanced ones.
Voilà. And then expand again.
I have documented this also on my blog
step by step, so
no worries. You can play play back the
recording of the session, too.
Once you have done all of these steps,
you can save this in a Power BI
template. Next time, simply start with
the template.
It's taking a little bit more time,
because it's getting all of the advanced
APIs.
In a few months, it will show those in a
list. Voilà.
Environment, company.
And then
where Where the data top?
And maybe also the name.
Remove the rest.
Do it differently.
Environment, company.
Name, data.
All right. Now, I will go for my APIs.
I can also leave the rest if I would
like to. Expand this once more.
And I have what I would like what I
wanted.
Now, remove other columns again.
Now, I get a list of all of the APIs
that I published, but I have the
environment name, the company name.
What do I do I do now? Usually, I'm
going
not load this in my data model. I'm
going to give this the name, for
example, APIs.
And then I'm going to start by
referencing this query.
Into a new one where I, for example,
then I'm going to say I only would like
these items.
Love this will be my items.
Query, I can now expand the data. I will
see coming in all of the column names.
And I have all of the data from the
items API I created, but multi-company,
multi-environment.
And later with a little bit of Power BI
or Power Query skills, you can also
create parameters for the environment
and for the company. You can even leave
in the parameters to choose the
environment. It will show you the
available companies. And you can filter
this also in Power BI.
We close this.
And I've used this
in a few other reports that I have
created. So, we have a simple example of
an inventory report where we are
fetching
some information from Business Central.
It's not really the best data model, but
okay. And we have the items here in the
middle connected to the item ledger
entries, the purchases, and the sales.
Because besides the inventory by item, I
also would like to be able to calculate
the availability, and then need to know
what's in sales and in purchase.
Interesting about this report is that it
is multi uh company. So, I have filtered
this on one environment, and I can get
the data from one or multiple uh
companies.
Very simple to uh to
And we can create a few measures and so
on.
So, I have some stock information,
some availability uh information, um
items by location. Okay, I also have an
RDLC report with the items by location,
but I like this a little bit better um
because it's also much very uh dynamic.
There are also possibilities to uh build
in
Where is it? Drill-throughs. So, if I
right-click on any of these uh numbers,
I can do a drill-through, uh go to the
details, and see where that number uh
comes from. Very simple to do in uh
Power BI, like a flow field
in Business Central.
So, that's multi-company, uh
multi-environments.
I've also created another report, which
is basically a finance report. Let me
quickly go into that one.
Here I am.
Um so, in very much the same way, I have
a report here with some uh general
ledger information
linked to accounts, I like an auto date,
uh a date table generated with a script,
and a few uh measures. And I can see the
amount, amount last year. I can compare
those on a monthly, uh quarterly uh
basis. I create some some other
measures, expenses, income, and so on.
Very easy to uh
to look at the data, data
year-over-year, some details, some
actuals.
We can do that. This finance report we
can actually create with the finance
APIs Microsoft created. Don't need any
custom APIs.
Now,
what is a little bit more difficult in
Power BI, but not impossible, is the
following: multi-fact data models.
In Power BI you would like to learn from
your data. You would like to compare
data. For example, you might want to
compare actuals with budgets. In that
case, you will have a not a snowflake or
um
a star uh data model, but multiple fact
uh tables. Which is, if you start to do
uh Power BI, exactly that what every
course is warning you not to do.
Multiple fact
So, uh we have our finance, GL, or sales
invoices
linked to customers with a date table,
but now I also would like to compare
this with a budget. And we have two fact
uh tables.
How can we get this to work?
Uh let's have a look.
So, I have this data model uh here,
exactly what I had on my uh slide.
I have my budget data that came from uh
Business Central. There was no table
relationship. I just have the data in
here. I have some measures. I have a
sales measure,
uh which is simply the sum of the amount
in the sales table. I have a budget
measure, which is simply the sum of the
amount in the budget table. And now, as
a clever Power BI person, I'm going to
add that to a nice matrix.
And I check my data, and I see, okay,
that's not really uh correct, because
the budget is actually 500 per month per
customer. That's what they added in uh
in Business Central.
So, how can we get this to work? Well,
you need to know a little bit about
granularity.
That's quite important. Um
what is the granularity of the data in a
Power BI report? It's the level of
detail that you have in there.
So, if you have unaggregated
data, you have a lot of detail
in there. Um
you can show a lot in Power BI, but the
report will be a little bit slower.
Uh the higher the level of aggregation
you have in there,
the faster the report will will be
there. But granularity is very
important. And to be more precise, you
need to understand the granularity of
your fact table and maybe also other
fact tables. And in this case, that's a
that's a problem cuz when I look at the
finance or the sales table,
I have that by day, multiple entries by
day, but in the budget table, you
usually have it by month.
Very rarely I see budgets per customer
per item per day. No, usually it's per
month. So, the granularity of these two
is a difference.
So, we need to try to figure out a way
to to link these two tables.
There are a few mechanisms that we can
implement. We're going to go relatively
quickly over them.
The first one is try to reduce the
granularity on all tables. For example,
um
group the sales table so that you also
have the data by month. You can connect
the fact tables
and it will work.
Another solution is to use a little bit
of DAX. TREATAS might be an interesting
function to to use. Third solution is,
okay, maybe we can add a table in the
middle and simulate star or snowflake.
And then the last solution might be to
use a little bit more DAX and
recalculate the budget so we also have
it per uh per day.
So, let's see how that uh it
Our first solution.
Look, I'm looking for report number two.
Yes.
What we have right here uh is a report
that uh looks a bit uh nicer. Uh we have
the uh
actuals versus budget. The budget seems
to be uh correct at 500.
As I entered it in Business Central. And
what happens? Well, we played a little
bit with the relationships. So, what you
see is that we linked the budget table
to the customer table using the customer
number.
And we also linked the budget table to
the date uh table uh using the uh month
number or budget date fields actually.
Okay, then we do some clicky clicky,
right we droppy, we create a visual, and
it seems to work. But, if you inspect
this a little bit uh closer, um at some
point it will no longer work.
Why?
Because there isn't really a link
between the budget and the sales
invoices. So, depending how you're going
to group your sales, you will not see
any data anymore. On top of that, the
budget date is always the first of the
month.
If you're looking at the second of the
month or uh you will also not see um
anything good. So, okay, this might seem
that it works, but uh it doesn't.
The third solution
is actually not a very bad solution. As
you can see in the data model, um
nothing much seems to have changed.
There is still no link between the
budget table and the uh sales uh table.
However, if I look in my visual,
uh the data is calculated correctly.
And the sum is also calculated
correctly.
Always two checks you need to do in
Power BI. Do I have the correct data and
do I have the correct sum?
Okay, so how did I do that? Well, a
little bit of DAX. It's a relatively new
function
but not so extremely complex. The sales
is still calculated the same way, sum of
the amount in the sales table, but the
budget table is calculated a little bit
differently.
And if I do more, I can show that
properly.
What are we using here?
I am calculating
the sum
of the amount in the budget table.
And then I'm moving over filters that I
have on the invoices table to the budget
table. So, the filter on customer number
in invoices will also be filtered
on the customer number in the budget
table and so on. So, treat as
is a function that you can use to move
filters from one table to another table.
So, you can create kind of a virtual
relationship between these two tables.
Very interesting, very powerful
uh function and uh it works.
So, it gives me that uh possibility to
visualize my uh my data.
Only one problem. Um it will move
filters from my sales table to the
budget uh table.
But again, I can still only see and
calculate the budget by months.
Right? If I would like to go any level
deeper, it uh it will not uh work.
Are there other solutions? Yes, of
course.
Let's have a look at another uh solution
uh here.
Okay, I'm still seeing the budgets um
calculated correctly by uh months.
And this solution is by adding some
table uh relations but in a much nicer
uh way.
Using a table in the middle.
And to be able to um move filters from
customer uh some uh sales to
budget and the other way around. Now,
this table basically is using the year
months
because in my budget table
I calculate a column year months.
In the date table, I have that too, a
little bit lower here.
And I use it to create a relationship.
So, I can link basically the budget via
the year months in the date table and to
the sales table and also via customers.
So, I can slice and dice in both
directions. This year months table is
not so difficult to create. You're
simply
doing a union of the year months you
find in the budget table and the ones in
the sales table. Voilà, the table is
created and auto updated.
Okay, it works. You don't need any
special DAX now to calculate my
budget
like in the previous
example. Simply the sum of the budget of
the amount in the budget table and also
get the get the result.
It works. Although personally, I don't
really like this solution because I
always, in each and every training, a
Power BI meet report needs a star or a
snowflake data model. One table in the
middle and some other tables surrounding
that. This is not a star or a snowflake.
So, not really highly recommended.
As again, this data model also doesn't
allow you to go lower than on a monthly
basis to calculate and compare budget
and and sales.
Okay, we have another solution that we
can have a look at and here
you notice the budget is calculated,
but it's a little bit lower than usual.
But, I have the possibility to go on a
day level.
So, this is an example of a Power BI
report where I'm going to recalculate,
reallocate the budgets. Uh I have a
monthly budget, but I'm going to
recalculate this into a daily budget
depending on how many working days there
are in every month.
I stole or borrowed this solution from
Marco and Alberto sqlbi.com, the DAX
gurus worldwide. So, it is not my
solution, but I like it quite a lot.
The data model is uh a lot better. You
see it's still
better than the previous one. And these
two tables
almost like a like a star.
In the date table, we simply need to add
something so that we know if uh a day is
a working day, yes or no. We're simply
saying that the weekend are not working
days, but you can make it a lot more uh
complex with holiday tables and and so
on and
And then, we need a few uh measures.
The sales measure is uh still the same,
sum of the amount in the same
invoices table.
Um there's another measure that uh we
use basically to see do we have a budget
in the budget table that we can use, or
do we need to recalculate it on a daily
basis, depending on how you're looking
at the uh budget.
And then, the simple measure uh of the
budget itself.
Not going to go into detail, uh but
basically, this will reallocate,
recalculate the budgets depending on the
number of working days in the month that
you are looking at. So, we can calculate
it by day, too.
Once you have that, you can also very
simply calculate the variance between uh
the two and display this uh this data.
Okay. These were a few examples of
things you can do in uh in Power BI. I
have have more that that I can show.
But, just to show you that again with
Power BI, we can do quite a lot.
That's is, let's say, a bit more
difficult to do with
uh data sets or report objects, or uh
maybe even Excel layouts.
Besides that,
um I have a little bit of time left,
Renato? Yeah. Okay.
Um I also would like to cover data
flows. Cuz everything that I've shown
you right now is what I can do with
Power BI. But
um
the poll also showed that not everyone
is using the data sources I suggested.
They might be using data flows or
something else, too.
And what's the problem?
If you have
a few Power BI reports like you see here
on top of my screen and all of them are
connecting to a Business Central and
refreshing, what happens is that all of
the tables and the points of the star
are simply importing same data
from Business Central at the same
moment.
That's inefficient. Um actually, the
data like master data
should only be fetched once from a
Business Central, kept somewhere, and
Power BI then needs to access that.
That's much better cuz then you only go
once to the data source. You can do that
with data flows.
On top of that, another advantage um
you might need to read the license guide
on what's allowed or not or how you need
to do it, but technically, uh you don't
need to have a Business Central license
to get the data in the data flow.
So, how do you create these data flows?
You simply need a Power BI Pro license,
and with that Power BI Pro license, you
go into the Power BI service, create a
workspace.
And in the workspace, we can then create
some data flows. So, let me quickly demo
that.
Almost there. So, I go to the Power BI
service. I already have my workspace,
new data flow.
Okay, I'm going to start with a new data
flow. I can also use data coming from
other data flows. I can export data
flows, import data flows, and so on.
Here, we can connect to many different
data sources, but Business Central is
now also in here.
It saves a little bit of time. We can
specify if you have too much time the
environment and the company and so on.
I'm not going to.
Um
I'm simply going to click next and I
will see all of them appearing here like
I also see that in Power BI uh desktop.
I'm expanding my environment.
Now I can expand my uh company and there
I will also see all of the uh web
services
APIs uh and so on and so on.
And I can connect to them and I can
import them. Basically, what I have here
is Power Query online.
I have already prepared a few uh data
flows.
Um let me sort this by type. I have my
uh master data data flow, a transactions
data flow, multi-environment, of course,
also.
In one data flow, you can import data
data from one and multiple APIs. Uh they
become separate tables. You can do
transformations if you would like to.
You have the whole Power Query suite
available. On top of that, in the data
flow,
you have more performance analyzing and
monitoring tools than you have in Power
BI Power Query.
You can give them a refresh schedule.
And basically, it's kind of an online
data warehouse that you're creating with
your importing data, but uh you don't
need to know anything about creating uh
data uh warehouses.
All right. I can talk much longer about
data flows, I'm not going to. It's Power
Query online and you can import data
like you do in Power BI. You can do
multi-company, multi-environment,
multi-data uh source. You can set
refresh schedules.
Once you have done that, well, you
simply go back to Power BI and you get
data, but instead of doing a get data
from the central, you get data from uh
data flows.
On top of that, Renate, you can also
make you very happy if you're creating
your Excel layouts.
Because in your Excel layout, you can
also or any Excel file, you can also say
get data
from Power Platform and also connect to
the data uh flows.
And then you don't need any special URL
anymore to get to your APIs or web
services, and put connect to the data
flows and that's it. That's it.
So, then accelerate you can do that.
For example, you can create an overview
of the inventory over multiple companies
within the report in Business Central.
So, data flows are really interesting to
have a look at. Reusable transformation
logic you can share a data flow, you can
put security on it.
Um you can give someone access to the
data flow. Another user can go and fetch
the data from Business Central.
You can refresh the data scheduled.
Every data flow can have a different
refresh schedule.
A lot of advantages uh
for using data flows.
Then
what else can we do with Power BI?
Usually, one of the first questions that
I get from many users after I spend a
lot of time creating an amazing data
model and some visualizations. I'm not
that good at visualizing, so I did my
best and the
customers usually say, "Okay,
uh can you get this to Excel?"
Okay, no problem. Power BI has that
foreseen.
There are many ways that you can do
that. So, once you have data in Power
BI, it can also be a data flow.
There are two features which are
interesting. Analyze in Excel
and export with the live connection.
The analyze in Excel you can find that
uh in the ribbon
at the top, file, export, analyze in
Excel. An Excel file will be generated.
You download the file, open the file. At
the right side you will see the data
model
uh available with all the relations and
the measures.
You can go to workspace where you find
your uh
data sets, click on the three dots, and
also do an analyze in Excel. Same
feature.
Then uh you can also go to the data set
overview on the top of the page, select
one, and also click on analyze in Excel.
So, in many places we have the analyze
in Excel uh button.
Um exporting with a live connection is a
little bit uh different. For that, we
first need to create a report in uh
Power BI Desktop and publish it.
Then, in the online report, you can
click on a visual. There is There are
three dots besides the visual. Uh
one of the options there is export data.
If you click on that now, then you can
select the summarized data version. It
will also create an Excel. The Excel is
still connected to the data set, which
is also really nice. But, be aware it's
limited to, I think, half a million rows
at this moment.
I'm not going to demo this, however,
it's very easy to um uh to do.
Okay.
A few more things which are really
interesting once you have your data in
Power BI
uh in the Power BI service. It can be
Power BI reports, it can be data flows,
it can be uh whatever.
Then, Microsoft is bringing some very
interesting um
functions in the future that will become
available.
One of those is uh Copilot for Power BI.
It's in preview right now for certain
people, uh but will become available in
the near future.
What will we be able to do with Copilot
in Power BI? Well, very similarly what
we can already do with the GitHub
Copilot in in Visual Studio Code when
you're writing DAX formulas,
uh it can suggest the formula based on
what you are looking for.
The quick measures, if you know them
already, have that functionality. So, it
can be really uh really interesting.
Besides that, we will also have the
possibility to type
in uh let's say human language the the
the the the visuals you would like to
see or the analysis you would like to
see, and it will be kind of
auto-generated.
So, I'm really curious on how that will
look like.
Small preview. It's not yet live, but
this is how it might look like. So, you
type in whatever you're looking for
and based on the data you already have
online,
uh well, the report, the insights uh
will be simply auto generated.
So, then as as let's say a report um
developer just have to focus on the data
set, the data model publish, and the
rest will uh basically happen
automatically.
Right now, there are a few things you
can already try out.
I go to my browser I quickly once more
and then in Power BI,
I can basically select the data sets.
So, let's go to the inventory data set
of my inventory uh report, and you can
already see this button.
Auto create the report based on the data
I have in my Power BI service.
You click on that
and you wait a few seconds.
And the report will be created if all
goes well.
Hello.
I have my report. Okay, looks nice, but
I would like to change that a little
bit. No problem.
It took a few fields, but I'm going to
change it. I would like it to use
inventory and availability and maybe
also month name and some data from this
and from that table.
And it will simply create a page of a of
a report for you.
If you're happy with that, uh you can
export this again and I as an Excel.
By the way, any any Power BI report can
also be exported to a PowerPoint with
the interactivity in there.
I can show the data underlying data
table.
And I should also be be able to save
this as a Power Power BI PPTX file. So,
that's already
uh live, but more is uh
is coming. Really looking forward to to
that.
Besides that, Fabric is also coming. You
might have heard about that. So, keep an
eye on it. It's kind of an umbrella on a
lot of Power BI tools that we'll be able
to to use.
Don't want to go too deep in there. One
last thing I would like to say about
Power BI and then I can give the word
back to Renato. Huh?
Is that the incremental refresh is
usually a question. Well, I have that
also explained on my vlog. We can do it
on Power BI itself. Basically, it's
something you can do on Power Query. You
split the table into two tables.
One needs to refresh, one doesn't need
to refresh. You load the data, you merge
it again.
Or with data flows, there is also an
incremental refresh setting that you can
simply activate if you have a date time
field in your data set. But remember
that the APIs
on the APIs, Power BI isn't really doing
query folding. So, you have to really
test and see if it's really refreshing
incrementally. But it's an interesting
scenario.
Well,
I'll give the word back to Renato.
Thank you. Thank you, Stephen, a lot of
Power BI.
Now I'm happy that I have finally Power
BI reports that I can embed in Business
Central.
Uh
and possibilities where I can use
Steven's reports either in role center
page or in some list pages.
And we know that by default we have a
Power BI report
part on role center list pages that we
can also extend. And here on this screen
I can show you that we I have some
extension of purchase order list pages
that is showing me information from uh
uh purchase order
lines for example of for my items.
Uh
I can also add multiple Power BI reports
uh
pages on one role center. And as I said,
it's very easy to extend existing list
pages with with new Power BI uh report
part. And this is what I will uh now
show you in in my in my demo.
Where uh I have one of the
I have one simple query where I'm here
my purchase purchase lines.
Uh
very simple and of course I have my
purchase orders list extension where I
added new fact box
for my Power BI.
And here I also uh specified that when I
select one of the purchase order, it
will automatically filter my
my Power BI report.
Uh in Power BI uh here I have my
uh my source my data source and of
course I see a lot of items for some
locations.
Now when I go to Business Central
uh into Business Central
in my uh purchasing
purchase orders
here on the right side I will see that I
have uh Power BI fact box and as I
navigate through
uh my purchase orders, it will
automatically show me the lines
from my purchase order
that I selected. So here I see that I
have on my purchase order 106003
that I'm uh purchasing this item for
this locations and of course information
about another another items.
To be able to uh enable this
I need to publish my Power BI report to
the Power BI service.
And I need on my report uh enable
filter on all pages. In this case, I
have document number as a filter. So
when I'm navigating through the purchase
order list
I see
my Power BI my uh items.
Uh another way that I can uh use Power
BI uh reports is through profiles.
So
uh or my roles and here I have
my role business manager Power BI
enabled, it is extended a role center
page with multiple Power BI
uh Power BI uh parts. And when I
select these under my settings,
here under where it is,
it's probably here.
Okay.
Click okay. In a few seconds, I will
receive my uh role center with the
multiple Power BI parts, where I can
enable different
uh enable different reports for my
for my users.
Okay. When I go home,
it will be here. So, my four Power BI
report pages.
And it can point to different reports.
Good.
Uh
another topic that we had for today is
uh
our platform,
which I'm going to show you right now.
We know that we have all these four uh
components with Dataverse as well. For
Power Platform uh and uh together uh
when we have all of them, we can
integrate them uh with Business Central
through APIs, custom APIs,
and and and so on.
And uh what are the most common
scenarios that we see that we are using
is that, for example, you can automate
uh with Power Automate data data set
refresh for Power BI.
So, for example, I can manually refresh
my data set for inventory.
Or I can send a notifications to my
users or my admins when some of my uh
Power BI metrics are uh reach some
certain threshold.
Uh another integration is combining data
from Dataverse with data from Business
Central, where we having uh possibility
to
uh integrate multiple data sources.
And last but not least, the one that I
like is uh Power BI embedding into the
Power Apps. So, you can build Power Apps
based on API from Business Central and
then add a Power BI report into that
Power Apps.
The report can be some other report that
is not connected to your Business
Central data.
And there we
as well can have contextual filtering
based on the selection.
Let me show you one of the examples
uh that I have. Uh so, here under the
Power Apps, so I have my
items
uh per
my items.
And here as you can see I have my Power
BI report for inventories.
And in order to enable you uh contextual
filtering, so you need to extend URL to
tile from dashboard in Power BI and
filter it per selection that you are
doing on your Power Apps
screen.
And here I'm filtering my
table, my primary key
to what I selected on my Power Apps.
So, that's very easy and simple way how
you can
filter uh Power BI report on your Power
Apps.
And one last thing that I would like to
show you is
before Q&A
is uh here
second, telemetry. Yes, so we run a lot
of reports today
before and so on. So, I would like to
show you how you can track all those
uh inside the business inside the Power
BI.
So, we have uh Power BI telemetry
application and under the usage
reports, I will find all my reports and
uh which layouts uh were consumed by my
users.
Uh what were
action that they are using, so download,
preview, print, or save. What is the
layout type?
And here if I scroll down, I will see
also all my reports and all layouts that
were used
uh
from my users.
Here on under the performance,
I find a little bit more about reports.
This is the
performance of my report that I use. So,
what is the
statistics?
Are they running background or in web
client? Which applications or extensions
were built with for this report?
Of course as well layouts
what are the statistics on SQL.
Steven showed you today that you can use
queries to query your data under the
incoming web service calls.
You will again find the details about
your APIs and how they are performing.
Good.
So, Steven 3 minutes more.
We need to make it
well very quickly.
Show a few things and then we open for
questions. So, some best practices and
you can read them off off the slides.
Just uh think about the data sets star
snowflake and the
read scalar. There's some trainings we
have also available about that of
course.
Some links about licensing but if you
like to combine all of these
technologies it can be a little bit
confusing.
We had a few polls before the session
started. No really no real surprises in
there.
Um interested to learn about I think we
covered most of the topics. Maybe should
have spent a little bit more time on on
the latest ones have but okay.
Developers should create the data sets
of course.
RDLC layout yeah, not so important
anymore I think but the data set is very
very important.
Power BI is for my answer is developers.
Why? Because it's the developer that
creates a data set the data model and
okay the layout can be the the user.
Okay, consultants and end users it can
also be be possible.
For Power BI data sets what do we use?
My recommendation is query APIs. You can
use all the stuff too. The other is
probably data flows or some other data
warehouse. We didn't cover that, but a
third-party data warehouse is also very
interesting to to build, but a little
bit more complex.
We have one slide where we compare
everything.
Um okay, RDLC difficult, you can print
it, you can email it as an attachment,
expressions, pixel perfect, but a
difficult. Word layout, you can print it
as PDF, email, in the body and the
attachments, no expressions, but a
little bit easier.
Excel layout, no print, very dynamic.
Power Query is available in there. Data
analysis on list pages is like having
pivot tables in Business Central. With
Power BI, lots of possibilities, data
flows also, and building a custom data
warehouse is also
sometimes required if you need to uh
process a lot of data.
Whenever you're going to choose for a
certain technology, don't let it depend
on the skill set in the organization,
but let it depend on the actual
requirements of the of the customer and
what you need the insights
uh to quote Sherlock Holmes, "It's a
capital mistake to theorize before one
has data." Well, so think about the data
that's uh that you need.
All right. We have about 1 and 1/2
minutes for
uh questions, so go ahead.
throw
Wait, not good throwing.
Yeah, you can all try.
Did you want this one?
Thank you. First question, um
what should you what should we use for a
test automation when we are going to the
right test?
I should be test against data or report.
And second question, if one does not
have a license for Power BI, what should
be the uh the solution for intercompany
reporting?
Well, um let me start with the second
question. If you don't have a Power BI
license, then you can do everything
except sharing. You cannot create uh
data flows. So, you can do quite a lot,
but uh in real life I would always
suggest a pro uh license at least.
The first how about testing? Well, the
report object uh you can create some
test code uh for uh for that. You can do
some simulations. Uh is the data correct
that you get? And are are the printouts
or layouts uh
layouts okay? But yeah, for Power BI and
all the rest there wasn't really a lot
of testing uh possible uh yet. CI/CD,
that's coming uh in or that's already
available with uh with Power BI, but
testing
Okay.
Thanks.
One.
Hi. Uh one small question about data
list
analysis and pages.
Is there any possibility to share
between users or
um set up for all maybe those analysis
use?
Well, uh for now there is no possibility
to share it.
So, uh what you build with your user is
uh there available available for your
user.
Maybe you can we can export only data
from to Excel and then share it share it
with your colleagues.
But I think it's a very good suggestion
to be able to share these data analysis
on these pages like with the profiles.
And if you have these kinds of
suggestions, you can always do that to
to Kenny on on Twitter or on the Ideas
website. He's really looking for
information. This is a very first
version of the of the tool and he is
going to invest a lot more in in that.
Thanks.
Yep.
Thanks. See you. One.
Hello. Small question. What if I have a
two um apps that extend the same report
and add a column to the same report?
To um
If they all If they each individually
define a layout
Yeah, then then it's for bar.
a layout?
Yeah. So the
two apps, multiple apps can extend the
same report, and the data set will be
extended. You will have more stuff in
the data set, but
you might not be aware of the other app
which is also extending, so you might
have a something really strange
happening at at run time, but it is
possible that multiple apps can extend
the same uh reports. Then like table or
page extensions, you can also run into
into conflicts. Layout-wise,
that will be a little bit more more
difficult. As a developer, um yeah, if
you have both apps in the environment,
you can try to prepare for uh for that,
but sometimes you only notice at run
time. So that's one of the reasons I'm
also not very keen on
uh report extensions as they are right
right right now. It's it's a risk
indeed.
Give the mic to the
Very similar question about report
layout. So, let's say we create report
extension, add new layout without any
field, just our custom layout. How to
make it the default layout for the
standard report? Is it possible, or is
always an option in the report?
Well, in the report extension itself,
it's it's impossible, but there's an
event that you can use in a code unit
where you can replace any existing
report with yours.
after substitute report, but it would
replace the whole report, not the layout
only. So,
Yeah, that's a neat good
question. Yeah.
Yeah. Uh and
does it require any additional setup to
to choose the custom layout from from
the report extension? Or is just a
choice on report request page?
In the In the report selection page,
there you can set what is the default
layouts, but in report extension, I
don't think you can say that that has to
be the default from from that on. Except
maybe if you add some code or and and
change a the record in in the report
selection table and market as default.
And one more small question.
RDL CR and RDL file, what is the
difference?
You see.
RDL C
I can see.
Report definition language for the
client technology Microsoft choice to be
able to render it inside Navision in the
report viewer a long time ago. RDL is
report definition language comes from
SQL Server but needs its own report
server to to run. I think officially the
real name is RDL C what what they are
using here. But try not to focus too
much on RDL C anymore.
Try to move to other technologies as a
recommendation I can
I would like to invite you to post us
questions in application because it's
next session right now.
So I would like to say thank you for
everyone for joining our session and
