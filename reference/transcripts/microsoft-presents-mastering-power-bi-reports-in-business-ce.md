# Microsoft Presents: Mastering Power BI Reports in Business Central

- **Source:** https://www.youtube.com/watch?v=k-_vDWlC8Nw
- **Video ID:** k-_vDWlC8Nw
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 37m59s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Yeah. So my name is Joshua and yeah I
will be presenting about something I
have been involved with which is the
PowerBI reports story of how we
integrate with Business Central and yeah
so
okay
it says mastering but maybe I'm not that
much of a master right it's like mainly
like the the work of uh a lot of uh very
nice like great colleagues so it's all
the kudos goes to them right and But
still I hope that what I'm going to tell
you it's somehow useful and well
I wanted to start a bit like um yeah we
usually in the technical side tend to go
straight to the technical thing right so
I wanted to motivate a bit and to think
a bit of why would you like to start
using PowerBI if you already are a
experienced partner and already like
know how a lot of other reporting
solutions you have why should you be
interested in uh using it. So I'll go a
bit general but bear with me it's kind
of stating the obvious but uh just to
set the stage right. So at the primary
thing we have businesses.
So businesses are like what an ERP is
trying to help uh solve all their
scenarios and they have business
processes. So there is the first point
where uh ERPs can hold some value right.
So we have for example uh people that
okay sell something or that buy
something or that receive something in a
warehouse. So encoding already all these
processes in real life into the ERP will
already provide some things like okay
make sure to not forget what you're
asking for or make sure to just like uh
send an email after this is done right
so this is the first part where a value
of an ERP comes but out of all of that a
lot of business data gets generated so
you name it you know it right in
business center we have all sort of
ledgers so we have a customer ledger
entries and bank ledger entries And
yeah, you name it, there's probably a
ledger. And with this, this is the part
that I think that is like okay, the the
juicy part that we can do something
about it, right? Like a lot of value
from an ERP comes with from this, right?
The the fact that we can do custom uh
presentations of data. So, and that is
what I will be understanding as
analytics and reporting uh in this
context. So, what options do we have in
business central?
So
okay so historically right we we have uh
a lot of things uh we have uh AL
functionality for example I don't know
if you have seen uh of course you have
seen financial reports right is a
built-in AL tool where you can like
define like your own rows and say like
these rows has certain formula this is
how I calculated and so on and also for
the columns and this is inside the
product but there are also RDLC layouts
right if you define your own AL
extension and you want to define exactly
how you want to print something then you
can use an RDLC layout and be very
precise on how things should look. You
have also Excel layouts and word
layouts, right? And okay, given that we
have so many options, then why should
you consider PowerBI? So, it pretty much
depends on the use case, right? If you
like if you really are interested in
printing something, then probably our
DLC is the way to go. Of course, uh
if you for example want to download
something and do something with it like
the data and and the person that is
going to do something with it is not
experienced in business intelligence
tools and so so on then maybe an Excel
file it's the right choice but PowerBI
enables us uh with a lot of good
scenarios that I think it's very
relevant that all of us start learning
and yeah okay so concretely what I think
that is the value of uh using PowerBI is
that it's very easy to create powerful
and interactive reports that integrate
with a lot of the Microsoft ecosystem.
So you have a bunch of ways of sourcing
data into it, right? So and it's also
like a very good tool if you're like if
the companies that you work with are
serious with business analytics then
probably these people will know PowerBI,
right? So
good. So Oh, okay. Well,
just to make my point concrete, right?
Like what do I mean by powerful
interactive reports? So this is an
example. So this is an example of the
finance uh thing that we are offer out
of the box report that we are offering
and here we can say for see for example
the net profit of this Kontoso demo data
company and um it's not on oh
can I
okay so I don't know how to show
can someone help
Yeah.
Or
or do I have to stop the presentation
maybe and then
Okay, he's coming.
I I want to share like what I'm seeing
on my screen and this the part the like
switch off from the presentation. Okay.
Super like this. Just
Yeah.
Cool.
So, well, this is concretely what I mean
by a interactive report, right? So, you
have the net profit of this company,
right? And the net profit margin. You
can see how it was calculated. You can
see the revenue, the cost of goods sold,
and the expenses. And you can see by
month, right? So and by fiscal year. So
if you select one of these, you will see
that these values change by me selecting
them. So that's the kind of things that
PowerBI makes rather simple to do. Or if
you select this one, then you'll see
that these are the months involved in
this fiscal year, right?
And not only that, right? For example,
if I go to the liabilities one, then I
can see like month by month and I can
drill down if I am like skeptic of some
of these
and I can see okay what entries were
involved here and of course if you still
want to do something with them to like a
fast analysis and you can download this
data into Excel but this is a and okay
this is a very good uh way to explore
data and to yeah to do to do it in an
interactive way, Right.
Good. So
then
how do I do this now?
Where is this
5% view?
That works. Okay.
So, okay. So that was my sales pitch of
why you should start trying to use
PowerBI or learn about it. Um and now
I'll start with the goal of today. So my
goal of today is to provide you with a
way of like okay this is my deck of
slides. I will have a bunch of links
there so that you can like explore all
around and uh if you want to like prof
like go more deep into a topic you can
just uh dive into it. Does anyone know
what this map is?
No, it's the Lord of the Rings, right?
Yeah. So, okay. So, yeah, PowerBI is
like in Riendell like with the elves and
business central is in Mordor, but maybe
it's it's a coincidence of where I put
the Yeah. Okay. So, I I'll just start,
right? So,
first part like how do we extract data
from Business Central into PowerBI? And
this is a very general thing like we do
it as in any other API uh integration.
And there are two essential ways in
which we do this. First one is through
explicit REST APIs that's uh API pages.
And there's another one that it's no
code uh O data endpoints.
So I'll start first with the explicit
rest APIs. You are probably
uh familiar about with this right? In AL
extensions, you can define your own page
or query objects of type API. Then you
publish your extension and this will be
uh possible to be consumed as an API.
Yeah. Through HTTP and then um we as
Microsoft uh provide a set of default
ones that you can use uh but you can
also if you have your own custom tables
or you have data extra data that you
want to show you can provide your custom
ones.
So the built-in APIs that we provide so
the they are always there right in any
business central environment that you
have they will be available for you to
call so you can rely on them and we uh
maintain the fact that they will always
be there right uh there are v1s and v2s
use v2s v1s are deprecated um and here
is a link where you can see all the
things that we are providing right so
it's a nice list and you can say okay
how do I query GL accounts or accounting
periods and all these things
okay
and besides the standard that is the one
that I'm linking here there are many
others uh that are published as in
different first party apps that you can
explore so there's recently been added
some subscription billing and some on
sustainability and also well uh the ones
that I'm we are using for powerbi
reports which is the analytics ones
which yeah and okay so how do we call
these APIs this is an example you are
probably familiar on how to query it so
you have an environment and this is the
name of your environment right and then
this is how you query the this is the
group uh of these APIs v2 and then you
say companies and you put the system ID
of the company in the in the URL and
then you say accounts so you're
referring ing to the GL accounts inside
the company. Good. And then you would
get a JSON.
Good. So
custom APIs. So that's the ones that we
provide. They're always there. You can
use them if they you find them useful.
But okay. So you can also do your own.
So this is an example, right? So you
have an API page and it's like uh yeah
you can you can have an al page and you
can define define certain properties as
page type and then um API group uh API
publisher API version is the properties
that you need to set. So in this case it
was group death star analytics the
publisher is the galactic empire and the
version is version 1.0 zero and then
here you can surface whatever you you
want. So these are a bit so and this is
how you would query it. Right?
Good. So that's the explicit rest API
pages. If you have your own AL
extensions, you can publish your own.
And now what about this no code data
endpoints. So if I were to say like this
is the way you should do it. I wouldn't
talk about this but just to give you a
full overview and because there's
something with PowerBI there that you
should be aware of, I will talk a bit
about the no code or data endpoints. So
this is a way that we have in business
central to in a very generic way just
expose uh data that it's in any page
query your code unit. So it doesn't
matter uh if it's meant to be consumed
as an API or not. You can just make it
available. This is through the web
services page. Uh but we shouldn't like
okay we provide some out of the box when
we run demo tool. uh but we should be uh
aware that the names that these uh
that these ones have are considered demo
data right so maybe this is a bit too
small ah I can zoom so so these are the
if you go to a new company and you
search for web services you will see
this list and you will see some that are
powerbi related and this was something
that we used for some of the power the
first powerbi reposs that we have but uh
if did you find useful by all means you
can use them. Uh but be aware that these
names you shouldn't rely on them. Uh and
that also performance-wise it's not uh
guaranteed right they have bunch of
things. If you just expose a page and
there's suddenly a guey something that
requires GUI like a message or something
or confirm dialogue then it will just
crash in an API client. So be aware of
it.
Okay. So those are the two main ways and
now let's talk about actually PowerBI
right because this is generic APIs. So
inside PowerBI you can find the business
central connector as any other connector
you can go to get data find the
connector and find the environment that
is of interest according to the uh user
with which you logged in in the tenant
where you logged in and then you can
find the API and yeah
essentially get the data as any other
source.
So if you explore what uh code gets
generated when you do that and you see
in the power query editor you will see
this function dynamics 365 business
central API with content options and
this is more or less how you use it. Uh
well I didn't mention it but the other
three are deprecated. You should be
using the this one.
Yeah. So
the first parameter is environment name
then the company name then the API
prefix and then a set of options that is
some metadata that you can do use to
like customize how this query is
actually done to the uh business central
service. So this for example is used
specifying to use the read only replica.
You may be familiar with this concept.
It's uh we maintain two databases. Uh
one in which like the actual user is
interacting with and modifying and one
is a read only replica and it's just a
copy of it. And the point is that it
doesn't take any locks or any and it's
independent of the other one. uh if it's
important for you the encoding of what
is being uh returned the time out of how
long will I be waiting for this request
to complete and the paging right because
this connector will do uh paging on over
all the records the records and yeah so
once you have that as a source then you
can further filter down on the table of
your interest
and if you have a custom uh route you
can also specify it like in the previous
example this is how you would specify
the custom uh uh API prefix and also
worth mentioning these arguments can be
null they take the default values
good
uh now so there's also another part of
the story which is how do you visualize
these reports once you have published a
powerbi report you can go to
app.powerbi.com powerbi.com and you see
your workspaces and see all of it and
that's that's where you would see them
but it's there's also the possibility of
seeing them inside business central. So
we have uh uh allowed for a lot of pages
to service PowerBI reports. There are
many ways in which this can happen. Uh
this is the full page but there they can
also be in a factbox or they can be like
in a customer card and they can take the
context of the record. I won't go that
deeply on it but here uh I'm providing a
link in which there is examples of how
this is done. uh here Enrico has
provided a very nice uh basic ways of
how to use this and this is also
something that we want to further
improve
and okay so those are the tools in that
we have to integrate with business
central and powerbi so
the out of the box reports so this is
using those tools to provide some
default experience that you can already
use and maybe benefit from So these are
the areas that we are covering. It's
finance, sales, purchasing, inventory,
inventory valuation, projects,
manufacturing, subscription, billing and
sustainability. There is some links so
that you can see what they contain. This
is about like explicitly what each
report means and and what they measures
do they provide and if you want to
install them, you can find them in this
link.
So uh we'll go together through the
installation in a bit. So okay so this
out of the box reports they have two
main components. One is the AL
application that supports the reports
that's exposing all the API parts and
and so on that we have been talking
about and the other part is the PowerBI
side which is the PowerBI template apps
about the AL application. So this is
very roughly the architecture of it. So
this is the PowerBI AL app on top of u
all of our other apps. for example bas
it is exposing the Microsoft analytics v
0.5 end API prefix that is consumed by
the template apps
and in order to know what to return it
uses information from the entities it
uses setup that we can configure for
example the amount of uh data that we
want to restrict uh for if you have too
much data you may want to limit on dates
You also have we also have this concept
of dimension flattening right now. So if
you know dimension set entries you will
know that yeah it's a table that has a
bunch of entries and many of them like
refer to the same. So what what what
it's currently done is that it's being
flattened inside business central and
then you can just query that without uh
yeah and the relationships would work a
bit nicer and it's also saving some
processing time. There's some talks we
maybe want to move this flattening into
the PVIX side but yeah it's it's uh
still being decided and the other part
of the application is these uh AL pages
that has that have all these embedded
things. So already in business central
you can just open them and see them.
Okay. And the template apps.
So something important that you well you
the template app uh cannot be directly
like modified and that is maybe not the
best if you want to customize it for
your own company or your own business.
Uh so that is uh the reason of al also
open sourcing these pbixx files. So you
can also just download them and see uh
exactly what each measure is, how it's
calculated and how the queries work. And
yeah in in this link you can find the
first tree. It's the inventory,
inventory valuation and finance.
uh but it is planned that they will
leave inside uh the AAP that it's they
contain to avoid problems with version
dependency but this is still something
that we are planning on how to properly
open source it and welcome contributions
as well. So the main components of the
template apps are the semantic model for
the problem domain that we are solving
the measures for the common KPIs and
metrics of the domain and some uh
theme for it. So just to show it very
quickly, this is an example, right? This
is the semantic model. If you know
PowerBI, this is how we model things and
this is how it figures out what things
to highlight and so on. And there is the
list of these measures that you can also
see how they are calculated.
Right.
Good. So they are there. You can
download them and if they don't work or
you want Yeah. So okay, enough enough
talking. Let's just try to set up a new
company.
So
good. So here I have
a company. Uh I have two companies
actually. So well there's of course the
demo ones but they I also have two other
companies. The yeah a health company and
the laboratory company. Okay. So I think
here I already have
yeah the PowerBI uh report set so I can
see them but I don't yet have them here.
Right. So let's go through the
installation.
So first I'll go to PowerBI connector
setup and this is because this is the
easiest way for me to find at least
apparently the link to where the uh
PowerBI apps live. So these are the apps
that need to be installed in the PowerBI
site.
So if you scroll down here, you will
find that for this version or 26.2
version, you can install it here and so
on. So let's go and install the
inventory one.
Okay. And and I had already installed
the inventory one for the other company,
right? So this is a different company
that wants to use it. So I can override
it if I want. No, I I want to install uh
install in another copy of into a new
workspace. So I will just install it uh
into a new workspace and I will call
this inventory for clinic.
So now it's installing the app. And
while this is done, let me Yeah. Okay.
Maybe we can wait a bit. I don't think
it will take that long.
Yeah. Okay. So this is the new one
and you open it and currently this is
not linked to the business central
instance that we have defined. So in
order to connect your data you can fill
in the parameters and in so it will warn
you here right like it will say you're
viewing this app with sample data
connect your data. Okay. So how do you
do that? You in the PowerBI connector
setup, you have the connection details,
put the company name,
you put the environment name.
Be uh aware that you have to set the
privacy level for this uh to whatever
makes sense for the data that you are
sourcing.
and then it will start refreshing.
Right? So while this is happening we can
go to the workspaces.
Um yeah
because this is like if you face
problems if there's errors this is like
where you would find them. So if you go
to the workspaces you can see the report
you can see the semantic uh model and
this is the one that we can uh set
properties. So by default it will
schedule once a day but you can reschedu
uh or set your own schedule. So if you
click the three dots next to the
semantic model you have a lot of things.
So for example the refresh history.
So this is the one that is being done
that it's actually now already finished.
And if you need to open a support
request or something like this, then you
can see it here. Uh the kind of
information that might be useful to
understand what's going wrong.
Uh
yeah. So with that then we should have
uh
yeah the company name is set to the
company that we just connected to and
this is all information that is was
retrieved from API pages from Business
Central. here and now in order to see
them inside business central. So in
order to see them inside business
central we can go here to PowerBI
reports and say okay inventory location.
So at this point uh we haven't set up
properly the reports here in this
company. So it will just guide me
through the wizard. It will ask me to
check the PowerBI license. you need a
PowerBI uh pro license in order to uh
schedule the refresh
and see the reports.
So this is the part that sets up the
connection and then it's the part that
sets up the uh specific uh reports out
out of the box reports. So you can set
several things that influence for
example how the date table gets
generated in PowerBI.
um
yeah the the date table range that you
should cons that should be considered
and stuff like this. So here is where we
link back right. So this is where we
link back the the reports that we just
installed uh into business central. So
this is how business central will know
which thing to show from which from your
uh workspace. So in inventory report you
can just say let's see and these are all
the workspaces that I have there. So
this was the clinic
ah it's the first one okay
and then inside you can see the report
and that is enough for now. Ideally, if
you install all of them, you can just
configure them there and that's it. And
then it will open the page and it will
load the page for that company. Right?
So, this is for this company that we
added.
Okay. And if you don't, of course, the
wizard will just go the first time, but
then you can go to PowerBI connector
setup and these settings are still here.
Here's where you can set them up and
other things, right? Like I was telling
you about this setup like the PowerBI
account categories. So
you will see some metrics like what what
how does it know which account is mapped
to assets and so on. So this is where uh
you can define these things
and yeah and if you want to limit the
amount of entries be aware that like it
is rather solid but it can still time
out like itself the PowerBI service. So
we recommend at least uh a lower volume
to do the initial uh population of data.
So that's that and just because it's
also something that because okay so you
you can have reports like this but you
can also have uh well I showed you that
you could have for two different
companies the out of the box reports but
you can also have multi-company reports
and that means uh embedding information
from two companies inside a single
PowerBI uh report.
Oops.
So this is a small example and I have
also uploaded this one in uh visit text
repo
just to prove the point right I for
these two companies that I set up I can
select
the BC companies
and based on what I select I have
different set of customers in each of
them and this is a different revenue so
how did I do this so we can maybe
uh yeah I won't go that thoroughly into
how this works, but I think it's uh
like in the in the M code. I mean,
yeah, let me wait a bit.
Yeah. So, here is where I define the
companies that I want to consider from
uh my environment, my a tenant. So you
can edit which companies by doing this
and then you would add more if you have
more.
And then how do you do the cross company
data? So for example the customers. So
if all the customers are different for
each of the companies then you can just
uh so if you see this table has
information for both companies. So you
can see the company name customer uh
number for this company but there's also
a customer number 10,000 for this other
company right so they are all merged
there so if you want to see how that is
done you can go here to the advanced
editor and this is like an example that
I have uh example M code for doing this
so
what I would like recommend like of
course you can do it like manually uh by
going it would work just fine if you
just select each of them and just select
the company and see it and then you
would do table combine or something like
this but you can also do use like copy
this thing this helper functions that
I've done and then the way that you
would use it is like this so you would
say expand the table and you will see
say which are the companies table that
you have as your source and then you
will just say how do you get that table
which is this table in company this is
is a prefix and this is the table that
I'm looking at. And by doing that and if
you have these things above then it will
do what I just showed you that it just
merges there and goes through each of
the companies and merges all this that
data.
Yeah. So those are the things I wanted
to show you. There are many areas of
opportunity here. I don't consider this
work to be done and we are constantly
evolving it. So we you saw that this set
of experience was a bit like I'll do a
bit here then I'll go a bit here and
then I'll go back a bit here. So we want
this to be much more smooth. We are
currently like seeing how to in out
install right and stuff like this and
also a better troubleshooting
experience. Right now there are many
pitfalls that if you don't know it's a
bit hard to figure it out and there is
more content planned as well and also uh
in general a better developer
experience. Right now we have pieces of
code here and there of the AL code. So
we could certainly improve it and
certainly make it easier for you to
extend. And if you have any ideas just
like let me know and if you recognize me
and you have some something just
tell me. I yeah we can make it work. I'm
not as brave as Haras to put my email on
the slides but I can happily give it to
you. I'll just uh yeah just ask me and
of course so frequent asked questions
before we jump into the general
questions I gave you the multi company
example that is one the licenses that
you need you do need powerbi pro for
this um and on premises are not support
by default but since we're giving the
pbixx then you can explore with that
right you can use the connector because
we do have a connector for onrem so you
can use that connector and use reuse use
the semantic model and the measures and
try to see but by default we are not
supporting it.
So yeah.
Okay. Why? Damn it. Okay.
Say okay. Yeah. uh you say that uh we
need the PowerBI pro license
but for using it yes as far as I
like I'm uh I'm managing it to create
this thing but if I'm a simple user do I
need a PowerBI
license to see the report inside
Business Central? Yeah.
So
we can try it out a bit like I can
verify it as far as we have it in our
documentation. We do say that we need it
in order to consume them but um yeah I I
can check it in a bit. So if I'm a
business center user without PowerBI
um license I cannot see the report.
Yeah. Okay. Just that.
Oh, that's a long throw.
Okay, I'll start. Uh, you mentioned a
replica database for getting
information. uh is that runtime um uh uh
information uh or is it a daily backup
uh I actually don't know the details of
how this read only replica but I know
who to ask so I can uh get back to you
with it I I I don't know how often it
happens to be honest okay thank you
uh just a quick question did you did you
have a chance to check the performance
what for example if you take the
ledger table and he has I don't know 10
million records and you pull it via API
how what's the
so that that's a big limitation we do
have a lot of customer cases that we are
trying to yeah they basically it times
out right so because it's in the end
doing a lot of uh HTTP requests and even
if they are paginated by 10,000 it will
eventually time out like by the powerbi
service that is calling it itself so
to mitigate that we can like do the we
have the actually I can show it I think
I I showed it we have the way a way to
limit the entries and at least for the
initial import we could like limit it
and then we can uh go from from certain
date onwards but uh yeah I do admit
there's there's something we can we can
do to improve in the data volume
and you have shown us the multi company
uh support But for example, if you have
the same customers in two companies, you
can merge that and show the uh revenue
from both companies for this exact
customer. Yes. No, no. I mean what I
showed you was also like an example
because we get the question often but
the things that you mentioned is exactly
why we cannot provide something out of
the box, right? because some C customers
may have the different names in but it's
actually the same in different companies
and this consolidation process is not
something that we can like adventure to
say this is how we should be doing it
right so it's very much like case
dependent so
it would be up to like the the person
that is trying to define these reports
to know how to handle this so I could
think for example of having a um set of
matched customers right and then try to
build queries is that like use that
information in order to do that. But
yeah, this was just the example. Yeah.
Okay.
Yeah. Uh
okay. It's it's a bit crazy throw but
okay.
It respects the permissions. Yeah. Okay.
The question if you of course you not
didn't know here uh it's about
permissions and uh whether it will
respect the user permissions and it
respects so
yeah so
the user that schedules the the refresh
it will respect the the permissions of
the user that schedules that refresh.
So, so if admin access has access to all
companies, the user that is accessing
the data will have the same access as
admin. Yes. But uh additionally, right,
we also provide permission sets. So in
business central, if you want to just
limit what they see inside business
central, then you have the regular
permission sets for the pages and then
you can limit there. For this company,
you can only see these pages. But of
course, nothing stops them from going to
app.powerbi.com, right? But yeah, it is
something that you should uh yeah limit
uh like from the BC side. Yeah. Okay.
Thank you.
Anyone else?
So that's it I think.
Okay. Thank you.
