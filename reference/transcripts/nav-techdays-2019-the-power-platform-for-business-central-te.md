# NAV TechDays 2019 - The Power Platform for Business Central Techies

- **Source:** https://www.youtube.com/watch?v=cp848e9WBFs
- **Video ID:** cp848e9WBFs
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 104m15s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Good afternoon. Thank you so much. Um,
it appears I'm um between you and the
weekend. Well, there is a uh a closing
session, but uh okay, that's not about
any technology anymore. So, uh very
short introduction for those who do not
know me. Um I'm a freelance technical
consultant and trainer. uh but means
that in a daily basis I do a lot of
development myself and I try to teach
others how to do so um by helping others
uh coaching uh delivering workshops um
but I do develop it myself and I think I
haven't developed in seaside for two
years now I'm not doing any seaside
development anymore well not totally
true for one customer I have seaside but
that is a customer who's on the way out
so I only need to create some XML ports.
Anyway, um uh I'm also an MVP for a
couple of years, which means that if I
do not work for partners or customers,
uh I spent my spare time on the product,
finding things out and trying to share
that with you. Um working in the channel
since 2002. And in the Netherlands, we
have what we call the Dutch dynamics
community, which I started about 10 year
10 years ago. Um and well that is a
community actually we have these kind of
sessions a little bit smaller about 200
people uh every time but that's four
times a year not one time a year so in
total we have 800 um if you want to
reach out or read my blog or want to
reach out with a question uh look at you
can you can find my my email here so I
want to start with a survey and of
course there is something behind this
because Um the results of this survey
will go into business central. So I
would uh like you to fill in this form
and um I will at the same time I will
give you a moment to get this one. You
can scan it. You can type in uh the
link. It will bring you to a Microsoft
form with just one single question. And
then uh I will switch to business
central to see what is coming in if it
works. It worked uh last night. So uh
let's hope it still works.
So let me
switch to Business Central here.
Yep.
This looks so nice.
Can I have Business Central, please?
There we go.
I know it's not the fastest thing in the
world, but here we go.
I do have some responses from you.
Nobody has no experience. Is that true?
The Wi-Fi can't take the response. But
anyway, uh you see responses coming in
40 44 43. Okay,
we have an expert in the room. Whoa,
two experts actually. Please come on
stage m maybe maybe I can learn
something from you.
Are there any Microsoft people? I should
have asked that as well.
So
what you see happening here is that you
filled out a survey, a form with
Microsoft forms and in the background I
have a um uh a Microsoft uh no not a
Microsoft flow I have a flow running
with power automate the new name that uh
sends all this data your responses back
into business central and of course I
will later on during this session uh
show you what else in the background.
So, um, great, this works. Thank you for
proving that my demo is really working.
Um,
I have not so many slides. I have about
nine demos in total. And if I talk for
every demo for 10 minutes, we're already
running out of time. So, let's hope that
works out.
um the power platform where are we going
to talk about in this session? I know
there was uh there were other sessions
uh uh today yesterday about uh uh also
flow or uh power apps whatever. So um my
idea is that I do not go uh not not
repeat what has been told in the other
sessions. Um I am not going over the
basics. I want to go into the technical
details of working with Power Apps and
Automate. Of course, um I need to start
somewhere. So maybe there will be a
little bit overlap in the beginning, but
trust me, uh I will go into the uh well
the the dark rooms of Power Automate and
Power Apps and tell you what works and
what doesn't work. So what we will do is
uh we will talk about uh Power Apps,
we'll talk about Power Automate and
we'll talk about the data connectors.
That's our focus. That's our topics for
this session. Um, we're not talking
about PowerBI, not talking about the
virtual agents and AI builder. That's
not my cup of tea actually. And common
data service. Um, we have seen Microsoft
is working on better integration with
that. So, I leave it to them for now.
Power Apps. What's the promise of Power
Apps? Create powerful apps. Well, that's
true. without writing a single line of
code and in a certain way that is true.
You do not code behind or write code
behind power apps.
Um I can tell you I just told about that
Dutch Dynamics community uh event that
we have in the Netherlands where we had
a session for functional consultants
talking about power apps and flow.
It was for functional consultants
because there was no code involved and
they complained
because it was too much of clicking,
too much of formula writing. And I can
tell you, you really uh uh need to write
some logical stuff. you type formulas
and uh maybe you could compare it a
little bit to writing um formulas or uh
writing macros in in in Excel. Um they
say it's like an Excel uh way of working
and yes it has a little bit of the UI of
Excel in the top where you have a
formula bar where you can select a
property and then write in something but
that's pretty much uh for the Excel uh
likeness. It is um really really about
logic and um writing those formulas is
something you need to learn and uh if
there is any user any end user who's
capable of writing uh uh apps and and
and uh putting together flows probably
he just had the wrong job. probably he
would also be a good developer because
it need you need to have uh uh that
background to know what you're doing. So
um with apps um power apps we create
apps that enables you or enables the end
user to read data write data take
actions. It is an an app that is focused
at a certain task. Now there's one thing
that I already want to say here. Um, if
you create apps, don't try to put too
many functionality into an app. You
rather uh uh create multiple apps
focusing on a specific task instead of
creating one big app where the user in
the start screen has to uh select what
function he wants to do. That is uh
overly complicating and that's not
needed. Now to get to that data, read
data, write data, you have connectors
and over 200 standard connectors are
available uh in um in Power Apps and uh
Power Automate. They share those
connectors and uh you can also create
custom connectors. Something I know at
least some people in this room are
waiting for to see that live. Um so the
connectors they um they connect to data.
I will come back to connectors later
what exactly that is or exactly but at
least what it is. So there is also a
business central connector connecting
data for business central
um and I will show you how that works.
So um what is a connector?
A connector enables the communication
between Power Apps, Power Automate and a
public available set of APIs. So if um a
data source does not have any APIs, it
would be quite hard to uh get the data
out of it into Power Apps or Power
Automate. So uh we're talking about APIs
and most of those data sources that uh
do have already uh connectors in
Business Central, you don't even have to
think about the their APIs. They're just
there and the the connector hides the
complexity of the APIs for you. Um
a connector in fact uh uh offers you a
set of operations in the form of actions
and triggers. And the action could be
simply uh something like uh read a
record. For example, we talk about
SharePoint uh read a file or uh an
action that creates a folder or a
connector for uh Outlook say create send
a new email or create a new task. uh all
these kind of actions are available for
you to call directly from power apps or
from power automate. Triggers are also
part of uh connectors and triggers work
the other way around. Triggers is
something that happens outside the
platform and they call the power
platform that something happened.
Triggers are specifically for power
automate. So uh power automate can
automatically start because of something
happened in the outside world. You don't
start a power app automatically because
something happened right a power app is
something that is user uh uh focused
user interface uh giving to the user. It
does not start automatically like hey uh
I'm a power app please uh type something
in.
A connector is describing
the actions and the uh triggers, the
available actions and triggers. A
connection
is based on a connector and is the real
connection to the data source. You can
have multiple connections
based on one connector.
The best way I can describe that to you
as uh the business central developers is
think of a table definition in business
central with fields with functions.
It does not represent the record. It
represents the table with the possible
fields and actions and and uh and
functions. But the real record does
contain the data. Well, it's not 100% uh
uh uh valid maybe, but that is quite a
similar thing with connectors and
connections. You can have the connector
with the operations and the connection
itself stores username, passwords or
whatever credentials you need to to get
to that uh data source and then on that
data source you can operate the actions
from uh uh the connector.
You might have seen this uh before. How
many people did attend the uh the
session uh before about power uh apps?
Okay. And how many did attend by way the
session of vehicle while about API
stuff?
Most of you. Good. Good.
Let me say this. Uh I will probably have
here some overlap with the session from
uh uh Alexander Tovich.
That's that's fine because I probably
tell something different at least uh and
about APIs that's great because I'm not
going to uh explain in detail how APIs
work. If you want to see that you
haven't seen the session then watch the
session on YouTube and you have all the
information you need. Um so Business
Central does have um uh a connector out
of the box available and uh in fact
there are two connectors. There's one
for PowerBI which I will not touch and
there's one for Power Apps and Flow
because they share connectors. If you
create for example a custom connector
with uh Power Apps then also that custom
connector is available in the flow
environment.
Um the
connector from Business Central that is
available is based on the APIs.
Well, not 100%.
It contains more than only the APIs. In
fact, it contains the APIs plus a list
of web services. And with web services,
I mean the pagebased web services that
are available in uh in business central
and it is a wide list of those web
services meaning it is a subset. You
cannot extend it. It is just a subset
that they take they will offer uh with
the connector that set of uh of web
services. Uh and I will of course show
you uh which one that uh that is and and
which are not. Um it supports um
business functions.
Um of course I took this slide from
Microsoft so I have to explain what with
business functions we mean here. that is
business functions like a record was
created, a record was uh uh modified,
record was deleted. Uh these kind of
stuff I don't consider that to be a real
business function. I mean creating a
record doesn't tell me anything. If you
keep in mind that creating a record in
business central just means when a user
enters a record that he just entered the
primary key and then on the page needs
to fill out all the fields and then the
fields if you save them it is a modify
on the record which could happen
multiple times when the user uh is
entering uh data in the page because you
may have uh uh set some cur page.update
uh lines uh here and there. So when the
user enters a record, he actually does
an insert, he does a modify, maybe
multiple modifies and then he leaves the
screen. So tell me what is the the
business function of that? When what
which moment do I have a new record?
When the record is created, when it was
modified first time, second time, when
it leaves the screen, is it finished?
Then that is not a business function. A
business function for me is when a sales
order is released or posted or when um
uh a customer uh is unblocked so I can
use it. That is a business function and
these business business functions are
not available with the standard
connector. The only business function
that you will find are triggers like
when an approval is requested for
customer sales uh uh quote purchase
invoice etc.
Um out of the box we get 12 flow
templates. I'll come to that uh later in
one of the next slides. And um we have
also the possibility that uh power apps
can create automatically create um an
app.
Okay, that's nice. We're going to do
that of course. Um so let's just dive
into Power Apps and let him create a um
uh an app out of the box based on the
custom uh based on the business central
connector.
What I need to tell you up front is that
not everything in that created app will
work. Let me demonstrate that.
So
I go to
my Power Apps environment make.p
powerapps.com
and here I have a um uh two apps that I
will demonstrate later. I'm going to
create a new app. So I have to choose
between canvas app, model driven app or
portal app. A canvas app is an app that
is um just a blank sheet of paper where
you can put controls anywhere on the
page with positioning them with XY
positions. Um just like we could do in
the past in the forums uh editor in the
classic client. That's the best
comparison I can make to Business
Central techies who are longer in the
channel and who remember the forms
editor. This is kind of the same. Um, a
modeldriven app is working different. We
won't touch it here because I think for
business central people working with um,
uh, business central as a data source,
the model driven app is based on CDS
data is probably a little bit more uh,
off uh, here. So, um, I'm going to
create a canvas app.
Um when I create a new canvas app, I can
choose to do that as a uh with a
template uh with as as an empty app, a
blank app or with uh a certain template
or I can start with my data. And that is
what I will do. Before I can start with
data, I must have a connection. The
connection is going to my data. So under
connections, I need to have a connection
to Business Central, which I already do
have here. But if I want to create a new
connection, which is possible, then I
can just create on a new connection. Do
a search on Business Central. U find out
that I have a couple of them, two custom
connectors, two standard connectors. Uh
by the way there is also a dynamics
nav connector. It's in preview
for a product that is uh kind of uh on
the way out but it is in preview. So
okay um I don't know what exactly the ID
is behind that. Uh but anyway, let's
focus at business central and you will
see a business central here and a
business central on premise here.
meaning that this business central is
going to link to the cloud version and
the on premise is linking to an onremise
installation and if you want to do that
with on premise you need to provide him
with the base URL of the uh O data web
services and so he can contact that
when you click on business central and
you create a new connection you get this
question and if you were in um uh well
those vehicles uh session you will
recognize this screen this is oorth he's
going to ask you if you uh want to uh uh
sign in as a user and if you never did
this before he will al also ask you do
you allow me to um uh to get access to
business central on your behalf. So what
you in fact are doing is you are
creating a connection with your
credentials.
I've done that already. So I can skip
that for now. But if you if I click on
this one, he will just create me uh
another uh connection. So I say cancel.
And then finally uh you will under
connections get a connection here where
you can see um the connect connection
with the credentials that he's using.
So, we're going to use that connection
to create an app from data. Um, I get it
listed here as a data source that he can
use to create uh data from or to create
an app from. And then he says, okay, you
need to choose a data set in my
environment that I have. I have two
different environments. I have a
production environment. I have a sandbox
environment. And if I would create
another environment, it will also be
listed here. He will also show you the
companies in that environment. In fact,
it if you have four environments and
let's say each environment will have uh
uh five companies, you will see 20 data
sets here.
That means that your app if you create
it with the standard business central
connector is linked to a specific
company in a specific environment.
If you want to create an app that is
bound to a different um uh company or a
different uh environment then you need
to create another app. For each company
that you have, you create a new power
app because the data set is bound to
that um uh to that particular company
environment combination.
I don't like it. I think that uh it you
should have uh when you open a power
app, you should get a question which
environment and which company do you
want to open? At least that's my idea.
But the standard connector does not
support that. So I go with the sandbox
Kronos USA and then I get a list of
tables that I can choose from. Now this
tables come from the standard APIs but
it's not only the standard APIs. It also
uh contains some um stuff that is called
workflow customers workflow items etc.
These are not APIs. These come from the
web services. If I go in business
central for web services
um you will see them and you will see
much more entities uh in that web
services. So let's find web services.
Come.
You will find
PowerBI stuff here.
Oops. A little bit fast. Let me uh sort
on the object name.
I cannot service name. It's okay.
Whatever. So, um I have native
invoicing, native uh stuff, native PDFs,
uh a number of services that start with
PowerBI, and I have a number of services
that start with workflow. And if I look
into this one, I don't see uh those
PowerBI stuff. I don't see those uh web
services with native, but I do see the
ones with workflow. This means that the
connector is offering you a subset of
the APIs combined, the standard
published APIs, API version one combined
with the web services. There's a
combination.
Does that make a difference? Yes, it
does. I will come to that later. So, for
now, I take um whatever I take items.
Now let's um yeah whatever I take items
and then say connect.
And now he's going to generate the app
based on the items in the Kronos USA
company in my sandbox environment.
It will take a couple of seconds and
then I will have a new app over here
and I can um just
use and run. Let me run it. And I can
click on it. Get into the the items. I
can uh item details. I can even say uh
this display name is a etn desk at
enough
tech days.
Say save that one. Please
go back. And then here
under items.
Yeah, I should have warmed up that one.
Come on.
And here we see an addins desk at nav
tech days. Just updated from power apps.
I can tell you when you do a demo for
customers, this is perfect.
when you do a demo for a management of a
company uh be careful
because they think okay we don't need
those developers anymore we can do this
um and this is not a joke I know a
company where that happened
so
not everything is working out of the box
let's try that filter thing here search
items
boom Nothing
maybe with asterisk wild card or
question mark or percentage
nothing. You don't get any result.
What's going on?
I have now here in the top a up checker
with a red dot that tells me that
something is wrong
and it tells me the requested operation
is invalid on browse gallery items.
So what is the problem? It says the
requested operation is invalid um
logical operator or is not allowed. I
must set allowed logical operators.
What's going on?
The item that I'm using here.
Um, let me go back to the list. I'm
here. I have a browse gallery. And the
browse gallery does have an items
source. And the item source is buildup
of sort columns,
search of items blah blah blah.
What in fact he is doing is this
search. This is um what the uh the the
source is of our gallery.
to dive a little bit more into that.
It's items
and items is that data source that we
selected when we created the app.
You see here with square brackets but it
is just to identify that this is a data
source apart from maybe a possible uh uh
global scope variable which could have
possibly the same name. That's why they
used the square brackets around it. But
we see a search in front of it. And the
search is the problem here. A search is
what we call in Power Apps a delegate
action
because Power Apps tries to delegate
everything to the data source.
Searching and filtering should not be
done on power on power appite on a
mobile device. You should not load the
complete data source onto the mobile
device and then do searching and uh
filtering because there's a cap on the
maximum number of uh records that will
be read on 500 records. So the filtering
will probably not even be working. So
what he tries to do is to delegate that
search and there is another one that is
called lookup. It tries to delegate that
to the ser to the data source to the
server of the data source
say hey you search for me and give me
back the results that makes sense of
course as long as the server is
supporting that apparently the server
does not support it what is this server
here is that the APIs
well I don't think that is the API
directly
I think but that is not confirmed. Um I
think there is some proxy between power
apps and business central transparent
for you. You don't see it but I have
seen the URL once uh in in a lock from a
uh a flow that failed. Um, I think
there's a proxy in between that does
with a web application that turns the
API output into a real data table that
can be read by power apps. So there's
also some tweaking on the data and that
web application is not has not
implemented those delegated actions.
Something I've heard that they are
working on. I think I saw that somewhere
on the forum. So um let's hope they're
going to support it later on next year.
But anyway, this is what we have today.
You can create it out of the box. Just
don't demo the search part. Okay.
So
that's for the first demo. Let's go back
to the presentation and go for demo
number two.
I want to update item inventory. Um, the
standard uh item API supports to update
inventory. Um, I've seen that the pres
uh directions somebody doing that and um
it cost me some time to find out where
the code is, but it appears that the
items API page is supporting it. You
don't need any customization
unless you don't like the anonymous
approach of that item API page.
So what's happening behind the scenes?
We first go into the uh the page itself.
Uh so
I have a the source code of the uh item
of the APIs the API version one as it
was released back in uh July. And there
is on that one a function called update
inventory.
And that is called automatically when
you call this API and you set the
inventory value to something different
than uh the real inventory value. Well,
it's going to check it here. Of course,
if that is the same, then exit.
Otherwise, it just initializes a item
journal line. Um, and then
what is that? Double click to exit. Come
on.
Why do I have that one?
Where does that come from?
I have no idea. Ah, that one. So, um, it
just generates an item journal line for
us and then posts it. Well, nice try.
Um, I'm personally not so sure if I'm
happy with this uh approach. Uh there is
another approach that you could think of
because there is a uh a real code unit
uh in Business Central that does also
inventory changes. Uh that's the one
that is called when you are on the items
page and you want to uh to to change the
inventory. So I wonder why they are not
using that one. But anyway um if you're
fine with this approach, you can use
this. So that means that I just can call
this API and uh set the uh the
inventory. So let's have a look at
inventory of uh the item etn desk. I
have four items on stock. Um and what I
can do and I just want to do it one time
with the API call itself from Postman.
So, uh, I have a postman here to get my
companies list. If you were in vehicle
wo sessions, you know why that is. I put
that one in my company ID. I say get
items.
I have now my total list of items here.
Okay, they used a different tool, but
that not really the point here. I have
that item ID. I take that one, put that
into a variable item ID and then finally
I can update inventory and I send
inventory. Let's take 25.
And I'm posting that with a patch to
this item. Just click send
and
let him crack on that. Okay. 200 status
200. Okay. Let's go back to Business
Central to F5. And I have 25 pieces.
That's how easy it is. Now, I'm going to
I'm going to do this from uh from Power
Apps.
So, I have a Power App and well, let's
not leave this one.
And why not do this from a real Power
App.
You see, I
hope
this one is going to work.
So, there we go. Adjust item inventory.
I've created a very simple uh app. And I
see here the 25 items.
Uh click on that one. And uh let's say,
oh, sorry, that was not 25. It was five.
and say save it. It's now adjusting
inventory and it says inventory has been
adjusted.
So really, let's find out
and go back to
the items here.
F5 and I have now five items.
And the only thing I did in Power Apps
is to work with the same technology that
was behind that uh create app that we
just saw. So let me go into the app
itself
and show you what is behind it. Um
sometimes you need to be a little
patient with this uh Power Apps editor.
It can sometimes take a while depends on
the network load I guess. Um
so what I do have here is first of all I
have a um connection here the items
table again that items table from my uh
connection and then I have bound this
items just to the uh the gallery. I'm
now here in my item repeater. So this is
my gallery and um that is based on items
the data source that I have here. Then I
have an other screen called the
inventory adjust uh adjust inventory
screen and on that one I have a uh edit
form and that edit form has a couple of
fields. Um, and if I click on edit
fields, I can see them. I've put a
number. The number is view text, so I
cannot change it. The display name is
also view text. That means I cannot
change it. Inventory is edit as a
number. That one can then be uh changed.
And then finally, I have this icon. And
what this icon is doing is just a number
of steps. I told you it's typing in
formulas. Now in this case, what I am
doing is I send a notification that the
uh I'm busy with adjusting inventory
because I know the next step is probably
going to take me a couple of seconds.
Then I submit form which means I because
this is a data set he knows that he
wants to update the data set. So he
takes away all the plumbing from me. Um
after that I say when it is ready uh
inventory has been adjusted and then I
navigate back to the main screen. So
four steps just behind one single uh uh
icon that uh has it on set on the on
select property.
So um
demo number two is down still works. I'm
happy.
Let me talk a little bit about that
standard connector because it has some
there is some missing information in
there or at least something happened
with that API version one that uh I am
not really happy with. The business
central connector is based on API
version one.
the beta version of uh the API which is
still there by the way but it's uh
marked as obsolete is will be taken away
and the beta version had a customers API
endpoint that was combining normal
fields and flow fields flow fields as
sales and amount due etc. But in version
one they splited that. They have now
created two or three different APIs. One
customer API with the normal fields and
another API with the financial data. So
if you want to call uh that if you
really want to to run a slower API
because it does some calc some calc
fields, you need to call the customer
financial data API endpoint. and uh that
that is then really uh returning the uh
the the flow fields.
It's not that easy to combine that in uh
in an app because that gallery and that
form are based on one data set not on
two. So you can only see the fields from
that single data set. And then if you
say, well, wait a second. Um, I have I I
can call in I can link it to my
financial data and then find the correct
record. So I can combine on one screen
fields from two data sources. Then
technically yes, that should be
possible. But the thing that you need to
do is that single thing that is not
supported by the business central
connector, you need to call a delegate
function to look up in that customer
financial data endpoint. which is not
going to work. So, uh the only solution
would be uh a big workaround that I
created, but I'm not going to
demonstrate because it it doesn't make
sense. I I created a flow that then
calls the the API, then returns it back
to uh uh the app and then stores it in a
collection and then blah blah blah. It
it it was a detour that takes uh three
four seconds every time you open a
customer card. Not really funny. So the
only real solution for that is uh create
a custom connector with the data that
you want to see. Um
standard connector also does not support
custom fields or custom tables. The
standard connector is fixed. It's a
white list of APIs and web services. You
cannot um add any custom API to that
one. You cannot add any custom web
service. There's one thing that is
possible though.
I uh said you earlier I told you that
the web services are also part of the
connector and the page based web
services
are based on pages that are extendable.
Well, for now I don't know if it's going
to change those pages currently are um
uh it's possible to extend them with a
page extension. So with that you can
create a pace extension for example for
the workflow um uh customers or workflow
purchase documents and add other fields
and in that way I was able in a current
project to add custom fields from the
purchase header to the standard API
connector. So I had no reason to create
a custom connector for that which saves
a lot of work actually. But as soon as
you want to um uh uh go with custom data
read is not in standard connector then
you have to create a custom connector.
A custom connector is the channel
between power apps power automate and
your APIs. It allows you to define your
own functions and triggers and it's
based on the open API specification
meaning that um open API 2 as far as I
know uh you could import a complete open
API specification. Unfortunately at this
moment you cannot generate an open API
specification from your custom APIs.
this is something they're working on but
it's uh their day is is Microsoft in
this case um that is coming I don't know
when I've not heard about any uh
estimation but it's something that's on
the radar because creating custom
connectors is really a tedious task if
you made a mistake you can start over
again or try to modify the the swagger
information yourself
uh let's just dive into that let's uh
look into a custom connector and see how
that works. So what I do have is
um a small
app and that app and those who were in
my uh workshop earlier this week on uh
Wednesday they will recognize this one.
Um u I'm creating friends. I have a
small table um with friends just code
and a name and a page that will show
them and we'll show all my friends. Let
me find out if I currently do have any
friends
in Business Central.
Well, I do have three uh friends. Me
just delete all the friends so you can
see that it's really working. And at
this moment I've unfriended everybody.
So I'm kind of a alone in the world. Um
so what I can do with an API I've
created uh an uh a friends API um that
allows me to create new friends to read
the friends etc. And I want to create a
custom connector that allows me to um um
to to read the friends and to uh uh to
create a new friend. That's that's the
goal. Let's try to do this. Um and I'm
uh just doing this from scratch. If it
doesn't work, I created it already
before, but um I know you guys want to
see this uh working in real life, so why
not just do it? Um so to work to work
with a custom connector we need to know
exactly the URLs. So I first start with
um let me close these here.
Um
my base URL that I will be using is a
base URL. Let me uh show it here. um is
based on a base URL API business central
toamics.com
on a certain tenant uh called
cloners.com company and the environment
is sandbox I can also uh what's that
here um not sure if I can enlarge this
doesn't work but you see here that it is
a get on chronos v2 kronos company
sandbox api my name sl uh um the group
nav days
the version on API dynamics business
central dynamics.com so that is my
information that I need um as the base
URL now on that one um I can get
companies I need companies uh because um
uh the friends uh uh API has the company
ID and the URL so I first start with
getting the companies
and then uh get this one. I put that
into my company variable and then
finally I can use that in my URL here.
Then say send and this is my complete
URL.
Okay. So what I need to do is to create
a custom connector that has uh that
calls the get friends. Let's let's just
start with that.
Um
let's close this one. leave
custom connectors. Um you find them
under data and then custom connectors.
Then we can uh create a new custom
connector
over here. I start to create it from
blank. So you see out of the box how
that works. um
BC French.
That's the name. The first thing that we
need to type in, we can uh uh use a
different icon if you want to um give it
a description, but what we really need
to type in is the um base uh the host
name of the URL, which is in this case
api.business central.dynamics.com.
The next thing is um if that base URL
needs to be extended with something that
can be applied to every single action
that we will create. So the base URL
that we type in here will be applied to
all actions from the connector. Meaning
that uh we can then shorten the URLs for
the connection. We only need to specify
the path behind the base URL. So if we
look at uh this one here, I've now just
specified only uh dynamics.com. Every
API will currently have /v2. So that's
something we uh at least can uh type in.
Oh, where is it? Here. So uh v2.0.
Don't forget the uh training uh slash.
But there's more. Um we also have
tenant. We have environment and we have
a company ID in here. For now, for this
demo, I will just um uh use this
complete URL as a base URL up to um the
this one here.
That is because um at this moment I I
know up front that I want to connect to
the uh this tenant. I want to connect to
this environment.
Later on you will see how to make that a
a variable. So I take
this Kronos company sandbox up to beta
and
this is going to be my base URL. The
next step is to specify security
com security. How do I authenticate
against the um the data source? And for
now I choose basic authentication.
But you should not type in a username
and a password here. We are creating a
definition. We are not creating the real
connection. So the only thing that you
need to type in in here is how what is
the caption for the username and a
password that you require for basic
authentication. So let's just type in
username password or to make that a
little bit more clear. I want to have
the service web service access key. And
here you'll see later on this web
service access key as the caption when
he uh uh asked for the real credentials.
The next step is uh the definition
itself. The definition um here is
containing actions, references,
policies. I will only talk about the
actions here. Uh the references and
policies are not really relevant for for
us with business central. I can create a
new action and the first action I want
to create is get friends. Read the uh
table friends from the database. So I
give this one a friendly name and an
operation ID which does not may uh
contain any spaces.
The request that um this one is based on
can be imported from a sample. It is a
get and the complete URL is in fact this
one. Well, it is I already specified
this as the base. So I can take only
this as the remaining part but it is not
really necessary to say okay I have
already created that as the uh as the
base URL. If you take the complete URL
you will find out that part of that URL
is already uh the base URL. So we will
take that out. So I uh copy that and
paste it in here. So this is my complete
URL and then say import.
That's fine. My request now contains of
a URL with no parameters. Come back to
the parameters later.
Then it has a response. So I have to
specify how does it look like? If you
have any friends and for that I can take
the response from here. But this one is
pretty empty. So we need to have at
least a response with one friend. So why
not create one friend at least friend
01. Um oh why would I do that by the way
in this way? Um I have another one in
Postman for that makes things even
easier.
Um no I cannot list this the cat. So I
do have a name. Uh let me edit this one.
This is going to be John Doe.
And now if I go to Postman, say send,
I do have that one as output. I copy
that. Go back to here. Uh oh, I was
here. Paste this as an example.
Import it.
And now when I click on default, I see
that he has recognized that in that
output is a O data context. an od e tag
a code and a name that's just what it
got out of that response that I just
pasted in well that is all information
that I need for the get friends so I can
now create the connector and this let's
just test it to see if it works
because at this moment we are close to
creating the app itself
in order to test
I have to create a connection first
because there's no connection based on
this connector. So that's the first
thing I need to do. And here I see
username and web service access key. My
username is AJK and my web service
access key is um go to users card.
This one
take that one. Press Ctrl C.
Paste it in. say create.
This one now moves out of the uh custom
connector creation. It goes to the um
connections list. But at least you can
see here the BC friends just created one
second ago. Go back into custom
connectors. Click on edit. We go to
test. We say we want to use this
connection. And then test the operation
get friends. and we get a 200 and we get
data.
So
now I'm going to create an app based on
this data.
So I quit custom connectors. I go to
apps and say I want to create a new
canvas app.
And by the way, I can tell you it's
going to fail.
I know why, but it will fail.
And the first thing I need to do is to
tell him what is my data source that I
want to use. I want to use BC friends.
And you know what? Not a single question
about which environment, which company
whatsoever.
And that is the difference between
custom connectors and a standard
connector. He will not ask you these
questions in Power Apps. No matter what
you do, you will not get this question.
So I want to uh uh insert a gallery over
here on my uh screen. Insert a gallery.
Gallery is what we know as a repeater.
Blank vertical. And I want to give him
as the source the friends.
But that is not what he can do. He says
here name isn't valid.
He does not know BC friends is a custom
connector with actions. So we need to
tell him what is the action that will
return our data set that I want to show
here. So I say get friends. That's the
action really with brackets because this
is a function
without any parameters.
Okay. So now we can work on this. Not
really because here I get an error
message. I hope you can read it, but it
says status code 404 message resource
not found.
And we'll see that here as well in the
runtime. I have an error message 404
resource not found. Well, this one took
me a couple of minutes to solve. Um
because everything looks fine, you can
go back into the custom connector, test
it again, it will work. What is the
problem here? In the uh custom
connector,
we have specified
that the URL of the um
uh the URL of the uh this uh endpoint
contains a company ID.
But Power Apps
treats this differently. Power Apps
wants to see this as a string with
quotation marks. And if you put
quotation marks here, then I cannot test
it. So the problem is I need to specify
this as a parameter rather than having
it as a fixed value. So don't put fixed
values in your custom connector. That's
the tip. So what I need to do is to
specify that company ID is a parameter
and to do that I just take the complete
URL. I uh post copy paste that into uh
notepad and say okay this one take that
one out
and this is going to be
company ID a parameter is uh used is
specified with curly brackets single
curly brackets around it. So I say
import from sample. This is get
and that is my URL. And then we see in
the path here a um parameter.
I can click on that one. Say yes this is
required. I can give it the default
value. Not going to do that. We'll still
fail. I will do that from uh from Power
Apps. And I still need to specify well I
don't need to respecify the response. So
this looks fine. I can now update the
connector. Test the connector once more
to see if everything works.
I need now to specify that company ID.
So I copy that one, paste it in, say
test operation. I have a status 200 and
data. So that one works fine. Now I have
updated my connector. However, um this
one doesn't know about it. So, what I
now need to do is to take out
this data source so we can refresh it.
Say, "Yep, here we go. This is the one."
And
now to find out hopefully that he knows.
Yeah, I need a company ID.
So,
this
is what I would like to do.
Okay. error is gone. So
let's see if I can get any data
inside my repeater. I want to insert
a label.
That label is now pointing to this item.
O data context. Oh, that's not what I
wanted. I want to see the code.
The code or the name. Hey, it's not
there. I have O data context only as
possible value, but I I'm I'm sure that
I do have code and I do have a name.
What's the problem here? Um the problem
is that we are looking at the O data
payload that comes back from the O uh
from uh API.
This is what you get and the data is
inside value. So the only thing that I
see here is oh data context and I can
see value but it doesn't look inside it.
But my real data my data set is this
part. This is an JSON array. I want to
show this into a gallery. So I need to
have the array. So my only option is go
to this one here and say behind this I
want to have value
and then
suddenly code is known.
Add another one here and say this is now
this item dot name. And there we go. So
now I have my value.
So this is how it works with custom
connectors
and because of the time I have some
other demos I'll skip the other one will
create it but creating it is a matter of
doing the same thing over again saying
create a custom connector now with post
in the parameters. Um, so we add another
action with post and then um we have an
an screen where you have some input
fields. You have a button that calls
that create action with the parameters.
That's it. It's not really impressive.
So
let's move on with the next part.
I have a
simple demo. A question that I get quite
some time. Can we do something with
pictures?
And uh can we uh u take a picture and
upload it to Business Central? And yes,
that is possible. Well, it worked
yesterday, so I hope it still works. The
um
thing is that I still have that.
Come on. Can you please go away with
this one?
Um the output of the picture is B 64
encoded. So that is something to keep in
mind. But with a custom connector, we
can upload it to uh to a blob field. So
what I do have here in Business Central
is a
pictures page.
I hope I deleted all my test pictures.
Yeah, there was one.
Um let me Create
uh get a picture.
Take picture
and please smile or wave or whatever.
Capture. Now he's uploading it to
Business Central.
That takes a moment, but
it should give me a success screen.
There we go.
And we do F5.
And we have another picture here.
This is you.
[Applause]
So what is behind this?
I do have an API
created for picture
and this is um just a simple table
the picture table with a blob field in
it. So that should be uh not really uh a
problem for you to understand. Um
what one thing that I uh need to do is
to uh upload my data it's going to be B
64 and um for that when I'm in the
picture API page I needed to do a little
trick. So here I have my picture API
page and if I create a record the thing
that I need to do here is
uh to find out if the B 64 started with
data column image that is uh what a
standard B 64 encoded image contains but
that is not a part that I need to have
into my image. So I need to strip that
off. it will end. There's a a complete
stream. I have no idea how long that
exactly will be, but it will end with a
comma and I need to have everything uh
removed up to the comma and then I will
have my real B 64 part. So that's what I
do here. I remove that and then I store
it with B 64
uh sorry in the I store it as binary in
the blob. So, of course, I do have a a
custom connector for that. And
that one is this one. Let me edit it.
And my definition here is create a
picture based on this complete URL which
is my URL for the pictures API. And in
that I have a body. The body is uh
containing data and an ID. Um the ID is
uh should be hidden but the data is what
my what my real data is going into. So
in my uh apps here I do have my camera
app say edit.
Yep.
The only thing that I did is uh I
created a take button, a capture button.
Normally with Power Apps, you have the
camera the camera uh control, you need
to click on the camera control to take a
photo. That's not what I did. I wanted
to have a picture um uh button. And for
that, if you want to use that, you need
to uh grab
the camera stream.
But to get the camera stream, you need
to set the camera stream property. So on
the camera I have a stream
uh property where is it stream rate and
set that one to 100. Then I can take
something from the uh from the stream.
So what happens here is that I call
create picture record which is the name
of that action on my custom API my
custom connector I create it with that
company ID and with an ID um that I
create here as a new gooit and the data
coming from the stream and if ready I
navigate away to the next screen.
So that's basically what happens. It's
not magic.
It's just create a table, create the
API, the custom connector, and then um
call it from Power Apps.
Okay,
let's move on. 22 minutes and I have
five more demos to go. So let's speed
up. Power Automate. Actually, something
I like a lot. Power Automate. what
exactly um is that doing? It is about
automating a process.
So um something happens and then uh in
one of your data sources and then you
take an action
without uh any human involvement well at
the start
but you can involve human uh if uh for
example with the approval say I want to
start a certain uh uh set of actions
when something happens but with
approvals I need human interaction so I
can't send out the approval to somebody,
wait for him to respond and then um the
the actions automatically continue. Um
you can work with uh AI builder for uh
uh automatic intelligent processes and
you have something new that's called the
UI flow um which is in preview that
promise you to uh to work even with
applications that do not have an API
because it will uh simulate user clicks
on that application. I can imagine how
it works on uh web applications. I have
no idea how that will work on a old uh
old visual basic 6 application for
example because flow is a power automate
is a uh a real SAS platform running
somewhere in the cloud. Anyway, what I
want you to show very quickly is a
little bit of the power of power
automate so you get an idea of how
powerful that actually is. So I go to uh
uh Power Automate to my flows and
create a new flow.
I skip this here. The first thing that I
need to do is to start with a trigger.
And what I'm going to do is to start
with an HTTP trigger. So this is when an
HTTP request is received.
This basically turns your flow into a
web service.
The URL of the web service will be
generated when we have saved the uh the
flow. Before we can save it, we need to
take one other step. And uh I will do
that. I will as a next step just send an
email.
I will send an email to um
well let's just send an email to myself.
whatever I have already that open admin
and
with subject uh new mail from flow
and oh in fact it's power automate
whatever
with body uh um
isn't
this powerful
let's save
Then go back to this one here. Now we
have a URL. I copy that one. I go to
Postman, create a new request,
post it in here,
set it to post,
and click on send.
It returns with status 202 accepted.
And
it should come in in a second.
Come on, you can do it.
No, there's not this forward field. So,
say okay. What's going on? It succeeded.
Okay. Well, the idea is that I would get
an email right here, but at this moment
it didn't come in. I this sometimes I
see that happening. The first time you
test this out, it can take a couple of
minutes up to two hours the first time.
That's what I experienced last week. Um,
so let's not wait for him to uh to
finish this. What I can see here in my
runs is that I did have a new email sent
to this admin user. And
ah I should have sent it to AJK. Wait a
second. I'm logged in as AJK and not as
admin. So oops I should have remembered
that.
So let's send it to
AJK.
Hopefully then it will be say be be
fast. Okay, let's go out go back to
Postman. Send it. The story about the
delay is still true because last week I
really had that u new created flow and
it took me it took him two hours to
arrive in my mailbox. But anyway, I have
a new email.
Imagine that. I now have this URL in
Business Central stored in the setup
table. You can just uh go with the
normal HTTP client post this URL and you
have sent an email out of Business
Central would just take you five minutes
to create it. Right? Let's make this a
little bit more powerful. What I want to
do with my flow is to tell flow that I
will receive a body. And let's create
that body here in Postman.
Say this is a raw body. It will be JSON.
And
I'm going to say the um email tool.
It's going to be again
my email address.
The subject
is email from Postman. And uh the body
will be
cool demo
for power automate.
I take this body here, copy it
and say generate
from here.
So now I have generated for him an JSON
schema.
Then in my email here I say please
say
take email two
take the subject
and take the body out of that request.
Save it.
Go to Postman and really send it.
Go back to my mail and I have new email
from Postman.
Can you imagine how powerful this is
from Business Central? If you have this
URL to send an email,
I hope you get the idea.
So, and this is just one example. Of
course, I could do other things which I
will show in the next demos.
Um,
40 minutes left. Let's see if that
works. I want to uh quickly go over the
approval templates. We have 12 approval
templates available and uh what uh what
you you it's not really impressive what
they are honestly because they are just
copies from each other. Um the only
difference between them is that they
have a different trigger and the trigger
is um uh approval requested for uh uh
purchase order, approval requested for
purchase invoice, approval requested for
sales quotes etc etc. But the rest of it
is exactly the same. We also have two
templates that are uh coming from
Microsoft flow community and that is um
nobody knows who has done that. Anybody
in the room
raise your hand because nobody knows who
created those two uh flow community
templates.
Uh it's a mystery. That's I told
Microsoft I said you don't have 12, you
have uh 14. They said no no no we have
two are there that we haven't created
ourselves. Uh anyway, um
those approval templates are linked to
workflow in business central and that is
what I want to show you quickly because
there are some little uh secrets behind
it that uh you need to know. So what I
will do first of all show you that
everything is live. I go to workflows.
Come on. I don't have any workflow here.
Then I go to flow and I say create a new
flow. Um create from template.
Search for my business central templates
and create uh one for purchase order.
It's going to show me the connectors
that he will use. I need to have a
connector for approvals. That's it. If I
want to change the account, I could do
here uh could change that. Say add a new
connection. Now I'm fine with this.
Continue.
And then the big um
uh fillin happens. I need to specify
sandbox. I need to specify the company.
Uh this the first thing when a purchase
document approval is requested.
Then the next step is to get the record
again from sandbox Kronos USA.
Then I have to start with um uh who to
type in who will approve this. For now I
take my
email address.
There we go. This person.
Then when the approval is ready, I have
a response from the approval. I check if
that one is approved or not. If it is
approved, I execute an action.
Don't forget to again type in
environment and company name. Every
action is on its own. That's why you
need to specify this. Um, and then
Groners USA on the reject part. Now I
can save this whole flow
and go back. Yeah, that's fine.
And then go back to business central.
Funny thing is if I do F5, nothing
happens. But if I close it and go back
workflows,
I do have a new workflow. So now I have
a new workflow created from business
central. Okay. So what what happened is
behind the scenes that he just called
business central say here is a new flow.
There is that first trigger that
registers himself in business central.
There's a lot of code behind the scenes
hardcoded creates that workflow with the
correct uh events responses etc. This is
a hardcoded piece of code that creates
this whole uh workflow. For example, in
the workflow, if you look at uh the
possible responses here, then you will
see send a record notification to a web
hook. This web hook is the URL from
Business Central that he created, which
is exactly the same type of URL that we
just created with the HTTP request that
I used to create an email.
So, um,
let's test this one because it's going
to fail. This This one is just going to
fail. Um,
just to make sure
that
my setup is correct. Yeah, this is what
I expected. This is out of the box. What
will happen?
Purchase orders.
Open a purchase order
and then say
request approval
send approval request
status is now set to pending approval.
And here in flow
I have a new flow run which is currently
running
and it's now waiting on start for
approval.
And that approval should come in here.
But it doesn't right now. This was what
happened last week to me that I tried
this out a couple of times and then I
went to bed and then at 2 a.m. or
something the approvals came in in this
inbox. So um instead of waiting because
we have only eight minutes left, I want
to move on and tell you what is going
wrong. If I approve, if I try to do that
from here, then it will fail because I I
get an error message saying that um AJK
is not allowed to take the next step.
That is what I will get as an answer as
an error message in flow. What is the
problem or the problem? What is what is
going on? I have a connection over here.
Um, business central is the flow is
connecting to business central with this
user ID ajk@cronis.com.
This is the user ID that will be seen by
the code in business central as being a
user that approves.
However, this is not an setup uh
approval user at this moment. So I need
to go to approval users
uh setup.
Come approval.
I don't want to. Okay. Approval user.
There we go. Um I need to create a
record and not just for AJK.
This is not enough. Um I need to have
the approver ID here. I need to have
that user that is used by flow by the
connection of flow. Need to have it in
the approver ID field or in the
substitute field. Well, I cannot approve
my own request. So if I look here,
it will show me somebody else
but not me. No, nothing in this case
because I did not have any other user in
this list and this is just the user
setup table. Now if I look here at
approver ID, I see finance and if I look
at this one, I will see AJK.
I can delete this line.
This is in fact the record that I need.
Well, to have that approver ID, I need
to have it as a record as well. But this
is what the minimum setup that you need.
The user that you have on the connection
needs to be in the approver ID column.
It doesn't have to be on the um uh line
of the user ID that does the request. As
long as it's somewhere a record with
that ID in the approver uh ID field,
then it's fine.
So um and then it will all work
automatically.
I'm not saying I'm happy with this. I
think there's some room for improvement,
but this is what it is.
Let's move on with the demo about the
survey.
Um, as you can imagine, I just created a
single uh a simple uh custom connector.
So, um, let me quickly show you that
custom connector here. It's not under
connectors, by the way. It's under data
and then custom connectors.
And there I have my survey connector. I
have for every uh different demo I
created a different connector. We can of
course combine it into one big
connector. That's just up to you.
So um here I have my definition and in
my definition I have create response
which goes to my custom API that I have
created to store responses in business
central but I have more. I've also
created an action to get environments.
So when I do that one, I get a list of
environments that I have enabled here uh
in my my um tenant and I do have a get
companies action.
So if I do test operations, I see the
companies here. Why is that important?
Well, in my definition for create
response, I have specified that
environment and company
are parameters. You see the curly
brackets. So they are here in the path
as parameters. And for environment, I
say this is a dynamic parameter which
comes from an other operation, the get
environments operation. I want to use
the value name to put that into the URL.
And the display name is for the
drop-down option value option caption.
And the same
with the company ID. He should get the
company ID from the get companies
operation. that one already has the
environment in its URL that he can take
that from my environment variable that I
already had and then have the value the
ID to use that to paste it into the URL
and the display name with the name for
the dropdown. As a result, what I get in
my flow
is here
create response
a drop-down with the uh sandboxes with
the environments that I have and the
companies that I have. So if I switch
here to production
couldn't okay no I was expecting him to
at least show me okay I know why my user
that I'm using is not in the production
environment anyway so that wouldn't work
but okay so um in this way we can give
the user who puts this together a real
nice experience
okay Um final demo.
Um
a couple of months ago I did a
presentation about working with files
and then this um uh Twitter uh feed uh
popped up and
some people said well you shouldn't work
with files.
Okay, that's a statement because if you
believe in that then my next demo is and
the final demo I promise uh it does not
make any sense
but I'm afraid we still have to work
with files. So I give you one ID what is
possible with power automate
uh we can use the APIs to upload files
into blob fields. So there's documented
so won't go uh deep into that. the the
picture API was also doing that. Um I
want to combine that API with flow. So I
have created an API uh with um uh an API
that uh creates an incoming document and
adds an attachment to it and that um is
uh created a flow for that. a custom
connector with the actions created a
flow that reacts to uh when a new email
arrives with an attachment then grab the
attachment and uploads it to the blob
field with the custom connector API
settings of API actions. So um with an
API uh with the trigger for email inbox
that is working but I could also create
a trigger for FTP or local file system
with a gateway connector etc.
So I want to have your help. Please send
me a PDF if you can miss one and I will
do so the same to finance@cronis.com
and I will show you that that one will
uh end up in business central. Um I'll
give you 15 seconds to get this email
address and I will do it myself too so
you can see this uh working. finance at
cronis.com.
5 4 3 2 1 and it's gone.
So, I'm going to mail something myself.
New message to finance at cronis.com.
Um, oops, that was not what I wanted.
say final demo,
attach a certain record, a PDF file and
send it.
Then
in Business Central,
go to incoming
documents.
Here is my final demo.
I will.
Okay. So guys, you have just sent an
email and now everybody can see it.
I will view my
PDF that I've just sent myself.
So here it is.
And oops, I see some more emails coming
in.
Let's take this one.
view.
There we go. So, that works.
And the others I will read later on
because then I did I did the same demo a
couple of months ago and then they sent
me some pictures in PDFs that I didn't
want to have opened at that moment. So,
I I know your dirty minds.
Okay. Um, that was the final demo. So
well I uh not really I had another demo
for custom triggers. Um just very
quickly I'm not going to um uh to go to
demonstrate it because it's time is up.
We can also create custom triggers and
custom triggers means that uh we have
seen that when um an uh approval is
requested that's a trigger that
Microsoft created. We can do the same.
We can create our own triggers for
example when a sales order is shipped a
real business process or when a user is
created or when inventory goes below a
certain level etc. And for that I have
created in business central a table to
store flow web hooks. I have created an
custom connector that specifies a
trigger that points to the API to store
the web hook.
Then in business central I say hey if
this business uh process occurs do I
have a web hook? If yes then send that
web hook a notification.
Do that very quickly
and that is
here in flow under my custom connectors.
The trigger
edit
definition. Here I have a trigger that
is called on ship sales order. And this
one points to a API flow web hooks. That
is an API that just stores a URL.
And inside um Business Central, I do
have a
an um some code
and that code I have this um table that
stores URL in a field notification URL
and then some code to execute this URL
which happens on after post sales dock.
If sales error is ship, then I'm going
to take an action. I call that web hook.
Well, let me um
look into Postman if
that one does have
any web hooks. At this moment, it does
have already a web hook. So, I've
created a um a flow for that.
when a sales order is shipped.
And here in the top you see when a sales
order is shipped in sandbox in that
company. If I save this u this this one
then he will register himself with that
URL that you see here. So and the next
thing is to create a task.
Let me do that one more time. That's
really the last demo under sales orders.
Let me ship a sales order
and not invoice it. That's the ID
because the task is hey you need to
invoice this one.
So
posting post only ship say okay
come can do that today please you want
to stop
and
two seconds ago this flow has run
and here under tasks
I should see a new task. There it is.
Create invoice for this sales order. So
that is what the flow was doing. It
says, hey, when a new sales order is
shipped, register again himself with
Business Central. Here's the URL. Then I
get the record that comes in when this
one happens. and then finally create
that task.
I think this is a real uh example of
doing business process rather than on
create uh record etc. So I let you go if
you have any questions feel free and
otherwise uh safe trip to home and uh
and and enjoy the closing.
I see a question over there. Oops.
I don't know if it works.
Should I switch that on?
Hello.
Yeah.
Yeah, it works. Perfect. Uh, just a
question about the licenses. So, I want
the license.
The license.
Yeah.
What about Business Center when you use
I'm I'm a techie guy, so I don't know a
lot about licenses, but let me tell you
this.
Um,
okay.
Business Central comes with a Dynamics
365 uh for Power Platform license.
Okay. But in October they changed that
license to they limited the possibility.
So I don't know top of my head what
exactly you can do with it.
Yeah.
But you earn a t-shirt for that
question.
Yeah. Thank you.
Next
over there.
Yeah.
Watch your back.
Thank you.
Um I I have a question
guys and a safe trip home
for those who are leaving now.
I have a question regarding the
connection.
Oh thank you.
Um if I'm creating a power app then I
have to specify a connection and I'm
connecting under my account or under the
creator account.
Yeah.
And if I pass it on to another user
good question.
Um can I change the credentials there?
So um what what happens if you have
created a power app that uses a
connection and you share the power app
with another user?
Some connectors can be shared, some
connectors cannot be shared and a
business central connector is a
connector that cannot be shared. So
every user needs to create his own
connection with its own credentials
but and that I haven't tried out yet. I
have seen that the custom connectors can
be shared. Okay. So if that is the case
then I can create a custom connector
share it with someone else who can then
enter business central under my
credentials.
I don't know if I would like that
neither.
But uh standard business central uh
connector doesn't do that. Good qu
question. You earn a t-shirt. Who wants
to have the next t-shirt? We have the
best question here.
Ah come on. You were you were just next.
Right.
Only if you have a good question.
We'll see. Um question about those apps
uh that you showed us on on phone
actually on smartphone. Yeah. You were
logged to the power apps or is is there
an easy way to deploy it as an Android
app in example? So um I think that's a
good question. So sure is yours. Um yes.
So what I did is I uh downloaded the
power apps from the uh the the play
store and then you log in with your uh
office 365 user. That's it. And then you
see uh you have to select the
environment. We can have multiple
environments in uh in Power Apps. Um but
you you select the environment and you
see the apps that you have access to
inside the power apps app that you
download from app store.
It's app in an app. Yes. Uh they have
something that's called portal app which
can be used by anonymous users but that
is basically a web application does not
require an uh an app on a mobile. Yep.
Thank you. uh
flow con uh a BC connector is still
preview as uh which is recommended uh to
using preview connect BC connector
can you speak a little bit but I don't
get a question
just speakh
okay
yeah uh BC connector is still preview
and uh uh I'm a I'm a function
consultant and our customer BC using BC
uh they interested in using B pro BC
connector but they say uh is it okay to
preview connector so uh which is better
using preview connector or uh use
creator and using custom connector
I'm not sure if I understand you
correctly but I think you say if it is
uh good to use the preview connector
because in preview is that your
Uh yes, this DC connector is preview.
It's preview. Yeah, it's fine to use. I
don't know why they put it in preview. I
have no idea why. It's already there for
months, years.
I don't know.
Hello. I have a question about uh
approval of
approved workflow. So for example if we
have a purchase invoice but uh for
different departments we have only one
to one one approver one approver for one
user.
So uh when you create that approval you
have the set of conditions that set of
conditions you can uh specify they will
be copied over to the workflow and there
it will filter the purchase order if it
fits to the um uh to the filters. And
what is uh even better you can use
custom fields on that filter. So if you
have any custom fields you want to
filter on with the approvals that works
because they are based on the web
service uh page web services. Uh so that
then they you can extend them with a
page extension as long as they allow it
because maybe sometime they say extend
will uh false and then it's over but for
now it works. Yep. You show that power
apps have a connection for BC on prem.
Yeah.
What about uh Power Automation? Does
this work with onrem installation or how
does this
Yeah. Uh yes it does. Same story. So you
create a connection for um Power Apps
for um Business Central uh onrem that
that will just work exactly the same
way.
Yeah.
Okay. That's it for the questions. I
have one question here.
Is it possible to use the custom
connector to create um a meeting invite
in Outlook?
Yes, the uh not Yeah, not a custom
connector. There is a connector to
create invites. So, you don't need a
custom connector for that.
Okay.
Yeah, there's out of the box available.
Okay.
Thank you so much. If you have any
further questions, you got my email
address, I hope so. Uh enjoy uh the
weekend.
