# BC TechDays 2023 - What's new in AL

- **Source:** https://www.youtube.com/watch?v=LwnMz0j9EXc
- **Video ID:** LwnMz0j9EXc
- **Channel:** mibuso.com
- **Published:** 2023-06-29
- **Duration:** 44m18s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

bit of audio there we go welcome
everyone
in the next 30 40 minutes we are going
to talk about what's new in Al it's
gonna be a lot about the AL extension
and what we've put in there and what
we've made of changes in there a little
bit about the language but we're going
to try and see if we can cover
everything probably not all of it but
most of it we have a lot to cover just
from the things we've brought today
we're going to talk a lot about Al
Explorer code analysis framework we're
going to talk about productivity
improvements we're talking we're going
to talk about the ale improvements the
attached debugger scenario and some
telemetry
so today I have Blanca with me here and
she with me are working on the developer
tools team and she will kick it off
there you go
yes
so let's start up with the L experience
home which was one of the latest
additions with this last release we have
already seen it in the keynote but let's
look at it a bit over again
so um Daily Explorer is a tool that you
can find as part of the AL extension
it's a webview and here you can navigate
and explore your code
it also allows you to understand the
structure of your code by providing a
very comprehensive overview so uh maybe
newcomers can get a more familiar more
easily with with your application
it also allows you to interact with some
of the the objects you can for example
go to source code you can run some
objects you can bookmark and some other
things
and it's also quite useful to discover
accessibility points so here you can
find those points where you can extend
and integrate the application
so let's look at the how it looks like
live yeah
so this is what DLX Pro looks like from
from Little extension
um yeah you have four tabs here
the first one is the objects one you
have a list of all the objects of your
application and also all the reference
objects so so the ones from your
dependencies
you can also um search any object if you
know it's ID or name you can also group
them by um
several aspects here so for example yeah
like a type
can also see the modules so
here for example you can
filter them by the bookmark so if you
are working in a with a set of objects
maybe in your development process then
it's quite handy because you can find
them here very easily
then the four other tabs these are the
extensibility points
um so for the events
here you can find the list of all the
events Publishers event that you can
subscribe to
and you can easily do it from here
then you have the apis tab so this is
also the list of all the API pages and
queries
um so if you want to access your
application from an external Source then
you can easily look here which one you
you can use
and last of all we have the extensible
enums that Implement interfaces so again
if you want to extend your application
um
in a structure manner then you can use
this extensible enums
and this is the first step that I we are
taking
um towards kind of creating these
development development Hub where
developers can access it in their
day-to-day and have only Sunny tools
just from one single UI
and with Al Explorer we also have the AL
home
this is also a webview
um and here is where we will share the
latest news for you
um the Developers
so we might share some important tips on
how to for example more productive and
efficient
um like some performance patterns we
might also share some important
announcements so maybe any upcoming
features or changes or any bugs that my
uh might be important for you to be
aware of
and it's also
quite nice for for us to see some
features for you to discover that you
might not be very familiar with
so make sure you have this enabled if
you want to receive the latest updates
yes and then we also did some
improvements to the code analyzer
framework
so the colonizer
um an ICS framework
um it's a big component in the perceived
performance during code authoring this
is because every change you do while
coding for example while you're typing
this will trigger are you calculate
recalculation of all the code
Diagnostics so of course if you have
large applications this can be a big
performance over here
so to save you from this headache we
made a few improvements here
so for example we optimized when the
rules are run oops
we also fixed some efficiencies and also
disable those rules that no longer run
and one of the biggest
[Music]
Improvement um
one of the biggest changes here is that
we added this new file scope
so this means that a code analysis only
runs on the current file
um
so of course this is a big performance
Advantage because you don't have to run
it through all the files you might lose
some Diagnostics but most Diagnostics
are local anyways and you can also get
the full Diagnostics to an apple
um so this has
a few advantages for you
um that you might have already perceived
so
you can now use code analysis regardless
of the size the size of your workspace
also if you have a big application you
can also continue to use a code analysis
because we will only look at the current
file
and then um
you can so some also some developers
would disable this
big performance overhead so you no
longer have to wait for um the CI CD
pipelines for doing a full build
and you can customize this using the
background code analysis setting
so this is a new setting that we have
added the current behavior that we have
is that if you work with a workspace
that is smaller than 105s so small
workspaces then we run all the code
analysis for all files unless you have
it disabled
but if you are working with workspaces
that are that have more than 100 files
then you use the background code
analysis setting to Define that behavior
and here basically you can set three
values
you can set it to to file or true this
is the default setting that we discussed
before and this basically means that
code analysis will only be run on the
active file
you can also set it a project which
means that this will run on all the flag
all the files of the active project
or you can also disable it by setting it
to none so no code analysis will run
this also depends on the scope where you
set this setting so of course you can
set it out folder level
um that case it will only apply to the
current project
you can also set it to the workspace
level in that case it will apply to all
the projects in the workspace
or you can also
set it on the user settings which will
apply to all the projects all the files
in all the places in all of the
workspaces
and then for dependent projects this of
course depends on the setting that you
use for that project and basically it
will only run core analysis on that
project if you have the background code
analysis setting set to project
also within this colonizes improvements
we also added a new parameter so output
analyzer statistics setting which
basically shows you a summary of the of
all the rules that were run and also the
time that was spent per room
so it's quite useful because it will
allow you to discover which routes are
running and maybe you want to disable
some of them because they are not very
useful or relevant to your case
so you can run a faster
and you can also see which rules are low
performing so you can also disable these
rules
um during code authoring and then you
can also get them later during the full
build or through the CI CD Pipelines
and another Improvement that we have
made within the colonizer framework was
that we now support URLs Forex external
roof sets
so this makes it easier to share and
maintain
um
and of course common common rules
and there are basically two ways you can
do that so the first way is that you can
use the AL rules and path setting
and then you specify the the URL for the
external rules set and then you can
disable or enable this pass using the
enable external rules so you can you
don't have to change that that URL
and then the second option is that you
can use you can add a URL in the include
reset setting in the rule set folder
using the the path parameter
and then you can also use this from the
AL compiler using the enable external
rulesets parameter
and then as like in every release we
also added new analyze rules so there
are quite a few of them I won't go
through all of them in detail but let's
look I have another view of what are
these ones
so um
we have added quite a few rules
um for the app source code
um
rules so we have added some rules
regarding the protested variables
breaking changes so for example if you
name it or modify them then there are
some rules to cover in those changes
then we also added a
a setting a rule to this to learn about
changing normal tables to temporary
then we added also a few rules regarding
a permission set extensions
um basically because you can use them to
Grant more permissions that you intended
to
then we also added a
[Music]
um for
the name sorry about that the name yeah
so for the business events we also had a
business events so of course we also
added some groups against that
for the per tenant extension cups we
also added a similar rules regarding the
permission set extensions
and also some rules for the the
application property
we also added a new UI code rule so for
um when the actions um in the with the
repeater scope
and then we also updated a UI code blue
regarding the about text and about title
properties
rules we also are ruled to the
so when you use a pragma weren't stable
you have to specify explicitly the code
say of those Diagnostics that they are
disabled in them instead of disable all
of them because some developers will
forget about that
and then a similar rules for the
permissions set usage
okay so let's look a bit more into those
new permissions set extension rules
because they are quite a bit everywhere
so basically with the permission cell
extensions
right now we have value rule or several
rules that um to detect the cases where
you use a permission set extension
to improve permissions for an object or
a permissions that is defined in another
application so you can use this to
extend permissions
um
exiting permissions in another
application
and you can also use a wild card
permission to Grant Global access
so we are adding Roots against that
and why well basically because this is a
very bad practice
so um this coming in current security
risk
uh by granting excessive religious to
users so in the first case you can our
user was an existing permission can
create a permission cell extension kinda
extend its own permissions and then can
publish it up
so it can basically extend it so
permissions and have more permissions
that what it was original intended to
and then also Wildcat permissions can
also be a security risk because you can
get more or Grant more privilegious than
you you would like to
so this is not enforced for upload PT or
submission
for appsource submission at this point
but it might be enforced a later point
or we might just not have support for
doing this in the future
is going to talk a little bit more air
productivity
let's see
yeah
so
thank you for this overview of some of
the analyzer and productivity
improvements there we've heard a lot of
your feedback and we've spent some time
on the team to think about what are the
things that we can do to help you guys
be a little more productive
um we can't bring back Seaside if
anybody is interested we're not going to
do that but let's look at a few of those
things so one of the things we looked at
was the temporary identifier so when
you're writing codes and you don't have
the Declaration of a variable in scope
it can be really hard to see whether a
variable is a temporary variable or not
unless you name your variables them so
forth maybe not everyone does that but
it can be difficult so we added this
intellisense here that gives you
insights into the fact that this
variable here is a temporary record
and you can all see the benefits of that
we've also changed the way we use
identifiers in events
so normally today you would specify the
the event publisher by specifying a name
in a string
and that is
it works but it's perhaps not what we
wanted we wanted it to be a symbol so we
made it an identifier which unlocks all
of the greatness we have in initial
Studio code for references
so one of those great references is the
code lens and when you use the code lens
or when you change your your event
subscriber or your event publisher into
an identifier you can actually see who's
using it here by clicking
link there the link in references okay
so you can see here we have a
event
that we can now see both the subscriber
and the publisher in one View
which is really nice
it allows you to skip through the
different implementations where you have
a subscriber and actually see what the
different implementations do okay
it also works the other way around so
when you go and click on the name of the
publisher press F12 you can go to that
publisher
so how do we change this
it's quite easy we made a code action
for you so it's pretty simple
you just have to change the string into
a identifier and then you're done you
can do that using the code action and
you can choose to do it for all your
subscribers in
the current document the current
workspace project you name it very easy
there we go one two three
should be super easy for all of you to
do it so you get the insights that
Visual Studio code can provide for you
and make it much easier easier for you
to navigate through the different
publisher and subscribers
we took this idea also to interfaces
where we added the go to implementations
so this allows you to pick an interface
and see all the implementations of that
interface quite easily right click press
go to implementations or control with 12
if you wanna
use the shortcuts
pretty nice
as interfaces is one of the key
components of building the usable and
nice maintainable code it's also very
nice that we can actually now go oops
oops ah one more we can actually go and
see all the implementations from a
variable so I have an interface
decoration in my code unit and I can see
all the different implementations here
so I can go and check which one I need
to go fix or add the new one if it's
missing and so forth that's pretty nice
okay
you do that there and you get that
overview
okay
so last release I think it was we added
the ability for you to move application
area from a field and up until the page
level so you didn't have to write
application area everywhere
some of us have been writing Pages for a
long time with application that area in
there so cleaning that up is a bit
tedious of course we made
a function for you to remove those
redundant
those redundant application areas
and we made another one to promote
okay
to promote those
and again you can do it on a workspace
on a project and on the specific
instance or document
okay more more to come
when working with the multiple projects
you might find it a bit challenging to
either copy or download the dependencies
between all those projects
we've now made it possible for you to
specify additional package cache paths
and then you can share now the
downloaded or copy distributed packages
between all your projects having them on
a shared folder or download site or
something so you can easily get access
to it
another path related change is for
folder pass for control add-ins
some of you might have tried this you
need to specify a million different
resources for control add-in one at a
time you sit there and type them in hope
it's all right no typos and everything
now
you can use a wild card isn't that nice
and it works
even for scripts style sheets and images
and now you don't have to type in every
single file and it works if you add a
file that is also added all these things
that's really nice
okay
let's stop with some of these
productivity improvements and talk about
the AL improvements
and I'm going to go through a few of
them not all of them but a few of them
a new one is formatting so on reports
you now have a format region
which allows you to render a report in a
different format that when your current
session is in
so you can have a Danish guy in the
Danish session actually rendering a
German report which is quite nice
there's a language table that you can
use to find the language ID that you
need in order to render this go try it
out
on records we added the read isolation
property that allows you to control the
lock escalations
it requires some knowledge and some
training on that I recommend you to go
and look at the session tomorrow on
locking in here
to learn much more about this read
isolation property
we've also added the set table on record
refs now you can actually work on the
same data both in your record ref and
your record
which is also a very needed feature
on streams the in-stream specifically we
have added maybe a bit overdue
I would say position and reset position
which allows you to control the position
on your stream and actually reread
very nice
some of you might have used inherit
entitlements and inherit permissions we
have now alignment on these two
functionalities that allows you to write
code where you control both the license
in terms of entitlement and the
permission
from code giving you the ability to
write a poor business critical processes
that should work regardless of whether a
user has permissions or has entitlements
this helps a lot
okay
now I'm going to talk about entitlements
for licensing so how many out here knows
about monetization in business Central
one two three four five six oh a few a
few okay so this is gonna be Technical
and it might be a bit tricky so bear
with me I'm just gonna use five minutes
talking a lot about entitlements it's a
passion of mine
okay imagine a scenario I want to uh
create an appsource app that has
licensing support out of the box
I want to support two scenarios gold and
silver
one or two and I want to make sure that
there's a trial scenario for new
customers and I want to make sure that I
support some custom licensing that I
used to have so in my existing app I
might have called out to my home server
and said hey this AED tenant is trying
to access some feature can you do that
and then I would allow him to continue
or not continue whether or not he's
registered with me I want that
functionality to continue working
okay so the first thing I do in my
feature here is my application is to
create
a couple of feature sets so this is the
way I like to do it you can do it
whatever you like we need to Define some
permissions that covers areas of my
application that I can need to turn on
or turn off depending on what license
you have
so here I have three features
then I'm going to define the maximum
permissions a user can have if he's
assigned one of my licenses so I'm going
to define a gold permission set that
includes the features that are available
when you have the gold license
I'm gonna do the same thing for the
silver and then finally I'm gonna
do a trial
and why am I doing a trial here is
because there's really no
trial support in the licensing that we
get from
from Microsoft so we need to build in
license or trial license into our
product so this will cover both the
trial well add some kind of date check
and the custom licensing
on the same maximum permission set okay
so far so good everyone with me
let's try the next step the next step is
to define the license
so the first thing I do is I create an
entitlement that defines a license for
my gold in this case
and it could look something like this
so here we have my my gold entitlement I
Define it using this new entitlement
type called per user of a plan
offer plan comes from appsource you have
an offer in app source and you have a
plan that actually defines this kind of
license
then you define the the ID as being the
fully qualified name of that plan in in
appsource
and then I map it to some permissions
yeah you can't really see that here but
the last line there of object
entitlements is the permission set that
I defined previously the maximum
permissions for my gold
scenario
okay I can do that also for my silver as
you can see here again
per user of a plan and I Define the ID
full qualified ID of my plan in
appsource and then I say these are the
maximum permissions these are the things
that people are entitled to when they
have my license
finally I need to do the same thing for
the trial
here because we don't have really a
trial but we do have something called
unlicensed so I will use the type on
license so when a user comes into
business Central and is using my app and
is unlicensed these are the entitlements
so these are the maximum missions he's
entitled to use
so far so good
one key thing to mention here
the way entitlements work the way you're
entitled to applications today the
Optics in your applications today is
implicit this means that when you upload
an app to business Central you have
access to all the objects
so you are licensed to use all the
objects in your application
then you add permissions on that on top
of that to control that when you add one
of these entitlements objects in your
application the implicit entitlements go
away
so when you add the first entitlement
object in your extension that is the
only entitlement a user will be given
based on whatever requirements you put
in that environment the no more implicit
okay
so far so good
now
then I need to use this somehow right
so let's see how we can use that
so here is an example of some code
uh I could write I could use all the
existing permission system we have I
could use access by permission and say
if you have execute right to something
then you can get access to this action
here I'm using the details of the
permission set so I know that this
object may only Grant you access
permission or execute permission in my
gold or in my silver scenario it's maybe
a bit tricky to use it like this you can
also use the normal like read access or
write permission or read permission
write permission from an object like a
table again you're looking into that an
object exists with a certain permission
in a certain permission set it can be a
bit tricky so we want something easier
to say whether it's gold or silver or
it's unlicensed right
okay so here I have another scenario
this is my do work app
the first thing I'll ask here is whether
the current user is entitled to my
entitlement set right
so this will essentially tell me whether
the user that is currently signed in is
assigned a license that entitles him to
my entitlement set
if he is then I can do something and
then we're all good
the next scenario here is whether or not
the user is analyzed so a user is coming
in
I've defined the unlicensed entitlement
set so therefore we can know whether the
user is unlicensed for my application
if he's not unlicensed but he's not gold
then he has some kind of license but not
something my code supports yet so I need
to throw an error obviously
Okay the third scenario here is custom
licensing so if I know he is unlicensed
and I have an existing custom licensing
model then this is the place where I
need to go call home and say
is is the person licensed in the old
system
if he is hey we continue doing that and
last but not least we have the trial
scenario where I can maybe save the date
for first time he does some kind of
operation and then validate whether it's
been 30 60 90 whatever it is
and that's my trial
okay
if you want to try it out it's currently
being released it's a still in public
preview as I
yeah it's around public preview right
now
um and you'll find it by this small flag
in appsource where you can choose to
sell through Microsoft yes I know if you
choose yes
and you define a plan then your plan
will show up in the marketplace this is
a Hello World example but still it
proves the point when you go to the
marketplace you will see the list of
plans and prices and the customer can
buy direct from the marketplace if they
so chooses
you can have hidden plans and other
configurations that allows you to
control this more granularly maybe ship
it to specific customers with specific
prices and so on all of that to be
learned more on online look at the
documentation
if you're all staring at a blank here
and saying what's an app and what
appsource tomorrow we have a nice
session oh actually today we have a nice
session on appsource the Miss devices
demystifization if I can say that word
so come talk to us about that and listen
what we have to say okay
enough with licensing even though I love
licenses we have to take it back a step
let's see oh yeah plants and yep there
we go
okay
let's go one back one step back into new
things in ale external business events
we've talked a lot about it both at the
keynote at the sessions around power
every apps and Power Platform and we're
also going to talk about it here because
it's really important
the new business external business event
is the only way you can raise events
outside of business Central
there are some equipped hooks
look-alikes today in business Central
but this is the right way of doing it
and this is what we're going to use
going forward
we talked about permissions this is
another way of doing permissions you can
restrict to who can subscribe to these
external business events by putting in
the required permission
here you could say you can only have my
gold
you can only use this if you have my
gold subscription for example
okay you can even do custom
categories
by extending the event category enum
let's talk about errors okay so with
error info we added two new methods the
add method or add action method that
allows you to add a button where a user
can invoke some kind of code unit method
where maybe we can fix up some data or
run some some other code that will do
something to get the user out of trouble
or we can add a navigation action where
the user can perhaps get a setup page or
maybe they open the record where
where the issue happened
it can look something like this
now I'm going to turn it back to Blanca
who's going to talk to us about more
error things in the debugging scenario
yes so um one of the big things that we
also came up with in all this release
was attached debugger for regular
debugger
so this was also a highly requested
feature and here it is
so um basically here we've done a few
improvements to regular debugging and
from now on you can
you can debug any existing user session
so that means that you can of course
regularly back your own existing session
as you could do before but you can also
debug any other user session
so it's quite useful if you for example
have a customer and the customer
encounters an error then you can log in
um well you can access there um session
and you can debug that session and you
control that session and discover what's
going on
um you can also debug any next session
also for any user
so this is also quite useful because it
blocks the scenario of service to
service
um
course where there's no user in both so
now you can actually do do this with a
regular debugging
um and with these improvements we
achieve parity between snapshot
debugging capabilities and regular
design capabilities
so everything that you could do before
with you had to do before with Snapchat
debugging now you can also do with
regular debugging so now regular
debugging is even more powerful
um for your everyday development
on the decent blocks of few scenarios
um so you can connect to an existing
session
um using the user ID
so to this you need to get the user ID
so if you are working for um you want to
debug for example a web planning session
then you can go to help my support
finder the session ID and then you can
copy that
um and then you can in your launch
configuration then you can add that the
session ID
um and debug that session
and here note that the break on next
parameter here it's not really important
because that session IDs
um sufficient
um
to know which session it is so we don't
need to specify that type of session
you can also attach to an existing
station for a specific user so um in
this case you you can you specify again
the decision ID and you specify the user
you want to debug the session for so the
owner of that session
if that user turns out to not be the
owner of that session then that debug
request will fail
um and the last of all you can also
attach to the next session of a specific
user so if you want to debug the next
session of a given type
um you have to specify that type with a
break on X parameter so that can be a
background session a web service session
or a web client session and then you use
this user ID to specify that the user
you want to to debug
that's session four
and if you want to know more about that
um just stay for the next session
um we will talk about more regular
debugging and so on
within the context of all the debunk
capabilities that we have
with the I turned a bit earlier but for
Telemetry we also have some improvements
for telemetry
um
so um telement is something that many of
you probably can take more advantage of
um you can it has many applications it
can give you great insights of the
activities and operations in other go
inside your application
you can also see the errors that use
this encounter you can also diagnose
them and diagnose them and help you
troubleshoot those issues using the
telemetry
you can also analyze the performance of
your application
um
CNA database statements or any
inefficient daily methods
and you can use this information to self
mitigate these errors so you can do it
with a for yourself
um you can also have an in-depth
analysis again of the performance of the
usage of
of the different aspects of your
application
and you can have a better understanding
of the customer usage and challenges
on the if you're not very familiar with
it I want to get started you can check
out our link with
AKA dot Ms BC Telemetry samples where we
have some sample Telemetry and you can
use it to play around with it and get a
feel of what it looks like
um perhaps use it for for your own
scenario
and as we also mentioned earlier in the
keynote we also have ai insights on this
data
so as for the improvements themselves
we added a
we cannot troubleshoot the errors that
users can see so you can see which
errors are these where they come from
what they are and so on
can also do a similar thing with those
permission issues that users might
encounter
you can also see information about the
login performance so you can see for
example if there were any
long Rhino methods or any long run SQL
statements or
or any log timeouts and so on
I also see more insights on the long run
nail methods so you can see which one
are those how much time they're taking
and other quite Reliant information
you also have a Telemetry on outgoing
web service performance
[Music]
um
then you also have Telemetry on the app
update so you can see which app updates
failed the data transfer usage and so on
you can also track performance of the
test results over time so not only for a
test run but also throughout the
different test runs
and the last of all you also have
Telemetry on the usage of algo for
githubs so the different algo events
that were used and which were which one
are are these
so let's see ability what this look like
in the UI so one of the the solutions
are you can now troubleshoot there is
that users can see so you can see uh
which customers are experiencing these
servers and how many you can also see
the message of of course what this
errors say not only in the language of
the customer itself but also in English
so I guess that's very helpful if you
don't speak the language of your
customer
and you can also see where do these
errors come from where apps do they come
from
before you also have this other view
with the permission issues
um you can also see which customers are
experiencing these permission issues you
can see what else do they see and where
they come from
and yes that was C for Telemetry and for
our presentation itself
you can check more resource here if you
have a question you can enrich some
Yammer if you're looking for more
resources then make sure to check ABC
all
um some of your ideas and busy ideas you
have here all the the relevant links if
you want to contact us
if you have here some interesting links
also if you want to get started and we
also added a survey here so just make
sure to check it out if if you want to
say something let us help us understand
what do you want what do you need
um by answering that survey
and
yeah I think that's it for
representation we have time for one
maybe two if they're short questions
anybody want to try out this one we have
one over here yep
here you go that's a pull through
there you go
it should be turned on try again
no can we turn on the orange one
try the older one ring the other catch
box which we tried the other one then
yeah so maybe just one question
but then you get a t-shirt also now
we'll throw it
hand it over
no no
let's try again maybe just State your
question I'll repeat it
attaching to the session yes if
you're back can we debug background
sessions using that can you debug
background sessions using a user ID that
is a good question
yes um can we do that
I would say normally I would say yes
because we can debug background sessions
so having a use ID on that should be
fine now in front of all of you I might
be wrong
[Laughter]
but please try it out give us a holler
if it doesn't work and we'll see if we
can get it to work
thank you good question though
we can do one more
one more over there yes
ah
you can create all the rules you want so
the question the real question is can
you get it to run with our rules
and as it is today no there is no simple
way of doing that there are attempts out
there in the community people who hack
into this and get it to run with our
rules but as we speak today there's no
prescribed way of you adding to our
rules as such you can add your own vs
code extension that does your own rules
but not add to ours at this point
go to PC ideas add your vote click click
click click click yeah get it up there
get it prioritized
okay that's it for us thank you very
much for attending and please stay here
for the next one
[Applause]
