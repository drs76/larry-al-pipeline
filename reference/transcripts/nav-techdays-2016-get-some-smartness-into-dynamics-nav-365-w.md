# NAV TechDays 2016: Get some Smartness into Dynamics NAV  365 with Notifications and Cortana Intelli

- **Source:** https://www.youtube.com/watch?v=dgy5pXkkVjA
- **Video ID:** dgy5pXkkVjA
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 82m48s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

hello and uh welcome so uh we're happy
to uh be able to talk about getting some
smartness into Dynamics
nav uh today my name is Claus myen and
this is yeser schz V so um we're both
with the nav application team I'm a
software architect in that team among
others responsible for for what we are
talking about uh today and yes yeah and
I've been working at the Mothership Ms
for like 8 and a half years now um the
last half year I've been spending on
trying to make NB smarter through
notifications uh and today I'll be a
guide through the world of
notifications uh in a couple of minutes
from now yeah right so um we have two
major things that we would like to share
with you so um first of all we'll do a
brief introduction of what we think is a
new interaction approach in na AV and in
EAP system systems in general talk a bit
about that then yesper will talk about
or give you all the details of
notifications and in particular the
notification API that we have introduced
in in a
2017 and um following that I'll
introduce you to Cortana in intelligence
we'll do a deep dive into machine
learning and I'll show you how you can
leverage that inside Na and we'll also
peek into how you can in general uh use
Cortana intelligence from
NV in other ways than by the apis that
we have
integrated so uh first as smarter in so
what what do we actually mean with that
uh yes but I will give you a bunch of
examples today but um I think basically
um we're trying to
U add things to ni not necessarily
machine learning or CER intelligence
that makes nav appear smarter so
traditionally nav and E Systems in
general they react to user input uh only
so I need a cash flow forecast I need to
uh update various worksheets I need to
press a button uh I need to go into
another worksheet I need to read out uh
a chart and and so on but what if
Dynamics nav could uh instead be
proactive so instead of just reacting to
what user does uh users do also um
notify users give users the right
information in the right uh context so a
couple of examples and we'll give many
more so for example it might be that if
a user signs up to let's say Dynamics
365 get into an empty company then a
natural thing to ask would be well hey
wouldn't you like to migrate your data
from your previous system so if you have
customers in in QuickBook Sage or what
whatever let us migrate them um and
another example um might be that well uh
while you are selling uh your items many
of those or the customer is selling many
of those let's keep track of the
inventory and notify the customer when
something uh is running out of stock so
these are two examples that we have
built into in 2017 and um so we're still
at an early stage I would say and we are
going to look a bit forward also in this
uh in this session but the two things we
have and we would like to show is then
this notification framework which is
basically an API to uh notify users in
the context of their work such as when
doing purchase orders or sales invoice
and so on and uh a deep integration of
Cortana
intelligence yes all right so
notifications um theyve been mentioned
in a few sessions before this one uh but
they've only been briefly touched upon
I'll try to go a little bit deeper into
what notifications are uh and when we
should use those um since you're at this
conference I assume you're all familiar
with na so that also means that you're
familiar with a dialogue like this hold
on hold on I know you're busy to to fill
out this invoice I just want to annoy
you with a question right here right now
do your mind obviously we do because
you're in a Zone you're in the flow you
just want to fill out a lot a bunch of
lines and now these annoying message
boxes and dialoges pop up and inter
you and you're probably also familiar
with this whenever you would like nav to
offer a little bit of assistance well
there is nothing to get you just get
stuck and na is painfully
silent so the primary motivation behind
uh our notifications are to go from
interrupting and telling to suggesting
and gently nudging in the right
direction and also to go from Silence to
lending a help in hand so this this is
where we should uh Leverage The Power of
notifications so I'm going to start this
uh this little talk with a demo and I'm
going to end it with a demo just to like
keep your attention and then in the
middle I'm going to work through a
million of slides to bore you to death
now I won't this will be very much
handon uh I'm going to spend most of the
time in an A and coding and we'll have
just a few slides with the very
Basics so let's dive into
it um switch the computer
so this should look familiar and as
Claus just mentioned this is a
completely new installation you see
there are no quotes nothing in here so
let's assume that I go to my vendors so
these are actually notifications that we
already implemented into the system so
if I click on my vendors now you'll see
want to import
entries uh which is of course a very
nice suggestion for someone who has
never worked with it because if you like
go up in here and you're completely lost
I want to
import n import import from data file it
might be a little bit complex to figure
out what how you should get your data
into na whereas this is just a click
away and off you go and also for the
trained user who does not want that and
maybe use Rapid start or whatever to get
this data in he can simply ignore this
notification so it's not
really requiring any attention unless
you want to so the other example would
be let's say we have a
customer Yu
Plumbing uh where we can create a sales
invoice
so what would a plumber need so he might
need
um of course a Plummer's
helper so before if you like uh if you
ran out of inventory you would get
stopped in your
flow now this allows you to re to
respond to this message at a later point
in time you can just first start
entering all information that you
need uh let's say he also needs one of
those drain cleaner obviously maybe even
10 see now the notification start
stacking up but you can still keep on
working and then in the end when you
like you can take a look okay what is
this I don't care about his credit limit
I know him he's a good guy so I might
just discard this one or ah yeah man I
forgot to to order some new plumbers
helper I will go into details with that
right now I'll start creating a purchase
invoice so you can do all from one spot
without being interrupted in your normal
workflow so this is the intention about
behind those
notifications uh I'm going to exit that
one
okay so the takeaway is the notification
is subtle and unobtrusive it never gets
in your way while you're in your Zone it
merely suggests a course of action this
is the absolute key for
those so when should those be used well
do use them when you want to suggest a
course of action related to the context
the user is in so whenever well what you
just saw uh whenever you're in the right
context and you want to suggest action
this is where we can use them also you
could provide some additional contextual
information let's say you chose a
customer which is a premium customer or
something then you want a notification
well this customer is one of your best
customers be extra careful when filling
out some information or something or of
course if you want to assist the user in
using the product like if you're
building extensions um and they require
some setup it would be a nice thing for
instance to show an show a notification
wherever that extension makes sense and
say hey you haven't set this up yet
would you like to do it now enable this
in that functionality so that the user
doesn't have to go in and search for
setups or doesn't have to go in and
search for for um ideas na AV will
present them one could also Imagine
something like did you know that you can
also uh like the sixth time that the
user enters a opens a page or if you
very often enter the same information
you can have some machine learning
behind it that sees okay you are always
entering this and that information it's
the same it's the same and then you
could suggest hey should we not default
to this so there like various um
examples of what you could do with these
however there are also situations where
you should not use them um whenever you
want to make sure that the user takes
action or you want to make sure that
he's aware of a certain condition then a
notification is not the right way to go
because you want the user to do an
active gesture and saying yes I
understood this um so for instance you
should never ever try to take an error
and turn it into a notification that
would just be well
nonsense um and also you should not use
this kind of notification if you want to
provide um information which is
unrelated to the current context so we
are planning on This Global notification
concept uh but we're not quite there yet
so these notifications are what we call
in context notification they should only
be used um well for stuff that has that
has this context relevant so don't try
to implement something where you start
sending messages to users across the and
like all of a sudden These Bars come up
because that will just will be abusing
the notifications and the user will
start disregarding them and that is not
the the idea
here so where do they work well they
work
everywhere um you've seen them working
in the web client obviously they work on
the phone they work on the tablet they
also work in the Outlook addin and also
they work on our Windows
client um moving
on moving on here we go how do the now
we spent a fair amount of time to make
this API as easy to use as possible so
actually you will not know where they
where this notification comes from it
can be called from the header of section
of a page or a table it can be called
from the lines from fact boxes uh from a
code unit that calls a code unit that
calls a code unit wherever you call it
from it will always be displayed in the
right place and if not please file a
book so time to get serious um the API
well as you can see it is not that big
yet we've got two and a half properties
two and a half well we've got the
message um which specifies the actual
message that you want to display to the
user then we've got the ID now you can
assign an ID if you want to be able to
reconnect to the notification in case
you want to update it or you want to
recall it else that's an optional
property then you have the scope uh well
at the moment it's local only so there's
no need to pay any attention to this one
eventually at some point I hope there
will be a global then we've got the
functions first one being sent which is
probably the most important one as soon
as you invoke send the message will
appear to the user uh we've got recall
well kind of says it all recalls the
notification if the ID property is
set then we've got the add action add an
action and then the pair set data and
get data um yeah well where you can
assign data to the notification and
retrieve it again I'll of course go into
detail with those when we start
coding which would be
now
so time to get our hands
dirty um let's get out of of the client
and into this one so we're going to
start out with a completely empty code
unit except for the
documentation um so ideally when you
implement notifications you should use
our um event model you do not want to
add the notifications directly on the
page even though they are UI related but
some of them might be reusable so they
should live in a code unit of them of of
themselves and obviously you should not
uh put them on tables uh so the best
idea is of course to use an EV
subscriber um so let's do
that so I've added a event event
subscriber here on after custom Custer
post code validates so whenever the post
code is validated then this trigger is
run um in we get the customer the
previous customer and the field number
from which this was
invoked and from in here we just call a
local uh function create address lookup
notification where we will set the
message this is our first notification
it's rather
useless and we'll fired so let's see if
that
works
let's create a new
customer and we enter some kind of a new
post
code and there we go this our first
notification rather useless indeed it
is so so far so good uh now uh let's try
to add an action to make this a little
bit more
useful so I'm just going to create one
more
function so the events Subs server stays
the
same um the message has now slightly
changed but now what we do is that we
add some data because now when there's
an action we typically want to react or
do something to an object right so for
that we need to store whatever object or
whatever information we want in the
notification so that we can retrieve it
again whenever the action is fired so
set data takes a name you can choose
whatever you want to and it takes a
value now this could also in this case
since the customer
has a primary key of just one field i'
simply take the uh take the customer
number you could also choose to take a
record ID if it is a more complex key
you can of course also use set data
various times if you want to add more
information to the to the
notification so now we've stored the
customer number into the
notification and now we can add an
action click here to get
amazed um you then specify the code unit
ID where you will find the function that
is is to be invoked and you give the
function
name the function that you call needs to
be public and it needs to have a
notification as a parameter that's the
only prerequisite and then of course it
needs to reside in the code unit
specified here and then that uh method
will be
invoked um so what we do in here is that
we now this notification of course
contains the notification where the
event was invoked
from um so we retrieve the customer
number with a get data function and we
get our customer we change the address
to you did not see that coming Street
one and we modify the
customer so let's see how that works uh
find a fun of it let's do it
in the
phone um so we go into our customers and
I create a new
one like
that and I enter some kind of post code
1 2 3 four
and here we
go so click here to get amazed let's see
no we didn't not see that coming or did
we so that's how easy it actually is to
get data in get data out modify
records
uh that
button so but this is still very much
constructed so let's try to make this uh
this very very useful and try to hook it
up to you might have seen this already
in um in the presentation of our lovely
new
IDE um but I've tried to extend it so
that we actually now can contact a
service with some for instance the ZIP
code or a phone number the service will
then try to retrieve company or the
customer information and if it can do
that and it can identify that exactly
one customer is found then it will
autocomplete the
address um so let's try to hook this
notification up to that
service
like
that so first of all I've now also added
another event subscriber which calls
into the exact same
function um ideally of course I mean you
add it to every single field that you
want to uh launch the notification from
so now we have two of
them
um so now if the create the create
notification has changed slightly
because we go into this uh lookup
service which I will not show you here
because it's a little bit more complex
and it simply checks for this customer
does this customer have enough
information uh well to so that we can
find the address of them and if we can
well then we show the notification uh if
not then
not um so this actually also comes in
handy because this communication and
figuring out running this algorithm
might actually take a while right so if
you would use like a button to say hey
can you now autocomplete my address and
then you would the user would have to
wait and then it comes a response no I
can't that would be an annoying
experience right but this notification
can just come up whenever the services
read has returned something so it kind
of is slightly ASN even though we're
still in in in the
context um so this one hasn't changed at
all uh and the complete address now
obviously updates the customer with an
address
information instead of just setting some
some address field so let's see how that
works
um I can now take the for instance phone
[Music]
number just need to make sure it's
updated so if I now paste in the phone
number that actually went pretty fast so
it finds it and we can now click update
address and we'll find our Microsoft
Development
Center yeah well and fill it in so that
was fairly
simple um but now what happens if I for
instance take my phone
[Music]
number so now we get the first
notification and then I take I don't
know so in England there are some zip
codes which actually relate to one
specific address not even a set of them
like for instance glos Smith client is
big enough to have their own ZIP code um
so if I use those then you can uniquely
identify the um the
address uh well now it found two that of
course is not ideal at any given time we
only want one of the notifications right
so this is where the recall comes
in so let me update the code and add
some recall
functionality all right
so
um primarily what we need to do is to
assign an ID to the
notification um the notification ID in
this case I just just uh made a little
function where past it in a guid uh
because at any given time I only ever
want one of these notifications there
cannot be multiple lines and multiple
variations of this notification there's
only one so you might as well just
assign one ID so that at any given time
I can get in contact with that
notification
again uh and now what that
does if I save
it let me get rid of those I'll create a
new
one
and add this and we get one
notification and now if all goes
well we still only get one notification
so this notification is now updated with
the latest
information so that's already good um um
but let's
say that we
actually take a valid post code
here let we say update
address oh sorry that's not what I
wanted let's try that again I get the
notification but it's actually not what
I want uh I want to enter the address
myself then it wouldn't make sense to
keep displaying this notification right
so if I now start entering an address
then the notification should go away so
how do we do
that that is fairly simple um now
I've added another event subscriber to
the onaf address
validate and if the end if the user
enters an address chances are well he
doesn't want the autoc completion
functionality hence we use the call the
recall notification function and what
that does is simply it has a local
variable which is our notific ification
we assign the ID through this function
again and we call the recall and the
notification
disappears so this is kind of the
essential bits and pieces of
notifications that you've got
here um yeah let's get back to the
presentation so there's one final thing
that I want to show you so we actually
we're working a lot on these
notifications so uh you can expect a lot
of goodies coming up uh in the following
releases um but we managed to squeeze
one thing into uh into nav before we
released very much last minute uh so
there might be certain notifications
that simply annoy you and you just don't
want to see them uh let's say your bus
installed some extension and it keeps on
like flooding you with these
notifications and you're just not
interested so you need some way of
turning them off right as you can on
every device these days so obviously we
needed something
similar um so we've created something
that we call M notifications which is
our notification
center um you can subscribe to this
lovely called uh uh publisher called un
initializing notification with default
State um and then you can call two
functions which will and allow the user
to enable or disable it so let me show
you how that
works this will be the
last bits of code
here
all right so I have subscribed to un
initializing notification with default
State uh and by subscribing to it we
register our notification and the my
notifications
page so all we need to do is call my
notifications um which is a record and
then we say insert default we add the
notification ID which is now
required in order to identify the
notification obviously it needs an name
it needs a description and then it needs
the defa uh well the default state if it
should be enabled by default or disabled
by
default so by doing
that when you go
into my
settings change when I receive
notifications you will see our little
address lookup service here which you
can now tick on tick off there's also a
different function in there uh that you
can use where you can then pass in the
record as well and then you can specify
filter
uh like for instance I want to see this
notification for a certain range of IDs
or if a certain Boolean is set or
whatever uh and else I do not want to
see it so it's actually pretty neatly
controllable so now of course if I
disable it just for the sake of
completeness let me take that one
again a damn it take
this
well yeah nothing happens great
um so the only thing that we now need to
implement uh is in this where we create
the notification this part if not my
notifications is enabled with this ID
well then exit uh and that's basically
it so that should be fairly fairly
straightforward to to code up
against um we are currently working on
something that we call notification life
cycle management uh where you can
have where you can store all the active
notifications for a given user and you
can dispose them and you can uh so they
uh like if you have multiple sales lines
you can get multiple notifications and
if you then for instance change a sales
line then that particular notification
will go away again and in order for that
to work of course all the notifications
need different IDs uh so it can get a
bit hairy so we're creating a little
framework for that um we will soon be
posting in uh a pattern on that so stay
tuned and that
basically completes my part and I'll of
course be happy to answer any questions
that you might have about notifications
in our Q&A
section okay thanks jper so um let's
turn to uh some of the uh underlying
data sources for uh for these uh
notifications so um and let's turn to uh
to Cortana Cortana
intelligence so um what I'm going to
do is to um talk about uh what Kotana
and gelin is and I'm going to focus
specifically on on machine learning
because that's what we have focused on
in in nav 2017 I will give some examples
of how CER intelligence is used used in
nav show how you could use coner
intelligence directly using uh build-in
apis and also how you can use cotana
intelligence
integration so um so what is cotana
intelligence so it's well I guess it's a
marketing name but it's also built on
the premise that we ER get more and more
data from diverse sources so uh to the
left uh up here we have a bunch of data
sources that generate lots of data um
data is worthless unless we can act upon
it uh in some meaningful way and what
Katana intellig in promises is to have
tools that will allow to transform data
into actionable uh information so um in
what we've been looking at in N 2017 the
primary source of data is uh apps and uh
nav in in particular but it could be
anything else a lot of other things so
it could be sensors that you have in a
warehouse um it could be data about how
users use an
application um it could be external data
sources such as weather forecasts and
and so on lots and lots of data so what
the CER intelligence then provides is a
technology
stack that uh goes all the way from very
basic information and data management to
pre what we call preconfigured Solutions
so data information management is all
about retrieving data transforming data
copying data uh and so on um there's the
ability to store data in Big Data stores
uh not SQL server but for example AER
data L and then the fun stuff starts up
here so machine learning and analytics
are part of this uh what is called as
machine learning and powerbi is is up
here uh dashboards and finally there are
preconfigured solutions one of which
we've built into nav 20
2017 right so this is just a rendering
uh same information but a bit more uh
detail and what I'm going to talk about
now is uh machine learning so what what
is machine learning and how can we use
it in in na AV so uh first of all um I'm
going to so I'm going to spend uh 10
minutes or so talk just talking about
the machine learning giving some
examples that are relevant to to nav so
so this is not necessarily a
prerequisite for using the apis that we
have build into n but I think it gives
well it's it's useful to have an
understanding of what is going on
underneath uh underneath these so um I
have some scenarios here and I have some
uh
different types of machine learnings but
first of all machine learning is a way
to teach a system to make uh predictions
for future data based on historical data
it's a bit different formulation than
the one Vincent came up with but uh I
think it makes good sense so let's take
a couple of examples so one example is
um the first one here will we have stock
out of an item so as we are selling
bicycles will when will we or will we
run out of stock at some point in that
case the historical data would be
historical sales of that that item right
so last month we sold 20 the month
before we sold 15 we sold 10 five and so
on very easy uh regression here so we
probably sell 30 the next month and if
our inventory is below 30 well we'll
probably run out of stock right so the
prediction we want to make in that case
is the inventory level for an item or
many
items um another example uh of a
scenario would be will we run out of
cash so will will a company run out of
cash um in that case what we want to
predict is actually cash flow so how
much cash is coming in how much cash is
going out what is the balance between
between those two and the historical
data that we we then need in order to do
that kind of uh prediction is uh
payables and receivables history at
least there may be other things that
that that we would want but if we have
that history we can make a prediction
based on that a third example is uh
whether a customer will will pay an
invoice late which might also be useful
in this cash flow situation so in that
case when we are uh creating a sales
invoice shipping something to a customer
we would want to
predict yes no will the customer pay
late so what so how do we enable that
how do we teach a system to do that
those kind of predictions we need some
historical data and in that case the
historical data would be historical
sales invoices for customers with um
payment dates so you can determine
whether you PID the L or not fourth
example uh would be uh which items can I
sell to this customer right so
um if I am if I'm in a conversation with
a customer what are the most likely
items that the customers buy that would
be the prediction that I would would
want could want to make and how do I
enable that prediction well I do that I
could do that by having a trans action
history for item uh bought by customers
and then try to find similar customers
that are similar to the one that I'm
doing the prediction for my last example
is uh ER the scenario is which uh
discount rate is optimal for for for
this sales invoice so the idea would be
to uh find the discount rate that would
be optimal such that the customer will
actually um buy based on the quote and
uh we would get uh the optimal amount of
of profit and the historical data there
would then be at least sales quotes and
invoice histories so I chose to have
these uh five examples because they okay
they both span types of machine learning
that is interesting in EAP or financial
applications and they also show what we
have built in and what is enabled using
HML so the first two examples up there
they are examples of forecasting or time
series forecasting so the historic data
for an item is a Time series and what
you can try to do is to continue that
time series based on properties of his
the historical data so that's built
directly into nav
27 using the time series API the last
the third one this one about will the
customer pay late yes or no that's a
classification it's actually a binary
classification so we're trying to we're
taking some data and putting in it into
one of two classes yes yes or no zero or
one true or
false um the fourth one is uh is
recommendation so you basically try to
find uh items in this case to recommend
to
customers based on either um well items
they've B previously so items that are
close to those items or customers that
are close in some way to uh to the
customer and the and the last one is
then uh regression so finding a
numerical value based on based on
historical data the last three uh right
now we'll have to use Asia ml
integration I'll show an example of that
um we hope to build apis for these uh in
the future but but no no guarantees on
that
um so let's take one of those this um
late payment prediction uh example so
let's say that the the UI that I
eventually want is something like this
it is recommended to ask for prepayment
for this invoice details never show
again uh something like that so this
would appear uh in my in in the sales
invoice page as I'm filling out an
invoice so I've filled out the name uh
the items the uh discount the payment
terms the uh address and so on and then
I want this uh this this notification to
appear
so so the question is how can we
actually enable this using uh machine
learning how can machine learning help
us us do that um so one thing you could
of course do would be to uh to take this
very specific scenario goes through all
your data uh try in some way to make a
big if then else uh function in the code
unit that would predict whether
customers would pay later or not but but
the what machine learning promises is
that well you can basically
take all of these problems that are
similar where you have data and uh
machine learning algorithms will will
train or give you something that can
make those kind of decisions so um in
this example we'll need to get some
historical um or example data so uh this
would be actual um historical sales uh
invoices so I've made an example it's a
bit of a Mickey Mouse examples you'll
probably need
uh more features of the data than this
but in this case I have
um I have three examples in my
historical data so for the first invoice
the customer paid $100 or three lines
the post code that the customer had was
Urban um the the customer on average
never pays late always pays in time and
in this instance the customer was not
late the second one was for $50 there
were four lines uh it was a Suburban
postal
code well and now realized that yeah
maybe the
uh examples are a bit biased here
towards Urban postcode but anyway but
the Suburban guy here uh he he paid uh
two days or he pays two days late on
average and he also paid late in this
case right so um these uh columns here
we call features so in this case I have
actually four features
of my uh historical data that I would
like to use as a basis for prediction
the last column here oops sorry the last
column here is what I want to predict
and and we call that a label so in this
example the label is this late yes no uh
true false 01 um property so this is
what we want to predict so in order to
train a model we need both data that has
the features and data that that has the
the the labels so um what do we next do
well we divide the data histo the
training data this historical data into
a set that we train a machine learning
model on so it could be that you do it
on uh you take 80% of all these sales uh
invoice data lines and use that to train
a model you hold out 20% Then you get a
a machine learning model that can
actually uh whoops given something like
this predict the label
and then you use the the 20% to test if
you actually get uh the right label
compared to what you had in historical
data if you're satisfied if you're the
properties of the predictions are uh
such that you're happy well then you're
ready to put put this model into uh into
production um so basically to enable
that uh that notification we would have
to find this set of historical sales
invoices run it through a machine
learning model get a model back put it
into code unit we'll see how in a bit
such that whenever you do a sales
invoice you give this partial data these
four features here to the model and it
will tell you whether it thinks the
customer will pay late uh or not and
then you do all the stuff that yes but
just showed hook hook it into the S
Sales invoice with the events and um
show
notification but let's go let's just go
a bit deeper because I think that's also
instructive so right now as I've talked
about the process of getting historical
data training
data then you train a model and in some
way you get something that can predict
back so that's a bit of magic but but
let let me show an a bit little bit
deeper example here so um one example of
a machine learning model is a decision
tree so that's basically a and if an
else
statement over your data that has been
trained by a machine learning algorithm
so um in this case you the uh the
algorithm that trains the model would
try to F would try to find the property
that divides the data best into
categories or clumps that have the same
prediction so maybe it's the algorithm
will see that it's the average late days
for customers that best predict whether
or not the customer will pay late again
seems reasonable right so um so the
first step in in this decision tree
could be that okay so uh if the average
late days
are I don't know less than less than one
let's predict that the customer doesn't
pay late and if the average late days
are greater than one let's predict that
the customer pays late now that's not
perfect right so maybe that's an
accuracy of
80% uh something like that so in in 20%
of the cases we guess wrong or the
algorithm gets us wrong right so even if
we predict that the customer will be
late some of them were actually uh sorry
were not late some of them were actually
late and the other way around here right
even if we predicted that all of these
would be late some of them actually paid
on time so what what does an algorithm
like that do well it it
continues um to the
uh to the next to the next level right
so maybe the next um level that the
algorithm decides to go into would be uh
to look at the total uh of the sales
line I had that feature and maybe
another thing to look at would be
payment terms right so do you get a
discount if you pay early then Pro maybe
people will pay on time or early um and
maybe if it's a big invoice uh it's more
likely that people pay late so so that
algorithm this decision tree algorithm
can continue in that way the output will
be a three in this case uh now it's a
bit better right it predicts a bit
better uh we might want a bit higher
accuracy and other properties of the
prediction but what you basically get
out of this training maybe you have
millions of sales invoices hundreds of
thousands of sales invoices that you
want to train on is a model that is
compact
so it's basically a rep representation
of of this tree you could even write at
least this Syle thing here in in Al code
in a few lines if average late days are
less than then and so on um so that
that's actually a general often the
property of machine learning that it's
difficult or expensive to train them
these models but once you have them
they're cheap to to use so so basically
the the um I mean the runtime cost of
using this is is is constant in time so
I have a sales record I can in constant
time get a prediction whereas the
training
um is more
expensive right and and now that I have
this this model the the that I have
trained on my historical data then the
expectation is that future for future
data that is customers with the sales
orders they would behave similarly to to
previous customers and if I have enough
data that would most probably be true
right so often if you have more data the
more data the the better in these cases
now this is a very simple um even
simplistic example so you you would
probably make many of those decision
trees you would combine them you would
do all sorts of Tricks but we have tools
for that asml but but at least I hope
you U you follow sort of the gist of of
machine learning now okay so um so let's
try to look look at what we then have
done in um in nav uh 2017 so now I'm
going to show examples of of Time series
uh
forecasting can you switch please
yep so
um let me
just
duplicate
so one of the uh the areas in which I
said we had used machine learning is in
um in item sales forecasting so in this
example here or in this demo data there
here I have um a bunch of
items um if I go into let me go into
into this this item uh I can see a uh a
forecast so in this case the uh
well the um I'm showing an inventory
inventory forecast and I'll pretty soon
run out of of these black
chairs um so what I could do here is
then to create a purchase order or
purchase
invoice uh based on um on on this
information that that I have gotten from
machine learning and whoops you have a
new
notification and in this case you I can
then add uh these items that uh I
apparently have previously bought from
first up Consultants to this purchase
order and and automate this this
process right so um so first of all this
uh this forecast here let's look a bit
more
into how it is uh it is set set up so
it's a Time serious prediction meaning
that we um summarize over time series
data in these in this case uh uh item
Ledger entries and uh we do that in
buckets in this case of months so um we
have a data point per month we go
back
um we um we go back 24 periods so we go
back two years with this data um when I
want a prediction I want the prediction
12 months ahead that's may maybe a bit
uh over optimistic on the accuracy of
these algorithms and here I'm saying
this is specific to this feature that if
I um look three months ahead and I can
see that I run out of stock in three
months then uh let me uh let me um make
a stock out
warning um then there's some some things
here that are uh maybe particularly
interesting so it's not that we have
built uh machine learning algorithms in
in Al code um uh we we use this part of
Cortana intelligence called ASA machine
learning and these um these two here is
uh an API URI and an API key that you
get by instantiating a um prepackage
solution that that we've
created um and there a few more uh
things there have of Interest one thing
here is
that um this error percentage so we're
basically saying that if our prediction
if we can see that our prediction is
probably more than 35% wrong let's not
um show the prediction to the user so
for example if I have
ER if if I predict that next month my
inventory will be 10 and the error here
is 50% well what my inventory will most
probably be between five and 15 which
may not be be super useful but let's
look at how you how you set this up so
in Dynamics 365 this is this is
basically set up out of the box so we
pre-provision maybe you saw uh
Constantine and camil's talk yesterday
we also pre pre um provision a bunch of
these machine learning web Services uh
when we deploy Dynamic 365 we store
these uis and keys in as a keywall and
retrieve them but you can also add them
add them directly and how do you do that
well what you do uh is
to instantiate our model this time
there's forecasting model in the K
intelligence Gallery so let me try to to
do that so this is a forecasting model
for Microsoft Dynamics 365 for
financials it's called that for for
marketing reasons but it also works just
fine for Dynamics uh Dynamics NV so
there's bunch of descriptions of how to
use the model uh the properties of the
model um even the internals of the
model if you're interested but there's
also a button to actually um start
deploying the model so that we can use
it inside in a so let me do that so it
says open in studio and now I'm going to
to open what is called as machine
Learning
Studio which is a tool
for
creating and evaluating machine learning
uh models so
um in this case I'm copying this
experiment I'm going to do it in this
region other options would be these and
I'm going to copy it to what is called a
workspace which is the as resource
that as your machine learning uh has as
its core called smarta Tech days let me
do
that
so now that I have um have done that I
get a
um graph so this is like a data data
flow graph of this experiment
um so I'll go through it uh in a bit but
let me just show how you deploy it so
you run it in ASA machine learning it
validates that the experiment is uh
valid um it takes a while a couple of
seconds in this case and then you deploy
uh a web service let's deploy a classic
web
service so that will create an an S
results which which is a web web service
that will when invoked use this model
here and now this API key that I showed
in the UI turns up here and we are using
a request response
API for machine learning so this um API
URI that was in the the UI turns up here
so what I can do now is copy these to um
to uh to NV and then enable machine
learning but I already did that so I'll
I'll keep it like that Um this can also
be automated with with pow shell and we
do that of course in Dynamics
365 um but let me just go back to this
uh
experiment uh and have a look at
it so
um the core of it is an ask script so um
R is a um statistical programming
language that's
also um very useful for machine learning
and for advanced statistics so um this
basically gets executed when you uh when
you execute or call this web service and
what it does is to select a Time series
model behind the scenes that that best
matches your
data and then do a prediction on uh on
that uh using that time series model or
that machine learning model and then uh
this part here oper operationalizes this
this experiment as a web service so give
it an input and
um the model
runs um you split we split the output
into two parts one of which is actually
the
um the prediction and another one which
is um data about the prediction so
that's the the basics of of HML I'm
going to go back to that
um in a bit so let's switch
again so but now let's uh let's look at
some uh some code here um so this is
what happens at the core of that
inventory forecast uh example so um
in this uh small uh snippet we use the
time series API and initialize it with
an API U and an API key so these were
these ashure ml credentials that we got
from from running running the
experiment um we then set a filter on uh
on item ler entries so we're looking at
sales um and then we prepare this item
leer data for forecasting so that's
that's the sort of the core of of of
this API that you
can um point to a uh table in this case
item thater entry and uh some fields on
that table so the first field here is a
grouping mechanism so we might want to
make predictions for many uh for many
items and if we do that we can group
those by in this case item number the
second field here is a type
stamp uh a date in this case so since
this is time service forecasting we need
we need a date um the last field here is
a a quantity so the two properties that
we need to do time Ser forecasting is a
date and a and a quantity and we have
that in the item Le ler
entry I then say that I want to um do a
monthly uh forecast or forecast based on
a monthly grouping of data I wanted to
start um on work date and I want
predictions 12 months ahead next thing I
do here is to uh then actually do the
forecast so this is where the the call
to asman happens um this Bas uh this
stuff up here basically just does data
prep operation and finally I get uh get
the forecast and
exit the value of uh of the forecast
s
again so
um so in this in this code unit I'm I'm
basically in invoking this method with
one um item number and then returning
the uh the forecast okay so it turned
out that for for this specific item we
predict that next month we will uh sell
minus or sorry sell
16.95 CH or what it
was right so but let's look at um a bit
more detail here so um I'm going to uh
to show um how the prepared data looks
just for having a deeper look and how
the um forecast that we get back uh
looks so let's let's run
that so still get this message so this
is the uh this is the prepared data so
since I only has specified one item or
group ID as we call it in in this
example um I have a Time series for um
for
um
for uh yeah for just for for this item
um I also so actually the 12th that I
specified there is how many historical
periods I I add so I have 12 uh 12
historical periods here of of sales
going from somewhere in 2015 to some
sometime in
2016 right and that is being sent to HML
and what do I get back so uh so in this
case I get I specified that I wanted
three um periods back so I get three
periods right so
1896s is in Period number 13 going to
sell around
17 then around 16 and then around
15.6 so what's the other things here so
so this is basically the um sorry should
that so this this is the the best guess
at the value this is then a Delta so
this is saying that okay we're we we are
guessing and actually in this case
rather somewhat certain that we are
selling
17 items but we will most probably sell
plus uh 17 plusus
3.46 so uh
between um at least between uh 14 and 21
of these so so that that may or may not
depending on the item be prediction that
we can use and in general these
predictions get better the more
historical data you sent and
um the more stable properties so to
speak the the sales
have okay I think that was
that so um so I hope that um that that
that showing this uh time Ser forecast
API convinced you somewhat that this
specific form of prediction is rather
simple so it's a matter of filtering
your
data uh preparing it through the time
series API and creating a forecast so in
essence you you don't have to think
about any of um the intricacies of
machine learning that I talked about
initially um which which is
good um so we've done some of that that
work for
you I'm Pro yeah so um
let's switch again so I just want to
show one other example where we
um where we use um this time series API
so in order to do that I need to be an
accountant so let me become
one
yes
so this is um the accountant role Center
so in uh in this case I has I have a a
cash flow cash flow forecast so the cash
flow for forecast is actually a
uh combination of many different things
so
uh uh money going in money going out
right so something you receive something
you pay some liquid funds future sales
orders future purchase orders that from
your C cash uh tax which you have to pay
um and also then cotana intelligence or
container intelligence contribution to
to this total so this Orange Line
basically shows the the total of our
cash uh and it's going up which is good
um so again what we do is to do
something similar to what what I just
shown with the items so we take the
history of uh um of payables and
receivables create two times areas and
do a prediction of of that and what we
then get back is something similar to
this so these are cash flow forecast
entries that come from kasana uh
intelligence so it's predicted payables
for a period um and it's predicted uh
receivables for uh a period as well and
we then add those to to uh to the cash
flow subtracting the sales orders and
purchase orders that we know about
already so um basically this was pretty
easy to build using this time series
library because we already had the uh
the complete infrastructure and uh
machine learning algorithms in in
place okay so
um I also or we also promised to talk a
bit about um sort of of the broader
Cortana intelligence
so among others these other uh machine
learning types classification regression
and and
recommendation so what I'm going to do
uh now is to do a different uh example
so um I'll explain it uh but it shows
how you can create a classification
model in in um in HML and I chose this
because it has something to do with
finan or CM at least and it also um
comes with a set of data so um the idea
is that um so I'm going to go back to to
to as machine learning so the idea is
that we
uh the scenarios that we have we company
we we're doing direct marketing so
sometimes our direct marketing efforts
work sometimes they don't but we would
like to actually predict for a given
customer what is a good way of doing uh
direct
marketing so um what I have
here except for the time series for
forecasting model is a uh an
experiment that
uh that I've adapted or taken from um
the Cortana Gallery actually so um this
is more
a sort of a problem specific uh
experiment but let me explain what it
does so it it start out starts out by
importing some data so in this case it
Imports data from Asha blob storage so
um a blob with um CSV
data it then uh takes some of the
columns in that CSV data it does a split
in training data and evaluation data as
you remember I I talked about so in this
case it uh it takes 70% of the the data
for training this is the left side of
this box and 30%
for uh
evaluation so if you follow the training
path of this data flow diagram we train
a model now it turns out that uh the
best way to uh to do this prediction is
a what is called a two class decision
jungle so this is actually something
that takes decision trees and makes a
lot of it how did I find that out well I
basically um did that by
um by
um trying uh sorry trying sorry let me
let me find it
um so this
decision by trying different uh models
so for example for classification
there's a whole bunch of different
um models that are all based on decision
trees as you saw uh so you can basically
try these out and then select the best
one
um so the model is trained and then
scored against that uh evaluation data
set and then you get an evaluation
out so let's go back to this uh import
data I just want to show you how it
looks so and why chose this so this is
the data set so I think it has some
60,000 records of direct
marketing
interaction um so it has some recency so
how long time ago did we actually last
contact
our
uh trade with that customer it has a
historical um purchase amount so in this
case uh for for for this person here
it's 142 uh
dollar um the person was interested in
both men's and women's
stuff um the customer is from uh
Suburban
place um not a newbie uh and the channel
that we um connected the person on to to
the person on was was phone in contrast
to to web or multi Channel or whatever
we have down here
um it's women's email segment and well
it didn't go so well so the customer
didn't actually visit the store after
that didn't spend anything of course um
so just another case in this case here
um with a women's email also Suburban uh
a little bit bit less spent and so on uh
we actually got a visit but no
conversion or no spent so um that is all
the data that we um that we
uh are going to train on the label is is
this that's the visit that's what I want
to predict so um so in here in in
training uh the model I'm saying that
here that um that I'm going to to
predict the visit right and and now I
can run similarly to what I did before
run this model but because not but but
because the um this model comes with a
specific data set or data set that is
specific uh to a customer or to and to
that data that the customer H has we're
going to create a um trained experiment
or predictive experiment specifically
for that for that um for that customer
and that set of data that I just showed
showed in in our time series example we
actually have a stateless experiment so
we basically send all the data the
historical data for let's say for an
item when we want to predict we train a
model and we predict at the same
time um and that can be done because the
data is is is is aggregated as much as
it is it wouldn't make sense to send
65,000 rows of um of data all the time
so this is is taking a a bit more uh the
training and and so on but once the
training is done and we have a
predictive
experiment take a minute or
two um the predictive uh experiment can
be deployed as a web service similarly
to to what uh we've done uh
before and in this case again there's an
input uh which would then be one record
of this direct marketing dat data and
there would be an output which is again
actually a record of this data but with
the label the visit label uh filled
in did we
finish yeah so a minute or two um on
this data set I can then publish that
model
um similar to what I did before this
predictive model I can get an API key
and an API URI and I could even uh use
that inside nav so let me let me show
that uh so this is this direct marketing
prediction so in this
case there's not such a nice API uh
wrapping wrapping all of this so
basically uh we use what's underneath
the stack of this uh time series API in
this example so I'm instantiating what
is called an HML connector again with an
API key and an API URI that I got from
from the experiment um saying that that
the experiment has an input and an
output it's called that and in the data
that I sent the label column is number
uh
11 then I um create an input so I create
an input of a customer contact that I
would like to predict so in this case it
um um let say it's a bit long longer ago
um that we were in contact with his
customer he actually he she actually
spent a lot uh was interested in both
men's and women's stuff role uh and so
on I can then send this data to uh to
SML and get an output uh here from from
the
data um first line and column number uh
and then I'm just making just make a
message uh box saying that the customer
is predicted to either visit or or not
visit um yeah so so in this case right
there there's no API support for for
training and there some API support for
for actually using a trained experiment
but let's just run this
one
um and see what it says so well it says
that that that this one is is probably
not going to visit let's take
another another customer here uh and see
what what what goes on so that customer
is then going going to visit so um so I
can now use this model in whatever way I
want in my application I probably
shouldn't be be creating dialog boxes
though but uh something else um and what
you could also see is that the um
actual prediction is much faster than
than the training so it takes a second
or so to do a a prediction so this data
preparation and
call um yeah let's go let's go
back
so almost wrapping up what else can you
do with
um with the Cortana uh Cortana
intelligence so uh apart we haven't
really um integrated yet I would say
it's it's cognitive services but you
could imagine thing there lots of things
you could do with that so in this
example I have two of our items taken
from from the item catalog and one of
the services that
um cognitive Services has is a v
computer vision API so I've actually ran
um these two items through that um that
Vision
API um so in this case I get uh
well that wasn't let me get out of that
didn't help so in this case I get um
back a what Cartana intelligence think
this thing is you might not be able to
read it but it says okay this is this is
probably a black chair and it's pretty
confident maybe not super confident but
uh with 44% certainty it thinks it's a
it's a black chair um it also is very
confident that it's Furniture a seat
that is black that is for indoor on the
floor and it's a
chair uh and not so confident that it's
actually feet which is
good um so the nature of these things is
that uh I think so apis like these
continue evolving for some items it's
pretty good for others it's not super
good so this is uh as far as I can see a
red lamp right
but it actually predicts that it's a red
bike to its uh at least it doesn't it's
not very confident that it's a red bike
so maybe we shouldn't think that but but
at least it can see that it's red which
is not uh surprising so um apis like
these could be used in in in a number of
different ways here's another example
where I ran some of the uh images of um
contexts that we have through uh through
the face detection API so there's both
an API where you can detect who is on
the face you could use that for
authentication for example but that's
also an API where you can detect
properties of faces which you you could
use for other things so in this case
here right there's a a guy here uh with
glasses um so the API says he's 42
probably it's a
male uh he
smiles he doesn't have a mustache
doesn't have sideburns very little beit
and he has reading glasses so this is
actually pretty good A lot of things you
could you could do with
that maybe coming up okay so um ending
up or wrapping up so in summary uh we've
tried to uh present a set of features
that uh we hope and expect will make nav
appear smarter more proactive and lead
to a better user experience potentially
better user experience in in nav and
we've done that by um introducing and
using this notification API so it allows
developers to build context aware
notification uh using a a builder
pattern so you create a notification you
add the properties to the notification
that you want and and you send it off
you can also retract it uh change it and
so on right now we support these in
context local notifications we also
presented how we used um cotana
intelligence so one part was this time
series uh forecasting API in which you
can basically take one one of the 300 or
so tables we have in na V with the time
and quantity
data massage that and put it through
through HML and get a prediction back
and finally I showed some of the things
that are also possible with uh with
cotana intelligence but maybe right now
with a bit more uh
footwork that's basically it thank you
yeah thank you
lot and uh questions now you got the
honor of throwing this
one here you
go I have a couple of
questions um you were talking about the
prices and how is the prices going to be
for uh the unpr nav
2017 right right so there there is of
course a price to uh machine learning
it's Microsoft so um so there is
actually uh so there's a free tier which
is absolutely useful for experimenting
and also small scale
um deployments there's also usage tier
that cost around $10 per month which you
can use from for multiple customers uh
multiple deployments which contain a
large amount of
of machine learning
capacity yeah okay so and um my other
question
is how about doing these experiments do
you need a lot of training to do it or
can you as a noral nav developer just go
in and start doing experiments and yeah
trying to figure out new ways to do it
yeah so I so uh I don't think that uh
any Naf developer should all the Naf
developers Just sh should to start doing
a doing these experiments I think that
asml is fairly easy to use and and um a
good way to do data science machine
learning I think the way to start would
be to try to use to utilize the time
series API which is basically a wrapped
up um HML experiment that you don't need
to to to look at which is prepackaged
for for nav okay and my last question is
how about data and how do handle the
data do Microsoft use the data that they
are getting from all the partners and
all their customers or is it yeah just
for our own
winning so technically in um in asan
machine learning the storage of data if
there is any is is is in there's a blob
storage connected to to one of these
machine learning workspaces and if you
store data it goes into that blob
storage
but in general Microsoft doesn't look at
customer customer data so it goes in
there um it's not something that that we
as Dynamics or nav get any well can look
at so um so if you I mean if you trust
the U sort of privacy features of Asher
you should be you should be
good
okay I have a question about um
synchronous
asynchronous execution of notifications
on the example you had a c which we have
you have a call which called
a post code API what happens if this get
stuck because then you call this event
even subscribers take the call and then
call something and then my Stu in this
place waiting for the answer from the
service what will happen then what would
be re reaction on the system well uh as
the code was constructed if the service
would time out then the notification
would never be launched uh so you would
actually never ever see anything so the
user would not recognize that anything
has happened and then the background
session would time out and then that
would just disappear U but of course if
you do something uh on the action uh
that you invoke on the notification then
obviously the system gets stuck so the
asynchronous uh property is good before
you show the notification if there is
any delay in whether you need to show it
or not and then the action you should
make sure that it's something that
happens immediately else you have the
same behavior as you have today with
just clicking a button and then you have
to stall and stare at your screen until
something happens right yes but the
event itself it fires synchronously so
as long as you finish the unv validate
code the event is filed and at that
point uh the subscriber gets control
yeah but it doesn't block the user so it
uh but you're you're right right so in
so in some of the cases for example
where we do item for forecast that can
potentially take a long time right you
have a thousand items you want to do a
forecast for that it's probably going to
take some minutes so what we do there is
basically to create a job queue entry
that runs in the background stores the
predictions and then we use that
whenever we need to uh to present a
notification so that's the solution
right now if possible okay thank you
yeah thank you first question to the
katana intelligence um have you tried
this um forecast with a is a real
customer where he maybe buys 1,000
products each day and has millions of of
item Ledger entries to to calculate is
this possible in in
time
so we don't we haven't tried it with a
customer with millions of item that you
interest no so um so we've this is this
is probably for for a smaller for
smaller data sets and for a smaller
customer um so but but if you can if you
can run this calculation of these
million on this million item that
entries in in reasonable time in a
background session then you can then you
can use the API so because the amount of
data that you actually sent to cotana is
is small so it would be the data
preparation that would be be the problem
right and you can optimize that okay so
so the the time it takes to send for
each item and to get the answer back
what's what do you expect what what time
delay do you expect for each item uh so
less than less than one second half a
second so let's say that you have around
100 um historical periods it's it's on
average around the well tens of
milliseconds okay so it's pretty pretty
pretty fast
