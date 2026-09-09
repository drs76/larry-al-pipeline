# Testing is Boring... Until Now!

- **Source:** https://www.youtube.com/watch?v=-DJ8Yn8VNeA
- **Video ID:** -DJ8Yn8VNeA
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 92m55s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

ladies and gentlemen good afternoon and thank
you for being back here in room 8 uh now the
next session is called testing is boring until
now and that is a promise made by Luke and Tina
[Music] are they all here just because it's
boring i don't know do you think Are you here
because testing is boring yes why are you
here then come on [Laughter] well that's a
good option yeah okay welcome welcome to testing
is boring until now come on come on my name is
Tina i'm an architect with Companion but I think
the only thing you need to know about me today
is that I'm a huge test automation enthusiast a
big test automation advocate but I kind of pale
in comparison with Luke so maybe Luke could you
introduce yourself for people who don't know you
what did you need to know about me no I'm here
because this is a this is always a fight well
no it's always a whatever enthusing moment to
tell about to talk about testing in my opinion
I hope the boring word is going to disappear the
way I would describe Luke is that he's kind of
like the the godfather of test automation and
business central because he wrote books about
it he wrote blogs about it he talked about it for
for many years but you should have seen his face
when I proposed back in January hey look could
we do a session where we say testing is boring
until now and it was like I consented to walk
away yeah he wasn't he didn't like that title
but I insisted and here we are anyway last year
I was doing a session at a different conference
uh which I titled I'm willing to fight for test
automation and I think you should too the premise
of that talk was that I as a developer I I like
to write tests but maybe sometimes the consultants
they don't want to see me write tests or maybe
the product owners they don't want to see me
write tests or the managers they don't want to
see me write tests or maybe sometimes I'm one
of those roles and developers they don't want to
write tests right the the session was all about
how they push back against the arguments why
we need test automation and how we push back
against those push backs But for today for all of
you I I do kind of expect that we all agree that
testing is important and that test automation is
important but just to get us all on the same page
I took two of the main takeaways from the session
last year why do we want to do test automation
why should we care about test automation well the
first reason is that when you build a feature you
want to test that feature and if it works you ship
it to your customers but then the next time when
you build another feature you're not sure if this
feature breaks anything from the first feature so
you kind of have to test both of them and then
for the third one you have to test all three of
them and you can kind of see from the picture
here that regression testing it takes more and
more and more and more time and if you don't do
test automation you're going to start drowning
in regression tests boring boring so that's boring
and the problem with drowning in regression tests
is that the answer to it is usually let's just not
test right and that's when you famously get this
picture a bug found in production is so much more
expensive to fix compared to a bug found in the
earlier stages in the stage of requirements
or design or coding or or even testing
so the first kind of argument why we need test
automation is because otherwise we're going to
drown in regression tests but there's another
reason why we cannot rely on manual testing for
regression tests the value of manual tests is only
there on the day you perform manual tests the next
time when you build another feature the value of
those manual tests it's no longer there but with
automated tests the value of an automated test
is there from the moment you create it all the
way into the future because you can run it again
and again and again every day every hour every
minute if you want to so the second reason why
we want to build test automation is because its
value goes into the future while manual testing
stays only on the day when we perform the tests
so these are kind of the the two main takeaways
and I think now we're all on the same page why
do we want to do test automation but then the
problem is that it's it's kind of boring you
know so what do you want me to say yeah uh if
you're still kind of early into this let's say
adventure of test automation there's a brilliant
webinar by Shavei on AOPA channel so if you want
to know more about that here's the the QR code
for use it it was for me also uh it's one of the
best kind of eye opening it is it is actually the
title is tests are bats that makes it even more
I think appealing yeah how much should we test
should we test everything so what are we going
to do today yeah so for today we're going to talk
about first a little bit about traditional testing
the the boring part and then what makes testing
no longer boring with page scripting and then
with datadriven testing and when we are going
to introduce these additional testing practices
in the end we're going to try to tie everything
together how it all comes together and of course
we're going to do a bit of a recap yeah but
I think for traditional testing there's no
one better to introduce it than the godfather of
traditional testing i'm I'm I'm already elevating
um you might recall some of you that were here
three years ago i did a presentation with Nicolola
Kukria from Microsoft and this was one of his uh
statements which actually I recall always recalled
and at that point I thought well this is straight
to the point test automation should shave sh save
you time yeah or money uh if not you're not doing
something you're not going to do something well
it's something wrong if if it's like over over
budget again like many project because of testing
that is postponed whatever if you don't manage
to bring down your cost with test automation
the statements was you're doing something wrong
keep that in mind somehow and with the things
we're going to show you and of course what has
been already there um in my opinion and in my
experience it's it's really going to help you to
bring down your cost uh but before we do uh before
we go into the different parts as Tina showed you
in the agenda let me discuss a little bit on my
favorite uh uh topic they call it hobby horse
i believe in English in Dutch it's stock party
uh something I always write because it's not just
the fun of it but it's the importance of it um
why on how can you test something if you have
no plan and a plan could be of course like I'm
experienced I've got some internal uh plan this
is what I always do but then still nobody can
check what you're doing and nobody can repeat it
when you're not there so this test plan concept is
uh something that I actually through test
automation really got into it uh working as
a tester at Microsoft manual tester you had to
do this also more or less uh what is a test plan
is a list of scenarios the things we're going
to implement at 4PS where I'm part-time working
the discussion is should we change the name to
scenario plan or scenario list it's not defining
tests it's what we're going to build and as such
what are we going to build we're going to build
user scenarios we're going to enable a user to do
something that's what this list tells you yeah and
uh u as such it it defines uh theoretically maybe
it's too big sometimes all the different behaviors
of the system like you slap me on the face on the
on my right side and I cry and you slap me on the
right left side and then I think now I'm going
to slap you whatever that's a behavior and each
thing is a different one so in this case there's
a a multitude of behaviors defined by all those
scenarios right um and as such as we know the
behavior that's what we're going to check yeah
that's that's the set of tests actually a test
in my opinion should not define oh this is it
we're going to test that the outcome is showing
this that's what we're going to check true but
what led to that there could be million different
ways to get there yeah and if we just say check
that that the outcome is there with one option
I'll already show it no you need to define the
scenarios um and as such you could even say it's
a translation of the pros in your requirement even
if it's user stories it's a translation of this
is what we're going to build uh in the workshop
we did this week actually I left him on Wednesday
to do him on his own we used AI to create a test
plan and I think we did get quite nice results
why this test plan so not as such what yeah
um why a test plan is a great tool that's from
what I found out by doing also it's a great tool
to review the requirements at 4PS we started
with this the goal was test automation where
we started with this challenge the requirement h
I've got six scenarios wait isn't there a seventh
or maybe other somebody else could say it's much
more easy to discuss it's not something oh yeah we
understand the requirements and then you sit down
start programming and you think what the heck is
this an option is this an option or a variation
right um so um sorry one too fast to keep a focus
on this one as such is also a great way to get
developers included in the knowledge of of and
testers and documenters if you include them so
it's a way of sharing the knowledge already and
uh that's an important part to drive the quality
of your software yeah if you're not able to come
up with the scenarios your requirements are uh
running short yeah they're not complete enough
okay so that's a bit about the test plan as such
an example and that's a little bit about what
you will see in the code examples also this is an
example from 4PS we use at that point just a plain
Excel sheet start to create some columns etc etc
but there is always uh a same structure in it the
first part is always let's say the functional
area what is the user story in our case and in
what part of that user story we're going to focus
yeah and then there's always a part where we uh
give each scenario a unique number and as a third
part of course that's the most important part the
description of the scenario those who have been
in the workshop I'm quite strict on how you phrase
that because it should be a user action ai came up
with attempt to do wait a user is not attempting
to do something the user is going to do something
and if the attempt is not going to succeed it
is and that's the last column uh my clicker is
probably I'm walking too far away uh but uh it's
a positive negative test if it doesn't succeed
it fails right so this is a bit about the test
plan uh if you want to know more uh in my book
or various uh uh presentations at Aropa one with
Christopher uh sitting here um so they all relate
somehow to this yeah so this my point to step into
traditional testing what we now call traditional
testing the the boring part right yeah yeah okay
okay the boring part the boring testing um why we
call it traditional testing this is the part of
test automation where we write AL coded test yeah
and this has been possible for quite a while but
let's say it started to accelerate due to the push
into extensions and first of all that you need to
deliver for apps source an app with test app right
so what is this about this is about uh defining
actually your automated tests by coding them in
AL because the platform allows us to do that yeah
by the way not 2009 service pack one that was in
the summer of 2009 that's almost 16 years ago 16
years wow yeah and the thing here is the platform
didn't allow you Sorry let me I got a call this
week so the platform didn't allow you to uh to
set up one test with a whole bunch of variations
so each uh unique scenario should be coded as
a unique test you will see in the some of the
examples and that's what I've been advocating for
quite a while um so let me show some examples i
put them on screen here because I'm not going
to dive too much in the code by the way before
we do our red thread is this uh business case
extended text on assembly document documents you
might all know the feature somehow that you have
uh extended text on sales and purchase documents
by the way nope
she's got a very long password that's why
did I put on my caps lock no I didn't it's
not easy to get in my to my laptop there
we go by the way I'm going to sneeze my
nose so you might maybe mute my microphone
you said boring i'm getting emotional so um in
short what I want to show you should I switch
and I'm Yeah we're going to switch it if I'm right
it's going to switch and it did but then it should
open up yeah so in short this is an extension to
the standard functionality you have extended text
on items on resources uh GL accounts I believe
and uh on purchase sales documents service
documents job planning lines I also believe you
can add one of those and it will add some extra
explan explanatory text yeah so I do have an item
here i call it BC something so let's have a look
yeah bc something bc item and this PC item has
automated automatic extended text uh turned on
and herefore I created an extra
extended text yeah and I turn it
on for assembly order and if I create an
assembly order assembly order whatever
you might see I do need to have more in the
header than this one so if I'm adding that item
you can see you should see that it as you can
see adds an extra line just to have everybody
in line it's not rocket science the the feature
has been uh in one of my repos for quite an age
already uh feel free to uh to go there and uh
take it from there yeah so the code examples
relate to this and actually it's about 60 to 90
test all together oh I'm go the other way around
uh and you could say these are if I go back
these are the three scenarios I will focus
on first I'm adding an item line like I just
did did just now on an assembly order or an
assembly quote or an assembly or blanket assembly
order it's called and then I'm going to test that
u for those familiar to give and when then I
always explode this thing and I define okay
what is the the circumstance ances what are the
circumstances the givens what is the when and
what is the then by the way what you saw just now
the first given I have an assam an item with all
things set I create an assembly order I add the
item that's the when and then as the then you
see that uh the extended text get added I'm a bit
struggling with my voice I'm going to sneeze one
I thought on uh Tuesday evening am I going to make
it with my voice so far so good i think you sound
great well it's not too bad um these are the two
the three code examples and each of the uh example
or each of the test I should say has a number and
you see the code in each of them this will move to
the second one and it's more or less the same yeah
and the third one it's more or less the same so in
that collection of 60 to 70 tests there are even
nine of those and nine of others so it's a lot of
work and I think well okay that's the boring part
and then you're lucky with this one there's only
two givens some might know from your own work
but I surely have sometimes one with 20 givens
all the way because we're so depending on on the
data yeah and that's a traditional by the way the
workshop and the sessions I did with Kristoff is
about how getting your code much better so your
testing becomes easier yeah but that was not
the goal for today because we're going to show
you some other things okay and that's the result
so so now let's talk about some some more fresh
uh topics in the world of testing now I had
this huge plan for how I'm going to introduce
page scripting to you but then Vincent threw a
a big wrench this morning you know I I was about
to say how I still remember from two years ago
how he introduced page scripting in the from the
lab part and I got super excited about that tool
and that I know a lot of you know page scripting
you've seen page scripting and how this is going
to be just kind of a reminder for all of us what
page scripting can do how you can use it but then
after this morning's from the lab session I feel
like this is again the boring part and what he
did is the interesting thing so I don't know i
think I'll have to redo this next year still I
do I do want to show you briefly like what is
page scripting right in one sentence it's a tool
that can help you record steps in Business Central
that you can then later replay so I'm going to
try to build a test uh a test automation for the
feature that Loop just presented to us i have
to switch to to my screen you're seeing it yeah
let me log in real quick so with page scripting
where do you find it you go to the cog wheel and
you have um an action here page scripting preview
you won't see it if you don't have the permissions
to work with page scripts there are two permission
sets one to record one to replay you need to have
the appropriate permissions to work with this so
not every user can use page scripting but once
you do have permissions you click it starting
with page scripting is super simple you click
start new and from this moment on as soon as this
red button here starts pulsating whatever I click
in the system gets recorded so if I navigate
to items to reproduce the business case Luke
introduced before you can see that it recorded me
navigating to items and I can create a new item i
can select a template for a new item i can turn on
the automatic extended text give it a description
item with X text now later on when we are going to
create the assembly order we will try to validate
that the first line of the assembly order has the
description from the item card and that the second
line comes from the extended text in order for
me to be able to validate at that point whatever
I've just put in I'm going to first copy this
value because when you are recording your page
scripts when you rightclick a field you get this
page scripting option available and you can copy
the value i'm also going to copy the item number
because in the assembly order I want to specify
this item that I've created in the first part
of the page script so I'm going to do the same
thing here paid scripting and copy and you
can see that it records that as additional
steps of the script now here I'm just going to
throw throw in a bit of a best practice when it
comes to page scripting when you're entering
values with page scripting like purchasing
code you might be tempted to just click on the
value from this drop-down menu don't do that
the problem with page scripting is that if here I
click drop ship it won't record that I've clicked
drop ship it will record that I've selected the
second row on the drop-down menu so if later on
we add an additional purchasing code something
that starts with A something that starts with
B you can kind of imagine that when I would be
replaying this script I wouldn't be selecting
drop ship i would be selecting callin so the best
practice when you're recording page scripts is to
always go to the select from full list and then
filter down your selection so that it only has
the entry that you actually want to click in my
case I'm going to type drop and you'll notice
that this drop filtering becomes part of the
recording and now that I only see one line here
I can click it and that gets selected recorded
so make sure to filter on the primary key yes
filter on the primary key i don't actually need
the purchasing code for for our example today
but I have all of these steps recorded and if
you want to undo a step while you're recording
you can click click the three dots here and you
can delete you cannot go back in the middle and
delete a certain certain step that's in the
middle here you can only delete the last step
and what I really liked is that uh Vincent kind of
experienced that pain firsthand today he couldn't
go and delete uh that missed entry so I do hope
that maybe they're going to fix that and we will
be able to go in the middle of the script and
modify the parts there modify the steps but today
we still kind of have to delete all of these steps
one by one so let me just remove everything that
here relates to the purchasing code delete delete
delete delete delete one more one more one more
okay and now I can continue with entering
the extended text for my item so I'm going
to navigate to extended text create a new one
give it a description extended text and while
you type do you notice it only records the action
not where you select it that's one of the major
uh values here i don't know any of you
working in an organization using visual
test tools like Selenium or whatever that's
a big pain in the ass because if Microsoft
comes up with a new version everything is
moved and all of a sudden all your scripts
breaks but here you can as long as it's
visible you can move it anywhere yeah so
we are going to validate if the second
line in the assembly order is added so
I'm going to have to copy this value as well
but now that we've created our item with the
extended text let's go out of all of these
pages and let's navigate to assembly orders
okay let's create a new one
i'm going to set the type to an item and now
here the number right i I don't want to select
the number i want to enter the same number that
I've created in the first part of the script so
what I'm going to do is rightclick page scripting
paste and you can see here my whole clipboard
so the description from the item card the number
from the item card the extended text line i need
to paste in the number and now we can see the two
lines have been added i can now validate them for
this to actually become an automated test not
just a recording of steps that should execute
so I can rightclick the description field page
scripting validate current value is equal to
the clipboard entry the first line should be
equal to the description that I copied from the
item card and I'm going to do the same thing
for the line two here validate current value
extended text lines and that was sort of like a
brief introduction of how do you record a page
script and then once you have it recorded you can
replay it to ensure that this functionality works
now to to replay it I first have to rewind to the
beginning but now if I just click play it won't
work because the first step says navigate to items
but we're already on the assembly order so this is
kind of the the second best practice when it comes
to page scripting start your recordings from roll
center always because then you won't have this
ambiguity of where should I stand when I execute
this uh this recording so I'm going to navigate
back to my RO center and I'm going to click play
and what you'll see that now all of these steps
are being executed step by step we're creating
the item we're creating the extended text and in
the end we're also validating if everything works
so I just created an automated test but I don't
have to be a developer to do this and that's where
I see like the biggest value of page scripting
i know in this room most of you if not all of
you are developers but that means creating test
automation is well very development effort heavy
but with these tests which yeah they're not as
good as AL tests I would say but we can have
consultants create tests but you can also look at
it for beyond the the the testing potential this
is a very good tool for reporting bugs because
I have many times received the message something
doesn't work from a consultant right and I'm like
okay but what were you even trying to do and even
as a consultant you get an email from your end
customers saying uh I got this issue that there's
nothing to post well yeah okay but what were you
trying to post in the first place when you got
that error so you know if I can teach you to
start using page scripting and you can teach
your consultants that they use page scripting and
they teach the end customers to use page scripting
then we won't only get the screenshots of the
errors we can get these recordings that we can
replay and maybe the recording won't work in our
containers because the the data isn't set up the
the right way but at least from the recording you
can see what they were trying to do and that that
can help a lot with troubleshooting the issues i
mean creating those documents I don't know word
document attachment or whatever to get all the
repro steps it's quite an effort yeah so with
these scripts you can save them here and it will
say that you might be uh containing some sensitive
data in the recording so be careful what you do
with it yeah yeah and you get back a YAML file
but about the YAML file Luke is going to talk more
about that so this was just kind of a brief highle
overview of how do you record scripts with page
script with page scripting tool and how do you
replay them and that this no longer needs to be a
developer's job to create some test automation at
4PS we have still quite a backlog on uh automated
coded test and we have quite a number luckily
of manual testers which have scripted everything
so uh they they rerun that on frequent basis you
could say uh but every time like if you go back to
the the graph that uh Tina showed manual testing
has a short value a short time stretch and after
that is gone yeah you do it again but it's the
same investment you're not going to win time or
money on that and we have decided with the next
regression test run we're going to spend an extra
week to do recordings so all the testers will
profit from it in the next time and and that's
also was the second graph as soon as you automated
things it's a longlasting value and you can run it
anytime but as a kind of step to something later
on also what I'm going to talk to yeah I think the
clicker works is uh shortly about the YAML uh so
as uh um Tus showed you can save it and that will
be saved into the YAML format for those who are
not familiar with it uh the the the the meaning
of YAML is yet another markup language so likes
HTML XML whatever another markup language um and
the format is used also in pipelines uh in Azure
DevOps for example so for those who are familiar
I show you a little bit it's not about getting
you to know everything but what Tina just said or
showed you can only delete the last step of course
I can go into the YAML file and remove anything
what I want yeah so editing in the YAML file
is possible it's a challenge and yes especially
if you talk about enabling non-technical people
to record test um yeah quite some testers in our
organization but you're not expecting that we're
going to No not really but we can so el elaborate
a little bit on this um the YAML files that we
use or actually maybe it general YAML files you
will find steps and I'll show you an example but
in those steps you have different types of what
a step can do navigate well you saw some things
as displayed in the page scripting pane navigating
to a certain page invoking I don't know if you saw
it but when he pushed that button to get uh u to
the extended text is going to invoke something and
opening up a page Well page is the page that's
going to be shown uh closing a page a page is
being closed yeah so close page is the action and
that is done it's it's the state you could say and
there are a number more focus you might have seen
as soon as Tina clicked on another field moved to
another field whatever however he did it that's
focus putting the focus on another field control
by the way for me this is uh a lot of noise in
the in in the recording because often you click
somewhere oh yeah like you did I think even in
between and it's not the field where you want
to be but it records it and you see it jumping um
you could maybe write a routine to clean it out
uh input setting the input where he put a value
in the description and then jumping to a certain
row where Tina actually said don't do that yeah
uh preferably I would even say don't go even
open that page and go filtering no you know the
value already type it in just type item in it and
the system will validate and and accept that yeah
and copying the value that's putting that on that
uh let's say page scripting clipboard where you
can start reusing it somewhere else um let me
quickly jump to this one here this is more or less
the script that uh uh Tina was recording and I
collapsed a lot of things you see all those types
of steps happening um there's one at the top I'll
discuss after this but then navigate page shown
invoke validate all kinds of things if we would
uh just uh elapse everything sorry the other
way around here yeah you will see everything
of the recording and I could go in if I want
and manipulate because he saved it but I can
also import it yeah and that's the whole idea as
especially the ca well especially surely the case
if you talk about a bug or like me I'm sitting
developing I think wait I don't think this is okay
or I don't understand or it doesn't work let me
record it and I'll send it to my product owner hey
uh you're not here today but I'm uh working in
this environment and I don't know what happening
in that step something goes different than I'm
expected please replay yeah um so what do you
do well let me uh shortly show you here so if the
tool is open I can go here to open recording and
I can select one of my scripts you see a number
of them by the way all the examples we have are
in a GitHub repo at the end there will be a link
to that so you can also make use of it so let's
uh open this one this is more or less this the the
scenario that uh Tina did record just now and I go
and replay so replay if if you were recording you
might uh rewind and then click on play and it's
going to execute the actions that I recorded yeah
it's uh I must say I always say UI is slow ui is
slow if you program this it's way faster yeah and
u but uh compared to what you can do and even like
internally we use a tool called u ranorex as a
visual test tool a generic one uh the testers were
looking at it like wow this is fast so compared
to many of those tools this is fast however
um and and I don't know if you realized you
said you need to close all your windows yeah
um as you can see in my case and uh as A tip
execute or exercise the discipline that what
you open close it yeah if a window stays open and
you run it the next time again you probably get a
failure because of more or less what you said
so make sure you go up you get things in place
you execute and you go down again let's say you
build up the tent you have fun at in the summer
and then you go back home break it down again okay
um let's go back to this one here so a little bit
about this YAML not going to do much more except
for the next part uh as you could have seen in my
uh uh listing or at least of the YAML I showed you
there's also possibility to include and what does
include mean include means is that you can uh uh
point to include another YAML file yeah those who
are familiar with test tools also like in test
manager in Azure DevOps you have shared steps
and shared steps are those steps that you're
going to recurrently doing yeah so if you want
to maintain it in one place well then make a
shared step because every time you need that
item or you need that customer or whatever yeah
um and in that context um what we're currently
doing at 4PS setting up how we're really going to
do this is that we're discussing about this one um
always be aware of preconditions in what you're
going eventually to exercise so like in our case
uh like Tina did also create an item u uh
append a extended text to it set the item that
uh uh to that uh that switch automatic extended
text and that's the preparations yeah or you could
even argue yeah what do I need more on assembly
order actually for this test nothing more just
a header and you go to the line so that's the
preps and then you go to execute you open up an
assembly order You could say okay creating the
assembly order the header could be part of the
preconditions the preps and then you insert the
item in the line yeah so to show you and actually
let's go back to my side here so how does that
look like in this file as you could see when I
collapsed everything there is this include section
this include section references file yeah and a
file in this case relative to where my file is
in what I call preconditions and this creates an
item without automatic extended text turned on and
of course extended text and without number series
I'll elaborate a little bit on that but let's
first have a look at this one so if we go here
I could now open that one so I have a file here
with includes Yeah ah that's something you need to
do um it needs to get access to your file system
and for that by the way your container should have
uh an certificate yeah you need to use HTTP
otherwise you can't access the file system um
and you can see I do have this uh uh folders here
so it needs to select the folders so the first one
I know my include is from the preconditions folder
yeah the second one the second include is from the
post conditions and then the third one it asks do
I may I access the folder where your script is in
um this is a challenge in in uh in pipelines
uh to be honest haven't addressed that yet
uh I know Tobius Fencer has been or the team
related to uh Alpaka has been working on that
and to be honest I was so busy I should have
dived into it but I didn't what do we see by
the way hey you get a line here now with this
triangle to collapse and elapse that's my post
condition file which is included at the start and
I didn't show you but I also have an include at
the end delete assembly order and item yeah um
to show you by the way I could run each of them
separately so I could say run the preconditions
let me check which one it was without yeah this
one so I can run this and that will create an
item for me with extended text yeah and then I
could do the main flow i open the main one without
includes i really need to say it because of myself
that I'm really doing this because I I well last
my demo didn't go that well but that was due to
the fact that I was maybe talking too much while
well I'm always talking too much to to some so it
runs it it has created the assembly order and yes
if I would go into assembly orders I will see we
do have oh sorry let's type it full more fully
here yeah you will see there is this assembly
the order just created okay so now I'll do the
post conditions and it will clean everything
out for me well I have to do this in three steps i
can do this with that one file having the includes
apparently something else happened probably
because I didn't save that window actually that's
it and it's a good demo as such uh let's run the
other one then we can see it runs it all in one go
so here this is with includes yep select the
folder sorry preconditions select the other one
and this one
okay so it can run past everything right now
okay i didn't clean it up but talk too much
that's a good one nevertheless um so that way you
can include things and and share things between
uh different recordings yeah uh there was one
way one thing coming by but I'll I'll probably
get back to that later uh that I wanted maybe you
can you can tell us how does that all compare to
to traditional testing how do you see like page
scripting if you would compare it now with so
if we put those things next to each other on the
left side the page scripting part the right side
traditional you could say the the page scripting
is typically for let's say non-develop of course
use it also as a developer but as the focus on uh
test automation getting the tests automated that's
a developer work the road to it is I think it's
a team effort it's a functional thing we don't we
don't implement test just because we're developers
we implement test because we have requirements but
you give power to the uh more functional roles
you could say within a development organization
the QA roles within the context of our relations
with customers to end users and um you could say
roughly in this uh talk in this perspective of
testing page scripting is about user acceptance
testing in general of course there's more usage to
it but if you put them roughly next to each other
and the advantage is it's of course reusable which
typically is the case with automated test yeah and
uh continuously actually if you use automated
test in general at the end of the line every
time you're not going to save money it's something
that should be running every time you do changes
in a pull request you as a developer while
you're developing and that the way you started
more or less you can just open up that pain
and just go yeah we put it in between quotes
if you look on the the the right side the given
when then before I'm going to implement I need
to have my tests planned what are the tests
detailed what are the steps the setup given
the execution and the verification I think on
the page scripting side you also need a plan
uh the fact that this thing failed was not due to
missing plan but I I really planned all the steps
uh actually my recording took two or three times
to really get the right one because you forget
something whatever if you don't have a plan and
just sit down it it it becomes a little bit uh
inefficient next to the fact how do you know if
your colleague A made some scripts and B made so
what is the coverage are we not duplicating are we
covering things well enough yeah uh nevertheless
it's easier to step in I fully agree uh test
isolation anybody familiar with test isolation
in execution if you have a yeah the light put up
the light uh with test automation the coded test
we by default run it in isolation so every time
something finishes it it reverts and yeah and uh
with this one you know data sticks in the database
and you should clean it up somewhat you can use
pre-built fixure but then make sure where you run
it that it's going to uh be useful in the sense
of that it's already there it's existing and as a
last two one yes you can run both in pipelines and
web client execution is always slower than test
automation okay so I want to talk a little bit
more about how do you run these page scripts in
the pipelines because the first time I saw that
running in the pipeline it was quite eyeopening
for me this what you see here on the screen is
running a traditional test in the pipeline you
you are developers you would most likely figure
out what went wrong here because you're you're
comfortable with pipelines but you know who isn't
testers and consultants if they see a screenshot
like that they don't like it page scripting is
using well in the pipelines it would be using a
note package called BC Replay now I did put the
link up here because we're developers we like to
tinker you can go and check this out this is what
you would use to run your page scripts but I would
say that maybe you shouldn't because I do want
everyone to actually transition to the managed
CI/CD solutions like Algo go for GitHub uh Alops
or Alpaka and they are going to implement the
support for us to run paid scripts in a pipeline
however I still want to show you how all of that
works you don't have to really take a look at at
the code here this is all in the repository which
we'll share later but let me just show you if I
run this script what's going to happen is that
a couple of browsers are going to spin up and I
have to switch to my my monitor for you to be able
to see that what's happening here is you can see
that four browser windows have uh spun up now you
wouldn't see that in a pipeline but this is quite
visual for us right now and I can show you I think
this is the one we were executing earlier no this
one was it's basically just executing the same
page script we saw a couple of times now that's
not too interesting what's interesting is what
happens when all of these scripts are run when
your scripts succeed or fail the BC replay tool
is going to offer to you a nice little report that
you can run with this npx playright show report
right as soon as you execute this command it's
going to serve an HTML report let's wait for it
to open up so I've had four different page scripts
in a folder that I've run with BC Replay two of
them passed two of them failed if I look at the
one that that has failed here's the cool part for
me you get a video of what actually happened there
which means as developers you could read the code
and figure out what went wrong but consultants can
also now troubleshoot when these scripts go wrong
in the pipeline because they look at the recording
and they can see oh okay maybe this is what what
we have to fix because here's another thing this
ugly looking link over here if you click it it
opens up Business Central with that same page
script loaded and then what you can do is you
can rightclick one of the steps and you can say
run to here and it's going to just execute these
steps and then you can manually click through the
rest to figure out where did we go wrong what do
we have to fix and again consultants can do that
it doesn't always have to be a developer that's
also what you can share yourself you can share a
link from the page scripting in this this the same
format why was this whole running page scripts in
pipelines so eye opening to me it's because
of the video here when I saw the video I was
like okay consultants can now troubleshoot failing
pipelines that's great but then I started thinking
more ahead what if we could use this video for
instructional videos right because what's the
problem with instructional videos we usually have
you create a video everything looks nice but then
in a couple of months your application changes
you move actions around you move fields around
and your UI doesn't look like it looked on the
day when you recorded that instructional video
what if we could use page scripting to create
those instructional videos right and then when
our UI changes we would just run these page
scripts again and we would get a new video
out of it that we could use wow but then getting
enthusiastic again like this this is really kind
of a dream for me because why even stop with
instructional videos what about documentation
documentation has the same problem we create the
perfect word document with screenshots with all
the highlights six months later it's useless
because we moved things around right what if
we wouldn't just take a screenshot and put it in a
word document what if instead we would say in this
place take a screenshot from the page script at
step six here put a screenshot from page script
at step nine right and then again six months later
when we want to update our documentation we would
just have like a magical button that would run all
of our page scripts and our documentation would
be updated now I I know I'm getting a bit ahead
of myself but you know page scripting today it's
making testing not boring but tomorrow it could
make documentation not boring as well that would
be that would be quite cool for me wow but that's
that's some some ideas that I have for the future
microsoft also has ideas where they would like
to take this tool what they shared on one of the
office hours is a couple of investment areas that
they would like where where they would potentially
see this tool evolving so I've put some of them on
the slide here ga for current scope support simple
added scenarios capture initial context localized
step descriptions so maybe Luke if I ask you
what's your pick from the ones we see here well I
think the the second one support simple editing i
mean if you want to give power to the functional
people i fully agree i mean if we had more of an
editing support maybe during the from the lab
session we could just remove those middle parts
out and the script would run again then there was
another pillar completeness of current uh features
manage suite in UI manage parameters in UI YAML
documentation capture extensions involved in
script and increased capture support for controls
and highlights what's your pick here the second
one that was the one I wanted to mention manage
parameters if you want to hand over things to
the includes that's a challenge at the moment and
surely if you create them as a us as a functional
user I kind of agree with parameters my pick here
however would be the managing suites in UI because
right now you have to import these paid scripts
one by one and run them one by one i think for
functional consultants it would be much easier if
they could uh import five six seven different uh
scripts and then manage that through through the
BC UI the next group is additional features save
and manage scripts on the server custom replay
speed allow testing for values and data sets
cross roll processes support multitasking feature
and running scripts without client your pick yeah
the second one both in in this tool and in the
replay of the video i mean the video goes voom and
the replays well it would be nice some steps that
you can really follow it i have to agree with that
one because it does kind of fuel my dream dream of
we could use those videos for instructional videos
but I do also want to highlight the saving and
managing scripts on the server i do think that
YAML files they are best managed if we put them
in like a repository yeah in a git repository so
we can have version control but for consultants I
think it could give them more power if they could
also manage these files on like a UAT server
at the customer finally we've got additional
use cases using the tool to document processes
possibly with screenshots conversion to VCPT
or AL test cases and using tool for templating
or macros for common user processes your pick
yeah BCPT i agree with the other one but still I
mean create B forbake showed a nice example that
actually we could record as users what we're doing
daily and then transform that into BCPT to to do
the load testing i have to mention screenshots
that would really be my dream if we could have
that magic to update everything by just clicking a
button and it runs through all of these recordings
so this was a bit on on the page scripting you
know this this wave of freshness that it brings
to traditional testing um if you'd like to know
more there's a Ryopa webinar there's the BC launch
event there's also a session from Microsoft
uh later today where they will talk more more
about it 4:00 so please go there but that's not
the only way of fresh news that's No no no no
no no there's more this one's much newer so page
scripting has been around for like 18 months or
so datadriven testing that's something we didn't
have before mature languages they did have that
we didn't and what is datadriven testing in
like the short sentence what it allows us to
do is that we build one AL test but we can then
run 18 different test cases which we can keep in
a separate file which again is going to make sure
that developers are not the bottleneck why did we
get datadriven testing of course it's because of
AI everything right now has to somehow tie into AI
so why was datadriven testing so needed so much
for AI AI test toolkit you saw some of that during
the keynote but if I would explain that in my
own words I pulled a couple of slides from a
different session that I've been doing throughout
the year the how to be a prompt engineer where I
was talking about how do you build a good prompt
right but once you have a good prompt how do you
ensure that that prompt is going to stay good
how do you do testing so I I had this example
of an AI feature something very simple that a
user could come into Business Central and put
into the box determine if a discount of 12% can
be approved for an order value of 8,000 if you
think about it if this is an AI feature how
do you test that when a user can come up with
so many different variations of these questions
well that's exactly how you would try to test it
you would try to write down this one one sentence
determine if a discount of 12% can be approved
for an order value of 8,000 and you would say the
expected result is reject and then you would try
to come up with many different questions right 7%
6,000 approve 17% 20,000 reject 3,000 8% reject
and you wouldn't only play with the amounts you
would also play with the wording determine if a
discount can I give is a discount for order value
is a discount acceptable right you can even get AI
to propose even more questions that you are going
to use in your tests if you're trying to support
a different language you would even have them in
multiple languages and with datadriven testing you
can now package all of that into a JSON f JSONL
file where you put a question and the response and
a question and a response and a question and
a response and Then on the AL side of things
you only need to build one AL test it would look
something like this the the important part here is
the AI test context in the first part of your test
you would pull out a question and the expected
response from that file that we saw a moment ago
then you would execute your AI feature the verify
allowed discount with this question from the file
which is going to give you an actual response
and then in the end you only have to kind of
assert if the expected response is the same as
the actual response so you only have to build one
AL test but it can execute hundreds of test cases
which are in this separate file which doesn't
have to be the responsibility of a developer
so we really need datadriven testing for AI i
think this is what it was built for yeah so this
AI test toolkit by the way you can download it or
install it from app source and if you're using a
container it's part of the test tool kit settings
but however AI what AI I mean let's not only dream
about AI it's not just AI as Tina started this
is about datadriven testing yeah so if we look
at it from AL what we used to let's call this the
datadriven test toolkit So you can do this i mean
you can create one flow but have multiple inputs
anyway that's not depending on whether it's meant
for AI of course they need it there so let's
have a little look at what datadriven testing
is this is about testing or describing as you
showed in your case one main flow and the rest
is actually gathering data getting your context
uh for both input and output checking yeah so
um if you need to build only one let's leave
the others to get the input created right so
when you run it you need to collect the input
and you need to collect let's say the expected
output and checked against that one so in a simple
example back to my test plan of three cases where
we add an extended item with extended tests to
assembly order you might recall those three test
cases there was a number one i don't know if you
can read it i guess so there was a number two on
my list and uh there was a number 67 on my list
and if you look at the code it's almost the same
we could go into the details but the details are
parameters that you could define as input so this
comes together development work into one case with
flow and as you can see here we have the input
part like on Tina's example also and we have the
output part or let's say this is how you gather
the input part and the output part by the way
I'm using like uh uh also in Tina's example the
uh AIT test AIT test code unit and it provides
you with a number of things already uh out of
the box but you're able to build your own things
around it if you want to do it somewhat different
feel free to do that of course so this means that
in my example I have three definitions of input
yeah I've got one main stream and this is the
definition of input by the way it can be in JSON
line format or in uh YAML yaml has the advantage
that is nicely grouped json has also some examples
but you can logger lines probably that makes it a
little bit more challenging so shortly in a demo
um so let's move here um I have here an online
environment by the way I normally work in
containers why online there is an issue in onrem
to run this tool you get a a kind of permissions
error uh we're in discussion with Microsoft on
it so it's going to be fixed but at the moment
it only runs in an online sandbox you cannot run
any tests by the way in a production environment
so if I open no not the AL but there is an AI and
it's called test suites part of the AI test tool
you can define a suite i already defined one um
and in that suite you can uh let's say list any
of your code units with those u uh methods by the
way one test method per code unit because you link
to one data set um so um in this case I created
that one flow and I linked to that one flow here
the data set the way you do it is go to input data
set import data set and here you can go and browse
through it or throw it on and put and you see I've
got quite a number i've actually done the whole
uh conversion for the whole case and then this
data set can be used those three sets as you saw
on the slides and now I can run the test and it's
going to execute and on the left side you will see
the result um what is good to know about this in
the background actually it in injects in the AL
test toolkit you might know that one already uh
AL test toolkit it injects here a suite for this
run and uh for this code unit actually and for
each it expands it per data set as you can see
this is where it used the first input the second
and the third input from the data set okay let's
go back um so this was a short demo on that one
and yeah the thing is what I already said this is
actually a group of nine tests yeah so I created
given three sets the the the code and I'll ask
my QA colleague to provide the other one so then
the whole set becomes nine uh sets yeah okay i'm
not going to demo that one uh if you compare the
two with each other of course it's still or again
a programmer that needs to be involved but I as a
programmer as a developer I don't need to do the
whole work i can leave the rest to somebody else
so I can come up with all the flows and what the
varants are is decided by a functional role okay
um regarding the uh uh pipeline I just said that's
a challenge now because of the pipeline will be on
prem and there's some uh issue at the moment with
permissions and of course um you run each test
in its isolation and then the next one cleaning
up between the two code units takes some time so
this going to take somewhat longer than we're used
to in the traditional way but I gather that we're
going to tackle that or get that tackled of course
now how does this all come together how does it
all come together right so so like we mentioned in
the beginning we introduced these two additional
testing practices so page scripting which can be
done by consultants and datadriven testing which
is partially a developer's job but partially
someone else can add these test test cases so
before I I kind of explain the story how does
this all come together for our organization I want
to first make it clear that I work with different
partners some of the partners we kind of build
a feature and then immediately we build the test
automation for it so a feature test feature test
feature test those are the partners which are not
going to benefit as much from these additional
testing practices but then on the other side
we also have partners who kind of create all of
the features and then maybe sometimes they test
something and those are the partners who are
really going to benefit from all of this coming
together so how it worked traditionally I as a
developer I would kind of create a feature right
and I would pass that feature to to a tester right
and a tester tester would try to break it see if
if it works if it doesn't work if it doesn't break
then that feature is okay and they add it to the
regression testing list and then everything
happens again as a developer I create a new
feature I pass it off to the tester the tester
again checks if everything's okay and if it's
okay they add it to the feature to the regression
testing list and when we actually try to do like
the the new publish the new deployment we have to
go through the whole regression test list to try
and test everything out um to see that nothing was
nothing was broken eventually we do get some time
carved out for the developers again where they can
take a feature off the regression tests and they
can create the test automation for That's why the
star turns into a gold star the problem however
is that we have two additional features added to
the regression tests and another gold star and
another two features that are untested so we start
to drown in these regression tests and that's the
situation that we always kind of try to avoid this
new way of working that we have now goes slightly
more like this as a developer I still create the
feature and I still pass it off to the to the
tester but the tester doesn't only try to see if
the feature works they also record the page script
for it right that's why the star is now a blue
star now of course these page scripts they're not
as uh let's say as efficient as fast as AL tests
do want AL tests but the fact that we now have a
lot of blue stars in our regression tests means
that when the regression testing period comes
around we can only execute those scripts and we're
done much sooner of course our end goal is that we
turn these blue stars into gold stars but we don't
have the time to turn everything into a gold star
and having blue stars helps a lot now how we kind
of manage that is that we have something called a
test overview this is not the test overview from
from our actual organization because that would
look super messy but imagine a test overview as
a list of all of your features i've listed here
some that you will all recognize so create sales
order post sales invoice create purchase order
like all of these features they have a certain
status right what's their status when it comes
to test automation some of them are gold stars
they have AL tests that's what we want that's
what we're looking for but not all of them some
of them have page scripts right but just because
they have page scripts that's not the the end goal
for that feature that's why we have another column
called target so where are we going to take this
feature once we have some development time ready
now from page scripts we usually want to go to AL
tests but sometimes from AL tests we might want
to go now to datadriven testing to be completely
honest we don't do much with datadriven testing
partially because the AI test toolkit was released
last month and partially because we still have to
go through a bit more upskilling so that we
can recognize which features are a good fit
for datadriven testing one example that I put here
is posting sales invoices like the the VAT posting
you can have many different VAT percentages
different VAT posting groups and that all ends
in a different VAT specification that to me sounds
like a very good example where I can have one AL
test but then all of these test cases that can
be created by by the consultants by the testers
now because we don't have enough time uh to create
all the gold stars that's why we also include this
column of priority right so when we actually have
time for the developers the testers decide this
test this feature should be picked up first maybe
because the page scripting is way too complex it's
too brittle it's breaking too often that should
be a high priority for us to turn it into an AL
test and I really wanted to show you this test
overview because it's kind of showcases that it's
not one tool that's better than the other tool
that's better than the third tool it's all three
working together we start with a page script but
we don't end with a page script we continue to an
AL test and now we'll continue with some of the
AL tests that will turn into datadriven tests and
now I think it's maybe time for a quick recap
close to the end I guess so looking back what
we discussed was let's say testing as such and
the huge effort you have to put in regression
testing if you do not automate it yeah uh looking
at those two charts which I also uh reference to
manual testing is short running the value of is
only at that time and the next time you have to
do it all again while the automation and that's
part of the what we're adding today with the
let's say let's scratch the boring yeah the the
fun part well the the fun part also in in saving
us a lot of repeat repetitive work uh is that we
can enable functional roles to also get included
in the automation both through page scripting and
to through datadriven development or datadriven
testing if you look at it this way in this graph
let's say in the traditional one the right side
is the biggest load is on developers although I
said it is a functional exercise in the end but
with page scripting it's tends to turn the other
way around to the uh functional roles more and
with datadriven testing you could say there's
a kind of balance where maybe development is
way much less than before but you give the power
to the uh QA you could come up with a test plan
with nine cases in my case but later on they
could actually find out we have three four
five extra and it's just a matter of updating
the data set um so take that home discuss it
um spread around and yes I think this is a good
way of looking at it we'll never get there in one
day uh we want to get somewhere for next week and
then the next month whatever set up a plan what
you're going to do which options you're going to
use and yes I agree the goal should be if you have
page scripted tests to really automate them in the
end but I guess and I think maybe that's the next
project to get that into AL code right having AI
helping us to create the AI ones so as a summary
testing is still needed of course and maybe
that's a very open door well is a very open door
uh I think And I hope you agree that test plan is
still important because in both or all three of
the cases you need to know what what you're going
to do page scripting is going to give control or
putting a load on the QA side and uh DDT gives you
the benefit of both yeah making it much easier to
spread the work around the team that brings us on
to the end I guess i guess quite some time left to
get some questions um as mentioned every uh the
whole code is to be found on this GitHub repo of
course the link is behind it but the the slide
deck will be shared and uh oh yeah what was this
last time oh yeah this week during the webinar
uh sorry the the workshop we had this workshop
on creating a test plan from user stories by
creating a rightful or a useful prompt and
at the end we asked the whole group please now
create a haiku from your test plan story so we
said to them there will be a winner so we have
two winners actually one winner and one beside
everybody you could say because of the context but
the winner for the workshop haiku competition is
uh Bula Sinis or Sanji sorry uh volumes rise and
fall bulk artists must not lose track integrity
wins I don't know what the the user story was
but we like this very much and then another one
getting emotional And this was one actually way
beyond what we were doing but we liked it very
much why must I test it it runs fine for me only
or only for me that's the buck I missed so both
can come up to us and they we promised a price so
you'll get something so we're getting to the end
what are we going to do we still have a couple of
minutes we have too many time for questions and
we have we have only four t-shirts well I don't
know could we do something else yeah i don't know
what what's happening i don't know [Music]
don't show
[Music] the [Music] la
so um where did you go well I went I went into
my lab uh this is a nod to to Vincent and all
of his amazing from the lab sessions uh right but
I took some time for the past few weekends to go
into my lab and try to see if I can make that
dream that I was kind of announcing earlier a
reality right what I was trying to do was I was
trying to see if I can get more use cases out of
page scripting if I can get paid scripting to not
only make testing more exciting but if I can also
get more out of it because with paid scripting
we already talked about it's using this node
package BC replay where you throw in a YAML file
and what comes out is a video so if I show you
this video again I'm just going to switch to the
one that passed you know here here's the example
let me play it the problem with these BC replay
videos is first this this is not a good quality
but the bigger problem is that it it replays
way way way too fast if you would use this as
an instructional video I don't think there's a
single person who's able to follow along what's
happening here yo you I don't know where are you
heading well you know when I was looking at this
uh I went a bit deeper into what VC Replay
is so let me just get this working again
yeah so BC Replay under the hood actually uses
something called Playright playright is a very
common uh framework used for test automation
well the UI automation of of web apps it does
the exact same thing as the BC Replay did for us
you throw in a Playright compatible script and it
gives you a recording but here's what Playright
can do on top of that it can highlight clicks it
can change replay speed it can capture screenshots
so that got me thinking can I use playright can I
use these under the hood parts to get more value
out of out of my page scripts did you Did you hook
the Microsoft feature i did some experimenting
so here's the video that I've created now with
putting some magic into Playright let me put this
into full screen first of all oh you don't see it
thank you for the reminder so first of all it's
better quality but that's not the the biggest
added value the replay is now slower and I'm
highlighting clicks that have been executed now
if I throw this to to like an end user they might
be able to follow this instructional video as it
goes through and shows you how do you set up an
item for autom uh for the extended text feature
but you know like I said why stop at instructional
videos the next thing that I've done is that I've
created a bit of a documentation for this feature
i have this business central assembly order with
extended text guide which yes has this video
recording but maybe you're a person who doesn't
like to just watch video recordings so I also made
a step-by-step process where you log into Business
Central this is what you have to click you
navigate to items you create a new item you select
the template you configure the item settings and
so on all the way here to the last step where we
enter uh the item into the assembly order now
like I said before here's the problem with
these documentation uh documents let me install
an extension that I've created for this example
let me go to extension management
i call it update UI page script
so let me install this one
okay and let me navigate to one of my items
so if I show you the screenshot here you can see
that this is how the item card looked like all of
these fields available this is how the like the
fact boxes looked like now with my new uh with my
new extension installed there's far less fields
here the picture has been moved down uh the the
[ __ ] boxes look differently i also changed a lot
of the things on the assembly orders i moved the
actions around i moved the sections around because
that's ordered again well I will try to but this
is this is what all of you are going through
you're changing your UI but these documentation
uh sides that you've created get obsolete so
wouldn't it be cool if we had this magical
b button that could update all of it well that's
the magical button that I tried to create um I put
this whole repository on on GitHub it's highly
experimental the playright docs magic but if
anyone wants to kind of navigate through what I've
been doing this is my magical button update docs
with my script uh that's now Playright compatible
and if I execute this we will see the same thing
you've seen before a browser will pop up and
now it's starting to record things but it's also
highlighting things that I've clicked things that
I've inputed the the buttons that I clicked and
because we have to wait this one minute for this
whole recording to go through I'll kind of narrate
what's happening so we na uh navigate to items
we click on the new item we select the template
we show more fields we enable the extended text
we enter the description into the description
field this is the new item card then yeah this
is the the UI how it currently looks in Business
Central oh we're now navigating to extended texts
we're going to create a new extended text give
it a description give it a certain line and now
it's going to go out close all of the pages down
and start navigating to assembly orders so it goes
into the assembly orders it creates a new assembly
order goes into the type sets the item and finally
puts in the item number and now everything's going
to close down because the the script is finished
okay so we re-recorded everything with the script
that I already had prepared before now if I
navigate you can see that this is the screenshot
in my documentation all I have to do is press
F5 and now you will see all of the screenshots
in my documentation have been replaced with new
screenshots that still highlight everything that
was clicked but it now it's I don't have to
spend even an hour collecting new screenshots
putting them in i just run all of my scripts that
I've created and with a refresh everything's done
so testing is no longer boring but documentation
isn't either wow the way but but wait thank you
so so can you can you just put a pull request
this in a pull request for Microsoft or I hope
so i think we kind of have to all look into the
direction of Microsoft and say can we maybe get a
bit more love into page scripting instead of just
AI and hopefully this becomes a reality like the
the way I imagine how Microsoft can do this for us
is if we first take a look at the DAML we've been
seeing today what if there was just a simple new
property i called it slow-mo because that's how
playright calls it a property where you specify
when you click on these actions uh it should be
like a second 1.3 seconds delay between you
execute the next section so it's a bit more
followable on the individual steps we could define
that highlight through right highlight what you've
clicked highlight what you've entered on
top of that what if there was a property
called screenshot name where you could enter the
screenshot name and it would save that screenshot
into a certain folder that you can then reference
when you're building your documentation documents
up and like this is the YAML view i wanted to
show also how this could be part of the UI for
consultants to be able to do the same thing
this is the properties page of one one of the
steps well what if there were just two additional
buttons one where you can say this step I want to
have highlighted and another one where you could
supply the screenshot name and that would save
the screenshot whenever the recording is at this
step so I really wanted to kind of turn this this
this dream of the future of documentation into
a bit of a reality and this is also kind of the
the end part of of the from the lab section and
with that I think we come to the last part which
is questions well just before questions Thank you
a big thank you to all of you there's a question
out there i think you should just be able to
talk into Yeah well we receive we've got three
t-shirts available i have one question about uh
page scripting this morning uh we we saw several
things about for example variable condition and so
on uh I think about when the user um intercept the
error but this error is fired by error info object
and this suggests to user uh for example open a
card and fix in this case the page script can go
on to the steps there's an issue with there's an
issue with errors and this specific one I don't
know but recording errors and replaying This is
still a problem so the exceptions unfortunately is
at this moment an issue in the page scripting this
specific one with the error info I must admit
I didn't try it so I'm not sure so you would
expect pushing the button that it continues with
the rest not sure about that if you have let's
say oldfashioned error messages like on the on
the bar underneath the bar etc that's an issue
at the moment okay and uh and uh if I intercept
this error and uh for example in in conditional
include different YAML file yeah there is
possibility that you have conditional steps
what is going to follow after that okay not on
the includes by the way it's not possible based by
uh a conditional yes no okay no okay you throw i
throw one two one two now come on another question
hi i've got uh two questions two possible one
shirt yeah sure one shirt um the first question
uh you showed us you can work with playright in
combination with uh page scripting uh do you know
whether it's also possible to work with Cyprus
with Cyprus no idea what I've shown here um I
didn't really take the the the page script as such
and feed it into playright that that doesn't work
so the way this actually works is playright throws
your page scripting recorder into business central
and business central runtime is executing these
steps i went through a bit of vibe coding to to
get myself a bit of a script that transforms
the page script uh recording as such into a
playright compatible script so there's no there's
no direct way for playright which means there's
also no direct way for for any other framework
i see that was one uh the the second question is
uh as far as I know uh page scripting is still in
preview right yeah do do you know anything about
uh when it's going to be Fan Nikolola mentioned
this morning that they're getting close to GA
so meaning that it's going to be out actually
if you go to the session from Vasil I forgot
the other names this afternoon at 4:00 they
were going to show some things actually a
couple of things that we didn't show yet so go
there yeah one two ah both bad one here you go
Hi you showed um the other way around okay hi and
you showed that you split up the page scripting
file in in different parts and you said that
there's an issue with the v passing variables
from this yeah is there a workar around um well I
think in in the file yourself you can do a little
bit more than we tried so far uh in that session
they will also talk about that so go there if you
want to learn we need to learn too i've I put
a question on yammer already on that they said
go to the session so that's it for now uh and we
have one shirt remaining yeah you throw I throw
again one two no come on you throw I throw here
you go and now one far off i'm just looking do I
see somebody has hand somewhere there whoa um yeah
I probably have a pretty simple question uh I'm
sorry if I missed the information in the session
uh I wanted to know um relating to datadriven
testing um you can import data sets do you have
to create the data sets per hand or is there an
easier way to uh provide data sets for AI testing
you can use GitHub copilot yeah that's actually
Tina signaled me you have to be fast i was
talking too much that was what I wanted to show
once you have three variants or whatever then the
next one is relatively easy using GitHub Copilot
okay yeah is that enough of an answer yeah
it's okay are you the first one that throws
at the same time as I do yeah another question
no shirt sorry up there oh there's going to be a
long throw where up up whoa you have a long leg
to reach you one two oh oh back to you almost
you have to walk down hello hello yeah hello hey
hello um the two qu question that I mention um
when it comes to manipulating a page script many
uh sections contain the property runtime reference
uh I've seen in my testing that manipulating this
especially when it comes to conditional statement
it can break scripts but I cannot find any clear
documentation on why it breaks yeah there's no
documentation at all i don't know either and
it's trial and error i think like I'm I'm not
sure if YAML documentation is part of the like
things they have to get sorted out to call it
GA but I think that's going to be part of it so
whatever the investment that they currently are
putting into page scripting which then I expect
would kind of surface around the next release time
I'm hoping YAML becomes part of that so we can at
least understand what's in there we can only hope
well to to add a little bit to that it was a bit
the picture like AI AI AI and page scripting is
going to suffer from that but they really are
adding something now and that's what they're
going to present so and there was some statement
on that documentation was going to come on that
yeah um and there is something I would like to
mention when it comes to page scripting and I do
not know whether it's intended behavior or not a
page script does not seem to care about whether a
field is visible or not it cares about whether a
field is exists not sure whether enabled matters
so if a field is invisible on a page but it still
exists within the code it will still validly put
uh data into this field i'm not sure whether
that's intended behavior or not when I tested
it was working like you expected so I'm not sure
about your statement whether that depends or mine
whatever on the version u let's get in contact we
did an explicit test because I mentioned a tool
like Ranorax those visual general generic visual
tools have problems when something moves so what
we tried and one of the reason to move is that
is very costly we we we tried like if we remove
a field yeah if we remove a field it fails if we
move a field field it just continues because it
doesn't need to know where it only addresses so
this looks different so let's see look look to
to maybe and if I hope I'm I and I think you you
hope too that I'm right because that what you want
yeah okay look yes can I add to that yeah please
yeah uh so we noticed the same behavior back in
in December um but we sent like I I remember
sending a huge email to Microsoft and it does
seem to to behave better in uh the the BC27 so
the preview version which you can get um maybe
they fixed it that that's why Luke didn't have the
the same no I tested 25 already but nevertheless
that's not a discussion let's see yeah I got
no shirt so sorry and now I failed to to catch
that's it we're on time I guess yeah we're on
time so again thank you all for coming and you
