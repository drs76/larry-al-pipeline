# NAV TechDays 2019 - How to make AI work for your Business... Central

- **Source:** https://www.youtube.com/watch?v=YvAvC3H2Ebc
- **Video ID:** YvAvC3H2Ebc
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 97m15s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

[Music]
thank you
good afternoon how are you doing
you survived to the last session
of our conference
yeah it's always a great experience to
have a
last session of the conference
just just after the lunch
so
i'm lucky
um so my name is dmitry i am
mvp in business applications
i have about 15 years of experience in
nav but also i have an experience in ai
for about three years so i have
like a mixed
something mixed in my brain
so um i live in saint peterburg
i have two kids
so today we will uh speak uh about uh
well it's artificial intelligence and uh
but it's more marketing world we will
dive into this uh word we will
look into the machine learning process
uh and then
we will dive into business central
frameworks that allow you to deal with
machine learning
um
areas um
yeah so by the way who was in my
session about artificial intelligence
last year
okay
uh so yeah last year we i was focused
more uh like how to build
models from scratch
so i will not focus on this this year i
will focus how to consume
ready models uh but also uh point you to
the
some examples how to build uh models
from scratch
if you want
so
but we before we start um
i just ask you to talk uh to take a
selfie
and send it to this
mail
you can use qr code
to access your
email
i will not do anything with your
selfies and with your emails i will
drop it just after the
session
uh i will do
self film by myself as well
myself and doing your selfies
so
yeah
done okay
so um for example
well
every um every
task
well you i think most of you are
developers or if you are even
consultants or managers
your job is to solve some
tasks yeah right but and you need to
uh know what you are going to solve so
for example
uh your customer manager or maybe wife
asks you to solve some case um
like uh how many items i will sell next
week or maybe your wife asks you how
many how much of them can i buy
um
and what you normally do in this
in these situations
well in the past in in
92 percent cases of today
you start uh conversations so what
influence on uh this task so
if you want to uh if you want to sell uh
something and you sell that before
uh and you want to to know how much will
you sell in the future so
actually you will
do some conversations and ask questions
so what influence on your sales
and then uh there is some yeah this
brainstorm phase when you can
just think about uh what's influence on
your sales
uh then i'll i think it's not the
correct slide not maybe with your wife
but yeah then you end up with final
solution
um
and your final solution
usually is an algorithm
so
algorithm what is algorithm is a
combinations of if else right so
if some item if it's a weekday or
saturday
maybe like this
um
if there is some event
near your
place where you sell your items
and many many ifs
then your forecast will be like some
value
then combinations of else and somewhere
so it's an algorithm
that's actually uh what we call
classical development approach so we
start with some
uh question what we are going to solve
uh then we define this algorithm
then we actually code that
then we test that
then we release that
and we
cycle that
throwing this away
so do we have an alternative to that
yes
and the answer is data
so um
think about uh the situation when
uh somebody
or something
uh just looking at your data
can produce
uh this
algorithms for you like
that will be uh the bottom also
combinations of many if and else but you
don't care how you just have a data
so for example you have some item ledger
entries or any kind sort of data in your
business central
and there you have
actually two groups
of
columns
the first group of columns called
features so what are features
features actually
something that influence on your future
predictions in this case uh
something which influence on sales if we
want to predict sales
in uh the other group actually it's
usually one column
uh it's something that we want to
predict
and it's called a label
so with the machine learning process
usually will you will see these two
terms features and label
so features what influence on
features something which influence on
labels
then
have this you just apply some magic
let's call it like that on current phase
which is called machine learning so
machine learning actually it's a
collection of mathematical algorithms
which are not something new which
were created like
in the even in the previous century
and then you have a predictive model
so predictive model is uh some kind of
black box or in a machine learning world
it's called a learning function
and that knows
how to get
labels from features
okay so this this is actually a
collection of this if else on the bottom
okay now we have a model
okay
and you want to predict future
you need to
tell
this model
what will be the features in the future
for example
you want to predict well in our case
sales and maybe
uh currency exchange rate or weather uh
other our features and they influence on
our sales
if you
uh trained oh i will
um
explain what the strain the model uh
further but if you trained if you
created this model using these features
uh that mean that you
to make a predictions
you should know what will be the weather
what will be the exchange rates in the
future so
many people actually think that
that machine learning is a some kind of
black box
and you have many different unsorted
data
and you just
push this data in this black box and
then you can just ask everything
well it's not like that
um
what on
on those features which which you used
for creation of model these features you
should use only to get predictions in
the future
so yeah actually without any development
in our case
um because we will use
business central framework for that
well almost without any development
and
now when you have this trained model
um
this model actually is done with the
artificial intelligence but yeah
artificial intelligence is more like a
marketing world actually it's uh
done by machine learning
so
two terms artificial intelligence and
machine learning
do you know the difference between them
yeah so so
so artificial intelligence or ai
actually
it's not a technology
it's
tasks uh that are characteristics of
human intelligence like
vision speech
language understanding uh maybe some
predictions and so on so
um
it's some kind of tasks so
very complicated tasks
that very
easy to
solve for us as a humans but very
difficult to develop
in the software
machine learning in this case it's a way
of achieving these tasks so these
machine learning are
the techniques the algorithms the
process so this the tools um
that allow
to create this um if else models on the
bottom from the data
so that's
mostly statistical algorithms uh used
inside
but i think um well if artificial
intelligence only tasks
and machine learning other tools can we
solve
artificial intelligence tasks with a
classical development approach
well technically yes
because
if you remember maybe in the beginning
of 19th there are there were
some ocr companies that tried to
recognize handwritten texts using the
classical development approach
uh
they
invested millions of dollars
in the millions lines of codes
and the quality was
poor right
but still
you can have this uh as an option
there is something in the middle
actually uh where you you can use as a
hybrid so
for example which mean that if you have
some complicated task
uh it's uh not always could be solved by
only machine learning
process
you can divide these tasks into
sub tasks part of them solve with
machine learning part of them with a
classical development and then combine
them to get their final result that will
be hybrid
so
one more important to understand from
that that
in machine learning process computers
learn from the data
why
ai became became so popular today
because mathematical algorithms they
existed before
that because of uh now we have too much
data
we can just
apply it now we have can apply these
mathematical algorithms to the to this
data and we can and we have uh
resources to calculate them
so some statistics uh for example before
all the humanity together produced two
exhibits of data like from the beginning
of humidity
community
then in 2013
all
we produced 10 exabytes of data
in 2019 we produce
so actually now we produce about two
exabytes of data every day
so that's
wow
right
so where ai could be applied
well actually in any kind of
industries
like a food industry you can check the
quality of the
of the products uh you can uh forecast
uh yield of the
um
food and oil and cooking and so on in
the
production for example
oh i i had a real case actually which is
uh
which works
um but i i don't think if it's legal in
uh
in belgium
but it's uh
legal in most of the countries like uh
netherlands the u.s some states in the
u.s so let's call it uh plants
so
there was a manufacturing process of
growing plants
and
actually we used their custom vision
model we trained custom visual model to
analyze the
uh
phase of growing of this plant and we
connected that
to the iot some iot devices where
it actually analyzed if
the current phase uh
of the plant is normal or less or it
should grow quicker and then it sends a
commons to a
uh to increase lights for example and to
increase temperature and so on so that
was interesting uh experience
unfortunately i didn't have
enough just samples for that but
yeah
just to remove some remote work
so everywhere we can
apply artificial intelligence with uh
some knowledge of how to apply and with
some creativity
so let's uh move into the
business central
we have in business central uh
predefined frameworks
to
train machine learning models
actually
so here are the
uh apis so i i
that's not like the official
split of this frameworks but i split it
on this
way
i think
because every
framework here solves
some special type of tasks
so now we will go through each of these
frameworks see them in
in action
how you can
develop smart applications using these
frameworks
uh microsoft also
use uh these frameworks in some of their
extensions that comes with uh business
central as well uh like a time series
that the oldest one actually so it is
still it was it uh appeared in i guess
nav 2017
uh
maybe in 18
so inventory sales forecast and um
cash flow forecasts they consume this uh
framework
then
uh ml prediction it's um another type of
a framework
late payment prediction extension use
this framework
to get predictions
then custom azure ml it's um
well it's built for
custom models created
in azure machine learning studio that's
something that i showed
uh last year
then a custom vision it's a image
analyzer tool so
to train actually
uh well not to train but to get uh
predictions about uh what's inside of
the image what's some what's text and so
on
so let's look in the time series api
where you can apply this
one
um you have data in business central and
what's important part
um
these data
should have a
date field which will answer on the
question when
happened
uh it should have some
master
data reference like what
for example item number if you want to
get the forecast for items or customer
number if you want to get information
about some customers and so on
and well how much
it could be quantity amount or whatever
but it should be some
decimal or integer value
then
you
get you take the prebuilt
model already
probably for you you just copy that to
your azure
resources and and publish as a web
service
and then you call this web service from
business central uh using this at time
series api which is stored in code unit
so let's see
the demo for that
i will show uh first the process then i
will drag you into the code
how it works
so uh assume we have uh here
some yeah you see the screen so you say
assume you have here uh like a
uh item ledger entry but this is
actually my custom table
um
about the sales of my items
with some additional fields
so
that's
well in current phase you shouldn't just
know that this is a completely custom
table so it could be any table in a
business central actually
we go to the
items
yeah
of course it's uh
start to be a little bit slow
so we go to the item card
and here
on the item card i have my rolling
action which i created
which is called update forecast
for this item
uh which he's doing now uh he
gets all the historical data about this
item
sends it to
my
published web service to get predictions
and return me
the predictions about sales for this
particular item for the next seven days
and you see that we have some values
here but they are
the same for every day
i will describe why
a little bit later let's go to the
code first
so
where is my
i guess it was my page extension
calculate
forecast
so
how this uh framework um
how how you can use this framework uh
first uh there is a variable do you see
okay or should i zoom it
so uh the code unit calls um time series
management
that's the first variable the second is
my custom table or it could be some base
table in a business central
um and then well date let's
i will i just use a date uh a record to
loop and do and to
make a calls uh for to take a forecast
for each date
uh then i um
use
two buffer tables um
describe it in a moment
and then uh time series model
also describe that in a moment how it
works
so
the first step here
i'm connecting to my web service
you see that here is an uh installation
function with a uri and the key so
how to get this uh web service
um
there is actually um
one uh
well during this session you will see
two secret links who who never knows
but uh they exist
so that's one of them
uh gallery.azure ai and slash uh the url
to this uh model
um
you
that's a here at the description of the
model but what you need to do is uh
click here open in studio
that actually will copy
your this
model to your
azure
but before that you need to create a
resource
which is called machine learning studio
classic workspace
just well just find it
here when you create and
you will get it
so
here you click launch machine learning
studio and you will get to uh here
so
this is machine learning studio is
actually a collection of uh so-called
experiments
um
experiment is actually
the process how to train a model and how
to get predictions and then how to
publish that as a web service in our
case
we will get this
[Music]
this picture
so
if i will zoom it
a little bit
we have here a web service
uh input and then web service output all
the magic actually happens here
between
here is uh our code
and if you will see
that
for time series uh
story
it
use three different mathematical uh
algorithms which are called arima etc
and stl
if you are not like
with a
mathematical degree it's okay uh if you
are interested you can just google uh
how it how this mathematical algorithm
works
uh but on this phase you should know
that um
well
technically what they are doing they
take uh your data so
the
date and uh amount and then extrapolate
your values to the future so using these
three mathematical algorithms
each algorithm potentially can give
different results
and
that's why
we also have here
a combination of these algorithms like
all
or etc plus arima or
etc plus steel so
what's a combination it's actually uh
this model will calculate forecasts for
using uh three of the algorithms and
then calculate the average so to make
the uh prediction like better
okay
so now you
well you copied that you actually don't
change here anything and then you click
here like a deploy web service
can i zoom it
so deploy web service
what what will happen it will create you
a web service
here
under the web service tab
with a key
and
url
here will be a url so you just need to
take these two parameters
and insert here
so to initialize a function
okay
now
we need to send
the historical data about sales to this
uh
forecast
uh it makes actually if we want to
predict uh forecast only for one item it
will not make sense to send all the data
about all items so we filter here by the
item id
next step uh which is called prepare
data
actually what's uh what is doing uh
inside
uh he's feeling a
buffer table so
you can pass there any a table
but
to send messages to a web service he
used a special buffer table
with a predefined uh
fields
so you specify
here what
field in your table is a item field
that's from my slide what
uh answering on what question
and uh which field in your table is a
date field
and
so here you specify features
here you specify two features actually
uh item number
item and date
and then you specify a label so what you
are going to predict in our case it will
be orders or sales
uh then you specify how much uh data how
much historical data do you want to
to take from your database to send to
the uh cloud
to get a prediction so you specify here
a period type
uh and here a quantity of this uh period
so it can be a day like you can take
one year so
365 days
uh or one year and
specify here one uh whatever
and here you specify a starting forecast
date so from from which date you want to
get a forecast
then
you
execute this get prepared data
then actually you call the forecast
so with this function call forecast uh
you specify for how many of the periods
you want to get the forecast in the
future in our case it will be seven so
seven days
uh so in this function actually take
your historical data sends to web
service and return forecast
um
and here we actually get the forecast uh
we just fill another buffer buffer table
uh
from the response and here we show the
uh result well to the user or you can do
anything with this uh result
in your cases okay
if you noticed
we
received some forecast from the
web service but the values for the next
seven days were
like the seven day if i remember there
were like 60
67 or whatever
so why the forecast uh doesn't change
because a time series api use only two
features it's a date and in our case
item number
which mean that there is something uh
else that influence on
your predictions that
these mathematical models just don't
take into account okay
so for uh to add more features so if you
have a situation when two features are
not enough
there is an another uh api which is
called ml prediction api
so the same story you have
data in business central
uh when what how much but also you have
another features which what influence on
your sales like the weather
may be
forecast in our case it will be some
events
uh holded by the restaurant
well
there is a limitation
in this framework
it can get
only 20
additional features
so
but in many cases it should be enough
uh you publish a math model
in your azure the same as a previous
demo i showed you it's actually another
model
but the process is the same
there is a new step here
which didn't exist in the
time series uh framework it's called a
training process
what is that so
time series with the time series
forecast you send it to the cloud all
historical data every time you wanted to
get a forecast
which is well
increase your productivity
or decrease your predicted sorry uh and
influence on a time and whatever
uh training process allow you to
get forecast without uh
without sending all the data every time
you train your model once with the
historical data
and then
you get this model and then you can use
this uh model
for predictions
i will show you how it works
yeah and then you just call this web
service using um code unit another code
unit 2003
yeah i guess
sent and then you just send this model
and uh
and also the features about the future
and get predictions
also you can with this framework you can
get some insights about predictions
late
prediction extension actually works uh
using this uh framework
um
so
yeah you so uh here the
development process actually and the
business process
for utilizing this framework uh splits
into two steps so you train your model
uh then you make a predictions using
trained model
uh also uh you can get such uh with this
piece of code you can get a
pdf file from the azure machine learning
service which will uh in a graphical way
will tell you how this model thinks
so this is actually those if else uh on
the bottom um
how the model
uh
trained itself using your data so it
take one feature which
uh the model thinks is the most
important feature for this uh forecast
then if some value it goes to this uh
direction or other direction uh this uh
this is called actually a tree uh view
and the depth of this
uh trees can be uh huge
uh it could be
hundreds it could be thousands even um
different
uh
directions
so yeah you take data train model
predict and research let's see the demo
how it works
and just switch to another
branch here
so it's train ml model
i'll first
publish that
and
we will see how it works and then i will
describe uh from technical parts of that
so um the same um data set actually yeah
by the way um data sets is also a term
that you will
hear a lot if you are using if you will
dive into machine learning world so data
set it's uh actually a
table in our case
so
uh i have an action here which is called
train
uh if i will in in if i will call if i
will push this action on current
phase
uh actually i will receive an error uh
that's actually important error that i
want to
uh showed you
uh because
it's not very intuitive uh but in most
cases you will get it
and you should know what to do with that
so
the problem here in in this column which
is called festival name
so the story here is that uh
there could be some
festivals that
that's
going on near my place where i sell some
food and they potentially influence on
my sales but in most cases there are in
most of the dates there are no festivals
so the column here is blank
right
and
empty
values is not something that machine
learning process likes
uh because in in machine learning
process they
they will just skip all the records with
if there is one
in if
in one column there is one
empty values
so how to how to deal with that well
very simple we just will
to train our model we will just replace
blanks to at least to something
we don't care to what but in this case i
will replace just to na
and that will be a value
so now we can train our model
so what he is doing now he takes all the
data
send it to the my web service then it's
actually
apply the
another mathematical algorithms there
and uh as a result returns me a model in
a base of 64 format
uh which actually um and
it it can be like
kilobytes of data
so this file in a base for 64 uh format
we should save somewhere in business
central doesn't matter where just we
will just save it in a
uh some blog field
and it also give us the quality of our
model so
uh
it tells us okay for this model the
quality is 50 so actually for the real
cases of course is very bad
uh but uh at least it's uh
in in this case it's better than a time
series uh api
gave us
also it uh
returns us this
pdf file
which
looking at which are you uh you can um
see how this uh model uh things i will
show that
uh in a minute how you can deal with
that
so now model is trained
and you are ready to
make predictions
so the same way as in a previous demo we
go to the same item
and click here on um
update forecast
what he's doing now
he's sending
he's not sending all the historical data
he's just sending this trained model to
the web service
uh and also uh the features about the
future to get this uh forecast
so we uh see here that well
well the values are
actually the same
um
so what is really the difference between
time series but if you
will look
how we can
look here
it starts with a some um it's something
which is uh
called go list
uh and go list is actually empty in
every row so it goes to no direction
uh then it checks if there is uh
if this item in a children menu and it's
actually not
and then it just give us 140
uh no it's actually goes uh
where did it go oh no it goes i think
here and then here so it's 74.
so if i will
do some adjustments here
i will
increase the quantity of this item
so just
adjust inventory
just i will say that okay i have
too much of that
by the way go list is something that in
a
restaurant business
means that when you
go to the restaurant you will be
recommended to purchase some
item
from the menu from this list so
and then also i can
i can exclude it from the children menu
let's see what happens
if i will
recalculate the forecast once again
so we see that their figures actually
changed and uh
in one day
it's we have uh 135
and other days we have 108 so
uh why this day is special that's
because of here is some event will
happen
which actually influence on our uh
forecast
so
how uh it works from the technical point
of view
so here we have uh two code units so the
first one is uh training
uh so we utilize here the
framework uh which is called ml
prediction management
but also we specify here my model
variable in a text format
we will receive the model in this
variable later
also we specify here our
custom table
and
then we
the same way as in previous demo we
connect to the
web service but what is this web service
there is actually another
link
here
which is called uh prediction experiment
so the same way you open that in a
studio
and that will copy uh here
another experiment
which is called a prediction experiment
so all the same way uh you have here web
service input output and uh all the
magic uh happens uh here
so in this in this uh framework the code
here is uh different
um
actually
with this uh framework which what is
also important to understand
uh it can return you not only uh some
integer or decimal values but also uh
text uh from the uh using
classificational uh algorithms
so uh what does it mean
assume that so there are two types of
mathematical algorithms that can solve
two types of different uh problems the
first
situation for example you want to
predict some value in our case it's
sales
uh it's some decimal or integer in our
in other case for example you want to
predict we which item will be the most
popular during the the some sales and
which mean that uh you will get a
prediction from the fixed list of values
so we have a fixed list of
items uh you and you will receive a
value from this fixed list in this case
in the first scenario
regression so-called regression
algorithms will be applied on the second
scenario classificational algorithms
will be applied
that's also important to know
uh so
and then
yeah so you just deploy that as a web
service
uh it will appear here as a separate web
service the same way you get a key and a
url
and paste it here
then here with a set record you specify
which table you will use for training
it could be any table
also
and here
with this
code you actually specify what will be
the features so which columns from your
table will influence on your sales
then
you also specify a label
so you specify features you specify a
label that's something that i showed you
uh before
and then you call this uh train function
uh it will actually send the all records
from your table train a model or receive
and the output will
give us a model in a text format
where we will save it in a text variable
and also it will return as a quality of
this model
and here you just
save this model inside of some setup
table for example it doesn't matter
where you just need to
then pick up this um
blob uh
when you want to get predictions
and then yeah here is a message that
uh your model is trained here is the
quality
the first step done
uh then you need to uh calculate the
forecast in our case
we call here the same
code unit ml prediction management
also we specify the table where we
stored our model before
and
specify
the
table from which we trained our model
also we specify the buffer table where
uh will be filled with a forecast tables
of forecast values by default
so we the same way we initialize uh
connection
to using the framework
then we
actually set a record here
telling which table the same way as a
previous
example also we hear this specify which
features will we use for predictions
that actually should be the same
features as you used for training that's
important to know
also you set the label what you are
going to predict it should be the same
label as you used for training process
and then you predict
so
and in this predict function you
send this model in a text format to the
web service
then you just get the forecast
in this buffer table temp time series
forecast
and show that to the user or you can do
anything with that as well
okay
going forward
so uh
times here is uh if we compare time
series with ml prediction
we can see that
it's better in situations when you have
more than two
features
it use a tree regression anova
mathematical algorithm
so can we increase the quality of that
model what yes
how we can use more features for example
or we can build custom ml
model
so what is a custom hrml
api
so you built your model in azure ml
studio completely from scratch so you
don't take anything existed you just
built it that from scratch
you publish that as a web service
you call this a web service from a
business central using a code unit 201
and
actually here is the link from the
previous days where i described in
detail how to build this a model from
scratch
but uh here is like uh once again uh how
how you do how you do that
very quickly
so
um you open uh azure machine learning
studio i will show you the demo a bit
later
so
uh the first thing you get your
historical data to machine learning
studio
uh then you uh well using some import
data models
then you i
will generate new features prepare data
for training it's actually optional step
uh usually it's required for machine
learning process
uh if your
initial data set is dirty if you have
good data set it well not required
then
you create actually two
data sets from one that's important step
so you split your data set into training
and testing
then you get you take the training data
set you train your model you applying
mathematical algorithms that exist in
azure machine learning studio
then you check the model
quality
and if the model quality is
suitable
you publish that as a web service
before publishing as a web service you
also do some adjustments to the process
you built the web service input humor
then you prepare data for predictions
actually this step is automatically
copied from the previous uh
step
then you do predictions applying the
already pre-trained module from the
previous step
and then you built the web service
output as human
so
let's do see some demo about that as
well
so i will switch to
another branch here custom
[Music]
custom azure ml
so yeah here actually we have
uh less code because
every old magic happens outside
so we will publish that
ah
so uh here we will go to this um
to this plotting that we used uh before
click on the update
forecast
uh now
now actually what happened
we in in business central now we don't
have anything we we don't have a trained
model we don't have and we don't send
the old historical data to the cloud and
this
on this step
uh in the cloud we already have a
so-called prediction web service which
knows
uh
how to uh create a forecast using the
features you sent using this ml
api
and you see that every day now we have
different value
so
how does it
happen
so if i will return to my
experiments
actually
this is uh
the process i did to train a model so i
import data from um
i can import data from business central
i can import data from anywhere
i actually do here some data
preparations i will not focus here
on the details um
much
uh the
important things here uh two steps uh to
train your data
you should remove duplicate rows so what
are duplicate rows it's uh
uh when you have uh
when you in your data set had
information that for example this
pudding yesterday i sold for
uh 100 dollars
and the second row that this building
yesterday i sold for uh 200 so where is
the truth right
which means that
this kind of problem is called duplicate
rows you need to somehow solve that
in
machine learning studio there is a model
for that remove duplicate rows so you
can
just remove everything or keep only the
first one
then here this another
module uh that actually you saw in a
previous demo
where i just replaced blanks to some
value
we do the same thing here so clean
missing data we replace blanks to n a
so um
here we actually split our data so i
actually i will show you some
visualization
um here is my data set which i used to
train this uh model
it consisted of
um well at least uh
40 000 rows and 10 uh columns
so that's those
table that you saw in the business
central actually
then here i split this data set into two
so
the 80
of the data set will be used for
training and the rest 20 will be used
for
uh testing so if i will take here the
uh training data set
it will consist of 30 000 rows so 10 000
rows will be kept for
testing
uh here is a
module which is called train model
actually it has only one configuration
parameter what do you want to predict
here you specify your uh label so in our
case it will be order
and you apply here uh
mathematical algorithms from the list
existing here
if you will go
to machine learning group
uh into the
initialize model group you will see
actually
four different groups of mathematical
algorithms
the most interesting for us will be
classificational algorithms
or regression algorithms so on this
phase you should understand what do you
want to predict if it will be a some
decimal integer value from an
unknown list it will be a regression
if you want to predict something from
the fixed list it will be a
classification it could be a bull
some boolean field for example yes or no
in this case it will be two class
uh two class uh
mathematical algorithms if you want to
take a predictive value from some
more
bigger list
there is a multi-class algorithms so
that's actually how you
decide which algorithms to apply to
train your model
so uh
when you're well actually to run all
these models here is a
action which is called run
so
it's a green
now i will not
run that because it will take some time
uh and then you score the model what
does mean score model
uh you
uh here actually take the testing data
set which is uh 10 000 rows and apply
trained model that you trained before
and
if i will look here
you will see that now i have additional
column so uh this
uh what this
so that's my testing data set it's seven
and a half thousand rows
what what's happening here so uh to test
the quality of the model it takes the
historical data set
it's and he he tries to well let's say
he tries to predict the past
okay
so uh he takes the old features from the
past
uh for each row he pre he make a
prediction
and then
uh you can compare what happened in
reality and how it would uh forecast
that using your model
so
you can well check row by row um
button
here we have also evaluate model
thing
model
where you can get the
so-called confidence of determination
which will show you the quality of the
model in this case it will be 71
which is well even better than we had in
using a ml prediction uh api
then you
publish that as a web experiment uh yeah
as a predictive experiment sorry the web
service
um
you will get
automatically you will get this uh
picture so
what this picture is about so actually
you you receive here web service input
you just need to specify the schema for
the web service input uh without any
programming just
connected to the model
which comes after
the
data
some data manipulation
so in this case these columns will be
the inputs for our web service
okay
and then you don't change anything here
and the rest in the end
here is the web service output which
will give you
the predictions
okay well actually
highlighted a little bit you by default
get the connection to here
uh where
so by default your web service output uh
will be all your columns from the web
service input plus predictions but you
can live with that
i just
change that a little bit so to have more
clear
web service output
so and in business central
we use another
another code unit to call this web
service which is called azure ml
connector
uh the same way we can connect with
intel s connection
using this uri and the key when you
publish this your own web service
uh you specify inputs name output by
default it's input one output one you
can take it
actually from
uh from here so web service output it
has a name which is output one the same
storage for web service input
then you specify uh
your
input column names so
that
they should name in the same
way as
you have
here
as you have here so that's in the name
of the columns that uh are
your web service input
uh then i'm just
looping through here from the date to
get uh forecast for the next uh seven
days so i call this web service for the
each day actually it's there is actually
a batch process it's a little bit more
complicated just for demo purposes i
uh leave
this
call day by day
then you here specify the
values for your
columns
for the next seven days
and then you just call this sent to
azure ml
so
as an output you will get
actually you will get a json
response uh where you can
just take the orders uh the predictions
of the orders in a text format that's uh
it will come in a text format then i
just evaluate here to the decimal and
save it to my table and then run it
here
so
that's actually how this
works
so if we compare
time series um these three frameworks
in our case i
when i trained a model by myself i used
uh even more powerful
mathematical algorithm which is called
boost decision tree regulation which
just gave me better
forecast
and we use uh here eight features
instead of
six before so
you still can increase the model quality
uh maybe adding more features applying
different mathematical algorithms so uh
or maybe
changing parameters in these
mathematical algorithms so
yeah let's return a little bit here
so um
when
important thing uh that you need to like
take out from this that machine learning
uh
training process is very creative
process so you're just experimenting uh
giving more data maybe another data
adding
more columns to data deleting columns
from data applying more algorithms
testing with different algorithms and so
um that's yeah that's uh could be
time consuming but
but you can at least start with this
frameworks which will do
all the job for you and you can just
see what happens
okay
do you want to see something really cool
uh i have actually prepared two
uh cool features
so
uh custom vision
um let's uh do some custom vision demo
you see my phone
yeah
so actually here is a business central
on my uh
sandbox on my iphone i published here uh
one extension that i built for
this custom vision uh
demo so what we're going to do
we will try to
purchase this
apple
just with uh just making a photo of them
from business central
so let's try to do that
um
we'll go to the
purchase orders
so we'll create a new purchased order
come on
for example with some vendor
um and i just uh created a new action
here uh create new purchase line from
camera
how cool is that
so i just
will activate my camera
let's see if it will
what
will
work
so i take a picture i use this
picture it will actually
send this picture to my trained custom
vision
model
actually yeah that's the second demo
that i wanted to show you let's let's
see
let's let's do like this
so
first one
okay
another side of this apple
come on
it's about light i don't know
um let me
try here
yeah actually i trained my model to
understand if uh
uh if this apple is fresh or not
if it's spoiled i just
uh
i just uh
tell that this item this apple is
spoiled and use another
one
but it should work like that
okay let's uh let's do let's go to the
um
to the
custom vision here
so actually the custom vision
it's uh
let's i will update it
so a custom vision it's a tool
uh that allows
yeah see that
so uh that allows you to train your uh
images and to tag them
so
uh the actually the images that i took
before
uh
so actually the
they i just uh
i had fresh apples that i trained and i
had a spoiled apples that i
used to
train the spoiled ones
uh but yeah it
and then i trained this model and uh
got the predictions now it thinks that
i don't know why maybe that's because of
this
light
on the background it thinks that it's uh
spoiled but we can
actually what we can do right now let's
check
we can actually
check them
and will tell that they are fresh
okay that will
retrain that
i wasn't expected that i should retrain
the model here but
we have some time
come on
it should
be quick
anyway let's see
while it's training let's see how it
works
from business central point of view
and then we will try to run this demo
once again
so um
custom vision api
what i'm doing here
actually i'm
uh i'm creating a new line
i call a take picture
framework accessible in business central
that's my function abort if spoiled so
that's um
what i what's where a custom vision uh
magic happened
and then i save the line if we have
fresh apple so let's go
here
so um
so this is my separate code unit
so how to deal with a custom vision so
we trained model uh in
custom vision.ai service
and in business central we have
image analysis management and also we
have image analysis a result
then uh we also specify the ura ayura
and the key let's uh
let's see if that was trained okay that
was somehow uh trained
let's uh
okay
publish that
and we
can get here a prediction url
so i will just copy that
to
here
and then i have also a custom vision key
so it's here
i guess it
will be the same
yeah
and and then i just will republish that
uh to my cloud sandbox
let's see if
something
changed
so i retrained my model
i republished my uh
okay
that's that's because i published that
uh
let's take a purchase order
let's run this once again
magic happening
or not happening
yeah we have this item fresh apple
[Applause]
so
uh
let's uh we have still
12 minutes i've
prepared something
cool for you
also
um
yeah let's uh let me for let me
describe some story also about custom
vision i
i think two minutes will be enough for
that
so um i just found this uh story uh
before traveling to directions uh us uh
this year
so that's a real story about the us uh
army army how they used um
custom vision
some years ago
so the idea there was that they wanted
to train their model to recognize tanks
i was a little bit afraid uh
showing this demo in the us you know
when the russian guy shows tanks in u.s
it's maybe
uh some somehow well i i feel i felt
comfortable but yeah
um
yeah so they trained their model on such
kind of uh pictures
they get they got a prediction model and
they when they tested this model on on
these uh pictures they got uh 100
accuracy that they were very happy with
that
so actually they uh took it uh then in
production
but what happened in production
uh
they well took a photo of a tank
but well in production it
told them that it's not a tank
so
but
believe me or not
when they got this
picture it told that it was a tank
so
why
yeah
the sky
correct
that's because of the sky they trained
they actually uh well
custom vision don't know what's a strain
what is tank sorry
they actually they trained their model
to recognize sky
if there were sky or not
so actually they will recognize clouds
uh
that's what can happen with the custom
missions
actually you should
uh take this in account actually i think
that uh something
similar happened here in this demo when
uh
lights and maybe
background of this uh
table also
took into the account
also the last thing that i want to show
you that was actually the continuation
of the first step that you made a selfie
and send me
so
ai
now can
uh produce some art
did you know about that
actually i was uh
i i in saint petersburg in hermitage in
may we had an exhibition which was
called ai art really and
i
was very
inspired from that
and what so there were
programmers actually
who produced art with artificial
intelligence
that's actually something unbelievable
happening so
um
i decided why not to train why not to
try that
uh during our
session
so actually
let's um
i will run the
c sharp um
project here
what actually
will
what magic will happen here
so the photos that you
send
in email with a flow
they
i hope
they appeared
in
my azure container yeah we have these
photos that's your photos actually
um
i i had that some photos before i think
i can just delete them because i don't i
didn't know
how much of you will
send me uh the photos
so um
so this uh we will
we will call this uh api well
i used postman for that
um
and it will give me actually the url
of some output image i really don't know
which what will be the result because
it's
let's say i come on
so yeah it's executed uh successfully
let's go to
okay let's
so actually what's uh
what he did
here
depending on well he took all your
photos and generated
a face
of the well i see it's a man
don't know why it's asian man
uh but uh it consists here well if i
will
i don't see if i will zoom it but it
really consists of all of your photos of
all of your
uh selfies as a tiles usually we can
uh
we can run it once once again
it will
really generate i think
some another
picture from that
yeah
so
is this magic yeah cool
i could say that that was the hardest
demo for me
i really prepared a lot for that
[Applause]
some useful links
uh time series api and mail prediction
model api uh the galleries that are used
also some
links to all start
uh
oti
so now you know how to implement ai
start and have fun that's my
recommendation
and remember that ai is not a sex and
you are not a teenager so stop talking
about it just do it
so thanks thank you very much for coming
and we have
uh we have three t-shirts and uh
and five minutes four questions if you
have them
yeah
one more beer
um this um
training the artificial
closer okay can you hear me now okay
this training of the artificial
intelligence seems a bit awkward for me
so
why don't they
make the make the training and testing
process just one process so you just
upload one file and then turn a slider
how much you want to train or how much
you want to
test
so it would be a lot easier
uh ml framework uh let us show which was
the second framework do the training and
testing in one step
okay yeah so this quality model that you
receive after the ml uh
framework training process uh actually
on the bottom in this web service it
also splits your data for training and
testing and then uh
do these predictions of the past and uh
give you the quality and next next part
is that if you have to use this
remove duplicate lines
so it makes a bit difficult to use for
example example item ledger entries to
training so you have to first pull the
data and then compress it and then put
it back
so
no i i don't think so so uh duplicate
lines is actually an errors it's it's
not uh
um
it's not related to some business cases
it's uh it's something that
um
you have two answers on one question you
know yeah so uh
in in the past
yesterday we sold 100 units and the next
next line says that we hold 50 units but
that's not an error if it's in the item
lecture into it you just have to
calculate them together
you can well yeah i understand your
question so in item ledger entries uh we
don't have a grouping by date right so
we have entries and one date can have
hundreds of uh
entries it's normal situation because um
and that works
it works yeah
in this ml studio you can also apply
grouping if you want to get
information if you want to calculate by
dates yeah you don't need to do anything
special in business central in this case
okay i think i should have taken part in
your in your workshop
[Laughter]
up
you are together
okay so
so the question is uh if we have our
internal um
ml system uh apart from azure uh could
we theoretically hook up this uh code
units which you have shown us uh to this
system or is it like really tied to the
hrml
i would say that it will be simpler to
just call a normal http request or it
will be easier for you to deal with it
another system because
uh well in the bottom it's just a web
service uh with a
http
request and response this frameworks
they just know how to
uh deal with authentication to azure ml
uh web services and uh how to
uh deal with uh sending these uh schemas
uh to and from and also how to get how
to
uh store the outputs from that so it's
just a like a middle tier
that knows how to deal with the hrml web
services but uh
in
other situations when you have a
prediction um
web services
outside or whatever
it doesn't mean
where uh you can just call normal uh
http requested calls
maybe it will be just
even
less lines of code
okay thanks
my question is how is the quality
calculated actually based on which
credit areas the quote is calculated
using test data sets so
um it's
yeah once again so uh you for example
have uh
if you have a data set how it works in
the past so actually it tries to predict
this path so it's uh it takes your data
set every row uh he predicts and then it
compare how it works
so that's how you get the model quality
it's basically accuracy of the already
okay yeah but it can change for example
if you change the set of uh data to
check then you will get another quality
so it's not really about the model you
built right and the algorithm that's why
you need to have
the data set which uh could uh
have answers on uh different situations
how it was before because if something
happened in the future that
uh wasn't before
actually you will
he will doesn't know how to deal with
that
he will give you some estimations of
course but the q the difference could be
more than expected
okay and uh the next question is
there are a lot of this mathematical uh
algorithm that you are using and one of
the some of them are not applicable
completely in
some situations but with a specific data
set so how do you know is there any
documentation which algorithm to apply
in which yeah that's a good question if
you will um
if you will watch the recording from the
previous tech days uh there is in the
link actually this this will be also
recorded and will be in youtube so you
can just uh go to the
last year i had a slide there
uh
so which uh mathematical algorithm
should you pick up depending on your uh
problems okay or you can just google
search
it's called
if you will search for
uh azure ml algorithm cheat sheet
it's called like that
not but
uh you will get this picture as well
okay thanks
i already have t-shirts so that's
good for you
yeah i have two questions uh actually uh
does it work with uh on-premise uh
version uh this is the first one uh this
all
it was all yours all yourself here was
in my local docker ah okay okay well
except uh the last demo
with a
image recognition well it's just simpler
to connect to
uh cloud from phone
cool cool and the second one you showed
how we can train uh the model uh fit
with data and get this five kilobytes
file with base 64 format uh
but my question what if i want to keep
my model up today and update it say
every sunday
night you can uh you can do that uh
without a mail prediction framework you
can do that
setting maybe some job queue
and actually this is
i think this kind of gpu already exist
in business central just to retrain your
model
if you trained your custom model you you
should deal with that somehow manually
but
also retrain uh your model and uh
then republish that well actually this
uh something that i did during this demo
about custom vision models so i just
retrained it uh published uh once again
yeah i just want to automate this
process not to click everything possible
well in custom vision there is an api
for that
in your azure machine training process
i don't know maybe it's this
okay okay thanks
any other questions oh
okay
thank you very much for the down first
fold
uh quick question about so here yeah
so uh
all of the machine learning most of the
topics are on prediction
i was wondering is there any more
detailed information about
other aspects of machine learning and ai
in terms of recommendations decision
making path finding for instance
yeah
if you
did you attend uh
the walters and vehicle session before
yeah
they actually showed how to
uh train uh custom vision model uh
to give you some recommendations uh
for new items so if you uh just liked or
disliked some uh
cars
they had that in their demos
so when
the store had new
car
uh
depending on your previous likes or
dislikes they
sent you a notification so that's
actually
training of a recommendation system
uh
you can
for well for for other uh
services uh powered by machine learning
you can go to cognitive services
that's a good place where you can just
uh
start from
okay thank you very much
yeah spotify and netflix
yeah that's how they recommend
apple or well as well
no
okay
thank you
