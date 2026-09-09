# Microsoft Presents: Mastering Contoso Demo Data in Business Central

- **Source:** https://www.youtube.com/watch?v=9Spb-4tYePA
- **Video ID:** 9Spb-4tYePA
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 39m37s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Ladies and gentlemen, for the next 90
minutes, we will have two speakers on
stage. Our second session is hosted by
Joshua Martinez with Mastering BI
reports in Business Central. But first,
get your hands together for our first
speaker of the day, Hyron Sun with
Mastering Contoso Damate in Business
Central.
[Music]
Hi. Hi everyone. My name is Haram. I'm a
software engineer from Microsoft and
this is my first time at Tech Days. So
I'm very happy to be here and to give
present you mastering Ktoso demo data in
Business Central.
And before we get started, let's test
this cool light we all get. How many of
you have worked with demo data in
Business Central before?
Okay, so that's actually many of you.
And how many of you have already played
around with Contoso demo data?
Okay, also quite a few people. That's
great. That's great. We will try to
cover both audience and we
work through it.
The agenda for today, we will first go
through the previous demo tool we have
in business central.
We give a brief overview of what's going
on and what's the future for it. And we
will give a quick introduction on the
contoso demo data overview of what the
tool is and what's the feature. And
we'll spend most of our times to build a
demo data module from scratch. So we all
learn how to build a demo data module
for your own customers. And finally,
we'll reserve some time for questions.
So the previous demo tool we provide you
is rapid start practice. Those are the
files you get in those brand new
environments.
I try to highlight the previous word.
Okay, it's visible up there. That's
great.
I highlight the previous because we are
moving away from this approach
for a few reasons. First one, it is a
monolith approach for demo data. You get
one file. It is not a trivial effort to
split this file into different modules.
Most of the time you either import all
demo data or no demo data. It goes
against the componentization we are
working in business central
and it is also hard to maintain. So
there is a few reasons that make it
difficult. First one is localizations.
For different localizations you want to
populate different tables. Then you need
two packages because different tables do
not exist in different localizations.
And version control is hard because it's
a simply file based system. So it's hard
to do version control. And translation
makes it even harder to maintain because
you need different files for different
translations. And finally upgrade is
hard to handle because unlike VS code
you get warnings says this table is
going to be obsoleted in couple of
waves.
It's simply a file sitting in your
computer.
And this is how we imagine you could
look like after a couple of iterations
working on demo data um to update
certain customers or vendors. and it
gets very ugly very soon
and for those reasons we worked towards
Contoso demo data
to address those issues and first of all
I'm very very happy to tell you that
from version 25.3 so it's already in
production we Microsoft internally have
completely migrated to conso demo data
that means all the environment you get
today all the SAS demo data are powered
by Ktoso including the demo we seen in
the keynote
and this is because we have a modulized
design in demo data Ktoso we separate
all our our demo datas into different
scenario based units
so each module can work separately and
together so if you like what Microsoft
shipped all of the data then perfectly
fine you get all the data or if you only
want to service scenario in your demo.
That's also all right. You don't need to
see all the data from different
scenarios that you don't intend to
present.
And what's more, we separate each module
into four data layers. This is to help
you further separate your data into
different chunks so it's easier to
maintain.
And we also support dependency. So you
don't have to copy paste your code
across different modules. If you need
some posting groups in the finance
module we provide simply take dependency
on it and we will generate the demo data
for you.
And there's a couple more things with
Ktoso. All the demo data leaves in your
repository as code
and that naturally brings some benefits
like so version control will be like g
source control like your any of your
other code. Translation is
straightforward as well just like how
you translation
labels nowadays.
We also built Ktoso demo data with
extensibility in mind so you can build
on top of what we have shipped
and we also packed in a few features to
help you speed up your productivity so
you can focus on building your demo data
scenarios.
We also offer some configuration.
So you can configure the demo data to
target
the end customer you're demoing. So it
feels more personalized
of what they're doing. And finally all
the code are open source at AO app
extensions repository.
So feel free to go check it out and
click around and see how we build
everything.
And here is a high level architecture of
how Ktoso demo data looks like. So at
its core is Contoso demo 2. The tool
itself does not contain any demo data.
Think of it orration engine that
includes the uh interface definition. It
includes the logic for dependencies and
things like that.
And on top of it, all the demo data are
built into modules. So here is a very
simplified view of how it looks like. We
have warehousing module and
manufacturing module that built by
Microsoft.
They are all separate modules.
And imagine your partner A that you do
not like whatever is shipped M by
Microsoft. That's perfectly fine. build
your own module directly on top of the
demo tool and then you'll be able to
generate your demo data without all the
distractions
or your partner B you do like what
Microsoft shipped out of the box but you
would just like some more additional
demo data so you can further demonstrate
your scenario
simply take dependency on the
warehousing and manufacturing scenarios
then those demo data will be generated
for you.
And let's do a quick recap.
Our plan is to stop shipping the Rapid
Star packages in the future. We have not
set a date for it yet, but this is our
plan that to completely migrate away
from the rapid star package based demo
data.
And we have internally fully migrated to
Ktoso demo data since version 25.3.
And because of its modulized and
extensible design
and next we're gonna do a bit more
hands-on very technical part. We'll
build a demo data for a shoes company
from scratch. Um I have uploaded all the
source code on BC tech repository. If
you're not familiar with that repository
here is a QR code uh that helps you
redirects you to the source code. Um you
can play around it and if you don't have
a chance to take a picture don't worry
um all the slices will be uploaded.
Yes. Before
diving into the code
I want to give the same advice that I
gave internally for Microsoft engineers
as well. When you build a demo data
module first explore what data has
already been generated in your
environment.
Click around and go to customer list,
item list and see what data is already
there. So you might find some things has
already been generated that fits in your
scenario. You don't have to generate
those datas. Take dependency and you'll
be there
and work through the scenario you want
to build manually. Create a customer,
create an item and create a sales order
using those customer and vendor and
items. And this way you have a clear
understanding of what data you need to
create.
Now let's dive into the code.
So get to get started is very
straightforward. Create an app. Take
dependency on Ktoso demo data. Extend
the enum and implement the interface.
I will swap into the code. Just quickly
check. Super. It looks all right. So
here I have a fairly blank app. Um I
have to admit I cheated a bit. We're not
going to do live coding here. All the
code I have coded uh beforehands.
So in the app.json nothing magical add
dependency to conso coffee demo data set
the app
and remember the version it has to be
bigger than 25.3 to leverage full power
of kto demo data. The app exists before
but we do not have that much feature
yet.
And the second step extend the enum on
top of Ktoso demo data module. This is
to tell Ktoso, hey we have a new module
called Ktoso shoes. Uh we would like to
be used by you
and implement the interface. It's also
straightforward. Autocomplete should
give you those blank procedures you need
to implement
and we will work through them one by
one. And so far we already built an
empty app that's actually already
publishable to um to the environment but
simply a demo data module that does
nothing.
So the next step is to find the
dependencies you want your module to
depend on. So by this stage you should
already know what data you want to use
when you click around the environment
and find those data and figure out which
module they belong. So you can take
dependencies
and let me check in the commit for the
next part.
Very simple. We have implemented the get
dependencies procedure. What it does is
we're giving a list of dependencies.
We're saying we need to take dependency
on the foundation module. And this is
because we need number series generated
from foundation module. We also take
dependency on the finance module. This
is because I would need to use the
posting groups generated there.
At this point you may think this is kind
of cheating. You are very familiar with
the codebase then of course you know
what demo data is generated in which
module
but worry not for
those who are not familiar with the
codebase jumping to the definition of
the enum. You can see a list of demo
data modules we provide out of the box.
actually all 17 modules so far
and you can easily jump into each
module's implementation to see what data
is created where.
And another
easier thing to do is let me go to the
definition of customer table.
Here we go.
This is definition of table customer. So
you might need a module that generates
data for customer. How do you know which
module is that? Scroll all the way to
the up
and you can see the name space is under
sales and that is why the customer data
is created inside the sales module. So
inside Ktoso we try to split demo data
according to the name space defined in
business central. So this way you can
get a general direction to see where
your data is packed.
Good. That's
all the dependencies.
And next we're going to create some
setup data of our own.
And this part we will use some thing
called helper code units that helps you
to easily insert demo data. Let's check
out the commit.
So here I have two code units that
insert demo data. I want to sell shoes
in my company. I want to sell shoes in
pairs. I do not want to sell only one of
them. So I create a new union of measure
called pair.
And the first thing to notice is this
procedure called insert union of
measure. This procedure is not defined
in this app. If we jump into the
definition,
you can see it is actually defined in
the demo tool itself. So inside control
demo tool, we ship a list of helper code
units that helps you insert data. So you
don't have to worry about all the
details inside. All you need to do is
provide the parameters and we insert the
data for you. And the logic is fairly
straightforward.
Let's just read through this procedure.
What we are doing here, we are checking
if the union of measure record already
exists. If already exists and we do not
want to override the data and the
procedure simply terminates
and if it doesn't exist, we will make
sure to assign the value to the record
in appropriate order and insert the data
for you. So those are some of the
productivity points we provide for you
so you can focus on building the demo
data scenario
and let's go back to the file. Another
point in this file to notice is the
procedure pair. So if you jump into the
jump into the definition here and you
can see this procedure is simply
referencing a label inside this file. So
you might be wondering okay why don't we
just simply refer to this label instead
why do we need to create a procedure and
this is one of the most important design
we choose in contoso is that for all
records you want to insert make sure to
define the primary key as a procedure
and in a descriptive way here we call it
pair so it is easier to reference
between files and later on we'll move to
master data
So you can simply call the procedure
instead of defining the same label twice
and then you have to keep them in sync.
And we what we also insert an item
category called shoes
very similar pattern as you can see
very straightforward.
So that's how we insert setup data. We
imagine setup data will include datas
like um jail accounts, posting setups,
posting groups, number series and things
like that.
The next step we implement is master
data. For master data, we imagine it
will contain datas like vendors,
customers, items and things like that.
Those data are a bit more complex
because they need to take reference on
the setup data we have just created or
setup data from different modules. So
let's take a look of what it looks like.
Check out the commit.
And here we have
the
first mask data. We're inserting some
shoes items.
And this file looks a bit messy, but
don't worry, the main content is very
straightforward. So, we're inserting
some items called sneakers, some
flip-flops, and some boots. Very simple.
All the rest is reference calls to other
data. What I want you to pay attention
is that in this file, we do not have
many hard-coded data. As you can see
here, first the gem product posting
group is actually created in the finance
module. We're just simply referring it
here. So we don't have to create it
again. And it's important that we use
procedure references instead of
hardcoded data. So you only have one
place to maintain it.
Okay. So we inserted some items. So for
all the shoes we just created, I would
like to insert some different shoe
sizes.
So for for each shoe, I give it two
sizes.
For 26 cm of the shoes, I give it a
description called UK 8.5 size. And for
27 cm, I give it description called UK
9.5.
And this is interesting because
um the data is only suitable for a UK
company. But what if my sh company was
very successful? I expand my business to
Belgium for example.
Now it brings us to the localization.
In Ktoso demo data, we take localization
very seriously because we as you may
know we maintain around 20 localizations
internally and as a matter of fact we
have 20 kontoso apps for each
localizations as well but we do not want
to copy paste our code 20 times. We
provided some features like the ktoso
coffee demo data setup. It's a setup
table that contains some of the fields
and values that you will find useful in
localizations.
And we also have some powerful events
defined in contoso demo to code unit
that allows you customize the data you
would like to see in different scenarios
and including localization.
Let's take a quick look how we managed
to make sure the company works in
Belgium as well.
So ideally this file should exist in a
separate app in the different
localization but here for convenience I
just define it as a separate file.
The first thing to note is the
record ktosu coffee demo data setup.
Let's jump into the definition.
As you can see here, it is defined in
the demo tool itself.
And in this table, we have the most
important field in this scenario is the
country and region code here. So when
you provision a new environment, this
field will be already set up for you
what localization it is. So you can
utilize it to determine which context
the code should be able to run on. We
also have some other powerful fields
like company type, is it v or is it
sales tax and things like that.
I will fold that here.
And as you can see this is a event
subscriber
to the code unit control demo tool.
There are two main events on before
generating demo data and on after
generating demo data.
For those two events, you get some
parameters. So you get to know the
context. You get to know which module we
are currently running. You get to know
which data level we are currently
executing. You can read the code like
this.
We're currently running demo data for
Ktoso shoes
and we have just finished generating
demo data for master data. So now I
would like to override the data so it's
suitable for my Belgium company.
I check the setup data setup table is
set to Belgium. If it is
then I tell the helper coordinates
if the data already exists I would like
to override the data.
I filter on all the shoes items I have
created
and I use again the helper code in to
override the data but this time I
specify I don't want UK shoe sizes
anymore. I would like to use the EU shoe
sizes.
And that's how you do uh localization
for uh to override some data in
different localizations.
And before we go to the next step, let's
go back to the implementation and see
what we have done.
We have taken dependency.
We have created some demo data for setup
data and some data from master data.
We also support to insert transactional
data. Those data are like social orders,
purchase symbols, item journal, things
like that.
And we also support historical data.
Those data are gel entries, posted sales
order or even some forecasting um you
have in your solution. We will not go
through those two procedures today. The
insertion of data follows a very similar
pattern.
And at the beginning here you can see we
have a configuration page procedure.
will also not implement here but we will
show you in a demo if how it can be used
in your scenario. So you can generize
personalized data
and let's switch to a quick demo of what
we have just built
and see how configuration works.
So here is a uh blank company completely
blank. uh we can quickly see a number
series maybe to verify I'm not lying
there's no data in this company and we
search for Kontoso
demo to page but this page when it's
open automatically load up all the
modules available in this environment
and at the bottom of the page you can
see we have Ktoso shoes
select the module and hit generate you
will insert all the data for you pick up
those implementations
and as you can see that finance and
foundation module has always also been
run. This is because we take dependency
on them. So they are also run to
generate the data.
And let's see all those cool shoes we
have created.
And here they are some of um shoes and
boots uh we have created.
And if we open those items, we can see
the union of measure is correctly set to
pair and item category code is also
correctly set.
And let's go to the item variance to
check the shoe sizes we specified. And
here you can see that we have size for
UK.
That's by design. And let's see
what if the company now expand to
Belgium.
Let's me select the correct company.
So now we switch to a Belgium company.
Again we go to Ktoso demo tool. And here
what's important to notice is to first
we go to Ktoso coffee demo data setup.
In this page, you can specify some of
the fields we just seen. In this case, I
want to change the country and region
code to Belgium.
And we select control to shoes again.
And we hit generate.
And now the control shoes data will be
run with the localized data. Again we go
to items,
select one of them and check the item
variant.
And here the description has been
correctly set to the EU sizes.
And this is what we have just built.
Let me quickly walk you through how it
will look like to do the configuration.
That is a power for tool that we
envision that you will use to generate
personalized data for the scenario.
Imagine you have completed build your
demo data but you would like the data to
be generated that's more suitable to the
customer you're going to demonstrate
tomorrow. That's all right. In some
modules you do not have to define the
configuration. For example, the bank
module does not have any configuration.
That's also okay. But for warehousing,
if you hit configure, you'll be able to
see there's a few options that allow you
to fill out. So in this scenario, if you
don't do anything, the module will
generate, but it will use some items of
its own provided in the module.
However, if you specify all the shoes we
have
just created now, the whole
manufacturing scenario will be run using
the items you have just provided.
This is going to take a while, but um
the idea is
you'll be able to demonstrate the
scenario using the personalized demo
data.
We will not wait for it to finish.
And we have saved some time for Q&A
before we switch back to see um what
data has been generated.
I got this cool tool. Uh perfect
already. Uh let's see if it works. I can
through it. Well, perfect. So, okay. Uh
maybe I'm wrong but in the past with uh
the standard demo data mh I never found
cost accounting
part cost accounting module. Yeah. Is
this fixing also that part or we have to
create our own uh cost accounting data?
That's a good question. So with the
ktoso demo data effort we did not
implement too many new demo data. What
we did is to switch to the underlying
engine to the new ktoso approach. So
most likely the demo data stays the same
as before
but that's a good idea. We can submit on
maybe BC ideas and we will work on it to
provide something out of the box. But
alternatively you can build your demo
data on top of kintoso as well. Yeah.
Yes, of course. But it's something that
we I have to spend time too. So, uh it
would be better if Microsoft can provide
demo data for each modules because uh
because accounting is something that is
very useful but creating demo data it's
time consuming. So definitely definitely
so if you can do it please do. Yes. Yes.
We were keeping that in mind. Please
submit an idea maybe on BC ideas. So we
let's try throwing as well.
Hey, can this mechanism also be used to
make like uh template uh companies if
you have like uh you're in a in a
certain business and you have a lot of
small customers mh using the same kind
of uh configurations that you can just
provide an ABC and you just choose okay
I want to run a company use not for demo
purposes But really like what you do
with initializing a new company with rep
start. Yeah, that's actually a a good
point. It is definitely possible. As a
matter of fact, right now many of the
when you provision a new environment,
you get one kronis and one my company,
right? And with the my company, the idea
is that we will only run the setup layer
of the data. So you can already kick off
a production company. And I think that's
definitely a possibility with this tool
as well to generate some templates and
um not for demonstration purposes but
already for production. That's
definitely possible.
I think that uh you showed some code
where you were were creating units of
measure. Mhm.
um when they were not there already. I
think uh I saw you were not calling the
init method on that record. Is that on
purpose? That's actually a very very
great question. So when I was coding the
whole process, I learned uh the in need
um actually doesn't do much when the
code is when the variable is defined
inside the procedure. Um at least that's
um what how I understand it. So that's a
really good question. At the beginning I
did the init but u u my colleagues told
me actually it does doesn't do much. I
think you should implement that. So you
think that's a better practice to you
also showed us a table where there was
an init value. Yes, that's true. And
that will not be inserted if you are not
calling the init method. Yeah, that's a
good point. That's a that's for another
session. Yes, that's a good point. I
would look it up. That's a That's a good
feedback. That's a good feedback.
And we have more questions there. Yes, I
have a question. Do you support uh
adding additional fields from table
extension using your data? So, for
example, I have an item. I want to
create it my contoso demo data, but I
need to add additional field. Mhm. Yeah,
that's also a possibility. Um so I think
there's first way is to do it is through
the helper coordinates but obviously we
couldn't know what um fields are there
given our base app. So what you could do
is to define your own helper coordinates
that's a wrapper around ours and but add
some additional logics. So this way you
can insert data that tailor to your
scenario or you can utilize the events
we just talked about on after and on
before generate to populate the data for
your scenario. And also actually um I
would suggest to check out some of the
apps in a app extensions. We do have
some apps that's facing the same problem
because there are some add-ons on top of
the base app. So they also need to
populate some custom fields. So check
that out. Thanks.
U
quickly just two questions. So for me,
if I understood this properly, it still
seems like you're hard coding the data.
So for example, if I have 20 uh sizes, I
don't know, UK, 9, 10, and so on. I
still have to create the labels for all
of them. Yes. So it's basically hard
coding more or less. Wouldn't it be
better just to have like a text file and
then pull all the data from text file,
insert it that way? Well, that's more
similar to what we were doing before.
The problem with the text files is that
they are hard to maintain because
they're simply not code. Well, you
they're also kind of hardcoded in
somewhere, right? And with when we
hardcoded in the code, it will be
version controlled and simply like any
other field. But definitely that's also
a possibility especially with the new
resource files feature. I don't know um
if many of you are familiar that's a new
capability we provide that you in the
app you can load some resource files
that's how we insert the images actually
um so you can quickly check out the code
um so if that's your preference um
that's also possible. Well I'm asking
because we are in ISV so we have I don't
know something around uh 300 tables.
Yeah. uh and if you want to create uh
like a demo data for 300 tables, you can
imagine it will be quite a lot of work.
Firstly creating all the routines which
inserts the data into this one and then
also creating all the labels for
different fields that you want to
insert. So it's a kind of a full-time
job for I don't know half a year. Yes,
but the good news is I only need to code
it once and um hopefully in the future
you can maintain the code and reuse it.
But definitely you could try to use
files to populate it. I think we have
some examples in the demo data to
populate. I can't remember what exactly
is maybe currencies. Um we we are
reading the files as well uh to populate
certain data that we do not want in the
code. So that's also a possibility.
Okay. Thank you.
Oh, we have a question there and um I
guess we'll try to make it work.
Careful. Perfect. That was a good throw.
Um, will the Contoso demo data also be
used for the automated testing or at
least the helper functions to create the
data? That's really a excellent idea
and uh we have been having a long
discussion internally. Um, I would like
the distinguishment between demo data
and test data. I think they
fundamentally serve different purposes.
Demo data should be something that looks
smooth like like we we just saw in the
keynote with the beers and power bank
and I think that should be the purpose
of demo data for test data. I think you
should be more focused on the
uh for example covers covering some of
the edge cases and things like that. But
uh definitely um we can explore to use
the helper code units to insert demo
data because um you save some time to
maintain the test library right um but
right now internally we have a a
separated process but you can definitely
try to um reuse them for testing
purposes. So there's only one thing on
top of my head is that in the helper
code we try to use validate as much as
possible. So those um validation
triggers on those defined those tables
will be taken into account. So the data
generated looks u realistic but in
testing purposes you probably don't
really care and skipping those
validations might speed up your test
data generation. But yeah that's
definitely something to consider.
There any more questions?
Okay, not much so far. I will switch to
the screen and see if we
completed the generation of demo data.
So the warehousing scenario has
completed uh sales order. Yes.
So if we switch to the sales order page,
you can see there is many sales orders
that's created. Some of them are created
by shoes module. But let's open a
warehousing sales order. In this case,
if you scroll down, you can see the
items inside this sales order is created
using the shoes uh module we provided.
And if you go back to the conto module
for warehousing, you hit configure
again. You can see that previously the
customer number and vendor number are
empty but in this case
they have been filled after the
generation and also locations has
already also been filled.
I don't know what I'm doing wrong but
yeah so if you have any other questions
or any specifics um you can find me at
the Microsoft booth downstairs. I
haven't been there but I I learned it in
the keynote that there will be a place
you can come and ask questions we can
discuss things even further or if you
are busy attending other sessions please
either email me um on this email address
or email val he's the lead engineer for
demo data
since the very beginning we have been
working on this for a few semesters So,
uh, reach out to us with any feedback
after you played around if you have any
suggestions to make it even better. And,
um, we're happy to answer any questions
for you.
And thanks. And that's all I have.
Thanks a lot.
[Applause]
