# BC TechDays 2023 - Unlock the Power of AL extension toolset: A detailed overview of AL code debug...

- **Source:** https://www.youtube.com/watch?v=2GBRAiupenE
- **Video ID:** 2GBRAiupenE
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 39m55s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

yes so hello everyone again
we also in this presentation and Thomas
with my colleague Thomas hello
so welcome to unlock the power of the
Galaxy 2 set where we will give you a
detailed overview of the AL code
um debugging and navigation
so for today's agenda we have a
so we're gonna look at three main things
first up it's a total shooting so we
will look at the different dividing
capabilities that we offer as part of
the AL extension so not so much as for
example the incline tools
we will also look of course at the L
Explorer which we have already seen
before since it's an important aspect
for navigation and the exploration of
your code
and last of all we will look at all of
those proactivity boosters that we will
have also as part of the L extension and
how to use them to be more proactive and
efficient
so first up is troubleshooting
so for this section we will first look
at the overview of the debunk
capabilities that we have
and then we will focus a little more on
regular debugging as we saw before there
are quite a few improvements in regular
debugging so we'll go through all of
this
um and then we also go a bit deeper into
how to debug the different type of
sessions
um under the break ones that we support
if you want to have a
broader overview of all the
troubleshooting capabilities that we
have in business Central then there's a
session last year also I'll take this
that you can check out
but let's get started with the debugging
overview capabilities
so probably speaking we have two types
of debugging we have regular debugging
and Snapchat debugging
many of you or most of you are probably
familiar with regular debugging this is
the kind where you set the breakpoints
in your code
um and then when the code execution hits
those breakpoints then you can inspect
the variables live
um and so on
whereas Snapchat debugging is a bit
different Unity said the snap points
ahead of time
then you initiate the Rebellion session
then the code executes no breakpoints
are hit and then you can once the
session has a need then you can Replay
that session and then you can inspect
the variables
so these two types have very different
capabilities that you need to be
familiar with so you know what can each
type do and what can they not
so the most important difference is that
regular debugging only supports sandbox
environments
whereas the Snapchat debugging supports
both sandbox and production so of course
if you have production environment then
use the snapshot debugging to throw as
you did
um then launch debugging so we thought I
mean a pressing F5 that launches the
browser and you can start debugging
that's only supported with regular
debugging
attached to an accession of a given type
this is also supported on both um
types of debugging
attached to an existing session given
its ID also support in both note that
these are also recent additions for
regular debugging
attached to a next session for a given
user also supporting both
debugger session belonging belonging to
other user also supporting both so again
if you want to debug another user's
another developer a customer session
then you don't have to reproduce
reproduce it from scratch then you can
just
debug that existing session
um without having to start from from
scratch
real-time control so this means being
able to as code as as code is executed
and being able to inspect the arrivals
to pause they pull over
um instead more breakpoints and so on
this is only supported in regular
debugging
um not in Snapchat because of course as
it can run in production you don't want
to stop your code as it's running
profiling information so if you want to
see the performance profile information
this is only supported in snapshot
debugging
and then replaying the debug session
this is only supported as in Snapchat
debugging so being able to replay that
scenario over again through the Snapchat
file that's only with Snapchat debugging
all right so I will see for the
capabilities
and because of this we also want to use
regular debugging and snapshot debugging
in different scenarios
so for regular debugging it's very good
while you are actively developing your
extension this is because again if you
want this traditional debug controls of
being able to inspect said breakpoints
and so live
this is very good for that
and also allows for faster publishing
because here for example when you launch
you publish the application so you can
already start
um debugging whereas in snapshot you
have to first
um publish it like a upload it and then
deploy it and that's exactly longer
so in general if you are working with a
Sandbox MRN then you want to
um use regular debugging because it's a
more powerful than Snapchat debugging
and then for Snapchat debugging a very
obvious one is that if you
have an environment then you are you
have to use Snapshot debugging
if you also need performance profiling
information Snapchat debugging
and also if you want to share the debug
resource of a session uh the snapshot
debugging you can also share that
snapshot file with other users so they
can also take a look at that debugging
session
all right so that was C4 the two main
types of debugging now let's look a bit
deeper into regular debugging and as we
saw before there are three types or
three ways of
regular debugging session
so you can launch your own session
you can attach to an existing session
well you can attach to the next session
or you can attach it to an existing
session
so many of you who have already debugged
in visuals in vs code
um but in business it's a bit different
because they use user is in one machine
but the session you want to debug is
another machine so let's see a bit of
this magic that's going behind the
scenes and how it works
for each of the types
so if you are debugging your own BC
online session then in that case you go
to this code you press F5 initiate the
debugging session and the cluster
balancer will find a node where to
initiate the Divine context
and then the browser will be launched
launched and then the cluster balancer
will direct that request to that to the
note where the debugging is taking place
uh when you are attaching to an existing
session it's a bit different because in
this case we already have an existing
session running one of the nodes
so in this case when you launch an
existing session and attached to access
session requesting vs code then you need
the idea of that session
then the cluster balancer with this ID
will search which one of the nodes has
this session
and then once it finds it then it will
direct that request to the node
and last of all if we want to attach to
the next session
then also vs code will send the the
request the cluster balancer will find a
node
and then the node will wait 10 minutes
um for for a session of that type to be
initiated
so when there's a session of that type
initiative then the cluster balancer
will hopefully find the node
um
and then initiate that debugging
session there
all right so again these three different
types of debugging session also have
different capabilities
so um if you want to Target a session
belonging to other user then you use
attach to an extra attached to existing
if you want to Target an assistant
session then use attach the existing
if you want to publish an extension
before debugging this is also only
possible with a launch debugging
you can debug web client sessions with
all the different types and this is
something also new for attached next
you can also debug no web client
sessions but this is a
usually want to go with attached to next
if you want to debug service if service
cost
um
you can also do that with attachable
system by Saving trigger getting hold of
the ID so in this case use attach to
next
um then only with launch you can specify
the startup option of a object ID and
object types so when you launch the
browser then it will initiate a
it will open that object so you can
start debugging
and then launch and attach next are
available for versions of BC and that
has to exist in is something that we
have added from bc22
okay so when do you want to use each
type of debug in a session
so launcher session is best suited when
you're actively developing the changes
um
yeah you can quickly launch it and then
you can see unexpected variables also
it publishes it before you launch it so
again you can sorry publish the you can
really start debugging and it's very
powerful if you use right because it's
way faster this is because it only
computes the differences so you thread
if if you have already done a full
publish
then attached to next you want to use
this when you debug a non-web client
session
so the minority of the time this is when
you are debugging a service to service
calls
this is on also the only way you can
debug install and upgrade code units
and also again there's this 10 minute
Timeout on how long this will wait for
the session if we exit that timeout then
that the back session will be uploaded
and finally attached to existing
use attach your existing if you want to
Target an already existing session so
again if you are very close to to doing
something and finding the problem and
you don't want to reproduce it from
scratch
or you also can have another user who
can reproduce that issue then you can
attach to the access sensation either
your own or another user session
um yeah how you specify this you use
this you can start this through
different configurations in the
launch.json file
for launch it looks something like this
the most important part is that request
essential launch
then you can specify the startup object
type and ID
and also the tenant is quite important
if the channel is not on your idd then
you can debug another tenant if you're
delegated on me
and you can also use one of our Snippets
you know how to memorize this by hard
for attach you next the request is set
to attach
then the most important part is that
break on next which defines the type of
session you want to attach next so it
can be web service client a background
session or a web client
and you can also specify the user ID of
the user you want to to attach to the
next session
and also we have a snippet that you can
use for this
and finally attached to existing here
the important part is to specify the
session ID which you can do through this
parameter
okay so that was quite a lot of theory
now let's look uh
a demon action
so let me show you how you can debug
another user session
so let's start
by starting here my way planned on a
user so I'm connected as Alex Wilbur
and I will go to customers and find a
customer card
and here I want to try this new
extension that the assets are filled the
membership number
so I will
type something here and okay I see an
error so I not sure what's going on
because the message is not very
descriptive
so I will go here to help and support
I will find the station ID
we'll copy that and then I will send
that to my developer or my partner
right so now I'm gonna be the partner
um
so I'm doing a bit of routine here but
uh as the partner I'm gonna
go to ABS code I'm going to start a
on a touch configuration
and here I just need to specify the
session ID
so I would like that in here
all right and now that I'm done with
that then I can start the debugging
session
so it's a publish
and then I will go to attach
one important aspect about this is that
the user that you're gonna
um do the the debug request has the
permission attach debug otherwise it
won't be able to do so
so in this case I'm I'm connected as a
I'm logged in as administrator
one
yes and you will see here that I I am
already attached to something
so if I'm here the customer I will try
to reproduce that
so we can troubleshoot it
and once I enter that then I will see my
vs code that we have actually hit the
breakpoint of the session so you can
start to see what's going on
so yeah that was quite useful to that
so now let's look back into the
breakpoints which you of course want to
use for any debugging session
so we support regular breakpoints but we
also support more advanced breakpoints
we have conditional breakpoints and
implicit breakpoints
so conditional breakpoints are very
straightforward you just set a
breakpoint in your code
you right click
then you go to edit breakpoint
and here you enter the expression so if
this expression evaluates the true then
we will hit the breakpoint otherwise
it won't be hit
an implicit breakpoints these are a bit
special so these are for specific
scenarios where we can break without
having to explicitly specify breakpoints
for each of the cases and in this case
is when we have errors or when we modify
records
and we do this using these two settings
and these two parameters in the launch
Json configurations so we can put break
on error
so this parameter specifies what to do
when it encounters an error you can set
it to all to break for all of the errors
you can set it to exclude try uh
want to to exclude those errors within a
trying function because you are already
handing them in some way
or you want to set it to none if you
don't want to break on any error
likewise you also have a break on record
right so this specifies what to do when
a record is modified you can also set it
to all so we'll always break when our
record is modified
you can set it to exclude temporary so
it will ignore temporary records
and you can also set it to none so it
won't break when a record is modified
okay so let's see this in action for
implicit breakpoints so when I break on
a record to break on a when I record is
modified
so I'm gonna go back into my web client
here
I'm gonna first
the attach
okay I'm gonna try out
I'm gonna go to my items list I'm gonna
try a new action
that I added for for the item card
but first i'm gonna attach to that
session because I don't want to break on
all the records that perceive that
um so I want to attach exactly when I
execute that action so I'm gonna go back
to my launch configuration
I'm gonna
break on here I'm gonna go for all
and I'm gonna launch that configuration
again
oops and I have to of course I have a
new session so I need to make sure that
I
update that
because otherwise it will fail so I'll
try that again
yes so now I'm attached
and then I can try Direction
and then I will see that I will
um hit on those when our record is
modified
all right so that was seated for a
debugging in extension and now Thomas
will show you some more cool things you
can do with Al extension
all right there we are I can hear myself
now perfect
so yes we just saw blanket how she was
able to attach the the debugger
um to her current session but we are
working on a uh on a slice here so we
can actually improve this experience
right here so that's what I want to to
demo for you right now
so what we have is that we can go in to
loot
so in here I have my own server running
and the first thing we have done
is that I want to learn more about the
customer
so I go into help and support
and I'm going to inspect the page
and now I can read all about all the
table fields and extensions that are
attrib contributing to to this page
right here
but what I'm really want to see is
available is probably the source code
behind this page right here
so we have added now a link you can
click here
and
just make sure it's the right one that
hits when we click on this one it sends
you directly to the page that you're
looking at so no more looking around for
the right name and the right ID and
whatnot
so given this object right here
we can now go in and let's say I want to
debug the on open page on this page
right here
so next thing I would normally do is I
would go into my launch.json here and I
would start typing in my attach
configuration right here
but here is the second half of where
this new feature will come in so we'll
close down the page inspector and we
will move back to the help and support
page and normally we'll go down copy the
session ID
but here we have added a new link for
attaching the debugger so now we click
here on this link that sends us back to
the studio code instance again
and now we'll ask you because I'm in a
sandbox environment what kind of
debugging do I want to do
but this one I want to do regular
debugging so it will create me the
launch configuration that matches my
choice here and with all the parameters
I have
and it will then style up the debugger
with this configuration right here
it's already right now you can see I
have attached successfully to the
current session right here
and if I then move back into my
my tenant here and then go in and
activate the unopen page
spinner because now it actually hit the
break points and we are in full swing
with our debugging session right here
so this is coming
sometime in the future here but it
should be coming in the next major
so that was it for our new feature that
will make it easier to debug
next up is that you can't really not
talk about the Explorer
it's the the tool that we've developed
for you to easily get an overview of all
of the objects events enums whatever you
have in
your projects and all of the
dependencies
so if we go back in here
then
I want to learn more about this price
assets
system here so I can go in I can find my
objects and I can quickly go and see the
source codes
and see there's this wonderful enum
right here I want to extend the type so
I can go back
go into extendable enum and
I can find my enum in here and from here
I can see okay
I know it's an extendable item that
implements an interface but what is the
interface that it's implementing
okay so now I have this the name of this
interface right here
and then I can go back
and I can get started on implementing my
my own code unit here for this interface
right here so this is one of the the
common use cases we see for the Explorer
where you want to discover and
understand
the code you're working with
but I won't bore you anymore with it
we've already seen a few demos of it if
you want to know more about it we just
had the the watch new just for the sake
of the recording and we also had a great
demo of it in the the keynote so let's
just move on for now
instead what I want to focus on is some
of these productivity boosters that we
have put into the products and that
might not
be known by everybody so maybe go
through some of them so again code
actions we've seen them before
um
but they're just so great it allows us
for
have an easier uptake of all of the
features that we're doing so you can
quickly get going and you can utilize
some of the new work that we are doing
here so for instance for for code units
here where you have interfaces do you
want to implement
we already got it covered we have a code
action to say
having to implement all of these
functions right here is
some work and
here the compiler can just help you with
it so it will generate you all of the
functions that you need to implement
um for this given interface right here
yeah you've already seen some of the
code actions here we have a list of
um of the ones we have they're split
into two categories either we fix
Diagnostics errors and warnings for you
or we are fixing up a code from
refactoring point of view
for instance when we moved from the the
previous promoted actions properties now
into the new modern action bar those are
the the kind of
refactorings you can do with code action
so far and there'll be more coming uh I
can already promise that
so the next thing I want to show is go
to implementation
already showed you that if you have an
interface and you want to understand who
actually already implements this one you
can go in you can right click and you
can see all these code units right here
but another thing you can do as well is
there might be big code units in there
so let's just go directly on the
procedure and ask for the implementation
of this procedure right here and then we
can go in and navigate directly
to the given feature uh the given
procedure
so
these small Improvement so you can
easily navigate everything here
next up is the type hierarchy
so
this is also kind of interesting in the
in the sense that the AL language is not
really an object-oriented language so
when you see type hurricane
highlighted in V Studio code from other
languages such as JavaScript or c-sharp
or what have you then you see a way
bigger tree of this but
with the typo key in Al you still get a
good overview about all of your
extension objects for a given object
right here so let me show you how that
looks like
if we go back
here already prepared a page extension
and I have the page right up here and I
want to see well I added my trigger in
here but what else might it be there
I'll say show Type R key and now it will
give me the list of all the other page
extensions and I'm going to navigate to
them
and see what kind of modifications are
they doing
so this can also be quite helpful to
understand where all the the changes to
my page or my table or my emails coming
from
next up is semantic code coloring
um and this one is a dear to me so
when we're looking at code such as this
one you see there's a lot of
I mean we have basically three colors to
work with right here and a lot of white
text for all of the identifiers
so we can do better here uh
so right now we also see that actually
the the current sort of way of coloring
here is based on a on a system called
text mates
basically a
set of regex rules that will just match
up on the given text that we have right
here so with these semantic
highlighting here we can actually do
semantic coloring off of all the the
words and the tokens right here so you
will
it will use the compiler
to tell what are we actually looking at
here so let me enable that and we can
have a look at this so we go into
settings
and we see
oh
we can label it right here and we move
back in and all of a sudden way more
colors
and if we go back to our page extension
we see that the text for instance now
has a different color and we can know
the difference for it we can also see
that instances like this where you have
a local variable of the name company
name and you also have the built-in
function of the same name shows that
what's going on right here
but some of you might not actually like
the way that we color things or might
want to highlight certain special
scenarios right here
so what you can do is you can either go
in and make your own theme and
set up
all of that or there is a more
lightweight way of going about this
so you can go into your settings
and you can make a custom set of rules
here
so for this one I'm saying
for these semantic tokens of parameters
I want to give them an italic underline
font style for the built-in functions I
want to call them green and for these
text made tones right here I want to
color them of the type keyword operator
I want to color them red
and now some of you might ask well but
how do I know all of this how can I
discover these tokens right here
so
we will go in and there's a wonderful
tool provided by Visual Studio code to
discover all of these
um classifications we have done
so if we as soon as we open that one up
you can click around and you can see
but this word right here
we have the semantic token of being a
parameter
and then that means that we are calling
it in certain way what we already see
right here that the the rules that we
put in through the settings is applying
now and we get the italic underlined for
the parameters the built-in functions in
our green and we can recognize them
from the other ones that are just yellow
here
and all of our operators turned red
so you can do whatever you are your
heart desires here
here all right and that was it for
coloring the next thing is
sticky scroll and this was also a
interesting feature that the vs code
team added that we
made available through our language as
well
and the benefit of sticker scroll here
is that in Al you have a lot of nested
elements
so when you go in and you see a page for
instance you see there's a page and it
has a layout it has the area it goes
into a group and it's the indentation
just go on and go on go on and sometimes
you get hard it can be hard to keep
track of where are you
so
this one we can go in
we can say well let's enable sticky
scroll
so this setting right here
and let's go back to our page and now as
soon as we start to scroll down we see
that the first line sticks to the top of
the the document right here and then as
we continue down more and more lines
starts to stick because the scope
we're narrowing in on
and of course I should go down you're
welcome
[Applause]
yeah
look at the point it follows your scope
one additional thing I would like to add
is the default setting is only set to
five indentations or five levels and as
soon as you get the first action in
you're already above five so
for this one I increased it to 10 and
that's how you can get into like the
field level
so that's what we have for for sticky
scroll right here
and the last one I want to show you is
global launch configurations
so for those of you who might be trying
out a lot of different ideas creating a
lot of apps
um
having to start up new projects all the
time
this might be uh the way you want to go
because then you don't have to create
all your launch configurations for every
single project you can store them
between every single project
so how do we do this well we can store
them in settings and for now
this is just the settings for the
projects what we already seen from
blanket earlier that you can also store
them in the workspace or in the user
and how do you then specify this launch
configuration well you go in
and you say I want to have a launch
setting right here it has a certain set
of configurations and then you have the
same object right here as you would
specify in your launch configuration
it's just a copy paste of it
so here it's just a launch to my sandbox
but it might as well be your Docker or
what have you
and with that that was all I've had for
showing off some of the interesting
features that we have added to our Al
language extension for view Studio code
if you want to learn more I saw this
light before
but we also have the the GitHub page for
our extension where you can submit
all your issues or what might have you
small tweaks
um
but that was it for me so if you have
any more questions
time for that
[Applause]
he's there
okay got one question yeah
nope
hello
I think this is working
okay
no
the green one is working the green one
is working
let's try the green one then again
can you hear it yeah
the features you were showing for
debugging before the new features are
they available both for our cloud and
for on-prem or only for cloud
they are available in in both scenarios
no difference yeah
any more questions we also had one we
have one over there
when using the code lens and we go
through the Explorer to one of the bass
apps can we see
all the references of example the
quantity on sales lines in our dependent
Maps
through the Explorer or well when you
dive down through the Explorer to the AL
file that it shows then you go to a
field let's say Quantity on sales line
and right click and say find all
references like you did with the
implementations are there any uh
way of doing that is it on the roadmap
so you can you can get all your
implementations for interfaces but if
you want to have references you have to
use the code and find references in the
code there is no edit capability in the
Explorer for finding references you have
no in general let's say you have a
dependency on base app if you
and you go down to it and you take the
quantity and you just want to see where
is that quantity used in
both the base up that you're dependent
on and your own app Etc can you do that
I know I can do it with my own field in
my table extension but my dependent Maps
yeah so you hit on a limitation I
believe so
you cannot do that for like what we call
like reference files so files that you
don't have in your own project right now
and you can only navigate to them at the
point
it's a wonderful idea and yeah go on PC
ideas and load it up because it is a no
limitation right now that you cannot ask
for references of of your references
okay
that's
and do we have any more questions
we have one over here
not directly related but uh
possible and near future that we get a
fix for the slash that we can debug
again objects with selection their name
absolutely of course that's very
frustrating most post routines and GL
account
yeah so that is something that we are
going on and you should see EFX I can't
promise you like tomorrow but uh yes
there should be effects coming out
oh we have one over here
thank you
um I was wondering you showed that it is
possible to have multiple sources of
your app files is it also possible to
have a destination for your compiled app
so normally I have to search in the
folder for my compiled app to be able to
share it or to upload it somewhere and I
want to have a release photo to and so
you want to specify in which studio yeah
I want to specify where to store the app
file or where to the destiny beat
destination
if you want to oh yeah I believe right
now it's only possible through the
command line interface yeah
um where you can specify it again
wonderful idea I mean
shouldn't be something good right now
so yeah I think that's it if there's no
more questions
it's hard to see
nope well if you can if you have any
more questions
come along at the Microsoft booth on the
allocated times right here and that's it
for us thank you so much
[Applause]
