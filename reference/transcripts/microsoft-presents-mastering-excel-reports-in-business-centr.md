# Microsoft Presents: Mastering Excel Reports in Business Central

- **Source:** https://www.youtube.com/watch?v=OYS5-kXMUnE
- **Video ID:** OYS5-kXMUnE
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 47m46s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

all right so welcome all to the last
technical session of the this conference
my name is Nicola and I have been
working with this product for the last
16 or 17 years it's almost 17 years
actually and the reason why I'm here
today is because I'm one of the
developers that was working on the Exel
layouts I was working more on the Excel
and a side and together with me I have
Neil Kenrick yeah I'm in L like and I
actually worked on the platform side of
this feature so I'm the one that is
responsible for the B time part yes so
today we want to teach you how we have
built these Excel layouts and I need to
switch the clicker probably let's see if
this one
works no it doesn't so it's the other
one uh
so I need to switch it to this side I
guess I'll just move to the until we
resolve this one so for the agenda the
topic is going to be like this so we're
going to start with what we did and I
would like to thank you all that have
filled the pool that we made because we
have seen that 90% of people did not see
the new XL that we did so we're going to
start with the short demo of the ex
layouts that were
created then Neil Kenrick is going to do
some hardcore engineering with building
the data sets and then I'm going to take
it over and then we are going to take it
into Excel Excel and I'll show you some
Excel magic and how we created the
layouts we are going to publish the
slides on the Yammer so if you need this
slide de you can easily find it
afterwards now because this is a
reporting session we need to start with
the pie chart of course and this is the
visual representation of how the time is
going to be spent so you can see that
it's very small amount of time in the
actual demos and we are going to spend a
lot of time explaining how to build a
specific data set you can also see that
the time is short so it's going to be
hard to fit it within the 45 minutes if
you have questions please come down or
reach to us through
Yammer so here uh the first topic of
today is what we did and also what are
we planning to do in this area and for
this one I'm going to switch straight
into the
demo and we are going to start with the
old stuff so these were are old Excel
layouts and they're basically based on
the Excel addin that is fetching the
data from the web services which is good
because it is
refreshable however it's using a net uh
it's using a Visual Basic and macros
thus it is disabled by default because
it represents a security risk and these
layouts were translated in multiple
languages however you were not able to
customize them at all so you couldn't
change anything on on this specific
layout the new layouts are looking
completely differently so you can see
that it is a really rich content that we
are exposing so we have pivot tables
here you have slicers so you can slice
and dice the information that you want
and basically you can use any Excel
element except Visual Basic and micros
that's the only thing that we can
blocked you're also able to create
multiple customer facing sheets so if
you want to see in additional reporting
in foreign currencies you can see it or
if you would like to see the money based
on the currency like this you can also
switch between the
tabs and the great addition that was
done is that now we are able to export
the data into multiple sheets so here
you can see that we have the customer
aging data which is the main set but I
can also export dimensions in separate
Sheets if I would like to create some
nice slicers so now it's much easier to
export and organize the data and
actually build the
reports if you want to access the
reports they are right next the new
reports are right next to the old
reports and the difference between them
is that the new ones have preview
attached to them and the reason why we
did this is because we were relatively
late with implementing this feature we
also did not wanted to drop it on the
customers without receiving feedback
from the community so for the next few
versions they are going to be in the
preview mode we are looking forward from
for the feedback from you guys and then
we are going to drop the preview and
hide the existing layouts and then they
are going to be removed from the
product U the main reason why we want to
do this is because we want to get rid of
macros and Visual Basic that's our main
driver also if you would like to find
them they are exposed through the Page
search you can easily find them they're
also in the role Explorer so it's quite
easy to navigate to
this to get to go back to the
slides a different view into this and
this is the actual picture of what we
did is with the green circles you can
see that these reports have already been
shipped the yellow ones are the ones
that we are planning to ship in the next
version and we have shipped most of the
reports in finance area how however we
also have three layouts that are
tracking emissions and for the other
areas the reports are also going to come
we are planning to implement more than
reports now we get a lot of questions
even from internal developers shouldn't
we be actually implementing powerbi and
the answer is no because you need both
in reality so you will need both powerbi
and Excel since they are fitting
different report
needs there is an excellent
documentation topic that is listed here
you can find it in the slid sheets and
access it after the
presentation that describes when should
you use which and what is the benefit of
powerbi or Excel and vice versa
unfortunately we don't have time to go
into this and I would invite you to
check it
out so that was all for the short intro
and now I'm handing it over for Neil
sonik to show us how to build the data
sets yeah and I'm going to talk a little
bit about what we have behind the scenes
before we actually get to the Excel
layout or the Excel vort
itself sort of the U
platform plain developer
experience for the uh good old vort
object what you need to consider when
you want to build an Excel layout on top
of a vport or design a new vport using
Excel one of the key features you have
to remember when you want to do excel is
the new property that we highlighted in
yellow because that is the one that
specifies that all top level data items
go to individual sheets which means that
you get a much more comprehensive data
set the other part that you have to
think about just Che the headlines now
the data set definition
itself you have the request
page layout section with the uh number
of lay layout that you want to have in
your vort one or more and a group of
labels that you want to have when you
have built all of this you can publish
your vort extension and start to play
around with
it data set and data items are the core
elements in the vport definition because
that is where you define what do you
want to have in your
data data items m to the tables and
columns are to the fields in your
individual uh tables and you can have
nested and you can have multiple boot
items for instance this case here where
we have three different root items that
will end up in three different data
sheets in the Excel
workbook you also have to specify a
table view where you can see the defin
the Sorting you can also set filters
that you want to have
predefined but be be careful here that
you don't filter too much
out for the request page like the other
reports you define the filter fields
that you want to have and it's a good
suggestion to find the most important
fields and let them be on the request
page from the beginning so user don't
have to search for them or add Fields
individually and there's a small hint
that we we found out that um many times
you use these buffer tables for data
items sort of temp tables where you
calculate stuff based on other tables
and fill it up if you can then stop
doing that because it
actually takes quite a lot of memory
from the NST when you B on the uh
Solutions and there are some small other
hints that we come up to later
on when you have this multi worksheet
then we have the definition that the
name of this root data item the first
one in the list that will also be the
worksheet
name in the Excel workbook like you see
here but we have the data contract
between the data set defination and the
Excel workbook for the sheets that we
have that we will fill out the data so
we have the sheet names they are the
same as the data iton names and we have
the column names that map to the column
s in the report definitions you cannot
change them because that will break the
contract and if we look a little bit
deeper into how the data is organized
and compared to the Legacy way we did it
before if you look at the same set of
data here the green ones are the actual
data whereas
the we col it are the null fields that
means that we have a lot of of repeated
data and if we just want to have this
one it's actually map to the single data
sheet we have in the new implementation
with multi sheets enabled so always take
that one if you migrate old sheets you
start by Def defining the Excel multiple
worksheet as two then you update the
data
sheet and it also have a huge impact on
how big this Excel workbook will be and
how much time it actually takes to
render it because if you have this
multi-work sheet enabled you actually
get a three times size reduction which
is quite important when you have the
bigger sheets and there's also the
benefit that the risk that you hit the
Excel limit of 1 million rows is much
smaller because we can have 1 million in
each sheet previously we just had one
sheet and it was easy to hit the limmit
and then nothing you could do about
that one of the key element that we have
that is crucial for especially
translation feature later on is how you
use labels in your bort
definition and there's several places
where you can use them you have labels
in the vort object itself which we use
for
headers you have column labels for each
column in the data item and remember
that they they are only included if you
have this include caption property on
the column otherwise they will not be
there and if you really want to
customize then think about using caption
class on the fields that sits behind
this table because then you can program
the caption yourself is not
static and where will these uh caption
data go in that we have a new caption
data workbook sheet but we get all the
captions in both for columns and
labels with the current language that
you have when you want the
report and you also have the option for
overriding if you don't like the value
or you want to have a different language
in or a new value then we have a
different sheet called translation data
which is a user defined sheet containing
custom data that we will not touch when
we update the workbook template
one of the last thing you have to
remember for request page we have these
about text about title that some people
will think sit on the report object and
can't find them but they are actually on
the request page because it's a UR
element and we use these two strings for
defining text that user can see for
instance this a trial balance Excel
dialogue is shown when you show the
request page for the report and we also
have it in the aggregated metadata sheet
where we have the two strings that you
can use in your
workbook one of the last things is the
layout we always use the new rendering
syntax which is a element we added to
the AL ports a couple of years ago when
we added the weord extensions and here
you can add one or more
layouts to a
report and here you have to remember if
you want to do it nicely for the users
caption and Su of are optional Fields
but they actually appear in the pages
that the end user can see when he wants
to select the layout or select the
layout from the request
page and you should remember to set the
default rendering layout in the report
object property
if you have a already warning report
then it's quite easy to add something
new to that one because what you do is
you go to request page you simply do a
send to and save the data set in a new
Excel
document download that one and you can
add it to the existing vport in the
layout section in the wending
section and start to update this layout
with whatever you need to have so it's
quite easy to
add and when you're done publish your
report
extension or if you want to play around
you can also use the uh page and have a
sort of a user defined layout that you
just have in application
side this one here we just add
one and for the end of the platform part
let's let's take a look at some design
considerations that you have to look at
when you define the report
itself look at what columns you need
don't take too many but don't ignore the
one that you might be using later on
because it's
easy easier to add a new layout than to
start with a new version of the
vort think about data item filters don't
filter too much
away and think about limits Excel can
handle 1 million rows in the
workbook but really consider if this is
necessary because it will take time for
Excel to load the workbook and if you
have too many 1 million V sheets it will
take more time than you want the end
user to spend on it and you should
always think translation into the design
here so in UAV vort extension Define the
translation file and make sure that you
get all your labels transl
pled and one of the last things to
consider if you want to have uh captions
don't use Virtual tables virtual tables
are platform tables that are in memory
and they don't have field captions so
you don't get any translation you don't
get any decent values for the
captions and one of the last thing you
should consider the data aggregation
where do you actually want to aggregate
your data do you want to do that in
Excel or do you want to aggregate in BC
and just have a limited set of rows in
Excel that depends on how much you want
to operate on your data in Excel the
more you aggregate on BC the less are
your options in
Excel so that was all more or less the
platform part and now we go to the magic
part thank you
NRI so now we are going to start with
Excel Magic and for this thing we are
going to recreate the trial balance
layout and the best way of doing it is
simply if you build it and publish it
you're going to get the default template
inserted and when you download it you
will get the Excel that you can work
with now I have done this just to save
some time it's speeded up it's not this
fast of course and now if I switch to my
machine to show you the demo it's the
same layout it's completely blank and it
has these sheets that Neil Henrik was
mentioning so you're going to get the
translation data caption data and we are
going to get three data sheets here the
reason why I'm doing it like this is
because it's much easier for me to code
and to make things in Excel if I can see
the date otherwise it's becoming quite
difficult without the date and the first
thing that we are going to do is that we
are going to start with power query and
also based on the pool not many people
more than 90% have never ever used the
power query and for this part we are
going to be using
Excel as PowerPoint and if you're
wondering how you can turn the Excel
into PowerPoint you just go here and you
uncheck the grid lines and now it's a
PowerPoint the Excel Masters say that
you should not be using PowerPoint but
you should present everything in
Excel so the thing that I would want to
say to you if you have not been using
the
Excel so yep I have been using this
power query a lot and I love it and I
would strongly recommend to you to try
it out I like it so much I made a meme
you know like how I'm looking when I'm
coding Excel I have been maintaining our
existing layouts and using macros and it
was not a fun experience at all with
power query you can do almost anything
that the macros can do and I in
Microsoft we want to stop using macros
you can use the macros in Excel they're
not going away Excel team is going to be
supporting them however Us in Microsoft
we don't want to use it because it
presents a security risk and it's also
also complicating our code
review
significantly power query is a shared
technology so you can use it both for
powerbi and Excel its main purpose is to
import and transform the data and the
language that it's using it's called M
and it's not only Excel and powerbi you
can export it to anything else like you
can use Microsoft Azure data Lake
storage data versus Excel powerbi it's
able to connect to the database local
files and even web services to read the
data from it and to write the data to
all of these endpoints so it is quite
powerful the good thing about it it's
also it's very easy to use if I would
select everything here to use it I just
need to go to data and here I can say
from table
range and I'm already in the power query
you don't need to learn M you can use
the UI and there is a lot of things that
you can do in UI the first purpose that
it is excellent for is strongly typing
your data set the thing here that you
can see is that the account is it thinks
it's an integer because we only have
numbers and we all know that the account
is not the integer but it is actually
text so we are going to switch it like
this and we will replace the current
step because it is wrong then if you
scroll a little bit more to the right
you will see that it thinks for some
decimals that it is integers and this is
because we only have zeros in the demo
data set so you can see here change type
and I want it to be a decimal
number additional thing that you can do
is that if you don't want something like
I do not want this cell I can just say
remove and then you're building steps on
top so you're building the
transformation of your date it's quite
powerful so as I said you can get web
services you can transpose the different
columns and rows replace the values fill
the blanks there is quite a lot that you
can
do however the two main things that we
are doing is one the first one is that
we do not want any null values so you
will see this in our Excel layouts so we
say replace null with
blank the reason why we are doing this
and I also would need to do it
here and ideally it should be a single
step so I don't pollute the steps the
main reason why we are doing this is
because if you want to build some
Advanced table relationships you're
going to get this kind of error if NS
somehow end up in the data set and this
is confusing to the end users so we want
to be sure that this case does not
happen and also one of the things that
we are going to do in our data sets is
that if null is in the decimal we are
going to set it to zero also for the
date times we are going to set it to
something like 100 years in the past so
it's clear clearly visible that
something is wrong does but still to be
able to use the data that we have
created in our layouts you will also see
that we have suffixed all of the queries
with query with underscore query and the
reason why we did this to be able to
distinguish what is a query and what is
actually the data sheet that we received
from the
platform and basically when you're done
with the transformation the thing that
you can do is that you can say I want to
close this one and load it to something
else and now I'm not sure how much you
can see but the options are table pivots
and only creating the connections so we
are usually loading the main data into
tables because we want to enable the end
users to use the data if you have
something that you want to keep in
memory you can only create the
connection and then it's kept in memory
so if I would say here please load it as
the query now I'm getting all of the
transform data and it's ready to be
exposed to the end
users if you want it to refresh when the
file opens the way of doing this is if
you click
properties and you have the following
options this background refresh needs to
be unchecked because the background
refresh is loading the data
synchronously so if you have multiple
queries pavots the data is not going to
load properly and then the user will
need to click refresh all and you want
to check this one yes I want it to
refresh when the file
opens and of course you want this
refresh all the last option is enable
fast data load this one is useful to
help you to load the data faster however
the UI is going to be less responsive
but since the user needs to wait for
this it's a good idea to check
it now we could do the same things with
the dimension one and dimension two we
could maybe even merge these queries so
you can get a nice dimension name here
that's very easy to do however we will
not have time in this presentation to do
it so now when I'm done with
the um Power query it's time to move to
the next topic and the next topic is
Pivot tables because this is a frequent
request from the customers and people
are asking a lot for the pivot tables so
I'm going to show you how are we usually
building the peot table so if I would
create a customer facing sheet and move
it to the front the way to do the pivot
table is going just like this and I
would say insert from table
range and here I can select the entire
query and now the pivot table is more or
less
ready and now I can insert the r here
I'm going to set the account and I want
the account name and I also want the
account
type and the things that I want to
summon is for example
balance balance debit and balance credit
and let's also put the net change for
example right so this pivot table is
already nicely shaping
up uh the trick that we do is that
sometimes you don't want this tree
because in this case it is looking ugly
uh in some cases you want the tree to be
able to expand and collapse however in
this case we are just listing the
additional columns and this is the trick
that I got from Jeremy
Visa so to get the table rendering more
nicely is that you go here and you can
select how the pivot is being shown and
one of the common options that we are
using is to show it in the tabular form
like this and then if in the sub totals
you say do not show
subtotals then you're getting its
rendering nicely so this is something
that we
want and we are using this pattern a lot
actually in our code and the last thing
that we need is that if we go to the
pivot table
options and here we want to uncheck this
expand collapse
buttons however we need to say we want
to refresh data when opening file and
now when when the customer opens the
file the entire data is going to be
automatically loaded and
reloaded so that was the second main
component that we are using the third
cool thing about the a layouts is
translations translations are extremely
valuable and this is something that our
end customers are asking for a lot and
this um previous report layouts are
supporting this and we needed this to be
supported in the new one
also the problem with Excel is that
Excel is not handling languages really
well Excel is usually being delivered in
a single
language uh so in this case we have
something that is quite unique in the
market and this is our ability to
translate in the sheet without writing
Al code so to show you how you can do
this one is that you can go to the
caption data and if you select this
trial balance
lcy and you go to the sheet the only
thing that I need to do is that I need
to put the dollar signs around it and
now the platform is going to
automatically translate it by using Al
translations so when we are rendering
this report in the platform we will go
through all of the dollar signs dollar
caption dollar and if we can match it if
it is matching the data that is listed
in the caption data we will
automatically translate the
values uh Neil scan quick question on
which elements are we be able to use use
this we can actually use it in most of
the UI elements in the Excel workbook
both for Sheet names headers we can use
it in pivot tables charts all the places
where you usually have captions that you
want to show to end users yes so but
that could be of course be places we
haven't found yet so if you find
something that is not translatable then
just let us know we fix it yes so I'm
here updating the captions while Neil
Kenrick was speaking and and now we can
get this entire pivot table together
with the sheet
translated also the translations work
with something like slicers so if I
would like to add a
slicer on the dimension one code you can
also get a slicer translated however be
sure that you are translating a caption
and not the name of the slicer and in
this case all of the UI elements are
going to be automatically it's quite
important but you always use the
captions in the UI elements because
names are Excel internal so if you try
to do a dollar in front of a name Excel
will
be uh will show an error later on next
time you try to load it yes and to show
you also second thing
here yep uh some of the UI elements are
not going to be translated and the
things that will not be translated are
the things that you you cannot change so
for example Grand totals that's going to
be in the language that the Excel is in
because Excel is not going to let you to
change this value it is something that
they type in
automatically um if I would like to add
an additional language for example let's
say that I would like to add French do I
need to go to Al or can I do it in Excel
you can do everything in Excel because
what you do is you go to the capture
data mhm
worksheet and then you copy all the uh
key values okay and paste them into the
translation data sheet which is a user
sheet mhm and here you can add the
translation language that you want to
have and you can paste in the translated
values that matches this uh key
value yes so something like this I have
it's already
ready it's a she cheat sheet so there's
no need to involve an Al developer just
to get a new language for your Excel
workbook you can do it yourself and
basically if I would like to add
something like here that I have in the
cheat sheet like hello Tech this am I
able to do this as well so because you
can simply add a new caption key for the
uh translation data sheet and then add
the languages that you want to have for
that one so it's easy to add new strings
to the system you simply add them to the
the translation data workbook and add
the values that you want to have in the
language you want to have and the
languages are using the uh usual culture
names y so we can have multiple and the
default value if you don't specify
Anything Is Us
English all right so I think we are
ready right I should only also provide
the English us here if I would like the
default
right because I don't have it in the
data set so I need all of the languages
that I want this
one
super so when you're ready and you have
done everything and we have this small
XL layout here the thing that we usually
do at the end is that we clean up the
data like
this and here we delete the table
rows and then if we go back to the data
and we refresh everything you can see
that now it is blank and this is a very
good test if you have forgotten some
references in general you will see also
our layouts that we ship them with no
data and from the power query you can
see this blank text that automatically
got
replaced now if I forget to clean some
sheets what is happening then yeah the
platform will take care of it so when
you import the new layout with data we
will delete the data when you import
imported because you really don't want
to have data in a layout that can be
sent to a different customer in a
different company so we try to make sure
that you don't share data by
mistake doing layouts all right so
Microsoft has turned on some security
here and I need to change it to non
business yes otherwise I would not be
able to upload it and here if we would
like to run it we can do it also without
any code so I can go to upload the
layout
mhm and the way how I do this is that I
type new and then I call it Tech this
demo and I say okay and here I can
select the layout and I was making this
one the thing that you also need to do
which I didn't do is to close it and
save it because otherwise it's not going
to let you upload
it which is a good safety check as well
that you have saved everything that you
need and here if you filter and you set
the filter to
be this ID now we have the tchas demo I
have switched the language to be French
and now if I say run report you will see
that we are running in French and it's
going to run and when you open
it the thing that you will see it is
moou Tech days there is no big red
security warnings for macros so you can
just enable the content and everything
is outo loaded and
refreshed so yes this was a short demo
of how you can add the additional
things and get the translations
enabled now for the other cool things
that we will briefly mention here one
thing is the aggregated metadata sheet
and this sheet here is actually hidden
so if you say unhide and you say I want
to see the aggregated metadata sheet in
this sheet you're going to get a lot of
information about this report and about
the environment that created it so
you'll get some information about the
platform and the report itself here is
the environment information so you can
see the environment name you can also
see the company name and Company ID
company name is useful if you want to
show it in the sheet so the user is able
to see to which company does this data
belong to while the company ID is very
useful if you want to consume the data
through the apis you can use BC apis and
show the data straight into this Excel
layouts there is a username that has
created this report also the date and
the language that the report was created
additional usage that you can use this
one is to create the lookups into the
bcui from the Excel which is also a
really cool usage if they would like to
find additional data they can use lookup
we also emit the uh request page filters
so if user has filtered something you
can use this information to show it in
the UI there is a cool feature as well
that we are going to change the existing
um functionality and this one is called
uh names and you can assign the name to
the variable and we are going to start
using it more in our layouts because it
simply ifies formulas
significantly now Neil Kenrick just to
ask you quickly um if people would like
to remove this aggregated metadata sheet
is that possible automatically or not uh
currently we don't automatically delete
it but there is no nothing that prevents
you from deleting the sheet if you want
to send your Excel workbook to someone
you can simply delete it it's not needed
and if you delete it from the layout it
will be recreated when you want the
report so it's a machine generated sheet
that can be removed if you don't want to
but if we get enough feedback uh we
might add an option so the sheet will be
optional if you don't need it for
instance if we always want to send
workbooks to external parties but you
don't want
to show this information then we can
make it
optional
super now for one thing that we do not
have time unfortunately today is about
applying 10 templates and styles we are
going to publish the guide how you can
do it in less than 3 minutes there are
few tricks that you can do in Excel to
do this rather quickly and the developer
that did the sustainability reports done
them in the green layouts and then he
was forced to apply this blue team he
wasn't very happy but he was able to do
it ra very quickly you know with the
tricks that that we did there are
refreshable AEL layouts Tanya has done
them and also rato has promised to write
something about it we have an extension
to generate the data so you can demo
them in a nicely way and it was done by
Jeremy whiska and you can also build the
dashboards there is a really nice Excel
topic how you can create and manage the
dashboards in Excel one of the things
that we wanted to do and we received the
feedback from the Excel team that we
have too many slices and the Excel guys
have recommended to us to create the
first sheet with slicers and then this
sheet can control all of the other
sheets so you know you go to the first
sheet you set how you want to see the
data and then you can just navigate
across the tabs and do
it and before we move on I forgot to say
one important thing that I got from AJ
Ansari so I'm going back to the power
query there is an excellent topic which
is called dashboard in a day and this is
trainings for
powerbi however they're explaining power
query in really nice way with large
amounts of details and here you have the
instructor content link that you can use
to download it and there you will find
really nice trainings about the power
query
yep and that was it so you got all of
the information that you need so now
you're ready to become an Excel
Wizard and we are going to switch back
to the
slides MH and if your for on so we would
really like to hear back from you and we
would like to invite you to try out the
things that you have seen today you can
join us on ymer and please provide
feedback here to the things after trying
them out we are also very interested in
the things that you have done so we can
see how you're using the platform and
all of the things that we did
and we are going to be posting
additional content with larger level of
details also additional tips and tricks
in Excel on the Yammer because we could
not cover everything today the goal was
to give you an endtoend overview of how
does the process looks
like I would like to give a special
kudos to T Tanya for writing these
comprehensive guides how you can build
refreshable apis how you can use
refreshable apis in Excel layouts she
has written an excellent documentation
topic stepbystep guide that you can use
to create the
refreshable Excel reports and the last
thing that I would like to say is that
when you're designing the Excel reports
think if it needs to be frozen in time
or if you want to use the apis one of
the limitations that is preventing us
from using the apis is the fact that
it's hard to use the apis with request
pitch so if you want to get a nice user
experience
refreshable Excel layouts do not it's a
little bit hard to do it with the
request
page yes and we'll have some time for
questions
yep so where is the
box I see
it so who had the question one over here
yep MH good hi okay um uh the capture
and the translation are picked from the
Excel Excel f
file yeah I I can hear you huh sorry you
were saying what can you repeat the
question the caption and the translation
yes in in the the Excel are picked from
the Excel f file uh they are picked up
from the a object itself so the the
caption work sheet is generated when you
want the report so the captions will be
written to the Excel workbook in the
language that you have when you want the
report instance so when we go to request
page or do send to Excel or you want the
report then we get all the caption data
and store in the caption work sheet with
the language that you have selected okay
yes so to show you this one is that if
you say include caption on the field as
Neil SC said it's going to be
automatically emitted as translated
value and there is also a label section
if you want to defy the global labels
you can find it in the code
here so I think it is somewhere around
here you see labels and these are Global
labels the also cool trick and thanks
for asking this is that you can get the
dynamic translations if you use the
caption class three and this includeing
data sets in our reports that we did you
can see that we are automatically
replacing the dimension quotes with the
actual value so you can get these
translations on the Fly
okay okay okay then yep any more
questions yes over
here I have two questions the first one
is
uh can we hide uh this uh additional
caption sheet and the other one with the
languages and is it going to cost a pro
uh uh I mean when we when we create the
XL as a layout can we uh hide it preh
hiide it so that when the report is
printed it doesn't show them yeah you
can all of the uh data sheets uh that we
generate and also the translation data
sheet can be hidden but before or after
it is printed no if if you upload the
layout or if you put it in the extension
whatever you put in it it's going to
become default for everybody so if you
see here I want to hide all of these
things mhm and you hide the
information it's going to be saved and
you know you can just hide it and then
each time when you download the layout
it's going to be hidden out of the box
and if you print the report it it will
also not show uh at uh it shouldn't but
you control what you print
right uh I would need to check this one
because yeah we didn't test printing
that much okay okay uh I believe that
there is probably a way of just saying
that I don't want to print these sheets
I would assume yes this this this is my
question can I say print only the data
like uh uh the data from the data sets
without this
additional uh sheets okay and the the
second question is about this power
query thing that you
showed and the additional sheet that you
created you said that uh it creates a
connection does it mean that if we save
the report so we print it and we save it
and uh tomorrow we will open it again
and it will refresh the data
automatically or we we or we have to
print the report again it it all depends
where you're getting the data from right
in my example I have downloaded it from
BC and then we are getting the data from
the sheet and it's going to stay like
that forever right uhuh okay but if you
use Tanya's example where she's reading
it from the API then it's going to be
refreshing it all the time okay and it's
up to you how you want to build it right
do you want it frozen in time like this
was the state today or if you want to
enable them to use Excel and not to go
to BC to constantly refresh the data can
also be more advanced multiple queries
in the workbook and some that they read
data from the report and something read
data from other
sources it's up to your sort of that's a
challenge for
you um any other questions or we are
also a bit over time
yeah let's do one more and then oops yep
almost then come down and we can discuss
what's St we are asking if if you have
created this layout now and and put it
in the report then you need three
additional colums in one of the data
sets yep how do you handle that because
it's very simple so if you need the
three additional columns in the data set
yeah you can go straight to the data set
and add them and they will be
automatically exposed to the pivot
itself or you can just add the three
additional columns to your report and
then you go to the template that you
have and you expose them in this data
tab that I have just hidden so I cannot
show you right okay so I can add add the
manually yes you can add a manually okay
perfect right Neil scri I'm not saying
something and if you for instance have a
a report that you want to extend we also
support the standard vort extensibility
so you can go and add new data item
new columns to extension on top of an
existing report no problem you would
need to update this one and also the
query if you're using the parkw and then
the pivot is going to automatically
get yep all right thank you all very
much
[Applause]
