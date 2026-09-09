# NAV TechDays 2017: Application SaaSification

- **Source:** https://www.youtube.com/watch?v=m9m5ZYAWGmg
- **Video ID:** m9m5ZYAWGmg
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 75m32s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

welcome this session about applications
education my name is Mike I worked in in
Microsoft since 2002 various roles
various projects for the past year have
been working on this application being
where we are focusing on application
classification significant so what will
we be talking about today well obviously
what is application specification we're
gonna show some examples from the
product then we're gonna sprinkle it
with some demos of how you can apply
certification using extensions so that
you can make some cool certifications as
well and hopefully at the end of it all
we will have some time for Q&A so we
would like to talk about what we put
into it the rules the guiding principles
for applying simplifications on a
existing product but before that Whitney
on stage is also muscle introduce
yourself hello my name is Thomas pimp Oh
I've been a software engineer in
Microsoft up one and a half year most of
my work revolves around bringing nav
functionality to SAS and also
simplification with the aim of improving
the user experience today during this
presentation I'm gonna show you a couple
of the sious if occasionally empal in
the form of extension with you but
before that Henry is going to introduce
the concept of certification and how we
at Microsoft have dealt with it in the
last year yeah thank you so application
certification is not so much about
refactoring functionality inside the
product per se but it's more about
refactoring the user experience
or simplifying the user experience so I
came across this presentation I attended
at one point with dr. Nilson who was
famous for UX and some thinking about
that and he mentioned this example of
the airplane industry during the 60s
where they had some severe crashes that
were all caused by human error so
obviously they summoned their
engineering team to look into this and
the engineering went through all the
individual controls inside the cockpit
you know how that looks but they
couldn't really find any bugs in the
individual controls as such but then
they started to look at the context of
how the controls were actually placed
inside the cockpit so you would have
things like this is your captain
speaking and dump all fuel and they
would sit right next to each other so
you can imagine right I have to take off
you would go this is your captain
speaking
oops we just accidentally down to all of
you so obviously they started to look
into how they could divide these
controls in a in a better way and
basically make the experience much
better and much safer anyway to some
extent application certification has
some similarities that this is not we
don't dump airplanes from the sky but in
terms of how we make a better product
for our users so it's not about
refactoring the underlying functionality
but what this is is not about is
education in general it's not about
taking the whole product and then turn
that into a solution like with the
platform and as we saw this morning at
the keynote
basically doing all the infrastructure
that's not what this is about
so we want to make the product more
intuitive easy to use and approach and
we went through an exercise of reducing
number of fields that are available you
can see one example here on fixed assets
where we reduce some of the fields that
the general fests have it's also about
becoming productive
stuff our users making the users feel
successful maybe also introduce some
beta arrow dialogues and then it's also
about introduce guidance like adding
notifications and just to recap on
notifications it's it's a less intrusive
way to basically hand the users and
guidance in the same context that
they're in and it also means better
feedback during data entry and faster
recovery from from mistakes it's also
about looking at processes that we can
shorten or make even simpler here it's
it can be using a wizard or assisted
setup it can also be offering different
capabilities for the users in this one
image up here it's like when a user is
creating a sales order to Iran either
start now from within the sales or they
can actually go on create either
purchase orders or purchase invoices but
purchase orders for different vendors
and different items and finally we also
think it's about the ability to create
different experiences reusing the same
optics so well now rather better we
start so if we look at the new part of
this this is basically standard nav when
they say fob started the x-axis is
basically the full application feature
set and then why is our aspiration we
wanted to we think it's easy to use but
we want to make it super easy so with
that in in mind we obviously had these
aspirations and ambitions but as always
reality showed us that
it's it it slowed us down significant
dates it was a lot of work actually to
make these changes and that that's one
of the interesting parts about making
things simple is actually a lot of work
so where are we where we are now this is
roughly where we at with Tenerife scope
we have I put up something here called
certification level one I'll come back
to that what that actually means so but
in the essence of time we actually had
to cut back level one is the lowest
level of our path so it was so to say so
that's what we're currently yet and then
just a quick representation of the
feature scope not sure you can all beat
this but I won't pay too much attention
so just bear in mind that this doesn't
represent the actual product because we
keep adding and keep changing what we
are implementing so what did we do so we
use experienced years application areas
we've been through a lot of existing in
AV functionality so this was not about
again adding new features we're also
working on making it easier to add
certification using extensions that's
also an ongoing effort with the new
developer experience and then in
collaboration with a select set of users
and program managers and our UX team we
also formalize the process around sorry
improving and simplifying the
application so in this image what you're
seeing here is the program managers heat
map it basically shows what we should
start with when we took on this mission
what are the most important features we
could possibly start with and then
engineering
we took a stab at how we couldn't build
a system to basically manage this
transformation for each of the features
included take them from an on-prem put
them into a solution so we broke that
into three layers in summary basically
this is what basically adds up the
journey for for certification in this
part of it at the first layer we have
the experience just as I mentioned they
set the experience for a company for
each of these experiences we have a
number of application areas which is
also the next layer that are tied to
them to make up a feature set like we
had and in the heat map before an
application areas I mean it's it's a
familiar concept but it's basically a
taxonomy for mapping our controls and
actions to the various experience and
that way sale of basically assisting
pages to much more specific scenarios
that we also identified as part of this
process and lastly the certification
guiding principles with the three
different levels in it was basically
done for us to apply further
simplifications and so just to start
with experience use inside the product
you start by selecting either basic or
sweet and then we based on that we map
these application areas to that given
experience so when we look at that
the basic
roll Center for a business manager in
Dynamics 365 it's a leaf we had these
two experiences two basic and sweet and
here you can see the raw Center for the
business manager it has less
functionality if you compare to sue the
sweet one for each feature this has to
be determined to best support the users
because there's always the risk that
Ross and I can just be replaced that
with features and feature diagrams and
whatnot but again at the it's it's still
about making you simple while still
offering sufficient functionality so a
quick recap again for the experience use
used to define the functionality
available per company for now we
introduce the two experiences in order
for this to work you have to map
application errors to controls on the
page using tacking and then run time the
application basically pass on a string
to the platform with the controls that
I'm able and then we return the set of
controls so let's just quickly look into
application areas you can have any
number of application areas and Tomaso
will shortly demo how you can add these
application areas using the extension
and on the team a lot of our time went
into actually checking the various
features for either basic and sweet to
begin with and later on we also added
more of these feature tax so for
instance on this one we have pre
payments on the sales allah pays we
simply add the tech prevalence it's done
using spreadsheets and data program
managers and then they basically decide
what you put in and then they decide
which controls we should make visible
and then in inside the product we have
like in basic you have no prepayments
oops and then in in sweet you you have
this so in other examples so we added
application areas in experiences it's
basically we be if you look at the
filter types on a sailor for instance in
this case we have the types so in the
old one you had all the different line
types listed then when we when then
inserted we had a basic experience that
basically filtered out what is not
included in basic like fixed assets
rights and charges and then in the sweet
experience we have everything available
that we had already texted this is one
way that we can use this application
areas to basically create a more sort of
user friendly data entry experience
because you now you can only see what
you actually can work with instead of
having everything you can basically
filter out things so with that in mind I
would like to pass it on to you so
before I show the code I'd like to spend
a couple of words in regard to what's
the state of application today well what
am I going to show you now it's still a
work in progress and as such does not
represent it on state of the application
and as it happens for anything under
development
it might be subject to change in the
future we have a plan to release it soon
but we don't have an ADA yet with that
being said I'm gonna jump to the example
in this example we are going to lay down
the foundation for an extension using
the application
area and we will do that by adding and
enable an application area extend and
experienced here by adding application
areas and modifying existing ones and
finally we'll be validating the
application area and the experience here
so I have a prepared solution in Visual
Studio code in the modern development
environment for those of you that have
been there was a earlier session today
explaining it but for those of you that
don't know about it it's basically the
place where now you develop the
extension beat you so in I don't know if
you can see the text back in the back
row but tell if you if you can't i will
increase the fontsize in this in this
example i'm the we are extending the
customer list at this point we are
adding at this point line set of seven
we are adding a new field the example
field which is followed by a series of
attributes and i want to point out your
attention to the line ten which has the
application area attributes to which we
have signed the example application area
that has been added by the by by this
extension this is very important because
if your extension failed to use
application area in any controls or
action they will not be visible if we
are using an experienced here at the
bottom of this on this file we are using
we are using the unopen page trigger and
we are we are showing a simple message
and we show them as a jolly if the
application area is enabled so now
before i show you all the groundwork
that's behind the experience here the
application area are going to run the
demo just to see it working
we're gonna see the code the rest of the
code it's gonna take a couple of seconds
so we got our message right before the
page is displayed for the first time and
when I press the okay we get the page we
get our example filled on top it's empty
because there's no data and we can go
back the code so how do you add an
application area that's done right here
by extending the application is the top
table that's very simple you just add a
new field a new boolean field and the
name of this field will be used in every
in the attribute that you want to type
with this application area and these
particular case the example application
there is a bit of an exception because
I'm using spacing inside it and you
might have noticed that paces are
omitted in the application area
attribute if I quickly jump back to the
previous example you can see here
example application is no space so now
our extension have an application area
but it needs to enable it in order to
work and that's done inside a code unit
of subtype installed like this one and
we do that inside the uninstalled hopper
company trigger again they called very
simple does nothing else than enabling
the application area if it's not already
enabled so so now we have the
application area but still our extension
will not be working unless we register
this application area inside an
experienced here and in this code unit I
have actually I will show you how to do
that so that is done inside the one of
them get experience application areas we
have different version of this of this
event
one for each experience here
in this case we chose to use the suite
because we want our overextension to be
visible inside the suite experienced
here and the the event shows exposes as
a temp record to the application area
setup table and the only thing you need
to do to enable the application area is
just to set it to true this event is
particularly important because it's
called every single time an experienced
year is reset and that can happen for
any reason it could happen because
usually switching back and forth between
application areas or you cannot happen
because owner of an upgrade and if your
explained extension failures - to
subscribe to this event do it in to
enable the application inside here then
it will probably end that will probably
end up being disabled another thing that
you might want to do inside these
functions is to modify the experience
here you can actually modify other
application area you might be for
example creating an extension that
extend the fixed asset in which case you
might want to fix us it to be enabled if
you are running your extension inside an
experienced ear they does not have fixed
asset enabled by default or in the
contrary if your extension is supposed
to replace fixed asset you might want to
accept to be disabled length world here
we are using we are subscribing to their
own validate application areas which as
the name suggests is used for validating
in the application areas inside the
unexperienced here why do you know that
to do that it's because some of you
might know there is no guarantee on the
order of execution of events that means
that what you have here what you are
doing here inside this function might
not reflect the final state of your
experience here you might have another
extension with another subscriber that
get succeed
that right after your subscriber and
disabled one of the application at the
time required for for your extension
leaving your extension in a state non
functioning state in which case you
might want to notify the user and that's
exactly what we are doing here at line
15 from 15 to 17 we just check if we are
in the presence of sweet then if our
application area is not enabled we just
display an error so to summarize what we
saw in this example we added an
application area on the app area setup
table by simply extending it with the
new boolean field we enabled the new
application area inside our unit of
subtype installed into an insulator
company and then we extended experienced
year with a new application area in
their own get experience sub area and we
also saw that in the same event is
possible to modify the experienced year
and that that event is very important
because gets called every single time
and experienced here is reset man event
in the system and then we validated
their application areas and finally we I
want to remind you to always start your
controls and action because otherwise
they will not be visible if you are if
your extension is working under an
experienced year I gonna give the were
quick to Harry thanks so yeah I want to
wrap up on application area so just some
some pros and cons it's it's nice to
have the ability to to tell you the
experience using application areas so
that's where it's it's very helpful it's
also we we can reuse the same optics so
we don't have to sit
different experiences using different
page objects for instance
some of the concepts basically mistakes
will happen it's it's a huge project to
take all these features attack all these
controls make sure that it all works in
the various combinations that we can
think of and obviously every single
control as I mentioned has to be checked
so for application errors you will have
access to this presentation afterwards
there's a link up here for the white
paper on the same if you're interested
so I want to talk about the application
certification so that the last part of
what we went into and we decided to go
for a bar which is about sort of adding
the final touch for these features in
terms of adding providing guidance
without minimize the number of controls
available actions and just in general
give it a scrub on the functional side
as well this this is not about the the
us part that was mentioned at the
keynote this morning you saw that a nice
new tenerife UX experience that this is
not related to it this is more an
attempt to to make the product more
light reduce the learning curve for our
users and in general make them have a
better more coherent experience when
they use nav especially for new walk-up
users to be consistent in that approach
that's why we we basically went about to
create these three levels to ensure that
we wouldn't have certain areas that
would only receive parts of it like we
wouldn't do the ribbon updates and that
part what we would do the ribbon updates
and the other one could be between sales
and purchase orders which would be maybe
a strange experience so to be consistent
we add
this and that then went in to become
part of the whole process of grooming
these feature areas sorry I have a bit
of a cold these days so we also really
discovered that engineering these the
difference between level one and level
two is a factor of a hundred percent in
terms at the time that went into it but
anyway let's let's proceed with the
individual levels so in level one this
is basically mandatory for dynamics 365
to know if otherwise it will not be
visible without these these steps so
again it's it's about adding the
application area to an experience to you
but there's also a slightly longer list
than I then I put up here but it is
things about adding the right permission
sets and map these to use the groups so
it's part of the plan when you open it
up be updated to help including tooltips
but there's also adding things to the
rows and as I mentioned what profile
should it be a business manager role
Center for instance and then we did a
lot of additional testing even on this
level of course so one level to go
slightly deeper we're also in this in
this case we're trimming back a bit on
the fields often we would just go into
show less mode we rearranged some of the
ribbon actions without hopefully
introducing too much intrusive changes
we all know that when you have a certain
pattern in the way you use the system
when we all of a sudden start
rearranging everything
it might even confuse users so with that
in mind we also introduce some basic
telemetry for most of our features and
this is telemetry and the usage of the
features is not about what people type
into our data as such
[Music]
so if we move on to the next one we had
the level three that's everything we
could think of in the bundle what we
thought into application certification
in around this time frame that could
obviously be more things we could look
at but the ambition level again as I
started out by showing you on the where
we at with with the different diagrams
we kind of realized along the way that
it was ambitious enough already
so from an engineering point of view
it's also about I mean you can see that
this is all the features a lot of the
features at least for nab that and the
capabilities within the team is not
necessary that we have all the knowledge
about all these different areas so it's
also kind of a journey for us to
actually we learned a lot of these
various processes and positive products
so level three adding more guidance for
the use of like assisted setup or we
thought it's also some examples here
like from fixed assets where we've been
didn't reduce the fields
ribbon simplifications as I mentioned
more guidance direct links for users on
the rows and we also introduced things
like the tools for instance that helped
users basically guide them to get
started with the system I also want to
show some of the assistance set up or
wizard examples so for instance my
gradient a user from another system like
QuickBooks was wrapped inside a wizard
making it easier to get go on also with
some instructions along the way
another example is sales tech setup
which is also possible to complete using
wizard and eliminating some
uncertainties as a new user
[Music]
it's all about giving them that sense
that when you've done it without and it
says you're all good then you have a
certainty that you are successful in
what you're doing and then just another
example is from from the fixed assets
where we have this again the
notification so user types in a new
fixed asset the notification pops up and
and ask if you would like to acquire
this fixed asset and then if you click
yes you start with this acquisition with
that some other examples is what I also
mentioned earlier this is also purchase
order which is also a good way for first
we announce to the user that you're out
of stock and then they can quickly move
in and and start their purchase process
so I also mentioned something about
reducing fields so if we look at some of
the principles for instance on a car
page it's all about thinking how we
design the information available for the
user what we show up front it's about
thinking of what what will the user
actually care about first and then we
promote these into the general fast tab
our field that we deemed less important
was moved in to show more additional
fields we also had a principle about
setting at the max amount of fields that
we should display and that that's also
about being consistent so now I want to
pass it on to you again somehow so
basically to show us how to apply some
of these principles using using
extensions
so earlier in our example we showed up
to lay down to make to lay down the
foundation the groundwork for an
extension to use an application area now
we're going to build on top of that
example and improve it by adding some
other specification element we're gonna
see how to add a notification and handle
the lifecycle of the notification and
we're gonna see how to an extension can
promote itself and improve the user
experience by using the video and
assistive setup pages again I have
another another solution ready for you I
will have to open it it's the same as
before it's just a new version which is
adding a new file the rest of the files
are still the same so this is the new
file I'm going before I'm gonna show you
the code I'm gonna run the example
publish it and and run it and we're
gonna see the notification in action
so we have the notification on top of
the page in the blue rectangle we have
some text to action the usual don't show
again action which disabled a
notification forever that we have an
example action that we click yet we see
a simple message like before and if we
go to the magnification page which is
the place where heaven moved in vacation
is an entry and where the user actually
enable or disable the notification or in
most of the cases re-enable it because
you might have have hidden it or
disabled it through the other action yes
and if you click the notification you
actually see it running here you can
test it and then we have a convenient
checkbox and filter on the side so let's
go to the code and so on top we have
some label which are used inside the
notification when I'm not gonna explain
those but instead I'm gonna go directly
to this part which is probably the most
interesting part is the yun Obon page
event on the sales invoice so and in the
body of this function we are making use
of this code unit called notification
lifecycle management this code unit is
basically a collector or well pers and
factoring method for notification we
strongly encourage you to to look inside
to learn it and hopefully use it if you
if you feel like it's useful and in this
case we are showing the creating the
notification with with a single code
which is created send local notification
it takes us first parameter the unique
ID of the notification and this get the
example notification ID is just a helper
function defined here at the end of the
file that returns a guity
and as a second parameter it gets a
record ID which is used to cobble the
notification with a specific record in
case you have multiple pages with the
same notification open and the third one
is the text that appears on the under
notification and the one after is is the
clickable text for the action and
finally we have the action itself which
is made of the code unit containing the
procedure and the name of the procedure
which is this example notification
action which is here at the bottom of
the file and so you might also notice
that I didn't declare any do not show
again action that comes with the factory
method instead here at line 25 we have
initialized notification this us with
the fault state this event your honor
your extension needs to subscribe to
this event in order to initialize the
notification in case if you don't do
that there notification might be
disabled if if the reason is that let's
run in the system again inside the body
of the function we make use of the
notification lifecycle management this
time we used the set notification
default state for current user that
contrarily to what the name suggests it
does not wholly set default state but it
also has a new entry to the my
notification page I know it's a bit
confusing as a matter of fact the first
parameter it's the ID again and the
second one is the the text in the my
notification page the third one is a
tooltip text and if finally we have we
have default the default state for the
notification yes so to summarize what
we're seeing our notification should
always be
she lies inside the oninitializing
notification with the fault state and
our way to set the default state is
through the set notification default
state in the notification lifecycle
management and I want also to remind you
what we encourage you to use and
familiarize yourself with a notification
lifecycle management code unit so
however you have another example which
is about using the video list an
assisted setup and in this example we're
gonna see how to island race in the
sister setup page and in the product
video page I'm gonna load now the other
solution
and like before I'm going to publish and
run it before we go into the code
sure we are in this is the setup page
you can see every every one of these
entries are assisted setup and in
particular the one here at the bottom is
the one that our extension adds I think
the text is a bit small again probably
resize it yes so we have our sister
setup here's a state in below did not
started because we haven't we haven't
run the sister that up yet and if we
click it we get an example I set up by
the way we created inside our extension
and if we want to see the feed your list
we can actually go to the home page and
here in the product videos page at the
very bottom we have added a new category
and a new video and of course perfectly
video there's a some video showing up so
random video taken from our application
so nothing special so back to the code
so the aligned seven we have this event
or register assist to set up from the
aggregated assist setup table which is
the one used for adding the new entry to
the assistant set up the event exposes
our temporary record in the same table
that's the one that's used for
populating the page and online 10 you
can see that from the same table we're
calling a method for adding the entry
which is their other extension assisted
setup it's again very simple just one
called
the first parameter is the ID of the
page it's followed by the text in the
entry the visibility state after that a
record that you - couple again the
initial status and end the icon name and
line 19 here we have instead the other
event that's used for for the product
video page and it's still owning it
buffer from the product video buffer
surprise this is this one again it's
very similar to what we saw before for
the sister setup it exposes a temporary
record the same that populates the table
they add the page and it also exposes a
series of helper methods in this case
we're using the add category to add a
new category and the add video to
category to add the video the first one
here takes the record as first parameter
and the name of the category as last the
video to category takes the record the
name of the video and a link to the
video itself and he reads the category
from the record itself that was
populated by the but the by the add
category call
so to sum up what we saw in this demo
the important parts is that a new entry
in the system set up a age can be added
by subscribing to the sorry or it is a
set up and that that event exposes a
series of metal on the same table and we
can use aggregated a sister set up the
other extensions sister set up to add a
new entry while for adding for adding a
new video today to the video list we
make use the own init buffer event in
the product video buffer table and again
we make use of the of the medal to
exposed by the same table in our example
add category in that video to category
I'm gonna give you the word yes these
are cool examples of basically how we
are now extending this out so it can be
done using extensions those facilities
as well so thanks for that
tomorrow you will come back later on yet
but I just want to talk about the
debridement simplifications that we also
want you this is basically to try and
and help our users quickly get an
overview and so simply reduce the number
of steps we have on the ribbon when
possible and again this of course has to
happen with a lot of respect for the
current processes and capabilities in in
the ribbon so this slide it's basically
an attempt to show some other general
thinking
about cleaning up the ribbon so at the
if we look at the the lowest part of the
image the Home tab basically you can see
the different action categories that we
are dealing with we have the Home tab we
have the which contains all the manage
sections we have process
navigate reporter than anything context
specific so our objective was to move as
much as possible into the home tab from
the other three sort of main tabs which
makes up the debrief and currently so
anything we could move from the action
tab into the Home tab and then put those
into the process category that was
basically the the attempt we went
through so we did the same for the
navigator and the report tab and so
general that the principles are that the
manage tab is for actions that are
related to creating editing deleting a
record where the actions tab is reserved
for for actions that manipulates or
creates data and it should also provide
feedback once an action is completed to
to the user the navigate tab of the
related info item step
it's basically containing action whose
sole purpose is to open a relevant or
related page
no dialogue and it shouldn't have any
apparent side effects and then finally
the report tab which yeah it's an action
for running reports either directly or
to request pace or or tile our page then
there's just a small example I I paste
it in here of reopening the reopen
action it's it's sitting in the process
promoted category and it is set to
promoted only so that's basically how we
move them around in
the code so with that in mind we applied
sort of the we we had to rewrite the
action tree a bit make some adjustments
we did this based on UX had some
recommendations for how we could
basically traverse the various actions
on each of the ribbons for all pages so
like just a small example we had on the
sales invoice we had customer from the
manage part but but should bother PE on
the navigator related information so we
we simply moved it over another small
example is moving an action like the
release which was on actions and then on
the actions tab sorry and then move that
to the to the Home tab as a promoter
don't we and that way we we simply went
through the exercise of reducing the the
various tabs moving as much as we could
that would make sense to the user in our
opinion into the Home tab and of course
we have been careful we believe in not
being too intrusive in this exercise so
I'm also I guess so just some guiding
principles for for written pages like
design principles would say it's again
promote new promote the set up action
focus on the context of the car page
when looking at navigation be generous
would promote it only it's it's quite
good clean up the tabs don't leave in
single actions on its app so we we also
in that process we also realized that we
had a number of pages now where you only
had one action in its half making it
should we say less useful so actually
have to navigate first and then just
find one action in there so in that case
we we moved it all to the home tab
so here's the just a snapshot of our
decision tree that we use to formalize
some rules around rewriting list page
ribbon actions I won't go into too much
details I also think it's fairly small
font but this is basically the way that
we remain consistent so just a couple of
key takeaways from this or from our
process it's a lot of work to make
features simple it's a process where we
often had to go in and build multiple
prototypes just to try them out and test
them out with both UX and also a select
group of inducers and simply figure out
what would work the best that so it
becomes sort of a iterative process
where we keep reinventing sort of the
wheel and keep changing and making new
decisions about what makes most sense in
this case and how do how do users
actually perceive the system when they
just walk up and and you said one thing
is to take a very skilled or trained
user comparing to somebody who may be
used to a different system and then
compare the two one of the things you
also discovered was that it was actually
fun to re-engineer these experiences
because when we looked at some of the
for instance the dialogues that we troll
in the face of our users we also
realized that it can be quite difficult
to feel successful in using NAV at that
point in in our opinion so we also
wanted to test out various ways to be
less intrusive like adding these
notifications giving them results to
help finish these set of tasks
that are often can be cumbersome fun fun
new you new users and then we also of
course spend some time thinking about
how can we actually make our users
become more productive using attentive
which is we think very important yeah
but now it's a muscle it's actually you
again so we we saw the public simple
examples before we've seen how you add a
new application area an experienced year
which was which was the foundation for
building an extension using an
experienced year then we show education
their life cycle then the Venus set up
and then to conclude this session I'm
going to show you how to extend the
wizard so for some of you that might
have worked with the wizard before I
know that extending wizard in the past
was particularly difficult they were not
really extension friendly like handing
on a page was a tremendous amount her
word well now things have changed or at
least we have tried to make wizard
extendable and two aligned experience to
extend one with what you have with
extending any other page and so this
example I gonna show how you can add new
steps the wizard how steps can be
initialized and ordered inside the
wizard and finally we are gonna see how
the controls that you add in each of the
step
can be validated again as before I have
a new version of the same project I'm
gonna load it actually this time around
I'm going to show you the wizard first
we are extending the fixed asset
acquisition wizard and I'm gonna take a
shortcut to show it to you because I
don't want to go through all the steps
to show it but it's simple it is so this
is the fixed asset acquisition wizard
you have an intro page you have the
navigation buttons below like in every
other wizard you get the next page of
the second page you have some controls
then you get the third page there's some
validation to be done and the button
below gets disabled so you insert
something anything and we get the next
enabled again finally we get to the
final page the next button is disabled
you get the finished button a different
icon on top that signals that this is
actually the final page so let's extend
it so this is a page extension and it
lines seven I'm adding our new steps my
step 1
by convention steps are represented as
group you can put whatever you want
inside the group and it gets displayed
according to what you press with the
navigation button when they get enabled
inside this group we have wave a field
this shows the current step we are at we
have a caption not very important and we
have
our visibility attributes that's
controlled by some variable then after
that we have we I've added some other
steps I've added my step three here
another group exactly the same as the
one before with a field show in which
step we're at and one last step here my
last step at the end the visibility of
each of this step is controlled by a
variable like I said before and
available are defined here at the bottom
of the page and they are updated inside
they don't after get record through a
call to get current step which returns
the name of the step get current step is
inside the the parent wizard and as
convention we our convention is to use
as name of the step the same name as the
same level of the group now this is
something I I wanted to show you him
this them but I couldn't because he I
changed we were working on couldn't make
it on time but but I was told this
morning we actually have it now in the
code unfortunately I cannot show it
today but now there's the possibility
for an extension to to use expression
inside the inside the visibility
attribute which means that all this code
you are seeing here in this section and
all these variables they are gone so you
end up having inside inside the veil
ability the visibility attribute the the
comparison operator with with the two
variable to be compared so back to the
extra code so now we have our wizard we
have the we have the steps we have a way
to control the visibility but the wizard
is not yet aware that these steps have
been added there's no way you can
control them through through the
navigation button and the way so you
need to reduce the steps um somehow into
the wizard and that's done inside the
inside this code unit
so here we have the uneven tone in the
steps which is exposed by any any wizard
and the event has as a parameter a
linked list containing called the
Wizards name and inside this section of
code we are actually modifying the
entire wizard so in the first line we're
removing the intro wizard in the second
line we're adding our first step as the
first step of the wizard in the third
one we're adding my step 3 after F a
details FA details in you might not know
it but it was the second step in the
wizard I showed you before and then we
add our my last step as the very last
step of the wizard so now we also have
registered the steps but it still needs
to have a way to validate the controls
that we eventually we had inside inside
the steps or the existing step so that
that is done inside inside the disorder
event at line 12 they own validate
current step this is a bit more
complicated when it comes to parameter
as it exposes the record the source
record for the page some text there
representing the current step and
finally a boolean bar which represents a
return value of the event and that's
used for enabling and disabled the
navigation button you see below in the
body of the function
we don't do anything special we just
switch over all the steps and then you
can put whatever code you want inside
here and and set the step is valid the
return value of the function and as I
said you will get the the navigation
button enabled or disabled according
so now I can actually publish and run
the demo we see we're gonna see the
result okay so this is our first page
the step here says my first step so it's
actually our first step and we no longer
have a link text from the previous
wizard if I press next we get what it
was the second page before and we press
next again I get my set free so we can
continue and we get again validation
validation again and then it was
followed by the final by the final step
of the wizard if you remember and in
this case it's no longer the final up we
no longer have the icon that we had
before that was signaling the end of the
wizard we the next button is not
disabled time and will actually have
another page and that's actually my last
page the page said I just started in
there in the wizard so to summarize what
we saw in this in this example you can
add new steps to a wizard by adding new
groups representing the steps or
modifying existing one in the same way
as you would do with any other element
in the page you can update the
visibility of the step by reading from
the gate current step exposed Bo from
exposed by the by the parent wizard can
the the steps are registered through the
only need on in the step event again
exposed by the parent wizard and the
validation is done inside their own
validate current step so I'm gonna give
the word for the
final part of the presentation yeah so
we're actually we're actually in good
time I would say but basically to
summarize what we showed you today we
talked about the application
certification using the three different
layers for Tenerife and how we apply
those we looked at some of the updates
with each of the ribbon and Tomaso also
demonstrated how all this can basically
be done true through the extensions v2
so this basically concludes our
presentation I think we're far ahead but
if there is there's also time for Q&A
for sure
we do have some some t-shirts if anybody
has any questions let us know
otherwise there's a question out there
yeah what you can throw this cube I just
want to give people a heads up before I
actually start throwing it but maybe we
can help each other out there I think
it's yeah
now I hope it works with all this effort
no sound there's another one coming okay
sounds better
yeah I have one question is it also your
job to unify the ribbons or to the
consistency of ribbons what my users are
always irritated that's the same thing
is not on the same position example
print out sometimes is on actions
sometimes on navigate or for all posting
a test report and posting on different
ribbon paths and not always together at
the same place this is also your job
then there's still very much to do yes
thank you that's that that's a good
question and yes it is part of what we
are also doing looking at as part of
this effort there is a lot to do for
sure and it's as is as I also mentioned
that there's a lot of grounds to be be
covered yet but yeah working on it doing
our best
absolutely any other questions
sorry one
good catch
hello hello yeah my question is about
application area set up currently its
own objects on properties I think it
would be much better to move it
somewhere to set up all to external file
or somehow but not to keep on objects
yeah that's a good point we are looking
into the future of how we're gonna apply
a application areas and how its to the
objects or if we're gonna move out or
but it's it's still for now we're still
gonna go with what would reside on on
each of the objects if if I got your
question we are thinking about it we we
do get feedback on this from time to
time I would say that as part of this
process we we took what was available to
us as part of this process but it is
something I know we are discussing
Thanks thank you
I think there's one too
well it might be a the different session
session but what about shortcut keys I
think that's really what make things
simple for users
yeah good in video doing about that
not much at the moment not for this
effort we're not but it's a very good
input I will make a note of it for sure
- together with the rest of the feedback
it's yeah
you ain't handing out these and now you
will get in question on the extension
system you were talking about three
levels yeah
is the roadmap for each level or when to
do you expect me to be in in the
application yeah very good question at
this point we have 14 Arif we have set
the bar significantly lower because we
are committed to deliver the entire
scope which is take precedence over
actually optimizing all the things we
would like to optimize so I don't have a
concrete sort of roadmap at this point
but I'd be happy to
we also have a block and we're gonna
post from time to time updates to this
so there will be more information on the
process of this Thanks
okay yeah I have a question OVA dude to
the right for you yeah
my other right yeah all right whatever
so when I look into the application
areas a lot of some co2 to create new
application areas there what does the
end-user see from that well if I just
use application area our basic and sweet
to put my functionality into basic or
sweet application experience to you how
you call that if I just do that the
end-user will have the same experience
compared to when I write all this code
to create my own application area so why
would I do that
what does that for the end-user thank
you but it's it's all about being I mean
we're gonna we're gonna put in more
experience to use as we go along as
Tomas also show we can also create these
perseus using extensions and in that you
might have a complete different type of
solution but still provided using the
standard objects in certain cases so you
can basically build a whole new process
around that business process or you can
build new role centers so if you want to
be part of the standard pack it's it's
yes you're absolutely right why go ahead
and spend the time of actually going
through the hoops of creating my own
application errors and and and so forth
so we we are applying this as a taxonomy
inside the product but but still it maps
to the same experience you could say so
what about adding your own experience
divs yeah that will make sense yeah
but we can tomorrow maybe you can
comment on this in terms of the
extensions you showed around experience
to use
or maybe we we can we can we can say
that yes it it will be possible to have
your own experience - yes and then you
can add your own application errors to
that that is the that is the OB Exodus
but right now it's it's a lockdown a
system we basically define these and
then the whole thing comes down to the
application errors but later on you will
be able to extend that and okay wait one
one comment just still repeat what the
other guys will say currently
application areas but set on paste level
controls on page level that should
definitely go to fields in the table
instead of on pages yeah
made a note of that several now okay no
I mean I don't know if you this question
is exactly for you I will I'm facing an
issue related to the notification
dispatcher if there is an error the
javac' you stop and there is no way to
continue except if someone goes to fix
the data obviously starting accumulating
pending emails and everything is this
part of user experience or not just to
be clear in my opinion should skip that
email with the air or maybe write a
notification and continue with the Q not
accumulating yeah yeah it's a it's a
good question maybe maybe if you have
time afterwards we can just quickly talk
just so I understand the yes please yeah
okay let's do that okay any other
questions at this point it's otherwise
talking about yeah okay you're talking
about the parents T or not I mean if you
if we add a new experience here that
it's that also includes the fields from
from the basic experience to here then
you're gonna then if your application is
part of basic it will also be part of
that experience here so I don't know if
that answer your question
maybe okay we can always check can
always discuss it after and yeah yessir
poverty
ah I see so yeah basically will will
that sort of taxonomy grow into more
like a tree and then if you can have
certain dependencies for other
application errors and so forth we're
still debating that I think that that
would be the only fair reply at this
point so it's something that we have
bumped down basically in terms of
scoping so yeah okay thank you everybody
for attending and good questions and
comments so thank you
[Applause]
