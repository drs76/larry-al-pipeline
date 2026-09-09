# BC TechDays 2022 - What's new in Business Central clients for AL developers

- **Source:** https://www.youtube.com/watch?v=vDts6rloS3I
- **Video ID:** vDts6rloS3I
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 47m03s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

ladies and gentlemen welcome in the
second session for today your hosts for
now are Quentin and Diego
[Music]
Mike yeah welcome everyone to this
session on what's new in business
Central clients for Al developers my
name is Quentin I'm part of the team
working on the AL compiler and all the
development tools and I will be costing
this session on my colleague I go yes hi
I'm ego karatani I work in the client
rank Mt for DC so this is the team that
works for web client
so during this session we will show you
some client improvements that we did
over the last releases we'll then show
you some improvements that we did
specifically on actions and then we'll
show you how we decided to restructure
the whole action bar for alpgs we'll
show you then the new Al promoted model
we'll show you all the new capabilities
that we got out of it both in the
application and in the client and
finally we'll walk you through how we
made this seamless transition for you as
developers but also for your users
all right so I can start with uh
Improvement we did in control add-in
so one of the problems we had with
control editing was that it was possible
for developers to write really bad code
so here you see an example where he
makes a callback request over server
every 10 seconds but it could be that
there's a controlling that does it every
once again or less and we actually had a
case a customer case where they were
complaining that the BC was running slow
and we found out it was because there's
a controller in making tons of requests
in a very short amount of time and I was
slowing down business Central so I can
show you how would that look like so
imagine there's a control ID that does
exactly that so this is making a request
or a server but then without waiting for
the reply for this callback it makes
tons of requests in a short time but
service needs to need to process that
and then you will send the result back
and it needs to do that one by one and
what's bad about this is that the
Callback request from the control add-in
they are processed in the same event
queue that we use for user interactions
such as saving data or activating fuse
so you can already imagine if there are
tons of requests like this you will slow
down business Central
and we try to improve this and how we
did it is this so let's say you have the
same again making a lot of requests but
now we added our internal cue for this
control add-in so this one will make
sure the request is sent one by one so
we send a request and then the result
will be processed and sent back then
we'll process the next one so by
separating the cues now we can have the
event queue for the user interaction
separated from it so BC can run faster
and keep running smoother so
there's some notes I want to make about
the internal queue so when the queue
reaches 20 we start displaying this
warning dialog so we can do that then
user can notice this and then
potentially let developer know about it
so they can catch these issues before
the control adding gets propagated with
more customers
but just a quick note but these numbers
are internal so we may adjust it in the
future but this is the numbers we have
and if the queue reaches 50 then we
actually start ignoring these new
messages and
so that's a new thing that the Callback
requests can get ignored so we actually
extended the invoke extensibility method
API and there's a new callback that you
see there which gets called if I request
it fails or ignored and there is a good
Microsoft documentation on this so I
suggest you to take a look
so the next topic that we'd like to
mention here or the next feature are
list views so list views have actually
been around in business Central for a
few releases but we felt it would be
good to remind you about the
capabilities that they offer since there
is some uh real value for your users so
what are list views and they're allowing
you to Define an alternative
representation of the data on the page
so you can filter and sort the data but
you can also do some UI customization so
that you can emphasize what is the most
relevant for the user in this View
you're defining them directly in Al in
your pages in your page extensions and
Page customizations so you can have them
directly from your pages but you can
also decide to extend the base
application for instance and Define your
custom views
so those views they're available in the
client and then can be customized
further by users you can access them
directly from this drop down or you can
also change view in this section from
the filter Pane and their users have the
ability to modify the filters create
their own views create copy of your
existing View and they can customize it
further
if we look at how this is under the hood
in the AL code we have a news
section here that you have on your pages
of type list and there you can Define
your view your view has a set of
different properties so here we have a
caption that is set we also have some
filters that are defined but also
another property that is here allowing
you to set a sorting Direction on one or
multiple fields
this one didn't have any UI
customizations and that leads us to the
next topic related to views we are
distinguishing between two different
types of views in business Central so we
have views with shared layouts which are
views that are just sharing the same
layout as the default view all which is
the view that is opened automatically
when you're opening a page and on this
view all the user personalizations and
profile configurations are applied
automatically the same way they are
applied on the default view
the second type of views are views with
their own custom layout so you can then
Define in code how the layout should
look like and those ones are not subject
to user personalization and profile
configurations
if we look now at a view that has a
custom layout you can see that the view
also here are some properties to filter
and so on but it also has a dedicated
layout section and in this section that
is very similar to what you would have
in a page extension or page
customization you can reorder fields and
you can also modify some of their
properties such as the visibility and
this in this example here I'm moving
first the name and balance and then we
have the phone number that is hidden
because it doesn't appear as relevant to
the user
so this is how you can leverage views
yeah so next I want to present uh one
Improvement we did for the data entry
for the grid
um so we had a problem with entering
multiple rows very fast we previously
made some improvements for multiple
columns in the same row but the problem
here is that we had only three draft
rows so if you were entering a lot of
rows quickly you could quickly run out
of these rows and you had to fill those
up before you can enter new rows so this
one can show how that would look so you
have three referrals there and if you're
entering Row one by one that's okay so
let's just say you entered one row then
we'll ask the server to create another
row to fill up the number of draft rows
so if you're doing that one by one that
is great it works fine but if you are
really entering rows really fast and you
can see in this case you made a lot of
rows three at once and then you run out
of draft rows so what we used to do we
still need to ask the server to fill up
these new referrals so you have to wait
for the reply to come back before you
can enter new rows and so that was
causing some performance issues for some
users the way we improve this is to
increase the number of draft rows to 15
so that's what we do but we still show
only three in the UI so I can go through
the same scenario that I just showed you
with this so if you do one row at a time
that is still the same we will ask for
the Callback to the server and you get a
reply and then you update the UI so
that's the same but then let's say you
enter three rows at once really fast and
now at this point we know that we have
still 12 rows available so we used to
ask the server but now we don't do that
we don't need to do this because we know
there are still Draft rules available so
we we can update the UI in the browser
side without contacting the server then
after that we do we still need to ask
the server for more rows but since the
UI was updated in the browser side user
can continue entering more rows really
fast
okay so now we would like to go through
some of the improvements we did for
action
so the first Improvement that we'd like
to show here is related to scope
repeater actions so those are the
actions that appear directly on your on
the rows of your list pages
and we're showing you here a snippet of
code
um that defines an action with scope
reviewer as you can see with the scope
reviewer property and we'll ask you now
what is wrong with this action
and well the answer is that you actually
needed the action to also be promoted in
order for it to always appear on the
page and that wasn't something the
compiler would let you know about you we
had it in the documentation but since
the compiler wasn't warning you about it
they were I think quite some chances
that some of your apps might be impacted
then so we decided to to fix that for
version 20 and earlier the behavior
Remains the Same so those scope repair
actions needs to be promoted but we're
introducing a new UI Cup rule that will
let you know that you have to use the
promoted action and that will be of
course version depending on the versions
your business Central you're targeting
and for version 21 we have fixed it so
that the scope repeater actions are just
displayed independently of the promoted
state of the action
yeah so next we have the split button
um so I'm sure you saw this in the
keynote already but now we have split
button in BC uh split button is another
New Concept that we we invented it's a
common UI component that's used across
different products and so for example
this is a one from the Outlook so
there's one called new email that you
can click on this button to invoke the
action associated with it or you can
click on the drop down arrow then this
will show other related items so we can
do this now in BC and the way you do it
is to have a group of actions and then
there's a new property called show as
and they need to set that to split
button and then the first visible and
enabled action from the group will be
used as the primary action of the split
button so in the screenshot you see
there there's a post action being shown
as a primary action and you can click on
it to invoke the action or you can click
on the drop down arrow which will
revealed all the actions inside the
group
so the next topic that we'll mention is
a topic that you've seen during the
keynote there was also a dedicated
session earlier today but it's related
to power automate
um Power automate allows you to create
automated workflows between products
without writing any code and among those
products you also have business Central
for which we have a set of connectors
that you can use
one of the main changes you'll see in
this release is that the poor automate
flows Associated to a page automatically
discovered and available in business
Central and you also have the ability to
customize those and move them around on
your page to put them where you think
they fit best
so in order to do this we had to have
some language support for it so we're
introducing a new concept that is named
custom actions and that we will use to
trigger actions outside of business
Central
and and right now you have the ability
to Define then actions of type flow if
we look at how the code looks like here
I'm adding a next custom action to the
customer card that points to some flow
there is a custom action type that is
set to flow right now so in the future
we'll reuse that concept when we Define
other scenarios and then you have some
properties that are dedicated to power
automate flows so you can get this
information from Power automate and then
fill in the flow ID or and the
environment ID where the flow is located
and that's how the runtime will know how
to trigger the flow
if you want to know more about this
there was a session earlier today about
empowering citizens and pro-l developers
to do more with Power Platform and we'll
then recommend you to have a look at the
recording when it becomes available
all right so now uh we like to introduce
you the new action bar syntax we
implemented for the full release
but before doing that I think it's the
best to explain how the action bar is
made today so here you see a very
typical action bar in business Central
and there are two parts to it and
there's one on the right hand side here
we sometimes also call it the action
repository so this is where all the
actions you define in AO including
groups will show up by default so you
can have a nested groups and all the
actions they will show up here and we
also have ones on the left these are we
call it them promoted actions and these
are actions that are promoted from the
right hand side and you have up to 20
promoted category groups where you can
put these actions into
and in AO code this is how you would
used to look so you could change the
caption of the promoted categories using
this property and to promote an action
you had to set the promoted property to
true and by default a promoted action
goes into the new category but you can
change that using this uh promoted
category property and we also have this
promoted is Big which was the Legacy
property we inherited from the windows
clients UI ribbon UI and this you could
use this to change the ordering of
actions and we also have promoted only
which was the property used to show
actions only on the left hand side but
you can probably see but promoted
actions are created implicitly because
you're not really telling the error code
where the action will show up so you had
to set the property to true and then the
client us will render at the right place
so this had several limitations and
restrictions for example it was not
possible to choose the exact ordering of
the promoted actions because you could
only specify where it goes into the
category but you couldn't choose the
ordering and you could also not create
new categories you had only up to 20 of
them and it was not possible to reorder
those categories either and another one
is that you couldn't create any
subgroups within those categories and
because of these language limitations we
also had some confusing experiences in
the client inclined designer so you
couldn't drag these promoting categories
around also you couldn't change the
ordering of the actions within a
promoted category so on top of this we
started to get very complicated pages so
for example our customer code has
literally more than 100 actions and it
was getting hard for us to create a very
well organized and user-friendly action
bar that can adapt to different
scenarios so we thought about maybe
having a extending of ideas of the
action repository concept so we could
maybe have one place where we have a
bunch of actions defined on the page and
you can select actions from there to the
left hand side and having references
maybe was a good idea because you can
have ways to have multiple promoted
actions in different places in the same
page which will allow you to have more
flexible and then comprehensive layout
of action
so this is those are the challenges that
we face with the previous model we're
using promoted properties and in order
to solve those we've introduced some new
Concepts in the action bar in ale so the
first one is that we have now a new area
that is named the promoted area and that
explicitly represents the left side of
the action bar and that one can contain
groups and references to actions the
second concept then is the new action
ref syntax and that is a new construct
that is representing a reference to an
action
they can only be defined in the promoted
area and they will inherit most of their
property from the target action since
they're just a reference and we don't
want to have code duplication they're
inheriting everything there only the
visibility can be customized
so we'll now move to visual studio code
and have a quick demo of how the
experience looks like editing those new
actions
so
I have a page here that is a pretty
simple one it has
a group with some actions and as you can
see none of them are promoted here
if I wanted to promote them I could use
the old model but then I would have some
limitations around where I'm defining
them and it's not really matching my
needs so I'll just start by writing a
new area here and as soon as I write I
get intelligence suggesting me that
there is a new area name promoted so
I'll just use that
and now I want to create a reference to
my actions so I'll use the snippet to
create a new actions and I have now to
specify a name for it so I'll just name
it action ref1 because I want to keep
things pretty simple here and then if I
move to the other part here I have to
enter which action I want to point to
and here I can specify either an action
or a custom action that we presented
before but if I use intellisense you'll
see that the suggestions are already
tailored for that and I only have
actions and custom actions suggested but
no groups or separators so I just use
action one here
and then again if I use intellisense to
see which properties are available for
me you can see that the visibility is
mentioned and the property is related to
obsoletion none of the other ones are
there because they're all inherited from
the target so I'll just set the
visibility explicitly to True which is
also a default value
and at this point you'll realize that
we're already some doing something that
wasn't possible in the old model because
now we have an action ref that is
defined directly in the promoted section
so as a top level action but if I wanted
to create a group or a category in the
old uh namings I can easily do it I just
create the group syntax the exact same
way I would do it on the other action
categories and once I am in this group I
have the ability to Define action refs
and then since I am explicitly defining
them I can choose in which order they
appear here I have first an action rate
for Action 2 and then action 3 but I
could just change them and Define how I
think they should appear in the UI
also this since these new categories are
defined as groups they are much more
customizable than before the promoted
categories could only have their caption
updated but now I get a whole range of
new properties that I can set on them
and I just use here the split button one
that was just shown earlier
now since this is a group I can also
have other groups defined so I can
create a nested group and have here
another action ref pointing to my
remaining action
so if I just take this app that I
published already and show it in
business Central you'll see that I have
my top level action showing here I have
here my group with the split button and
I have here the actions under it and
then my nested group so that unlocks
much more capabilities for you when
you're defining those if I go back now
to the presentation
we can have a summary of the
capabilities between the two models so
for the permanent models we were limited
to 20 categories and we couldn't create
new ones that's something that is fixed
now I can explicitly reorder them I can
Define subcategories if I want to
they are much more customizable I can do
other things than just changing the
caption I can order the action ref
exactly how I want them and I can even
Define them as top level actions
so that shows the new capabilities we're
getting now
one thing to mention though you cannot
mix the promoted action syntax and the
action ref syntax within the same object
so if you're defining a page or a page
extension you have to choose either
you're still using the old syntax or
you're moving forward
but you can have objects using the
action ref syntax and some other objects
using the promoted syntax within the
same extension
so now iGo will present you how we
made them work side by side yeah so as
quintan just explained you cannot mix
the V1 syntax which is the promoted
action syntax and the V2 which is the
action ref syntax but you can use
whichever format you want to use for
your extensions and the base page can be
either in V1 or V2 so you can have them
side by side and this is possible
because V1 pages are converted for you
into the V2 format under the hood so you
don't need to worry about which format
that you have so I can show you that in
demo
so
all right so let's say there's a page
that you don't own this is a page
written in a V1 and you can see that
there's some actions are has promoted
and it has promoted is big and so on and
you decided to write an extension on
this V1 page and since you like the
action ref syntax you decided to write
this in V2 format which you can do so
so here I'm just changing the ordering
of the promoted categories this is
something else you couldn't do before
you already noticed that this name of
groups are created for you automatically
so if I try to start typing you can
actually see
this chromatically category groups are
there for you to use
so this one really shows you that the V1
page was converted under the hood
and I can also move action around
to the root level so this one shows you
the action one which is underscore
promoted this is the name of the
promoted action that they generated for
you so the base action was called action
one over here but this promoted version
of this over there so you can already
use this to make your extension but you
can also Target the base action if you
want to do that you still have access to
the action too this is the base action
one of the base actions you see there
and you can change the caption and
that's great you can do that so this is
an example of how you can write the V2
extension on top of a V1 page but let's
say the owner of this page decided to
update a new syntax now so they wanted
to convert this page into V2 so the one
way you can do is to use the code action
we added code action is a visual studio
code feature that you can use to invoke
some actions when you execute it and
Quentin will show after this more about
this but just I'm just going to use this
for now to convert this page into the
YouTube format so you can click on this
and now the page is converted into V2
already so I can maybe show you that in
the
get a diff so it's easy to see what
changed so you can see that the Audi
promoted related categories are removed
for example the name of the categories
are not there anymore but instead groups
are created with the caption you
specified and
for the promoted actions they are
removed and then action refs are created
and if you pay attention to the promoted
is Big property so these two action one
in action 2 were promoted into the same
category but the second action had
promoted as big so you would expect that
the action 2 comes before action one and
that's exactly what's happening here so
you see the action 2 first in action one
so but there's one uh thing to be aware
of if you are converting your V1 page
into V2 format in order to not break any
dependent extensions extending your page
you need to use this naming conventions
that we created so for promoted
categories you want to use the category
underscore and name of the category so
in this case the process and then for
Action ref you want to use the name of
the action underscore promoted so by
using this convention you can make sure
that there are any dependent extensions
will continue to work so if you remember
how the extension we created looked like
it was already using these naming
conventions over here
so that's great but we actually added
appsource cop rule so you can notice
this if you didn't name your action refs
or promote characters properly so let's
say I didn't use this naming convention
but use something like action one ref
then
yeah there's a error that you get here
saying that action one underscore
promoted is not found so it's telling me
that the any some dependent extensions
may break so this is a way that you can
use to make sure that the extensions
will not break you on your page
yeah and then this is just a summary of
how a valid conversion should look like
um for promoted actions you should use
the name of the action underscore
promoted and for promoted categories we
have the category underscore promoted
so you've already seen that you can rely
on some tooling that we're proposing you
in Visual Studio code to make sure that
your conversion is done properly and we
see now that works on one page but when
you're converting an app you have
usually more than one and you're using
this promoted properties in
a lot of them so in the next demo we'll
show you how we decided to leverage some
of the capabilities that Visual Studio
code offers with Collections and improve
them so that we actually can offer you
now the ability to fix multiple Pages at
once
so as you can see here I have opened the
system application for Microsoft and I
have a version here of the system
application that is using promoted
properties so you see that I have quite
some of them
if I go now to visual studio code and
use the light bulb that was shown before
you can see that we have now different
Scopes that are appearing we can run the
The Collection either on one specific
instance on all of them in the same
document so if you using different page
objects in the same document which isn't
really a great practice but we would
support that too and you can do it on a
project and even more interestingly on
the workspace level so if you have
multiple projects loaded together in
Visual Studio code you can also apply it
there so if I run this
I should see that now all my pages have
been converted
let me just reload the environment
so I have the promoted properties I will
just select one page here and run
through the code action
and then what you would see I will jump
to git is that I'll have the same kind
of changes done as what I go presented
earlier so we just need a bit of time
for the workspace to finish loading and
get another chance for running that do
we edit this capability uh here for this
specific action for the conversion but
that's not the only case you'll see it
we have it added it also on the UI on
the quadcop rule for a missing
parenthesis and in the future we'll be
adding into more codections that are
available through Visual Studio code
so this takes a bit of time
I think we might just yeah move forward
so we'll show you another demo of it if
we have some time at the end but you
have the ability to run it on different
Scopes and we actually use this to
convert the system application and
brought it to the latest format and we
did it not only on the system
application but also on the base
application and that allowed us to have
also the chance for making further
improvements in the beta sub
so
now it actually worked if I save all the
files here and I go to git you can see
that all of them were converted the
exact same way
um as when one page was converted so
removing all the promoted properties and
using the action array here
so
if we go back now to the presentation
we have converted the base application
but then we also took the chance to to
do a lot of improvements there whether
they're in the client or in the
application itself we could leverage the
new syntax that we had and we have here
a comparison between the sales order
action bar and version 20 and version 21
and you can notice some things already
so when you open it now the action bar
will be automatically pinned so that you
can get access to the most important
actions in one click
we've also as mentioned during the
keynote used the Telemetry that we had
in order to reorder the actions based on
the usage that we've seen and in order
to have them in a in a more consistent
way
we've also
cleaned up the top 40 categories that
you can see here and decided to move
some of them as sub categories so that
they make the most sense for you
we've also decided to leverage the use
of split buttons so that now you can
also access the actions within those
subcategories in one click
and we've decided to merge The Entity
group so here there is appearing as
order and the navigate group because
they had some kind of overlapping and
similar meaning and created some
confusions for users that were coming to
business Central
finally the last thing you'll see on
this slide is that we're automatically
renaming the process category to home so
that we're providing an experience that
is more in line with other Microsoft
products
so with all of this we're aiming at
making it simpler for you to navigate
the action bar but also where you try to
improve the consistency of the action
bar across different pages in the
product in version 20 you can see that
the top categories were already kind of
aligned but then if you look at the
action within them that was pretty
different from one page to another and
users then might have had to relearn how
to use each page
with version 21 I'm taking the same
three pages as before we can see that
the top categories are much more similar
then of course there are some changes
that are specific for each of the pages
but also the actions themselves then are
appearing in the same orders with the
same split buttons at the same places
and so on so that when users are used to
a page they can just move to the next
one easily
yeah so we talked a lot about the AO
improvements so now I want to show you
some of the client improvements and
capabilities
so it's a good news that the action bar
of personal Edition will continue to
work with the new model now it's
actually more powerful because you can
drag categories around and you can Nest
the groups and move actions to the root
level you can do all you can do all that
now
um and then another Improvement we made
is one ux Improvement so in previous
releases we had the some actions that
could be removed and some action that
could be hidden and it was really
confusing to see why we had this
difference you really had to understand
how the promoted actions worked in Al
and then regular users couldn't possibly
figure this out so in this case removed
was actually selling promoted only to
true so this implies this action is
already promoted somewhere else and then
height was setting visible to false so
this was very confusing so in version 21
we made it consistent so that the
removable always remove the action or
action ref from the current extension
you're designing and height will set
visible property to false
and I also want to spend a bit time uh
discussing about the promoted only a
little bit so in the new action bar
syntax we no longer have the concept of
promoted only and we wanted to treat all
the promoted actions by uh promoting
only by default and this is by Design
because we wanted to let users focus on
the promoted section so so they spend
less time on the repository area to find
their actions so we actually added
several UI capabilities to do this so
users can start focusing more on the
left hand side so here's one of them we
did so if you have a group of actions
that are all promoted in this case you
have a group there and then both of the
actions are promoted we no longer render
this on the right hand side because you
already have them available on the left
hand side so this is a screenshot that
you see there you can see that there are
no actions on the right hand side so
this is one change we did so that we can
reduce the Clutter and let users focus
more on the left hand side there's
another UIC
ability we added so if a group has some
promoted actions in this case you have
three actions and two of them are
promoted and the last one is not and if
you render this this is how you will
look we will still render the group
there's a posting group there and
directly under this group you have a
list of unpromoted actions inside the
group and then for promoted actions we
added a system group called other that
you can see here and we hide the
promoted actions into this group so a
user will need to have one extra click
to get to those so this is a way for us
to encourage users to focus more on the
left hand side
and here you can turn off the use short
menu if you don't like the other so you
can have a list of action in the same
group
so I can show you some of this in the
demo
all right so here is a sales invoice
document and I can show you how you can
now drag actions around at the root
level so you can have the invoice group
and change the ordering of the groups
which you couldn't do before and you can
also open the group and change the
ordering of this action this is also new
you can even decide to Nest the group
into another one so you can take this
and then put it into the invoice group
so that's new
um and lastly I want to show you about
the other menu UI so this group has
three unpromoted actions and you have
the bunch of promoted actions into the
other menu we also added a tooltip so
that the user can learn what this menu
is used for so let's try to hide start
hiding these actions because
now this attaches PDF is the last
visible action which is not promoted
inside this group and if I hide this or
move this out of this posting group then
and all the actions in there will be
promoted so in this case the posting
group will be hidden so I can try to
maybe move the style of the posting
group
so now you notice that the posting group
is now grayed out so this is indicating
that it will be hidden and all that
that's because all the visible actions
are promoted somewhere else
so and then if I exit personalizations
there'll be no more posting group
so this way we can reduce the Clutter
more on the right hand side
so let's go back to the slide
so yeah we talked a lot about how air
developers can update the new syntax and
then transition into the new one but uh
since I I just demoed
um some capability in the UI capability
changes that will affect the current
current users so I want to also discuss
a bit about how users can transition
into the new layout
so for that we added a feature flag
called modern action bar and this is um
disabled for existing users for
upgrading to version 21 but for new
users we enabled it by default so they
can get the shiny layout
um so I can explain more about what this
flag does but basically it when it's on
you get the full action bar experience
but when it's off we turn off or revert
some of the features we did the ones
that the most has the most UI impact so
that users who are used to the old
layout continue to see the same looking
action bar
um so here's the future management page
and you can actually have a find a link
that says try out so user can actually
click on this and see if they like the
future or not so that's easy for them to
do
so here's one feature that we try to
revert when the feature flag is set to
off so as Quentin showed earlier we
decided to Nest some promoted categories
in the version 21. so for example here
you see the release and post actions
being nested inside the process or home
group but this is a change in the layout
so in version 21 if you have the feature
flag set to off we will move any nested
promoted categories back to the root so
you see the one that's above in the
screenshot there so this looks like what
it used to be before
and here's another thing we do so let me
just explain a scenario so here you have
a group that's hidden and inside here
you have an action which is promoted has
a problem that equals true so in version
20 uh you will still see the promoted
action on the left hand side and that's
because the way we created the promoted
action was by taking a copy of the base
action and then put it into the left
hand side so it was no longer under a
hidden group when it was moved to the
left side but in version 21 we have
action reps and the visibility of action
ref depends on the visibility of the
base action so in version 21 you will
not see this action and that would be a
breaking change so again if you have the
feature flag turned off even with this
layout in in this ale code you will
still see the action promoted in the
left hand side
and for those we have also added UI Cup
rules so that if you're in these
situations in your Extensions by
enabling the UI cops you will get some
additional information about this
pattern being used and the fact that
we're changing the behavior at runtime
so the other thing that is impacting
user is not just the layout of the page
the the action bar on their Pages as
such but also all the customizations
that they did over time because you and
your users might have customized the
pages and this might have used also the
promoted properties and as we've seen
before we cannot mix the uh promoted
syntax with the action Drive syntax so
we had to find a way to convert all the
different types of personalizations that
you can do in the client in business
Central
for user personalization we've defined a
fully automated experience so the con
the customizations which are stored also
as Al code will be automatically
converted this will reuse some of the
internals of the code action that you
see in JS code so everything is tied
together and that will be something that
should go to Italian notice for the
users it should just work out when they
start using their environments in
version 21.
for profile customization same
experience the conversion is also
totally automated we're also doing it on
import so if you have exported some
profiles that have promoted syntax and
you're importing them on your new
environment they're converted
automatically to the latest syntax since
we know that some of you are keeping
their profiles on their Source control
and are editing them in vs code we've
then decided to add some extra
information during the import process
but also started to add partner
Telemetry photos so that you can get a
summary of the operations that were done
on your code
for the designer mode that you have that
is available in sandboxes or that you
can get by publishing your extensions
from vs code and starting the designer
in the this extension context we've
defined a one-click conversion so if
you're starting from vs code you have
the ability to use the code actions that
we just shown earlier but if you're also
publishing now an extension that has
some pages in The promoted syntax you'll
see in the web client that you have this
lock icon here and that one will prevent
you from customizing the page but if you
just click on it you'll have the
opportunity to convert your page
automatically
so just to show you uh now a short demo
of how the experience looks like when
you're importing profiles
um you have here your profile zip that
contains different customizations and
some of those customizations you have
here some promoted properties
if you take this to business Central and
then run through the client the import
profile feature you'll get through the
wizard here and you'll have a warning
that is reported the import is
successful but there is a warning so
let's see what that one says
if we look at it it tells you that the
runtime has detected the usage of
duplicated constructs that's converted
them to the latest syntax so you have
here information about the conversion as
mentioned we've also added partner
Telemetry signals so that you can have
another way of tracking this down and we
are showing you here as well all the
additional Telemetry that we added for
profile configuration General so you'll
be able to know now when your profile
configurations are being changed updated
removed created exported and so on
so if you now decide to take this
profile and just export it from your
environment you get again a zip file but
now when you open the customization you
see that the file has been converted to
the latest syntax and it is equivalent
to what you used to have previously
so as a summary for this session you've
seen different things we've shown you
mainly the new promoted action model
based on action refs we've shown you
also that you have now the ability to
create split buttons but also Define
some custom actions pointing to power
automate flows
yeah and then for client features now
you have scope repeat actions that you
can use without promoting the action we
also pin the Home tab by default
um yes the the group has been renamed
from process to home and what an
actionable features an enhanced
personalization capabilities and lastly
the automated conversion of the client
customizations of Quintin just demote
and with this this is concluding our
session and presentation here so we'll
take questions if you have
some so make sure to
get the microphone up yeah yes first of
all it looks nice the new action bar but
I have a question you're saying you are
can do one things in one click
how about the keyboard access you know
the users that are heavy users using it
all day they are complaining from using
the mouse all the time to to click have
you done any improvements or are you
thinking about doing any improvements
for the action bar
to access it from keyboard only right so
the action by already supports most of
the keyboard access did you have any
problem exactly uh describing the
keyboard issues
how do you access the the action bar and
move around in it without using the
mouse right so you can you use a tab
keys to First focus into the action bar
so you once you have focus in one of the
buttons you can use it Focus around but
then you need to have Focus first right
right yes you don't you have not made a
shortcut or something that brings you
directly to
yeah we don't have that currently okay
suggestion yeah but but nice
okay
any more questions
nope
throw this one
who was it
let's see yeah okay yeah
are there any options to Advent time
change the action bar
so to help the user only see
the actions uh suitable for a current
state of the record
so you have the ability to Define some
variables that would control some of the
properties on the actions themselves
then for the action refs they are very
simple and we do not allow you there to
have some conditional Expressions but
since the visibility of the action RF is
defined by the visible property on the
action ref and the one on the base
action you can have then some controls
on changing your action bar layout at
runtime on the non on the repository
sidewalls on the promoted side using
those
okay
yeah I see one question over there yeah
okay
I think that will be the last question
and then we'll be available for you
after I have a question regarding the
Callback from the control add-ins the
new one yeah that's only thrown for
errors that occur during uh during the
queuing not any errors that occur in the
AL code right
right so that is also used for the one
is ignored an error from the Callback
yes I believe
from the code as well so do I get any
any uh information which error was
thrown
no I think you just you just get a
callback but it doesn't tell you which
area occurred I believe so
okay thank you
yep I think if you have more questions
we'll take them after the next session
or ask them directly through the app
thank you
[Applause]
[Music]
