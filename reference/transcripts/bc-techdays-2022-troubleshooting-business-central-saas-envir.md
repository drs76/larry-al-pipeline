# BC TechDays 2022 - Troubleshooting Business Central SaaS environments

- **Source:** https://www.youtube.com/watch?v=fhLhEs-lZd4
- **Video ID:** fhLhEs-lZd4
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 44m05s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

thank you
foreign
all the screens
[Music]
I'm coming back down
tonight
[Music]
ladies and Gentlemen please welcome
Kalman Perez and Nikolai Dobrev
[Music]
whenever you're ready
yeah
good day everybody so welcome to this
session on troubleshooting business
Central on SAS environment
my name is Carmen Beres and I'm here
with here with Nikolai Dobrev my
colleague
the first time ever
so his first presentation ever so bear
in mind
yes
thank you
[Applause]
okay so today agenda is we are going to
talk a little bit about telemetry
then we are going to delve more into in
client tools
then we are going to show you some of
the debugging enhancements we have done
for the October release
done more on Snapshot debugging and a
little bit on profiling thank you and I
give the word to Nikolai hello welcome
everyone
uh welcome to today's session I'll
probably cover some of the topics that
you already saw
uh in the keynote earlier today
so you you heard about Telemetry Vincent
talked about it
however we can't really talk about
troubleshooting SAS environments without
mentioning telemetry
so
tomorrow will be another session about
it where you can get in-depth knowledge
but we should point out what you can
actually learn from Telemetry you can
get information about all kinds of
events and what has been performed uh on
your environments also a new thing from
this release is our power bi which was
the power bi app which was demoed on the
keynote you can find it here on that URL
please go and visit
in addition to telemetry
and in addition to the incline profiler
that you saw presented by the Ida we
have multiple other tools in the in
client in the client that you can use to
troubleshoot your environment we have
multiple scenarios that can be covered
and you can discover issues only in the
client
so I'll take you on a journey uh to the
web browser where we can actually go and
see how powerful the client is
so I'm opening the browser now
and our our first stop is how we can
troubleshoot the connectivity I believe
you see yes
so here you can see a checksum with
different steps and basically what we do
here is we check the connectivity
between your in this currently our web
browser to your tenant
so I'll run the check you can see
everything supposed to be good yes it is
good if something fails for example you
fail to log in or the CDN is down you
get actually an information and hence
what might have been wrong and how you
can fix it so let's jump to business
Central
you can find the connectivity check
actually on the usual business Central
URL and if you have different
environments you can go slash your
environment name and then slash
connectivity
so we have the business Central here
open and I'll jump to customers
and we'll start our journey from here so
what you should first do when you have
issues and you want to find information
in the client is to go to the uh the
question mark button up here and then go
to help and support you saw that page
earlier today so I won't really cover
much about it
but I want to say that up here in
troubleshoot you have useful links to
for example get to know the last known
error apparently known errors in that
environment you can inspect Pages or
analyze the performance using the
inclined profiler
uh you'll hear more about performance
later yes
down there we have report a problem here
you can get metadata that is very useful
for us so when you have issues you
should send us for example everything
that is up here and we can see also
information about your client and server
session ID so please remember that
server station ID because it will come
in handy later in that session and you
can also enable additional logging
so let's go to inspect pages and open
the page inspector here for example you
can get information about all the table
fields and what extension they're coming
from we can see the extension we can see
page filters also which are applied on
that page we can see the extensions
besides The Usual Suspects system
application based application you can
see that I have a demo extension now
we'll discover what it does in addition
you can see how long each of the
extensions has taken or they have
contributed when you open the current
page
so what does my extension do it actually
doesn't do anything good so I will show
you I've added two actions here the
first one prepare our press and the
second one is do harm let's see what do
harm will do
so I'll jump afterwards to employee list
it's another custom page and I'll try to
add an employee just a demo employee
let's say John Doe and then an address
test and we can see that it hangs we
cannot save right now so what is
happening we can go to database logs and
try to see information up here and we
can see that there is a database log on
that particular table so we can't really
save the information and you can see
also from which session ID that database
lock has been acquired
and that's actually the session ID that
I showed you earlier
so when we talk about databases and
writing to to databases tables and more
we can also explore all the data you
have on your current environment by
going to another page called table
information here you can see statistics
about each one of your tables it's it's
a very big page that's why it's loading
uh uh each one of your pages how many
records it has what is the the each one
of your records how many tables it has
how many uh Records it has what is the
table number what is the size
of each one of them and then index size
and more on what else you can do is you
can for example click on the number of
records and that one will open another
page where you can inspect in details
the data for that current
table
you can see all the fields you can also
change the
The View and here you can see all the
fields and the data field over there
in addition to that table information we
have few other Pages related to
databases so let's just type databases
and see what we'll get
so the first one that I'll open is
weight statistics we already saw
database logs let's go to a statistics
here you can see sorted by category
how long you have waited for certain
operations to to be performed uh you can
see when that operation has started how
long it has taken and more
and then the the last one related to
database
performance is not actually missing
indexes so what do we do in business
entries we analyze all of your queries
to the database and we're trying to
improve them right we can't really alter
your code but we can give you
suggestions so what we do here is we
analyze your queries we see what type of
queries you do and and we we analyze if
you have actually indexes added for
these certain
search fields and then we can suggest
you missing indexes currently I don't
have any because that's a test
environment but you can see yours up
here and that will boost your
performance
good we talked about databases let's now
talk about another scenario let's
imagine that
you're writing AO code
and you have subscribed to an event
but your event never gets fired and and
your code never gets executed and that's
what Ida showed is the event recorder
and I don't have the time to actually
demo it live but if we go to a vent
recorder
page we open the event recorder what I
usually do is I open it in a in a new
window
and then record the steps of the
scenario where you expect your code to
be executed you get something like this
and that's a list of older events that
have been triggered during your scenario
you can see some of them the the code
that the type is event trigger which is
the system one then there are custom
events and then you can check if your
event
that you have subscribed to is the right
one and then you can analyze why it
hasn't been triggered
good
let's jump to another page
which is called effective permissions
so here you can analyze for each one of
your users what permissions they have so
what problems might solve that is if you
for example have single users which
cannot let's say
run a report or they cannot log in then
you can come here and you can analyze
per application object
if a certain user you can change the
user here if a certain user has
permissions to execute read and more you
can also see them by permission sets
good
what else we can take we can see here is
scheduled tasks
and that's an overview of all the
background tasks that are running on the
current tenant
you can get more information
by going to show job queue details you
can get information about the recurrence
of the task
you can also get information about the
timeout for example the object where
that task has been implemented its ID or
the type which can be coded or a report
and when I mentioned reports I want to
show you something that's the last thing
let's let's just go to I don't know
sales orders
let's open sales orders it's a list page
and let's try to report so what you can
do is I guess if you have events
subscribed to when you publish a a
report you can actually go and analyze
the data without actually publishing it
by opening the request page and then
pressing consent to and then here you
can you can select uh in what data type
you want to export that report
and let's say we open it in Excel
and then we say okay and in a second we
downloaded
a report and we can open it in Excel
you can download it as raw data you can
also download it
together with the layout
and then you can analyze everything that
is up here
okay with that being said we'll move to
the next topic
and common will take over
thank you
[Applause]
so
let's talk a bit about debugging
enhancements and let's jump
with a demo
yeah so I was clicking around in order
not to kill this session uh in order not
to waste time for you that I start up
and publish something so I have here a
small app that is already debugged
oh
you can't see my screen can you
okay better
sorry
let's go back so I have here can you see
uh what is that what so I have here a
small app
and uh what he's going to do I'm
debugging that in Visual Studio code
so I'm attached to this session
if I click on the action here you know
like show locks I mean it's revealing
already what I want to show yes and Ida
she was talking about that so in the
database statistics we have added you a
new entry that's about locks so you will
see from now on as you debug on each
frame
what were the locks taken
so if I go here I just you know I there
was a log the customer table and I did a
fine first
then if I continue I modify the item
table so there was another lock taken so
and I think this will be helpful for you
as as we continue
we may add more things here but uh for
now you have locks
so let me go back to my presentation
and what other enhancements have we done
so
we have added you a new setting
to exclude temporary record read write
so if you specify that you don't want uh
to break on temporary course then you
can you have a new option for that
we have a new setting to exclude
breaking on
try functions on errors there
and we have already already added a new
entry that besides your application
object you can also specify which
startup company you are going to use
when you say F5 or Ctrl F5
so let's jump to the next topic that's
about snapshot debugging
so how many of you have used snapshot
debugging I think yeah okay good some
yeah yeah good well so what is Snapshot
debugging so let's try to Define what we
are doing here
so you can imagine snapshot debugging as
being
it's really really something like that
it's a video recorder
but it doesn't takes frames picture
frames it takes stack frames so what it
does it listens as El executes on the
business Central server and it records
or stack frames and given well-defined
points which we call Snap points it is
going to take context and what do I mean
by context at these points these
well-defined points we are going to take
all variables globals and locals
and so snapshot debugging is not as
intrusive as normal debugging we could
never allow you to debug
production environments with the real
debugger the only way to do this is the
snapshot debugger
so in a nutshell how do you do this
operation so everything starts from
Azure Studio code
you set your snap points and then you
start the snapshot debugging session
then you perform your scenario and then
you stop snapshot debugging and download
a snapshot file this will be a local
file on your disk which you made it
debuggable
as any debugging you know snapshot has
its own launch.org configuration so let
me just mention a few things that may be
different and completely other than in
other
debugging types so one is the session ID
the session ID is an integer like
decline has just presented to you can
see it on the help and support page so
what does it mean if you specify a
session ID in your launch.json then a
snapshot debugger session may try to
attach to that session if it finds it
then you can specify a user ID
this is the ID of a user that you want
to attach to
then you can specify something called
snapshot verbosity
uh so El execution so Al itself as the
web as any client communicates with the
server is quite a chatty operation so
there are many AR calls so if you don't
want a large file you can only say that
I want to collect uh stack frames on
Snap points
and then you can specify an execution
context and a profiling type and what
are these you know snapshot debugging is
also used for profiling so you can you
can you can specify whether you want a
debug profile or both and if you are
profiling what kind of profiling you
want to perform but later on these
so what are snap points I was all
talking about you know what are these so
they are nothing else but break points
but there is a big difference between a
debugger breakpoint and a snap point is
uh that if you do a snapshot debugging
session you have to sort of know
what you want to what you will do and
you have to place these breakpoints snap
points ahead of time
because these are the only places where
variables are going to be collected
so how do you do all these things you go
to visual studio code you create your
snapshot Json file and then basically
you use the command
or you press F7 so when you have
initialized the snapshot there are many
things that can happen if you specify
the session ID then it will immediately
connect to that session if not
is going to sit on some business Central
server and it's going to wait
for the next client that you specified
with a break on next to connect
you can view all snapshots like clicking
this button here
on the left bottom side of Visual Studio
code and that will show you the status
of our snapshot sessions that you have
started
so when you are done with your scenario
then you press alt F7 or you shoot a
command and that will basically download
you a zip file
so let's just go through the states
because you know this can be confusing
when you do snapshots so there are four
states there is an initialized
that's when the server is waiting
to connect to an ex-client then you you
have started it
and when you when your state is started
that's when you should do your scenario
and when you finished it then yeah
that's the finished it and then when you
have downloaded a snapshot then you can
debug it so you can only debug
downloaded snapshots
and uh yeah warning so you know snapshot
debugging more or less happens on
other users
connection so that other user will get
notified by this big dialog box that you
know somebody's sneaking into your
session
and because of this you know not
everybody can do a snapshot debugging
session so you need to get this
permission set
and so all the other things that we have
in debugging like resource exposure and
non-debuggable methods and dynamic IP
protections are respected as with the
normal debugger I said that snapshot
debugging is not as intrusive as the
real debugger but it's still you know
you are basically fishing on a
production server where many other
people are doing their job so you know
we have some limits you have only 10
minutes for a scenario
and so once you are in initialized state
you have 30 minutes to get to a starting
State otherwise your session is going to
be kicked out and after 10 minutes
whatever you record it that's going to
be your snapshot
yeah so once you finish then you
downloaded a file that's a snapshot file
it's downloaded to the snapshots folder
you can override it
uh with the snapshot output bus settings
one thing to note here that the snapshot
file so on Snap so on Snap points we
collect variable informations and
variables are considered gdpr compliant
data
so handle it with care
I mean you can yeah you can distribute
it but you know just be aware that you
know it may contain gdpr compliant data
and so once you have a file downloaded
you can debug it
so how do you debug it you just click on
the left hand side
button to show all your downloaded
sessions and then you select one and
then debugging will start and then how
this is working is
if you collected snap points then it
will be the first snap point that is
going to break
if you don't have snap points but the
execution triggered an error
then all errors Al errors I buy design
considered as snap points so there will
be context on on errors and it will stop
on the first error if you have none of
these then is the first stack frame but
then probably you know your your
snapshot is not very much usable because
yeah so you don't have anything
okay
so let's demo this thing
so
yep
okay for this scenario
close
okay so this is a
risky scenario let's do this one yeah
it's it's a you know we are going to
snapshot debug web API course yes
and what happens here I I prepare
Postman
that it runs one of my API pages that I
created
and what happens is
my web API cores are running on behalf
of this customer you know this is the
one that is running the web API called
the snapshot debugging will be done by
delegated admin not this guy
so I hope you know how to set this up
you know the first thing we have to do
here when we do
uh web API debugging so we have to get a
bearer token for for this guy yes and in
order you have to set up certain things
in Postman so you have to fill out your
client ID and client secrets you can
find that in the app that you have
registered uh with Azure active
directory
and the same app that is registered for
you in Business Center or somewhere so
let's get a new access token for this
guy
okay
so I'm going to use this access token
to actually
do
a web API core this will take some time
and hopefully it will show something
yeah so you know we have an error yes
you know and the task now is snapshot
debug this error so see what happens
okay
to do that
I go back to visual studio code and as I
mentioned
I already set this up I don't want to
waste your time you know I have a
launch.json it's very simple it does you
know it just connects to a production
environment this is what I show you it
happens on a production environment
and
yeah this is my code so you know I
already set up just to prove how this
snap Point thingy work
I already set three break points here
okay now I'm gonna say F7
on this one
yeah it's doing something
the snapshot debugger initial request
has succeeded so something appears here
I have something initialized oops
oh you can still see only I can see
okay
so if I go back to postman
and I repeat my scenario
then in principle what should happen
here I should be able to finish it and
get a file
see it's already finished because web
API sessions are coming going yes
so let's download this one
yeah so we got to find so let's try to
debug it so I click on this button
and I open this snapshot file
and once it opens it stopped at the
first snap Point okay so what I said
that you know that on on these things
and snap points you have variable
information
okay
so if I press F5 now I should hit the
next snap point
good so I have variable information
if I press F5 again
then I get
to some call what I wanted to emphasize
is and the reason I put this snap Point
here is I don't know how many of you are
knowing that you know it is the debug
console that I use most to evaluate
variables so in this state at this line
all you know all variables are there so
I can just take this content as text and
see what's the value
so you have
evaluated the reason I'm saying is that
if had this been a large tax like you
know one kilobyte or dated you wouldn't
be able to see you would only be able to
see chunks of this
okay and the gutter appeared
looks like we have a bug because
originally it did not appear so what are
these so these these lines are the lines
that have been executed while you took a
snapshot session
yes so for example this wasn't called
but these were called
and then if I press F5
then I get to this place which is an
error condition I did not put a snap
point on this one this just appear
because errors are treated as uh as snap
points and we are always going to take
information on that one and you know the
reason why this failed is that my
exchange rate is not set up correctly I
mean this is still good old times yeah
look at this one it's yeah this is how
it looks today
you were always going down
okay
so
let's continue
one second
yeah so just a little recap so what's
the big difference between debunking and
snapshot debugging yeah snapshot
debugging is available in production
basically that's it normal debugging is
not available because it's an intrusive
one you know imagine you put a lock on
the customer table why a debug
okay so the next topic is profiling
so we have introduced the profiler the
AR profiler a year ago as I remember
and
what is that so a debt profiler the one
that was released one year ago is based
on something we call instrumentation so
instrumentation is based on on snapshots
and uh let me just illustrate in a
a small demo what it is doing so you
know let's imagine that we are executing
a procedure called fool
so as as a snapshot goes it starts as we
entered we've got the stack frame for
Foo we start recording and we record
then Foo was calling some other method
we record that one and then you know we
gather the time when other exited and
then we get her the time on when Foo
exited and what we get out of these
we have actually measured the so-called
full time
of how much Foo has executed but we also
know the self time so these are two
concepts in the profiler terminology
so a full-time follow method is
everything from start to the end
self time are basically you can think of
it as the instructions plus system calls
no other AR calls okay
the next release I think this was yeah
it was in Spring we have introduced a
new profiler which is called which is
based on another technique called
sampling
so what's the difference between the two
one
sampling is a way
less intrusive operation so it has much
less overhead
and
the but there are there are some
carriers that not all cores are captured
you know so you may miss information but
it's good enough to know what went wrong
in my opinion
instrumentation on the other end is very
resource intensive it contains more
details but the file is big and
everything yeah so you know depending on
your scenario you can use one or the
other one
we have ex okay so let me let me just
tell you a few words about this sampling
so how does this work so imagine that a
drum is beating at 100 milliseconds
on-prem you can customize this 100
millisecond to your own wish so at let's
assume that you know first 100
millisecond passed then we are looking
at Al execution we are looking at the
frame stack frame and we can see that
the run method was called then another
100 millisecond passes
and then we see that Ron was calling foo
foo was calling bar and bar was calling
small we record that too
then another 300 milliseconds path like
this
then in the
300th millisecond you know so either
we had run coiling full bar or small or
else or smaller ones called
and then execution comes back to run and
either and as the stack we are always
looking at you know what was on the top
of the stack and how much time it was on
the top of the stack and from this logic
we can deduce what was a methods
own time or self time and we are going
to do some algorithm to deduce what was
the full time
and by the end you get something like
this in Visual Studio code
yeah the sampling profiler has two
usages
one is in the incline profiler it's
actually very simple either she has
shown it to you
uh
and for hardcore Developers
you can do it from Visual Studio code by
specifying in your
snapshot Json file that you want to do
sampling and not instrumentation
so
let's demo the ER profiler
the good thing I'm not going to demo the
sampling one because that was shown to
you now let's go back to the good old
one the instrumentation one and why am I
doing that because uh you know
previously I did the snapshot debugging
session for you so let's see if we can
get some profiling data out of those
snapshots
so for that
I'm going to run a command generate
profile file
and then you know I have a few snapshots
here let's choose the last one
so this is going to generate me
something called a profile file you know
a profile file is basically
you know we have our own extension and
we have an editor for this this editor
that you can see it's an a you know it's
called a CPU profile file but in
principle it's it's following
Google's chromium output
so what do you see here so you see here
this is called
top down view so you see core Stacks as
they were happening
yes so what you see here that you know
on aftergot character code this method
and then I actually you can see the self
time and the total time so get exchanger
is what it was taking one second
and then yeah I have a method do some
delay which you know was taken one
second
uh and that's it you have another view
called bottom up
in this view we are going to show you
each frame and who called into that
frame so you know it's the inverse of
what you see before so for example if
you want to go full path like get the
exchange rate was called by
get latest exchange rate this is a base
article it was called I get exchange
rate it was in my code unit and so on
and then everything started far on after
get cool record
these are sortable
these columns and there is a very simple
query language in here
that we have developed for you so you
can we are compiler team so we are
providing parsers so you can press press
here
and add sign and then type something and
then you know it gives you some help
that these are the commands that you can
use for example I can do something like
s
like served and greater than three
thousand there is nothing like that you
know so 300 and then it will go show you
all the all the frames that had that
information
more
if you have the source code then or in
the symbols then you can go to
definition by just clicking on any of
these
and that's very helpful because then you
can analyze okay so this took one second
but what actually took one second there
yeah so that said
let's continue so I was mentioning that
this is one view yeah so you know this
air CPU profile it's it's an editor yes
what what if you don't like this you
know
because I said this is chromium
technology so in principle
you should be able to to see all this in
other
profilers that support chromium
technology let's just take a competitor
one
let's see if you feel the prior for
Firefox profiler we can open our profile
okay before that let me just take the
pass that I don't search a lot here
so load profile from a file let's see
what happens
yeah
it understands it so this is you know
this yeah this is a very good profiler
by the way you know it's uh it has a
much better UI I have to admit that so
you know but it doesn't show the
information so it won't go to source
code and uh it you know we are we have
additions to this chromium
output and those of course will not be
seen here I can repeat the same scenario
for you in F12 in in Chrome or
or Edge in the developer tools I can
open the same profile file there too
okay
so back to the slides
so what about you know I'm gonna finish
with this this this slide here so you
should use the incline profiler it's a
very very
easy tool even and even your end users
could use it and then us developers can
get the air CPU profile file that was
created by the in-client profiler and
then you can open that in a visual
studio code AR project so just as I'm
mentioning so if you get downloads
things from the incline profiler and you
double click on it it's not going to
open we don't support yet initializing
the AI language server from the entire
profiler
and then if you want hardcore profiling
then use Visual Studio code with
snapshots and samplings that is going to
get you more detailed data you are not
going to lose
frames as with instrumentation but
instrumentation is also very helpful if
you just want to get started and see
what is slow in your system
with this
I think we are done
and don't go away you know because we
are going to continue
our colleagues are going to continue
with the migration part
so let's just give them like two minutes
until they they prepare the presentation
for you thank you very much
[Applause]
so next session Cloud migration our
speakers Roman cyber Julia and Nicola
