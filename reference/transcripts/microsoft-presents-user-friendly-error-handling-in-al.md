# Microsoft Presents: User friendly error handling in AL

- **Source:** https://www.youtube.com/watch?v=D8233xMjVog
- **Video ID:** D8233xMjVog
- **Channel:** mibuso.com
- **Published:** 2024-06-16
- **Duration:** 44m47s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

yes I'll just start talking uh we'll
give you an introduction to the
different types of Errors uh how you
build a better experience using the
error info object we'll talk about
collectible errors we'll touch upon
guidelines and best
practices and maybe also talk a little
about where we want to take this things
that haven't been implemented
yet so I like to think of errors a bit
like a crime scene like where did the
crime take place what weapon was used
and and who is the villain now this
might seem a little off but let's take
some of the examples here so where now
of course the developer speak for that
would be well that's the stack Trace but
you can also think of where as well what
was the surroundings in that was it
during usage of the client was it part
of an OD dat call was it a job queue job
Etc so that's the wear part
and then we have the harder one about
well what weapon was used for this
hideous crime of raising this error um
was it an error in the data entry was it
a data error that was in the database
already which could be in the current
record on another record what you got
returned from a query or it can be
something a little less within your
control the permission set up how the
external system is set up and just be a
plain coding error and then there's also
the very nice Group which is just called
bad
luck um and then you have so who's the
villain now the villain is usually also
the one who can fix it so so this
actually makes a bit of difference so it
can be the current user it can be a
privileged user for permissions it can
be the developer it can never be micros
oh it can actually be Microsoft um or
maybe you just need some divine
intervention to actually solve this um
so where are we taking this well if you
take a look at the some of these
examples of Errors the top one where the
user has typed an invalid date it's CL
quite clear who's the villain it's a
user himself and it's quite easy to fix
you just type something correctly and
then you have a group of data dependent
errors and then all the way at the
bottom you start having the more fluffy
one another user has modified the record
I guess that's in the bad luck
category um and synchronization you can
argue whether that is bad luck or just
pure poor setup but in this presentation
we are mainly going to focus on where
the interactive usage of the
product and the weapon where the weapon
is basically the business Central data
where that is the main cause for errors
and then also where the current user can
actually fix the problem in business
Central so we want to help them moving
forward and inorder in order to do that
we're talking about actionable errors
where it's important that users can
recognize the error they understand what
went wrong and then they can either
repair or report the
error so uh so I started working three
years back and I used to see a message
like this while reproducing an scenario
and do you know what this error could
mean like it says there are no Warehouse
receipt lines created but why yeah the
why is hard I think it's quite clear
what went wrong but yeah but as a user I
have I had no clue but now what we have
done is we have we are using the these
actionable errors to add more details to
the error messages in this case we uh
tell the user okay what might have
caused this error in this case maybe
I've already created the weos shipment
lines that's why I cannot create more
and you also have the action to directly
navigate to the page uh and uh that
helps me as an end user to uh in
investigate and understand what went
wrong uh so we have another example in
this case I'm doing a field validation
I'm trying to update a quantity in the
sales line but I'm getting an error
message that I cannot change it reason
being there's a purchase order linked to
it and the good part here is even though
it's a field validation I still get that
uh actionable error or the navigation uh
action which I can directly go into the
purchase
order and if the same validation was
triggered from an action uh we would get
a dialogue message instead so the web
client is doing the magic to uh display
the same error in different formats
depending on the
context so can anasa can you tell us how
we can build such experiences in
business Central yes of course so now
let's look at the implementation details
so first of all error info object it is
an object that we have quite recently
relatively recently added to the AL
language uh and you can think of it as a
recipe for building an error dialogue so
it is a structure for grouping
information about an error um you can
use error info to implement different
error handling Frameworks that we have
in business Central so for example
actionable errors or collectible errors
both of which we are going to um cover
in this session so first of all let's
take a look at what are the advantages
of using the objects instead of passing
a very long list of parameters to a
method so first of all you can select
what you want to fill in so all the uh
properties have default values you can
only set one you can set all of them you
don't have to uh spend more time on on
filling all of the details one by one it
also gives you more flexibility so you
can set them in any order you want um
you don't have to get into the hell of
figuring out what what is the fifth
parameter in the long um method thought
um what does this one mean uh and also
that's a good one Microsoft additions
are not going to Breaking changes so we
can add new properties whatever we want
and your code uh won't be uh broken by
that so this is a API these are the
methods the instance methods for error
info object uh but no worries we're not
going to dissect this Slide line by line
we don't want to sit here forever so
let's just jump directly to the
highlights
uh we can see a very nice error dialogue
here that allows the user to reopen a
document directly from an error dialogue
right so let's break it down uh title
error info allows developer to set the
descriptive title for a
dialogue and then this nice button here
in the right corner that says reopen
document that is an action the add
action method allows you as a developer
to attach specific custom actions to
give
error dialogues so users after clicking
the action can follow the link and then
for example fix the problem and then
come back to the original page uh so we
can think of it as a kind of guided
error
resolution so now let's see how does
this translate into code by the way this
is a sample code it's not a production
code it's just for the demonstration
purposes so that we do we do understand
uh how to implement similar error
dialogues um let's start with the even
subscriber because that's where the code
execution will start uh this one is very
simple it just verifies if the sales
header status is open if it's not then
it means that we are in a error state
right so now let's configure the error
info object we are setting the message
we are setting the title that's obvious
and then this one is nice we are setting
the system ID and system ID can be
accessed afterwards uh in the action
implementation can I just add something
here there's also the ability to set the
record ID system ID is the way to go
it's easier for us to handle than the
record
ID yes so now after setting the system
ID we are finally adding an action uh
you can see yes the tool tip uh that
will appear on the button of the action
the code unit and then the method um
this is the action implementation right
you need to make sure that the action
exists because we you are referencing it
by name and also if you notice uh this
one takes error info as a parameter so
this is a contract between the uh action
API and the error info object uh so that
one is implemented so we can go inside
and take a look at what is it doing um
it just takes sales header um by the
system ID that we have provided before
in an error info object and then the
perform manual reopen method is invoked
right another example the this one
actually has two actions first one is a
regular action another one is a
navigation action let's see what are the
differences here um here what's uh
interesting is that we use custom
Dimensions uh so custom dimensions are
not strongly typed just bu of properties
so have if you have any additional logic
here uh you can fill in the custom
dimensions and then access them uh
inside the uh action procedure
itself yes so this is the um action we
you can see custom dimensions are uh
referenced
inside here this one so this is a
navigation action uh as you can already
see it's easier to implement than the
addaction right because you just need to
set the page number and call add
navigation action um so you don't need a
whole new procedure to be declared uh
you're just going to open the page with
the number that you have specified uh so
just quickly to compare action needs a
method uh navigation doesn't need a
method uh one is used for fix it
scenarios so the user wants to maybe go
there and there's some additional logic
required navigation action is just like
show it show me the page um and then add
action supports custom
Dimensions okay so let's move to Tool
tips um tool tips are short informative
texts uh that appear when users hover
over different elements of the interface
and in business Central disc can be uh
either an action a field or f f box or
an activity button um and these text
provide a quick explanations about the
features without overwhelming with
details right so they give you inside
info on how things work without making
you read the whole
manual here we have a nice example of a
tool tip it says shows open Warehouse
shipment lines already created for this
document right so as you can notice is
not crowding the user interface user can
hover over it uh to get more more
information uh but there is no way could
we could have put all this text on a
button right uh so that's why tool tips
are uh very very useful and how can you
uh attach them to the action very easy
error info object add action method the
last text parameter this is what is
going to be a tool tip on action and the
same goes for navigation action
so now yens will we talk about yeah I
want to take the opportunity now that
we've mentioned the world tool word tool
tip to mention that we have added the
ability to add tool tips on table Fields
rather than on page controls it's not
strictly related to error info but if
you start adding tool tips to Fields
instead then it allows us to then start
harvesting that when we know that the
weapon that was committing the use to
commit the crime was a certain feeli now
actually we can start building logic
that also takes advantage of that tool
tip so in general remember you can now
specify it also on tables so just to add
it's not just this so with the all the
keynote presentation what we heard about
copilot even the chat Paine in the
copilot would rely on these tool tips to
get some more information so that's
really good idea to add good tool tips
good caption so that we can make the uh
users and also the C it understand
what's happening so you can make AI even
smarter um detailed message right so
here we are U shifting away from the
errors that the users can fix themselves
and move a bit towards the errors that
require a support or an engineer
intervention right so detailed message
will be mostly helpful uh in these
scenarios uh it is not shown to the end
users but it's tucked away in the copy
details section of the error dialogue uh
when the users uh copy the copy error
details then uh apart from the detailed
message uh the text will be enhanced
with the session IDs time stamps and uh
all the useful support info uh we have
also added uh share in teams and sharing
Outlook that's also handy um and you are
not required to send the detailed
message the detailed will be empty right
uh but your future self will thank you
if you do trust me because it will come
back at you when you need to to
troubleshoot the error and you need to
figure out what has happened so think of
it as like what technical information
will I need in case this error happens
and I get a support case or a customer
case um but maybe don't be to veros
don't write a novel there unless you
like reading novels uh attached to
support cases you can have ai generated
novel for you and put it into the tool
that's even and then make AI under you
know read and Abstract everything uh so
that's a nice example of where can you
get the uh details right the technical
details so here that's the HTTP P client
failure and we are getting the uh last
error text out of it and we are feeding
this populating this um the detailed
message uh with that uh error text so uh
here is how it will look
like that's a nice screenshot uh we are
having trouble contacting Shopify can
you please Dragon after some time so we
are clicking on share details copy a
details this is what will appear in the
clipboard yes the error message we can
see that detail error the SSL connection
could not be established remote
certificate right that's a perfect
example of a message you don't want to
display to the end user because imagine
um um an accountant seeing this they
might think that their computer suddenly
switched to a foreign language language
right and like some really bad things
happened uh so this is a perfect
candidate for a detailed message then
further internal session IDs time stamps
right can you spot the Z UTC very
important so it's you know when you have
the customer case and it says yesterday
5:00 p.m. something bad happened so now
the question is what is yesterday what
is even today right uh which time zone
because otherwise we end up
investigating with your local onw time
and then the customer is sitting in
Japan right so that problem solved you
have the time stamp with UTC uh in the
clipboard yes Al Co stack useful for Al
developers custom
Dimensions yes so we have made it even
more smooth to encourage the users to
send that information to support so we
can click on generate email the new uh
email with the title will be um
generated for you uh and it's very very
good to have that in a text um I think
we are a very technical crowd here right
so raise your hand if you had to at
least even once in your lifetime
transfer the value of a goid from a
screenshot to a
text waste of time right so yes this is
in a text format just copy paste send
it
um yes this is an example of a detailed
message um coming from the validation
errors right the inline validation
errors
okay test F
improvements so um a while ago we have
looked at our Telemetry data AC coming
from across all of the production
clusters that we have and we're trying
to figure out what were the most common
errors that are bothering the
users and it turned out that test field
errors were quite a prominent group
there right so we figured that we might
Implement a platform support uh to make
the test field uh actionable so this is
the platform logic that's how platform
figures out uh what page to open uh when
the user gets a test field error so what
action to uh actually attached there may
I add a comment here yes you could also
interpret this as Microsoft being lazy
because we probably have thousands of
usages of test field so if we can fix it
in one place we don't need to go and
change 2,000 places in the Bas app
yes so that's the logic here if the page
can be found us using drill down page ID
and thir card page ID from the record if
that is found then let's verify the read
and execute permissions on a page right
why is that so imagine that we put a
very nice Action Link on an error
dialogue user clicks it boom permission
error right that's not the best user
experience that's not what we want to uh
display so this condition needs to be
met destination data needs to be
different from the current record and
also destination page needs to be
different from the current page right
because sometimes test field errors need
to be fixed on the same page just on a
different field right so if if we have
automatically added a link to open the
same page on top of the original one
that's also a nice experience right so
if all of the these conditions are met
then we are adding the uh link to uh to
the test field error
yeah
let's great so let's see uh a demo of
that so the scenario here is that we are
in the general ledger setup we want to
set the additional reporting currency to
Australian dollars right
yes reporting let's find additional
reporting Australian
dollars we need to fill all the details
let's choose the first one from the
list okay error right test field error
the show currency card that's the
navigation action that the platform has
added with no Al code required here
right and um yeah let's see how it will
work this one says actually residual
gains account must have a value in uh in
Australian dollars right so let's see
what happens if we uh click the currency
card yes we have Australian dollars here
right let's find the field that was
actually um empty let's set this up to
the first value from the list let's go
back let's
see yes we are filling the details again
let's
retry okay another one A different one
residual losses account right still on
Australia LS both of them are required
so let's try to navigate there so pay
attention to the fact that this is
Australian dollars right because the
users user wanted to set Australian
dollars not Euros right so this is
filtered already to the correct uh
record correct
currency let's R try and let's finally
hope that this will resolve all the
issues perfect right error fixed so it
was quite smooth the user had to only
follow the links right and they were
able to resolve the issue without uh you
know getting back and forth because
without the link they would need to open
the tab find currencies find the page uh
find Australian dollars fill everything
up right this is smooth this is going
from directly from the error
message great rection will you now talk
about collectible errors it's actually
James uh can you add some details about
the collectible error before I go into
collectible errors is actually a pretty
old feature we did it in 2021 I think uh
it allows you to continue execution
while you collect the error so you can
postpone showing it and then show all of
them together now some of the design
principles is what I just mentioned and
also you can reuse uh error racing code
so you don't need to do something
special when you want to collect it the
existing error code should not change
Behavior so if you're not collecting the
errors then it'll still air out as you
normally would and then it was
definitely a goal to make sure that the
if code unit runs worked as it used to
and avoid accidental commits but let's
take a look at how we build it in the
product yeah so uh imagine I'm an
accountant I'm doing my day-to-day job I
would like to post some uh lines General
General lines uh or general journal
lines to pay my vendors I have three
lines here and let's try to post the
lines and see what happens oh no there's
an error uh so this time the error is
okay something to do with dimensions and
uh I need to change the dimension uh
from inter company for the business
group to home okay let's see how we can
do that so in this in the context I can
see it's on the first line of the uh
general journal line so I can go there
go to the dimension click on it and edit
the dimension set entry and change the
business group here to home once I do
that let's try to post it again and see
if it works ah no there's another error
this time this time it's about uh the
sales Campaign which I'm using is wrong
yeah right now it's not winter so I need
to go and delete this so let's do that
for the first line as we did previously
uh so just deleted the line let's try
again come on there's another error
error after error like on all the lines
one by one and this is what I am in the
situation and probably our users are
frustrated as well having to do this
let's see how it is done today uh or how
it was before sorry so it was it is done
today for the posting routine so what
happens in the posting routine is we
check the dimensions and when we do the
check we use error message management to
log the errors in this case uh the
errors are logged into the error message
record and the code execution stops as
soon as the error is encountered and we
just show the errors as we encounter
that uh so let's can we do something
better by using collectible errors uh so
let's start by adding a property on the
uh check or attribute which is called
error behavior and we can set it to
collect um and then let's let's see what
happens inside the check line
routine uh so the on on run of the code
unit we have check Dimensions inside
that when we check the dimension we need
to just make sure if there is an error
we need to set the property on the error
info to collectable that's true uh once
we do that what platform will do is when
it every time it encounters the error
rather than throwing it right away it
will keep collecting it in the
background and we can do the same thing
with test field on the record and the
field error by passing the error info
object to the uh to those uh uh
procedures so if we uh just rely on this
uh there would be a default error
message and thrown by the platform which
which will say okay there are there were
multiple error encountered and it will
just show the first one and you can find
rest of the details in the uh copy error
details not a very nice experience what
if you would like to change this and
handle this in our regular error message
page yeah and this is what you see if
you didn't really handle the error so
when you came out of the error Behavior
collect then it would end up showing
this rather ugly thing but that's back
to the we still want it to error at the
end unless you've done something right
to keep the existing code running and
it's basically just a handshake you set
the era in to be collectible and then
when that is being run inside a scope
where you do collect then we actually
start collecting them and allow you to
continue exactly so here we'll try to
handle this in the custom UI in this
case the Beloved error message page
which our customers are used to
everything Remains the Same except now
uh when we are running the procedure uh
whenever we run let's say we can use the
code unit do run and uh if there is an
error if it's not successful we can use
this collect errors procedure and within
that what we are doing is uh we are
calling the has collected error uh
function from the platform uh which
tells us there were some errors inside
the code unit and what we can do is we
can do get collected errors which will
give us the list of uh all the error
info objects we can iterate through them
and in this case we are pushing them
into the temporary error message record
um so another thing is we need to make
sure that we clear the collected dat
message otherwise the platform will give
you that uh default notif uh error
dialogue uh we want to avoid that so we
can do that by using this clear
collected errors or we can set the
Boolean property through in the get
collected errors which will clear the
error
messages and uh and just to show that uh
we can then take this uh temporary
record where we collected all the errors
uh pass it down to the error message
page and it will all work and we will
get the error message uh so let's see
how how it is implemented uh in in the
place uh so we have a feature called uh
check the lines while you're or check
the data while you're working so it
happens in the background uh background
so you can enable that feature from the
general ledger setup so on the right you
can see there's a fact box now where
while working on the general journal
lines I can see the list of Errors so
there are six errors right now so if it
drill down you will see all the
collected message at once in one place
in the eror message page however uh we
have done something better so we have
released an extension called error
messages with recommendation what we
have done is we have improved the user
experience here by extending the
extending the page uh so here you have a
little bit cleaner interface uh and user
can click on the error message to
reproduce the same beautiful error
dialogue with the title description and
they can also use the same functionality
to share the D details uh with the
support team and after that on the right
we have moved all the details about the
error message to a fact box so even here
you have the context where you can see
that the error was on the first line and
we have added uh something called
subcontext or the error location which
is in this case it was Dimension set
entry because that's where the actual
error error happened so user can
directly drill down there and also fix
the error by them themselves this is all
about understanding the error so we also
need the source uh in this case the
default dimensions of the vendor is
governing the rules of the dimensions so
user can go there and look at the rules
and they can understand the error much
better in this uh using this
extension uh what if we can do something
even better like now there's an column
called recommended action a user can go
there and once they have understood the
error and how to deal with it they can
accept the fix what we provide so in
this case uh it's we need to change the
dimension so it's uh gives a nice
confirmation dialogue which says uh we
need to set the dimension to a certain
value we can accept that message and
once it's done we get a nice
confirmation or acknowledgement message
that yeah we it has been changed and on
the background you can see the status
has changed to fixed uh how about we
select all of them together and accept
the recommended
action and this time we get a
confirmation message saying okay five
out of six would be fixed uh because it
already knows that one has been fixed so
we can accept this and voila so we are
able to fix all of them and I'm happy as
an accountant I can go ahead and do my
posting let's see what happens or what
happened in the background and how did
we implement this so in the error
message table in the extension we have
extended few the table uh error message
record with few Fields especially the
title uh the recommended action caption
uh the message status and the subcontext
related stuff we have an interface
implementation in an enum which governs
like for this particular error message
what is the fix required let's look into
the uh interface so the interface you
would have to implement is uh uh the
error message fix which contains three
uh procedures one of them is the set
error message uh properties uh where you
can set all the properties like title uh
caption and uh yeah uh the subc context
and the next is the on fix error this is
the logic for the fix and you will have
the access to the error message which
should contain all the information you
need when you're uh trying to fix the
eror in a different transaction and on
success meage is the acknowledgement you
get after fixing the error message so
this is all done on top of uh error
message management uh so if you are
using error message management to log
the errors this is what you should use
um and of course don't forget to extend
the enum because that's what would be
used uh for so that's how we would
identify which error fix you need would
be applied to the error message uh so
let's look at the B Bas app code in the
error error message management module uh
so we have added a procedure called add
subc context to the last error message
in this uh we just get the last error
message and trigger an event because uh
we want to read that uh information in
an extension and the tag can be used to
identif ify uniquely which error message
are you talking
about and in this subscriber uh so we
can skip the logic if the if the tag is
not uh U so if if the error is not does
not belong to this uh fix so you can
identify using tag and then you can
validate all the extended Fields uh in
this case the subcontext and the title
and all the other properties so once you
do that uh uh you should be able to
provide a better experience so right now
we are not going into the details about
how you write the fix but it should be
very similar to uh the normal add action
fixes you would
add uh and you should be able to get
more details about the extension and uh
how to write the ER effect and what
methods to implement in the uh GitHub
link here and so prank Shuman it seems
that you have just described two
different approaches to error handling
right so which one would you recommend
using yeah that's a nice catch uh so
right now uh the issue is we don't have
the support to get the actions from the
error info object so if you are using
error info object you can continue doing
that uh but if you are used to using the
error message management module to log
your errors because that was the old way
to collect the errors in an error
message record uh so you should you have
to use this intermediate solution but
eventually when we have the access to
the properties I'm looking at you so uh
in that sense uh we should be able to
give the same experience we should be
able to collect the errors because when
we show the error messages in the error
message page from the error message
management uh module we collect all the
error infos we also collect these and
combine them and show it to the user but
at this point we will lose the
information about the add actions from
the error info object but hopefully soon
in the
product yeah that's the limitation I was
talking about and this should take our
user experience from here to here
and uh so yence I'll hand it over to you
to share some guidelines and best
practices yes and I'll take the easy
route out and point to
documentation where there is actually a
section about actionable errors
collecting errors Etc so yes you could
have to just go and read the
documentation but there are a few things
that we would like to highlight first of
all it's time to move away from just
giving one piece of text when an error
happens so replace your error text with
error error info because it allows you
to build a much richer experience for
the user for the error messages remember
it should be possible to recognize the
error that's the title part the body
content well that is why if it's
relevant and then how to fix it if it's
something you can either describe in
words even better if you can add an
action that allows you to fix it then
add add an action with clear description
and in use the detailed message for
technical information for advanced users
that can help them troubleshoot the
issue in the documentation the navigate
and um other actions they're called fix
it and show it actions um and then also
just consider in general to make most
errors collectible because but now you
play nicely if somebody wants to collect
all the errors in case you run it inside
an error Behavior collect scope so these
were just some of the guidelines you can
see more of them in the uh
documentation now
troubleshooting yes so you know
hopefully if you all use our info
objects and make your ER dialogs
actionable then no troubleshooting no
customer support cases all the users
will be able to solve their problems uh
by themselves but before that actually
becomes a reality you still need to
troubleshoot sometimes right so so here
is the help and support page uh it's
very nice uh users can get information
on what is the version of the
application what is the version of the
platform that they are um using uh they
can go and see the last know error
inspect pages and data uh they can also
turn on additional loging which is um
useful sometimes um and then they can
navigate to the latest error this is
that page we can see the error code the
error text the call stack this is mostly
relevant for uh Al defs then can I just
add a comment yes so if you have a user
that can actually reproduce the problem
get them to do the detail logging you'll
get every single SQL call you'll get all
the BOS to liit and of course you've set
up Telemetry so that you can actually
see it then have them copy the details
because now you have the session ID you
plug that into your Crystal query and
now you have basically everything the
system could collect currently for a
point um next one you can also take a
look at page 709 uh which is error
message register this one contains
errors coming from posting and uh job C
execution also useful if your users are
having uh some
troubles Telemetry so yes hopefully you
have um Telemetry set up in all your
production tenants uh all Telemetry is
documented so and and it also contains
signals for uh error information so all
the errors that the user see you will be
able to access them afterwards um in the
app insights account um it's also pretty
nicely documented so you can go there
afterwards even if you don't know what
uh a given signal means go there verify
and uh troubleshoot the the
problems
yes just a few slides on where we're
taking this first of all we're on a
growing product and as it grows actually
the support needs get larger but
generally customers will get happier if
they can solve the problems themselves
so there is also a bit of self-help here
that we get to do fewer support tickets
if we actually give a good error
handling we can also see the textual
information get more more valuable
because with with AI we have the ability
to actually use the text more so provide
more text around the areas provide more
context and also we see more and more
needs for automation you can set up
alerts through Telemetry so that you
automatically restart a server is if a
certain error happens
Etc now if you would take more the sort
of tactical view so what do we expect to
add to this well everything will
basically revolve around the error info
object because that one the moment we
have the source of the era or the um
weapon used
then we can start navigating to it if we
have tool tips about we can do a lot of
things and we will add all of that
capability to the error info object um
improving the default handling and we're
also going to at some point look at the
bulk handling so you get more standard
components for these collectible errors
Etc and at some point we might even get
a function pointer so that you don't
need to remember that it needs to have a
certain um method signature but that's a
bit further out into the
future and with this we are about time
to do some questions well of course if
when you get the slides it's always nice
to know the general business Central
resources so I want to thank you for
your time and then we'll open it up for
questions I
can yeah did you find one there yes in
the
T-shirt t-shirt done there so when you
say function pointer you mean we might
be able to someday pass the method
reference as a strongly typed thing to
the add action similar to FN subscribers
so so that would be lovely I don't think
it's happening tomorrow or anytime soon
maybe but yes that would be awesome
right yes Stefan is here you can you can
you know talk with
him Implement fix so knowing end users
if you give that to them they're just
going to hit it and say fix and there
are going to be cases where it's not
actually proper could you log to change
log at least that you've inserted or
modified so if I go in as a partner and
I need to reverse it I can see who did
it because if you go back to the account
and say Hey you changed this they're
going to say no I
didn't so um yes so there is an there's
logging automatically built in some ways
you have the audit fields which will
actually show that you actually did
change it um I would have to check
exactly what we log in Telemetry for
when the user actually invokes the the
error actions because we should be
logging that as well but I off the top
of my head I cannot remember exactly
what we log but that's basically what
you want to do you have the audit fields
and you have Telemetry to actually
provide evidence of what really happened
and which I I'm sure is happening on the
application Insight side it's just more
on the application side itself from the
end user perspective yeah maybe um good
good input we'll consider if there are
some things we can do better there so
but uh currently uh in case of error
message register if something has been
committed to the error message record
and you fix it there you should be able
to see who made the changes last but
yeah we need something more but robust
to track like who did some
changes yeah I saw uh that you mentioned
that you had some rules for when for
example you mentioned the the test field
there were some rules for when you would
activate this I didn't maybe quite get
it but uh I just know that we use the
test field a lot uh also in the in the
base code for kind of assertions so in
some cases for example the the journal
line that you you kind of make test Feld
on it doesn't really exist and so on how
how do you handle that so then we will
just we won't add an action if we can't
find um for example if not all the
conditions from from from the slide that
I showed you are met we just don't add
an action and it's up for the developer
to actually specify what should be the
the page like what should be the the one
to be opened okay yeah right yeah and so
it's basically if we can uniquely Define
a navigation to the crime scene we allow
you to get there um we might later add
the ability as to revert to the current
page with if it was on that page and
then have that field highlighted that
has not been built yet
um it's a little bit of a p pity that
you have to uh Define actions Twice
first on the error info and then when
it's collectible but could could a work
around be that if we could store the
error info in a dictionary and connect
it to the the temporary
um uh yeah to the temporary error the
record done we on page we we could
actually get the original error info if
uh we are running it straight
away yes I so let let's talk afterwards
just to understand the details because
uh we do know that there are some
information we could collect well you
could say a little better so that you
have them readily available later um but
I'm not sure I just grasped exactly what
uh the request was and maybe we should
just take that uh offline y sorry about
that and one
last we're up there I was just about to
make a very long throw a h
Mary I all uh will the error action
dialogue functionality run in modal way
and if so uh concerning all other p
pages that the user will run on custom
action will also they run in model mode
or
not in in general they run modally yes
uh and the way you would set up the
standard UI is actually you you show it
after the transaction has been uh rolled
back so you're not keeping the
transaction open if that's your concern
but yes they will be shown modally but
you're not holding locks while while
you're showing the modal data because it
this is after the transaction roll back
so you go back and fix the error and
then you do what you do
again open pages yeah yeah the user will
open pages and then the user would have
to go back and for instance do the
action again it is not an interruption
of a flow because that would give us
severe locking
problems thank you um we will stay
around we will allow people to leave
we're down here please come and ask
questions we love it to get feedback on
the features and where we should take
this next thank you everyone thank you
so much
