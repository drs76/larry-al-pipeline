# NAV TechDays 2015 - NAV 2016 Electronic document management & OCR

- **Source:** https://www.youtube.com/watch?v=lpXW4nJjt3s
- **Video ID:** lpXW4nJjt3s
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 86m57s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

we are running late on the schedule so
for a very brief introduction i will say
that my name is nicola and i'm a
software developer from microsoft
some problem with the microphone i know
okay my name is ciprian i'm also a
software developer and from microsoft
and today we'll be talking about
currency exchange updates ocr and
electronic document management
so to start with the overview
okay
just a second
yes
so in this picture you can see the
full overview this is the big picture
which is showing you to which
services
microsoft nx nav 2016 can integrate out
of the box
so
the boxes in blue are the services that
were available from the version
2015. so we were able to
integrate into amc and get the bank
feeds and you were also able to send
electronic statutory return reports
and the boxes in green are the services
that we have added during the 2016
release
so we have added automatic current
exchange rates
from european central bank and yahoo
you're also able to integrate into crm
and microsoft social listening
so you can get feedback from the users
then we have the
electronic documents
and we support various different formats
people
yoyo ubl and mx
you you're also able to send and receive
the electronic documents through the
trade shift
and lastly we are able to do the ocr
through the document capture
all of these services are connected and
shown through this service setup page so
this page if you navigate to it you are
able to see which services are installed
on the system
for the next version nav 2017 we are
planning to grow this list even further
so we'll integrate to more external
services
so on the agenda for today
i'll start by damming to you the
currency exchange rate updates then
cheaply chiplian is going to show to you
the e invoices and we'll finish
by me demoing to you the ocr
functionality that we can implement
so for each one of these functionality
we will start with a brief demo showing
you the how does it look to the end user
then we will
dig deep into the code and show you some
how does the code flow and
some specifics around implementation and
lastly some generic parts that you can
reuse if there are any in the future
so to begin
for the current exchange rate services
we have implemented automatic currency
exchange rate updates
the reason why we needed to do this is
because this is one of the commonly used
scenarios from the end users and most of
you have probably implemented something
similar
so most of the partners have
hard-coded certain feeds
that the customers are using
thus we needed to provide a freedom of
choice definitely with some limitations
because most of the users are going to
be using the feeds from their own local
banks
uh when we were designing the feature we
were not expecting that most of the
users will pay thus we do not have the
authentication we have focused on the
free currency exchange rates races
and our goal was to enable you to do
this entirely to setup without writing
any code so
entire feature is designed to be data
driven
success criteria for easy setup was that
it must be easier than writing code so
this was a lesson that i learned from
the senior developer who said to me if
you're writing a setup and it's much
easier to write the code it means that
you're doing something wrong and it's
not correct
and for the node code modification
this is for the majority of scenarios of
course we are not able to provide any
integration out of the box
thus in few scenarios you will have to
modify the code
so for the demo we'll start with setting
up the currency exchange rates from the
ecb and then we'll
implement some of the harder
and i will demo to you how you can use
the text transformations
so if you go to the setup page
that is here
we have provided yahoo out of the box
but let's say that i would like to
create a new one to the acb
and i will just write european central
bank
in the description oops
and then for the service url i'll go
here
now i need to tell to the system how to
parse this xml and the xml is looking
like this so european central bank as
you can see is providing a very nicely
formatted xml so you can easily see what
the date is what the rate is and what
the currency is related to the euro
so in the system i need to tell it where
to find the currency information so it
is this node here
and the system is going to generate the
xpath expression
you can type it in manually if you want
however it is much easier to use the
lookup to fill it out
now for the currency code i can easily
see that it is named currency and it's
named us dollar
and
starting date is here
and exchange rate amount is
here
and relational exchange amount we hard
codes to 1 because it is always one euro
to the foreign currency
now i can easily see on this page
through the preview function
if i have set it right
and
system will tell me which information
would be committed to the currency
exchange rates if i was to make this
service production
so if i take a look at the exchange rate
for danish crowner i can see it's
7.46 which means it is correct
so
since this was a rather easy fit to
implement
let's try something
harder
yahoo exchange rates they have a bit
harder
feed
so if you take a look how does it look
like
we can go here
and you can see that they have
connected the currency codes so the
first one is the source one and the
second one is the destination so this is
great britain pounds to
united's emirates dinner
thus to parse this text we needed to
provide some of the text transformations
so you can define them here through the
ui
and basically this rule is saying that i
want fourth character to sixth character
by defining the it starts on the
character four and it is
length three
and then the system is going to extract
the part of the string and map it to the
currency
now when i was preparing for this
presentation i was trying to find some
really hard streams to parse and
the hardest that i managed to find
was looking like this so if you take a
look
this is a really hard stream to parse
because basically if i was trying to
make something harder to pass i wouldn't
be able to because
first the currency codes they are
connected
and
this is a very long string that is
difficult to pass parse
this is growing depending on the name of
the currency
then the
date is very difficult to parse because
it has thursday november 9 so
through the cl this would be impossible
to parse we would have to use the dotnet
interrupt
and the exchange rates are being done
like this
so this currency feed is very hard to
parse
so to answer the question is this fit
possible to parse with the current
system unfortunately the answer is no
because i was trying to set it up and i
failed
however
now i can use my favorite sentence that
i'm often using
it is working on my box because while
preparing for it i have implemented the
fix so i will demo to you for the first
time
uh two or three additions that we will
check into the product and release so
so you will see how you can
parse
a harder string like this one so if i go
again to the current exchange
and i create this new one
i'll call it like this
and okay i provide the source url
now i need to do the mapping again just
a second
so the main item is this one here
then the currency code is
here
then the starting date is this text here
then the exchange rate amount is
here
and the relational exchange amount is
again one
however now i have to create a
transformation rule for each one of
these nodes
so for the type for the currency code i
have to create a rule which says
so for this one i will have to use a
regular expression
so in the previous in the version that
we shipped the regular expression can
only do the replace so we have splitted
it now so you can
specify do you want to replace the text
or do you want to match the text on
so this function will match the text
we have also added the ability to test
the string straight on the page so you
can see if it is working or not
so from this one i can simply take the
title
and paste it here
and now i have to specify a regular
expression
so first let's start by matching
everything
so when i hit update i get in the
results what is going to be transformed
now let's try to match everything that
is
after gbp sign
and it works
so and if i would like to get this value
here i need to tell to the system
please match
everything that is in between the
brackets after the gpp sign up
i did something wrong
just a second
yeah we can use
that's why the cheat sheet is here
and i get australian dollar indian
so thanks
[Applause]
so starting date
is going i'm going to demo this one
before the starting date so let's see
that how we can exchange rate amount
and for the exchange rate we can use the
substring we have extended the substring
so in case you do not like the regular
expressions
some things can be passed very easily so
if i take this one as a
test
i can simply say to it please start at
the equal mark
and end on the first blank sign
i have to put quotes because microsoft
dynamics nav is going to trim the white
places so you have to start with quotes
so if i say update you can see that it
is successfully parsing the
amount
so in some cases you can simply use the
substring by providing the starting
string and the ending
string so that one is going to parse the
amount and for the data i need to create
a new rule
oops
and
so if i copy paste
this one
and i have it
so if i say which format the date field
is and i say update
it
doesn't work
so let's try now
nope
just a second
yep
okay this one works so i can see that
the system has successfully parsed the
date
so when i close it and i hit preview
let's see if anything is going to pop up
and i i'm getting the current exchange
feeds from this rs feed
so uh this code is going to be checked
in soon and it is going to be
hopefully in the next release maybe we
will downport it to the previous
versions i can also share the objects by
uh me booster form
so getting back to the demo
on this page here
after you have set up the currency
exchange rates you need to enable it
and when you are enabling it
it is asking you do you want to run this
as a background job by using the job
queues so if i say yes
i get the job queue window which is
enabling me to conf to say to the system
how often do i want to update the
currency exchange rates
so you can here specify the recurrence
to update every five minutes or to run
it daily
and then the task is going to run
i can also go to the currencies
and i can trigger the update manually by
using the update exchange rates
and this is going to update the exchange
rating that are coming from the yahoo
service
we can see that the date has changed to
today the ones that are actually mapped
on the ecb service
okay so that was for the demo
so
how it works these were the components
that we have used and we have tried to
make the system completely data-driven
thus we have used the data exchange
framework as the backbone
uh if you're not familiar with the data
exchange framework it is
basically i would describe it as
data-driven generic xml port
so
it is able to parse also comma separate
strings and it's also able to parse xml
since it is very difficult to define the
data exchange definition we have built
the simplified ui so the mapping that
you have seen is an actual
simplification on the data exchange
setup table
we are also able to parse the json feeds
and for this purpose we have implemented
json.xml converter
and the text transformations were
written as a separate library that you
can reuse for any code that you would
like
we are just using it for this one
so this is the flow a user can start the
procedure by using these three actions
either manually or it can run in the
background or they can use the preview
action as the test
when user starts the action we will
invoke the
code unit that is called update currency
exchange rates
and then from the setup table we are
going to read the url
we will fetch the data
then the question is is it in json
format or not if it is in json we have
to convert it into xml and then we land
it into the data exchange table
that exchange table is able only to
accept the xml or the comma separated
files
now
parsing part is being done by the
generic parser first so generic parser
is going to read the definition
which is connected to the text
transformation rules
then it is going to store the parse.xml
in the data exchange fields
and then we will call a custom mapping
code unit that we have written to
transfer the data into the
currency exchange rates table
we needed the custom code unit because
we wanted also to have the preview so
preview needs to run on the temporary
table and also we needed to provide some
defaulting logic between the fields
otherwise there are also generic
functions that you could use
for your
flows so it's not necessary to
implement this one
the boxes that are highlighted in blue
in the image are the boxes that we have
added specifically for the currency
exchange rates and everything else is
highly generic so you can see that
only the beginning and the end is
currency exchange specific
now
defining the data exchange definition is
rather hard because this is the pitch
that you would use to create a
definition
and it is very rich with the
functionality it has many fields however
it is very difficult to use
because after you're done doing the
definition here
so on each of the parts you would have
to specify the
expot you would have to specify the
lines
some of the mapping code units then you
would have to open another page where
you are connecting the fields to the
xbox
and it has the five tables in the
background so it is a rather rich
functionality however it is hard to use
for the simplified ui we have replaced
these two pages with a small subpart and
this is highly reusable you can just put
it on any page if you would like to do
the similar mapping
the ui subpart is connected to the temp
table and the temp table is responsible
for actually modifying and reading and
writing to the data exchange definition
that the generic parts can reuse
afterwards
for the code that you have to do to
surface this functionality you have to
add the part on the page
and to add the following code on the
page to connect it so when you insert a
record this code is actually setting the
suggested fields you can tell to the
user which fields are necessary to be
filled
otherwise user can select them
themselves
and on after get current records is
actually populating the part if the
definition is already there
so
from the updated part you need to set
data exchange code and call the generic
function that is updated so as you can
see there is not a lot of code to be
written to be reused
for the json to xml converter if you
would like to use this functionality
it is in this code unit and you can use
two functions json.xml and json to
xml create default route
the second function is not in the code
that we have shipped we have discovered
it recently and the problem is because
xml needs to have a root note and json
doesn't
thus if you call the green function on
the json that doesn't have a root note
it is going to fail and the fix as you
can see is very simple you need to add
the root node just name it root and then
it is going to work
and for the last part for the
transformation rule
and this is
the entire code is
implemented within this table and the
only function that you need to call
after setting the fields is transform
text
and then it's going to end up in this
huge case statement that you can extend
if you need any additional
transformations
we have already received feedback from
our mvps that date and time formatting
doesn't extract time which we should
also fix
so we are looking for the feedback in
case you need something additional
yep so for the incoming documents
cheapening
so
am i one
yes looks like
hello again everybody
i have to apologize a bit my voice
it looks like i lost it a couple of days
ago so if i don't manage to finish i'll
do the demo and equal i will do the
talking
but
so i will talk about the electronic
invoicing and the nikola will follow up
with the ocr management
but first of all i would like to go and
make a small introduction into one of
the features we released a few time few
releases ago is the incoming documents
feature
just out of curiosity how many of you
used it or ever heard about this feature
well very popular feature only five
hands
so so
what is this feature about so i will do
a bit of a demo or actually an
introduction to the
feature
so if i
connect to an nav instance that we have
on azure hopefully the internet works
yes
so incoming documents
it's pretty easy to find it you know
just search
so
the initial feature was pretty basic
maybe that's why it's not very used
it was mainly a repository
containing a link
to an external
document repository like sharepoint for
example so you could have the link here
and the idea was any documents you
received in emails or
okay one thing
one second
looks like i have to share the screen
or move it yes
okay
so now it's a bit awkward but i'll try
to deal with it
did you have the same problem
no
okay let's let me switch to this machine
because
then i will see what i'm doing
sorry about that
so if i find the usb port here
so okay all good
so
the incoming document feature the the
initial
functionality was pretty basic so as i
said it was mainly the repository and
what you could do
[Music]
if it opens yes
you had this link to the external
repository and then for example the the
flow was the following you go and open
the actual document and then you go and
create here
an
incoming document into the sorry
document
so it's the wrong page
the wrong link actually new again
it's a bit slow because it has a
component so it loads it
so you open the document from the
sharepoint and then you have some
options here what you can
now we grouped into in the new release
into this common
method and then another functionality
was supported you you have the approval
functionality you could release or
reopen and reject
in enough 2016
we added quite a lot of functionality
and it's
highly used in the electronic invoicing
and in the ocr services nikola will
demonstrate that
you have like you can create now the
incoming documents in several ways
for example you can on a camera capable
device unfortunately not this one so i'm
talking about tablets or phones you have
the options to create it from
from just taking a picture and nikola
will demonstrate this during the ocr
demo
otherwise let's say if you receive from
your customer
an electronic invoice that's in my case
i choose the people format
so let's choose this one
and wait a bit
um
what the page will now try we'll try to
identify what kind of document is this
one so we implemented let's call it a
sniffing functionality so it identify
the data exchange type so it is actually
a people invoice
and then the nice features
we think we added is you have a peak
view
through what the document is about so
you have some financial information as
you can see
so you can see who sent you this
document so what is the party that sent
you this document some information about
the party
what is the currency dates
and what are the amounts
for this document
then also something we added into nav
2016 you have the option to create
automatically a document so using also
the data exchange type it will create in
this case it will be a purchase invoice
so all quite fast and
without
almost touching the keyboard actually if
you use the workflow that's been
released also enough 2016 you can do
this without even seeing the documentary
posting and all this releasing
all this out of the
box
so you also have an option to create a
journal line based on the document you
receive if you don't want a document you
just want a journal line you have
a map text to account and i have to say
that in my previous demo i will talk
about and i'll show you how to create
automatically the document and how to
use the map to text to account
functionality
then
in the end of the presentation nikola
will talk about how the incoming
documents are integrating into the
ocr services
one more thing i have to mention
one more enhancement is now you you can
attach to the incoming document
several attachments so the first one or
the most important one it is called the
main attachment you can see it here
that is called main attachment because
it is the document that will be used in
the flows for the electronic invoicing
or for the ocr services
and then you have the option to attach
more documents and then they will be
added as
additional or supportive documents
so it can be an email or a picture or so
on
so now if i switch back
to the demo and i get rid of this
okay
let's yeah but you can't get it
how can i get this one yes yeah
close it
all good
so as a summary so as i said we have a
back porting capability so we have the
still the legacy support of creating the
documents manually and
doing the approval but now it's using
the workflow capabilities
then we have added the automatic
creation of the documents so the
sniffing functionality and creating
getting the document and even creating
and posting the actual document inside
the nav
we have support for main attachment and
additional attachments
we have camera integration you can take
a picture and then send it to ocr and
continue the flow as you'll see in
nicolas demo
and then
we have as i said integration with
document exchange service and the ocr
service so that was
in short about the incoming documents
so now let's go into the electronic
invoicing
a small introduction
about why electronic invoicing so first
of all many in
more and more countries are
mandating to use the electronic
invoicing in business to government and
this most probably in the near future
will be mandatory also for business to
business
then in the current global market
every company might have business
relations with companies from
many countries and so they have to
support many formats in order for the
electronic invoices to work you need a
common vocabulary to use
and then for the small business it's
quite challenging
from the point of view of cost it's it's
quite costly to support different
formats and they can be forced by
big
companies to do to support their own
format or for
countries they might have their specific
format
so
what do we think we need to in nav we
need a generic electronic invoice
platform so to be able to
create these documents and consume them
we need to support the standard formats
like people and other standard formats
and then we need a common document
exchange service
so
what did we do to achieve this in
microsoft dynamics nav 2016
we added support standard support for
international things so for example we
added now the gln on vendors and
customers dln is a unique identifier of
the companies
we added gtins for the item numbers we
added for the items we added the tax
codes currency and so on
then we have a flexible sending option
so using the new feature of document
sending profile
you can choose to combine
how you want to send the documents to
your customer it's either electronically
or it is a email you can do all at once
or you just choose separately
then we have extensible formats
so out of the box we support few formats
globally is the people
and then in some countries we have some
specific formats for the country like
oil ubl
and we think the way we
developed
this it's pretty easy to plug in new
formats
especially in the new sending profile
functionality
and then we integrate it into a free
document exchange service and that's
what i will talk in my demo will be
about integrating with the trade shift
one service
and
as i
already mentioned using the out of the
box workflow functionality
you can
have an automatic process from receiving
the document and even posting it
so all without
touching the keyboard all in the batch
mode
now
as i said i'll talk about tradeshift why
did we choose trade shift well they if
you check their vision is pretty simple
they just want to connect every business
in the world maybe they can do that
hopefully they can
so when the reason we choose them they
have
support quite quite many formats is more
than 20 formats
and we also think it's pretty easy to
set up
and i'll try to show it in the next
minute so
i will go into the demo mode so i have
three more or less big demos to show you
i'll start by showing you how you can
set up trade shift
and then
we already set up two azure machines one
is company a and one is company b so
company a will be the sender of a
document so i'll show you how to send
the electronic invoice
to company b that is the receivers and
then on the other side
i'll show you how to receive an
electronic invoice just one second
excuse me
so
let's get the demo
okay
first of all
we'll start with the setup of the
environment so i have to mention that
this has been done in two places
unfortunately for now
so first of all you have to go on the
trade shift side
and sign up create an account there do
the linking with your business partners
and then you have to do
some setup in the in nav
i have to mention that rate shift has
two
services one is the production service
and must be used only for production as
we were told
and then if you need demos or as a
developer you want to enhance or see how
it is working you have the sandbox or
the test environment that's what i will
be using now
i was told that they are identical
but i noticed that sometimes the test
environment is a bit underpowered so
let's see if
uh
i've already created the accounts
in tradeshift
okay i
might have mistyped it or i forgot the
http
so
enough
conference
one
it
oops
well it's not my
computer so
and i love nav as a password
i guess everyone
feels the same
it looks it takes some time it's either
a
wrong password or a
slow connection
i can try also with the competition
ah
slowly
comes up
well yeah it's
mainly about the competition
okay now i lost track
okay we have to do it again
conference one
that
oh
book.com
at least we use the outlook as a email
provider
and i love
nav
sorry about that
so there are three things you have to
set up here well first of all you have
to sign up the sign up process is pretty
simple it's the same as signing up for
facebook you just need an
email account then you'll get the
registration the confirmation and you
say yeah okay i'm
i'm okay with that
then you have to go here
if that works
and then you have to introduce
your company details so we accept the
address name and some logo whatever the
most important field in this scenario is
the gln number it's the unique
identifier of your company
that's how you'll be find found
when someone sends you a document in
with trade shift
then you have to add
your business partner to the to the
network so you you do it the same as you
add a new friend in facebook so you send
a request and if the business partner
accepts then you are all set up
and the last
part you have to set up
you have to install an app what's the
reason of that
from nav we use the rest api calls to
call into the tradeshift account so for
that you need to authorize so the
authorization keys are provided by the
trade shift provider they are easy to
remember
as you can see maybe you cannot really
see
but
and i'll show you what do you do with
this case so that's kind of all on the
trade shift side so now if we come back
to nav
and if i find my
okay
here
to set up in nav there is also a few
places you have to go first of all i've
already set it up
before so but i'll just show you in the
company information
there is a the new field that we added
the most important one in this scenario
is the gln
then you can have also the vt
registration number
that can also work
but the jln is the primary one
and then
make sure that you have the swift code
and the i band filled in
and that's all about the company
information
then
you have to set up the service
so as
nikola mentioned we have the service
connection overview
implemented enough 2016 that shows you a
nice overview of all the services that
are available in
nav
so we'll just pick the document exchange
setup
and
by default you can do the set urls to
default it will default to the
production environment so make sure you
add dash sandbox if you want to do it
only for demo purposes
and then
for the authorization you just have to
copy the keys that are on the trade
shift side that i showed you on the up
so
you copied the keys here and the tenant
id
you test if the connections is
the settings are okay it looks like they
are okay and then you enable the service
when you enable same as for the currency
exchange rates there will be some job
queues being generated in this case
there will be two job queues
and i set them to refresh every minute
why two
one is used to check the document status
because when sending a document
it is an asynchronous process so trade
chip will say yes i received it but then
it takes couple of seconds to dispatch
the the document and you can get errors
because of business firewall or whatever
reasons
then this queue will check to see if the
document has been delivered or not
and then the second queue is used for
receiving and i'll talk about it maybe
when i'll go to the receiving part
so
well the slides don't say much here
this is all about well actually i forgot
one important thing
um i already created upfront
a customer
i'll just show it to you it's called
company
b
so accept details about name contacts
and whatever
again the most important field
is on the invoicing tab if i'm not wrong
is the gln number so make sure you have
this filled in and then
i don't know how many of you are
familiar with the mini app in the mini
app we have the send to functionality
and people said that it's quite nice so
they will have want to have it in the
big up so we actually did
step forward
we implemented the
something we call it the document
sending profile
so
what is that
if we open the one that i already
created for this customer
it's a way to say how do i want this
document to be sent i can print it i can
email it i can send it to disk all at
the same time or separately and then i
define this document type the document
profile and then i assign it to customer
with a group of customers for my
scenario i just choose that i want to
send it through document exchange
service
and i want to use the
people 2.0 format because the the for
now trade shift does not support people
2.1
and then the formats
it's something that are defined in the
electronic
document formats
so out of the box we support exporting
four documents is the sales invoice
sales credit memo service invoice and
service credit memo and we support two
two formats people 2.0 and people 2.1
the way we structure this we have
the so the xml is generated by xml port
and we just have some code units as a
wrapper on the xml port and in my last
demo i'll try to show you how to add a
new format
if you
so now let's
go to the second part of the demo
because that's all i hope i didn't
forget anything about setting it up will
not switch to the slides because it just
says demo
sending the document
so let's try to send the document
so we'll create a
sales invoice
i will say new
i will choose the newly created
customer
yeah yeah
some
so what i will sell
sorry oh this is the mini app
but i actually don't want the mini app
yes
oops
misspelled so nicola any help do you
know how do i get the non-miniap is this
one
hopefully
yeah that looks like better well the
reason i don't want the minion because i
want to be able also to put an item
charge
okay
so i will sell the famous bicycle
let's put two pieces of it
and then i'll put an item charge
i'll put some freight
and let's say one is for 100 gbp most
probably 100 it's enough
then
we just go on the actions tab
or actually on the home
do post and send and here it comes into
the picture the default
sending profile that we choose
so we that's what and i just say okay
yes
oh of course i forgot to invoice the
flight so i will go here
assign the
[Music]
item charge assignment
a bit of a supply chain or
suggest item charge assignment yeah
doesn't matter
close and let's try again
so what is saying now that the document
is sent to send to the service provider
what that means is just send
then we have an option to see what
happened on the service provider so we
can wait for the queue to process the
document
or we can directly go
and check the
document because we added the status
so there are few documents i did some
trying before it says that it's already
sent to the sorry delivered to the
recipient so the other party
must have received it
so that's
all about sending the document
now
let's go on the company b
so on company b you have similar setup
for similar check you have to go and
verify that the company information
is
properly
filled in
so the gla number check that it is
populated and then you check the service
connection page
it's a bit slow sometime
it's not my machine
and do the same check
for the document exchange service
so it's already pre-filled it's already
enabled i already copied the
authorization keys for my
for my company and then
i have to make sure that the job queue
for the receiving part it's ready it
says enable
well what happens on the receiving part
this job queue will pull
trade shift is anything new for me
anything new for me and in the moment
there is something new it will pick that
document
in the original format if there is any
or in the tsubl format that tradeshift
provides and then it will create
or it should create an entry in the
incoming documents
page
so let's see
now i have to remember which one was the
invoice 034
oops too many pages i think is this one
what was the total
8100 yes
so as you can see
i'll show more
uh the sniffer identified that is a
paypal invoice
it displays the financial information
the summary of it and it looks like it's
the one that i sent previously from
company a
so now let's try to create the purchase
invoice into our system
before doing that i will show you that i
already create a vendor
in the system
you know if we go to vendors
so i search for company
is the company a and again the important
field there
is the
gla number
that is here
you can double check well not really
because you don't have the access to
this but it's not fake it's it should
work
[Music]
so now let's try to create the document
inside the nav we'll hit this button
and this will just go and try to create
a document but it says that there are
some errors
so which are the errors now in nav 2016
we actually also
propose it as a pattern we have error
messaging where we collect all the
errors into one place
so the errors here
uh
there is a bit of a problem because they
are too long and they don't really fit
nicely into this
but maybe that will be fixed the errors
are mainly about the items that i put on
the initial invoice so i sold the
bicycle in a
gl account i have to mention that all
the other non-item
things that you put on the sales line
will be treated as gl accounts when
coming in the
in on the receiver side
so to fix this
let's go first to the
bicycle
first of all i have to double check
what the error says it says the company
couldn't find item number 1000 so we
click this
i know that item number 1000 let's say
is the touring bicycle we go here
and we do the vendor
so it's the company a
if from company here you receive this
item number 1000 then it should be a
touring bicycle
let's try to create the document again
it's still not working because we just
fixed the problem with the with the item
now we have to fix the problem of the of
the charge so to do this we use the map
text to account functionality
here you can define some global ones so
for anything
you have just use this
or we can be more specific and we create
some text unfortunately for now you have
to put it exactly as it is and it says
fried charge jb's petition
so let's try it
jb
okay now
jb
edition
and then i want them to be posted to
these accounts
i think will be the debited account if
i'm not totally wrong
so let's try again
i was not very lucky i forgot
i
misspelled something as i can see
sp
double d
is it no
spadish was it like this
i don't have a cheap
cheat sheet
edition hopefully
well now it takes longer so i might be
lucky so it says that the purchase
invoice has been created i can easily
access it by saying open record
so this is my purchase invoice so i have
two items of the bicycle
and one
charge
and the totals are matching if the
totals will not match or the v80s are
different i'll get
some warnings in the error
uh on the incoming document page and
then i
sorry i decide what i do with that
that's all
you can follow then you can
approve the document post it and that's
it
now let's go back
to the presentation i'll go
oh
are you switched
did you switch okay good
how it works
well
i would say that uh one picture worth
1000 words
i will say one picture what's in this
case 1000 lines of code or
so
i will not show you a lot of code but
i'll try to talk
about the design and just showing you
some diagrams
so what components did we use to in the
trade shift integration and not only
also other service integration are
similar so we have a communication
manager
i'll talk about it
we use also the data exchange
framework to create the entities
we have the document sending profile
that i just talked about it i hope you
remember that the error and warnings and
also we have an activity log that is
trying to log what are the activities
that have been processed
manually or by batches
so i'll try to take one by one and talk
mainly about the first two
so the
communication manager yes
what is the idea we call it a
communication manager but it has few
components
uh so the main component is the code
unit in this case is 4 1410
that is responsible with communicating
with trade shift and there are some
dependencies first of all this is like a
wrapper on the
generic http web management code unit
and then it uses also because connecting
to the trade shift requires
authentication
we decided to use a
dotnet add-in for
obtaining the signature i personally
hate to do
a lot of string manipulation in cal so i
found it much easier to do it in dotnet
so i just created the dotnet add-in
and that will provide the signature
to get the signature you will have to
use the setup parameters that are saved
in table 1275 the setup table
so the communication manager is
responsible for
sending requests to trade shift and then
receiving responses and processing them
then i'll try to
explain sorry a bit about what happens
when you send the document so the flow
is
the user goes on the posted
on the invoice
that's not what on the posted the
invoice and then it chooses send to
in this case it will do in the sending
profile will select to document exchange
service trade shift
then behind the scenes what is happening
it also selects the format what format
he wants to to use it so behind the
scenes
the export document sending profile will
call into code unit 6 100. it depends on
the document type
and that is just the wrapper as i
explained to the xml port that will do
the export then this is packed sent to
the communication module that i talked
to just a few seconds ago
and that will send it to to tradeshift
well here it's a bit
more communication it's because sending
a document is in few steps first it's
putting the document
then it's dispatching it and then it
treats any errors it has
and then it is this happens well at once
and then if the as the process is
asynchronous i
have this job queue in between to check
what is the status
and all this is being logged into an
activity log table
on the receiving side we have another
job queue that calls every i don't know
one minute five minutes depends on how
you set it up calls into this code unit
four twenty fourteen twenty one that is
just actually calling the communication
module
the communication module will poll trade
shift do i have anything new do i have
anything new when it comes it picks it
up and as you saw it puts it in the
incoming document
page and then it does one more call it
marks on the trade shift side that this
document is processed so next time is
doing the polling
will not process it one more time
that's
all about the communication module
then the data exchange definitions
these are the two that we have out of
the box so it's the people credit memo
and the people invoice
and the flow is like the following
the document is the input it's the xml
file
so we use the data exchange framework
to parse this file so it's using the
definitions and puts the data into data
exchange tables then we have a custom
we try to call it generic
code unit 1214
that will extract this data into a
generic table it's called 12
14 also
and the data in this table looks like
this actually it tries to say
this
value
should go into this table into this
field but this is like an unprocessed
data because that's what we get from the
file but in our system
we should identify what's the customer
what's uh
the item and so on so for that we have
code unit 1217
that will process the data further so
it will identify what's the customer
number the item number and so on and
then the last step
we use coordinate 1218
to pull this data from this table and
push it into the
actual entities
the purchase header and purchase lines
as per my example
these quad units 12 18 and 12 17 are
pretty bounded to the actual results of
the purchase header and lines
so moving forward i will skip
this
and i'll advertise a bit tomorrow we
have another session about design
patterns
where we will talk a bit more in detail
maybe about these errors and warnings
i'm a bit
late and then also about the activity
log there are two patterns that were
proposed into in this
nav 2016
development and then i will
try to go
about
extending the functionality
i had planned for two functionalities to
be extended but
i don't really have time for both of
them so i'll just explain about this
first one and i'll provide the code
it's already done in the next release so
maybe it will be ported is extracting
additional attachments
so the paypal xml
supports adding
attachments to it so it has a base64
encoding and you can put
emails images whatever you want
and then the demo was about how to
extract these attachments so
it still keeps the pebble document as
the main document so it will be the main
attachment and then it will pull also
the eventual additional attachments it
can be the email that you received from
your customer or a picture with the
christmas greetings and so on code is
pretty simple is like
five lines of code and you're done
then the second demo that i will try to
do it right now it's a pretty
straightforward is how do you add
additional formats
so nikolai you closed my
i'm sorry not visual studio
will not develop anything in visual
studio right now
i need seaside actually
does it work on your machine
okay
so let's suppose that you have a
customer asking you
where there is a
rule from the specific country to
support people 2.2 let's say that that
will come
or any other format
you can choose to implement it any way
you want or you can choose also our way
of implementing it as i said we have
can you say this
we have an xml port that will generate
the actual xml file so
i'll pick one of this let's say people
2.1
and in my demo i'll be pretty
lazy
and i'll just
renumber it
and change the name
so i'm done implementing the people 2.2
version that was pretty fast
so you you can do the same
we're actually doing the real
implementation of the new format you
want to support
then there is one more step you have to
do
if you go to 16
range i think
oops
i will do the same
copy paste programming
more or less
so i picked this export sales invoice i
will renumber it also
put it 1610
maybe it's a bit too many
and i'll call it
2.2
and then i have to do one more thing
because this is using the
i have to get used to this keyboard okay
here it is
it's using the people 2.1 so i want to
make it people 2.2 and the end is here
just change this
save
and then if you open the nav
locally it's already here
i told you the
document sending profile has two parts
first is the electronic
document
format
so we'll just go here and do again what
we did by now just copy paste
f8 we call it 2.2
nikola is being
a bit nervous
i'm a bit late
okay
uh
it is a sales invoice and then i'll use
what code you need to create it 1610
that i just created
and not this but 1610
yes
and
come on
it's thinking i don't know why
i don't think i did anything wrong
nikola help your machine doesn't listen
to me
just try again
restart windows sorry
yeah it works but okay now
you can optionally add
a validation
so that will validate that before
posting you know trying to generate the
document it's it is
generate into a valid
uh people document so i'll put its
f4
sales validation and i'll use the same
and we are almost done
i'll just go into the document sending
profiles
and update my current
profile i'll create a new one
i'll call it people
2.2
then i say send the electron and then
magically i should see the new one here
here it is
so and then
i'm kind of done what it's next you go
to the sales
invoice
oh invoice not order
come on yeah do new
i'm not sure you have you didn't have so
i'll put customer 10 000. this is the
local installation we are not on the
so we'll do post and send let's say and
i just want to show you that you'll have
it also here
here it is
so you select you say yes and eventually
it will work so it's that easy you just
have to code
how you want what is the export
you
plug it in
in few lines
into the in not code but just
in the ui and you're done then you are
ready to
to rock
i think that's all i had for today
if you have any question
sorry if you have
that was not me
it's not done
it's not yet done
because nikola is next
hello
i wanted to say that i am done not
nicola
sound
okay
so
okay so nikola document
management yes so for the last part we
will show you the ocr functionality
so
ocr is being used so you can capture the
documents and you can transfer them into
the invoices quite quickly so we were
aiming for the scenario where you're
processing a lot of paper documents or
you're sending it to the external
accounting service to do it for you
thus it needed to be automated
so
the benefits that we tried to do is to
enable an easy way to capture an invoice
to store it and to extract the header
information
the entire flow is possible to be
automated through the workflow
and also it is later possible to find
the original receipts that were
connected to nav invoices
so
entire functionality is implemented by
using lexmark invoice capture service
it's also called read soft
and
basically
it's cloud-based you can get the account
and be up and running in 10 minutes
for all of the microsoft nav users we
have
made the following agreement
it's called freemium and you can leave
whenever you want there is no setup fee
and you can get the free subscription up
to 75 invoices in month
if you are over the limit in this the
small text up there says it is one
dollar per additional invoice to be
scanned
but there is also a subscription account
that is 105 dollars a month
and then scanning additional invoices is
half a dollar i think
so to show you a demo
so let's say that i'm a user and i'll
connect my phone
okay
let's just see
okay yes and i have installed in
microsoft and the dynamics nav
application
and you can see on the role center for
the small business i have a camera
option
and this camera action can only be shown
if the device that i'm using has a
camera on it specifically so if you open
this role center in the windows client
or web client it will not be visible
so if i take a camera
now i can take a look at this printed
invoice that i got from the bicycle
traders i purchased some bicycles from
my company
and we can see that they are trustworthy
company because they are using nav and
board reporting
so this is going now to upload the
picture into nav and i can see that my
incoming documents has number has
changed
so i can also take another picture from
the camera
no not that one
oh
okay more junk
so yeah
so to take one picture of the audience
yay
cool
so
all of these items have ended up in the
incoming documents
and i can see it here so if i open the
incoming document to see how it looks
like
come on
i can see it looks exactly the same as
the photo that i have taken
so
basically it is i'll show you the
actually endless
if i go back
we'll use this one for demo because the
lighting here is horrible so
nothing would show up but the actual
photo is i think
here
hello
yeah glitches
let's just continue it in the web
clients
okay to close the phone
projection app f4
so
if i go to the web client instance
and the incoming documents
the photo that i have taken is here
yes
so in order to get the ocr up and
running you have to first subscribe for
the ocr service and then you need to set
it up in the nav
and you can do it by opening the ocr
setup
and they will provide you a username a
password and the authorization key you
type in the service url and then you can
say test connection
and it is going to tell you if this is
connected successfully or not and you
can select the default ocr template
default ocr template you selected when
you subscribe for these services
for this account we are using dns
invoices and swedish invoices
so if i use the danish invoices and mark
the service as enabled
same as all of the other services that
you've seen today we can also automate
it through the jobq windows so you can
automatically receive and send the ocr
invoices
so if i go back to the photo that i
would like to send
all that i have to do here is that
i cannot send it to the job queue or if
it is really urgent i can send it to the
ocr service
so if i invoke this section
and the document was sent successfully
to the ocr service
and i can maybe send another document to
the ocr service let's see so this
invoice is a different one
so if i say send to ocr service first
this invoice is from right away
so let's see how it looks like
it is looking something like this
so it's a different document than the
one that i have sent
so
let's see if the
read software has processed it
the speed actually depends on the time
of the day so how many requests their
services has
so now you can ask receive from the ocr
service
and i can see that the document was
successfully received
and it has extracted some data here
so it says that is from this vendor and
this is the vat registration number so i
can dock it
and compare it to the actual
invoice
just let's see if it is 100 correct
so it says bicycle independent traders
yes that's the company's name and
vit registration number is correct
and gyro number is correct when the
invoice number is correct
the currency code is correct and it
hasn't extracted for some reasons the
amount including v80
so i can correct that
by using the actions
and i have here the action correct ocr
data
and here
i can type in the actual amount which
was
42 500.
now you can also send feedback to the
ocr service and their service is taking
this feedback and it is trying to learn
so for every new invoice that is trying
to process it should become smarter
as such
so i can send them a feedback in order
to
get better results in the future
and now from this invoice i can create a
document
so if i select create a document this is
of course going to fail
because i'm lacking some setup
and it says it cannot find the
appropriate gl account for this vendor
the reason why we need a gl account is
because
ocr is only able to extract header date
so all of the invoice information needs
to end up on the gl account
so in order to set it up
i will need to
enter the
vendor name
here
and type in the debit account number
let's say it's this one for example
and the credit one and our balancing
source type is a vendor
and it is his account
no
yep
so if i close this one
and try to create a document again
it is successful with warnings
and if i open it it says that the
information that i have in the system
how much this item cost is mismatching
his invoice
so i can either go and update the
data that i have or simply just post an
invoice
and here's the invoice that you can see
it was created with the vendor and
everything was transferred to the gl
account
we added the option
if you made a mistake you can just
simply remove a reference and delete the
record
and you can also transfer it to the
journal line
as such
so if i open the journal line
you will see that the
account is here
and also vendor balancing account was
set to the thing that i have
specified
so let's see what happened with this one
so if i edit it
and i say
receive from the ocr service
yep
so it's recognized that the vit is the
vendor vit registration number is
correct bank account number is correct
invoice number is correct order number
is correct
and it managed to extract all of the
date so just to show it
because this invoice was
a bit better scanned so it was probably
higher resolution than the previous one
so let's see
so you see that d
just a second
you see that the amounts are matching
vit is matching total including v8 is
matching cvr number is v80 number and
other information is also
correct okay so that was for the demo
to switch back
so
we are only able to extract the headers
but if you would like you can extend the
invoice capturing system and for that
you need to become a lexmark partner and
they will enable you to use their sdk
thus you can write the missing part and
that is mapping the invoice lines to the
actual items
they are also allowing you to resell the
ocr instances and this slide was taken
from the directions i do not know
exactly what the details are however
there is the opportunity for you if you
would like to become a lexmark partner
and partner with them around
ocr functionality
so extracting the lines is possible by
using their sdk however it is not
working out of the box
so for the code how does it work
it can start as a manual action or it
can start through the job queue we are
using two different code units to invoke
it
and then this
blue box is actually the one that is
doing the
communication with the read soft
if the sending was successful
we will invoke the event in the code
unit
133 and this
event is being used for workflow
purposes you can also use it to extend
but basically it's there for the
automation and we are of course locking
both successes and fair layers into the
activity log
receiving it's similar as sending
however the important parts here is to
understand that
we will create a new incoming document
attachment which will be the xml and
then we treat it the same way as we are
treating all of the electronic documents
so the flow that you saw in in chip demo
is going to take over from there
important thing to mention here which is
the last thing is that this code unit
which is called ocr service management
unfortunately it is very read soft and
like smart specific so the name is maybe
a bit misleading
so you may think it is a generic one
however it is very
lex mark specific
yes which is the same for trade as
cheap and as i think so if you would
like to extend or change this
functionality you can either change this
code unit or you can follow the same
implementation that we did and use the
different objects
yep so for the summary so we have demo
to you the current exchange rates how
you can set it up and the demodulated
dream setup shipping and showing you
electronic documents sending and
receiving purpose and extending it
and lastly the ocr we will not demo
today because we are running out of time
how you can automate the entire process
through workload so you'll have to trust
our word
it is possible to automate from taking
the picture from the camera to creating
an actual document that user doesn't
have to do a single click in case of
and there is also a session about
workflow where you can learn more about
the functionality which is one of the
additional reasons why we decided not to
demo it today
yep
so
there is more information at this link
and we are open for q a
so for the first five questions we have
five t-shirts
yes
do you have a microphone
maybe not or live just yes
uh you want a t-shirt okay
[Music]
yes
so the question is for mapping text
accounts that we have shown for the
vendor are we planning to
transformations
and the answer is no
unfortunate
you can do it
if we get enough feedback from you guys
we will do it
so that's the thing
yes
where are the documents
the documents are stored in the incoming
documents table incoming document
attachment table so it is locally in the
nav
and you can also store them externally
but then you have to use a link
and that's it
well i know some partners did
implementation when they store them in
the azure blob or other
or
when is microsoft going to start using
the e invoicing
themselves
i really don't know i'm not into the
accounting so
i honestly do not know what we use for
invoicing
i think they're using ax
but i'm not sure
yes
what about the template if i change the
template
it will be okay or not yes it should be
they're not using templates for much
okay yes and
if
on their site you can also define the
template
i'm not sure if it is part of the free
package or not
but you as a developer can also create
additional templates so you can do the
mapping for the ocr and tell it where
does each mapping comes from and these
kind of things okay thank you yes
yeah there are some questions on the
other side
okay in the beginning of the session we
saw that you could
map an xml to
data fields and you can transform the
text
looks like it's only one function with a
case statement you can extend
will it be possible in the future to
actually nest functions uh yes it will
be
i didn't manage to make it but it will
be yes okay that was the plan as well
thank you
on the other side there are some people
hi so for croatia we also need to
provide the
e-documents
for government
is there a possibility for our existing
customers to do it on previous versions
with what you've shown today to use it
or there is some technological
limit
so we need to figure out another way to
do it you mean for trade shift
for trade shift integration if you can
send the
it's an a bill so it's just sending
documents to government
i think you can just take the same
approach that we did
so as far as i know we didn't use any
new platform functionality no no the
platform functionality there is nothing
new so i'm pretty sure
and use it yes so the you're mostly
using.net interop and that's it
so
i mean you would have to port the cll
objects
because you will be missing tables and
these thing kind of things right
thank you
if the
invoice line
of an incoming invoice has the
description
uh travel or a plane ticket to madrid
okay
so
how do i
find my account number
that's the problem because you can only
map
account number to a vendor right
so that's the limitation
and it's totally honestly i don't know
if it is a big limitation for you or not
and even if even if i um
make a definition
of the text to the the account number it
can be
several accounts
for instance for several people then you
would have to do the lines manually
which is not so nice but yes
that's the problem because with the sdk
that we have we cannot touch the lines
we are not getting any information about
the lines
thus we cannot do any decisions based on
the lines yeah so okay
but if you have more questions you can
approach us and we'll be happy to answer
yes okay thank you so thank you
