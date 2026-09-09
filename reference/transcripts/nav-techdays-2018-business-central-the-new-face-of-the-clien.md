# NAV TechDays 2018 - Business Central: The new face of the client

- **Source:** https://www.youtube.com/watch?v=9Vh1b6h-iNc
- **Video ID:** 9Vh1b6h-iNc
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 93m12s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

welcome to business central the new face
of the client session we have prepared a
lot of great content for you today and
we happy to see you here before we start
we would like to introduce ourselves
quickly I'm Thomas Group Laos cos I'm
engineering lead at business central
team responsible for desktop and mobile
clients and my name is Andrea Tina the
client team with Thomas yeah Andrea
let's do our tradition of Navtech days
and start giving first t-shirt today to
a person who can answer a personal
question about you does anyone know how
many times andrea has already presented
at nap tech days I'll give you a hint
it's less than 8 times a bit more we say
fall for ya yeah that's correct
thank you yeah andrea is quite seasoned
present already a snap take this while
we answering questions and giving away
t-shirts I would like to ask one more
question do you remember what was the
last thing we introduced last year in
client session what was the big new
thing it also wasn't a keynote this year
hint I was on stage doing that there was
some pink involved I'm close but it's
related to the UI I think you noticed
the change it's called modern modern UI
someone said it cool thank you so that
was the last big thing we introduced
last year and in spirit of continuing
from where we left we'd like to start
this year session with modern look and
feel we would like to introduce new
components new UI patterns and also give
a bit of backstory and decisions which
went into making this UI next we'll talk
about productivity
we are continuously investing in
productivity we will talk about some
great new components and productivity
features like advanced filtering and you
can bet that we working on many more
productivity features for spring then we
will talk about one business central lab
which now connects to on-prem and cloud
channels lastly we will wrap up with Q&A
and answer your questions so new look
and feel when users are using products
and in cloud they have different
expectations they expect the product to
continuously evolve improve and adopt
latest technical and design patterns
when we introduced business central
brand which unified on-premises and
cloud offering we wanted the users to
associate these qualities business
central and creating the new modern
refreshing the modern the UI was one of
the key cornerstones to achieve that
mission to do it from from the get-go we
set some key goals for the modern UI
first of all we wanted to align UI with
other Microsoft productivity and
business products then we wanted to
reuse as much as possible existing
application concepts and not necessarily
introduce new ones so users can adopt
new UI with little or no partner work we
also wanted to architect the components
in a way that they are ready for the
future so we can increment them and
improving incrementally and we designed
all the components from the ground up to
be accessible product productivity in
mind and also scalable to achieve these
goals the design and engineering teams
worked in a tight collaboration in
interative development setup we were
coming up with different concepts ideas
prototypes doing user testing and
repeating this until we would reach a
result which met all of our goals and
you can imagine it's not always easy to
say goodbye to a prototype which didn't
work it's very hard to discard something
you loved initially but we recognize
that that is the way to improve the user
experience and push it forward to the
experience which users are delighted
with so Andrea is gonna dive a little
bit deeper into different building
blocks which constitutes the modern UI
and explaining more in detail our
reasoning behind every single component
here you go Andrea perfect thank you so
much so let's get it started
this year many things happen and we
released a lot we actually went through
two different releases we have the
spring release this year and also the
fall release and we have introduced a
lot of new things as you probably
noticed a few of these things you've
already seen during the keynote
yesterday and arena went through them
you will see again some of these today
but the idea is that we will go through
them a little bit more in details and we
start from the this spring release they
will move to the fall release and in the
spring release we decided to put a lot
of effort in restyling and refreshing
our all centers I mean role centers are
the first page we hit when we get in
business central that's what we would
call home that's why we wanted to put a
lot of effort in restoring them and a
lot of the new features did light up
just in role centers in the spring
release so let's go through the mostly
the major ones of them and we start with
the navigation so as Irena mentioned
yesterday during the keynote we have a
new navigation paradigm we got rid of
the side navigation and we aligned to
new and modern interfaces for web
applications today and put it on top it
means that now we save space with free
up space for what it is more important
which is your content in the page and we
just occupy a little tiny bit of the top
space or our pages and that's where
navigation bars today are expected to be
by users
in the internet when in the in the cloud
world and all your areas are just going
to be there next we have our action bar
so as you probably noticed there is no
more ribbon and harina was pretty clear
on that we got rid of that and not
getting me wrong it's not like I had a
ribbon it's not like we did a head
ribbon it was a nice control but it
wasn't perfect it had a very nice goal
in mind which was bringing all the
actions one click away from you and it
did succeed in these in this objective
the problem is that as downside the
reborn got very crowded with different
control different items and especially
for beginning for beginners for users
that did use the properly first time for
them it was quite hard to find the way
around in a sea of cement controls and
was not so easy to spot the actions they
wanted to use so that's why we decided
we recognize that all fees recognize
that we pulled along and we decided to
okay let's stop for a different paradigm
and that's where the action bar comes in
place in the Rose Center it takes the
form of a list of items which is pretty
flexible and in here you see there when
it is rendered next to another control
it actually used uses a wrap layout but
we will see that if there is no other
act artifacts rendered next to it it
will actually take the whole space so
it's very flexible control and all
familiar concepts like grouping are
still there there is a little bit of
effort on your side because now the
constants are a bit different so if you
want your actions to light up into these
new controls you need to rework the
grouping and rework the promotion policy
that you have so there is this little
work to do we went through that and you
will have to go through that but it's
really worth it next we have our keys so
if you say you're all Center the first
thing I think about is queues because
they are so prominent eye catching they
are engineered to to basically display
in a little tiny area
very complex information and data and we
recognize they're very important so we
refresh them we actually give you the
ability to render them in two different
modes we have are normally out and we
have wide layout a wide layout is fit
for for data that requires more than one
in two digits so when you have certain
values that for example decimal values
that does need more space we know that
so let's let's use more space and that's
where the wide layout comes in place and
of course all the familiar constable
cues are still there it's possible to
define actions on them and it's possible
we still have sentiments just a bit of
different colors and a better styling
and now refreshed last but not least a
new headline control this is a brand new
control rename being said showed you
yesterday how powerful can be let me go
through that a little bit more so the
headline control is part of these new
experience we want to bring in business
central the all idea is that we won't be
the central to look like a newspaper
every morning you read the newspaper
about your business and you want to see
big headlines when it comes to breaking
news of something important in use know
about your business and those are what
headlines are for so as developers you
can code these ad lines and you can in a
Carville display messages to the user
and you can make them actionable as well
so prominent actionable and a brand new
experience and very even though the the
control is very powerful it is very easy
to to actually develop that but let's
see all these things in action so let me
switch to my demo so okay let's just
refresh it
so role centers here we go
so as I already told you the navigation
bar is here on top so when designing the
navigation bar we had exploration as
design objective so you can the the new
idea of this navigation paradigm is now
that the user can explore the different
sections of your application without
navigating into them directly so these
are important because the user can keep
the context while still exploring the
different areas of your product and is
it very effective it has proved to be a
very good pattern and that's what we
wanted to bring in business central
nothing nothing to do on your side here
it just comes for free no new metadata
it will just light up the action bar as
I told you here it is rendering a little
rap table layout you will see later that
if the headline control is not there it
will take the whole space so very
flexible as well you can see here that
different icons are used and for reports
for for other actions new actions the
way you control these is by placing
these actions in the proper groups
so go ahead the documentation is very
clear on that and you can do that little
work which is required to to have your
actions properly rendered on screen in
this new control cues here they are
usual concepts sentiments are there as I
told you they're actionable and they
bring the usual experience refreshed and
then the headline control so I told you
that as you can see the headline control
can display in a carousel different
messages and you can define actions on
them the headline control is reloaded
every time you load the page and you can
it's dynamic you code it and it can
bring up a lot of insights about your
about the business inside your
application and I told you it is very
powerful
but it's actually very very easy to to
code and develop andreia can we prove
that yep okay let's do that and let's
switch to my demo environment here this
my development environment so excited
this is the first time I do an Al
session I used to go see al now it's al
so let's try this thing we're going to
create a page extension and modify our
role center in at an intelligence
provision and I'm going to create my own
headline control with my own headlines
and I'm going to replace that in the
business center business manager role
Center so let's start this yesterday you
saw with Vincent how to quickly create
an al project Alt alt a old al you
create a new project you provision
alternate and that's it so I've done
this thing already so here it is I'm
connected to my turn already and I have
BS code ready for development so the
first thing I want to do is I want to
modify the role that the business
manager or Center so I want to start
from the page who remembers the page
number of the business measure of center
again no four digits starts with a nine
again again 19:22 yep where are you sir
it was in the ballpark let's on two
three and perfectly so let's move on yet
90 twenty two so that's the page that I
want and yeah that's the role Center
saved so now let's start creating a few
files so actually I don't need many fast
just here so the first file I'm going to
create ease I'm going to call in my
headline
actually my head extension dot al and
this is going to host my extension my
pet extension but before doing that I
want to create the page part so as you
know if you want to create a new
headline control you need to create a
headline part that you're going to use
inside a page so this one is going to be
that part so let's call it my head part
yeah and let's start from here let's
stop coding the headline control now the
thing is that it's easy to code it you
define the the page you give it the
layout but the point is that we don't
really do these things as programmers
it's just nice to start from snippet and
it's pretty standard way of doing things
so what I want to do is show you how
quick it is to just get to our
documentation and find the documentation
for that like control and just that
snippet that's the only thing we need to
start from so let's go business central
headline control and that's here and we
are given the basic structure of a
headline control just right
documentation page I'm just gonna use
that why not and here it is
I'm just going to give you a different
number because I want to use 50 100 for
the page extension and I'm just going to
rename in my head and that's it these
are the four different messages that we
want to display and we can just modify
them
rocks that's it that's my headline
that's done so let's go back to the page
extension and let's start that so that's
just declare a page extension and let's
just use a number as I told you 15 100
speedy pretty neat and we can call it my
extension and after that we can just
tell it to extend an existing page so as
you can see intelligence in visual
studio code already gives me some hints
so I can pinpoint the page that
remembering numbers or anything like
that so here I am I'm coding my page
extension let's create a new layout
section because that's what I want to do
I want to modify the layout and what we
want to do what I want to do is I want
to replace the existing headline control
it means that I'm going to hide the
existing one and I'm going to add the
one that I just created so it means that
I'm going to modify something so I don't
know which control it is I should look
at the at the page structure and
everything but you see mr. code is just
very very nice and gives me the caption
so you see here control 139 gives me the
caption is the headline headline RC
business control so I'm just going to
use that that's the control I want to
use and as I said I'm going to set
visibility to false cool so far so good
now I've hidden the control and I can
add the one that I just created after
always after the same one and I want to
add a part of course so let's give it a
name and then I'm going to point to my
head the one I just created and let me
just
caption and that's it that's done seems
like there are no errors control 5 that
gets published and we will see it
lighting up in my browser in a few
seconds so it will connect to my tenant
that I've really provision and open that
for me and it should go straight to the
to the Rose Center and my new headline
should just be there no it's not
y-yes wow that was quick and he I
thought it was some kind of advanced
question who got it yeah yes precisely
so the application area so application
area needs to be said in order for the
control to be laid out so and here it is
application area oh and we need to do
these not just for the for the part but
also for each single one of these
controls in the headline control that I
just created control save and my syntax
is now neat and perfect control 5 you
know the drill is going to publish it
and it's going to open another another
in another top business central and now
I should see my headline control and
there it is Microsoft business central
box so as easy as that Thomas that's
cool is it enough I think you proved the
point ok cool
moving on yeah spring release done check
full release so let's talk about that
because in the full release what we
decided to do is of course to roll out
the rest of code name Madonna to the
other pages that we have so and in the
concept of that effort we have
introduced a bunch of new controls let's
go through them
patience parlay out I have a question
for you how many of you have messy desks
oh come on you're lying okay bring up
those hands so my father used to
complain a lot when I was living with
with my father my mother and about my
past it was very messy but let's face it
that's not Mass that's our own
definition of order and we have that and
our customers do as well their guys have
just pile of sales invoices as ordered
quotes and that's what we wanted to
bring him business central the good
parts of it so this experience can be
seen in the new stacked layout which
provides to the user visually the
context both the navigation context but
also the the flow he has been through up
to that point the operation the process
they has done so far so it's it brings
up the context and it is very important
the other thing we want to light up
Arena mentioned that we have a back
button but that's that's a tiny
improvement but it's so important
because it brings up a very consistent
experience across all pages that is very
good for for first users the other thing
is of course the action bar the action
bar is the new home for our actions
you've seen that in the Ross Center in
our in our pages though it looks
different of course
no more ribbon even in card augments
work sheets we have the action bar there
as well and the new paradigm now is used
for displaying your actions again there
is a little bit of effort there because
you need to rework the grouping of your
actions in order for them to be properly
displayed and available to your users
but apart from that then the new control
is just going to work in your
applications and take the best of it do
these little bit of grouping it's really
worth it
action bar also four-page parts so if
you remember previously the actions for
page parts used to be placed in the
ribbon in a special contextual tab it
was really fueled for our customers and
users to relate that those actions were
referring to that page part and we
understood that especially for beginners
it was really difficult to relate to get
these association so we decided to to
work on that so got rid of the ribbon
and we have the action bar but instead
of placing the contextual actions inside
the action bar we decided to create a
contextual action bar for parts which is
closer to the part which is so it's more
relatable and it's much easier to
associate these actions to the part and
also they are not polluting the page
action bar it means there is more space
for for other actions and that is very
important a new header we have worked on
restyling the titles in the subtitle and
we have created a special place for crud
system actions the Edit toggle is there
the new action is there the delete
action is there it's also much easier to
identify the page view mode so you can
easily understand if you're in edit mode
of view mode thanks to the toggle just
there in a prominent area before this
action were in there in the ribbon in
the Home tab not so prominent but and
again these are out of the action bar it
means they're not polluting via your
action so there is more space for your
actions navigation actions those are
always in the spirit of not polluting
the action bar with platform stuff we
have extracted those that were
previously placed in the ribbon in kind
of obscure area well and now they're
placed in the middle of the page in a
familiar place and in a place where
they're expected to be and we have
decided to bring up this nice browsing
experience like as a newspaper you saw
the animation yesterday with arena and
that's just what user expects us to do
where they expect those actions to be
there that's just platform doing that
there is no effort on your side no new
metadata nothing like that
and we have the ability of setting a
wide layout for our pages now in this
period of having this paper layout in
our pages of course the our pages now
take less space but as users you might
want to use the full size of your screen
because just you want it for whatever
other reason so that's why we give you
the ability to expand the page and take
advantage of the whole screen size you
have no matter how big your screen is
and last but not least we have decided
to restyle our controls they look more
modern they look refreshed our edit
actions assist added lookup date picker
boolean new boolean controls and so on
all new and refreshed we have increased
the spacing between them so it's easier
to the whole page is more readable
basically and we added that just a
little tiny feature which is so
effective connecting dots that help the
user figure out which filled the the
caps were first following along it's a
good UI pattern actually and well with
that let's see all these things in
action so let's go back to my tenant and
well let's open a customer here it is
and let's just create a new sales
invoice you see the stacked layout is
giving me the context I know that the
page before was the customer page I'm
creating the sales invoice for so I can
quickly click on the on the gray area
and go back to to that page so this is
another paradigm to go back I can also
use a scape just by using the keyboard
and that's also it's also as you can see
a navigation pattern and let's just
create an our document says order this
time and the back button helps me if I
am a new user and I don't know that by
clicking on the gray area I can be
brought back I can always use the back
button and there I am it seems a small
thing but it is so important for new
users they so they will never get lost
in our pages and next we have our action
bar so as I told you the now our action
will reside in these new control
basically it takes so little space
compared to the ribbon it means more
space for content you might argue okay
Andrea that's cool but now all my
actions are one more click away compared
to the ribbon it's not entirely true
because the first time there might be
but remember that you have the option to
ping the pain so that next time your
action are going to be there just one
click away for real and you can of
course on pin it and hide it so very
flexible the the same goes for
contextual the contextual action bar so
fact rate and you say is invoice you
will see that now lines my page per
lines also features a page action and
same exact things it's the same control
matches are in there need to rework a
little bit on the grouping in order to
make my actions appear where I want them
to appear as I said refreshed refreshed
ILO's and my toggle is now here in a
prominent position telling me precisely
which mode I am in also the let's talk
about the the page layout as you can see
our pages now look thinner inspired by
the paper layout but if I want I can
expand them and you saw that before
this is especially true when you're suc
boxes boxes occupy the side area
and it means there is less space in
total that's why we automatically enter
wide layout when you open a fact box and
familiar concepts are still there we
memorize the the state so next time you
open an arrow says invoice the fact box
is going to be in the same set as it was
before if you left it open it's gonna be
open if you love that close it's gonna
be closed and let me go back and as I
told you our new navigation actions are
there so the browsing experience across
record is is much nicer than before and
those controls are much more
discoverable and the new controls now
are in place refreshed as well and all
of them are being designed with
accessibility in mind so just by using
the keyboard you can navigate across
them and keyboard only you can just feel
values in your page in a very familiar
way and that's that's it for me Thomas
yeah really good demos especially liked
the one with modern dev experience I
think it reminds me so much of the
front-end development and experience if
it's like just playing development to me
you know you have a browser on one side
you have your ID on other side
you change the curve it's a it hot
reloads you see the changes in your
browser so it's very effective I love it
it's really amazing it can have that for
application developers in business
central so let's talk about productivity
productivity is another key area where
we continuously invest we understand how
important productivity it is for our
users you want them to and to enable
users to complete their tasks faster we
also want to reduce the barrier of
switching to cloud and finally we want
to reimagine the productivity for the
web so it's not only about
features which we had previously and
just copying them it's thinking more
broadly what makes sense on a web and
reimagine those experiences and creating
an awesome productive web client and one
of those features is tell me tell me
what you want to do is such a natural
question to ask and tell me is evolution
of what we previously called page search
page search was okay if you exactly knew
what you're looking for which is kind of
contradicting to action of looking for
something but we looked around and we
try to find similar problems other
products are trying to solve with having
a lot of complexity and all the actions
in a product and balancing that with
discoverability for the end user and we
fell in love with how office solved it
and they solve it exactly the same tell
me and we wanted to bring that to
business central so tell me is in
exactly the same place as page search
was but now it's more powerful and it's
more contextual so tell me a dialogue
when you search for something it first
shows the actions from the root page you
are on so if you're on sales order it's
gonna show actions matching your search
term on sales order then after that we
have grouping of different search
results based on the category usage
category and next we show page and tasks
and user always has an option to expand
and see more detailed view but we first
show a couple of results which matches
the search query the best next we have
okay the clicker is still working
let's go quickly so next and we have
reports and finally we have the
commendation that's something another
completely new thing so when you search
if you are using cloud product we also
surface documentation results from
Microsoft Business Central online
document dogs and currently it's limited
only for cloud solution and we only
surface our documentation but we're
investigating different sources of the
information which we could be including
here and we see a lot of potential there
also for our partners so next let's see
how it works in action
so you see you saw a bit of that in in
the keynote because it is truly our new
favorite keyboard shortcut and that is
alt q' so when you hit all cue tell me
appears and it asks what you want to do
well in this case I would actually want
to know what are the limitations of tell
me how do you find that well you ask
tell me tell me about tell me and in
documentation actually we get first
matches frequently asked questions about
tell me okay let's see
and our all actions from my current page
is horrible and tell me
well no it's only from the root page so
actions from sub pages will not surface
at least at this stage so that was cool
we just learned something let's try some
different scenario let's say I want to
create a customer quote so first I will
search for customer and I want a
customer list and by the way I'm just
using my keyboard I'm trying to do and
this entire scenario of just using
keyboard shortcuts no mouse no touchpad
so focus is still in in customers so now
I can pick my customer and I will pick
Alpine sky ski house and I could I could
open the customer but I kind of already
selected the customer so let's hit all q
again and then press
you so actually first action is matching
this cue the sales quote so only thing I
need to do is hit enter again because we
by default will activate the first
result if you hit enter so hit enter and
it creates a sales quote still haven't
used mass in any way using just tell me
combination of shortcuts and yeah it's
all very productive user experience and
that is what we're trying to achieve
here so next let's talk about some dev
tips like what does it mean for it for
you
so first search for actions it just
works you don't have to do anything to
activate that but you need to set more
informative captions on page pages and
reports because we use the caption to do
actual matching of the search terms so
the more informative captions you set
the better the search will be next yo
you need to opt-in to tell me four pages
and reports by setting usage category
property and the property you pick
actually will decide where the page of
report goes you saw those two categories
with pages and tasks and reports yeah
and lastly documentation only includes
online help dogs currently and it does
and we will not surface anything on Prem
so I'm Prem that feature is not
activated it only works on cloud so we
saw global well tell me is in a way a
global search with a touch of contextual
awareness then we you always also are
familiar with list my cross column
search in lists which is local search
but what does user do when he tried all
of those options and he can no longer
come up with a better search term he
uses filtering and filtering was
something we didn't have in web client
and we wanted to change that we looked
around and we did again
just reiterating that we always trying
to not just copy what we have would
actually reimagine it for the web and
make it better so we looked at a lot of
websites and users already are kind of
familiar with filtering if they ever
booked a flight or a hotel and usually
you find it in a website if you do the
search you see your flights and then you
do filtering on certain categories and
that usually the filter pane is on the
left side of the page and we wanted to
keep that pattern so no matter if it's a
experienced user of it's an user
business central feels just familiar and
when when that pane opens in a in the
list page you just immediately know what
it does it's filtering so we wanted to
make it better and let's break it down
what the filtering pane does first of
all you can select any number of columns
and enter your filtering expressions and
we support all previously supported
filtering expressions like data
expressions application defined tokens
ranges and so on logical operators all
of that so there next we also
reintroduced flow filters so column
filters you can map you could think that
they are for reducing the amount of
results you get and floor filters are
reducing the amount of data used for the
computed values in those records and
lastly we one of the things we were we
pushed the web experience further we
introduced a stateful modifications of
filters so you can actually work on your
filters you can close the pane navigate
away navigate back with the same
navigation action and your filter
filters are still gonna be there as long
as your session lives when the session
expires they'll be discarded for now we
don't have the saved views so you could
modify a view and save it as a different
for you but that's something we are
looking in
in your future and also filter pane now
accommodates all the views so they are
next to the filters so everything is
contextual when you modify filter on the
view the view name actually becomes
italic to indicate that this is like a
dirty and eventually you'll be able to
save it so let's see how it works so
I'll go to items and again I will try to
prove our commitment to productivity by
using all the new shortcuts and all the
new goodies we introduced in spring and
fall so have an items list and I'm
actually just interested in chairs so
I'll hit f3 and immediately the search
field is focused so I'll type in chair
and this is the first level of like
reducing the data set it's just using
free text search cross column search so
now I get all the all the items matching
a keyword chair but I see that and by
the way the focus is still in search and
I want to do something with the grid so
I'll hit f3 again and I'm back in the
grid without clicking I'm just back in
in a grid and I continue my flow so I
see a lot of items have quantity on hand
zero and that's not very useful I don't
want to I don't want to have those so
what I will do I will hit alt shift f3
and what the scheme keyboard shortcut
does it creates a filter line with
column I was on in a grid with no value
you can also filter it to this value and
it's additive so you can keep filtering
on different values and it will be
prefilled but this time I just want to
enter greater than zero and it will be
activated when I leave the field so how
do I jump back into grid I hit ctrl
enter and I'm back at exactly same
column I was before so I did all of this
data selection actions
and I was able to do that all of it just
by using keyboard shortcuts so next it's
kind of looks okay we filtered the
uninteresting items now let's do
something so these items are from all
locations but I am actually interested
in items which have quantities in
certain locations so I'll use another
keyboard shortcut which is control shift
f3 and I'm actually focused at the flow
filters and this is another area where
we push the experience further so now
when you select an in column we're
actually giving you searches to type
experience in the field of a type
location it automatically auto fills the
the name and I can say East or main and
again I can hit control enter and go
back to a grid and what happens happened
first of all I searched for all the
items which match the chair then I
removed all the items which have no
quantity on hand and I'm going to change
the flow filter to change the quantity
to only take into account these items
from locations in East and main and
since some of them didn't have any the
gods also filtered out because of the
first filter and I did all of this just
by using keyboard so I was working on a
grid and next let's see if I want to
know more about filter and filters and
expressions I'll just use tell me again
and we have awesome documentation
explaining you all the things you can do
the filtering it's basically a
reiteration of all that was not the
result but
yes so you can find all the
documentation of different expressions
for search expressions we support the
same goes for filtering ranges and it's
just great documentation material it
takes a bit of I can't imagine it takes
a bit of time to learn this secret
language of filtering but it's really
powerful and now it's available in back
find next I want to show one more thing
with with range with expressions so if I
go to sales orders and I can expand
filter pane also by using an action in
on a page and I want to filter sales
orders based on actually let's give us a
bit more space so that's a good point
yes we need to add that shortcut I will
I remember this so I was actually is
that I wanted to find something with
dates it's due due date and I want
everything greater than today - seven
months and when I once I leave the field
the expression will be evaluated and it
computes the date so all the richness of
filtering and expressions application
divided tokens is still supported copy
next copy and paste I imagine everyone
is thinking of course that she just
worked right but it's not always the
store is not always that simple copying
text values it is pretty straightforward
and we can do it but we want to again
push the experience further on the web
and we want contextual copy and pasting
so now you can do copy and paste of rows
in same list
you can do copy and paste to similar
lists as long as column order count and
type smashes you can also do copy and
pasting from other productivity
offerings like Excel Outlook and the
same restrictions apply of column order
types account and you can do it other
way around copying data from business
central into other productivity product
and you also as you saw in keynote you
get a bit of more formatting so it's not
just dumping the tabular data in Outlook
we actually formatted for using HTML so
it looks nicer it matches the business
central teaming and now I'd like to show
you one of the awesome scenarios which
we enabled so when i when i sholde
should tell me i partially completed the
sales quote scenario i didn't really
fill in the lines right so let's
complete that let's do it again just
using keyboard this time
so now we have a crowd but we don't have
any lines and let's imagine that our
sales agent already sent is an item
catalog to a customer and he since he's
not very tech savvy he just used Excel
just used Excel to write down what
customer wants and they agreed on some
special prices based on how many items
they are ordering so I have just tabular
data in Excel it happens to match the
number of columns the types and the
ordering so I'm gonna just hit ctrl C
I'll copy it I'll come back to business
central I will tab tab tab into a grid
to our first empty column I will say it
ctrl V and all the lines are filled in
I'm done now I hit and last thing to do
ask tell me how to release it and then I
can and out by the way also the old when
I pasted all the values were computed so
the amounts matches and everything is
correct so now we only need to call tell
me again and do release and that's it
I'm done and again I could have
completed this scenario just using my
keyboard I didn't need to enter all of
these lines manually you can figure out
productivity patterns which works for
you and we trying to constantly improve
them and just connect things together so
everything works image seamlessly let's
go back to the demo so keyboard
shortcuts this this release all these
two releases in spring and fall in total
we introduced 11 new shortcuts I think
in total now we have over 40 shortcuts
and again it seems feels like yeah let's
just copy all the work
which we already had in previous clients
and bring that to the web but again
story is not as simple as that we're
trying to look at what kind of patterns
users are expecting the web what they
are used to what they are used to from
other apps web sites what they are used
to from different products and what they
know already from Windows client so
taking all of this information and we're
trying to come up with coherent story
which makes sense for the web and still
pushes the productivity experience
further and we don't really expect that
everyone will just learn the new
shortcuts especially the ones which
don't necessarily match Windows client
so we prepared great documentation
listing all the shortcuts explaining
what they do and we also have a
printable cheat sheet which you can put
on your desk and you can also I know
quiz your colleague until he remembers
all of them that could be a game yeah
okay I'll just give a second if you're
taking pictures but I will share the
slides later accessibility accessibility
is one of those things which Microsoft
feels very strongly about Marcus will
have has a commitment to not ship any
new software which is not accessible
because we want to be inclusive to the
workforce to the broad workforce and
enable everyone to work with our product
doesn't matter with you using keyboard
or using assistive technologies we want
and the big thing is that business
central is now accessible and what does
that mean that means that any partner
building a solution on business central
is by default on a desktop accessible so
we are delivering on Microsoft while
commitment to accessibility and
inclusive workforce we also committed to
maintain this rating and push it forward
and we also do the same on mobile next
and investing in accessibility
contributes to the broad experience of
productive
as I said when you enable your product
to work really well with keyboard you
enable at the same time all kinds of
productivity features which you didn't
imagine first and when we build new
components for modern UI everything was
built from ground up to be accessible
and that will be our commitment in the
future so one last thing is one app one
application is a change with it when you
introduce business central branding in
spring where we aligned cloud and
on-premise brands and we wanted this to
be reflected in our mobile applications
too
so previously we had two mobile
applications we had Dynamics NAV and we
had financials so we were really branded
financials to be business central and
enabled it to connect to cloud and
on-premise tenants so now there's only
one app before branding and you don't
have this duality anymore we still have
the dynamics nav app it will be on the
store if you need to connect to Dynamics
NAV tenants 2018 and previous if you use
business central you just use business
central lab I need to connects to both
and something one of our PMS forced me
to say because you love iPhone X we also
support iPhone X but for me it's we are
building a cloud product and people just
expect us that we will be constantly up
taking the new things so yeah we have
iPhone neck support and now I would like
to invite to the stage
Yevgeniy who is one of engineering
managers from our internal teams who
will tell more about building a customer
grave product using business central
platform for office users is great demos
do you like what you seen so far yes you
did we all this amazing stuff
all right so my team always telling me
Evgeny if you cannot make memorable
presentation at least try to make it
short so this will be the goal for now
one year ago Microsoft released a new
product as a part of office 365 which is
called Microsoft invoicing in those days
is was proudly built based on a project
in the reef oh that's how we call our
services back then and the product
evolved over the year and as they're
going to release a new version within
upcoming weeks we decided to take a
radical change as organization and move
from office 65 look and feel to business
and trial modern user experience and by
the way now you know how the medina came
in from but then I came from a modern
division so we just call it modern for
now and the challenge for us was because
our users as a consumers and the
consumer is very different to the
business central user because you had a
choice if the software doesn't reflect
or feel in a way you know how expect it
if it feels him Dom will just lost him
right away so the ability to reach
consumer soul is something very unique
for us so let me show you how the
product is look which are going to shape
any car of any couple of weeks in North
America in UK based on the auto mode
dynastic so I'm going to switch back to
our demo alright so first of all I have
a consumer I'm not technical guy I don't
know anything about business central
anything exists I start my work here so
I go to office.com where all application
is you know my beautiful PowerPoint or
Excel and here I can see a new product
called invoicing so I'm going to just
click this one the first thing you can
notice but user will never do we use
that business central dynamics that comm
invoicing as a way to get there
that's why utilize our fifth line end
point so you can find a tenant in
milliseconds for you
as
experience right away so the first thing
you will notice to miss my home page
but you know it's a classical or all
center and if you look in the content
it's so straight for us I don't even
explain it to you so I see my main list
of actions I can see my numbers I can
see my call to actions and em I see my
graphs and actually the users use the
term colorful inside when they relate to
what you see on the screen right away so
as you might notice we don't have
headline control partially because you
don't have a lot of data to show there
but also partially because we wanted to
you to save some space so what I want
you to do now I just want you quickly
look what you see on the screen so as a
new consumer user I see something called
get started and what we figure out that
it's very hard sometimes can be to
explain how to set up a system or to
find where all settings are so what we
do here just in his eyes you can promote
you know here's all the settings you can
do if you want to set up your product
your business information your email
integrations if you want to integrate
two different therapy system so on and
so forth
sometimes you want to promote a specific
set up action so in this case we decided
to show him here's the easiest way for
you to set up your online payments it's
just a sub page out of all the settings
you seen before and when the user
completes this task you can just change
the ability of this task so he won't see
it anymore
so we use this actionable cue section
also to showcase I will set up tasks and
once you complete we can just move away
now let me show you how my entities
looks like so here's my invoicing list
and it's very straightforward for you
and for me I can loose a lot of data I
can copy to excel I can definitely see
when I have a problem with the invoices
like here I want to take an action now
if I'm going to my customer list what's
new for us and as a user I can use
different tile layout and here's a
picture which my daughter drove and but
for me is a user it brings a bit more
shiny experience when it was my customer
data because when I compare my contacts
from a phone from exchange I usually
bring a lot of image and information
with me I can always pray
my home button to go home which is very
very important because I will never get
lost so let me quickly create a new
invoice for you or see how the
experience looks like so I press the
plus button again I don't need to sync
which is great so we don't lost me so
far I'm pressing the plus button I have
the beautiful new page layout I have a
field which I need to fill out when I
start to type you don't see my fingers
but the system simply react exactly what
I would expect it to do so and that's
actually very very great so in this case
I just like the customer I see it yeah
it's a wrong pronunciation but it's my
horrible English and then on the right
side for me and on the right side for
you we use a box to put a lit bit
more information about the customer if
you interacted with the past so I'm
going to do the same just add you know
one invoice line and that's really it
now what you do next well in this case
is very straightforward my action bar is
answered by default so I can clearly see
an action I can take in this case I can
go ahead and preview my invoice and this
is like a first time we derived slightly
from business financial behavior instead
it's just download a document we'll just
use our PDF control to preview it right
away so you can see here's my
professional-looking invoice which I'm
going to say it like I just checked my
final details and finally I can just
send it to Alice's Wonderland in the two
clicks any two clicks when my invoice is
sent what's happening the system takes
me back when I just started to my home
page and what you can see right away is
that my colorful insights got
immediately refreshed exactly as you can
see I would expect and it just worked
like that so I'm going to do I'm going
to drill down a little bit in a colorful
inside so here is an Alice in Wonderland
and it's so I saw him some history with
her and hmm there was an overdue invoice
and so on so forth so as I navigate
through the system and this new modern
experience for me it's very very easy to
go back and for the consumer it's a
super essential because you'll never get
him lost
all right it was a very very short demo
as I promised so let's summarize what
we've just seen you seen a modern
consumer product which Microsoft is
going to shape and upcoming weeks Barra
which is powerful which is powered by
the business central platform you've
seen how the new look and feel and how
we can use the space of the components
to achieve the experience when I build I
cannot overstate how much accessibility
is important for Microsoft we would
never ever able to ship any product as a
part of office 365
which is the biggest productivity suite
in the world like 130 million customers
if our platform wasn't accessible from
day one nor we were able to ship any
product on the microscope brand which
doesn't have a high level of security
requirements and proficiency by default
I put a couple of quotes which i think
is interesting to reflect for this
audience one of the variation we had as
a group when we build this product it's
how great more than a work for a simple
scenarios when you think about all the
demos in today is built based nav
heritage so it's a lot of actions a lot
of action groups it's a lot of content
but in now a simple case oh you can say
straightforward cases we can also
achieve very nice user experience and we
just amazing about that when we show
this fork to our formal yeah formal
general manager Marco that was a quote
which he shared which he shared with all
our organization basically saying is
that he really inspired us is product
groups and also use it partners to take
all this modern work and build very nice
experiences for the end users which is
simple and easy to use
finally another quote I want to share
with you so here is the comment which
one of our customer left to us so what
he said but she said new invoicing is so
pretty and there was a smile in in the
end but what she really really mean that
it's not invoicing that it's our new
modern division experience is so pretty
and what is really mean for this
audience how a business central platform
is a very pretty and then you get a
comment like that was a consumer it's
very very hard to I mean it's not
granted it's very very hard to deserve
the try to put this quote on the stage
because when consumers put comments like
that it usually means it's more than
look and feel it's something about how
the indirect is a product how natural
seems to work and I just you know
delight you're on a good day so this is
the message from delivered today that
you've seen a lot of great demos of a
small scenes here and here but it should
allow you as a partner and other the
Microsoft able platform so you can
deliver truly beautiful consumer ed
experiences now in fact we always
provide a lot of feedback by since it's
work to have a platform you know all the
improvements we can do to make it even
better and what I'm going to do now I'm
going to invite the stage back Thomas
Andrea to show what's coming
wherever shortly to make it the story
even great thank you so now let's talk
about what's coming next
I'm I'm really sure that Aaron here came
for this moment to see something which
we are working in progress which no one
has seen yet and there's always comes a
big disclaimer that things you'll see
next is working progress we are not
guaranteed that features will look
exactly the same when they ship in a
spring and if they definitely gonna ship
in spring if you want to hear more about
our release notes they will be announced
after year and there will be a stronger
commitment and a list of things which
will be included in spring release but
all of this disclaimers let's see what's
coming next Andrea yeah so last year
back on this stage I concluded our
presentation with a sneak peek of
Madonna and now I would like to demo one
new feature we're working
at the moment still work-in-progress you
saw in one of Thomas demos you were
filling an invoice what was the order
you were typing a lot man that was sales
quote I say squad yeah he was tap tap
tap tap tap tap tap well he was filling
in the document basically it was timing
too much and we have a feature for
avoiding users to to tap too much but
just go straight to the fields that we
want them to go to in order to fill in
the document you know which feature is
that yes precisely again the same one
okay you already have one I will try to
figure out another question but yes
quick entry so quick entry as well it's
a feature it's one of those features you
have any Windows client and web plan
still doesn't have well coming yeah and
it's working progress I'm delighted to
tell you that it's working progress
we're making it up and in a web client
but as Thomas said we don't just fill
the gap when the Windows client and just
blindly copy the feature into the web
client we try to do is asking ourselves
does this feature make sense in the new
world if it does how can we improve it
in order to increase experience and
increase productivity and proficiency in
general and that's also the question I
asked ourselves when it came to quick
entry so we decided to yes let's bring
support for quick entry but let's also
add something more to improve the whole
scenario so most lies let just go
straight to the demo and well let's
let's create a new sales invoice so I am
a minor I'm not here and I'm gonna use
the keyboard of course quick Henry's
normal keyboarding so alt arrow down I'm
going to pick customer and I have it and
now guess what I'm going to move using
enter by using enter
moving towards the different fields now
the future was partially supporting the
web client but now there is possible so
I can jump straight into the grid by
just hitting Enter space I can get the
item okay that's it
always with keyboarding I'm gonna go out
I wrote down I'm going to select our
front wheel enter and that's my line has
been saved enter and then enter jumping
to quantity and I'm selling it to chew
cool enter again and I go straight to
line discount because that's how did the
blog pass the site experience but I just
realized that actually I don't need you
I want three of them so I could go shift
tab my shift tab I would need to go one
two three times shift tab in order to
reach the the quantity field well not
really introducing shift enter and with
shift enter
I am reverse quick entry in the
experience has to say and I can fix it
so I mean quick entry was designed to be
a formal long experience as if humans
did not make mistakes but we make
mistakes we are humans after all so we
just recognize that and we implemented
this new feature which extends the quick
entry experience so reverse screw
counter is also possible using the
combination shift enter so I made my
edit and well of course the notification
updates and and you know him I just
completed my my line now I I want to go
out of it because I want to keep filling
out stuff in my in my invoice and if I
hit enter again the quick entry how I
behave is that it will go through the
different lines of the of the grid until
reaching the last quick and to reachable
field the last row and there when I hit
enter I can jump out of the grid the
point is I'm done I'm actually done I
didn't in this great so I want to just
go out control enter already let's you
go out of the grid but it will focus on
the first field out of the way which is
subtotal
that's not where I want to be I want to
keep the quick answer experience so
introducing control shift enter and
control shift enter gets me out of the
grid to the first quick entry reachable
field out of the grid so we have
improved experience to to really get the
most out of it and here I can move on I
can keep hitting enter to basically
reach all the fields in my page and
enjoy this experience of course will be
personalizable indiscernible yes you
will be able to set a quick entry in
personalization and if I reach last
field and keep on clicking enter the
feature is cyclic so you will jump to
the first field of the page shift enter
you go back to the last one so we have
socket feature forward backwards jump in
the grid out of the grid quick jump out
of greed all these new features and
quick entry we're working on that and
it's going just to be amazing awesome
and right that's it for me ok I will
show you something which kind of was
mentioned in the keynote it's the new
virtual grid experience so we got a lot
of feedback that oh yeah please don't
read that our grids are quite slow to
load on web client and they also are a
bit also you can it's very noticeable
when you switch the list layout type so
what we did and we saw what you saw in
the keynote
presented by harina is that we utilize
the grid so we actually are rendering
only the rows which are visible to the
user that means that we can load a lot
more data without paying the cost of
rendering it and that is a common
pattern which we adopted and partially
built using some great technology from
react and another set of gain when we
visualize the grid we also reduce the
memory footprint that means that we are
a better citizen in
browser we're consuming less memory that
means less power they are more friendly
on devices which are power constrained
and basically you don't really Almo we
can't really see where we have the new
grid and where is the old grid is just
like a lot faster and that's awesome
because users they don't and other thing
you see here is that you can keep
scrolling and now we have this my
network connection I think that so when
we scrolling the grid and everything
here is working progress so that demo
gods of course we keep showing user the
loading rows so he never hits this brick
wall of loading more we don't want that
experience anymore once we want to allow
user to just keep scrolling and will
continuously load more data when it
becomes available from the server then
let's go to a sales order
and here it's a document page type and
in this page type we have a grid and but
we also have bunch of fields on this car
on this page and when users are trying
to enter sales order lines it's not that
comfortable of experience because you
have just a tiny area for your lines and
we heard this feedback and we thought
what could we do better well we could
actually introduce an expand button and
guess what it does it makes the grid
fullscreen and we still keep the list
totals so you see them at the bottom
because they are connected to the grid
they are the computations from the grid
and this is very much in progress so you
still see like double action bars that
will change because we only need the
contextual action bar fault for the grid
and another thing which we cannot do in
the card in the document page is to show
the filter pane because there's simply
no space to show a filter pane so in
focus mode we have enough space to show
the filter pane so you will be able to
do your quick data entry and the filter
pane will also be expanded or expandable
on the side so be able to filter for
sales order lines or any lines while
working in a grid and it just works
seamlessly another thing you might
notice is this guy tiny tiny indicator
in the corner which has saved what does
that mean when users especially new
users new to business central trying to
create for example sales order they
don't quite not always understand what
is auto save and when we actually save
something and when we don't so when you
open a new sales order and it's a draft
record we don't see any status but
actually if I start selecting customer
name we'll get a customer sorry a record
ID so it's filled and now it says it's
saved but actually because actually now
the record does exist and it is saved so
introduced a
save indicator which shows to the user
when his interactions trigger a
communication of the server and when the
data actually reaches the web server so
user is always aware what is his record
state yeah that was the last sneak peek
and we have many more productivity
features coming in spring and you will
see them in release notes which will be
released sometime after near so stay
tuned we would like to finish with one
thing which is very important for us
it's your feedback and one way to voice
it is to use our cloud products or
navigate to IDs ID in the cloud solution
you can actually hit smiley face and
submit your idea
please check the portal submit new ideas
or upload ideas which was already posted
by the community because this is very
important for us we're using this to
prioritize our work and this will help
us to create a great platform which is
ready for the cloud thank you now it's
time for your questions just another ask
with dummy feature did you fit in or do
you think to put in some Easter eggs an
example could be okay
senior song Cortana could pop up and
sings a song unfortunately we have a
policy about Easter eggs
I just wanted to get a bit more of an
idea about what's happening with
personalization in new modern UI
particularly things like resizing
reordering columns that sort of thing so
resizing columns have already shipped if
you enter personalization mode you can
resize the column width all right so
that's only within the personalization
mode that's not something you can do
that because you obviously in the old
right you could just do that drag that
is true you have to enter the
personalization mode to do that and
that's something we discussed but yeah
we're trying to prioritize other things
but it's something we are thinking about
cool thank you
in the classic client was a great
fishery were able to mark particular
records and then set to view only market
ones so it's kind of custom filtering if
you have something like that or you have
plans to implement it no but it sounds
like a great idea which you could submit
your ideas side and people my question
is regarding the inclined designer last
year you showed up the inclined designer
where you could add the fields and then
save it as an extension one of the
features that's disabled is adding a
page part and actions and things like
that are you guys working on it any
progress or update
so in general we are working on designer
of personalization experiences in
various parts of the product and some of
that will be addressed but I cannot
comment on exactly what will be you'll
see it in our release notes but it is in
our pipeline in general to enable more
and more things you can change we always
try to make it step by step that you can
always personalize something and design
at the same time will you support themes
like dark mode high contrast people will
we as I say as I mentioned last year the
whole modern experience is basically
driven by a seeming engine under the
hood so there is something that will pop
up at a certain time we're thinking
about that
at the moment we cannot make a statement
precisely when it is going to be and how
the experience exactly is going to be
but we're thinking about the definitely
I guess users will search for it yeah so
ideas side go there submit submit that
idea and we laid out the architectural
pieces for it but we didn't quite yet
arrived to the experience which we want
to expose and how that interaction would
work but yeah definitely submit an idea
of what that will help us to prioritize
there was a question there okay you
already have two votes
I am some I saw yesterday in the keynote
was the page inspector something we use
quite a lot is the practice report
feature to view the data set exported
Visual Studio we haven't been able to
find that and as a central is there any
plan to do just that functionality well
it's definitely something we are aware
of and again it just boils down to
prioritization and that again same
answers could have or that idea to help
us prioritize it to see what the partner
community feels how they feel about this
feature and how it is okay thanks
two questions regarding the filtering
first one is it possible to filter by
all columns in the table or only those
added to the to the page so you can
first first to show all the visible
columns but below that there's also
actually our old columns all columns
from the source table okay so it's
available right now
yeah okay and the second one gives in
the document layout of the page is it
possible to filter lines yeah so that's
that's what I showed that we don't have
the place to show the filter pane but we
still have the previously available
feature filter to this column it's a bit
clunky experience but when we have the
focus mode we'll be able to show the
full-fledged filter pane and allow all
the same behavior we have a list okay
thank you so previously filter to this
to the to this column is still there in
like document pages so you can click on
right-click on the column and it can
still filter on that column hi regional
settings are they attached to the user
or to the company that I'm working like
a date format point comma that's a good
question I will need to get back to you
okay
well now the cherish's oh sorry one more
again filtering on option feelings is it
still true that you can only filter on
one option field from a drop line you
can select multiple that's that's
correct that is one of the missing
features we have and again we wanted to
shape the filter experience as complete
as we could but that was just one of the
things which went out of scope and we
definitely want to come back and add it
and in general we want to add multi
option selection so one one once that is
available we can also reuse that for the
filtering thing thanks
hello
so you mentioned before that you
implemented some react features into the
loading times on bigger lists and etc so
my question is with the flow filters
does that help
eventually loading up how did the flow
filters load up do they load up when the
row is just loaded up from the sequel or
they're trying to load up just when you
open the page so the command computation
part actually happens on a different
part of the stack so the react client
side didn't really affect that it's just
about the client experience of loading
massive lists that's that's what it's
about so the the backend for computing
loading actually data doing computation
is still the same oh thank you tell me I
can ask a few questions sure I was
wondering do you have brick views in sub
pages if it's something you would like
to have again we will see the color of
the text the style texts are there more
colors so at the moment the the theme
that we have is the modern a theme so
those are the six colors score set that
we have the pallet that we have later on
still we need a story we need to define
all of these we might think about adding
more same
or we might think even about letting you
define your own themes and colors
at the moment no in the future we will
say the style text there's no yeah so
those are we've kept the same palette
for style views we've seen that you can
navigate by keyboard yes it is
accessible using keyboard it's possible
to go through them every single
component was again I will just
reiterate architecture from ground up to
be accessible and we constantly every
time we ship a release we do testing
accessibility testing and we make sure
that we're still compliant and I was
wondering if you can pin one action at a
time right now no but that's a great
suggestion that's it thank you we have
three minutes left
so still time up there there are two
questions hello hello non editable
screens and the lookup doesn't seem to
work again on a non editable screens no
energy if you're in the item entries you
want to go to the location there's no
looker because the screen isn't editable
that's going to be fixed or design if it
looks like a bug I can't tell really if
by the time please report it we can have
a conversation just later and so we can
process a bit more of this scene behind
you there was another gentleman
thank you so like my question is in
Windows client so users usually would
have multiple screens they can open
multiple windows and they can you know
they can have one page on one screen and
so on so how does it work in web client
can we have a pop-up window that would
or day need to open multiple tabs right
now you have to open multiple tabs but
it's actually something we fought about
and again it will be awesome idea for
idea side to see how people react to it
and how how they think it should be
prioritised okay well thinking about it
behind you just to continue on the
previous question because if you correct
so licensing issue so definitely if you
yeah it is a reasoning for having them
the pop-up thing because then you don't
need a new session yes 25 seconds one
quick one well you saw in our demos that
we did use edge as well and chrome our
point is that we support all browsers
and not just ad so we optimize for our
experiences with Firefox with super
Firefox we support Safari we support
edge IE and in the other browsers so
it's a multiverse with different
browsers and we support all of them and
we just try to show the reality in the
demos we use all kinds of
yeah I think he should get a t-shirt
totally we have one last actually no no
hello that perfect 40 minutes of seconds
over time now we just did it thank you
thank you everyone
[Applause]
