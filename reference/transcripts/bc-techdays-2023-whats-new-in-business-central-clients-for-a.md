# BC TechDays 2023 - What's new in Business Central clients for AL developers

- **Source:** https://www.youtube.com/watch?v=8rrFDGa8y-w
- **Video ID:** 8rrFDGa8y-w
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 39m10s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

hello everyone welcome to this session
where we talk about what's new in
business Central clients for Al
developers I am Mary Dan orcha and I'm
vasu Lilia and we're both software
engineers in the business Central
clients team
so during this session you will learn
how to unlock the latest user
productivity features such as actionable
error messages for mail code
you'll also discover which new features
your users can enjoy without you writing
a single new line of Al code such as
analysis mode access keys and more
Additionally you will also get an
exclusive
of what new apis we're planning for the
Autumn release
so a brief look at our agenda for today
of course we're going to talk about
features that you already see and can
use with business Central version 22 so
then again we also have some exciting
things coming straight from the lab and
being unveiled here for the first time
we don't want to tell you what those are
yet so we'll just keep the suspense
going for a little bit longer
let's get started with the first item of
the day and that is access keys with key
tips so access Keys boost your
productivity in business Central with
quick and easy keyboard access to
navigation and actions on any page
you might be already familiar with this
feature as you've seen or used it in
other Microsoft 365 products such as
word excel PowerPoint and so many more
but let's go and see how this works
within business Central and why it does
boost your productivity
whoopsie
okay I'm now in business Central in my
role Center
of course your first question is how do
I get to see these access keys or
keytips well all you need to do is press
alt on the keyboard and you will see
these characters popping up next to your
navigation menu so your navigation
groups or the links that you have
bookmarked to pages that use very often
and also next to the actions we call
these characters key tips and what key
tips do is they allow you to press one
character in your keyboard to invoke the
item that they're shown next to so let's
say I want to start a new purchase order
in my actions I will press X on my
keyboard and you'll see that the key
tips will appear for everything under
the actions and if I wanted to start a
purchase quote I would just press P here
but let's say I don't want to do that
and I want to go back to navigation so
how do I get back to the previous
context what you need to do is just
press escape on the keyboard your backup
will level where you started
so for navigation I will press J because
apparently all of them start with j and
we'll go back to this later and explain
why all of them start with j
let's go into sales and you'll see the
group is expanded key tips appear for
everything under sales I want to go on
to customers press C
okay in the customers list yet again you
have your navigation menu you have your
action bar you can use keytips again
just press alt and you see keytips
popping up
now what do I want to do here well for
the customer that is already selected I
want to start a new sales quote you can
easily do that by pressing n as we see
new document has a key Tip n and then we
press s for sales quote you're on to
starting your new sales quote and then
again the sales quad you have an action
bar you can use keytips again
well that's great we can use keytips
but how do they help us
well when you have daily flows that you
do very often it's very easy to memorize
the access keys to that flow so let's
say we started a new sales quote without
NS if I do that very fast on the
keyboard I'm already starting my sales
quote even faster than it would have
took me to go there with my mouse or
even worse with the keyboard tapping and
using your arrows back and forth
so that's how you can be very efficient
using key tips
okay apparently they're great they're
useful they help us so much what do you
need to do for your customers to be able
to use key tips well nothing really
except get them on the latest version
which is version 22.
we generate key tips on the platform and
you don't need to write a single line of
Al code to get key tips
okay that's great now how are key tips
determined by us well we use the actions
caption or if there's no caption the
action's name and typically for the
actions that we want you to get to first
in the page you will see the shorter key
tips that are just one character long so
we see that now for home new document
and you can also see that the key tip is
typically the first letter in the word
or the first letter in the second word
there's also some cases
my resolution is quite High here and you
cannot see the rest
um but yeah there's also some cases if I
go into more where report for example we
have the key tip T and you see that it's
not the first or the second character
and why is that well for some of the
actions that we know that customers use
very often throughout Pages we want to
make sure that we have consistency in
different pages so that you always use
your access keys in the same way and
therefore we have a few preferred key
tips that we assign to actions
you also see that as we said before for
navigation groups they started with J
for the action groups here they start
with X if I go back up a level with
Escape you'll see for some of our system
actions they start with that
why that is is because we want you to
give we want to give you a context when
using key tips so if you're into
navigation you press J and you only have
the subset of the contacts that you want
to go to
okay
we learned about key tips how we
generate them let's go back and see a
quick cheat sheet on how you can use
keytips so we said we can open the key
tip mode with alt you can move around by
either activating key tips with a
character that is shown on the keyboard
or you can even use your navigation with
the arrows up right left and so on and
of course execute tips by using Alt as
we saw the feature is available for
navigation menus navigation links the
primary action bar and the roles
interactions
of course if we see that you love the
feature we will try and expand it in the
future
now we come back to a point where you
know about shortcuts
we use the keyboard to invoke actions
but also keep access Keys we use the
keyboard to invoke actions what's the
difference and why you need both of them
well keyboard shortcuts are defined in
Al by developers whereas when it comes
to access Keys they're generated by the
platform
and given that your keyboard shortcuts
are defined by you in al they are only
available for those select actions that
you define them on but for Access Keys
they're assigned to all the actions in
the page
going back to keyboard shortcuts since
you defined them the same action will
have the same shortcut in all pages that
it's shown in for Access Keys as we as
we showed before
the key tip that is assigned or the
access key that is assigned it depends
on where your action is shown so if
there was an action we have print and
post for example they both start with P
if post is shot on first then it takes B
and print for example will take R that's
uh something and therefore
since position and determines access
keys that means that when you move
actions left and right their access key
might change
book keyboard shortcuts of course are
not affected by personalization
now when we talk about personalization
what else do you have to share about it
thanks Sarita so previously actions in
parts were determined by Al and users
didn't have the opportunity to organize
their actions in parts of the way that
they wanted so that in order to do that
it required writing new extensions so in
version 22 we enabled personalization
mode for action bar in parts so if we go
to the product now and we enable
personalization mode we can see the same
designer experience for the action bar
in part as for the main action bar
so this is built on the same capability
as the main action bar which means that
you get supports for split buttons and
of course teaching tips which means that
you can now write onboarding and
teaching tips for your actions in parts
so in order to get an easy access to
actions you can promote split buttons on
the root level or you can drag and drop
an action into the manage group as the
manage group is the pinned Group by
default when you access the page
so since we introduced personalization
of actions in parts we also added a more
granular clearing of personalization
but be aware that
if you clear personalization in Parts it
will reflect on every place that you
reuse this page
and this feature is only available when
the modern action bar feature is turned
on so if you haven't done that already
make sure to flip the switch and give
the feature a try
so what else do we have for productivity
so another boost that we're giving to
your productivity for your users is
being able to analyze data on list Pages
this allows you to quickly extract
insights from your data in business
Central without having to switch to a
different app run a report or involve
your developers to write a new report
when you analyze data you can design
filters columns grouping and pivots you
can save your work work across different
tabs you can find column totals copy all
your data and import it to excel
PowerPoint and anywhere else you need
um let's start with noting that this
feature needs to be enabled via feature
management
so I'll go into the products and see how
we can use analysis mode
when you're in a list page in business
Central you'll know that this feature is
enabled when you see the analyze toggle
shown on the action bar to get into
analysis mode all you need to do is just
enable this toggle
when we're in analysis mode you no
longer see
um the actions that we had on on the
action bar because we want you to be
able
um to focus on analyzing your data
instead of manipulating it
so when I start analyzing I will let's
say start a new tab because that is my
old analysis
I typically like to start by clearing up
all the view and starting from scratch
now let's say a few terms first when
you're analyzing this area over here as
I explained with the tabs is called the
tabs pane you have your data area where
you can see all the data from your list
and of course you have your field
modifier area over here to the right
that I expanded right now
so as I said I like to start from a
clean slate I will just double click
this checkbox and then get rid of all
the columns that I was showing
I'm in my customer Ledger entries and
I'm interested in seeing what customer
is generating the most revenue for me
so I will start doing that by first
looking at
um what tape what columns I'm interested
in that would be the document number for
example the customer number or name
maybe the name makes more sense I'm not
a machine
um and then of course I want to look at
the amounts for all my invoices or
document numbers and the remaining
amounts
okay now I can see the data that I'm
actually interested in analyzing you
also have some quick insights to see
that you have 416 rows in this list and
of course that is a long list to scroll
so we don't want to do that
how I can help myself is of course I can
group my list by a certain column and
how I do that is if I want to I'm
interested in one customer right so I
want to see what customers generating
what Revenue I would go and drag and
drop the customer name into the row
groups and you will already see that
everything is immediately grouped
now that looks good you can of course
select your data to find out what is the
minimum revenue from a certain customer
the maximum but of course you can also
do that by sorting and I can see that
the School of Fine Art is the highest
revenue
and then trade research gives me the
lowest Revenue
so that's looking good maybe you can see
that also some columns are do not have
enough space to show the whole title how
you can fix that of course as in Excel
you can make the column wider or you can
wrap your column headers to see all the
text or of course of course you can also
Auto size all your columns to fit
now that looks good for the first part
of my analysis but maybe I want to get a
bit more granular and look at the data
throughout different quarters
[Music]
and how I do that well I'll go back into
modifying my columns and my groupings
and since I'm interested in looking at
all these data based on the dates I want
to go into pivot mode
and find out a bit more so when it comes
to working with dates business Central
enables you to not only look at the
exact dates but also look at the year
that the item or invoice was posted on
you can look at the quarter or the month
so I want to do an analysis on quarters
as we said of course I would select that
column to show up and then I want to
Pivot on it so again we use drag and
drop to get the quarter and push it over
to the column labels and you can see
that q1 already showed up in here
now I also want to do the analysis on
quarters for you each year so I'll also
select that year
that column called year and drag it over
to the column labels that I'm pivoting
on of course they accidentally showed up
here for me but it's very easy to remove
them from the grouping as you have your
row groups right here and I'm not
interested in grouping by quarter or
year so I'll we'll remove them
okay so I have my data and you can
expand and collapse to look into it
there's so much that I have to
horizontally scroll well as we said you
don't need to do that of course use the
auto size option for all columns to fit
and I have a bit too much so I'll
collapse again
and make my columns a bit bigger
okay so that's looking good I can look
at how every quarter looks for different
data I think
I added too many columns to this because
amount is somehow interior twice
very easy to fix
this is also in here twice then I have
some leftover filters that I'm not
interested in but of course the fix is
just get rid of anything you're not
interested in
so I'm looking then at the different
quarters within a year if I want to
actually compare how quarter one is
doing between different years all you
have to do is switch the order that you
put them in in the column labels and I'm
more interested in quarters throughout
different years and you see in quarter
one for your 2021 2022 and so on so it's
very quick very efficient I can go
straight into exporting this data and
sending it to my partners and so on
so this looks great because it allows
your customers to do data analysis very
efficiently
but you can also analyze data based on
what your customers are analyzing data
on that sounds a bit like a brain teaser
what I want to say is that you can see
if your customer and how your customer
is using data analysis by heading over
to our power bi usage reports and going
into client actions as you see over here
looking at usage across customers for
client features such as data analysis
and you can also go deeper into this
data to see on which Pages your
customers analyze data on to be able to
give them more tailored reports per user
or per page
now when we talk about working with data
bulk data entry and working manually
with data very easily leads to errors so
busy will tell us a bit more on how we
help customers in that case
so errors are a great cause of loss of
efficiency and contribute to poor user
experience and this is mainly because
error messages are often cryptic so
let's go to business Central and I'm on
a sales order that is a status release
but I want to change the contact
I perform that modification and then I
counter this issue and to most of you
this is enough to understand what needs
to be done
but to a regular user this seems a bit
cryptic a bit robotic because they need
to discover that they need to access the
release Tab and then reopen an order
so what can you do in order to improve
this and make your users more productive
so in version 22
we added two new first of all sorry
let's take a look at what the code does
at the moment
so we subscribe to this event where we
test the status of a sales header and if
it's not of a state is open then we just
throw an error to stop execution
but in version 22 we introduced two new
apis on the error info object which are
add action and add navigation action
so how can you help your users be more
productive
so right from here you can add a more
user-friendly message that you can
explain to the user why they encounter
this error
and you can add an action to help them
resolve the problem right there from the
error dialog
so what this method accepts is the
caption of the action that you are that
you want to display the code unit ID and
the procedure name that resolves the
error on behalf
so I've written a small procedure in
here that reopens a sales document where
I get the sales record by the system ID
and then I perform a manual reopen so I
can go ahead and then copy the name of
the method and then just add it to the
action and then just throw the error
so let's see how this looks right now
I perform the same thing
go to change the contact and then I see
this
so I think we can all agree that this
looks much better than previously so the
users can just reopen the order right
from here without losing any context and
then go ahead and then just perform the
modification that they initially wanted
to
but we saw another method which was ad
navigation action so let's take this
example I want to go to the warehouse
pegs page
and then I navigate to it and then I
encounter this
so
a bit better user message but
I'm still confused like what do I do how
do how do I resolve where do I go from
here
well what's currently happening is again
we have a subscriber that every time
that we check for if the user is a
warehouse employee and if it's not we
just throw the error
but this is not that straightforward it
requires a bit decision on user side so
uh
what can we do in this case
so in here we can add a navigation
action we can help the user to the next
step of resolving the error
so this method accepts just the caption
name but you need to remember to pass on
the page number where you want to take
the user
and of course maybe improve the error
message too
so if we go here and then I perform the
same steps
I want to go to Warehouse picks
and then we say this
much better so I can go from the context
of what I wanted to do right here to
perform these steps that I need to do in
order to resolve the error so when uh
how do you get to use it yourself so
when you get to decide
how to help the user resolve the error
and how to use these two methods you
need to think about two things so in
order to use add action you need to be
certain of the expected outcome how to
resolve the error so we saw the example
for the sales document we knew exactly
that the status needed to be opened so
instead of relying on the user to go and
find the action where they can do it you
can just hand them the solution and make
them more productive but for the
navigation action like it requires a bit
more decision on the user side like
there are multiple steps that it's not
that straightforward to um
uh to solve but remember when using the
add navigation action uh if you're not
certain that the user has permissions to
access the page you might cause more
aggravation by showing more error
dialogues so be mindful
and this is currently in preview in our
app General availability will be in a
minor update and these actions are not
yet supported in inline validation bar
but coming soon there will be a blog
post about uh user experience guidelines
to how to help you how to write
actionable error messages
and talking about actions this is a call
to action for you to migrate to Modern
views
so views are just lists that have
predefined filters and previously we
defined these Legacy views as actions on
the role Center
uh show hence how many of you are still
using Legacy views
okay
not that many which is fantastic but
um
Legacy views are being deprecated in
favor of the new modern views which were
introduced four years ago so I'd like to
point you to a guide how to do and how
to go and migrate your legacy views so
as I mentioned these are actions on the
role Center
so all you need to do is just query all
your role Center pages and then look for
actions that pass the Run page view
so this was the Legacy Way of how to
define you and it relied on a lot of
platform magic of how to make this
happen so you can just cut this and
remove it from your role Center and you
can see I have two which is copy pasted
obviously and we can use them all the
more declarative method that we can
Define it on the place where on the page
that it filters which in our case is the
shieldist page
so in here in this in the page uh uh um
in the page we have a new section which
is called views
and we can just paste this and it's no
longer an action it's a view and since
we are already defining it in a place
where it filter where on the page that
is filtering we don't no longer need
this and then we can just pass the
filters
so it's easy as that and what you can do
additionally to improve the uh the
experience for the user is that now you
have the possibility to define a
different layout for each view so you
can just show the data for this
particular view that you wanted so uh
remember
Legacy views are deprecated they will be
removed soon and make sure to migrate to
Modern views
that's a great call to action and it's
also the closing note for the first part
of our session which was the features
and changes that you already have out in
version 22 but now we move on to the
second part and talk about new exciting
things that are coming into business
Central that we're working on from the
lab of course they're subject to change
um but exciting things and I hope you
enjoy uh hearing about them so drumroll
to the first feature that we're
introducing is fishtex editor now this
is maybe not new to you whoa yeah let's
see some excitement
you have seen the Rich Text Editor in
the email editor you've seen it now
recently in the marketing text generator
throughout our different demos you've
really wanted to use it and couldn't
well now is the time that we're making
the Rich Text Editor widely available
for Al developers to use in any pages
there's a few conditions but let's go
into the product let's go make an
extension where I use this editor in a
page so let's say I want to use the Rich
Text Editor to add Rich comments to my
customer card of course how I do that is
I will define an extension to the
customer page
where I will add a new field that
resides alone in a group with two
properties that are quite important
extended data type will be rich content
and multi-line will be set to true so
let's reiterate the three conditions for
you to see the Rich Text Editor in any
page are to add a field with two
properties extended data type Rich
content and multi multi-line set to true
that resides alone in a group
well that's looking good of course if
I'm adding this new field to the page
then I also had have to head over and
add it to the table so also extend my
customer table with this new field that
is Rich Text comment of type blob
now just a second on that on why it
should be blob of course you can also
edit as a text but when it comes to text
we have this 2048 character limit that
we put into our database and then since
we are persisting this type of efficient
text content in HTML format it can very
easily exceed that limit so using a blob
gives you the opportunity to actually
write longer and longer not longer
longer and richer text
um how would that look in the product
well I'm here in my customers list if I
open a customer card I added the comment
after the general group and here it is
you can easily use it write a comment so
this is my favorite customer
and I want my sales associates to really
be able to see that this is my favorite
customer so make the font size huge for
them
and then why is it my favorite Customer
because he always pays on time I don't
have any remaining amounts from him
and that's a huge green flag so
highlight that in green oops lost my
selection
um
there
pays on time without the fee uh of
course we're in 2023 I have I must add
an emoji
there Bridge text that you can add to
your card and use it anywhere you want
so this is good but when it comes to
blobs there's also something that we
have to note on how you read and write
these blobs into your databases into
your tables and that is
let's start here first how do we read it
well I'll just add a page trigger on
after we get current record which will
get the comment from the customer
comments
and again to write this over I will add
inside the field
a trigger on validate
um
and I have a snippet on this
which will set the comment and modify
the record so let's go the customer
comments is actually a code unit that I
added and let's go see how these
functions or methods are implemented
so I'm inside my code unit we're first
looking at the get comment so how we
read blobs is of course using streams
you have to first calculate the field
which was the rich text comment that I
added to the table create your in-stream
assign a text encoding please make sure
to use the same text encoding when
you're reading and writing the blob and
then you will read
similarly when it comes to writing this
or setting the comment we create the
outstream with that same text encoding
and just write this out of course I
modified my record over here in the page
so I did need to do it in my code unit
um and yeah that's about it for what we
have for Rich Text Editor but of course
we have more things to show and the
second thing that we want to show you
from the lab is tell me on mobile
we hope to see some excitement
so when it comes to navigation in
business Central
tell me on mobile allows you to search
for pages and reports on your mobile
devices it gives your users access to
any page from their business Central
mobile app on their phones on their
tablets in the same way as the desktop
version of the popular search or tell me
feature as we call it
so as I was saying when it comes to
navigation and you want to do it in the
desktop version there's so many ways you
can do it at least that's what I think
when you're in the enroll Center of
course you have your navigation menus
you have your bookmark Pages where you
visit which you visit very often if
you're feeling a bit exploratory you
could head over to your rolexplorer and
see what pages are available for you and
then you can get a bit more Curious go
into what is available for all rows and
different roles in different departments
and do that but if you don't have any
time of course what we're using very
often ourselves and what we see you
using is the search or tell me feature
which you can access here in the
products menu bar or with the keyboard
shortcut alt Q so I can search for sales
and I get so many results pages and
tests and reports and so on
if I want to do the same thing on mobile
well I open the mobile app and this is
what I see I have my cues I can click on
them to get to the pages or reports that
they link to and then I also have of
course my navigation bar with my
bookmark pages
but if I want to get to anything other
than that well good luck to me good luck
to you if you're trying this challenge
because it's really hard
so now that we add search me to mobile
devices what you can actually do in your
mobile devices is
head over
um you can go to your navigation Pane
and we have added this new search field
you just click on that and it opens tell
me on mobile I can again search for
sales look at all the pages that pop up
all the reports
it acts as them the same way that I do
in desktop
of course you'll only see the pages that
you have permissions to same as you do
in desktop
and then if you want to let's say find
one of these Pages more often we also
allow you to bookmark any page from tell
me
and of course it's available in the
navigation pane but also you can use the
keyboard shortcut to open it up anytime
maybe that is not very relevant to the
phone but tell me is of course as I said
also available on tablet where you
typically have a Bluetooth keyboard
added or connected to it more often and
on tablet of course as I said either old
queue or you have this new icon on the
top header where you can open tell me
again and have that very similar
um UI that you've already seen on
desktop
I think it's a bit small but um
I think you can see it
Okay so
that is tell me on desktop
very exciting things yeah and onto buses
for something else that we're
introducing or working on yeah last but
not least
in the next release we're working on
supporting
the
come on barcodes Kenner yes
yes come on come on
so uh
how barcos can barcodes are input today
in business Central are either typed
manually which is error prone and very
slow or through some third party which
are not really as performance as
performing this natively
so we are working on supporting native
barcode scanning capabilities where we
are utilizing the camera on the device
to scan and parse the barcode
so uh
let's take let's see what it takes just
to
use this feature
so I'm on a page that I have just a
single field and the only thing that you
need to do is annotate the field with
extended data type and then we see a new
one barcode
and it's easy as that
so since this is from the lab and the
setup is very complicated I've recorded
videos and pictures so you gotta trust
me that it works
but if you don't like you have to wait
to try it out
uh so now we see a new action next to
the field which is similar to drill down
and assist edit but um
when you click on it the camera is
invoked and now you see a different
canvas in the middle which you can point
to a barcode scanner to a barcode and it
scans the barcode parses it and inputs
to the field so let's see that one more
time how fast and snappy it is so you go
you click if you point directly at a
barcode it's easy as that it's so good
so if we want to go and
stack multiple fields of barcodes and
what would happen would see the same
thing like action Associated to the
field and you click on the action scan
the barcode it's input on the field that
is associated to but this is just by
annotating a field with barcode what if
you want to do some
more cool Al logic like invoke request
barcodes programmatically
so let's imagine that we want to put a q
tile on the role Center that you can
click and then you can request a barcode
scan the barcode and use that barcode as
a starting point for more data entry on
a device
so uh if I go to visual studio and such
as every other capability in which we
have so far camera provider location
provider we're adding a new one which is
the barcode scanner provider so you need
to add a dependency to this in your
project and now we can start working
with it
so as I said I'm going to create a cue
part I'm going to add a queue which I
would like to use to trigger and request
a barcode
so in order to be able to use this you
of course need to declare a variable of
the provider and you need to initialize
it as soon as possible which would be on
the open page so you can only do that
if the barcode scanner is available and
it will be available on new devices
meaning on phone and tablet
so I have created my instance and I can
go ahead in my uh on the action trigger
on the Queue tile I can go and use this
barcode scanner provider and then I can
request a scan
so uh
when uh what this will do this will open
the camera experience as we saw and when
the barcode scanner will be scanned and
parsed and available it invokes this uh
trigger this method on the barcode
scanner provider where we pass the
barcode value and the format of the
barcode so I can just create a record
and then open the page
so let's see how this looks like so we
have the queue I can press the queue and
then see the same experience as as it
was for the field
and then we can open the page
so possibilities are endless you think
of what you how you want to use this
we're also exploring the uh possibility
of supporting uh Hardware barcode
scanners as well
so uh
we're glad to hear your feedback on this
so today we saw a lot of features that
we introduced in version 22. boosting
productivity through using access keys
with key tips and personalization of
actions in Parts also analysis View and
then we talked about actionable error
messages how you can help your users to
be more productive and remember for
those of you who haven't already
migrated to Modern views as Legacy views
will be deprecated and then we saw a lot
of new features that are from the lab
such as Rich Text Editor that's coming
to you now and Page search on mobile and
of course barcode scans
so that was for our agenda for today we
have some time for Q a
if you have any questions
okay
yes
error messages
you know how the the passing the method
is a literal string
ing to the actual function name so it
can be searched with ale Explorer
um I'm not aware of uh because I don't
think it's very loud no no maybe we can
say it was it heard it yeah so the
question was whether whether these will
be supported through Al Explorer so uh
I I I'm not aware of that but uh the
ideas website is open so if you see you
can create an idea for it and get enough
app votes for it yeah of course okay we
have a tissue for YouTube okay
um when
so when the tell me is available on a
mobile
um can we disable it
[Laughter]
considering
during future management but if we if
you want us to be a bit more granular
than that would that be specific to
users or just completely disable it for
everyone we're looking forward to
hearing your feedback because this is
still something that we're working on
okay because sometimes we want to you
know like just a fix you know
functionality for a certain user that's
why we want to disable it and just keep
it that way yeah so it would be good and
we are going to be available after the
session in the booth so for any question
additional questions and feedback you
can reach us there uh we would like we
don't we don't have more time
yes so we would like to thank you for
your attention
