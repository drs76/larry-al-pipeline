# BC TechDays 2022 - Permissions revisited

- **Source:** https://www.youtube.com/watch?v=c8qOFzVW7PQ
- **Video ID:** c8qOFzVW7PQ
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 45m42s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

um onto the agenda so we'll give an
introduction about the permission system
uh and then we'll get into composing
permission sets and talking about the
new exclusion uh of permission sets and
permissions
uh how it works and give you examples of
how to use it uh we'll go over the new
UI for creating permission sets talk
about the inherent permissions and
inherent entitlements properties
um and then talk about what's coming
next so I'll hand it off to Jens to talk
about the introduction
yeah
all right so
nope no clicker not that one I will stay
here instead
so you probably all know and love the
there it is the business Central
permission system
you have worked with this for quite a
while but there might be a few things
that you didn't know about the
permission system
first of all it is used not just to
Grant user permissions at the bottom of
it you have the license for on-premise
the entitlements for the SAS solution
this is actually to protect the IP owner
that this user should only be allowed to
do this if you have actually paid your
license
Etc now the entitlement is mainly for us
because your apps is usually in the free
range
now in order to perform an operation you
also need to fulfill the constraints of
the system an example there is the
read-only access that you can set up
where you're now talking to read-only
replica that is actually implemented
inside through the permission system so
it'll block anything that is not a
read-only operation for tables then
there are the permissions that you know
of the that the administrator can set up
and that will be the main topic today
and then on top of this you can actually
also add test permission sets if you
want to simulate how this runs when you
also have permissions applied because
you can there add an extra permission
set on top of it and since the user
needs to have access through all of
these layers then you can add this in
the test permissions and simulate any
problems
that you'll see there but we are going
to focus on
the administrator the one that sets up
the permissions and how that can affect
you
we've invented we've invested quite a
bit in permissions over the last few
releases we have moved them to metadata
and now we have also improved how the
end user can set up permission sets so
what we're looking to achieve is
to spend less time setting up
permissions we can see from Telemetry
that the permissions pages are open
they're open for quite a while then
they're closed and they're opened again
and I don't think it's because people
really love to open the permission Pages
um well maybe they do you tell me
but it actually seems to be a relatively
time consuming task to set this up
correctly
the second part is actually
understanding what you've set up because
it's not that easy
um I'm in the server runtime team and we
very often get the question oh the
permission system doesn't work
and then we'll look at it and in the end
well it is very very seldom that it's
the permission system that doesn't work
it was just that it had a different
effect than the user actually expected
and then what we also want to achieve
with this investment in permissions is
to reduce the maintenance burden so that
when you upgrade stuff then you don't
have to redo things again
so how are we going about that
well first off we want to move to
well-defined understandable building
blocks
so that our our end users the
administrators they should work with
permission sets rather than individual
permissions we shouldn't require them to
know about the table structure they
should know about what the user needs to
be able to perform
so we need permission sets to explain
what it does and then the administrator
grants access to
the duties that users need to perform
not the underlying tables Etc that's one
of the goals
reducing the maintenance burden well
when we're upgrading to new versions you
want to automatically get the new
required permissions and I'll get back
to why this is a place where we actually
very often struggle and we want to make
it easy to distribute permission sets
together with your app with your
extensions
and we've also invested in automatically
assigning roles to users Etc
third goal is to make this simpler if
you look at our permission sets
they're huge
they're really big and you think why I
just need I just need to log in why do I
need access to an um casillion table
um
I'll get back to why that is and some of
the tools that we have created so that
we can actually make it simpler and we
can remove some of the odd permissions
that are needed just because the system
might initialize because it's the first
time you log in Etc
now we still want to retain the
flexibility we actually want that to
make it even greater by allowing you to
specify the granularity and the
abstraction level that you want to work
at or where you want your customers to
work
all right
let's dig into this so
composing permission sets what does
composing permission set mean well that
actually means building new permission
sets by gathering other permission sets
so you compose them together
you know that in permission sets for the
traditional permissions as they could
contain permissions you have indirect
permissions and direct permissions and
for tables and execute permissions Etc
all nice and good but the compose
permission set can also include other
permission sets
so set a includes set B and set C and
hence it includes all the permissions
that are in B and C so in this case the
compose permission set will contain
everything that is in either the a
permission set or in another permission
set
this is actually just saying the same
but it actually also highlights that
there is no limit
to the level the hierarchy level you can
Nest these as deep as you like now I'm
not saying you're doing your users a
favor if you make a 38 level deep
hierarchy of permission sets I'm not
sure they're going to thank you for that
but you're no longer limited to having
user groups permission sets no you can
have permission set that includes
another one which includes another one
and then you can Define the granularity
that you need by composing in this way
now you might think that this is old
news
because
you could do this already in 2021 way
one in metadata that was actually the
release where we moved the permission
sets
into metadata so that you could not just
distribute them together with your app
you could see here that it has included
permission sets but it was cheating a
little
because actually when it was
add it to the system it would just be
flattened so at that point in time there
wasn't really any permission sets inside
other permission sets
now with version 20 which is what you
have right now
then actually already version 20 support
this having permission sets inside
permission sets because the information
gets added to a small Trio of system
tables you have tenant permission set
which has permissions in it but then it
also has
permission set relations where it can
include other permission sets now this
is being kept at runtime so the one you
saw before you will now at runtime also
be able to see that this permission set
includes this other one so at runtime
there's also a hierarchy that is
retained so let's see how we Define a
composed permission set in the UI and
this is where Derek is
more of the expert yeah okay so it's a
little hard to see but it's
the basics is basically the top left I
mean you can see the information that
name as you could before but then also
gives you the type
um now in the middle section it's a list
where you can include and exclude your
permissions
um and this is yeah so those are for
permissions I mean table data your page
so on and so forth
in the bottom left now this section is
the one that's really new where you can
include permission sets this is also
where you will be excluding and we'll
talk about that later and on the split
view so on the right side is where you
would see the result of your permission
sets and the hierarchical structure that
actually is there so for example in here
where I have d365 read included
it does show me that I have d365
included and my inclusion status is full
meaning that I have everything included
we'll get into that a little later
and on the right side we have a fact box
and this one specifically shows you the
permissions that are added uh into the
selected permission sets
and now how do you see like the result
of this whole composition after you've
created your permission set with all the
inclusions and inclusions we have a new
table called expanded permissions and if
I just go back once like real quick in
the top left we have an action view all
permissions and this opens the expanded
permissions page and will show you the a
flattened list of all the permissions
that is the result from your permission
set
yes and we're gonna see this live in the
product in in a moment so what are the
benefits for you here well the benefit
is that you can create hierarchies you
can create something that works for your
line of business you can compose these
permission sets you can ship them as
separate extensions or apps if you would
so like
um so you decide and just as a sample
you could decide to have a structure
where you have roles duties and tasks so
you have the bigger role on top which
includes all the duties that you expect
this role to fulfill and in order to do
this duty this user needs to have access
to these tasks and then underneath the
task you will actually have the actual
permissions this is something that
we at least believe users will have an
easier time to relate to because this is
something they're giving access to what
the user needs to do
and now
this is all nice and good now we're
going to talk about exclusion
it's very weird that we actually like to
we normally like to talk about inclusion
and inclusive behaviors but just in this
case we'll talk a little about the
benefits of exclusion
and be aware we will go into
excruciating detail about what it means
sometimes
the permission sets aren't right for you
they are not fine-grained enough they
might include too many permissions you
don't agree with Microsoft or your
partner's definition of what a sales
order clerk should be able to do so you
want to remove something
in previous versions what you would have
done is copy a permission set
unfortunately this means that now it's
up to you when we upgrade then if
Microsoft added new permission to that
permission set because a sales order
clerk now needs that then you had to do
it and you wouldn't really figure it out
until the customer would call you and
say I can no longer do task a
so this is actually one of the most
frequent problems we could see happening
out there so we wanted to see if we
could solve this
and what we've come up with is the
ability to now this might sound odd to
add excluded permissions so you're
adding something that excludes something
so we actually added this in 2022 wave
one the ability to exclude permissions
how many of you have made use of it so
far
I'm actually happy to hear that
because I'll get back to in a moment
that we had to change the behavior a
little bit so I'm happy if it has
doesn't take have because there are some
odd cases where
it may not work as you would expect but
the tenant permission table has a new
field called type so when you add
permissions
well if you change the type to exclude
now suddenly you're subtracting
permissions instead
so for instance in this example here you
have the d365 basic the HR edit full
access and then in the employee
permission set you exclude the
permissions to modify and delete for the
table data HR confidential
command line
now this use if this is the permission
set that you assign to the employee that
employee can no longer modify and delete
from this table
now you can do the same with permission
sets just like the permissions had a
type then the relation between the
permissions also has a type you can see
that in small
inconspicuous little red arrow over
there that points to the type which can
either be include or exclude include as
a default but you can also exclude a
permission set
so how does this work
so warning
this is math
it is set theory
so what we do is that when you have a
permission set that includes others then
in this case you have the P top
permission set and that includes
permission sets P1 and P2 and then some
explicit permissions p e x
and then it excludes permissions set 01
and it excludes explicit permissions oex
the explicit ones
now in set theory notation we will do
the union of all the included permission
sets and their permissions
and then we're going to do the
complement and then on the other side
we'll do the union of all the things we
should exclude and then we'll take the
complement between these two which in
normal words is we subtract
think of this as subtract just in a set
theory manner
and then the visual representation here
is you had the blue ones representing
what you had included and then you
excluded the white ones and what you
have left is basically what's left of
the blue ones
an easier way maybe to think of this is
that what we do now we've optimized a
little behind the scene but we calculate
the expanded list we just calculate the
sum of everything that's included as a
list of permissions put that to one side
then we calculate the list of everything
that you have excluded
put that to aside now I have two lists
and now I take well for every element
over here I look up in the excluded list
should I exclude it if if I should
exclude it then I take it out and then
you end up with that list so of course
if you exclude something that is not in
the included list it has no effect
because you can't exclude something that
wasn't there already
so this is how it works
this is if you had managed to code
around because the system tables were
there in version 20. and if you had
coded this you could have added
exclusions to permission sets but we
actually realized that it didn't work
the way we wanted it to do because it
was effectively implemented as a skip so
if you excluded a permission set then we
would skip it during the calculation but
that is not the same as
removing them at the end because if you
restructured your permission set then
the permission set that you excluded May
no longer be in the tree anymore
and then suddenly you had this
dependency on how we'd internally
defined but we're gonna go painstakingly
through some examples
but now with this change then we have
just said that it works exactly as I
explained before
you can do this in two ways
you can do this in metadata
so you had to include permission sets
now you have a new thing new kid in town
excluded commission sets
and then you can also specify
permissions and you might look at where
is the excluded permissions
it's not there
and I don't think we will add it
because
you can just just create a small
permission set with what you want to
exclude and then exclude that as a
permission set which also that's
actually how we want we want to group
things together so you don't have as
granular things so unless there is a big
pushback then we're probably just going
to leave it with the excluded permission
sets
you can also do this in the UI and now I
think it's time to
talk about that and how you do that so
instead of showing it to you there I'll
show it to you in the product excellent
choice excellent choice
yep all right so I have a BC Tech days
permission set so you can see I have
d365 read and email admin uh included
so let me edit that
let me take out email edit
so change that from include to exclude
and now you can see on the right side
that is
my inclusion status have suddenly become
partial and if I look into email edit
email admin it actually includes email
edit and now the inclusion status is
actually excluded so none of those
permissions are going to be
you won't see them in the expanded
permissions
so if you act you can actually this is a
whole tree and it will go down all the
way and you can take a look so for
example here's like email address there
as well and it's excluded
sorry can you just leave that on there
yeah no if you look at this you might be
a little surprised
because yeah of course the email edit is
excluded
but what about this language edit which
is now stated as only partially there
what's gone wrong here that's actually
well is that what I wanted
yes so uh so in this case system
application edit it includes uh email
edit and it includes uh cues and kpis
data classifications so on so forth now
because system application added
loses the permissions from email edit it
shows that it's partial because it's
still including some other stuff but
it's now lost those permissions that it
was initially including yes so now we're
actually going to do a little trick or a
little quiz you can go another trick a
quiz
um there is no scoring Etc but I would
recommend that you try and follow me
along the way and just see if you
understand what this exclusion actually
means so we have an example
relatively simple example where you have
these permission sets DC b and a the
permission set a includes permissions
three and five
permission set B includes permissions
four and five
and as you can probably guess if you
look at it what's in D well that's
permissions three four and five
since it's just sets then it's not that
there are two instances of formation
fight no it's just permission five is
there so this is our basic sample what
we're going to do now is see what
happens when we start excluding from
this and then you can whenever I'll just
show examples then you can think so what
would you think and then of course
you'll get the answer right after so
start very simple
what would happen when we exclude
permission three what would you expect
there to be
commission 345 or permission four and
five
not the hardest exercise right but we
need to start a little easy
yep it'll contain permissions four and
five because the original list was three
four five
and then the exclusion list was three
take that out so we have four and five
left
easy peasy right what's so hard about
this
so now we have a new one that includes D
and excludes
permission five
what would you expect here
three four five
or only three four because you did
notice that permission five was there
twice
give it a little thought
think about how this could be and then
well
you have permission three and four left
because
you had the list of three four five now
we remove five so you have three and
four left
so far so good so as long as we're
talking about individual permissions
this is easy
now we come to the permission settings
now G no
we're not excluding the permission sets
yet now we have G that includes D and
excludes
C sorry yes so you have the G has the D
and then it's exclude C so what's left
at this point in time
is it empty
or because C is actually empty just has
other permission sets inside so what do
you have do you have the empty set at
the end or do you have permissions three
four and five
well
the answer is
it's empty because
since G
excluded C then it excluded the list of
permissions that are inside c meaning
that they've excludes 3.5 meaning
there's nothing left
now we have that the new permission set
h
includes d
and it excludes B
so if we had just skipped no
come on so what do you expect here
we expect it to be empty
we're expected to just have permission
three
oh would it you expect it to have
permission three and five
yes is three
and this is this is actually the
difference between skipping
and excluding because if we just skipped
B when we calculated it then you would
have had three and five left but since
we're doing it in the math notation we
talked about earlier then you'll end up
with permission three
I just have one or two more
so now we have a new permission set I
which includes D just like before and
now it excludes q and Q includes A and B
so what do you get now empty permission
345 or do you get an error
well you get the empty because first we
take all the ones that are included
three four five
then we need to take everything that's
excluded now we need to calculate the
full q q includes A and B which means
that's also three four five
so subtract those from each other and
now it's empty
and I think this is the last example no
second last
and now you have J that includes D like
before and then it excludes R which ex
and R includes A and B and excludes P5
so now you're excluding a permission set
that itself excludes something
what would you expect to be empty or
permission five
well
it'll be permission five because if you
calculate r
then R is three four five and then
exclude 5 meaning that R is three and
four when you exclude that from three
four five
you have five left
and then the small one here
what if you then have D D1 if D had been
a little bit different and eating
included both C and then B again would
it make any difference
no it would not it is just the same it
doesn't matter if you include something
multiple times it doesn't count more
it's not like a voting system that oh
I've been included four times
but I've I've only been excluded twice
so I'm there twice still no that's not
the way it works
it by the way another thing that doesn't
come clear here is it is not a deny
permission
it does not mean you can't get this
permission from another permission set
it just means that in this permission
set where I've had these and then I
exclude this it's no longer inside this
but it doesn't deny you from getting it
somewhere else because the problem with
the deny is it's very counter-intuitive
that by assigning an extra permission
set to a user he could certainly do less
because that one contained a deny
permission
so it is not at an eye the whole idea is
it does not matter how the permission
set is structured internally whether
in all of these examples
just take this one again
if we had to find D as just being
permission three four and five not
including anything else just permission
three four and five you would have
gotten exactly
the same results it does not matter how
it's internally structured foreign
let's take a look at creating some
sorry for going through all of these
details but there is this surprise that
will just I exclude a permission set and
then I actually exclude all of the
permissions that are in there and not
just not calculate it in but let's see
some examples yeah so I'll go over some
of the examples yes went through uh but
show you through the UI so firstly I
have permission set a as you can still
mentioned I mean it includes permission
three and five just quickly to show you
the expanded permissions this is how it
looks like so three and five
um and permission set B
I have included 4 and 5. as you can see
and then in C I have included permission
sets A and B
so in this one I'll get the result of
three four and five
so now
um with the very first example I'm just
going to include D and I'm sure all of
you can imagine already it's going to
oops nope if I mentioned C uh versus
that c
and the result will be 3 4 and 5. but
let's go on to excluding more stuff so
I'll go to memory set e
let me edit this
let me include permission set d
uh and then exclude
um version three
as CN hat inside shown us this will
actually give us permission it's uh four
and five so when we open up the expander
permissions it will calculate it and
give us that result
um and then if we go to permission set f
now let's include D again
and let's exclude C
so we know D includes C and if we
exclude C here what we will expect is
that it actually shows us the inclusion
status is excluded because all the
permissions have been removed and if we
expand it
there are no permissions in this
permission set
so simple enough uh and one more uh for
instance h
now I am going to include A and B here
there's that a and but I'm just at B
and then I am going to go back and go
into a primary side I
and here is where I am going to include
the
but exclude
h
uh let me change that to exclude so
similarly now I guess I'm like the one
from before I am excluding
um D which includes A and B and then I'm
including amp uh and then H is the one
that is uh excluding the permissions
so that is how it looks uh for the from
the UI playing around with the inclusion
and exclusions uh for this
uh this
oh yeah
yeah so excluding uh information some
considerations to take note of
so I mean you can really surgically
choose what permissions you want to
remove from your final permission set so
I mean excluding existing permission
sets will often exclude too much for
example if you take like d365 premium
and you want to take away I don't know
d36 if I read you're basically taking
read away from almost everything
um and then what you should do is kind
of create small permission sets with the
ones that you really want to exclude
like Ian said alluded to earlier I mean
you want to pick the permissions that
you really want to take out and then put
that into a permission set and then
exclude that one permission set
um the permission owner uh
yeah this is actually me yes so you
might want to look to us if we are
excluding permission sets inside
permission sets when we ship something
but since we're the original owner then
in general we're just going to include
stuff the exclude is mainly there for
tweaking what somebody else was shipping
in the end it doesn't matter because the
internal representation doesn't matter
but if you're the permission set owner
you would normally just include
permission set and this also works best
with small permission sets because
remember that it might take
15 permissions to allow somebody to edit
something
but it only takes one to take that
ability away
because he needs access to all of them
so you can just take one away so you can
surgically remove the ability to do
things let's see how this works with the
copy permission set
Etc and how this can solve the problem
that we talked about earlier with
copying permissions at and keeping it
updated
all right so let's go back to the
product
okay
so the copy point is that action still
the same it's up there but now the
slight difference now you have the copy
operation
so the one that all of you know is
basically a flat copy so if I did this
flat copy now
I would just call this basic flat
very quickly
um you guys can imagine it would just
give me a whole flat list of permissions
within the permission set
maybe I should have chosen basic
bad choice for demo right now
okay uh let me choose something else to
show the others uh okay but you guys
know what the flat and coffee is
and then there is a copy by reference
and this is the default that we would
like you to actually use
so uh reference copy
and what happens with this one is
actually it select that yeah so it
basically just includes that information
set that you had just chosen so I know a
lot of you your customers use custom
permission sets and sometimes you take
basically like a d365 basic for example
and build on top of that and take stuff
out but you don't get the stuff that we
add in the future however now if you do
this copy by reference you will include
our stuff whenever we also make changes
but you can also then add the stuff that
you want to exclude from d365 basic for
example
and there is one more uh let me just
select this one again copy permission
sets and which is basically clone
clone copy and
that's the name kind of suggests it does
an exact clone of the information set so
all the inclusions and uh that you get
wait did this one not have
ah okay I should just pick another one
real quick
uh like maybe dope
I am sorry I need to fight
conceivables yes this one okay
let's make a quick copy of this clone it
to
yes
and if we open this you can see I get
all the permissions that I had
originally included in that permission
set and all the information sets that
were included as well so this is another
way to do that
now if I go back to the slides
so yeah
um so yeah so as I had mentioned now
this is a quick recap so with reference
it basically includes the selected
permission set in your new permission
set the flat list is what all of you
already know is the old Behavior it just
flattens the whole permission set and
does the copy and actually what we're
trying to say is don't do that yes
um and then clone is basically just
sticking uh cloning it exactly uh
with all the permissions and permission
sets whereas included included from the
original
um and then what I want to just quickly
go over is that I mean these permissions
uh permission sets can also be exported
into example so this is the this is the
old way that I'm sure some of you if all
of you work with uh there's some
slightly new changes
um where
the permissions that relation is also
now included
and there's a slight tag version 2.0
it's just such that you can actually
still use your old xmls to be imported
and it's still one action you don't have
to specify hey include a new one or old
one this it's red from the version
um so this is for the system permission
set and then there's also the tenant
information set but one slight
difference with between the tenant and
the system permission set being exported
is that there is a related scope it's
just so that we know if it's being taken
from a system permission set or not
and of the ends for inherent permissions
yes so I mentioned earlier that we also
want to simplify the permission sets and
one of the tools which has been there
since version 20 but it was only there
for on-prem scope that is now available
also for cloud scope so we're going to
repeat it here
this is inherent permission which is an
ability to elevate user permissions in
this particular scope actually within
this particular method if you do that
then it is granted during the specific
method execution
and you no longer need to add this
permission to the permission set
this allows us to get more clean and
comprehensible permission set because
all of these are permissions can now be
removed
um
it should be noted you cannot change the
permission setup of other extensions you
can only do this for your own objects so
if you need to read your own setup table
then you can say well I want to make
sure that whatever user runs this code
it can actually read the setup table
then you can have this inherent
permissions there
the syntax is an attribute on the method
um and you'll see an example there but I
just want to highlight at the bottom
there's an inherent permission scope
because as I mentioned before we both
have permissions and entitlements by
default this will when you add this
attribute it will give you both
permissions and entitlements I know that
you don't need to worry so much about
entitlements but it's just for
information it is there it can either be
set to both permissions only or
entitlement only
the example that we have is actually we
used to require general ledger entry
read from indirect read permissions in
order to log in
and that's because if we're in the demo
setup then it needs to figure out a
default work date and it does that by
taking the latest entry in the general
ledger entry it's not that we're giving
the user access to general ledger but it
would fail if you didn't have it so
that's why it was there was this odd
indirect permission now we've just
attributed this code
and now this will always
succeed regardless of which user is
running it so this user no longer needs
to get indirect permissions assigned to
General ledge entry
the scope of inherent permissions
follows down the stack so if you put it
on the top then you call other methods
then you still have this inherent
permissions
but
if an event gets raised we strip those
inherent permissions away because you
could not know when you called this code
whether there would be an event
subscriber later you don't want that
code to run with elevated permissions so
it's only for your own permissions it's
only for your own call stack event
subscribers can't do it now of course if
you're if you are the event subscriber
yourself
then you can attribute the event
subscriber with inherent permissions and
now we're back in the game right
so this um allows you to take away some
of these and also make the code more
stable particularly for initialization
or is my feature enabled and stuff like
that so when should you use this
well first of all you should use this
for small dedicated tasks you shouldn't
be running large processes with inherent
permissions that's not what is there
you're not meant to circumvent the
security system
but why should you require read rights
just to see whether this feature was
enabled for instance so small dedicated
tasks ideally
methods that don't call other methods
just to keep it simple
you will probably limit this to critical
code paths where you never want this to
fail regardless of the user
I think where we have mainly used this
are for system tasks for instance first
time somebody logs in and we need to
initialize some tables well it's really
sad to have to give right access for a
user just because you don't know which
user will be the first one who goes into
that and you don't want to initialize it
you can run this with inherent
permissions now you no longer need to
set this up in the permission set
but you also have to think that you're
taking away the administrator or Stan as
we call him the business owner you're
taking away his ability to remove this
right again because you're saying this
code will always just give the user this
permission within this method scope
we've added more to the permission story
we've added isolated events and we've
added stuff to how we deal with
entitlements Etc but these are the
things that we wanted to highlight
to you because they are the most
relevant to you to know about and sorry
for dragging you through so deeply about
the excluded permissions but we want you
to understand how it actually works
so let's wrap this up
so we wanted to create well-defined
understandable building blocks and what
we have delivered there is to help this
is the ability to have these
hierarchical permission sets and a UI
that actually lets you navigate the tree
and see the results of doing this
that's actually also to the part I said
earlier understand what you do
um we want to reduce the maintenance
burden that's mainly regarding this
copying permission set Etc where you
should stop copying flat permission sets
copy by reference instead
if you remember one thing from this
session and that's it that's good enough
for me
to simplify permission sets we have
added the inherent permissions attribute
and then for flexibility we have added
the ability to exclude permissions and
permission sets and remember this also
gives you the opportunity to basically
create an app which contains permission
sets for your line of business and even
if it doesn't completely match a user's
needs then they can still surgically
remove what they didn't agree with
and with that we just want to talk about
there are we are almost done with what
we want to do with permission sets but
there are still some things to do yes
um so I mean we want to further
compromise the permission sets that we
already have I mean all of you know I
mean d35 basic premium all that I mean
includes a lot of stuff we want to chop
that down to bite size as in the keynote
Bugsy mentioned oh Peter mentioned that
uh we wanted to be by like scenarios and
all that
yeah and we're also gonna introduce the
inherent permissions on object which is
basically you take away the opportunity
to set up Security on this object that
should be used sparingly but for
instance setup tables and there are
others where it just doesn't make sense
that you should ever be able to set it
up yeah uh and then we want to improve
troubleshooting tools and have new tools
for you for example if you wanted to
find with like the GL entry for example
that which permission set is actually
granting that permission
and then we're going to add even further
to Telemetry and to auditing
capabilities we already have Telemetry
when permission sets gets added to users
removed from users Etc so that when the
customer calls and tells you as of
Friday I can no longer do blah then you
can actually go in in Telemetry or in
your audit log and say oh well that's
probably because the administrator did
this and then you can actually fix the
problem
and damn we only have one or two minutes
yeah
has anyone have
questions
there's a question there in the do we
use this we can try I don't know
tests yep
okay dude why don't you tell me and then
I'll repeat it
okay
that's that excludes from the
table yes so
