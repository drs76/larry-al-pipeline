# BC TechDays 2022 - Opening Keynote

- **Source:** https://www.youtube.com/watch?v=iFJXRBKhL9k
- **Video ID:** iFJXRBKhL9k
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 111m45s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

good morning everybody it's so great to
be back at tech days after three years
um
it's we always love coming at this
conference and uh we really really
missed you
um
and
as luke said you know we we we send we
send 39 people for microsoft usually we
only send about 15 people but this year
we send as much as as many as 39
people to engage with you meet with you
deliver content
sessions workshops
so you'll see of course all the usual
suspects the people you
you've met before if you've come to take
this before but you'll also see some
some new faces
but we wanted to
we wanted to take it actually a step
further and we wanted to give you a tour
of our facility back in uh incorporated
by the microsoft development center uh
so you can see where uh business central
is made so we've prepared a small video
for you
enjoy
[Music]
it is so incredibly humbling to see so
much passion growing around business
central around the world for so many
years it is your efforts every day
making someone's dreams and someone's
potential realized through the magic of
business central and much like you
microsoft business central developers
are passionate creative and unbelievably
smart individuals
so let me show you how the magic of
software comes to life in these worlds
[Music]
hey we're the application foundation
team and when we're not working on the
building modules for the system
application we're looking at your open
source pull requests on github
hi i'm sam and i work on the business
central web client
hi i'm alia and we are business center
staff management
hey guys my name is nikolai i'm part of
the compiler team i have to go now but
see you soon
hi i'm monak i work in app integration
team see you soon
hi my name is blanca and when i'm not
making coffee i'm busy working on
developer tools
[Music]
hi i'm susena i'm riding the developer
dog school business center
hi i'm christina hi i'm giselle and we
are the release manager team we are
releasing regular updates to business
central
and now when we had a glimpse into who
is building business central let's take
a look at how is it built
[Music]
wow what an incredible set of tools and
improvements
we can't wait to see how far you can
take it
welcome to tech days developers
assemble
all right that was a that was a quick
tour thank you
quick introduction of the team we have
the team had a lot of fun making that
video so i hope you enjoyed it uh so
before we uh we dive into um more
technical things and i know that's why
you're here this is bc tech days i
wanted to share a few numbers with you
because business central has a
tremendous online momentum at the moment
last time we we were here in 2019
there were about there was about there
were about 450 solution on the on the
app source and now we have more than
2700 uh applications thanks to you
thanks to your dedication to uh to the
products thanks to your loyalty
we had 1400 partners selling business
central now we have more than 3 800
and a growth of
more than 60 year over year of number of
customers for the product so tremendous
momentum for for business central
in terms of uh well worldwide footprint
we we have business central available in
91 countries and we will be soon very
soon adding 20 more countries covering
of the world gross domestic products so
on the map it looks like this you can
see all the places where business
central is currently available
and there's practically you know nowhere
in the world where you cannot get
business central
so the these ones these countries are
the one where business central is
available today and very soon in uh in a
few months he'll be available in these
additional countries
now
we have as i mentioned before more than
2700 solution on the app source but we
of course would like
to have even more and for that it's very
important that um
you get productive and and you have the
best tooling in the world and that we're
really concerned about your productivity
so um we're gonna we're going to dive
right into it to talk about the tooling
and productivity and for that i want to
invite ida
on stage welcome ida
[Music]
thank you vincent
hello everyone
i really would like to take all this
energy
the energy of our amazing developer
community
we haven't seen you for three years
but trust me
we have heard you
on yammer an idea thought and of course
on the github and on twitter
we have collected your feedback about
what you would like us to do to make
your productivity tools better
we have
make a really really long backlog of all
the productivity tools for our
developers
what is missing what are your pain
points
but i want to share something with you
today
to be really honest you know we have
been
um we have not focused as much as we
wanted to on this long pro productivity
background we couldn't prioritize it as
much because
running a platform at a scale is really
hard
we have been really focused on of
fundamentals of our service to have a
seamless service that is scalable that
is secure
and that is running really really fast
we have been also really focused on
automating almost everything and when i
say everything i'm really serious
automating almost everything in our
daily operations not only for us but
also for you for our partners for var
and our administrators
and you know
it is so rewarding
i have been working in this product for
20 years and honestly it's so rewarding
to see all that hard work is paying off
we have this extraordinary momentum
we are really
growing
great and we have all this world
coverage
and now that we have settled with our
service fundamentals
you know we start to see an opening
and we ask
of team
now we have that backlog
that is you have no idea how fine-tuned
by
peter
a very nice pm he is every year telling
me either productivity backlog either
productivity backlog and actually we
have started to work on that
a lot and i'm going to tell you that we
are going to focus more and more on the
productivity tools that make your life
the developers easier
i'm going to share actually some of
those
improvements and highly ask features
that we have made for you in this
release
there is a lot on the
screen but i'm going to actually walk
you through to some of them and the rest
of them i'm sure you have already looked
at it in the workshop or in upcoming
session you are going to take a look
let's start with the first one
primary key intellisense improvement one
of our highly asked feature so in this
release we introduce
a new decoration
that has primary key with the order on
the field
and the great thing about that is now
when you are writing the code for
example when you are
sorting or filtering on the tables then
you can see all the keys that they order
and get a better insight
let's look at another
highly asked feature setting the default
application area
you know there is a story about this
i think there was a frustrated developer
that write to us on the yammer i'm
adding a lot of control to a page right
now and i need to bloody type every
single time this default application
area if not
you know it doesn't show on the page why
you hate us so much
so
i don't know maybe you are sitting here
somewhere in the room just want to tell
you
we truly don't and that's why
in this relief
we have enabled of controls
to actually inherit the application area
from the parent page or report so now
you can just add the application area
set it on the report or page and that's
it
so
the next one
i think many of you are aware that
a few releases back we really ship a
better permission set a story
in al syntax
but
we didn't provide you the tool to
generate
these permission sets in al just like we
have done for xml permission sets
and obviously many of you come and told
us you know
it's really really hard every time i
want to make a new object i need to go
and find the permission it takes me out
of context it's waste of time and
actually you told us you know that's why
we are not moving to the
new
al syntax because it's really cumbersome
okay
we try to fix that
now it's the one-liner we are
introducing a new vs command that not
only it can generate the permission set
in a l but also it can update it for all
the existing objects in your active
projects so hopefully with this
not only you use the permission set
scenario much more you are going to
convert it to this
and syntax
and
the next one
actually the last one and i really
wanted to talk about this a bit because
you know
i know how much you work hard
put a lot of your mental capacity
building a solution
and
trying to perfect your algorithm and of
course
you don't want to when somebody is
debugging and start to see your code
so protecting your ip is super duper
important for us
and
in
last year we introduced the resource
exposure policy that gives you the
granular control so you can actually
set your code in a way that it wants to
be exposed you have a control over that
but then we didn't want to actually stop
there
because some of you told us that many
times when
sometimes if you have an appsource app
you want to actually deploy it as a dev
extension
on the customer for customer to test and
in that case you are not protected
therefore in this release we have
introduced for you
the dev extension flag
that actually when you are using that
then you can apply
all those exposure policies to your dev
extension as well and
to be
protected which is i think it's good and
i recommend you use it
so
this was just a few
selected ones that i just chose to show
you
but if you want to see more of course
there is more but before all that
i actually want we start to
imagine something together
so
imagine
that you have a tool
that this tool
every time when you are extending a code
right when you are extending it can
discover for you the events
that are raised in the code that you are
extending
and then you don't need to go and add
those events manually you can just copy
the signature
and put it under and get going wouldn't
that be nice
to have such a tool
we shipped this tool three years ago how
many of you in the audience are using
event recorder
yeah this is totally matching of
telemetry honestly
you know the usage of
event recorder
in telemetry is really low but let's
hold that out there i want we do another
imagination i promise you it's the last
one together
so imagine you have 500 objects
and you're changing only two objects
when you are changing these two objects
now you want to publish it
then you need to sit in front of a
screen because you need updates
all these objects are getting compiled
all 500
objects at the same time
and
it is just waste of time
so wouldn't you think it would have been
nice if the vs code could have grabbed
only that two object that you modify
publish it just like that and then you
could test it
wouldn't be that awesome that we have
such a tool
especially when you are dealing with a
lot of objects
you know we have also that too
how many of you use rad rapid
application develop please tell the
truth
okay
perfectly matches of telemetry if this
is a sample audience because
the usage of red is even lower than
event recorder
the whole point i'm trying to make is
we are we are building these tools for
you we are really investing on them
and we think it will dramatically
change your developer experience and
maybe we are not doing good enough you
know maybe you have a lot of feedback
and stuff but please start using it and
give us feedback and we can always do
better
if
you heard about this tool just today
there are easy link for you to go and
check them out very nice documentation
on that
so i talked about a lot about running a
cloud service
but i would say
you know
when it comes to the tooling it's not
always about productivity
to keep of customer running
we need
to make sure that we can fix the issues
very quickly
and that's why
we have built for you this beautiful set
of tools i hope many of you are already
familiar with some of those you know
that if you want to see
what is going on on a page and the page
load and the data on the page you can
use the page inspector
you can actually take a snapshot
live from production environment
and debug it offline through the
snapshot debugger you can look at the
aerial profiler and
analyze your performance problem and
track the execution time just few of
those two
all of them we have ship and i hope you
are familiar with it
but
let's do not imagining but what if
what if we could involve
of customers
of consultants of partner support
to make the initial performance
investigation themselves
without
involving your very expensive and a
scale time
to dramatically reduce the support cost
and this is something that many of our
partners because they are in the same
business as us right it's talking about
the support is really expensive
and
for that
think about
if you can analyze as a user as a
customer
your
performance issues yourself in our
beautiful web client let's have a look
so i'm waiting for my screen to appear
i think everybody can see it
i need a
small refresh
we were talking this morning if we have
sacrificed enough codes for our
democrats so
i hope it has been enough
so imagine i'm a customer
i'm a user in the customer side we saw
there was 12 percent of you in the
audience
great
and
recently i have seen that the opening
the sales invoices are really really
slow and i want to figure out why
so i go to the first place i know
which is help
beautiful help page and i can see the
help and support link in the bottom i
click on it
there is a section troubleshooting
analyze performance nice let me check
that out
even though that seems quite advanced
and this opens the performance
profiler
and like all other nice
pages it has a teaching tool let me
figure out how i can work with this okay
ah this seems quite easy so it is as
easy as actually a start reproduce and
stop
i think
i can manage that
let me try
okay
i get back to my sales invoice
and i'm going to try to open one of this
before that i need to start recording
so let me pick up one of those
okay
it's opening
now i can see
it's really really
slow
finally
it opened up
good
then
let me stop it
wow
now i can see a view of all the apps
that were involved when you open
the sales invoice
and i can see i can actually see
the time
they take
for each app
and if i look at it i can see the
invoice customization app is taking
quite some time
so
let me see who owns that maybe there is
something for that here there is so i
can actually switch that by a publisher
this is actually my reseller that
installed this quite recently
and i can see probably caused all the
problem
let me see if i can find some more
information what about here
maybe i can dig a bit deeper
show technical information okay
now i have another pie chart that
actually
it shows the time it take
within each app
wow okay
i can see i was right actually the
invoice customization really really
seems as slow
so that is the problem the app from my
real estate at least i think so
and there is some other information here
some more detail time is meant by
application object um
call tree
but remember i'm a user
so
this stuff seems a little bit too
complicated for me
what i can do now i can actually still
go ahead and create a support case
and send it to my reseller to my partner
but another thing i can do i can
actually share it through the one drive
the profile that i produce or actually
download
it so
so when i download this okay that's fine
i create my support case i attach this
so it make it much faster also for
support to figure that out hopefully
and now let's switch the rules i'm the
partner
i just
receive this profile and the support
case from my customer
and you know what i can do actually i
have great option because i can send
this to my support folks and tell them
actually and those support first they
can
get this file upload it in their own web
client performance profiler and verify
the case
isn't that beautiful
or
after they verified the case then i can
ask my developer to have a look through
this dig a bit deeper to you through air
profiler in vs code
and that is exactly what i have done i
asked my developer
so my developer actually received this
and open it up
maybe now i can actually sort it so i
can have this i can see all the calls
and with the time that it took but
let me actually sort it so i can see it
with the time is spent sorted
and it's quite obvious right process
sales
invoice
is taking a lot of time
and
because i am a developer and i have
access to code i can actually navigate
to god now and look into it or even
better if we i want to really analyze
the execution and my variable statement
they can then i can attach to my
production environment
grab a snapshot
download it
to my project
and debug it offline and that's exactly
what i did
so
i go and run this to debug offline
i hope how many of you by the way until
this runs are using a snapshot debugger
i hope i see more hands more hands
matching again our telemetry
awesome so
going to the snap point enough code
i can actually see the
actual time of
the random time
306 awesome
and
if i look at the code cutter i can
clearly see
the code that's run and by the way this
is a new thing so this vision indicator
we have added in this
release if you want to know whether your
conditional statement run or not so you
can
define a new snap point and continue
your investigation this is a very very
nice way to see
clearly which part of code has run
but in this case you know
because it's quite obvious i don't need
further in the
information the time is matching
and as a developer i'm so happy because
first of all i didn't need to reproduce
this issue
and the best part of that i didn't waste
my time going to look at another
partner code
so
if i come back to my
slides
yep
that was not all
we have actually added quite few
other debugging enhancements
that i would like to share some of them
with you and for more please attend the
troubleshooting
session i think it happens right after
the session
so
developing and troubleshooting in cloud
sandboxes without direct sql access
is
not easy because then the al cards that
cause the lock it's not easy to catch
that
and of course i know you can see the
logs today in the web client but then
you always need to go and create a new
session and it is not interactive it's
quite cumbersome so that's why we
decided to
add the sql logs inside for you inside
of the debugger so
next time when you are developing your
code or when you are troubleshooting it
is much easier just in time to see what
are the calls that's causing all the
locking and fix all the performance
issues
this was actually this is of
a business central app team they are
using this and i can see they're sitting
here they are swearing but it's one of a
very very popular feature
so the next one
many of us has told us that you always
want to
to investigate
in different scenarios in a context of a
specific company
that's kind of important today you need
to go change it from web client or go
and change the default company and
that's not very easy so many of you
voted and asked us and we have delivered
again
so now you can actually from the
launch you can configure and set the
company and start debugging which i
think it's going to be really helping
you to debug more efficiently
and then
um there are two more things that i
wanted to share
so you know many of you told us that
when you want to break you don't want
all the time break and try function you
really want to go and debug the on hand
and this way extension so now we have
provide you this absolute try option
that you can go and try and go and
efficiently really
debug after
uh unhandled errors and the last not
least the same applies on temporary
record changes you really want to go and
figure out what are the troubles with
committed
changes so if you would like you can
also exclude that just
easier and better
troubleshooting
and debugging
so
business central
we really provide for you a powerful
source of tool to troubleshoot issues
with data with code with performance
and
we really encourage you to use this tool
by the way of telemetry shows that many
of you higher percentage but
i hope it grows and grows because it
will really make your life easier and
make your customer run more seamlessly
so if you want to know how to use all
these two go to our
master site aqua ms pc troubleshoot
thank you very much
vincent
i think you want to explain some more
about how we are tuning
up
so ida talked a lot about
productivity improvement and
troubleshooting and debugging
and so of course all these activities
are very important uh as a developer but
uh
once you have written a lot of code and
and and done some debugging and and
fine-tuning of performance you need to
actually really tune your app and it's
really important um that
um you do that in order for your
customers to keep happy uh you've seen
you know how many customers we have in
the cloud today
so
i want to talk a little bit about that
subject
and the first thing i want to talk about
is telemetry you heard aida mentioned
telemetry a lot of times
from from our point of view we we have
we really use telemetry a lot
for for bc
i would like to see a show of hands how
many of you have enabled telemetry in
your extension
i had quite a few hands and that's good
but i i you know i i hope that after
i've shown that
and advertised for it that next year
when i ask the same question i would
like to see like everybody raise their
hands because villametri is really
something you should you should use
so how just a quick reminder how do you
enable telemetry in your in your
application
uh in your extensions first you got to
go into the azure portal create an
application inside
resource in azure
and you'll get a key
and you go to the bc admin center and
enter the application inside key in the
business central admin center and that's
it you
you have your telemetry um
up and running for that
but we want it to so that that's pretty
easy and then you can you can start go
to uh to application insights on the
azure portal and you can start setting
up
monitors set up
you know
do some query on see what's going on in
your in your extension but we wanted to
take it a step further and help you get
started with building dashboards and and
getting uh really a lot of insights in
your application so for that
we uh we're introducing the bc um
usage analytics app it's a power bi app
you go to powerbi.com
sign up and and download the app the app
is free
and and you can start
see what what the telemetry we provide
from the extension
that what it gives you i'm going to show
you
how it looks like
instead of
talking about it because it's best to
demo it
all right so
here i'm in um
can you see my screen now
hang on i need to i think turn off my
presentation
all right here we go
so this is so if you go to power bi and
install the uh the this app
this is what you'll see
so it comes with a lot of of test data
so the data that i'm going to show you
here does not come from your extension
obviously but what you need to do to see
your telemetry from your extension you
need to click on that link connect your
data
enter the uh the application inside key
that was talking about before
the look back period this is how long
time you want to go back and look at
the data and and a couple of other
information and that's it that's all you
need to do and once you've done that all
what i'm going to show you
here all the dashboards will light up
and you'll see all that data you don't
need to do anything in your extension
except for one thing but i'll get back
to that
so i just you know there's as you can
see there's tons of dashboards here and
i won't you know i won't have time to go
through all of them so i'm just going to
give you a quick tour
on the session dashboard you can see
how many sessions from various tenants
whether it's coming from production and
sandbox the type of sec of stations they
are
i can go here and look at the at the
client types
i can see here for example what browsers
my customers are using and whether they
are accessing bc from desktop or tablet
and which which client os they have even
the the resolution of the screen i can
see as well
i can see where my users are located
geographically
i can see here for example i have a lot
of users in the united kingdom
um i can also take a look at the pages
see
i can see for example here that the
wall center is one of the
most
shown page not so surprisingly
tons of other
information let me jump to the errors
dashboard uh i can see how many errors
uh
my users
get
there's no for example here i can see
there's no login errors which is which
is great but there are some error
dialogues so i can drill down in that
and see how which dialogues are actually
shown and how many times
since there's really a lot of
information here
performance uh there's also some great
performance dashboard we give you some
recommendation of things you could do
for optimizing the performance of your
extension
i can see
uh things on page views you know how you
know how long time it takes to display
certain pages
um long-running sql queries
uh long-running l methods so tons of
information and a lot more um so just
you know that was just to give you a
quick tour of what you can do so go and
you know go and try it out play with it
you'll see that's really really great
there's one one dashboard that won't
light up uh and this is the one called
uh feature usage
so if you want if you want data from
your extension you will need to write
some code there to actually uh emit your
own telemetry and that's uh that's a way
and you don't need to write a lot of
code it's pretty easy but that's that's
the way you can go and and uh get
telemetry about your feature about what
your extension is doing
but if you don't do it you'll get you'll
get all the other all the other data
that's just uh uh uh show you
for free um so
i really really encourage you to go and
use this uh this app
again it's free application insight is
not free but it's not very expensive
the app the app from power bi is free
and
let me get back to the presentation here
here we go so
a few links um aka.ms slash bc telemetry
repo that will take you directly to the
uh
the power bi store where you can
download the app and if you go on ak dma
slash bc telemetry samples
um
you'll get to or a bc tech
github repository where there's tons of
of samples on videos and how to uh how
to get started with telemetry by the way
are you familiar with the bc tech repo
yeah a few hands so you'll hear me
advertise about it uh several times
during this keynote it's a great place
to get all sorts of resources there's
tons of samples tons of demos there code
you can use and you can even contribute
but i'll you know i'll talk about it
again
all right
now
i'm going to talk about
moving data because what we can see in
our telemetry is when
you're moving data around
it really takes a long time and we can
see that
especially for example upgrade scenarios
when you're upgrading your extension
from one version to the next it's very
common that you will need to transfer a
large amount of data
and
usually that takes a long time
and depending of course on how much data
but if you have you know even a you know
a few thousand records it will slow down
uh your your your upgrade
so this is why we're introducing data
transfer at landing speed
so
on the
left hand side here you'll see some code
and that's what that's type of code you
would usually write to
transfer data from one table to the
other you know pretty straightforward
have a
origin table and a destination table
do a simple loop and copy each field
over
and you can imagine
when you do that you iterate in a l so
it goes back and forth between al and
sql and and for each iteration of the
loop it generates a certain number of
sql statement
i don't know how many but let's assume
it generates i don't know maybe five sql
statements
so if you have a thousand records you
will generate five thousand sql
statement but if you have a million
records you will generate five million
uh sql statements so as you can imagine
this is not a very efficient way to move
data within a database
and actually sql
is very good at moving large amount of
data so
the idea is to let sql do that operation
for you instead of each everything
through here and this is why we're
introducing
the data transfer object
so this is a new way to move large
amount of data so it's very simple as
you can see you create a data transfer
object
indicate set up which table you are
copying from and which table you copy to
set up which fields you want to copy and
call the copy fields method and that's
it
and that will transfer the data in a few
sql statements no matter how many
recalls you have in a table that will be
the same amount of sql statement that
will be executed within sql
of course the gain in time depends on
how large
the tables are obviously and how many
fields you copy but we've made some
experiments and we can see that in
certain scenarios we have
a performance improvement by a factor up
to 200.
so
really if you have you know really
encourage you to use this new construct
if you have code that looks like on the
left-hand side of my slice please go and
refactor your code to look uh what's on
the on the left-hand side
and you'll see you know really
significant performance improvement
so talking about uh performance
improvement a while ago we released the
business central performance toolkit
and
the reason why we anybody familiar with
it
yeah a few people great so uh the reason
why i released that toolkit if you're
not familiar with this because we very
often we get that question uh
you know i have this customer who
with you know
that many that much data and and my
customer is doing so many transaction
per
hour is my system going to perform
and and truly we cannot really answer
that question for the simple reason that
um the solution as you well know the
solution that is running at the customer
is a combination of the microsoft app
and your app and maybe even some other
third-party app
and
that means the code that is running we
don't we don't know anything about the
code that is running and and the best
way to assess the performance of a
system like this is actually to test it
out
so that's why we introduced the
performance toolkit which is a great
toolkit that allows you to
simulate your scenarios and the
scenarios that you might be concerned
about performance-wise and simulate um
a large amount of users accessing the uh
the system simultaneously
so
in order to
leverage the performance toolkit you
need to install the the business
performance toolkit al extension
from the app store
and then you need to get some powershell
scripts from the dvd or from a docker
environment to
launch the test and run the tests
then you probably want to go to github
and and get some sample tests uh to get
you started and use them as a template
and kind of rewrite them to to write
your own scenarios
and you will of course need to rename
renumber the test to be in your id range
and then you're ready to start writing
texts so it's not very complicated but
it's still quite a few steps to get you
started and in order to
make the adoption of
of of uh the
the business central performance toolkit
even easier we're introducing the
bcpt vs code extension
so it's not an ale extension uh not to
be confused with the next al extension
it's a visual studio code extension
but let me show you how how it works
so
here i'm in visual studio code
and i have installed the
business central performance toolkit
extension and i go and set up a new
um i want to set up a new project and i
point it to my sandbox so look at the
bottom of the screen here you'll see
that's where it's interesting
i need to
authenticate here but if you look at the
bottom
right corner you'll see what's going on
in in vs code
so it's fetching
information from the environments
right
and
then i indicate where i want to save my
project here
and now it's
installing the uh the business central
performance toolkit
once that's done
it's downloading the test and renaming
them for you so everything is automated
you don't need to do anything here
and it's adding
the configuration for for for the app so
it's going to be the app.json and the
launch is not going to be configured
uh you know properly so i don't have to
do that either
and it's copying the powershell script
so i'll have them in my project and
that's it now i can open the project
that's got created so it's a newel
extension
and you'll see here i have
i have all the scripts available there
ready to run my launch.json is
configured and my app.json is configured
pointing to my sandbox environment and i
have the the tests here
ready to be customized
so i just need to download symbols again
i'm you know downloading these symbols
from from my sandbox here
and when that's done i can go ahead and
compile and publish
publish this this app
and it will open in a second it will
open business central right on
onto the business central
performance toolkit suite page and i can
start creating a new test suite here
so here we go it's
compiling here
let's give it a couple of seconds and
it's opening directly into the uh the
performance toolkit
test page suite page and i can just go
ahead and create a new test suite from
here
and pick the tests that
that i want to include in the test suite
so there are all the tests that were on
my solution are available there
so there you go that's that's how easy
it is to to get started with the with
the business central uh performance
toolkit so we'll release that
application that visual studio code
extension is not available quite yet on
the store but we'll release it very very
soon
so that was you know a couple of things
i wanted to share about
fine-tuning your applications um i hope
i hope you may make use of these um of
these tools
uh but another way to now we talked
about productivity and and um how to be
you know more efficient and and do more
with with our tools but another way to
to be more productive is also to
leverage and integrate with some of the
other great technology where we have at
microsoft
and to talk about that i would like to
invite harina on stage
there you go
so i'm very excited to be here today in
antwerp uh as vincent mentioned it has
been quite some years and actually my
first time is exactly the first uh badge
on luke's
slide on
2013 nafta days 2013.
so um let's uh start talking about our
platform and let's remind ourselves what
is the core mission of microsoft power
platform that is to enable everyone to
uh foster innovation
and many of us i'm sure we have heard a
lot this phrase that statistics say that
in the next half a decade we will be
building 500 million apps and i want to
hear this i'm thinking 500 million apps
this is a huge number and can we really
do that
and what it means for us as developers
it means that we should be able to uh
deliver core value to customers fast
now we tend to think that our platform
comes with uh
with simplicity for the end user and for
citizen developers but we professional
developers are the ones that are
building high
high scalable high quality
repetitive solutions that help our
customers automate uh business processes
so
the thing is that
al as winston mentioned and we have seen
also ira's fantastic demos
is is very powerful and is very flexible
uh and is a tool that you can use to do
a ton of things but power platform
brings a whole new dimension for you in
terms of developer productivity
because this is what it is in in in
essence right is an amazing set of tools
that you can use on top of the microsoft
cloud
to build state-of-the-art solutions for
your customers
now let's take a peek
at the microsoft power platform universe
what do we have here um we have 600 plus
connectors and you know whenever i talk
with automate and power up steam they
tell me this number is growing
as we speak
uh and these connectors are ready for
you to
uh you know to use them to help help you
connect your solutions with external
system uh build and automate our
existing systems and so on and then we
have of course the dataverse stack which
is a whole new other you know dimension
it's a high highly scale high trusted
data platform that comes with a ton of
innovation uh the ai the data analysis
the data search and so on
power apps
our pages our automate are also there
for you to help you surface uh data to
your users and also automate processes
let's not forget dynamics 365
is also part of this universe
and together with the microsoft 365
collaborative solutions and the power of
the azure cloud the development tools we
have available github and vs code all of
these makes power platform one of the
most innovative comprehensive innovation
engine you have available
also at your fingertips here in business
central
because this is the message that we want
to convey to you today that is that
business central is deeply integrated
with our platform we have power bi
connectors to uh build your reports we
have the power platform connectors we
have just recently ga in in april
release and they are also ready for you
to build power-ups uh mobile apps uh go
and build a fantastic assistant bots for
for your customers
and then again the dataverse the
dataverse
stack is also a priority for us in the
sense that we have the data versus
synchronization with dynamics 365
and the virtual tables and
what we can promise to you is that in
the upcoming ways we will continue this
investments and we will continue to
enab to enable more and more scenarios
that will light up
in your solutions
with very little cost
from development perspective
um so now um
i'm supposed to tell you a story
and uh let's see if i actually
sacrificed and he goes to the
uh demo demo gods
but
let's give it a try
so i'm going to switch to my machine yes
so today it is our
10-year anniversary for bc tech days
right
and um
you know luke and his team has started
organizing this many many months ago we
all know that
and the team has been very busy
um by dealing with vendors suppliers
invoices are flying around
and one of them has landed in my inbox
here because today in this story i will
also be part of
the team that is helping luke organize
the event
so
let's um
let's go ahead and preview this invoice
and see what it entails
okay these are the refreshments that
luke has ordered for this conference
we almost have tasted uh with our eyes
these beers a couple of minutes ago
and notice here that there is also one
two bore green beer which somehow
mysteriously
sneak into this invoice someone out
there must have really insisted that
that they only drink danish beer
now
let's see how business central
can help luke and his team today
um to process this invoice with
only a couple of clicks
now
um
only only a couple we are going to use
for this the uh outlook add-in
and um
let's send this document to
uh to the back-end
so we're going to go to the attachments
page and
attach directly from email
and then press ok
and this document has now landed
in
business central
now here we have
um
our special vendor that luke and his
team are using and we all always strive
to order the best beers uh to a special
brewery which you call best brewery and
since they're using business central i
mean this vendor could just be best
bureau for bc
now let's see
um if
business central can help me process
this invoice
with only one click and i can see here
that in the automate
menu i have
process invoice action that is so great
and
looking at this action when i'm running
it now
it is obvious to me that this is a
automation flow action
and
because i recognize the
power automate maker experience right
here embedded within business central so
let me go ahead and run this flow
and
another thing that i wanted to mention
here is that
that is possible all of this is possible
because in the april release we have
brought power automate the automation
platform that everybody loves in the
heart of business central
and um
what does that mean that power automate
now is part of the business central dna
it simply means that you will have this
automate context menu pervasive across
business central pages and you will be
able
directly from you within web client to
create manage and and run flows
but
i am planning to use
this action quite a lot
and
right now it's somewhere buried in the
more options menu
so let me go ahead and see if i
can
actually
move this process invoice action right
here in my promoted area
now that's good now this action is
available for me with one click how cool
is that
so
now that my action has run
i have here
my own personal chat with power automate
and you know power automate is doing a
great job and notifying me
hey this your invoice is ready for you
to review
um so let's go ahead and do that of
course we need to check this is this is
an automation flow which i have just
recently built so we need to check if
the information actually matches
um so let's go ahead and do so
and it does and again these two work
beer here i mean i don't understand
so let's uh let's go ahead and uh share
this with the rest of the busy tactics
team
and
see if we can actually solve this
mystery
and i'm going to share this with the
rest of my team i must say share the
teams is also one of my favorite action
i like to talk a lot as many of you know
and i like to collaborate also with my
peers so um
let's uh let's see here i also have a
new features from microsoft now i don't
only share the link
uh to this to this record but also i get
a beautiful adaptive card which gives me
as a glimpse the information i need
about this invoice so i'm going to share
this on my team's channel
and let's go ahead here and see
if the team has received my message and
it did
but i can actually go here one step
further and uh and simply pin this uh
invoice on the top
of my channel
and once i go ahead and do that i can
start a conversation and say hey
anyone
knows
who
ordered
the tuber
and let's hope my colleagues will help
me
solve this mystery
now isn't this just magical i know i'm a
little bit biased you know since i love
our platform but let's think about this
the data just uh
oh okay
this is because look supports denmark
aha so the mysterious order was of you
because of you look okay want to bulk
beer on you that's fine
so um
yeah
so uh so so as i was saying look at how
data actually flows seamlessly between
so many systems between outlook
between
business central power automate come
back to teams and power and business
central again and all of this
you can do it without and the end users
actually noticing the
data connection points you have here
um and just to kind of show you that
this is not just magic we can take a
look at the
maker experience in power automate for
the process invoice flow
so what do we see here
we see that we have used the for
selected record trigger this is a brand
new trigger we have introduced in april
release which actually has a great
capability of of connecting the context
of your record in the business central
page
with the automation flow so your record
will be passed through this to this flow
uh another
cool thing that uh
client engineers also loved to play with
in preparing this demo for us today
that is how did we extract the
information from invoices and that is
using ai builder
again a top uh uh
innovative technology we have available
here a whisper platform and i just want
to say that yes the team had fun uh but
you know they have also work to do so um
yeah we just actually used the pre-built
model uh ai model that a builder comes
with so it's not like we have spent a
ton of time
preparing this flow
and
then
the flow is fairly simple we go ahead
and create the invoice header with this
the lines we notify the uh the
on the team's channel that with the
adaptive card that the um
document has been registered as invoice
and also we notify by mail and i can
actually confirm here that i did receive
an email with the purchase invoice
so that that concludes my demo again it
is something that we have stitched
together uh in uh in in a couple of days
special for this event to celebrate here
the 10-year anniversary for for bc and i
hope you you enjoyed it you enjoyed it
as much as uh we did uh building on and
and preparing for for for it
so let's come back to slides now
let me see is this one right
and
yeah okay i had so before i wrap
actually i had one more slide that i
wanted to show but somehow it didn't
reach into the powerpoint and that is
about how automation uh flow actions uh
work
um so basically in this release um now
in october the automation flow actions
will have a correspondent
in l um that we that we call custom
actions um and that
these custom actions will um will
actually point to your
flow to your automate
flow and uh to your flow environment so
how you build these solutions you go
ahead you write your flows on power
automate with on your maker experience
you package them as an
app source solution then you go to a l
you write code for these automation flow
actions you package them and an
extension and there you go you're ready
to distribute this to your customers
now okay i can now move on to the next
topic which is the modern action bar and
somehow i for the ones who pay attention
they probably noticed
that i have already showed one of the
goodies uh when i uh uh customized the
promo process invoice action
but let's uh go more into it so in this
release we have
been modernizing we have started a
journey of modernizing the action bar
and as always what we have done is we
have taken an analysis of
360 degrees analysis of all the data
points we had on how our users interact
with the action bar
and what it made it more interesting
this time around that is the amount of
telemetry we had available um
for for
identifying sequencing and patterns
because in many in many ways the what we
can clearly say is that the
decision that we have made into when we
have done the action bar organizations
they are actually very much telemetry
driven 280 million telemetry data points
i mean we couldn't resist of using that
much data right
and we have also run heuristics on the
95 percent of most used action with a
strong focus on efficiency and
consistency of the actions
we have
also
deeply taking a look at your feedback
and not only your figure but your users
feedback uh in how the action bar uh is
being used and and what are the gaps and
what are the features that that our
users will want to see in the product
so how did the modern action bar come to
life
well some of the feedback was we wanted
to have intuitive and flexible
personalization and for this we needed
to have a new way of defining the action
structures and menus in l pages
we have introduced a new concept called
action ref that i'm going to talk a
little bit about in a second
the other part that was really a top
priority for us was backward
compatibility
because when you
go to your customers and enable the
modern action bar we wanted to make sure
that the personalization and
customizations are not going to be lost
and we also have invested
quite a lot in the tooling
so that transition between the old model
and the new one is very smooth
we also had a focus on efficiency and
this is why we have done a lot of small
optimizations of the of the action bar
and how the actions are are rendered in
that area
we have introduced a new control split
button that you're going to
see it in action and love it just as i
do
and then um we also have focused on the
consistency of actions um
actions covering 95
of all all usage should not be uh
only available in more option area this
is something that we have seen from our
telemetry and we have really uh
try to make sure that these actions will
be available for you in the promoted
area maybe with with one click even
right
now coming back to the al meta model and
what were these uh two
main concepts that powers the new action
bar so one of them is the promoted area
we wanted to make sure that the promoted
area is a first-class citizen
on l pages
and why is that because
otherwise we could not have had this
flexibility on on the personalization um
if you remember first many of you i
think do uh windows client had did have
personalization of promoted area no
doubt uh but it was somewhere stored on
an xml file you know uh distributing all
client machines very hard to upgrade and
a very cumbersome to deal with um and
this is why we wanted to make sure the
al meta model is strong enough for us to
build a great ui uh with it
the other concept is action ref
the action left are a light
representation of an action and here the
principle has been we want you to be
able to um um have your actions where
you would like in the action define them
as you want but not duplicate the code
right so you write your action code once
and then you point your action ref to
the base action and you can surface it
where you want in on the page
and we have primarily used it for
promoted areas but uh there are more
other usages
and i'm sure you will see that
in in the sessions
so now let's uh
switch to my machine and see if i can
show you a sneak peek
of how the action bar looks right now on
the pages where the modern action bar
is enabled
so
the first thing we notice here is that
the action bar opens in
by default in pinned mode
that is a request we had for from many
users
and
also feedback we have gotten from users
research
we also have taken a look at consistency
with office products and microsoft 365
of course uh there you always we always
have the home area in the or in the home
area
um you can find your most used actions
and this is why we kind of rename the
process area to home
and these are the
magical
split buttons
i must admit that when i saw it on the
mock-up from from our fantastic ux theme
i was thinking okay what is really
so cool about it right but actually um
it's it's pretty it's pretty awesome uh
the reason being because first of all
it's just a group
like from a perspective but is rendered
as a split button the other thing it
gives you the advantage you can group
these similar actions but you don't have
to think now what is the caption like
can i have some other new term that
didn't appear in the action bar before
is it navigate is it navigate one is it
related or what it is right so you can
group them without necessarily thinking
what the caption should be
and the most important thing is the
first and most used action is
clickable
right so uh you go ahead and post this i
don't feel like it
and
let me show you another
uh very interesting uh thing you can do
with it it is which is like let's assume
i'm not happy with post but i normally
use post a new i can just go ahead and
move this uh around and now boston you
become my
my most used action
another another interesting
uh feature is also that you can go ahead
and reorder the actions
here in the promoted area
we are supporting now subgroups in the
promoted area and you can also play
around with uh with these menus if you
if you wish so so
demos here can go forever you can move
around actions uh promote them demote
them
do do whatever you want basically we
right now the action bar is
as flexible as we wanted to be there are
still more work to come and more more
scenarios to enable but
from our perspective it's a great step
forward
also more options
area we have
reduced clutter here meaning once you
promote your actions they will not be
available in the more options area
anymore so we have reduced clutter here
and
one more detail before i wrap up that is
the navigate menu so some of you
probably remember navigate menu
that was also confusing for many of our
new users and maybe also part of
existing users and this is why we have
collapsed the data bound actions uh into
the entity menu so right now not invoice
for example menu contains also some of
the actions from the navigate area
so that
that concludes my demo on the
action bar
and i think what you have seen is just
the tip of the iceberg and you will see
a lot more in the in the sessions today
and tomorrow
and now let's continue on the modern
modernization theme and let's hear how
flexible our permission system has
become
thank you foxy
[Applause]
let's see
you're absolutely right thank you
so
we are going to modernize the permission
system as well
it is not a secret that the permission
system is not really easy to set up it's
not easy to
create new permissions even though we
got a whole lot of new features for
generating permission sets and also
moving the permissions to metadata
but in all honesty besides that we
haven't really made changes to the
permission system since it was created
in the very early days of navision
so it is time to modernize it for sure
let's take first
a look at the
the goals for this
so
one of the goals is as i said to make
this usable
and also make it understandable we want
to have well-defined building blocks
that you can assign to users
and we want to have some granularity
where we can assign you know big areas
of permissions or very fine
defi small areas of the permissions and
to do that we need to build a hierarchy
instead so you can select which level in
the hierarchy that you want to assign
we also want them to be easy to
understand
so
rather than only having permission sets
that are defined in in different areas
of the application we want to have
scenario-driven permission sets
so you can assign
permissions for a specific scenario like
posting an invoice rather having a full
area of invoicing
so that gives you much more flexibility
in this
we of course also
heard the feedback that
they are really hard to maintain
and especially one thing
has given you a lot of pain that is if
you needed to have a
slightly different permission set than
one of ours then you basically need to
create a copy and every time that we
make changes to our permission sets you
would need to remember to make those
changes as well and that of course is
very cumbersome
so
one of the things we want to do here is
we want to be able to create permission
sets based on another permission set and
this is exactly how we are creating this
hierarchy
then there's also
actually a number of areas in the
applications where
it's actually not necessary to have
permissions
you know think of it
for example the change log why do you
need to have permissions to write to the
changelog it's kind of built-in
functionality and everyone should have
that
so
we want to make some functionality that
can make it easier to define those
permissions
so you don't need to assign it to the
users
let me just drill into a couple of
new features that we are coming with
here
one of them is
really the features that that we are
using to build the hierarchy that i just
talked about
the ability to inc ability to include
permission sets when you're creating
permission sets and the ability to
exclude permission sets
so the exclude is very important here as
well
so if you look at the example that i
have here
i have a permission set that i'm
creating that's called test tables
restricted and it includes two other
permission sets the system application
test tables and the local test tables
but it actually also
excludes another permission set which is
called the restricted local test tables
and the resulting permissions that
you'll get is kind of the blue area that
you see on on the slide here uh where
you know we first add up all the
included ones uh and then we subtract
the excluded ones so with this we can
build some very powerful uh hierarchies
that gives exactly the permissions that
users needs
the other
functionality that we have introduced in
this release is the so-called inherent
permissions
as i said before there are sometimes
some areas where you just
want to give the system permission and
you don't need to assign those to to
customers
to the users
and the example i have here is actually
a procedure get default work date
which has an attribute here that's
called inherent permissions that gives
you
indirect reader access to the gl entry
table
so you don't need to assign that
permission to any users because whenever
they call this function you know they
will automatically get this permission
right now the inherent permission
property is only working on on on the
method scope here
but we are working also of enabling this
at the optic level so you can have you
know larger objects that that have
specific permissions built in
let me take a step back here and
you know when we're saying
modernizing the permission system
what progress have we done so far and
what is the plans going forward
so as i said before we have been working
on a lot of tools
in the toolbox so so we can build up
some some good permission sets um here
most importantly we moved it to metadata
so you can actually update your
permission sets in
while you update your code
so that's a very important piece and
then the two things that i just
mentioned here the include and exclude
permissions and the inherent permissions
we also
switched the entire application to have
permissions as metadata
we did that a couple of releases ago
and in this release we're actually
starting to build up this hierarchy of
permission sets and if you look at two
specific areas if you look at the system
application you will actually to be able
to see how we have done that
also there's a very important scenario
driven permission set called login
permissions because login is actually a
very important scenario
so there you can kind of get a flavor of
how we are thinking about building those
permission sets as well
but before we go any further
um
we want to start using the inherent
permissions as well because we need to
remove as much
from the permission of of the
application that you don't need to set
permissions for before we start building
more permission sets
and then we really need to do this right
because if we are going to create a
completely new permission structure a
hierarchical permission structure for
the application we want to do it right
so we want to take some time actually
thinking about what what is the taxonomy
of permission sets you know you have
some areas maybe and then you have some
scenarios and but we need to figure that
out before we start implementing it
and then finally of course we need to
start implementing and release it to you
this is going to be a
longer process
because we want to do this absolutely
right so you shouldn't expect that the
next release will have a completely
recreated permission system
but but we are starting on this now uh
and and i'm sure it's gonna be much much
easier to assign permissions and create
new permissions uh going forward
and that actually wraps up the uh the
engineering side of this yes thank you
boxy
so
now we you've seen how we uh you know
we've talked about product productivity
how to be more productive or to
troubleshoot and find you on your app
we've talked about how to integrate with
other products and and how to modernize
the app and now when you've done all
these
the next thing you need to take care of
is the life cycle of your solution and
and your operations and so for that i
would like to invite freddie on stage to
talk about devops
thank you
[Music]
you heard reena talk about modernizing
the action bar and
boxing about modernizing the the
permissions
why doesn't it say modernizing devops
here but so that's what i'm going to
talk about
but i'm going to introduce somebody to
you i'm going to introduce let's see we
have
here
simon
works for a partner simon
is the lead of a team and they've been
creating a
an app
for a customer and simon is happy as you
can see
simon
is done they're delivering the app and
the customer is
is also happy but the customer also
follows the trend in in it world and
they know something which simon did not
anticipate
they are asking simon about source
control and
continuous integration and simon says
yeah yep we have source and source
control and every time a single
developer is doing anything we integrate
it with the other guys so
isn't that what you mean by
continuous integration
well
not entirely
what about automated test execution and
you heard about the performance test we
can automate those as well shouldn't we
like make sure that
the next change you do to this app
doesn't like kill performance for for us
your
customer and
simon gets a little confused
now the customer throws around a number
of other words like dependency
management and
and and and all of these things and
simon starts to get worried and yeah
do you test your our app
for the next major and
do we do continuous deployment
continuous delivery simon is is kind of
a little worried now
and then
when he kind of realizes that he needs
to
maintain all of this he starts to cry
and
when he realizes that he needs to do
that
for many many apps he's crying his eyes
out right
until
he discovers
algo for github
is a
devops tool for business central
partners and it doesn't require you to
know anything about
about devops about docker about yaml
about powershell or anything like that
it is a plug and play tool it is where
devops becomes a tool instead of an
investment area
and
algo for github supports all of the
things that
were worrying simon just a moment ago
in fact
it does that out of the box
and it's a simple plug and play solution
so
simon is happy again
so i'll do a short demo of
how
simon is using this
and
simon's app really what he has he has
his
files right here in a folder
and
i want to create a repository with these
apps so the thing that simon needs to do
is to go
akms algo pte because it's a pt that
he's creating
and this one will log me into
to to github and i'll say use this
template to create a new repository
based on this template
i'll select that owner i'll just put it
in my oh that's not simon oh sorry about
that
my s3
and i'll say private and create a
repository
for the devops piece
i'm now done
oh i'm almost done
right i'm
now i'm done
so this is what it takes to set up
devops for
the project of course we need to add
the file still and we do that by just
adding the project to this one
files let's find these things and then
drag them into this
and
github will enumerate the folders and
add these files
to my repository
scroll down and just
add these to a branch
propose the changes
and github will do some work on
processing the files and creating a
pull request for me sometimes this takes
minutes sometimes it takes seconds
and i'll just create this pull request
and the pull request is automatically
then
added to to github and the ci cd
pipeline automatically kicks in
and builds your test you'll build your
app
and runs the test on that app so i
didn't do anything i just created a
repository and added the code
now you might think that
it can't be that simple right i mean
we're special we have a lot of things
that other partners don't have so we we
can't use that for just out of the box
but in fact i had workshops with a
number of partners
the two last day and i think all
partners in that workshop ended up
coming out of the workshop saying
we can use that
even though every partner before the
workshop set we don't think we can
so
a few other things if we look at it'll
go for github the secret or the secret
source of ailgo for github is really all
of these workflows that are there to
help you work with
algo for github and
the one action that i want to
promote here is the very last one here
update algo system files
as you probably know if you have created
a
github repository based on
a template then you kind of
took a copy of that and now you're lost
with
how that template looked at that point
in time
well not with a go for github with that
one you can apply new changes to the to
the template you will you will never be
lost in an old version and you'll always
be running towards the version of algo
that you originally took and then you
can update to the newest version
and
simply have the latest
innovations and the latest bits of ailgo
for github
just by running
workflow
so with that
for more information
i'll be at the ask the experts booth
today if you have any questions on that
akms algo
and then
our al go for github group on yammer and
then my blog of course
and i'll leave you with two statements
one of them is
that people saying that they're too busy
to set up devops
is kind of like a woodcutter who's
saying he's too busy to sharpen his saw
right
and then
i did claim
that this could be used for all partners
but let's see if
boxy can you use that as well
for his
development team
thank you freddie
this looks
amazing can you hear me yeah so thank
you freddie this looks amazing and yes i
must admit um
you know this is certainly usable for
developers
and i actually want to make an
announcement here
because we are going to use this because
we obviously want happy developers as
well
i can see them smiling already
so we are moving the system application
to algo for github so the system
application is already
on github but to be honest the way it
works today is that the master the
source for this this is our in internal
repository and then whenever you know
we make changes to it we we actually
create a pull request to move those
changes to github so github is not the
source
today
but we're going to change this
we're going to make
algo for github the primary environment
for developers
and for testing of the system
application
and that means that our developers in
microsoft will making pull requests
directly
in github
and you'll be able to follow it as it
happens and you'll be able to comment on
it and you will also be able to
contribute to it
directly on github just like our
engineers
and and with that i actually want to
welcome you all
to the new system application team on
github welcome to the team
[Applause]
so let's take a little step back here
talk about what we have done on with the
application on github so far
so right now we have 83 extensions
on github and that's actually excluding
the local variations and test tools and
all our tests there
at the last time we met here in 2019 we
had about 30
extensions there so it's been increased
being a lot here
similar on the system application we had
about 40 the last time we met and now we
are 81 so also more than double that
amount so
it's great to see all those
contributions to that
and we just alone the 42 you know the
last year we've seen 42 contributions uh
that actually made it into the product
so there's been some that didn't make it
into the product of course but 42 that
made it into the product so thank you
all for those contributions uh to to
github and to making the application
better
and if you want to contribute there's a
couple of akas on the screen here
where you can see how you can get
started on on contributing to this
so what is next then for the application
on github where do we want to take this
um
we have a lot of extensions already and
we have the system application now on
algo for github
and that's obviously the the first step
here
the second step is that
every new feature that we built
whether it's something that that's small
or it's a local feature or if it's a
major new thing you know we're going to
make that as an extension and we're
going to make that or make that
available on github
a good example for that is actually the
shopify connector that we built
here last released last year you know
that is a extension on github so you can
all see and follow and contribute and
comment and what to do
similar
whenever we take functionality out of
the the base application
and that could be uh you know some w1
functionality or it could be some local
functionality
then we make it into an extension
and we put it on github and a good
example of that is the interstat
functionality that we are shipping in
the next release here
where we have taken into stat for for
actually from multiple localizations and
created one big interest at
implementation that's going to
eventually replace those
we put it on github as an extension and
you're all welcome to see and contribute
to that
right now we have as you probably all
know the ideas website or
dot msl bc ideas
and we have github as another source for
uh
you know getting feedback from you uh
and from our customers
and they're not totally aligned
you know so the bc ideas have this
ability to vote
so you can suggest features and others
can vote on those we don't have that on
github yet but on github we can kind of
uh we can have some code development
going on and that's really powerful as
well and we really need to align these
two things so uh maybe we get some
voting capabilities into uh
the
github
or we get some contribution capabilities
into bc ideas
but we need to align these and and our
dream here is that we can have some of
the features that
is on bc ideas that we actually have a
collaborative engineering experience on
github on so we actually start
implementing some of those ideas on
github
so we need to
be aligning these two
and finally i also want to announce here
that we do want to start taking a
pull request for the base application
this is something that we have had
requests for for a long time
but in all honesty you know if we look
at all the checks that our base
application goes through before we can
actually ship this
it is pretty difficult to to get
take pull requests from this but we are
going to pilot this and hopefully we
find a good way for for handling all
this
so going forward we can get
more and more of the base application
there
and are actually also taking real
pull requests on the
on the base application
so as you can see we are doing a lot uh
and and the future for the application
is on github and we are you know step by
step moving closer and closer to getting
more and more
of the application on on github so we
can all work together on on on this
great application
thank you boxy
thank you boxes i really look forward to
your contribution on
on github and on
on on the app i'm looking for the
clicker
here it is all right
so um
a couple of things about technologies
and a call to action
i'm going to talk about a few things
here that that might impact you uh and i
think i wanted to we thought we wanted
to give you a heads up on on these
things so the first thing is the move to
oauth
so so what is that we are moving towards
what does that mean that means that
the web access keys also know that basic
authentication
is deprecated and we will remove them
from the product very soon
and you should be using oauth2 instead
why are we doing that well security
security security as we move to the
cloud we need constantly to harden on
security and the move to us too is part
of that so we're moving the entire
business central to this much more
secure way of authenticating
and when is this going to happen well
actually now we were supposed to remove
it from the product already in the
spring release but we could see from our
telemetry that
a lot of you were still using it uh so
we kind of held on to it a little bit
more a little longer but we are going to
remove it on the first of october so
there's still a little bit of time but
if you're using web access key you need
to go and refactor your code otherwise
uh any
web access you do to bc will stop
working
there's a sample on bc tech uh
at this link that shows how to
uh how to do a rest client using roster
you see it's pretty simple there's it's
not very different than using web apps
as key
and you can you know use that that
sample as a starting point
the next thing i want to announce is we
that we are moving to dot net core
and what does that mean well we already
have quite a few components pretty much
every component is in business central
are already on.net core but uh one of
the last one and the hardest one we had
to migrate was the nst and the industry
will be running on.net core very very
soon
and that means for you that you have
server side.net add-ins uh you need to
migrate them to dotnet standard at a
minimum
uh actually there is another option
which i'll um talk about in a in the
next slide which which is the one we
recommend
for you to move
and stay compatible with net core
so why are we doing that well dot net
core is
offering significantly better
performance
and although um you know the net
framework is still
is still supported it's effectively in
sustained engineering
and your entire azure is on.net core so
if we want to leverage other services or
the libraries
we also need to be on network ourselves
in order to stay current and evolve with
with azure
and as i mentioned the net
framework is is on sustain engineering
and dot net core is really where
microsoft is investing for the future
and and doing all the improvements
uh when is this going to happen well um
2023 what is wave one this is when we
will release
dotnet sorry nst on.net core so be ready
for it and you should start go and and
update your server side add-ins uh
before that how many of you have
server-side edits
well i don't see many hints that's good
that means there's a
lot of work to do uh so the the the the
architecture we recommend to move
your your server side add-in is um is
the following if you have a server side
and it looks like this
you you have some
dot net code and um you probably call it
through or you call it through a.net
interrupt either from an extension or
possibly even through the customized
base app
and what you could do when uh
everything will be running in the dot
net core
runtime is migrate your own add-ins to
net core but if you reference a third
part library
third-party library which doesn't have a
dot net core version then you will not
be able to do that so instead what we
recommend is to move to a cloud-ready
architecture which looks like this
and in order to do that it's pretty
simple you take your server side add-in
and whatever
third-party library you you reference
and put them in a function app in the
cloud and that's pretty straightforward
and very simple and instead of using
donate interrupt you call your dotnet
server side add-in through http request
and and that's it and whether your nst
is running
on-prem or in the cloud that doesn't
matter
this works
so this is really truly the architecture
we recommend
there is a sample on bc tech
again uh
where there is a
sample code before
the migration to a function app and
after so you can see how it's done
so go and check it
out now
um
we come to the section that we know you
enjoy take days it's a tradition we
always have a
section called from the lab where we
show you things which might or might
make it might or might not make it to
the product the prototypes experiment
we're doing
i've shown things uh in the past
where which never made it to the product
but uh you always give us the feedback
that you like that section so um you
know this time shouldn't be an exception
although the things i'm going to show
you now i'm pretty sure you know i'm
pretty confident they will make it to
the product because we are very very
close
um so
let's start with
the first
prototype i want to show you
which is actually
something that is a
more of a user feature
so
when we you know we have a lot of lists
in the business centrals i'm sure you
you're aware of
and
um
if i
look at my sales order here for example
we have
um underneath
to display that that list we are using a
um a a web control which is a grid
control and we are going soon to replace
that control with a with a much more
event advanced one uh which can do a lot
of things and and
gradually we'll we'll we'll turn on some
of the feature that this grid can do and
i want to give you a quick um a quick
appetizer of what what what's possible
so
um
if i go here and you're familiar with
the tile view for the list
the last menu item called analyzes you
will not see it in the product that's
the prototype part but if i turn the
grid here on analyze this mode
i can
you can see here i can do a lot of a lot
of cool stuff for example i can go and
let's look at the amount
of my sales order i can mark some of
them and you see at the bottom
the sum of it you know the min and max
the count so something you might be
familiar with from from excel i can do
that directly now in the product without
without having to export to excel
i can
do
grouping for example by
customer names so i have my customers
here and
i can go and you know
expand and in a kind of tree view you
know do some grouping
i can go and pin that column on the
right
on the left sorry which you can do all
well with or we can already do that with
the um the grid we have but i can also
pin another column here
on the left if if i sorry on the right
if i want to and it's very useful for
example if you have very large very wide
lists right
let me show you another cool feature in
that as well let's go back to
grab the the amount
column here
and
if i go and
show you know marks
mark my my customers with the amount of
product ship
i can do a
chart here
so i can see you know by customers i can
see the amount the amount shipped here
and and you can go and just again
directly in the product i can go and
show a
pie chart or other advanced charts if i
want
i can go into pivot mode as well and do
all sorts of cool pivot things i can
pivot on the on other dimension for
example on the status of my order
either on the
horizontal axis or or
vertical here you can see about the
status of my heart on the top so
really a lot of cool feature in this in
this grid where you can do
on-screen bi
with your data
so that was that was the first
you know cool pro top i wanted to share
with you
thank you
[Applause]
so now let's switch to um back to the
developer just somewhere you know most
of you are developers so um
i said the best for the last
um so one of the things we're going to
release pretty soon in the visual studio
code extension
is um
the um al development central so that's
a great there would be a screen
a tab that will appear when you start up
visual studio code if you want
and we will be able to push some feeds
and information about al and about all
developments so
you know great way for you to get news
and and about what's happening with
their developments new features in the
compiler and officially base code and
only for real so you might find you
might be familiar with a similar
page there's a page like this in visual
studio for those of you who know it so
this is the basically the equivalent of
it but for al and l development
so this is coming very soon
now
how many of you have been using seaside
in the past
yeah lots of hints lots of things so uh
when we uh when we move to uh to visual
studio code um
some we you know we kind of you know we
move some of the functionality that that
we're in in seaside we had the object
designer
and some of the designers so as
i'm sure you you've noticed they are not
there anymore in visual studio code and
instead we went for a more text-based
approach so we replaced this with a more
advanced intellisense and some snippets
uh which is basically what uh visual
code is is about it's a it's a text
editor but you gave us some feedback and
some of you i'm sure are still
missing the object designer and some of
the designer so
we've heard your feedback and
you know this is something that we are
going to release very soon and this is
the el
explorer
which is
what
the object designer was to seaside it is
to visual studio code here so i can see
all my objects here
uh from from my from my extension and by
the way the grid that is used here is
the same grid that i showed you before
same controls i can also do a lot of
cool stuff i can filter by you know my
own extension here which i have only a
few objects here
i can go and bookmark some objects
and filter on the bookmarked objects you
know typically that would be the objects
you are working with
i can go and filter by type or group by
type so i can see all my code units
you know i can go and combine these
filtering you know i can see all my code
units for my extension my pages
and of course i can navigate if i double
click
on the on one of the object i navigate
directly to the code as you would expect
right
so this is coming very soon in
in uh in the al vs code extension
now the next part i'm going to show you
now it's it's not quite there yet we're
still working on it but i couldn't
resist showing to you you'll see there's
a button here called design so you won't
see that in the first iteration of um of
this release
but if i go and click it on on my table
i'm opening a designer here and let me
uh
let me split this on the right
and then i go and
reopen
this in text so i have the designer and
the code side by side and then i can go
and do the things that you would expect
and you that you missed from uh from
seaside i can go and add some you know
edit some some property without writing
any code and you see you know my code
get updated
right away
i can go and also edit the code here and
you see this full round trip between the
designer and the code
now take a look at the fields here
i might want to change for example my
picture fill to uh to something else
and my screen is a little bit cramped
here let me
i can you know if i if i want it to be
say a media set instead of a blog you
see it's changed here
and i can change it back to a blob
uh
and so forth so
this is coming very very soon uh not in
the first iteration you'll have to be a
little bit patient but uh
but we we are going to release that i'm
pretty sure even though it's in the from
the lab session
on the other objects you know if i look
at a page there are also some cool
functionality where i can
go and take a look for example at the
layout and show it as a
you know as a tree view
so it gives me an overview of my layout
so i hope you uh thank you
so i'm sure you i'm sure you'll be
looking forward to uh to the designers
um
we heard your feedback and it's coming
to you very soon
now before um before i let you go
enjoy the rest of the conference
uh
i will share the roadmap for business
central um for the upcoming release the
upcoming release is is there very very
soon and these are the um
the the themes of this release we we've
done a lot of investments in in making
business central a uh a seamless
uh service in terms of operation in
terms of performance
uh we've invested in onboarding to help
your customer get started faster um
with framework there
horina talked about the power platform
and we make a lot we made a lot of
investments there as well
and teams
and of course the developer tools and
productivity is always an area where uh
which has a lot of um a lot of love from
from us and from from from our team
again
bc tech
aka.slashbystick go and check it out
it's a great resource for
samples for
videos dashboards there is
there is some some powershell script
there so go and check it out you can
contribute there as well we welcome
contribution
um it's a it's a really great resource
uh
place
and if you want to know more about some
of the things we talk about this this
keynote of course we we only had time to
scratch the surface so you only saw the
tip of the iceberg but there are some
sessions where
you can go deeper in some of the
subjects we addressed here um if you
want to know about more about the
business central performance toolkit
there's a full session about it
bugs you talk about permission we also
have an entire session for it the 45
minute stations for this
uh open source um this is a session to
go if you want to learn more how to
contribute
troubleshooting and we have as much as
three sessions on the
microsoft 365 and the power platform
and there's tons of other great stations
that's just to name a few the stance of
gray station i mean look has put
together a fantastic program this year
again
thank you again to be such a great
community thank you again for being so
engaged into business central
and enjoy the rest of the conference
[Applause]
