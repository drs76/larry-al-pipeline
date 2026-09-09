# BC TechDays 2022 - Adopting "Onboarding first" developer mindset

- **Source:** https://www.youtube.com/watch?v=_DCc62HWxMY
- **Video ID:** _DCc62HWxMY
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 45m30s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

welcome everyone to adopting onboarding
first mindset
uh
i'm thomas groblowskas i'm engineering
manager at business central client team
and with me i have cody yeah i'm cody
hoover a software engineer under thomas
on the client team yep our team is
responsible for developing business
central mobile and web clients and we
also we're contributing to onboarding
effort
so onboarding framework
it's
one of the continuous investments we
have been doing for at least last two
years we have been adding new
capabilities release over release we
have done that because we truly believe
that onboarding framework can help
partners to transform
their process and their business into
scalable
fast growth
mode
because onboarding framework helps to
take a very
repetitive tasks and turn them into a
really repeatable process that is
codified and can be shipped with
extension instead of being a loose
process defined server on paper maybe at
first
yeah
and today we're going to take a bit more
developer focused approach we're going
to take a look at al code we're going to
also give a little bit of sneak peek and
design thinking what like what is what
were the thoughts behind that code
and hopefully will inspire you
to also
come on board onboarding journey
so
looking at the agenda
first we'll take a look a bit what is
the onboarding first mindset we're going
to take a look at some of the building
blocks how to build a good checklist
how to guide users through configuration
or automate it at best
how to enrich onboarding experience with
page links videos and also adding tours
to pages so you can introduce pages to
your users who have never seen that page
before and lastly we also take a look
how to leverage the help pane
but before we dive in i just want to
maybe show hands how many of you looking
at the agenda have
seen or heard those topics
could you give a shout of hands okay
we have a couple
how many of you tried those concepts in
ale
all right we also have a few and how
many of you have onboarding pieces at
least pieces of onboarding framework
running in production right now
oh yeah we also have a couple so
hopefully our mission today is to
inspire you
to first
get
overview of what is possible how to
apply it and use it in your production
code
yep
so
onboarding mindset
first
onboarding mindset is
to start early
onboarding should not be an afterthought
that you put once you've finished
writing code or inverse already shipped
in
production it should become part of your
developer workflow and even further
design and requirement analysis flow
you should take a look at your product
and
the functionality it provides and sit
down and or at least imagine a
consultant role in your mind and see
which steps of the onboarding are
repetitive very labor intensive that
means a lot of manual work and can be
easily transferred to code or ideally
automated and taking these processes and
then trying to codify them in all codes
so they become repeatable and
consistent as well with consistent
quality and of course as any good
developer mindset it should be iterative
so you implement
you see the results from live getting
feedback from consultants you tweak the
process and you keep going until it's
perfect
so
today
we're gonna
take a
look at
a simple extension we have built to show
off some of these uh capabilities we'll
be stepping into shoes of an icv
developing a shoe management extension
and just to warn you there'll be
probably more shoe related puns in the
presentation
so
i will be assuming you're all of more of
a
let's let's say a product manager
someone dealing with business
requirements
taking users perspective and not so much
oriented into code and cody will be the
opposite uh he will be writing code and
also guiding us through what is possible
in onboarding framework and helping
us to arrive at uh a great conclusion
so maybe let's take a look first what do
we have in our sample extension yeah
[Music]
great
so first let's go ahead and start with
what are the basic building blocks of
just switch your screen
nope uh
extended instead of duplicated
fantastic
so let's go ahead and look at the the
base pages that we have in our
application
[Music]
to know what sort of onboarding flow we
might be working with so
it's a shoe management application
where our main entry point is going to
be a list of shoes that we have in our
inventory
currently it's pretty empty
and then as we receive new shoes into
our inventory
we expect they are going to
be entered in we can type in
information about that shoe itself but
what's really important for people
wanting to buy the shoes from us is
if we have the right size
right now i can see though we don't have
any size information
yep so looking at this extension we
could call it
feature complete uh and just call it a
day and ship it to appsource but of
course now we're a bit smarter we are
trying to
adopt this uh onboarding first developer
mindset so we'll be taking steps and
adding and enhancing this
extension and one of the first things we
should think about is setup cody what
kind of setup do we need for this
extension
well
right now i see that i have a size list
it's empty if i wanted to add a size to
it at the moment i don't actually know
what size i should be adding am i going
to use a u.s size a european size yeah
that's going to be tough to settle on
because i'm from eu you're from u.s so
tough choice yes but i think what we can
do is give the users of this extension
the possibility to choose for themselves
we can use an assisted setup that'll
guide them through that setup process
and allow them to make the choice that's
best for them
so let's leave the product now and go
into
code
and see
what we can do so first for an assisted
setup right we're going to have the page
itself and we won't go through the code
for that it's just a simple wizard that
prompts the user with a choice but once
we have that
that page that assisted setup wizard
available
we need to expose that
so we can do that
in the
via code unit
where
using an event subscriber to
sign up for the on register assisted
setup page
we can go ahead and call the
guidedexperience.insertassistededup
assisted setup function
and point to our assisted setup page
the great thing about this
guided experience
insert assisted setup is that not only
is it going to make this available as an
assisted setup in the set of all setups
available to the
users it's also going to expose this
further to the onboarding framework so
we can put that in a checklist
so users will know to go through this
right away when they see the product
but for now we've just added this to our
library of possible items to actually
put that in the checklist so our user
gets to it right away
we're going to do that as part of our
app installation
so we've chosen to do that in the
uninstall app per company
trigger the reason we're doing that is
if we ever want to add new checklist
items
or update this after
some users may have seen a checklist
before this will ensure that gets added
but there are a lot of different life
cycle events and triggers that may work
better for your needs
let's go ahead and see
what we need to do to get that into the
checklist
so here we are actually re-inserting it
re-registering it as an assisted
setup um through the procedure from our
other code unit
and then we just call checklist.insert
we just have to tell it that it is an
assisted setup and tell it which
assisted setup we're pointing to
and it will appear automatically
we can also choose what order we want
this to be relative to other checklist
items we can limit what profiles this is
relevant to so we could say that it's
relevant to all users regardless of
their profile which is
what we've actually done here or we
could limit this just to some specific
profiles
we also have the ability to choose
whether all users should complete this
as part of every user's onboarding
process or in the case of our
this assisted setup we only need to
insert those
those sizes once so that we can pass
false
it is important to note that
if you call
either of these methods more than one
time the call that comes last is going
to win so if you
if you there we go um
so if we were to
nope okay
getting weird um so if we call uh insert
assisted setup
later with different text
that's going to overwrite
what was called the first time but since
we're just calling the same procedure we
don't have to worry about that
that was simple
what are other types of guided
experience we could insert because this
looks like a meta that has more members
yeah so right now we're just using it at
register and assisted setup but we could
also go ahead and add
some help links videos tours and i'll
talk a little bit more about each of
those so a help link or a learn link is
just going to insert a url
that can be added to a checklist that
will open to your own documentation site
it might link to a partner integration
if you're integrating with some other
services that's relevant to your setup
and
the same as before
you can call this insert learn link and
then if you did want that in your
checklist
you would just have to say that it's of
type learn and pass that same url that
you registered with
similarly we can add a video to give you
a video tour
recorded for the product or any other
video information you want
if we want to guide them through some
great functionality that we add in our
extension we can start a tour directly
from this checklist that's going to take
them to the page
give them some information about it and
guide them through the important fields
actions etc on their page and for this
again we're just going to call insert
tour
and pass the the page that we want to
lead to
now
if we are perhaps extending some other
page so we're adding fields somewhere
but we we want to make sure our users
get a tour to that page i mentioned
before that if we were to call this and
point
to some other page that we don't own
but we might overwrite something that
the original extension may have or the
original app may have defined so instead
of setting a tour on some page that we
don't own
there's yet another one that we can use
instead called insert application
feature
now insert application feature does a
very similar thing to tour or to the
other ones except instead of only
pointing to a page we can point to
anything so let's say that we've
extended a shoe card from another app we
can actually insert an application
feature using a code unit that's going
to launch the shoe card that means we
can provide whatever extra information
and context we want in that checklist
experience without overwriting what the
original author has done and again the
same we just insert it as an application
feature with that same
information
amazing that was a really nice summary
of all the different guided experience
items that can be put together and it
also displayed how we can combine
both internal application features and
external external rich media like videos
and links to create a really
nice step-by-step onboarding experience
so maybe let's take a look how that
looks in practice absolutely
so if we go back to the extension that
we've deployed that has our checklist
the first thing that our users are going
to see when they they open to to get
started is this welcoming banner
if they accept the prompt to get started
they are going to see
this item to start
setting up the shoe extension
so if they go ahead and start that this
starts that wizard that we added as our
item earlier
we can
choose the shoe sizes
let's go with european
i guess i don't know what size i am
but we'll make it work um we can then go
ahead and just take a look at our shoe
sizes list and see that those were
already added users shouldn't need to go
do that
um
and this is an example of teaching tips
that we'll come back to later
um but great so our assisted setup
worked
so we can go ahead and finish that
now
we didn't
intentionally add this here
but we can go ahead and see how we can
add some additional checklist items even
without doing encode
so
i can go to the
checklist administration page
and here i can see all of the
checklist items that are currently
configured across the company we can see
that we have a lot of
items for a bunch of different roles and
we can also see this setup
shoe extension that we
um that we added
if we wanted we can go create a new one
and create a checklist item so
uh what we wanted was a tour right
so we can click on this tour
from here we can see all of the tasks
that are registered as tours so these
are items where somebody said guided
experience.insert tour
if we had chosen
one of the other types we would have got
a different list
so here we want the tour
this is actually going to tell me that
one already exists because as we saw
there was a tour checklist item on the
role center that's going to make sure
that we're aware that we're overriding
something
that somebody had already added
but like i said there's a way we can get
around that
we can go to the application feature
instead
and uh from here
we can actually launch some other tour
some other
setup page
but that's
actually not what we want so i'm going
to go ahead and delete that
and just like that that will no longer
be
on the page
so that's how we can even without code
go manually
configure
checklist items
this is really great because what kodi
just showed there's
two paths you can if you're building a
bigger application that requires
extensive uh setup you can just
programmatically create checklists
together the guided experience items
that you insert and just ship that out
of the box and once the extension is
installed the checklist will be
populated and consultants can complete
the final setup or this other way if
your app is smaller
or not necessarily you can insert the
guided experience items as options to
the guided experience administration
page but not directly insert to the
checklist so you leave
it to maybe a bar who's assembling a
different uh
ip from different providers and building
the final checklist not programmatically
but just by manually assembling tasks so
this is really powerful because it
allows to tailor the experience on
based on what is required at the last
mile
yup so this is really neat
so we just
kind of are done with the checklist and
we are now adding the tour to a page
that is uh unfamiliar to the user and
consultant probably would like to show
it and demo it in an expressive way so
the next thing cody what do we have for
that yeah so
so we can see that we've already added
here we want to start a tour but what is
that tour actually going to show the
user and how do we make that available
to them
so we want to take them to the shoe card
page
and if we look at this
uh all tours must have must start with
some properties at the page level
uh so if i go
and do
uh these properties for the about title
and the about text these are the two
properties that are required for making
that appear
coded what are those stars
yeah this is something that's starting
to pop up in some of the
strings that we can add but we can use a
bit of markdown syntax so here we've
used stars to bold
the name of a page
now
we have some guidance on when to use the
syntax such as bolding or italics or
links
in this case we're using bold because it
is the name of a page we want to
emphasize uh
the name of sort of a proper noun in the
context of business sensual we don't
want to overuse this because we don't
want our teaching tips to be very shouty
and
overwhelming to the user but in this
case this is important enough that we
think we want to add it
but in some places we actually want to
emphasize it even a little bit more
i think one of the most important fields
on this page is the size field
so if i go down there
i might want to add a stop in the tour
to that as well
and here
i can go even one step further more than
just bolding it i can actually
say that the size field should link to
the shoe size list so that users not
only know it's important
how to or what
the source of that information is from
but they can actually go there directly
from the tour
in an interactive way
at the moment these are limited only to
internal business central links you can
only link to
another business central page you can't
link out to some other external
documentation
but there are some ways to do that
through a different system that we'll
come to later
um it's also important to point out who
sorry where these properties and can be
added the about title and the about text
these can be added on any page object
they can be added on any page part
and they can be added on any field
they can also be added on any action at
the root level of a page at the moment
we don't support them on
page part actions
yeah there's one other thing i want to
point out because these two things are
right next to each other
what is the difference between the tool
tip and these about properties why would
i want to use one over the other
can i just make them the same
tool tips are meant to be
what this field is
they're relevant for every field in your
application it's very likely it's very
reasonable for every field to have a
tooltip set and that's going to be what
appears only when the user manually
hovers over the caption for that field
these about titles and about text these
are going to be
describing why the user cares about that
field why is it important to them what
can they do with it and it needs to be
important enough that it meets
that it's one of those top few fields
that the user will want to go through a
short tour to get to them
so they they should not generally
be the same thing
um
yep
can i use rich text in the tooltip you
cannot use rich text in the tooltip
right now the main place it's supported
is in the about text property but who
knows what the future holds
i will say one thing about this shoe
size list since we are linking to it
from a tour we may want to
go ahead and
go
add
a quick teaching tip to that page as
well so that when users are taken there
they will also have the context of why
they were taken there otherwise
they may feel lost in that moment
so
but now that we've added that let's jump
in
back to business central and see what
that tour looks like
so we can see and the teaching tip or
sorry in the checklist and this is
actually a point where i can
point something out really quick
um
there are
multiple strings that you can define
when you are inserting the guided
experience item
you can insert a short title on the left
a longer title on the right it looks
like i may have mixed them up as well as
a description of them and a duration
all of that information is going to help
users understand uh why this checklist
is right for them uh whether the amount
of time is something they can do now or
later
and so the better information you give
the more successful this tour is going
to be for the user
and try to keep them from hitting skip
for now on everyone
so let's go ahead and just start the
tour
when we do that we're taken directly to
the page
we see the the tour down here
um
and we can go ahead and take that
as we said that's going to point to the
field on the page
now if we had had multiple tour steps on
this pointing to multiple fields the
order would be
the order that users see the fields not
the order in which the teaching tips are
defined so what that also means is if i
had an extension that had its own
teaching tip
pointed to a field in the and that was
inserted above
my field it would get there first or if
the user came in personalized and moved
fields around the teaching tips are
going to go in a logical order and not
be jumping left and right that also
means that the text you add in teaching
tips shouldn't make assumptions about
where it is on the page
um or or what order tips are going to be
revealed to users so do keep that in
mind
yeah
we can see here that if i click on the
shoe size list
i'm going to jump directly to that page
we have that
tour
tip
that was shown to us but i actually
don't want to take a tour on this right
now so i'll go back and i'm right where
i was left off the the tour is seamless
[Music]
right where it was
one additional thing is
microsoft also has some great
information we want to share with our
users
but we understand that if a developer
has put a teaching tip
in a place
they feel that's important and we defer
to that but we do also make a few system
ui elements available as optional tours
at the end
so we can point to some information like
the work date or this open a new window
um control
but when we're done with the tour
we just say got it well what if user
wants to come back and revisit the term
well there's a couple different ways to
do it the one we'll look at right now is
simply hovering over
the
an item in the
in the top corner of the page and
that'll make that appear where they can
retake it again
and as i said there's another way that
we can look at later
but i think we're done with this for now
when we leave this page and we go back
we can see that because the user
completed the tour the checklist item
intelligently auto-completes
and the user knows that they're ready
for business
this is really great i think teaching
tips are very expressive way of
introducing a page but as cody mentioned
we probably should reserve them for the
key fields that need explaining and not
just over explain every page and keep
that property
precious
but it doesn't remove the need for
having more traditional documentation as
well maybe linking to a help
page or help
microsoft docs for example we link to
them extensively as well so what kodi
are options for using a more traditional
style of
helping the user yeah all of the
traditional help that you may already be
using in your extensions are still
available
and in fact recently we've made it even
better and easier to use
so especially for apps on appsource the
entry point for all help is going to be
the context sensitive help url that you
set in your app.json file this is the
route
that's going to serve as one the
the base default help url for all of
your pages
um
uh
so if no additional context uh
contextual help is provided uh it will
go to there
but then
if we go into our
shoe card again
if we want to link to a very specific
help page just for this we have a couple
different options
one
is that
we can define a relative
link and this is going to be relative to
that value set in app.app.json
and applied to the context sensitive
help page property
and so it will just append those two
together or like if uh
if your help
service isn't set up that way that
relative links are appropriate um you
can always use
a more
absolute path i'm using the helplink
property
and that will just override that value
from app.json for this particular page
you cannot have both properties at once
the compiler will complain so it'll make
sure that that you aren't making any
mistakes there
in our case though
uh our help does work this way we'll go
ahead and use that
and now we can see what that looks like
in the product
so once we've deployed that extension if
we go
to our shoe card
there are a few different ways we can
access that help
one way sort of the the traditional way
that happened in the past was through
tooltips clicking the learn more
property in the past this would have
opened a
new tab pointing to that url
that resolved for that field
what a lot of people a lot of users and
perhaps even developers didn't know was
if you had extensions on this page
you would just have to click around and
click a bunch of learn more links until
you got the help that you wanted that's
not the way it works anymore because now
when we click learn more we actually
open the help pane and here we have a
lot of great help provided
in a great way
for users to consume and understand
so starting at the very top we can
actually see the teaching tip that we
added for this page
and we already have a way to just retake
the tour from here if users don't
discover uh that they can restart that
from somewhere in the in the header for
the page they can find it from the help
pane
and retake that tour
we can also see that right under that we
have a learn more link
pointing to the same link that would
have been there before
and what's great about this is that if
we have multiple extensions on the page
we'll also be able to get more
information
about that and these links are going to
live side by side with microsoft
documentation content as well if you're
modifying any w1 pages or
um
yeah building building on the baser
system app so
yeah thanks cody this was a really
detailed summary of how taking a very um
empty not empty but extension that has
no
guiding rails and really lifting that
experience to the next level and
hopefully adding all of these steps and
thinking through the process from setup
to introduction of the pages and the
help experience really will help
to reduce the amount of time we need to
spend on onboarding
training and hopefully support as well
when we release this to theoretically
release this to app source
well actually i also would like to maybe
build on top of this and fast forward a
little bit i think
we can fast forward and assume that our
shoe management extension is a big
success it has laid out the foundation
for view management uh in the world
and others are building on stronghold
foundation of our extension and i would
like to show how that would look like
and how
onboarding framework allows to
seamlessly integrate onboarding
experiences from
ip from different isps
kodi if you could switch to my
computer cool so i'm in visual studio
code
i start by taking a dependency on view
management extension
one thing i do as kodi also that just
taught us is i also define context
sensitive help url because my
augmentation and health will live in a
different place than shoe management
currently does
one of the main purposes of my extension
is to supplement the shoe management
page and i think one thing that it was
missing was adding some style because
style is very important so i extend a
shoe card page by adding a field or
defining shoe style
i also make sure to add all the
properties we just saw with about title
about text to introduce that new
field because i also feel that it's a
very important and will be become very
important part of this page i also
utilize
links in my teaching tip so i link to
the shoe style list page so users can
explore what
complete list of files they can pick
from and yeah and also define the
contextual sense to help page
specifically
for
this page in this case it links to pc
tech because that's our favorite
page
so i deployed the extension and let's
see how that looks in practice how the
experience changes
uh of course refresh
and jump to my environment
to management extension is already
installed shoe style extension has also
been published
well actually i see that
i just noticed i'm in the wrong
environment as onboarding one it should
be onboarding 3.
that's something new we also added in
this release the
quick plug
we also have now environment uh and
company picker that allows to very
quickly change environments without
losing context i can decide to jump to a
new tab with my new settings or i can
change in place and just switch
environment and company one click really
nice
okay so let's go back to onboarding uh
let's go to
cart
and i have taken this tour one more time
and now i can see that
the size is highlighted as cody showed
but now also we see issue style field
also being called out in the tour so
onboarding framework make sure that
same
we made
the design choice that order of the
fields not matter and it's a very
important design consideration that you
have to take into account because anyone
can extend your page and this is what is
happening here but since there's no
assumptions it just feels one naturally
seamless flow i also have a link to my
shoe style
stylus page uh
got it now i saw what's new on this page
and i should be able to
effortlessly
at the same time if i open help paint
that kodi also just showed
we also see that about apps on this page
now we see two two apps
so there is first app that is the owner
of this page and there is also
styles that i contribute
i don't know cody could you explain a
bit more how that works behind the
scenes
yeah so for every
uh every app that modifies the page
we're able to show all of that help like
i mentioned before
previously let's say you added two
separate fields to a page and they were
added to a couple different groups
spread around the page users would only
find that help if they knew
that one field on the page was added by
a different app than
some other field and that's just not
something that users should need to care
about so now no matter how many fields
you add on a page there's just going to
be one
link for you in the help pane
that users can easily use to find
also with a little bit of information
about what publisher and what extension
it is it'll let them know
whether that is the help link that's
going to help answer the questions they
have
perfect this is really seamless
so let's jump to a recap i think we just
built one shoe management extension it
has now a really nice seamless
onboarding flow we built on top of it
still this the flow really makes sense
and users will be happy to
be introduced to it
so recapping
onboarding framework helps to turn uh
customer onboarding into repeatable
process
uh it's a smart idea to start thinking
about onboarding early maybe even before
writing a line of ale code to really
think through the experience and
supporting
processes and steps
consultants will need to do and consider
translating that to code
also you have a broad set of tools in
the onboarding framework to make that a
reality you can build and assemble a
checklist you can use assisted setup
you can add teaching tips to pages
and of course the page synopsis which is
the main teaching tip for the page and
also you can bring your help content to
alpane
and if you want to learn a bit more and
just go at your own pace we also have a
really short link akms pc onboarding
that details the story and
can follow along yeah
thank you all that was it
we
yeah
we actually carved out a little bit of
time so we'll take questions first for
our session and then we can take
questions as well for the session before
and we have two t-shirts so best
questions gets t-shirts
okay one t-shirt for you and then one
t-shirt for our session who has a
question
if there's none no no t-shirts just ask
something and you'll get the t-shirt
we have eight minutes
um
is there any way to like uh
have a rule for this
like when you should add an
about text or something maybe for a
promoted action or something that we
should add a
vortex or is there any guideline to it
yep so if you go to that uh aka ms bc
onboarding um
there's a bit more guidance from our ux
team that guides how we've chosen uh to
use them within
our microsoft application
in general you want to use them if
there's something that's novel and
important
specifically for making use of that page
it's not something that necessarily
every page needs we don't add it to
every page
but there's a bit more of that textual
guidance but if you think it's very
important
consider adding it but probably don't
add it to every page
and i think we outline it on there but
the the rule of thumb that we go for
is really no more than three
uh
three fields or actions added to the
page um anything more than three to five
uh users start to get very fatigued by
going through all of the steps
and they're much more likely to to exit
them
great question
let's wait for one question and
otherwise you'll get the t-shirt
come on
he was the first one so he gets the
t-shirt okay
decided he broke the silence okay there
we go
hi oh i actually had a question to to
just uh for the previous session
um
is there any
so my understand that this contribution
to the base app would be
only to the latest version the cloud
version
do you guys consider
add sort of a flow where people can
contribute to the previous one which
would be on premise that's definitely
not part of this pilot no so it has its
own
set of challenges to backward features
because you might take dependencies on
things that we don't have available in
earlier versions
um
i mean if if there is a high demand for
it i'm i'm open to
these ideas but i think to start with
with it will be the latest released
version okay so currently it would be
the 20x version that that you will be
working on here but it's just a little
bit of con
connection to this question
but i mean as as the pr goes would it
potentially be possible that you guys
will move this to a
to a lower fix i mean if you make a
request and say like you know hey let's
just say it's an extensibility request
and you really really need that let's
say in version 19. yeah yeah you know
we can talk okay
absolutely i mean it of course it
depends on the complexity if this is
going to be overly complex then i mean
this just won't scale but if it's
something simple you absolutely we can
talk about that yes cool always happy to
help thanks there's someone right behind
you with a question
thank you
so
i have again a question to jasper and to
to your
conversation and the question is
like regarding the alap extensions in
case we request a new event or like
event
extensibility etc we receive an answer
like quite fast that's great but the
question is about the feature requests
and extensibility enhancement do you
have some
like
rules for that and in case customer
needs something for how long time should
we wait to get a response from you for
that
so you mean the issues now and not
pulling requests the issues like not
about the new uh repo if it's event
request yeah i mean we try to process
them as quickly as we can
the inflow varies a lot right so
sometimes we get you know hundreds
within days and sometimes we only get a
few
so we don't really have any sla like
there's no guaranteed time to fix
we have seen a few examples of
extensibility enhancement requests which
were rather complex actually to
implement and as we need to implement
them that's our time so then
you know those take a little longer to
do some of them even took half a year or
a year i've seen
normally with event requests we try to
turn them around rather quickly so if
it's if it's a simple event and it's an
event that is sound it makes sense to
have it at that spot you can expect that
it's in the product within
a month or two
and regarding the feature requests like
the same approach just if it's a feature
request then then we need to see when it
fits into our backlog again this i mean
some of these feature requests are
actually rather large
we try to process as many of these ideas
as we can
um but since we need to do it we're kind
of the bottleneck here but that's what
we're trying to address with the open
source story right so if it's really
something that you need now you will
have a way to do it yourself and that's
going to put you on the fast track so
there we can make sure you know that
things get turned around really quickly
so i would highly encourage you to you
know for going forward do these things
yourself uh and then you will have them
much much faster than you have okay
that's understandable and the last
question for that part like previously
we have a nav where we have a
possibility to change everything in a
standard court for now we have a
business central where we can only
possibility to subscribe to something
but also we have like some pages we can
which we can see inside the visual
studio code like just sales header for
example but other pages are securely
hide like with internal uh like internal
property let's say and it's impossible
to see it directly but it's still
possible to find a github it's like in
case we issued with some we we see some
issues which is not working in case we
just copied that for our extension and
use it as not an internal is it a
workaround to it or like should we avoid
that you should avoid that yes
absolutely by all means that was a
question to receive an answer and to
give it to my customer
thank you
you can absolutely refer to me for that
thank you
um
with the contribution previously that
was
where uh you had problems where you need
to re-number all the up if to make
changes to some of the modules you need
to renumber and into the pte range and
there was something with the license is
that something that you
are addressing you marine yes we're
looking into that so so i've
continuously worked on the kronos
license to turn it actually into a
developer license that has open ranges
the only limitation you can say on the
chronos demo license these days is that
you can only you know post in
january through march so that kind of
makes it unusable for production other
than that the chronos license should be
a full developer license that you can
use okay we're going to start using id
ninja if you've heard of that one from
yego
and we're using that so that you know
that you can find the next available id
and then we're not stepping on each
other's toast with these ids so that's
going to get rolled out as well
so then we hope that that this is gonna
gonna fly nicely excellent thanks
anyone
no that was it okay yeah one more maybe
one more
yes so i heard some information that
you guys have very extensive
um
a lot of testing
coming on on a base app yes so
there was some information that there is
like more than
10 hours of machine
learning we're running a lot of tools to
run the
the base app test
so would this be part of
this open source
thing so if i will fork it and i for
example doing my commits to my branch
i would need to run the same big builds
usually you don't need to run run the
entire suite uh but when you do the when
you check in the pull request we're
gonna run the ci process and that ci
process is gonna run the entire suite
we can be a little bit intelligent about
like which tests we need to execute on
so we don't always run the full thing if
we see an area hasn't turned we don't
really run these tests so we can be
smart about that
um but you're not going to get through
unless our test suite passes and that's
it
when i'm doing my commit
this is on my repo it's on my own course
if you do it on yourself then yourself
you need to run your test yourself but
of course the entire test suite is
available i mean and you of course
encourage first to make a local run to
see if your tests pass
or maybe we can have an extra session on
that you know
it would be interesting to actually see
it and then good suggestion i'll take
that with me
all right time is up thank you very much
thank you
