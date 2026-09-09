# Microsoft Presents: New capabilities in reporting and analysis views

- **Source:** https://www.youtube.com/watch?v=OJqA6-l4lCg
- **Video ID:** OJqA6-l4lCg
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 51m03s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

All right. So, uh thank you everyone for
coming and welcome to our session. I
know it's the very last session. So,
thank you very much for uh making it to
the session and I hope you will learn
something useful uh today. So, for this
session, we're going to present the new
capabilities in report and data analysis
with analysis mode. Um and for our
agenda today, we have a few things. So
we will be looking into the newest
capabilities for this analysis. Um also
the new reporting features for AL and in
runtime and the Easter development of
reports with the word and excel layouts.
And then we'll have a short Q&A after
the session and if you have also any
other questions during the session just
feel free to ask them in the in the
application and then we will also review
those too.
Yes. So before diving deep into each one
of these new capabilities, let's uh take
a step back and look at the report and
analytics from an organization point of
view.
So it is clear that uh this is a very
important aspect for many businesses to
give them a good overview of their
business processes but different rows
have also different data needs. So you
can imagine that the higher you go out
you go up in the hierarchy the more h
the need the need is greater for the
data aggregation.
Um so if you are for example in
leadership you might uh want more
performance data and KPIs and
dashboards. Um if you are more in a
management level then you might be more
interested interested into trends or
summaries or other reports. And then if
you are in a more specialized row then
likely you need more h to work more with
specialized data and to that in a more
dynamic way. Um so with a different
needs that also means uh that there are
different tools for uh each of the
different scenarios. So for example in
the management uh sector you might work
more with PowerBI
whereas in the more specialized roles
you might work more with Excel or maybe
the built-in tools in business central
like data analysis where you can have a
more hands-on experience with the data.
Um but in this session we will be
focusing more in the new capabilities
for the latter one. So we will look more
into the analysis um Excel and and Word.
Um yeah and just uh out of curiosity to
know our audience better. So can you uh
just I guess light your your light um if
you are a developer in the in the room.
All right. Or yeah raise your hand so it
works. Thank you. Okay. So looks like
about half and half. All right. So um as
you can see the world of reporting is
changing. We have many different tools
for the different needs. So just be
aware that the next time a customer
comes to you and ask you to build a a
report you should uh refrain from just
going with a typical short just how
should it be formatted? Um and just try
to ask what do you want to analyze and
what do you want to use it for. This way
you can make sure that you pick up the
right tool for the different needs um
such as a PowerBI or you can do a query
and the list page data analysis within
the uh client or also maybe a reports
with with Excel or documents with word
layouts and again in this session we
will only look at the latest
capabilities in the latter three uh
tools that we have in business central.
So first up uh it's the newest
capabilities in data analysis. How many
of you know data analysis or analysis
mode in in BC?
Okay, quite a few. Uh yeah, so for those
of you who who don't really know it, h
this is a feature that came in 2023
uh release wave two I think. Yeah. And
uh it allows you to h do complex data
analysis within the tool list pages and
queries directly from the web client and
without needing a developer at all. And
it has been a huge success for our end
users. But one of the biggest
limitations with this feature is that
you are limited to the data that is
already present in the list page or in
the query. So if you want to work with
more data um then that's when you need
to involve a developer uh to either
create a page extension or create a new
query. So now you can analyze that
but we have solved this problem uh this
release actually with a 26.2 which was
released last Friday. So now you can you
can also try this feature now and uh
what we have done is that we have now
enabled customers to add or end users to
add uh fields from related tables and
pages directly in the web client and
without having uh to call a developer to
do it. So, um, yeah, it's a huge step
for users to self-service in in that
aspect. And I'm going to go ahead and
and show you how it works directly from
from the web plane. So, uh, we can look
at our customer ledger entries.
This is my list page. And to go into
analysis mode, I can just click this uh
button over here. And this is my list
page in analysis mode. Again, I so many
of you are already familiar with this,
but um for those of who of you who don't
now, you can do some operations with
your data. You can hide or show columns.
You can group your uh data. You can also
put some filters directly from here. You
can also do some aggregations. Um and
you can also use the analysis assist
feature. So you can do all these
operations just with a natural language.
Um but again I'm only limited to the
data that I have in this list page until
now. So now if I go to the analysis tab
then I will find this new um this new
action here add columns from. And when I
hover over that then I will see a a list
of uh tables where I can add my fields
from. So the first suggestion is that I
can add fields from the underlying
table. So in this case the customer
ledger entry. So I can add fields from
this table that are not already exposed
in the in the list page as opposed to
creating a list a list page extension or
I can also add h fields from tables that
have a table relation to this underlying
table in AL.
So for example, these are the table
names and next to it I can see that
table relation that is defined in a in
the AL code and it can be that a table
is related through multiple relations.
So that's why I can have more than one
entry here. So I can join for example
the dimension value through different uh
relations.
Um and the ones that I show here is just
a a few uh suggested suggested ones. But
if I want the full list of all the
tables and all the relations that I can
use, I can go and click other source.
But in this case, let's go ahead and
click currency.
And you can see here, this will open a
new popup window where I can see all the
fields that belong to the currency
table. But then, of course, users are
usually more familiar with pages because
that's what they they use in their
day-to-day life. That's what's surfaced
in the client. So if you prefer you can
also select a list or a card page that
implements this table
and uh yeah you can also look at the
full list. So in this case I can pick
the currency card
and now I can see all the fields that
belong to the currency card page with
the descriptions and some sample values.
So now I can go ahead and select a few
of those.
Click okay.
Then I get a small disclaimer about some
functionality limitations. Um, but
nothing too big to worry about.
And then once I do that, then I have to
scroll all the way down to my list. And
then I will see the new fields that have
been added to my list.
Then of course I can order them around
or I can also delete them if I no longer
want them.
And another thing that I can do is from
let's say I want a particular column. So
I also have that column menu and I can
add the columns that directly from here.
So let's add more information about the
customer. For example, let's look for
the city.
So now I can add the city field.
And now my field is added next to the
customer name. So I don't have to move
them around. Um yeah. So, as you can
see, I just created a new data set with
the related related fields directly from
the web client and without having to
involve a developer at all. And as you
would expect, I can now perform the
usual operations that I would usually do
in analysis mode. Um, so I can for
example group by that. So here's my city
field.
So now I can group all my customer
ledger entries by the city of the
customer.
I can also filter by that. So if I want
to look just as the Chicago ones for
example,
if I don't misspell it, it should work.
Oops.
Yeah, you got the that one. I can also
do the usual aggregations.
So I can see all the aggregations for
the Chicago customers.
And then I can also if I want to do more
data analysis I can also export this to
Excel.
So I can just open that in Excel
and as you can see it keeps my related
tables that I have added here and I can
do more analysis in here.
Um yeah so everything is uh supported
here except analysis assist. So that's
the only thing that is still not working
with related fields but uh there's some
work on that. So
so yeah that was it for the demo. Um now
I can show you a bit how it works under
the hood so you could understand better
what's going on. And this is a
combination of work between the server
and the client. So the first thing that
happens on the server side is that as I
told you we kind of scrape all the AL
code and we get the table relationships
that are um h that relate to the
underlying table of that list page. Um
and then we filter those tables uh so we
filter out the ones where the user
doesn't have access to the table. We
filter those internal ones. We filter
the temporary ones and such. So we don't
expose what we don't want to expose to
the end users and we send that list to
the client. Then in the client you see
that list that we saw before and then
once the user selects the table that
they want to use then that's when we
select the fields and we show the fields
and also these are filtered. So we don't
show the fields that are internal or
that are not supported in analysis mode.
And then once we have the table relation
and the field selected by selected by
the user, we send that to the server
side like also alongside the data
operations that the the user is doing in
the client. And then on the server we
create a dynamic query. And this dynamic
query is actually an AL object. And then
we compile that AL object. And then we
have a an object that we can can work
with. And we perform all the
transformations that are needed. And
then we run that query. And we send that
information back to the client which is
what you the data that you see.
And uh this is a bit more of how the
dynamic query looks like. Um, as you can
see, there's a column for every field.
There's also a data item for every uh
table relation that you have. Um, it's
also possible to have the same table
through multiple relations. And then you
also see that the data item link
corresponds to the table relation that
you selected, which again also comes
from the AL code.
So that was it for the newest capability
for data analysis or the main one at
least. Um,
and there's also a small uh also a new
capability. It's a smaller one. So in
the get URL AL method, you can now use
you will now have a layout parameter. So
now you can use this to for example open
pages analysis mode. So you can embed
this URL um in your AL code and then
when you click it, it can open it in in
analysis mode. And there are also some
other uh values that you can use for
that layout parameter.
And that was it for what's new in the
analysis. And now Mirro will go through
some of the latest advancements in the
document reporting. Yes, thank you
Blanca. All right. So let's see now all
the new capabilities that we introduced
in the last couple of releases for
reporting. And let's start from AL.
First of all, it is now possible to use
.NET formats for numbers. That means
that we can now specify advanced
formatting like the one that we have
here in the example by using the auto
format expression. So as you can expect
we can now finally support this case
where depending on the value of the
number we can properly format it
depending on the use case. We know we
have different cases and sometimes we
need some particular formatting from the
customer. One small comment um this is
only available for auto format
expression. it is not available yet for
format function.
We also introduced a new trigger called
on pre- rendering and as part of this
effort we also added the capabilities to
the server to append a list of PDF
documents to attach a list of documents
to be embedded in the PDF and to secure
your document setting admin and user
passwords.
You can see this step as a as a step
where we are collecting data that are
then used later on when we are rendering
the the layout.
We use this one um in our effort to
update the invoicing but of of course as
other triggers you can use them for
other purposes as well.
And finally, as we are modernizing our
layouts, we wanted to make our life,
your life and our customer life easier
to handle different version of layouts.
And more specifically, we added three
new AL properties to mark a layout as
obsolete. So now in AL you can set the
obsolete tag, the state and the reason.
And this is also shown in the report
layouts page. Um I will show show that
in a second. and it can be set through
the UI in your uploader layouts. And of
course, I cannot mark your layout as
obsolete. So, I need to be the one
uploading it.
Now, let's move on the runtime side and
let's see all the small improvements
here and there that can help you working
with layouts. And to do that, let me
switch to our environment. All right.
Very first, I just want to show you the
exploring reports page. Um, and if you
ever wonder if we have any reports in
BC, this is a good place to start. We
have quite a few. We now have an info
icon here which shows the about title,
about text. So, it explains what the
report is about. And you can also now
open the request page in a new window
with this new action. So, you can now
run the report without leaving your
session. And one reason why I wanted to
tell you about this is that we are also
using these properties in other
functionalities for example in search so
that we can make reports more
discoverable. I cannot say too much here
but we are also planning to use this one
more broadly throughout the product. So
it's a very small change is very little
effort but it can actually provide value
to your customers. Now, let's visit the
report layouts page
and let's take a look at what's new in
here. Well, if we scroll all the way to
the right, we can find now four new
columns. The first one refers to what I
was showing before. Now, we can see if a
layout is obsolete or not. So, it's
pretty easily visible from the UI as
well. The second one is this Excel
sheets. Um, some of you might already
understand what it is. for the rest and
please bear a moment let's park it I
will show you later in practice and
finally we have these two new column
last modified date and last modified by
now you might be wondering why they are
empty that's just because it's um these
reports are uh from the basup but you
will see when I create a new one that
those will be populated with my um
account and these are meant to help you
troubleshooting
if we focus on the action bar here we
can see that compared to one year ago.
We have quite more options. First of
all, we can now update and export the
layout. And this action updates the
layout with the latest metadata. We then
can export the report schema. When we
run this action, we download the custom
XML. So think about a case where you you
have a word layout. It's ready. The
structure is really good. You only need
now the business central data item so
that you can populate it before
uploading again in business central.
Well, you can simply come here. You
download the XML and then you import it
in Word and you're ready to go. In a
similar way, but let's say that this
time you want to create a new layout
from scratch and you already have the
report object in Business Central. Now,
when you create a new layout here, let's
call it BC Tech
empty
and let's use a word. Now, you have this
option to create a blank layout. And
what this does, if I toggle on, it will
automatically create a new layout. And
in this case, it's a word. So it
generates a word document which is
empty. But of course, it's already
including all the custom XML and
everything you need to start building
the layout.
Finally, we have these two new actions
here which are meant again to help
troubleshooting and handling customers.
The first one is show layout info. This
opens a very simple dialogue with a few
information available. Um you have the
system ID here. This is the one that you
can use in telemetry when you're
investigating what's what happens in the
log and then you have the last modified
date. They create a date and by um we
know cases where the customer is
complaining the layout was working
yesterday is printing something
different. What happens? Nobody knows.
Um then that's going to make it easier
to understand okay who was it did
something change in the meantime and so
on.
And to support again this story, we also
added a new action to validate a layout.
When you run TS1, we execute a number of
validation steps. Of course, if they all
succeed, the the layout is validated.
But if one of them fails, for example,
let's say that the font validation uh
fails. I know that's something that
happens. I heard some cases like that.
Then you will have a good message
saying, well, the font validation has
failed. And then you have a good
starting point to take the layout and
fix it. One small comment uh for font
validation. It is available on RDL and
it's not supported yet on word and excel
but the team is working on it. So that's
coming very soon.
All right. So these were quite a few
small action here and there but overall
they provide a good improvement to our
experience. Now let's see how we made
working with word layouts easier and
more funny and how we can make more
flexible layouts. But before jumping
into that, I know some of you might have
this question. So let me have a small
disclosure here. RDL is here to stay.
Our investments in word and excel
doesn't mean that RDL is being
deprecated.
We believe there are different needs.
Customer have different needs and
therefore we have different tools. I'm a
developer. Many of you are developers.
We know there are complex scenarios
where RDL just works better. So please
keep using that for those cases. But we
also believe and that's why our
investment in word and excel that there
are many other cases where we need
simpler things where we can offload the
work even to the customer. Customers are
familiar with word are familiar familiar
with excel. So sometimes we can use this
new tool to make our life easier and
help them empower our final customer to
do whatever they need without us
spending resources. So how can we do
that?
One small uh addition that we have today
is the new two new report metadata the
report metadata and the report request.
These are always available, always
included in the custom XML. And as you
can see here in the screenshot, they
provide very general data that you
normally use whatever report you're
making. We have the report ID, the
about, um, the title, the name, we have
the username, the company, all of that.
So, you don't need to code them in a Yel
anymore. They're going to be there no
matter what. Just go and use them.
How many of you have heard about the
word addin?
Okay, very little. Nice. So, you're
going to find out today um last it's a
few months now that in in office you can
go and download the business center
we're adding. It's the first version and
for now it provides you the ability to
add comments to a layout and to work and
make the layout more flexible with
conditional visibility controls.
We also have fully support for se for
sections. That means that we can now
finally go and change properties like
margins, orientation, we can add
footers, watermarks, whatever you want
to do with sections, it is now finally
supported. So all of that, let's see how
we can actually use these tools in word
and let's take an example and see how we
can make them more flexible and have
more fun. So for today's demo, I have a
small extension that generates some
sample data and I already have a layout.
So let me run it and show you what we
have today, what we're working on. So we
have it's very simple as you can see. Um
maybe I can zoom in a little bit. Yes,
we have a sales order with a description
and we have a first table which seems to
contain um a number of different objects
and this seems to be the main content of
the layout. If we scroll even more, we
have another table with additional info,
something that looks more like appendix
or things like that. So, how can we
improve that? There's a few things I
would like to improve. Let me show you
how I can do that. Today, I keep the
first tab open so that we can go back
and go back and forth and compare.
So, first thing I will export the layout
and open it in word.
All right,
cool. So, if we look at the menu here, I
already have the business central addin.
If you don't know how to do it, just go
on the app source, search business
central and you will find it. Otherwise,
please refer to our documentation. There
are tutorials, videos or ask questions
later on. Um, we have two main sections
here. The first one is layout controls
and the second one is help and support.
I will quickly show you
these um these links just because we
have actually improved our documentation
quite a bit. We have a lot of examples.
I know it's a little bit hidden. That's
why I'm showing it today. But it's
inside here under programming developing
reports. So please go take a look. There
are tutorials for world layouts,
tutorials more specific for the word
addin. But now let's move to something
more interesting.
Okay. If we look at the layout controls
we have today, the first one is insert
layout comment. This one it inserts a
control and whatever content we insert
inside the control will be hidden from
the report when we render it. So you can
use this one for documentation, you can
use it for versioning, any kind of
things that you want to have it when
you're working with the layout, but you
don't want to print it.
And then if we expand this hide if empty
group, we have four new actions. The
first one is hide empty table. And as
the name suggests, it allows you when
you apply to a table, it allows you to
hide the table if it doesn't contain any
data. The second one is hide empty table
row. This can be applied to any row of
the table and it must be applied to a
data item. If this data item is empty,
the whole row is removed. So you can
conditionally show and remove rows. In a
similar fashion, we have hide empty
table column. This one must be applied
to a repeater and it must be applied to
the column header. So to the data item
of the column header. We'll see in a
second. And when when we do that if all
the rows of the repeater have an empty
value for that column then we can remove
the whole column and free up space on
the table. And finally we have high
field of zero. This is not bound to any
repeater or table. It can be applied to
any data item and as the name says if
the value of the data item is equal to
zero then it's hidden. So let's see how
we can take advantage of that.
Let's go back here. So the first thing
I'll zoom out a little bit.
The first thing that I want to I would
like to improve here is that if I look
at this column column to hide is empty
in this case. So it's taking up space.
It doesn't provide any value. I would
like to remove it. But I cannot simply
remove the column because there's a
second sales order which actually has
value in there. So I want to do that
conditionally. Right? So how can I do
that? Well, as I showed before, we have
a new control for that. So I can simply
come here. This is the column header
that I want to conditionally remove. I
select it and then I click on hide empty
table column. That's it.
What else can we do here? Let's assume
in this example that this field to hide
is one of it's a field where my customer
it doesn't really make sense to be zero,
but it happens to be a numeric field. So
I want to show it if there's something
in there, but if it's zero, I don't want
to see it. It's just clutter. It doesn't
make sense. So let me show how I can do
that. In this case, I only want to work
on the data item. So I can select it.
All right, I can select it here and
hit on hide field of zero. Again, very
simple, very straightforward. And
there's a one final change that I would
like to do. My customer is has a weird
question today like he's asking me he
wants this layout to only show the
objects that have an actual value here
so that they have this row to height
greater than zero. So I would like to
remove the first row and the second row
depending on the value. But if I go back
here and expand the action menu I have a
hide empty table row but there's no hide
table row if equal to zero. But maybe
what we can do is to combine two
different controls. So let's see how we
can do that. First of all, I'm selecting
again the data item. And now the first
thing I want to do is say, well, if the
value is equal to zero, let's hide it. I
don't want to see it. Done. And now I
can try to apply a second
a second control, which is if it's zero,
hide it. If it's empty, hide the whole
row. Let's see. All right. So now let's
save. And now that we have all these
changes, let's create a new layout and
see if they all work. So let's call it
BC tech days new
word.
And let's run the report.
All right. So as you can see here, we
already see something happened. Let's
see if it happened the right thing.
Okay, so the first column, the first
thing we wanted to do was to remove this
column if it was empty. And if we go
back here, we can see that now the first
sales order doesn't have that column
anymore. The whole space is used better.
I have no clutter in there. But the
what's important also is that if I
scroll down this one, the second order,
I have values and the column is still
there.
Second of all, we wanted to hide this
field to hide in case the value was
equal to zero. And if we take a look
here, the field to high is now empty. So
that worked as well. And finally, as you
can probably already see from the fact
that we only have two rows and we don't
have four rows anymore. Just double
check. The first one and the third one
had a zero value in the last column and
therefore they have been deleted. So we
can combine two different controls
together and have uh kind of a
combination effect.
Okay, there's one final thing that I
would like to improve here. Um and if
you look at this additional info table,
this is more appendix and it takes a lot
of space. It's a lot of text. So I would
like to move it maybe put it landscape
and I would like also to make the main
page out of footer something like that.
So let me show you how we can do that
with section which since I mentioned
that we now support section. Let's see
it in practice. So I can come here
and in layout I can add a next page
section break.
Now these are two different sections.
And for this one I want to change the
orientation to landscape so they can
take all the space. We can optimize it.
And finally, for the main page,
in case we have a lot of orders, I just
want to
Yes, I want to add a footer. Let's go
with a simple one. All right. And now I
want to unlink this one. And since on
the second page, I don't need it, I'm
just going to remove it.
There you go. So, let's go back here
and update the layout.
Let's run the report one last time. And
as you can see now we have the first
page is clear. We have our footer. Of
course we could have way more things
here. And the second one is landscape
orientation and so on. So this is a very
simple case to showcase that now we can
support sections. You can think about
using watermarks and many other kind of
things.
Okay. Now that we have our new layout, I
want to show you what I mentioned before
that you can obsolate the layout from
the UI. So, how can you do that? Well,
let me do that with the the old one,
which I don't like it anymore. I can
simply edit info. And now we have a new
toggle mark layout as obsolete.
And that's it. And now it's also shown
here. Now, as a small suggestion, you
probably also want to reflect that on a
title or the description, but this is
how you can do it. All right.
Okay, we also have a few other small
improvements here and there. Uh, I don't
have time today, but please go and check
out our videos, check out our
documentation. There's a lot of more
content in there. We also didn't forget
about Excel and we have a few
improvements there that I would like to
share with you. First of all, we now
have a new AL property called Excel
layout multiple data sheets. How many of
you already know this one?
Okay, not that many. I expected more.
But for those who know, you might be
wondering, well, but that already
existed. And that's correct because it
existed, but it was only for the report
object. Now we introduced it for the for
the layout object as well. So now every
layout can override the report default
value. And this is again it's also
available on the UI and it's also
visible on the UI. So every layout might
have different needs. And then you can
specify whatever you want.
Since we have a little time, I will show
you how you can do that.
So let's say we create a new layout
here. Let's call it BC tech
uh Excel.
All right.
Excel.
Let's create a empty layout for
simplicity. And now you can see that we
have a new property. We can default to
the report object or we can use a
specific one for this one. I'll go with
a multiple data sheets layout. And we
can see here in the column that I showed
at the beginning.
Okay. And finally, how many of you have
ever written something like this in
Excel?
Okay. I see a few people. Did you like
it? No. I see. I I agree. I agree. Well,
from now on, you don't need to do it
anymore because we introduce what we
call named formulas, which under the
hood is a very simple mapping between a
readable name and this XO lookup
formulas. And you can see all of them in
formulas name manager. And if we take a
very quick look, if we download this
layout and I open it in Excel,
let's go here. Let's say that in this
col in this cell I want to show the
company name then I can simply type
equal as for any other functions and
search for company name
and you see here I can select and there
you go and again if you want to explore
more formulas name manager
and you can see here we have mapped a
lot of different functions that are
commonly used and of course you can
build your
Great. So, we have 10 minutes left. I
know we also maybe a bit over time from
the previous one. So, we have five
minutes to three. But I will take one
minute to show you a sneak peek of
what's coming in 27 because I mentioned
a lot where we are modernizing our
layout. So, let's see something about
it. This is our old production order
statistics. And now from the next
release, we are going to have two new
layouts. one for Word, one for Excel.
The reason why we're having two is
because looking at our telemetry, we
notice both use cases. So there's people
printing the layouts, there's people
downloading and exporting the layout. So
that's why we are going for two. And if
we if I show you some other example
here, you can notice that we are trying
to keep a consistent look uh throughout
all the layout. So that's what you can
expect um coming.
All right. So
if you have any doubts, if you don't
know how to use something, if you want
to explore more, you have a lot of
references here. These are very specific
to analytics and reporting.
So I'll give you a second and we will
also share the the slides. If you want
to see all the other small features that
we introduced and we haven't had time
today to cover, please go and watch the
launch event. There's a little bit more
both for data analysis and for
reporting. And of course if you have any
question for general business central
you you you have the links here. So now
we have some time left. If you have any
questions blank and I we are here and
and we can answer and if you have
questions after the session as Blanca
mentioned before feel free to write them
in the in the app.
So get a t-shirt. Yeah. Yeah. I will.
All right. That's good to try.
Okay. So, uh about LDL reports. So, I
understand that the most improvements
are in Excel and Word layouts, but maybe
you have something planned for all the
RDL reporting or well, you should just
forget about them. Yes. Um okay. So, we
I can say pretty honestly, so I cannot
say much, right? But also things can
change but um we don't have plans to
improve or we are not investing right
now in improving RTL which again I want
to stress it doesn't mean we are
removing or we are planning to remove
RDL that's not the case we are just
simply our resources for now we are
trying to improve the story in word and
excel layouts so that's a pretty pre
but we know it's important for you guys
and that's why it's it's staying
and there's also another question over
there and a t-shirt.
So wonder
I'll go there first and come to you.
There you go. Thanks. Uh when using word
layouts, uh I had a question. I had a
document with several levels and they
asked to add a nested level and I didn't
get it. I is there an improvement in the
future for that? Yes. So I think I
understand the question. We do support
some level of nesting. Yeah. But not all
cases. Sometimes it can be very let's
say very specific. But yes, we do I can
say that we are planning to improve that
scenario as well. So to add an add level
or a nested level to to support more
nesting levels to make it more. Yeah.
Yeah. You have almost you can nest it
now but I had to add it in an existing
document. I had to head a next level or
a nested next level. So I didn't succeed
at it. So I had to create the document.
Okay. Uh again, okay. So So you didn't
manage to use the existing layout. Yes.
Yes, I did existing layout. For example,
uh an invoice. Okay. You have to add a
new level all nested or not nested.
That's not important. But I didn't
succeed. And I was wondering is there a
future uh solution for it? Okay. So
there are two parts of this question.
The first one is uh when we are work
with layouts like this they might be
very specific and for that please we can
talk later reach out because we we are
very happy to help. We have many cases
in Yammer where the partner reached out
to us and said I have the very specific
case it doesn't work and actually in a
couple of times it became a new feature
like we supported the hide row at the
beginning was only for repeaters and
because of one of you guys having a
problem we actually extended and now
supports all the rows so it doesn't need
to be a repeater. So that's the first
thing. In general, uh yes, we are
planning to um add more capabilities and
support more cases or more nesting and
more complicated scenarios even for
conditional not only limited to tables,
not only limited to uh repeater. So yes,
that's the plan.
Uh in analysis mode, we have private
mode and it shows us group data, but now
the result is not interactive. Do you
have any plans to make this uh result
result data interactive that a user can
click on it and show based on which job
entries or other entries uh the result
some calculated?
So what do you mean with interactive
uh like uh when you have flow field you
click on it and you show the data set
that uh based on which this value was
calculated. Mhm. And do you have uh
plans to make the same in analysis mode
in pilot? In private navigating. Yeah.
Um I don't think there are plans for it
now. Mhm. But uh there might be. If you
think it's a good idea and you get
Exactly. That's what I was going to say.
If you think that's a good idea, put it
in busy ideas, get some votes, and then
it will be prioritized. And then also I
just want to stress again um Yammer we
listen to it and especially for
reporting I know the PM very closely
he's very active in there and we have
cases where before starting developing
we come there we ask you guys we are
planning to do this this and that what
do you think and then we get feedback so
that we can start from iteration one to
get it closer to what you need and not
only what we have in mind because many
times it needs you know different
iterations. Uh
that's right. Watch out.
There you go.
Uh you showed the the query like the
behind the scenes of the analysis view.
Are we able to get those queries? Not at
the moment because that would be kind of
useful to just you know get the analysis
mode and then just get the query and
then perhaps build a report out of the
query.
It is not possible right now but it
could be useful. Of course you will have
to deal with any of the issues with IDs.
Yeah. Yeah. Yeah. Of course. I mean I
mean just getting the bull coded where
you useful again PC ideas or but yeah
not possible at the moment. I see. I see
anymore. Okay.
Um, is there a way to publish um
document attachments with the e
documents feature? You talked about it
briefly earlier.
Uh, so
there's um not for now it might happen
but there's some so we some of you might
might be asking okay why is a trigger
why we don't have an AL API I guess and
makes sense. Uh there's some licensing
issues that we are trying to smooth out.
That's the main the main point. So
that's why we have to expose it in this
kind of way. Uh so if we manage to
resolve all those issues, uh yes, we
will also we we would also like to give
you more power in that sense. Just do
whatever you want kind of thing. Uh but
yeah, we need there are some
complicities in that sense. Okay. Thank
you. So I cannot guarantee because it's
it's not really a technical problem.
It's more licensing problem. Okay. Yeah.
Thanks.
No worries. Any
other one there?
So yeah, I'm curious. Um I just before
came from another session and there it
was like okay RDL if you haven't learned
it yet don't learn it because it's
overdue. You're saying it's not going to
go. Mhm. But it's not supported anymore.
And as soon as security issues arise
there, they will just have to eliminate
it. So So I guess the question is should
I invest my time on RDL or not? Is it?
Yeah, but it's contradictionary. So some
say it's it's going to be faded out
because it's it's overdue and we're
going to put all effort on on Word and
Excel and yeah, we don't have the same
features yet, but yes. So I I understand
the sentiment of saying well Microsoft
is investing all all the other ones that
means today they don't tell me that they
are deprecating but that we are going to
lose RDL. Um what I can say is that
that's not the case. It's just a matter
of what we are investing what we believe
we can provide more value right now at
the current stage and that's where we we
believe we have a lot that we can
improve in word and excel and RDL for
now uh we are not planning to expand it
but there's definitely no plan for now
to to remove anything so I wouldn't say
that you should be concerned about it
that's what I'm saying I'm I'm not
concerned but it's it's yeah I don't
know what's uh
think of it now that's that's more the
thing no so uh
Again, the the reason why I sent that
message was to reassure that RDL is
staying because we know it's a concern
that people had and it's a reasonable
looking at where we investing, you might
think that way, but that's that's not
the case. That's all I I can say. Okay.
Thank you.
So, a question on the joints. How how
many levels deep can you go? Is it just
one relation or is it multiple uh deep
with NLS view and you can do as many as
you want. Uh I guess there are no
restrictions. It's like creating a
query, right? Uh but all the joints are
done on the on the base table, right? So
you cannot chain joins to so you join to
one table. Yeah. With another one and
then you chain the next join to that
table. That's not possible at the
moment. All the joints are done on the
base table. But maybe we could support
that. uh in the future if it's needed.
Yeah. And is it only for analysis view
or is it also something you would
consider for personalized that users can
add uh fields on their pages. So for now
it's just analysis view. Okay. Okay.
Thank you.
Any other question? Yeah.
Um my question is um if you do a report
extension
and have programming in it that you know
will only be used in your new layout,
would it be then best practice to
actually code it away in a way and
saying only use this code if this layout
is used so to not to clutter it?
Um I'm not sure I understand the
question. Maybe can you rephrase it? So
maybe um you make a report extension for
the sales invoice. Yeah. And the
customer says um in my new layout I want
to see if the line is uh in if the sales
invoice is um is link uh was linked to
to assembly order. Okay. um that the
assembly components are posted or the
bomb components
um and you and it this isn't standard
for the um already existing Microsoft um
layout and it's only in your layout that
you then
uh program your report extension to only
get the assem uh the uh new data item if
it's your layout that is being printed.
Okay. Um
so okay let me let me ask you a second
what is your concern here? Um my concern
is that uh we currently have a customer
that has um two other third-party
extensions. Yeah. That also has um
report extension for the um for the
sales documents, but they want us to
make a specific layout for them with
even more extensions. Yeah. And we want
to um and the um the data that is um the
whole data set that is given to the
report layout is very very cluttered
now. All right. Yeah. And we want to
reduce the clutter but also don't want
to um of course to um result in that the
other layouts can't be printed anymore
because something now is missing or the
data is different or something. So we
were thinking about uh um programming
stuff like only do this code if this
layout is selected to pre be printed.
Okay. Okay. Well, I would say you can
follow the So I have also another
comment later, but um I would say you
can follow the approach of either having
a new report and try to I guess it
really gets to the case where how much
overlap you need between the two, right?
Um if you have a lot of overlap then it
might make sense what you're doing. Um
if you can differentiate the two things
then it might be easier to say let me
have a smaller one that works with a new
one and I don't have cloud. But what I
would like to say is that one of the
investments that we have right now is to
improve the experience in word for
working with a custom XML. So that's
something that might help you. I believe
it might help quite a bit in the future.
So I know today we we are working with
this custom XML right which is not the
nicest uh and we want to build an
experience where it's much easier to use
it and I'm saying this because it might
help your case where the report has a
lot of data item and it's kind of
complex to work with it but then in the
future might be easier even though you
have a lot of them. Okay. So it's just
something to keep in mind because it's
something that we are working on right
now. Can I ask another? Yes of course.
Um, is there any thought to um allowing
query to be used as a data item in
reports or should we just use an integer
data item and then go from there?
Not that I know. Not that I know. I
don't know if Blanka if you know a
little bit more about it if we have any
plan in that sense. About what? Sorry.
If if we can support query in the query
as a data item instead of just tables.
No, as a for pages. No, but I mean you
can publish a query and then you will
see the query as in BC, right? No, no,
as as a re as a data item in a report.
Oh, no, no, yeah. No, okay. But um yeah,
no, but I guess this could be again a BC
idea or we should here is I would need
help from the PM to be MO. Yeah, we were
saying if we just cut it short and then
we can just answer the questions maybe
at Yes. Yes, of course. So if you have
any other question please come there and
so that thank
