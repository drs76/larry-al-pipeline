# NAV TechDays 2019 - Unlocking new integration potential for 365 BC with Azure Event Grid and ...

- **Source:** https://www.youtube.com/watch?v=EASOq9SpIwQ
- **Video ID:** EASOq9SpIwQ
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 92m50s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

afternoon how are you doing good lunch
I don't have a good lunch yeah
so welcome you to take this our session
today we will speak about integrations
about data synchronizations about tools
that we can apply in this process and
yeah so my name is Dmitry I am an MVP of
mostly return meaningless yeah so I'm an
MVP I have about 15 years in any we
experience I also focus now on some AI
stuff I also will have a session about
AI tomorrow so you're also welcome
spoiler so I live in st. Petersburg
which is in Russia not in Florida and I
have two kids and welcome Turanga hello
everyone I'm Chandrasekhar a member for
past four years for business central and
I have seven years of experience in nav
and to his experience in PC I live in
Auckland New Zealand like the edge of
the world but I'm actually from Sri
Lanka and I flew like thirty two hours
to get here so let's see well please
give him give his guy a good applause
let's he travelled ninety thousand
kilometres to share the knowledge with
you
so going to the session that this is our
agenda for today first we are going to
talk about reactive programming a little
bit about theory and then Dmitry is
going to talk about admin API which is
now new cool feature in business central
and and he's going to show a little bit
on that and cool demos then we talk
about the event grid and then we jump
into the hands-on after the hands-on we
will talk about design considerations
and
finally the takeaways so going back to
the this slide the most common
integration problem if I ask the
question from the people most of them
tell me that is the main issue is
keeping system in sync you can integrate
applications but keeping them in sync is
the most common problem in the past we
didn't have this problem much the reason
is most of the applications were huge
applications and all the functionalities
that needed for the business was built
within that app but now with the new way
of patterns and thinking people decided
ok we are not going to split the
application and put it in a separate
applications and then so then we can
give the better experience for the user
with coming to this approach now we run
into a problem with how we can
synchronize this applications together
so because in the organization you need
data flow across the entire organization
so people come up with different
technologies different terminal
technologies and different patterns
these are the two main patterns that
actually will people use one is polling
and push so what a what's polling
polling means that if I'm the main
application think that I'm the main
application is which is busy and then
I'm saying I have the data set if you
have any if you need that data set just
come to me and tell me what you need
then I will give you the data set to you
which is perfect so I'm the BC some
application comes to me and asked can I
get the customer information so I said
yes I can get the customer information
what are the customer numbers so he give
me the data I give it back perfectly
working fine the adoption is push what
in push is it says I heard the data said
please don't come to me you're annoying
me so much coming all the time to me and
asked in the data set I will come to
your doorstep I'll deliver the data set
to you this also has real nice path but
if you talk about the poly mo you will
get into more be solid issues that with
the poly one is consistency
think about scenario that there are two
applications running and the synchronous
and sync interval is thirty minutes that
means at any given point of time your
application will be thirty minutes out
of sync with the other application so in
order to minimize that what we can do is
we can minimize the time frame that how
much time that this application get
synchronized so we move it 30 minutes to
one minute now fine now the Capon is one
minute but the problem is every one
minute we get this knock as main
application do a how data and then I'll
in another minute do you have data so
it's keep on getting creating noise in
the main application and it's asking
keep saying the question sometimes it
says yes I have data most of the time
with tests no I don't have any data
please do not come to me but still keep
on asking the same basic questions so I
used to pretty high I don't have that
yes if you if you're familiar with Big
Bang Theory small at Sheldon coming to
Penny's doorstep and like not you need
all the time so it's it's really
annoying
this will definitely drain the resources
in the main application because rather
than its focusing on what it does best
like servicing to the customer now it
has to request 100 different calls
coming on every one minute just asking
dataset so it's draining resources what
are the changes with the push now that
main application take the responsibility
of pushing the data and keeping the
other system sink bingo scenario that
you have business central as a main
application which contain the data set
and you have far other systems which is
interested of this data set now business
central has to go on each and every five
systems and said this is the data set
this is the data set it has to be liver
everything it's like this is for you
yes is for you please take oh you are
not available
take you're not available take more than
that some application said no that's not
the format I won't I
I won't in a different format I don't
know what that means
so can you convert integrate that I can
understand so the business central the
most of the time developers has to
develop an extension that actually
convert the data set which understand by
the other system and also being a
developer of the BC now I have to put
five different hats to understand what's
the scheme of that other system so
what's this there requirement what's the
end point looked like and what's the how
I connect to that I have to understand
all of them so it's it's making very
complex so main application rather than
now catering for the business need its
catering for the integration needs yeah
but also its it's complex but also it
will take time because you need to go to
every application and send the data
instead of doing like a normal work
that's true so that's why we thought
like okay rather than can't we come up
with the new solution with new
technologies that max of better before
we jump into that why don't you talk
about like what are the real life see
notice that we have this problem in the
PC level yeah
for example assume that there is a whole
new company I personally worked like 10
years with one big customer who is in
marine business and they had three
headquarters around the world and yeah
and also I guess about 50 different
legal entities with different
localizations and they had one they had
had to have one master date or one
general account one list of customers
one list of vendors and so on
and one list of items and we had to
synchronize this data somehow this is a
really complex because you have many
databases different localizations and
what we have now with the business
central in the cloud well the business
could be the same right we have a
holding company and illegal entities
with different localizations but we can
the idea just to show you the idea is to
manage everything from the holding
company so you don't have to go like
different open different windows you
just do everything on the holding
company itself yeah I guess so and when
you want to manage all these
environments so as administrator's you
need to create in new environment
politicalization or and then you should
create the companies then you if we're
talking about business central yeah you
to have the same schema you will need to
publish also extensions to all these
environments so they have the same
extensions if you are talking about
business central cloud you need to
configure upgrade windows for all these
environments you need to manage backups
somehow well Microsoft managed back up
by but I mean that you can have your own
policy just to have a backup on your own
server and check the health of all
environments so it could be complicated
if you have these environments somehow
disconnected we have so called
administration API so administration API
allows you to provide you an API to
manage all administration tasks remotely
without to go into the client to
business central slash admin center and
the idea for the demo
I prepared why I thought okay we have a
holding company why shouldn't we manage
all the environments from this holding
company that could be a cool thing so I
created an extension for that I wish I
caught busy environments manager
let me show first how it could work so
I'm connecting to my holding company of
course here forward my possible so here
now I am using docker environment so
just also to show you that I can call
outside the world from docker that's
okay so and that's actually the list of
my environments I can update it if I
will go to the administration
api-related as well you will see the
same list but before we go to the
process let's focus on our configuration
so I have here a resource URL that's
actually the main URL for the API API
business central a dynamic sitcom I have
a tenant domain so that's actually my ad
domain account I have app ID what's app
ID I'll show you in some seconds and I
have username and password so to be able
to use admin API
the first thing you have to configure
connection and connection will actually
have a action for that which is called
test connection okay that works and to
test to get connection technically you
need to get a token for preparing this
demo that was the most complicated part
for me actually because we're isn't get
the token I'm getting it here because
there is actually a good documentation
about administration API on a Microsoft
website but to get the token Microsoft
provides you a dotnet library that
actually connects to the endpoint and
give you the token back but we are in
extension world no dot nap so actually
it took me I think two hours to drive
into the process actually left into the
github with the open source of these
dotnet libraries and just discovered the
URL that is called and the body that I
need so that's actually the answer so I
need this URL to call and the body to
construct so the grant type is actually
a password here it could be a secret key
it the coke could be in this case will
be a bit more complicated I use a
password identification for that so this
an AED identification using a login and
password then I pass the username the
password and the client ID and the
resource so where to get all these
things you should go to well
you can go to my blog as well where I
actually have a description about that
but you should go to your asier to ad
configuration and here you have app
registrations so you create a new
registration for your app let's go to
this app so when you will register your
app you will get an application ID so
that's the ID I use here the client ID
but also you need to configure them let
me check it I think it's in the
identification yeah so the type here
should be public and you should
configure also redirect URI also you
should give this app permissions to
access business central it could be read
access or write access in our case it
should be right accessible so this how
much 3 steps will give you all you need
to access the endpoint and to get out
invitation key so here I just use the
body also the content type will be
application and I just call this client
and receive a response read from Jason
and there I will see their token so I
have this token so this token has also
the period of valid period so it will be
I guess like a three maybe five minutes
so I call this I get this token every
time I call admin API to actually so
next okay will general with this
I have update action so let's see how it
works
could you need to get environments so
it's all very simple
I have a special API request admin a
version number two by the way Microsoft
upgraded admin API to version number two
at the beginning of November now we have
what more readable URL then applications
business central and environments with
this I will get my environments so
actually called web service save the
result and passing providing here also
the authentification token here and and
yeah I have this environments now I want
for example to create environments from
here so we can also do this
so I created action for that with a nice
wizard so I can for example create
production prod and Z which will be for
example a New Zealand our localization
that's the one yeah I can choose a type
production or sandbox okay once again
roads and the next finish
so now he sent me another pool to admin
API you see that it will be created with
the latest version which is 15 number
15.1 but yeah for this demo it's enough
but if you want you can also specify the
version in this wizard and send the
version to the URL as well so now we see
the status is preparing if I will update
my administration Center you will see
here that's the new entropy and it's
also preparing well maybe you you can
also as I told you you can configure
sandbox is cure maybe you want well you
played with the sandbox and you want to
delete it possible you click on the
remove well I created this workflow so
do you do you really want to delete this
environment I click yes are you sure
well to double check ok yes are you
drunk
oh well of course I am am I
yeah of course a that's how I prepare
for the sessions usually sorry yeah go
to sleep ok let's let's try once again
so remove yes sure yes drunk ok no not
as much okay let's so now it's removing
it's also will take some time if I will
go here and update you will see that
this one is also removing let's see in
the AL how it works so the simplest part
is removing things that's always very
simple together you know just destroy
that so for removing part you just need
URL
with this different URL request actually
so you provide the same URL as before
but with environment name so you want to
remove and then you add this
authorization with a get identification
talking so you get the token once oh
yeah and then you just call client
delete URL and get some response and you
are done when you want to create new
environment also not very complicated so
you specify here in the URL the name of
the environments you want to provide
rate then you create a body for that so
it will be adjacent simple JSON file
with environment country so it will be
localization version and environment
type so if I will go just here so it's a
simple you know adjacent construction
that build this and then you also
specify that our bodies in JSON format
and you use put not post but put methods
to call this API so yeah I think that
you can continue with right
so we talk about the yeah so I created
in environments it's possible also to
create companies it's possible also to
manage extensions there there is another
set of api's which is called automation
api's so they are a form for creation of
companies to create to manage extensions
even to publish configuration packages
and so on so many possibilities but yeah
now it creates its environment and tango
so I have no empty environment how how
should I sync data there so some master
data from my holding company for that we
can go into demo but before that I would
like to talk about couple of current so
now we create the or the environments
within the master company now what are
the challenges that we have when we
trying to synchronize the data now he
created the New Zealand one company
which is we use English and the master
company is also in New Zealand which is
English but now he can create an
environment for Russia different
language then he can create enough
different environment for different
country I cannot create inverter for
Russian so different language so then
the people in those countries will use a
different language so how are we going
to do that are we going to maintain
different languages in the master
company are we going to address that and
and any given point of time they are
like multiple companies interested on
the information stored in the master so
how are we going to synchronize all this
information into the sub companies at
once without affecting the performance
of the master company so that's another
challenge that we have and the down the
line the company owners come and said ok
we are expanding our business we install
a new entity now we want to synchronize
the entire data set with
new company so should we do the project
again like taking the requirement taking
the old recommends again to the
development deployment
are you ready testing and then after the
final confirmation deploy the production
are we going to use that pattern or is
there a more agile way that we can
address this and also sometimes they can
come and say okay at the first phase we
are going to integrate these entities
this couple of entities only and in the
second phase when everything is going
smooth and we are like confident about
the product and what integration then we
will talk about the other entities so we
build the integration deployed it works
fine no cause in the midnight asking
that this is not working so everything
is good
then they sign off saying that okay we
start the phase - now we need these
custom entities being synced with our
sub companies so do you how to spend the
entire amount of time again or is there
more agile way to address this so those
are the challenges that we face and
there are a couple of ways to handle in
busy without using any other outside
technologies one is push event into the
internal table and build an API within
business central and then ask the
subsystems to call this and take the
data from there and the other one is we
have the subscriber functionality in the
business center so the sub companies
they can create a subscription in the
master company so customer record
changed subscriber functionality will
call the all these subscribers and said
these records been changed in business
central do you want them and this is if
you want them these are the IDs for this
customers this is the URL so first
approach something happening even happen
in business central we push it to a
internal table and allow it to access
through API the second option is same
thing even happen in BC this time we are
not putting into internal table we are
calling subscribe
and said that something changed if you
won't come and get the data set and then
they will call the api's and Cody the
data set looks fine looks okay but we
face challenges when it in production
everything works fine annuity one is too
many API requests you have five
different companies frequently there
come back and ask in the information
from the master so too many requests
coming to that and we know that we have
like 60 or hundred API calls per minute
we can cater in BC an increase of the
security threat now we have to give our
API keys to all these sub companies if
we are not going through API management
in Azure so we are sharing our keys to
all the other subsystems which is going
to be a loophole in our security the
other thing is rapid growth of the
database this mainly applies for first
option which is storing the data in
internal table we can't create a batch
process we can create a batch process
actually to delete data but down the
line one system suddenly wakes up in the
middle of the night and said oh yes I
need this data set and it's in the
master company so I'll go back and
quarry that by that time our job has
been run data set been clear so again
problems and also the deadlock number of
API calls coming in now main system is
catering for those and people are forced
in journals it created more data and
deadlocks the people will campaign that
ok BC is low it's getting dead logs like
we can't post a simple transaction can
you do something about this so those are
the couple of challenges that we face
daily basis so many problems yes so
what's the better solution would be you
asking me yes I'm missing you ok I'm
with the problems ok you are in the
trouble so let's think what could be a
solution can you give us a real life
sample yeah
let's imagine that you are going to sell
a house let's imagine that you have a
house okay let's imagine that you want
to sell this house so what you are doing
is in this case you are going to broker
who was responsible be responsible to
find your potential customers and well
he you just described your house we have
a big house like you I hope so with a
good territory and usually describe this
house to the broker and broker will have
a list for example of potential
customers he will call all the customers
potential and provide the information
and ask ok you do want to buy this house
do you want to buy this how do you want
to buy this house on the other way this
broker also have for example some
website which is available for everyone
so even the potential customers who is
not in his list can go to this website
and see your house and maybe make a
decision to purchase right so and this
broker here is like a middle tier right
yes so why not we have some smart middle
tier here the less disturbing so broker
handle the old things and you get the
money people get the house yeah you're
good to go
yeah broker also will have some money
but yeah yeah small broker fee leave it
that we can live with that
so we have such service in Asia among
all the services which is called event
grid so event grid actually this is this
broker so it can as the input get the
messages
well okay I'm not messages well I bought
messages a bit later but he can get some
information about what happened in other
systems about some data and then he can
push this data to other systems which
you know about or other systems can
subscribe to even grid also to to get
information about okay what has what had
changed before so as there are many
connectors which can send which can send
information to event grid and event grid
has many connections about other
services so we know how to deal with the
different constructions of web calls for
different systems so why don't you use
this invalid to handle this we have a
custom connection I guess yeah there for
which we can call for the business
central and then use business central so
we can use a housing company as the
input and all the subsidiary companies
as their output and the good thing about
this is like it you can initiate this
with the simple HTTP request so you
don't have to do like very complex calls
just a simple it's so simple you can
post it data into the wind grid and also
the other thing is that you can have
like multiple subscribers so when you
send the information to even grid at the
same time it all subscribers get light
up if the filters are correct and they
are like interested on that even topic
so what is an email so event is well
what happened right so something happens
you have new and new customer record or
maybe you change something on customer
record or maybe you deleted customer
record this or something happened so and
you answer you should
sent these information so what happened
to the event agree there are some a
mandatory fields on the header
there are there are topics their subject
and event type so what are them so topic
and the subject are something that you
can manage by your by yourself it's it's
some kind of grouping the events so for
example a topic could be about could be
like a business central so something
happened in the business central and
subject could be that something happened
in customers yeah
on the other hand the topic could be
sales for example just like a part of
like a business theory and subject could
be like a customer or another subject
could be sales order so that's up to you
how you can manage that and event type
is actually what happened so which is if
records create deleted or modified and
then you have event time so when it
happened and you have ID of this event
so of this message and that he were sent
from business central in our case to
event grid then you have a body and the
body is you construct by yourself so
it's what you need you can construct by
yourself what happened what fields were
changed you not to pass all the customer
table for example just maybe you want to
track only some feels like address
country I don't know the name of the
customer or v80 number so so you
construct here the body and then you
just send it to even grid and yeah and
then just then and you do you forget
about that you don't care what happened
with that after that's the main idea I
think that's the main advantage of that
yes so it's it's a collective
combination of push and pull it's like
man let's do some optical optimal
compromises so these are like a couple
of sample scenarios with even grid where
that think that you in storage you have
the file being created so now you need
to a translate that so you can push that
even to the wind grid so even grid well
with the actual functions it picks up
the file and translate it using natural
cognitive services and the automation
sequel database in being created in
sequel and now you need to run some pre
validations in the using as your
functions so what it happens is it push
the data set into a even grid a sure
function triggers that and it runs out
all the database properties are set
correctly the other thing is like
virtual machine is being positioned so
all the tanks are being corrected all
the configurations are corrected you can
do all these things
be-because this soon as I put it in here
because they have the inbuilt connectors
so you don't have to reinvent the wheel
you can use those connectors and push
the data into even greater this is the
most important part for us as a BC we
don't have a connector we've in the
business central itself so we will have
to use a third party which is the custom
topics so we create as TTP requests we
push it to even grid and then after that
it's the imagination that you you can
use project caps you can use flow you
can use a any technology that connect
with even grid so yeah in our scenario
here like a holding company and other
legal entities so it's not like that
only like other legal entity but it's
another country so not languages so if
you just assume that you just if you
just sync data and the holding company
for example is not
in English then well you have data thing
but it will this information with this
data will be not understandable and it's
in both for your legal interests it will
make no sense
so using this middle tier you can also
provide some additional transformations
for example maybe about translation
possible yes it's possible
mmm we'll show them a demo so hands-on
what we're going to do is we have a we
are going to integrate couple of
entities with the multiple legal
entities and we are going to use
different entities different languages
and then I'm going to show you like how
much would be easy to add a new language
into this integration and also how much
it would be easy to add a new entity so
before that this is the like basic
structure of our demo what we have is in
this side this side we have the master
company master company will push the
data set into event grid then we have
this logic app which translate any data
set that comes in the filter of GL
account it uses the cognitive service
get the response and push it back to the
even grid then we had two logic apps
running in here which his filters for
English and the GL account so if the
language is if the message is translated
to English then it will subscribe to
that take it and push up to these sub
companies and this one different
language same entity and push it to the
related legal entities so that's the
main I derived demo okay come on can't
wait to see yes
so this our master company no you know
I'm still in this yes so this one must
accompany and if I go to my New Zealand
company and go to the chart of accounts
and this is my de different languages
I'll go to chart of account and this is
my version which is in different
language so I'll open the chart of
accounts for each company just to show
that we don't have any data and I'm not
expecting a data for are you because we
haven't configured the language for are
you yet so in my master company I go to
chart of account I will show the code
later before that I want to show them
show you how it's been done so I need to
publish this to our chart of accounts
who met us about cohere yeah sorry who
much is about code here we build an
extension to sync rest it's there so we
like to select the chart of accounts
this 12 and then we click here it says
do you want to synchronize scindia's we
need to sync transit it takes couple of
seconds it says yes if I go to this this
is not a as you even grid this is just a
Viva that means whatever happens in even
grid we can see that through this this
is webhook so if I open this so it's the
message as being translated now I got
the English language translated de so
that means logic app I showed you
previously this was recap picks up the
message translate through the cognitive
services and push it back so it's going
through and now if I go to New Zealand
and i refresh this I have the data set
there and if I go to this company I have
the language I have translated and if I
go to Russia
I don't have anything so the Russian was
not supported language now you want to
add that otherwise Dimitri will I will
be said yeah yes so to do that before I
do that I would like to show the setup
for this so everyone happy that that has
a synchronous properly so the photons we
pushed to all of them are here so the
setup we have three setups in this the
first thing that we have is API
endpoints
in here what we start is we had
different type of end points internally
it's like if you want to store the data
set internally other one is if you want
to push it to even grid as your function
or HTTP code it supports and then the
API endpoint we store in here and the
access case we must and stored in here
as well so this is the first setup that
you need to have you need to have the
endpoint for the even grid and the
second of setup is def exchange
definition which is an inbuilt
functionality but be little bit extended
it so point of using data exchange
definition is if I open this these are
the message has been pushed to even grid
so you can see it right now I'm only
pushing these four fields now if you in
the middle of the production now we want
to add a new field so how we do it do
you have to config what's your
preference do you like to have it been
configured or do you want to deploy a
new version of the extension after
modifying the code so we went with the
configuration model in here we define
this is the these are the fields that we
need to push to even bread or not
they've been great actually in this
point of the data exchange
it's about exporting the data set out in
a JSON format we said these are the
fields that we want to export it out and
then we said in here for the chart of
account table this is the mapping we
want so if I want to add a new field I
can simply add a new line and then map
it to the field in the actual table so
then the data set will be changed and
you'll have the new messages or real
without any coding without any coding
just configuration of yes well that's
cool and
then once we have that we need to have a
another one small set up now we have the
end point where we want to connect and
now we know what's the message that we
want like the data set we want now we
need to connect these two or have a
question yes when you add when you want
to add a new field for example and this
field is course created by an extension
yes it's available hindi so it means
that in this configuration mode you just
add a few from another extension yes so
once you have that we go to data
synchronization list
in here for the gel account we said okay
for the table 50 chart of accounts I
need to use as your even grid and this
is my endpoint this is my subject for
the message and for the topic
destination and the source and the
version of the message the version of
the message is simply because in the
load in the even grid you can consider
it that only this logic will apply for
the message type version is one point
zero if it's two point zero don't
applied it only applies with that so
that means you're guaranteeing that
whatever the application that works with
one point zero is not been will work
even if you create a new version of that
and in here you specifically say that
okay I won't use this data exchange
definition to export the data set from
business central and those are the only
set up that you need to add so with this
configuration of version of version and
actually you are avoiding breaking
changes for other sort of already
working applications yes yeah that's
cool so if you can remember that we
didn't get the Aria version the
languages now how much would it be easy
to add our route to here for that I need
to go to my report room so if you
haven't used a portal before you can
simply create it free which is I think
give one month rate for $200 which is
more than enough for it to play around
so I have a resource group for tech
ds-2019 and I have a bunch of resources
in here so first I will show that how if
before I go into the adding a Russian
language I would like to show that even
with how much would it be easy to create
even grid go to search I even grid and
I'm taking you in the topic and I click
Add
it has the name and/or location that's
it and it will create type after couple
of seconds it create the even grid topic
and once it's created it will look like
this that's it this is the endpoint
topic that I was talking about
previously on the setup and in the
access keys it generated access keys so
you can store it in a business central
or you can use a show keyword for that
so it's that's the only setup that you
need to do in to create the even grid so
you need to create even grease by topics
right yes but still you can use a one
even grid and you can in the subject
level you can send the different
subjects yeah that's what normally we do
we don't create like even different even
bits for different customers we use at
one and then use a subject to group the
messages
that's much easy for us do you know how
they build its bit
they build it's quite cheap for the one
minute first 1 million transactions so
first 500 thousand transactions if I'm
not mistaken is free after that every 1
million transaction is 0.6 dollars
points to the door yes so so it's you
just await one coffee and you're good to
go with the you Ingrid do you know where
is the coffee 40.6 yes yes so but but I
mean that it doesn't matter how much of
this of this and where event Greece do
you have so they're built by the message
messages yeah so okay so that's why you
can group them in depending on maybe
your business cases so it it could be
like a business arrears or maybe system
so well you can have only one and we
agreed let's manage ok so if I go to
this this is the logic gap that we want
to modify which is do the translation we
already have logic app credit to push
the message to the Russian version but
but we don't
message that getting translated into the
language we want so we go to the test
this is the Translate message for the GL
account which is a logic app so I go to
this edit and I have a bunch of
variables defined in here and then
before I go to that I want to show this
I have this array which says that these
are the languages I want to add now I
want to add Russia but I don't know
what's the language code that cognitive
service used to represent the Russian
language
so I go to postman I have the API called
for this I said yes get me the languages
so it brings back all the languages I
need so it says are you so I need to add
are you for my logic cap now I know the
language code so I had that oh thank you
you're placed it's on the beginning yes
much easy because then it translate the
first one so I would show the first
respective no other reference that's it
I can still show that it doesn't have
any chart of account in this version so
I go back to my master company now I say
oh mahadji cap after adding the Ru and
go to chart of accounts i select first
12 which is i published previously and I
said synchronize selected records and
yep
if I go to this now I'll see that is the
first message it's been pushed
Mussa just coming through and if i go to
trash inversion and press f5 i have it
translated it's a translation correct
give me three well not completely a
one yeah Marie I would kind of
live with that so for that if it's not
giving the exact same thing you want you
can train the model yeah call great
service yeah this is like down from the
I'm joking no translation by the way
yeah not a yeah okay so we have
that now it took me like a couple of
seconds to add a new language you can do
this in any language that support I
think it's like many languages is goes
through see all these languages supports
cognitive service so that means any
place that you open a new company it
will be supported with the community
service so that's done now I want to do
is what I want to do is I want to add a
new entity in here we have entity
synchronization built for customer but
we don't have anything for the vendors
now the customer comment says we need to
vent the synchronous as well so how are
we going to do that for that what I have
to do is I have to go to logic gap and
check the customer because those
entities are like quite similar datasets
and I said I need to clone it so I
cloned this
give a name wait for couple of seconds
so it can validate the name and I said
yes I need to create this one it takes
like a couple of five to ten seconds to
create the logic gap that we have to
wait so this is to create the logic gap
for translations which translate these
things so we have already been grid
yes we have already given grid and now
we want to translate the messages coming
to the logic even grid into a different
entity type which is for the vendor we
have the logic app that translate the
message that coming for the customer
type uh-huh but now we want to add
vendor entity okay so which means that
well in our case we want to translate
yes but first first step is translate
then push it back to in grid then we
have another logic app looking at the
entity and then grab that and push it to
the environment and if we well if we
don't want to translate generation there
just to put it to the even grid and then
it will take message from there okay so
even for the new new entity okay so it's
been created so I go to that resource I
click I edit add and go to code all I do
is find customer
when they're but I need to make sure
that it's the camp's replace all
I think I did everything correctly yep
don't worry what happens in and after
days will stay on YouTube so I save this
and I much design I'd takes couple of
seconds
yeah now it's pointing to the vendor and
now the translation part is fine now I
want to push this to the Russian
language so I taken the logic app which
push this message to the re version and
then I cloned this logic app as well for
defenders
this will be not this much easy in your
real life because the data set will be
different for the demo purpose we are
using Li exactly similar data set that's
why I'm not manipulating with the logic
helps keep the body but in the real life
scenario that exactly laughs in order
you will have trace spend a little bit
more time to construct your body of the
message so yeah but still it's less time
then you just need to create some a.l
code to deal with all the systems right
so in this project episode I'm going to
find and replay and so to replace so I'm
going to do the customer
yep I replaced all I got a designer it
takes a couple of seconds and I said so
so it's all good
and if I go to my companies and we said
purchasing vendors this is my new saloon
company this is my de and this is my are
not these companies have data for the
vendors right now if you notice that we
only create this for the Russian
language so if I go to the my master my
browser is
and I said okay I need this too and it
has been pushed
so complete the translate in transit en
so
yep there you go so the message has been
transformed
translate it and push it to the Russian
version so I already was cloned that and
change it a couple of places that's it
so but in the real life as I mentioned
early it'll be little bit different but
you can work with that thank you I'll go
back to the code so we built this
extension we have two extensions in the
rebuild what needs to export extract the
data set and push it to the even grid
other one is to map what are the
entities that we need to extract the
data out so this the even would handle
the one of the main code unit it's as I
mentioned early it's a very simple HTTP
request so we have a function that which
create the message or the body of the
message that accept the by the even grid
so we use this function to construct the
message we pass the variables and then
it construct and post the message so we
have the content type and the we take
the access key endpoint URL and simply
do a post before that's all we need to
do to connect to connect business
central to Azure even great but now the
thing is this is this option that I
showed you is really good if you want to
push the data once but how it would be
work if you want to do it very
constantly like you said change
something on the master company now we
want to automate that you want to push
it to the even grid without user
clicking a button for that what we did
was we extend the workflows and with the
workflows what we did was a that idea
actually I need to mention that it was
idea from lot one of my colleagues who
was sitting on the front row
he came up with the idea that why don't
we extend the workflows and we connect
we're close with the even braids so by
doing that we get more configurable way
of doing things like if a customer
record changed export the data set using
their exchange definition and then push
it to even grid same way any entity that
support by Britain Microsoft we can have
different filters like do not post put
it to the even grid if this field is
changed only for this set of fields then
we have more control over that so we
came up with divert loss yeah so did you
understand correctly that okay we we
have for example customer record yep and
something was changed we need to know
about that that this was changed and
then when we know when we know that this
was changed we should send the message
to even greet right yes so okay so how
we can know that something was changed
as I understand that we have well one
one example we can use like events for
example on modify on info on on delete
and create an extension that will
subscribe to this event and then sent a
message that's the one case but in this
case we need to call it to code right so
to add code for each record for each
table for each event type and use
markers that you proposed to use
workflows that exist in a busy central
already yeah yes okay that was the plan
so if I call quickly go back
we have workflow here for customer names
change I only use for that if there's
customer record is changed the name is
changed then export the data exchange
definition and push it to the even grid
so this is the configuration that we
have in the workflow and I forgot the
customer and if I change anything it
will push the data set into even grid so
I'll take one of the customers from the
New Zealand company so this data set and
in the master company I just add one
just to track the changes so it's now
changed to one and after a couple of
seconds it should be in here
I'm just wondering if David's changed
one I'm just wondering if for example
will you synchronize data from the this
change was synchronized with a legal
entity with a seizure accompany right
yes and if somebody for example changed
this record in a subsidiary company and
then if this record was changed after in
a coding company and even greed will
also update yes this even right now the
process is we all right there any
changes that happen in the sub company
so right now the rule is the master data
is handled in the main company okay
so it will like replace the change made
in subsidiary with the change made in
the holding company yes okay and there
are an example if for example somebody
deleted this record what will happen in
a subsidiary company it will create that
automatic it will create it created yes
oh that's crazy
if it's not there it will create it if
it's there it will update it it really
works it works I just want it to be a
bad boss man just don't leave me the
chance so what we in here what we do is
a we will be putting this code in the
jet hub and if I go to this I have the
two repositories already being published
and we have two data sync and event
handler so you can look into this and if
you have any good ideas you can more
than welcome to a create a pull request
and what we do is in here we take the
data set out through the data exchange
definition and create a simple JSON file
and in the web flow response week adding
a new event which I used to like when
even and the response like when the
customer record is changed quick export
the data set and create a data
integration event entry so that's the
workflows
and we have coordinate which is for the
Jason in here we use the JSON objects
that in the business center so we add
the fields we want and then pass the
create a buffer table put all the fields
into the data set into that and use this
it will return us the JSON file which is
adjacent array so we put it into the
even include in the even with message
and publish it to the in grid which
works fine what are the other demos can
I kind of wish for my yes are you guys
interesting to have also this demo that
I showed you before about this be seen
where environments manager to have to
use this I have edition when my github
it's just a private repository now you
want to show github because I showed my
one oh yeah of course I will just make
it public the name of that small them
about a github
okay now you also have this report to
Republic you can use it so shall I take
it and we go back to the slides and if
you have enough time we'll come back to
the code again okay I guess it's the
next right yes
oh no that's your part yes that's my
part yeah this is some question that
Demetrius while I was preparing for the
demos how are we going to handle custom
fields now we have the integer we have
specifically said that these are the
fields now customer is changing face
quite frequently and how are we going to
handle it the one way of doing is a this
is something also idea from my colleague
we have we created an API which takes a
JSON message and with that we takes the
message type and also the entity type
then we have the oops sorry I'll go back
yes we take that and based on the
message version and message type we take
which are the data exchange definition
that we want to use so message type
comes at 2.0 and the customer then we
know that which workflow we need to
trigger it so then workflow triggers and
it says okay the message is 2.0 that
means it has three fields in the version
1.0 it only has two fields so it knows
the how to read the jason it takes it it
data set and then within the detection
definition you can have the process code
it processing coordinate so it runs the
process data process code unit which
will extract and push it to the actual
table so this is another way of handling
the custom fields other adoption would
be to modify the logic gap and modify
the data exchange definition by yourself
like every time customer do some changes
if for example the custom field or you
declare that you want to sync some
custom field but this custom filters not
exists in other environment what will
happen so then what you can do is you
can created a different data exchange
definitions on the sub company and say
that okay this is optional so if the
value is there then it will trigger the
validation triggers otherwise it says
okay I don't get this field so I'm just
ignore it and move on you have the
answer forever my question so about the
design considerations follow the event
core concepts which is like do not have
events like when you look in at the one
event you need to be able to understand
what that event is about if you are if
you can't understand okay this is a
customer update and it contains all the
information I have and then if you have
to look another event to complete
another message to understand then you
are moving out of the logic of even grid
even grid is about taking a message
which is individual and do not have in
relationship with any other messages the
other thing is you need to define event
triggers like since we have hundred
thousand executions free it doesn't mean
that you have to push all the messages
into Ingrid you need to understand what
are the scenarios that I actually need
this data set to be outside and also how
much data is enough like that's a one
very most common question most of the
time what we used to do is we expose
like 50 different fields thinking that
okay this might this might be needed in
a future so we'll expose that and then
the data set get bigger and bigger so we
need to understand that what's the data
set that actually need for the customer
and since now we have a way of
configuring it manually by the user so
we don't have to exposed all the fields
that in the table and also there's a
limit in the vein read the message
should be in 64 kilobyte in the preview
it was 1 1 MB but in the when
it's come to generally available it
became 64kb so your message need to be
in the 64 kilobytes for some reason for
some reason if you can't fit your
message to 64 kb so country use even
grid no you still can
for that we have a pattern called claim
check
which means you push the message to a
you can do different ways
if the preferred way for me is we push
the message into actual function actual
function takes that message store in a
blob storage and then pass like a
signature message which is like basic
structures in that for this tenant this
ID for these customers being changed and
this is a token if you want you can go
to this place and take the message so
roger cave will take take that token go
to the azure blob storage and take the
message from there so we are not passing
the huge message to deliver it we are
storing in somewhere and then when it's
needed it's being handed over to the
logical this is this pattern only been
needed if you have like a massive data
set which exceeds 64 KB 64 kilobytes is
quite enough I guess for Jason Jason
yeah it's more than enough
so they take wage so yeah that was
amazing actually I could take this one
take away that that's this way when
greets its Wow nice that's one take away
so but in reality well you can use that
in your real business scenarios and if
you have the need to sync data between
different systems or now test was to
three more different business and roles
but in the in your case it could be a
business central and
be some other software for items maybe
are some software for dealing with the
customers on what whatever so if you
have if you want to think data or I
guess it's the wonderful solution which
gives you this middle tier yeah yeah so
let's keep your business central working
keep you other systems working as well
yeah you want to show some more code or
we we can go to Q&A yeah I can go back
to the code well we have at least two to
million chance to two minutes to show
some code and then Q&A I'll open up my
other we don't see your green yes let me
reopen that ok you have some secrets
there
yes
for the data sync my other extension
what I have is for each and every entity
I have a code unit which actually go
through the its take the set ups and
called the my other function which is
the which is in the other extension
which is create integration event entry
and it passed the entity and these
parameters so this is the code unit and
if you want to add like a new entity
what you need to do is you can cook you
can copy paste this one and change the
record like table IDs and then you are
good to go with that so it's these code
is like what per entity I'm I'm happy to
keep it is per entity so copy paste it
and give a new name for the vendors and
then you are good to go and if you have
any questions you can always send it to
it to me and or email me and then I will
be able to help you need any information
should we use even good to send you a
message
mmm your mails I can play the subscribe
for that just not to bother you on using
your time difference how much by the way
it's 12 hours it's exactly well of us
now it's 3:00 in the morning New Zealand
okay so yeah why not she was sleeping
yeah so we have you want to continue on
this one okay we have like 10 minutes
for Q&A
there were sound short a t-shirt is to
say should we give them for the first
three yes or to the last three otherwise
no one will ask questions they will wait
for the last but can they will stay ok
this is the microphone
it will it was cool push push push okay
he was actually pulling from the middle
hills okay how do you check in the
target company if it should get data or
so to use of job queue or it's waiting
somehow the right now we do not have
that set up like we configured it in way
that it always push but you can create a
set up in the middle saying that okay
you can deactivate and activate it but
you also interesting character that when
you when event grid push the messages to
the subsidiary company in our case
technically we use API yes so URL and so
this is some published API it could be
maybe custom API or it could be
basically I so in this case if this is a
custom API you can actually control
what's going on them right and also what
I can what we can do is in the message
that we push I think I still have
messages in this messages like one of
the topics we can specify that what are
the tenants that you need to synchronize
so you pass that message into the even
grid and then logic app then logic app
knows what are the tenants actually need
to be seen to it so you can extend add a
new field saying that these are the
tenants that need to be synchronous from
there from there onwards you can use
that the adoption you can use is a API
management from the API management you
can specify what are the URLs that you
need to call so from that you can
control that as well even know also that
it should send to business central using
core of even grid so no code on the
target company's target business central
databases yeah because it's published
API so it could be it sends the
information to the published API so it
could be it could be like a standard API
or you
you want to synchronize data I guess if
I'm wrong and then if you want to
synchronize some custom tables you need
to publish this on the subsidiary
company also as a custom API and then
you can call this API so now I'm proven
right so any other questions
oh yeah like hi this will be a
two-parter because I want to elaborate
on the question you just had and does
the do these messages work only a
real-time I mean do the only push and
that's it and the message is gone and my
scenario would be you assume that all
your subsidiaries are listening and are
online but we have a scenario where one
goes offline for let's say an hour all
right and the message was pushed and I
is it gone or I know it will retry up to
24 hours so if the your endpoint is down
even if it will try to send the message
till 24 hours and after 24 hours it will
push it to Delta Tech you just like the
service Busters okay so the message will
will stay somewhere up there so I can
come up and read it again if I missed
something
no it will it's not because it's not
going to stop the even bit is you can't
come to Ingrid and say that can I have
the message it's like even grid will try
it so till 24 hours if the first atom if
your system is down it will wait for
like five minutes you can configure the
how much the intervals are it will wait
for that and it will go back to the
system and said okay I opt if it's up it
will hand over so this will go till 24
hours after that even 24 hours it's not
there it will push it to tetra Tech you
so you can then manually say that push
this to the this endpoint okay the
second part is the data exchange part
where you can
more fields let's say - gln Tresor
customer and you add a new field in the
master data and you have 100
subsidiaries so how you synchronize the
data exchange part in these subsidiaries
sorry I can well data exchange you have
a field mapping yeah the customer has
five fields name address and so on yes
okay you add a new field in the master
data that you want to synchronize
through subsidiaries yes do subsidiaries
also use the data exchange channel part
so they can map their fields in the
subsidiaries that's why I showed it to
options B option one is I go back to my
slide quickly well you had to two
questions but I think it's fair enough
to give you on the one shot so this is
the second option like if the subsidies
have different options like if they want
to map a field in two different yeah
they get the message and message says
that customer name but you want to map
it for different entity different field
then you can go with this approach which
will go through the directions
definition to import the data set into
your company but for the demo purpose
what we did was we create the custom
api's so we explore the data set and we
push it to custom API so it's like a
one-to-one mapping in the field level
but if you want to have more flexible
option then it's the better option would
be to pass it to the data exchange
definition and then from there you can
have to take it so for that every
company should have their own directions
definition in there and if they master
data changes in master data exchange
definition changes all the hundreds on
so on subsidiaries need to manually know
you can create at it you can creation
for that as well so any changes happen
in the master company you can update all
the directions definitions in the
subsidiary companies it's just a
configuration you can also sync
configurations right so now while and
you use data exchange for that also
[Laughter]
anyway I will try it sorry one more one
here uh here okay if you're using
talk today with Larson 2017 the district
solar Allah the go-between translation
and subscribing of the mr. it so ya know
can you use this one with nerve agent
and something and what is the benefit
that is not available in in the best
options I guess I guess you can use this
with the 2017 because it's just calling
a HTTP request but for the best talk or
you can if I'm not mistaken you can but
I can I need to be come back to you on
that because I'm I haven't used to be
stopped much so I will come back to you
will talk to after session and I can
come back to definitely on that I think
he deserved it sure yeah
you have the question that we can answer
okay I have a question too but without
sure okay event greet what possibilities
for locking do you have there
because if I was part of the master
company I would like to know exact state
of each sub company are there any API
for getting responses back for the
handshaking of data that has if it has
reached the end in finally or I mean you
want to know if the data was
synchronized or not yeah excellent from
the metal yeah that would be typically
that is what I see at customers where I
do master data synchronization you can
you can trigger a email or notification
from the even grid but from the business
center and then call the master company
through that but right now what we are
trying to avoid is that like getting the
handshake like okay did you receive the
data set that's the point of actually
implementing the even grid so if you try
to wait for the message
then the whole point of unit will be
gone so for that what I can suggest is
what you can do is you can create
another subscriber switches in the even
grid which will give you the response
that where the message is still being
delivered or not other a new push back
to the master company
are there any login available in areas
where you have the login yeah you do
have the login but for in order to do
that you have to login to the edge or
even grid but you can create a dashboard
and you can pull the data set out from
there as long as the subtable you might
create in the master the company to
collect all these information yeah then
it's okay yeah yeah that's option do so
that's all right right that's good yeah
any other questions so that's that and I
another question yeah do have time 6
seconds try in this you translate
autofill I think in the end a message
using the translation to layer on Asia
yes easy to man can we imagine 12 just a
selection of we can select which field
is going to be translated yes I I didn't
actually translate all the fields I only
translate the name I can quickly show
you the logic gap for that
I guess that was the last question
let me so in fact you're so in here that
what I do is I take the data and create
an array so I specifically say that okay
I need to translate the name and some
other fields so I take that and create
an array because in the cognitive
service you can only translate one value
you can you can pass you can't pass
adjacent message so you have to be
elected value you need to pass so what I
do is with the pipeline I construct that
one line and then pass it to Coventry
service get a one response and then
split into multiple based on the
pipelines so you you make the setup into
the logic at yes yes because in the what
we want to do is we want to give the
responsibility for the person who is
doing the integration right now if we
because the translation happen in the
logic gap so he should make the decision
on whether this message should be
translated or not yeah but if you so if
you had a new field to be a to be
synchronized you have to make the set at
the Constituent can make a set up in
that yes into the VC by that you you
need someone else you need someone else
to change if you want translate into
different language then you need someone
as to modify the budget gap there okay
okay thank you very much for coming
Thank You Thomas
[Applause]
