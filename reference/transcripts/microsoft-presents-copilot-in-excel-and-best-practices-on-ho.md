# Microsoft Presents: Copilot in Excel, and best practices on how to work with data in Excel add-in

- **Source:** https://www.youtube.com/watch?v=7t3fAC_Bsa8
- **Video ID:** 7t3fAC_Bsa8
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 37m59s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Ladies and gentlemen, please welcome
Matty and Shria and
[Music]
hello. So, welcome to the last session
of the conference
and a quick show of hand. How many of
you have actually used the Excel addin?
Okay, so quite a few. That's nice. Um we
are here to talk about
the Exceladden and demystify few of the
things that goes on underneath it. And
um with me is my colleague Martin
Nielson and uh my name is Shrian
Minskar. I am working at uh Microsoft in
the server team in business central and
I'm working on the mostly backend
functionality which is going into the
Excel addin functionality and I will let
Matty introduce himself. Yeah. Uh so I'm
Matt Nilson and I'm also working for
Microsoft and I'm working in the team
connected experiences and we mostly work
with integrations like teams and outlook
and copilot and excel in this case.
Yeah. Uh so the agenda for today is we
are going to talk what's so interesting
about Excel addin why we are going to
talk about it and what do we want you to
know what things are going underneath it
what things are going under the hood uh
then we are touching upon a little bit
of architecture of how the functionality
works end to end
uh Matt is going to do a demo with some
co-pilot in excel functionality shown as
well and then we'll do a technical deep
dive into how the addin works and how
the underlying web services are
supporting this functionality and
finally uh I think we'll have some time
for the questions. So let's talk about
what's so interesting about Excel addin
and why we are talking about it. So
Excel do you know that it is the most
used integration in business central.
It has a mau more than 100,000 and many
many users use it.
which is very fascinating.
What it allows you to do is to do
seamless data editing between Excel and
Business Central. So, it's like a
two-way sync that goes on between Excel
and Business Central. It also allows you
to use some of the Excel tricks that you
have, some of the Excel knowledge that
you have and the changes you can make in
either of the part, they are synced
together. So it gives you an ability to
use your Excel knowledge to do changes
to the data in business central
and it also supports multi-comp and
multi-environment workflows. So in the
Excel addin you can actually change the
company you can change the environment
and I think that's very very convenient
when you want to deal with data between
different companies and different
environments right let's touch up upon
the architecture a little bit so it all
starts in the browser where you click
upon the edit in Excel action on a list
page
when you do that it opens an Excel
workbook with dynamics office addin
embedded inside it and that addin is uh
the excel addin. So at this point of
time it tries to initialize itself
um and it basically calls a business
central service to get some
configuration. That configuration
includes uh things which are very
specific to business central and which
allows the addin to target a particular
environment and mind well that the addin
actually is a common addin. It's an
excel addin is a common addin which is
shared across multiple different
Microsoft products like finance and
operations. uh business central use the
same addin but it is the configuration
which makes it very specific to the
business central scenarios uh and to the
changes to the data that you want to do.
So once the call goes to the service uh
in SAS the Excel addin provider service
it goes to the environment and it
retrieves the information about your
tenant like what environments it has
what companies it has and then this
information is passed back to the addin.
Once the information is passed back the
addin makes the call to get the O data
metadata. Now once the metadata is
available to the addin this is what
tells the addin to map the columns in
the entity to the columns in the excel.
So at this point of time the metadata is
the one that is responsible for making a
connection between the entity and the
properties to the columns in the Excel
addin that you see. And once you have
that binding then you can do operations.
Then you can do a get operation, you can
do a post operation, you can do delete,
update and so on. So this is how it
looks from front end to back end. And um
these are uh things that are going on in
the in under the hood.
So um now Matchy will do a demo of how
the addin works and we'll show you some
of the functionalities that you might
not know about, might not seen. Uh so
over to you Matty. Yes.
Uh so everything starts in business
central and uh as we saw in the diagram
uh we're going to click edit and u the
page I've chosen for this demo is the
items page
and um so what we're going to do first
is just apply a filter because we want
to sh uh show that the filters they also
carry over from business central into
the uh the Excel addin. So let's say
that we filter on just all of the ones
that start with the 19 in the number
series and uh we click edit in Excel and
uh then it downloads the workbook that
we saw in the diagram. So I've cheated a
little bit and I've already downloaded a
workbook that I have open over here but
it's going to look exactly like this if
you open the other one and um so let's
go through some of the basic
functionality first. Uh let's say that
we want to create a a new item in this
sheet. So what you can do is you can go
into the design pane and uh you can look
at the table. So this is the data source
information and you can see which one is
the primary key of the items page. In
this case we can see that number is the
primary key. Uh so let's take a number
from one of the other ones. And uh we'll
just take we'll change it a bit to
something that doesn't exist in BC.
Change it to 10. And uh the description
it doesn't really matter but it's nice
to have. And uh we'll just take one from
the one above. and we'll go back to the
addin and we'll publish this. So now
what happens in the background is that
uh we make an o data call to business
central that inserts this record and we
see it was successful. So one of the
other things that you can do is that um
you can also delete this row that we
just created of course uh and uh it's
similar just like deleting the row in
Excel and you can publish that and then
the addin is going to give us a a
warning that we're going to be deleting
a row when we do this.
Yeah. Okay. Let's just let's refresh one
time to just get all of the E tags on
the over data endpoint completely
refreshed. Uh so it was this one that I
created 1910 and uh let's delete this
one and uh publish
and this one should also be gone from
business central now. And uh if after
the creation if you went to BC you would
be able to see the row and after the
deletion it has disappeared in BC. So
this is one of the really powerful
things about that in that basically
everybody like all of the accountants
that doesn't work with business central
usually they can they know how to edit
an Excel sheet and they can update all
of the data uh and that's one of the
reasons why it's such a um popular
integration. So one of the things that
I've done in this uh tenant is that I've
installed an extension uh with the sales
forecast. So, I thought it would be fun
to um to do some kind of forecasting of
how many of these items are we actually
going to sell in 20 26 for example. Um
and I have the forecast data here and
what I filled out is all of the uh line
numbers uh which corresponds to the
items and then I've just done some
random number that we sold in 2023 and
2025 and then I wanted to try to use
Excel co-pilot to to give us a forecast
for 2025. And uh I've already um
prepared a prompt and it's exactly what
I just said. Uh so let's see if Excel
coil can help us with this. So hopefully
what it does is that it gives us a
column that we can just insert. But
sometimes it gives you a formula that
you have to apply as well. But I hope
that's not the case this time. Uh let's
see. Okay, so we're lucky. It actually
does give us the column. And uh what I
can do is I can take all of this and I
can insert it into a column that I've
added myself through an extension. And
uh I'll just copy this in here
and uh I'll go back to the addon and I
can publish this. So this shows one of
the ways that people who are very
comfortable with Excel, they can use new
co-pilot, they can integrate it with uh
business central even. So one of the
things that we notice here is that some
of the sales forecast is set to zero.
And I'll just show you the code for the
extension here. And uh I've just have a
normal page extension where I've added a
field sales forecast. And uh I also have
um a table field and it's an integer.
And uh then I added some on validate
method. And what it basically says is
that um uh if the client type is oat v4
then if the sales forecast is less than
50 then just set it equal to zero. And
it's just some arbitrary logic because I
wanted to show that even when you do
this through uh Excel, all of the normal
business logic is still being executed
if you do it like this. So you can
support all of the customer use cases
like this. Uh if they want special
behavior for Excel
um and uh let's go back to the addin. Uh
so one of the other things that I wanted
to show is that uh we have this uh
options dialogue in the addin. And uh
one of the things you can do is you can
change the language and the language
there actually corresponds to the
language inside of my settings. So it
supports localization and um you can
also change around the environments. We
have currently select the production
environment but you can easily without
reloading the addin uh change
environments and companies to support
that use case.
Um so what I thought now was let's try
to go under the hood. Um so this is just
a normal office addin. anyone could
actually go and develop an office addin.
And uh one of the things that we can do
to go under the hood is that we can
change this Excel file to a zip file.
And when you do that with Excel files,
you can actually see what's underneath
like what's embedded in the workbook
that we export from Business Central.
And uh one of the interesting things is
this uh Excel uh folder and inside of
that one we have uh web extensions and
we have tasks P task pes. So this is the
one of the things that does that it it
seamlessly opens a task pane when the
user opens the workbook and uh then it's
going to load the uh this the extension
specified in this file web extensions
and uh we can see that we are loading an
addin with an ID WA 104 and this
actually corresponds to the ID of the
Microsoft Dynamics office addin in the
uh office store. Um and then we can see
that we are seating a lot of properties
from Business Central. And uh some of
the values that we recognize here is for
example the uh the company down here and
the production environment and the
language that I just showed in the
office tab. Uh so there's really nothing
magical going on in the background. Um
yeah, I think that that's it for the
demo. Uh do you also wanted to show the
uh the changes to companies and
environments that you can do from the
workbook?
Yeah. No, it's okay. It's okay. Thank
you. All right. So let's shift back to
the presentation.
All right.
So the next slide. Yeah. Uh so this is
the add in Excel module and we're
hosting it publicly on GitHub. So anyone
can see the active development going on
in the module and uh anyone can
contribute as well. This is some of the
poll request of all of the latest
development going on. And uh I even I I
added one of my poll request that is
like in a draft mode and one of the
partners is Stek. I hope he doesn't mind
that I mention him but he's uh reviewing
my poll request when I open them for the
edit Excel module. So it's so nice to
see that all of the partners are also
contributing to making uh this module
better
and um okay and then to something else.
So how how can we extend the
functionality in this addin by using AL
extensions. So some of the things that
we need to keep in mind is that when we
send a web request uh through O data and
the API is um is backed by a page then
all of the normal triggers is actually
going to be executed just as if you had
a UI interaction just like if you
visited the the web client. Um and so
all of this logic is going to be
executed all of the complicated business
logic. And um then we can also
distinguish between what client is
accessing your extension. So if you have
some code in your extension and you only
want it to run uh through the API, then
you could for example distinguish based
on the current client type uh to make
sure that you're not doing a lot of UI
stuff in these triggers to enhance the
performance of the addin.
And um then you sometimes you have a
page like a worksheet page for example
that doesn't have the edit excel button.
we only add it by default to some
specific pages like the list page and uh
so this this uh code that I've um I've
added it's um it's like a helper
function uh to add edit an excel action
to a a worksheet page and uh what you
basically do is you take dependency on
the edit excel code unit and they take
dependency out the code unit for the
filters and um then you can add fields
and these fields that you're adding here
in the filters it basically corresponds
to the the filter the section of the
addin. Uh, exactly. So, this is in this
example because it's a worksheet page,
it makes sense to filter based on the
batch name and the template name. Uh, so
you don't just dump all of the data into
the Excel sheet for the customer. And
then eventually you'll call the edit
page in Excel and you also give in like
what is the page ID that I want uh to
base the web service based on that the
addin is going to connect to. Yes.
All right. So uh now I'm going to talk a
little bit about the backend
functionality how the OATA web services
are supporting this functionality in
total. So starting from the like the
start these are the integrations that
business central supports like any web
service uh that you want to any
integration that we want to have with
business central can be supported with
these three technologies. One is REST
API, another is O data and third one is
SOAP. Now as most of you should know
that SOAP is on its way to depreciation
and rest API and O data is the one which
we uh recommend using out of that Excel
addin uses O data. So we'll talk a
little bit more about O data uh and uh
some more details about it. So, ODATA
web services business central um have
been there for some time but just like a
primer ODATA is a application level
protocol which builds on top of restful
API interfaces.
It can perform C operations uh for your
data in business central and you can
expose your um objects like pages,
queries, code units as O data endpoints
and then interact with them.
And it has support for standard over
operators like filter, top etc etc. And
most importantly it also supports
operators like batch which is important
when you are posting in bulk like when
you're doing updates in bulk or deletes
in bulk. This is the operator that makes
it more performant and along with batch
operator if you do some u combine other
operators then it will basically be very
targeted. These operators are passed to
the server and then server is what takes
care of making sure that it is a
performant operation and I can explain a
little bit more about that. So uh the
documentation you can find it on this
link about O data services. Now what
happens when Excel addin is doing stuff
on the UI. When you have an Excel addin
and you are clicking a refresh button,
it actually makes a get call to the
business central environment to retrieve
the data. And when you're doing a
publish, it makes a post call, right?
And that post call is actually a batch
call which uh can do updates, deletes,
etc.
So, let me show you a little bit of um
demo about this data calls.
So, this is my environment. Just refresh
it.
Okay, let me start Fiddler.
So let's start from the place where
Matty uh demoed some of the
functionality. So I'm going to the items
page as well
and then I'm going to just open this
page in Excel.
So while the workbook is opening and the
Excel addin is initializing
it is doing all those stuff that I
mentioned on the architecture slide. So
it is contacting the business central
service to um get the configuration. It
is then contacting uh getting the
environments getting the tenants and
then basically trying to initialize
everything. So you can support a
particular environment with uh this
particular addin and at this point of
time it has loaded the data. So let's
see um if you can find the calls that
the addin has made in the background and
uh we we found those calls. So we start
with the metadata call. The first call
is to get the metadata that I explained
in the architecture diagram. So at this
point of time the metadata is helps it
to map from entities to the columns
right and then it ends up in getting the
get called to an entity called item card
excel. So this looks like a web service
to me. Let's go and find out if we have
that in our environment. So I will go to
web services.
And in the list of web services
I have this web service which is
item_card excel. So when you are using
edit and excel functionality
uh web service is created out of the box
for you to work with excel and you can
use the same work uh same web service to
do bunch of other stuffs. So um I'm just
looking at the API it is item card
excel. So let me go to a tool like
Insomnia
and if I use the same um endpoint to
make a call to Business Central, it is
this item card Excel. It should give me
the data. This data was used to load the
Excel workbook, right? And um basically
um this is how it works. So you can also
use the same web service to make post
calls and other type of operations
normal OD operations you want to do. Um
while we are at it I want to show and
tell you more about O data metadata
because it's uh it's essential uh to
have a little bit of understanding of
how it works. So O data metadata is
uh can be retrieved while an endpoint
called dollar metadata. Once you uh
retrieve the metadata, it will show up
as an kind of XML XML structure, right?
And this is the EDM model. This is the
entity data model that defines uh the
metadata.
You can see some entities like media.
Uh then you can also see some entities
like u company and they also have
properties associated with those
entities. And um going back to
talking about metadata,
it is represented as EDM model and uh to
query the metadata document, you have to
go to this endpoint and it's a
representation of service um data model
which is expose exposed for client
consumption. So client can be anything.
In this case, our client is Excel addin
but it can be any other client and it
looks like this. So I just showed you um
it has entities and properties. I want
to dig a little deeper into how this
metadata model is actually generated.
So um
when you call this endpoint at the
business central environment, we if we
don't have that model, we try to
generate it the first time and then we
cach it. Obviously we don't want to
generate it. It's an expensive
operation. We don't want to generate it
every time.
uh but while we are generating the
metadata model it starts with adding
some of the default companies like
company entity and some properties for
the company entity. Then it adds media
entity and add media properties. Right?
So these are two uh entities which are
added by default. Now it goes and adds
one of the web service entities that are
coming out of the box like sales order.
So when you log into your business
center environment, you see some web
services already there. Right? Some of
the web services are out of the box like
sales order and it adds the properties
for that sales order entity now when you
are opening a p list page in edit in
Excel it tries to add the entity for
that particular list page or that
particular entity. Right? For in our
example, it is item card Excel and then
it also adds the properties for item
card. When these entities are being
added to the metadata model, mind you
that if there is an error while you're
trying to add the entity,
then that entity is not available in the
model. So model has a list of entities
only the entity where the problem
occurred is not available in the model,
but rest of the entities are there. So
all your web services will keep on
continuing to work as you expect. But if
there is a problem in generating
metadata for one of the entity, it will
not be there and you will not be able to
call uh any web services for that
entity.
So why am why am I telling you about
this?
Uh some of the common pitfalls that we
have seen in edit in Excel functionality
is um customers try to open it open a
page in edit in Excel and uh for some
reason they say that this metadata is
not there and they get a screen like
this u the error is this error box error
loading metadata this entity was not
found or could not be retrieved or
something like that and this is most uh
common pitfall that we have seen And why
it happens is as I mentioned in the
previous slide, it was there was a
problem while you were adding the entity
in the metadata model.
And in most cases, the reason is you
have an extension where the property
name of the some page it actually
conflicts with the property name
mentioned in the base page. So if you
get such an error uh go ahead and do
check your extensions if there is a
conflict or not because due to the
conflict the entity was not added to the
list of entities in the model and that's
why your web service is not working.
That's why your edit in Excel
functionality is not working. Um this is
one of the biggest sources of um tickets
that we have. So just wanted to let you
know about that. And there is one more
thing which Matty wants to talk about.
Yeah. So let let's say that we for
example have a trigger like on modify
record. So let's say that you update
10,000 rows in the Excel addin. Then
this trigger is going to run for each of
those rows and uh let's say that you
have x amount of SQL calls inside of a
trigger like this. Then it's going to be
10,000 times x amount of SQL calls and
all of these small SQL calls inside of
the trigger is all going to the database
individually. Like there's no way to
optimize that kind of a performance. Uh
so if if you have code like this and uh
it's necessary for the application to
work then you would need some kind of
workaround where you tell the the end
user to filter out a lot so you don't
update that many rows at a time for
example or if it's only necessary for
the UI to have this trigger then you
could use some of the things I showed
earlier to to filter out based on the
client right
yes and these are the links which uh
tell you about known limitations in
metadata generation and it it might be a
helpful resource to find out some errors
in edit in Excel and some other links
related to troubleshooting web services.
So while we are talking about O data web
services and while we are talking about
edit in Excel, it's also important to
mention that uh about other types of
APIs that business central supports.
uh you remember the diagram that I
showed there are three possible uh
technologies that you can use to
integrate uh with business central one
is rest api and other is o data and
third is soap soap is on its way to
depreciation let's talk about o data
versus rest apis now when you want to do
a new integration we always recommend
that you use rest apis
rest apis are available through API
pages and they are tailored for
performance
So uh if you have a new integration
coming up do use rest APIs
and on top of that you the rest APIs are
built under the hood also as an O data
model. So you can also retrieve the
metadata for the rest APIs that uh you
have in the business central and which
also means that you can it supports all
the data operators like filter top batch
etc etc.
So uh I would say that rest APIs are
uh recommended for new integrations and
for very specific logic which is very
tied to your page then you have to use
the data. Another important thing to
notice is when you use O data web
service which is tied to the page, it
also executes the triggers on the page.
So if you have some triggers which are
not essential for um for any kind of
integration that you have you are having
then if the trigger is getting executed
unnecessarily and which leads to slower
loading of data in edit in Excel and
other scenarios. Um there is a way
around which you can use uh in your
pages like in your extensions. You can
probably use client type as O data v4
and then it can just um filter out the
logic only for client type uh UI or
client type or data v4. So you can use
that trick but uh importantly you have
to be mindful that when an web service
is tied to a page the triggers on the
pages are also getting executed.
So uh that was our content that was what
we wanted to show. Uh feel free to
contact us here and this is a small link
with all the integrations that are
possible with business center through
office. Do check out the video on that
link as well. Thank you.
And it's time for questions.
We have a question over there.
Um, so you showed that we can edit and
delete data from Excel uh in Business
Central.
How does the control set function work?
So if you make a mistake or you want to
go back, does it recreate? Uh sorry, can
you talk a little bit louder? Just So if
you delete the record in Excel from BC,
yeah, and you press Ctrl Z, does it
automatically recreate it or Yeah. Yeah,
you can get it back like that. But if
you for example delete it in Business
Central and then you uh close down the
workbook, then it's gone, right? So it's
a very fragile way of doing it. Okay.
Yeah. Thank you.
Any
other questions? Oh, yeah.
If I understand it correctly, then
you're technically creating tenant web
service for communication. Uh but aren't
uh O data tenant web service for
Microsoft pages duplicated uh or is this
a
that you are still allowed to create it
with your the web services you are
allowed to create it but it is not
deprecated. SOAP is on its way to
depreciation but uh recommendation is to
use REST APIs. know what I mean? I
thought few weeks ago they mentioned you
won't be able to publish a tenant web
service for a Microsoft page or for a
page that is contained in an app with
the publisher Microsoft
but or how do you handle this? I I don't
think that the O data web services is
getting deprecated anytime soon. Uh I'm
not sure. No, not the O data web
service. I think it's a setup. There is
a error in the system app when you will
add in BC29
or so uh or when you try to insert a 10
web service for page that is part of
Microsoft if if you send us an email we
will definitely look into it. Uh yeah I
haven't heard about it. We haven't seen
it. Do send me an email. Yeah, if you if
you came across something. Sorry.
Okay. Um, if you update the data from
Excel, is everything updated or only the
the columns you changed? Yeah. So, it it
it tries to only update the one row that
you're updating. So, it knows how to
optimize it in that sense. Okay. And one
more thing when we um enabled it for a
customer they went to the app source and
found the app but on the page of the app
there's only mentioned you need o data
service for dynamics ax
no word about business central so they
were a little bit confused yeah but
that's maybe yeah so the addin is also
used by other products so that might be
why the office addin on the page is not
mentioning anything about business
central okay But could add an mention
for business center. Yeah, it's a good
idea. Thank you.
Any more questions? You have it.
Uh so if I create a new table uh we call
it supercars and I want now my uh
customers to basically edit the data in
in Excel. So I need to create an all
data or rest API on the page. No, it it
will all happen automatically. Like
let's say that um you have a card page
and you have a list page that points to
the card page. Then the list list page
by default will have the edit angel
action up at the top. Okay. And the
connector on the side will be also
updated. Yeah. Yeah. Yeah. So it creates
the web service automatically uh every
time if it doesn't exist. Yeah.
Right. Any more questions
all the way up there? You can throw it
again.
all the way there.
Okay.
Thanks to Thank you. Um it's not a
technical related question but um
eventually you can open uh Excel again
and show us the the the addin because
you know in real life if you work with
the addin and you did a lot of changes
uh it occurs that if you put the data
back into the worksheet some error
occurs and then you got the error lock
on the right side of Excel and you can
have a closer look on it and based on
the usability it happens very often that
you close the full addin instead of the
error work after that. It's very hard to
handle to open the edin again. And if
it's possible, it seems to be that the
connection is lost and you can't still
continue inside of spreadsheet. So, can
you close the addin? Yeah. So, you're
saying if I click the exit up here?
Yeah. So, now try to open it again.
So, and that's based on on the user
experience.
Here
it works because in a demo environment
mostly the time it works but in real
life environment it's very uh happens
very often that connection is lost. Is
there a reason for that and how can I
just uh reauthenticate instead of just
closing the spreadsheet and start it
again? Yeah, it's very hard to answer
because I haven't seen that error
actually. Okay, so you just need a
screenshot on an email. Yeah, exactly.
That would help a lot. Thank you. One
one more. um since a couple of months
now. Sometimes it appears depending on
your regional settings that if you just
put data into an amount field of a
worksheet, push it back uh to uh
business central that depending on
different regional settings um business
central updates updated the the amount
field with a different amount that you
have um pushed to business central. It
seems to be based on I don't know the
point or the um the comma separator of
the thousand um formatting. Do you know
something about that? Uh it's very hard
with localization in uh in these add-ins
to make it work across uh like we
support the languages uh and uh yeah so
it's very hard when language like when
different regions they represented
either with a dot or a comma how that
works exactly but but I mean it was in
German environment it was in German and
it works for a very long time and that
there was a update and then it didn't so
okay I mean for for the user the problem
is um if you only have one or two lines
Yeah, I mean it works and you can see it
immediately. But if you um push I don't
know 20 or 100 lines to the worksheet,
you have to go through and it is
something like an incoming statement um
it's uh doesn't really help you to um
work more efficient. Um so push the data
back from Excel instead of just entered
manually. So eventually this something
you can close a look on it and yeah may
maybe an email would be good for that
one as well. Okay, thank you. You know
what happens with email. Yeah. Yeah.
Thank you so much. Thank you. Welcome.
All right. Any more last questions?
I think then that's it. Thank you.
There's one more question down here.
If you check out the Excel and make
changes and in the meantime someone
change the data in VC and you try to
publish it again um you get a message
you need to reload it but if you reload
this you lose all your changes. Is there
any option to keep my changes at least
for the items that were not changed in
Business Central? No, we don't have
that. Uh so I would suggest opening a
separate workbook even though it's kind
of a hassle as well obviously and uh
it's it's just because it's based on a
model where we try not to override data
that someone else has changed right and
then this is how we represent it with
the error. Um
but yeah right now there is no better
way. So at least it doesn't like when
you click publish and you've made
changes and someone else have changed
it. At least it doesn't remove and and
refresh so you lose everything
immediately. That would be even worse,
right? Yes. Uh at least you still have
the changes that you made somewhere. Uh
so I would probably suggest a new
workbook for that. Uh but we don't have
anything on the drawing board for I
haven't even thought about it actually.
So
yeah.
Right. Thank you.
So any more questions?
Okay. Thank you very much for attending
the session. Thank you.
