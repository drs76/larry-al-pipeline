# Microsoft Presents: Obsolete Move, Future of delocalization and componentization

- **Source:** https://www.youtube.com/watch?v=Du1Rtjh6wYc
- **Video ID:** Du1Rtjh6wYc
- **Channel:** mibuso.com
- **Published:** 2024-06-17
- **Duration:** 45m53s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

so are you all excited ready to go new
topic we're going to talk about
something else than patterns we're going
to talk about code right so this session
is about move and how that impacts
localization and
componentization so I'm going to stumble
up that word like 10 times in the next
five minutes so help me be patient H
with me today I have Thomas and G and we
are from the engineering team and we're
going to talk a little more about this
fine thing but before we go into the
details let's talk about uh where we
actually got the idea from for
this so you all know the application we
this worldwide based application we just
saw it had a W1 name on it but that's
not quite true right so we have this
single package that's called the base
application it used to be bigger than it
is today uh but it also used to have
some uh some localization in there
even in the base application yes of
course there are some packages that on
top that has some localizations in there
but most more often than not we actually
had a situation where we needed to put
some localiza localization into the base
app and when we couldn't make that work
across all the different countries out
there we had to do the simple version
and copy the whole base application into
a new application and call this one the
Dutch one or the English one or whatever
and and you can imagine the frustration
of a developer who has to change a sing
change a single line of code in the base
application and Port that to many many
different lines in many different
applications just to find that there's a
conflict in the last application he gets
to right all the frustration so
obviously we want to change that
so what we want to do is take that
single application and turn it into
something else and the first thing we we
did and what we want to continue with is
take something out and we all saw in the
keynote today that we have a a system
layer and also a business Foundation
layer which gives us like some of the
functionality that's common to all the
different versions We have out there and
we want to do even more want to take
this monolith and break it down into
smaller components smaller packages
smaller apps that we can release and
maintain individually so we don't have
to worry about taking that whole big
thing and shipping it every time
we also want to be a little more agile
and being able to kind of change things
out
underneath the big challenge with this
is breaking
changes how can we make any change we do
a little less
breaking we would like to make it
non-breaking obviously but uh that's a
bit difficult right so how can we make
it a little less breaking at least
that's our idea that's how we want to do
it that's what we think of when we're
looking at the cloud we want to do
things more efficient more agile and we
want to be really good at this so what
are our
options well today we already have
something in the product we have
Absolution Absolution allows us to
Define that we are going to change
something here we are going to do
something new we're going to introduce a
new module a new functionality and you
should think about uptaking it we can
talk about when we will do it and you
guys can see that we are going to
implement this is it has some benefits
and some drawbacks one of the key
drawbacks here is that we need to
maintain some kind of side by side
implementation so while everybody who's
depending on the functionality that's
moving to a new module is kind of
looking at it and prepare preparing for
it we need to kind of have those two
systems running side by side causing a
lot of challenges and we really not
building a new functionality we just
want to move the existing one over here
right so it should be the same thing
there should be no news there okay what
else do we
have we have a an application
abstraction so in the app Json you will
find there we go uh you will find this
application uh property and it has a
version number and that's kind of the
abstraction that talks about all the
applications that are below that that's
the base application the system
application the foundation and a lot of
other apps behind that that single
number and you can do the same thing so
you can have your app that's kind of
abstracting away all the dependencies
that you have right this gives us some
benefits that means we can move things
around underneath this abstraction
without anybody know noticing and the
way we do this is by setting the
propagate uh dependencies property which
means that if you are depending on the
application then automatically all the
dependencies are included in your
dependency chain
great work right now we can actually do
it right so we have some good options
here we can do Absolution and we can do
the application abstraction all great
work but still there's something missing
what about the data what about the data
right the data is always the challenge
here right how can we make that less
breaking when we move the data we have
actually uh some functionality we have
data migration it's much easier these
days to move data from one table to
another table using the data migration
good options
again we really just want to move it we
don't want to copy it right so maybe
yeah maybe that's not it we also have
the feature keys so if we had that
sidebyside implementation we could
choose at some given point or the
customer could choose at some given
point to switch over and we could copy
the data there if we want to but again H
it's maybe not quite what we want
so we can't get it all we all know that
it's not possible can't get it all so we
choose the hardest problem the hardest
problem here is the data right we want
to move the data without having to write
upgrade code without having to copy data
so we want to move the data the symbols
we have a good solution for so we
introduced the new Absolution State
actually the two pending move and
moved and there are two new properties
they moved from and they moved to
so that gives you an indication that
something is about to move where it's
moving from where it's moving to or
something has moved where it's moved
from and where it's moved to right
should make this move a little
easier the properties are available on
tables and
Fields And it removes completely the
need to copy data because underneath
when you're synchronizing the extensions
we will be renaming the tables
underneath so that there's no copying of
data it's simply just repurposing the
tables
underneath so now we have a solution
that works for both symbols and
data but I don't take my word for it
yeah do you want to show how it works
yeah thank you
so um I'm going to demo uh the move
table um and some of the different um
places you can move the data but instead
of showing you a uh let's move table a
from extension one to extend you table
one in extension two I uh wanted to make
something that's a little bit more
relatable so as you do these days I
asked co-pilot to um come up with some
ideas for a demo app that I could easily
build that would then allow me to
demonstrate this capability and co-pilot
I don't know if it had any alterior
motives but it suggested I should create
an app that tracks the human worker
efficiency uh by tracking coffee
consumption and then um also employee
energy levels and then see how that
correlates to how efficiently they've in
you know perform tasks it's a little
concerning maybe but uh I went ahead and
just built that app so here's a
representation of the uh the app I built
it's it's supposed to be a little bit of
a a big app it's not that big but so um
it can track uh coffee consumption of
employees it can track their energy
levels throughout the day um task
completion as they they go through that
and then it'll calculate the how
efficient they are for each task with
you know at whatever point they are so
um of course this still doesn't show how
to move so we use it to break up the Bas
app right we want to componentize this
big thing so in my demo I'll be I'll be
doing the same so I'll first show you
the the one big app then I made an
intermediate preparation step where I
used pending move and then in the
version two of my app I actually split
it up into these five apps and the the
human worker efficiency tracker is um
where all the data used to be and then
it's going to move down into the various
individual apps
so let me show
you so um I just have this is business
Central um unmodified so far and here I
have my version one of the app I have
all these objects you can see I have
some table some pages a ro Center
extension number of things and there's
going to be a lot of publishing involved
in this demo so bear bear with me
because
it should publish just
fine see if it does that okay so um I
edited the RO Center so I can I can
easily show you these things right so U
expected energy boost coffee consumption
energy levels task entries but I have no
data because you know so I I also built
a um demo data app which is rather
simple it just populates some random
data in the in these in these tables so
I go ahead and publish
that and that goes well oh
sorry so now we should have data in all
these tables so the what data is there
doesn't really matter but you can see
here like this employee from this task
from this time to this time and they
were you know this is how efficient they
were compared to what was
expected um so that's version one
of my app and I think it's a little bit
too big it has four features you know
let's try and split that up
so I um of course I've prepared all of
this so you don't have to watch me
actually do
it so uh version
1.1 this is
uh it's kind of an an optional step you
don't have to do this but I think it's
nice if you want to follow non-breaking
principles and
and um warn people about what you're
going to do so I I created a little uh
Base Library which just has an enum and
Ro Center extension my my coffee Tracker
app now has uh you know the table I
split it into folders so I can organize
my code and here for the first time I've
indicated I'm going to be moving this
table and this is the app ID of the app
I'm going to move it to which at this
point doesn't exist but I prepopulated
it
and the same for uh for some of these
other uh
features and of course I also created
some table extensions so this field used
to be in the my task table and now I've
put it in a table extension still within
all within the the same
app um when you indicate pending move
this this generates a a cop warning for
you right so um by the way I have all
rules almost all rules enabled here so
the reason I'm not getting a warning is
because I've pragma all the ones this I
I do it this way I enable all the
warnings and then I go through them and
when I think I've handled it I add a
pragma so it goes away and I don't see
it anymore so you'll you'll see this uh
throughout the demo so I can obviously
go ahead and publish this
and there's been no change in in in
logic really this is exactly the same
app just structured a little bit
differently in the in the source code so
as you'd expect there is also no change
in the UI and there's no change in the
data everything's
fine but now on
to making actual separate apps so if I
go over to my version two uh
workspace now these are all individual
apps and you'll see some of these uh app
IDs come
back
so never mind some of these warnings um
if you if when we look at the table now
the all the obsolete properties are gone
because this is the new app which sits
below my human worker so this this now
indicates where the table has moved from
and it is moved from this human worker
efficiency Tracker app down here where
in my source code I only have the table
and the page extensions but I also I
like to split my code into you know so I
can very clearly see where things are so
my legacy table is now this one and this
has been
moved the reason you need to keep this
metadata is the the system needs to
know um what what moved from where to
where and you know what what was the
schema so that you don't accidentally
move a table and change its schema at
the same time because that would be
rather breaking so you don't need any
code in here but you do need to keep all
the SQL schema elements so the the I
guess appsource cop can can verify that
you're not breaking stuff um so there is
I'm by the way demoing what you would do
as a in a developer scenario
so I I could try and publish this space
now but I I already have an app
installed on my system that has this
enum so it's just going to complain so
since we're in a Dev scenario I can very
easily go and just uninstall it and that
will make things a little bit easier for
my demo so if I go in here and uninstall
this thing there shouldn't I don't want
to remove the data that's kind of the
point of the demo so
uh there it is it's gone so now
unfortunately you have to sit here and
watch me publish five extensions but
should be rather quick
um
so think if I put them side by side we
can get through it a little bit
quicker so the the this first um Base
Library has no tables so it's really not
not that interesting but I I wanted to
structure my code nicely so
Sor so this is now the first um table
that has been moved to a different app
and you can see not all of my actions
are appearing because I haven't
installed those apps yet um when you do
this from vs code it works a little bit
differently than if you were to try this
in production and I think Thomas will
explain why later but um my data has
already moved and that's purely because
I'm doing this from vs code otherwise
you wouldn't be able to to run the table
um so yeah unfortunately I have to run
through all of these so bear with
me and I hope I don't miss
one also I I don't want to wait for the
browser to load I don't need
that so there we go uh and now I've
published all of the apps let me get rid
of some of these I don't need
them
and now I'm running on my split app I
have still have all my data it didn't go
anywhere and in extension
management I can see I have lots of
version twos now which is nice but I
still have this uh demo data app on
version one and
and I can go and install that and even
though it's now pointing
to the split apps it still installs it
still works it can still find all of the
tables even though they're in different
apps now and that's because I used
propagate dependencies
in my human worker app Json so here I
have defined prop
dependencies and I have set the
dependencies to all of the individual
apps so that was my first demo I
think
so seems pretty easy to split the app
there are no issues but when you uh
technically it's fairly easy but
logically you can run into very simple
issues where you you still have to make
a choice right so here's an example
where uh your your big app may add a
group of actions and you know you add
you add several actions and then when
you split the app each of the actions
goes to an individual app well who owns
the group who's going to add the group
you you don't know there's probably not
a good place to to put that so you might
have to restructure some of your UI um
when you're splitting your app and you
do that for um these are the trickier
decisions you have to make technically
it's just all about dependencies and you
can solve those um so this the demo I
just did we moved tables down from one
app down into sub apps but you might
want to move tables another
way so moving sideways between two
unrelated apps I'm I'm going to use the
same apps as a demo so um here I want to
move a table from my new coffee Tracker
app to my energy level Tracker
app there's no dependency between these
so these are these could be two
completely unrelated um
apps and it works exactly the same way
so if I go back
here
yeah um I created the version 2.1 it's
like I like preparing uh my code for
this so this um expected energy boost
table tells you if you drink this much
coffee this is what I expect your your
energy boost to be really belongs in the
other app so again I I set pending move
and where it's going to move
to and again like the move from property
don't need that anymore so I commented
that out and that there's not much
obviously I have to move the the page
with it as well and again this is just a
a preparation step so I published that
if anybody depends on my app they will
now know hey this table that I'm using
it's going to go away at some point in
the future so you know prepare um again
same app nothing much to to show here in
my version three where I've actually
done the move you can see I I'm didn't
add the other apps to this workspace
because it's not relevant for the demo
in the um cof Tracker app now the
table's gone but I have it as a as a
legacy so it's exactly the same as in
the first
scenario and in the energy level Tracker
app I have now moved my table
here and my energy boost is here so I
should now be able to publish these apps
and hopefully it'll work and this time I
don't have to uninstall anything which
is also nice I hope it works so that
published let
me go back and publish the other
[Music]
one so you might wonder how it is that
nothing is breaking while I'm publishing
these and that is because I have nobody
depending on my coffee Tracker app that
doesn't also depend on the energy level
boost app the energy level tracker if I
had an app that only depended on my
coffee tracker it would absolutely be
broken now because the table is gone and
it it would complain that it can't find
the page it can't find the so as you can
see here here my data is still there but
it is now in another app and if I go
back to extension
management I can it's not very
interesting but you can see version
three version three my uh my other apps
didn't change they're still installed my
demo data app is still there so that all
still works um so that was a sideways
move and the third way you can move a
table is you can move it up so the next
demo which unfortunately is going to
look exactly like the previous one is
going to move a table from the task
Tracker app to the human worker
efficiency Tracker app and again if you
had somebody depending on that task
tracker that didn't depend on the other
app you would break
them but I made my demo so it wouldn't
break
so um so let me very quickly show you
that uh
so again I did the same thing um so I
have my preparation here version
three where I I think is this one that I
move want to move yeah so this is a
table that stores expected efficiency
you know some people work faster than
others so you can put in how fast you
think people will work and then the AI
can compare their actual performance
versus
this um so this table is going to is
going to move up um same thing with the
page
so I publish
this again this this is just to give
people a warning you can also see that
using pending move I can indicate that
the table is moving and where it's
moving to but in the receiving app there
is no change yet I can't indicate that
it's going to get a new table um so for
that unfortunately you have to wait
until it's actually
published uh I think this is my last
version so again I use the exact same
pattern as before I put the table in a
legacy folder it's now moved
to um by the way I forgot to mention
might go go back a bit um and then in my
human worker efficiency Tracker app I
now got the new table over here so when
I publish this this will move
um the thing I forgot to mention earlier
is when we split the
table with these table
extensions these these these fields got
moved back up so I'll I'll um I'll show
it on the on the slide in a bit
um sorry for messing up that bit showing
you let me just quickly publish these so
you can see that moving up also works
and doesn't break if you handle your
dependencies um again I know the demo
isn't very visually appealing because
it's the same thing over and over again
but
I wanted to show that it actually works
let's
see so now I'm on the very last version
I finally got all my tables where I want
them I still have all my data in the
right
places and you know the tables didn't
change they didn't move so that's that's
nice um if I just very very quickly go
back
version two which is the bit that I
missed
before I think I had some here right so
in the task table I I had a field called
expected duration that um is a field
that moved back to the app so the the
table itself moved down to the task app
but this field
moved up or stayed in the the human
worker
uh tracker and and the syntax is is
identical right so this this all works
very nicely and um there's yeah you can
you can now split a table between two
apps create a table extension and table
it's very nice feature helps us a
lot um very final bit that I wanted to
show you after all my demo it's kind of
a recap of the where we ended so we
started with one really big app with
four different features and then we
split the app into five different apps
where each app now handles only one
thing and version wise the demo data app
is still on version one because that
didn't change at all the bass is still
on version two the coffee tracker and
energy level tracker that was the the
first sideways move there on version
three and the task tracker and the human
worker TC tracker there are version four
that was the the move
up so if I now go back to the slides
this is a recap of all the demos I just
showed where went from one big app to
all the separate apps and that's how you
would um use it as a developer it seems
to all work just fine but Thomas is now
going to explain all the internals and
why it isn't as simple as it looks yes
thank you g all right let's step forward
here so we also got showing his
presentation about how we are going to
move all these tables and Fields we
moving them down we moving them sideways
and we are moving them up um around here
and the name of the game here is to
handle all of your dependencies because
doing a move is a breaking change you
are going to annotate your tables on
your feels with having been moved and at
that situation you will not be able to
access them you need to then have a
reference to the new table or the new
set of
fields so when we had a look at his um
um an overview of his extensions right
here we could see that his top level was
was the the app that he started out with
and he annotated that one with being a
propagated dependency so all of the
dependency it has is now showing out to
his demo data and all the other apps
that might depend on his apps so from
his perspective it all looks good and
from all the other ones that are
depending on just this one app it all
looks good as well because now you only
did the the down move but if you were to
have all these are published out into uh
the world and somebody would take a
dependency on task tracker for instance
and he would move the the tables up then
that would be a breaking change and we
need to to handle the situation so from
a Microsoft point of view we try to
handle this with the
application
um package where we have propagated
dependencies over the base application
system application business Foundation
all these ones so we can move tables and
fields around within our uh scope of
extensions and then we will not be as
breaking um for everybody else so that's
a recommendation for for you as well to
think
about but what does this mean actually
for the upgrade process so when you are
going to use these ones um what are we
going to do here well first of all we
still need to respect the order of the
dependencies when you do the
publishing the compiler still needs to
find all of its references um so we need
to follow this but second we also need
to make sure that we publish all of the
apps before we synchronize them so they
know about all of the fields that we
have about to
synchronize because and and well sorry
another situation that we might come
into is if we do a half done move then
we can also get into situations where a
table has been renamed and then the
system cannot find it under the original
name so we need to make sure that all
the apps has been published been synced
and been installed and now we're in a
good shape again so we can actually have
a a fully working system so if we take a
look at how that would look in the real
world scenario we would will publish all
of them in the dependency uh tree order
and then we will start syncing and of
course last we will do the install for
for all the apps
here all right so how can we use this
for componentization here well we will
use this one uh and continue to use
these move operations in Microsoft for
actually splitting up our own apps into
more and more and dividing them into
smaller components so we can iterate on
them
individually um so you will see more and
more of these obsolete moving properties
around the uh our
apps um because our main goal is to have
a standardized version of the base
application so we don't have a localized
version for each country um but those
are instead a separate app that are
built on top of our standardized set of
standardized base application but again
this is an organic growth it's not going
to come to tomorrow it's going to take
some time but we are getting there we're
working towards it it's this is the the
goal of
everything so right now using the
obsolete move properties here um and the
move to and move from properties these
are limited for now for first party apps
for for Microsoft apps because we need
to make sure that all of these ones are
really working well so we need to make
sure that we can walk before we run with
this set of features right here
um this is your data and this is really
critical to get it right in time we will
open up for more and more Partners so we
can slowly weave out the the worst set
of issues right
here
and
um so everybody should make sure that
they first of all take a dependency on
the application um dependency as we've
defined in the app Json um and not on
the base application or business uh or
business Foundation app because of these
situations where we're moving fields and
tables
around um and this will be uh a
multi-release um set of uh moves and we
will create more clarity about how what
can you expect from us in these
situations um where we are going to move
these tables and fields around and and
restructure our our own code um and we
also create clarity about when can you
actually start removing some of these
tables and Fields again because as you
the Keen ey one you might have seen ger
was having both the Old and the new set
of tables in it each app but living side
by side um so at some point we need to
to clean up as well so what can you do
today
well keep up with all the changes that
we are doing um we try to to be less
breaking as possible um we try our best
um but but yeah take the dependency on
the application one um if you find that
you're missing some symbols have a look
into the mve
properties um they will give you the app
ID and from there you can you can figure
out what is actually the app that you
are missing a dependency on and and what
are some of the changes here
um and you can also start componenti
your own App G did that with his 1.1
version of the uh the human coffee
efficiency tracker um where he started
moving or he started splitting up his
table into table extensions as well as
his table so he started splitting it
into individual feature
groups
um you can start using Nam spaces in
relation to this so you're still having
the same separation you have a a good
idea of what feature lives in what area
um and and that way you you kind of have
your your functionality split into
different components and you're ready
when this feature is available to um to
you so all in all mind your uh
dependencies because this is a breaking
change um and uh yeah let's see where
this one
goes so this is all for us right
now and we are opening up for questions
from the audience
[Applause]
oh so many questions have couple that
the one who doesn't want to te go
ahead no I don't want a
t-shirt um um two questions you can give
it to another um actually you named the
name spaces at the last part you didn't
use it in your demo right so do you in
your preps already need to prep those
name spaces for what you do what you're
going to do actually you don't have to
no and think of name spaces as just
being the prefix to your object name
it's part of the object name so you
can't once you set it you can't change
it so I could have gone in my version
1.1 and added all name spaces in the
when I split it you know between the
coffee tracker and the energy level
tracker uh and if I'd made a mistake
like in my second and third demo there
basically mistakes right the table I
left the table in the wrong app I I
would be stuck with the the wrong name
space I've been asking for ways to
rename namespaces maybe in a future
version we'll get that but for now uh
namespace is optional once you use it
you're stuck with them um so you if you
they're useful for you go use them but
it's it's entirely optional and it's not
related to the the move no uh at all so
okay yeah and I had another question um
um you yeah in the upgrade uh Thomas you
said uh with with a half syn you you
might be in problems um so uh if you
would exercise this on a production
environment how do you prevent that not
to get into problems in the sense of I
need to be disciplined I understand but
is there a way of something reminding me
hey wait there is something more there
or is it like well Luke you're lost uh
at your responsibility or is there
something to be in the future there that
would help me to say I have this
combinations more or less inform the
system that I'm going to upload them and
should upload them first or publish them
them first before I do the sync yeah so
right now we don't have any system to
help you guide with this entire flow
right here but yes it would be nice to
actually signal to the uh yeah to the
this is a part of the walk a t-shirt for
him I'll give it to somebody over here
first yeah see a hand there
sorry if I do a better job with your
T-shirt
nope I was thinking about how this would
break uh external apps that is dependent
on the app that you're trying to
simplify um do you need to add all the
extra dependencies for example you have
some apis that you have made in a
different app that is dependent on the
human coffee uh big app and then it gets
break down into multiple different apps
can you still have that original
dependency and everything will work or
do you need to make extra dependencies
on the different
apps good question so I think G showed
it very nicely with the fact that he had
a single app to begin with as long as
you're depending on that and the the
only dependencies that app has is the
ones that's broken into and you use the
propagate dependencies then it works
fine but if you have you move something
completely out of that dependency tree
somewhere else then your consumer will
have to uptake a new dependency right
okay so so you can still it is a form of
grouping still when you have the
propagated dependency yeah and it's only
one level that's also important to know
so G has a good example in his maybe we
can go back to that slide uh so he's
taking an a dependency directly from the
original app to the base implementation
here imagine he didn't do
that then anyone using objects in the
Base Library here would have to uptake a
new dependency because it doesn't
propagate more than one level right so
that it's also important when you design
the the the dec componentization right
take that into account okay it's it's
okay to have a breaking change because
you can announce it and you can say to
people hey we're going to move it out to
a different app somewhere else and
please add a new dependency to your
consumers that's okay but if you don't
want to do that then you need to be
mindful about these dependencies yeah so
if I make a group app that has
dependencies to a lot of different apps
that has propagated dependencies then I
only need to have one dependency in my
API app on that group app exactly
amazing t-shirt
well thank
you hey so if I want to use the moved
from move to uh features but what if I
just don't install the move to app and
will the data the previous data be in
some kind of limbo like unavailable or
um you still need the other app to take
it over it's only at that point in time
we actually do the the rename and you we
move the data this is the Half Bake
scenario we have where you didn't
complete the last step yeah can't access
the data because the symbol is gone from
that app but the data is still in
database so so you should take it over
as soon as possible you should get that
last app installed yeah maybe we add
tooling I don't know yeah I think to to
clarify that's a difference between the
vs code publish which I showed because
vs code does publish sync install all in
one step so it works in vs code but
that's because it's a special code path
for the developer scenario because
otherwise you'd be stuck you know
running a bunch of Powershell commands
all the the time when you do this in a
cloud a Sandbox or production
environment or anything a little bit
more serious you have to follow the
pattern that Thomas said which is first
you publish everything so the system
knows the entire picture then you sync
all of them you have to do it in the
right order and then you can install all
of them and if you mess up and you leave
your system you know in a Half Baked
State you will have issues and and yes
it would be very nice if that you could
then somehow see like where in the
process did you get stuck like hey
you're missing syncing this app for
example that would be very
nice and maybe one one little more
question um is there already some kind
of schedule when we get rid of the
Legacy parts that we like you you showed
it in your app where you you need to
keep the original schema information in
there right yeah yeah so I don't think
we have any concrete information about
when we're going to do this um what we I
think have announced is that
uh in version 26 we're going to be
cleaning up all the currently
obsolete uh obsolete removed
tables and that so we're we're looking
at we don't want if something was
obsoleted at the end of version 25 we're
not going to remove it in 26 right so
we're we're probably going to take
everything that was obsolete removed
version 23 and below and we'll clean up
the SQL schema that's in the plan for
version 26 I I would imagine that when
we get around to cleaning up these these
Legacy tables we will snap to the same
schedule we use for that yeah so since
this is a newer feature I don't think
any of it is going to get removed before
version
31 is a while away so you know no rush
okay you guys have time to figure it
out yeah about the uh name spaces and
the affixes that we are using now for
objects um I know you didn't mention
this but we have a session tomorrow come
you have a session tomorrow about that
it's called name spaces come and
ask all right I'll wait yeah but it
includes moving data between table that
now without the affixes is that so the
handled as well unrelated to namespaces
the reason why we mentioned it is
because when you do the whole
refactoring and preparing your your
application to be moved it can be nice
to segment that into name spaces like
when you extract the table extension put
it in some name space where it belongs
so you're kind of ready for the move
where it's not a rename because if you
rename the or original table then it
it's a breaking change right so it's
just a choice it's not really related to
the move it's more of a suggestion here
the name
spaces I think last question then
they're going to kick us out okay lucky
me okay I'm just curious about the fact
you said that that would would not be a
breaking change if you kept re uh kept
depending on the top level uh
application but what if you have made an
index that now contains Fields split
into different uh apps wouldn't that be
a problem or have you finally allowed us
to make indexes across no changes there
no changes there so that would be a
breaking change yeah if you if you moved
parts of the table that participates in
the in the index yes could you could
risk of customers having issues if you
this kind of split up if you put them
into indexes yes then that would be if
the customers have put them into indexes
yeah no absolutely so that that will
happen that is the breaking part of it
we cannot solve all the breaking issues
okay that is
true all right I think that's it for us
we're out of time sorry let's go away
over
here so thank you very much yeah thank
you
