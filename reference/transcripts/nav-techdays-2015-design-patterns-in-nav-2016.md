# NAV TechDays 2015 - Design Patterns in NAV 2016

- **Source:** https://www.youtube.com/watch?v=eyRRFVDJXEk
- **Video ID:** eyRRFVDJXEk
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 91m15s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

so hello everyone and welcome to the
presentation about design patterns my
name is Nicola and I'm an application
developer from Microsoft's yeah my name
is Supriya
I'm also an application developer from
Microsoft I'm not from Microsoft but
from a Gilles and cloud-ready software
yes so design patents presentation is
going to be different than any others
because in the past we used to have the
separate event Microsoft would present
design patterns and the partners had a
separate session so this is the first
time that we are holding the session
together which is great because in order
for this event and this effort to
succeed we would really like to get
partner participation so we have
collaborated in the past with MVPs
around the design pattern but what we
are really looking is the participation
of all of your guys in this effort and
it is crucial for us because Microsoft
we are writing the base and you guys are
expanding and building on top of this
base so your feedback for us both
positive and negative is really
important because we need to know which
stuff have worked well in the past and
which stuff we should stop doing and as
well we have received a lot of knowledge
from the community some of the examples
you managed to see in the presentation
so for the agenda for today we'll talk
about these patterns gary is going to
talk at the end about the events and
chipping and I are going to present to
you passwords and sensitive data a
variant facet data-driven blocked entry
try methods logging how you can do the
error message processing and dynamics
request page events are unfortunately
the first thing on the slide but due to
some last-minute changes we have flipped
the order so cheap plane is going to
begin with the password insensitive
sorry my voice is a bit better than
yesterday but still I hope I'll be able
to finish this session also so let's
start with the first pattern is the
password and sensitive data
as all we now in today's world the
privacy and security is very important
for our users so if they feel that their
data is kept in a safe location then
they build a trustworthy relation with a
navy so that's what we want so before
talking about the pattern itself let's
imagine the following so imagine that
you do not have a wallet so then you
will have to store the credit cards
that's your data that is very sensitive
in random places you can have some in
your pocket some on the desk some in
different places in luggages whatever
that makes it not a very safe way to
save your data because anyone can access
it and anyone can use it or misuse it
let's say it like this now let's do the
second in my native example let's say
that you have a wallet but everyone has
permission to access it so that being
friends family kids and other people so
that also makes a very untrustworthy
relation because your data your
financial data it might not look very
well after you everyone has access to
these credit cards and then the last
example let's say that you have a wallet
you are the only person that has access
to it but your card says no pins or the
pins is clearly clearly display on the
car
if by somehow someone manages to get
access to your cards then again your
data will be in trouble so now to go
back to NAV world let's say that nav
data is kept in through an electronic
wallet so let's see what are the
solutions for the problems that I
already mentioned so credit card stored
randomly or let's say it data stored
randomly into nav the solution might
no don't do that but encapsulate the
data into one single place so have one
only one a single storage place then
don't let anyone access any data you
want they want so provide a single point
of access to to this data and then well
pins in the computer world usually
translates with encrypting data so if
the two above are fulfilled your data
will be even much more safer if you
encrypt it so let's see how we did this
what this pattern is proposing of course
the first step will fit will be to when
you type data into a password like fill
you would like the data to be not
visible so maybe most of you is already
aware on any control on the page there
is a property that you can send is the
extended data type property so if you
change it to a masked then you'll get
this in the UI so instead of the
characters you type you'll just see dots
then going to fulfill the first keep
your data into one single place so
encapsulate the sensitive data in
Microsoft Dynamics NAV 2016 we propose
the following we just have one single
table that keeps all the password and
sensitive related data and that's what
we need do we need just a key and the
value and these data the permissions to
these data were indirect permission so
all the sensitive data you just keep it
here and then you don't let you let only
specific objects to access this data so
it's about a single point of access so
to change this data it's only the object
that keeps it will do that so it will
offer in the table to 1261 if I'm not
wrong there are two functions to save
the password and of course with the
option to encrypt it or not
and then to retrieve the password then
also for the single point of access you
put the objects that want to access this
table and one thing you have to remember
is you have to give permissions to this
table and then you code this is the only
access point to the service password
table so for example in the serums
Sierra CRM setup or all the service
related setups you have the table that
will access has the only access to the
service password table and the code
looks pretty much like this and then you
have to set up the permissions on the
direct access table so this is about
keeping the data in one place and
providing single access to this data
then the third step comes and it has
encryption so in Microsoft Dynamics NAV
2016 we added platform support for
encrypting and decrypting so all these
keys will be stored on the server and
you can save them in a file or locally
that you can use in case you need to
recover some some data from a backup for
example so these are the the functions
that we provide in the platform side but
you don't really have to use exactly
these functions because we in the up
side we created the library that are
like wrappers on the platform function
so it's like an API we try to provide so
if you have to encrypt the crypt
whatever please use this encryption
management code unit then nav as we all
know it's a free-will system you can
post sell stuff that you don't have air
you can have negative inventory the same
is with the encryption by default we do
not encrypt the stuff that's why it's a
good habit that you suggest the user
that it's really in crypt
the password insensitive data so then
you cannot snippet of code like this one
were you
if there is no encryption you ask the
user if he wants to encrypt and then it
follows the procedure of encrypting and
saving the key so as a summary there are
three parts of this pattern
so first encapsulate the sensitive data
so keep this sensitive data into one
single place then provide a library or
an API that's the only thing that can
access this data so single access points
to this data and then the list but not
the last encrypted data to make it even
more safe so now the good things about
and the bad things that are about this
pattern so the good ones
it is highly reusable and scalable and
it gives the data in in a secure way the
best part at least in this release is
that the platform supports encrypting
maximum 250 characters in all the
features that we have by now this was
more than enough because in general it's
all about passwords and you will not
have hope I guess you'll not have
passwords more than 250 characters and
security numbers social security number
or pins they are in general small but
going forward there might be a need that
you want to to be able to encrypt larger
amounts of data so that's the first
pattern for today and then I'll switch
to Nicola so for the second button we'll
be talking about varying facade so as a
proceed pattern from the object oriented
world is a very powerful pattern because
its purpose is to provide a single
interface to a block of code and to
encapsulate all of the code into a
single place and a variance per set is
our way of implementing the facade
pattern into nav in order to get the
first facade pattern in any way we have
to have a very strong interface that
is not going to change so this function
needs to take all of the possible
parameters from the purchase header to
the bank statement and through a single
interface and it shouldn't change and
also it should be able to take the
record ref and record ID and process
them internal so what is the problem
that you are trying to fix is that
whenever we are trying to support a new
record this is usually the flow that you
are following so first we start by
duplicating the function we change the
record type and then we change all of
the namings within the functions we do a
few tweaks here and there and then we
just we are done this and the problem
with this approach is that we often end
up with more than 90% of the codes
duplicated to show you the example from
the product this is actual code snippet
from the product from the code unit
which is called document print and on
the Left we have a function print
purchase cutter and on the right we have
the function that is called sprint
service together and the big question
here is what is really the difference
between these two functions so by
investigating the code you can see that
the report selection is different case
statements just in the options and for
some reason someone is throwing an error
in case of the service header and not in
the case of the purchase header
why is the implementation like that the
outer new probably and we cannot know so
is it by intention or has it been
forgotten the intention is basically
lost so this is the actual printout of
the code units all of the 12 functions
that we have with different records and
some of them are exactly the same as the
tool that you saw and some of them are
completely different so spotting the
difference and understanding what
exactly is the difference between the
functions and why is extremely hard for
the next level this is just the
visualization how it look like
we would add eight more records and you
can handle the court like this only in
two ways first ways that your on any
rigid I and you can understand the
entire code base like this and have it
in your head
second is if you have excellent test
code coverage otherwise basically you're
doing something that is called screen
based development so you do a change and
then if nobody screens that you broke
something then it's fine right which is
unfortunate to something that we end up
doing right in the legacy code so to
extend the problem it to the definition
so if you are following the approach of
duplicating the functions with each new
records that you're add basically you're
making the code worse because you're
adding one more flow to the code code is
becoming harder tricks I understand it
is harder to maintain because every bug
fix needs to be done on one more place
it's really hard to extend and to update
because you cannot use the events and
you cannot use the hooks because you
have to do them on 20 places it's done
and one it's hard to test because you
need to duplicate tests and maintain
them as well and each time and you want
to add the new table you have to spend
the same amount of time the solution is
that we need is a single interface to
the block of code and we need to make
the table specific code and the common
code clearly visible to the developer
and adding the new record should not
require any changes to the code if
possible otherwise they should be
minimal on the clearly defined places so
let's take a look how does the patent
look like in the practice how could we
write the print document
function hypothetically so the main part
of the pattern is the signature so
instead of the passing of the actual
records we are passing in a variant
which can be any record and it is not
necessary for departing itself but the
good practice is to combine this pattern
with the argument table pattern because
then you will not have to change the
signature in the future for those of you
that are not familiar with the argument
table pattern the idea is that all of
the other arguments you would put within
a table because we can easily add fields
to the table itself
and not have to change the signature and
then you can simply reuse the field on
the place that you need it thus you will
not have to change the signature itself
now since we have passed in a variant
the question is how we are using it and
it is very simple you can just use it
instead of the actual record so report
dot R on page run code unit at run or
just invoking a regular function it will
work because the variant is going to be
casted to the actual record by platform
automatically now there is also no
ability that you can get the record ref
and you will need a record ref if you
want to support passing in the record
ref and the record ID and we have made
this one easy by extracting the code
into the code unit that is called
datatype management so you can easily
get the record ref and in order to
consume it you need to cast it back to
the variant so this piece of
functionality is one of the excellent
examples of us from Microsoft taking
this from the partner community because
I believe it was the idea done by Carey
and what was the one blocking about it
and and the whole thing was that while
you guys were doing this and
implementing like that it was a jack and
a pretty big one because this wasn't
supposed to work like this but since
we've now from Microsoft they're using
it now it is a pattern the distinct the
distinction is which is an important
point is the question is is something
working by accident or is something
working by design and unfortunately this
is not the best way of doing it however
this is a compiler limitation and fixing
the compiler was harder than getting the
agreement from the platform to support
this behavior in the future so they
could promise to support this we have
written the test around it so basically
it is safe to use now
now the next thing around the pattern
which is important is in some cases you
will have to do the table specific code
so you will need to get the table back
from the variant and access certain
fields or invoke certain functions on
the record so let's say that you need to
call prepare a good function and you can
easily do this by using a record Ref
a record ref can easily tell you which
table number it is and then you can cast
the variant back to the actual table and
do very specific processing so from
object-oriented world if we compare
something like this if you are casting
it back by using type it means that
you're doing something wrong
because you should be using an interface
for it start behavior and this is our
work around because we do not have an
interface and also this variant that you
are defining in a signature is the
equivalent of an object ideally it
should be replaced by an interface
however we do not have this ability and
it is a good practice if you can avoid
using this case statement to avoid it so
how are you getting a record back from
the variant very important thing is that
you shouldn't assign directly because
then you will lose filters if you use
copy it will preserve the filters and if
you're using record drafts at the table
is going to put it back so to summarize
so we have started from something like
this and we can replace it with
something like this and to make sure
that we hit all of the things that we
need we have the clear separation
between the table specific codes and the
common code we have a single flow
through the function and we have
minimized the cost of adding the new
records and it is easy to extend with
hooks and events because now we have a
single flow and less code in the code
unit
so constant classes if you need only if
you use it just don't use it as a camera
so this is supposed to work for major
functionality that you plan to use
product wide the reason why is you will
lose the compiler protection so and you
can run into the runtime errors in some
cases second problem is that you cannot
pass variant with a var so if the code
unit is changing the records you need
just to fetch it back after the Col unit
is done you can very easily lose the
filters so be sure to test that the
filters are staying there this table
specific case statements in some cases
they can explode and if this happens you
can fix the problem by using two other
patterns one is argument table so
instead of doing the case within the
function you can assign it before you
call the function as one of the
parameters thus you do not have to
create a gigantic case statement within
the code or you can reuse rules table
pattern for those of you that are not
familiar with the Routh table pattern it
is specifying how does the functionality
behave within a table and the perfect
example is print printer selections
where you can select which report for
which document is going to print be
printed and now final recommendation is
try to limit the numbers of K statements
and avoid if possible to be a bit more
specific so around the right number so
humble suggestion is that the best
number is of course none one is okay so
if you're using two please explain why
do you need this and if you're using
three or more no way that you're
checking this coding because this will
just create a maintenance here in the
future because you have splitted the
logic on multiple place okay so that was
it so it looks like we can talk till
tomorrow because the chronometer is not
started so after we finish with our
presentation you are welcome to join so
the next pattern is the data driven
identity button when you might need this
one you know that once you create okay
now I get it
so once you create any V record it can
be used by anyone so you it might be
situations when you want to restrict
usage of a record till some condition is
met
so one condition one example could be
that when you create a customer maybe
you don't want to allow users to use it
unless it is being approved by a
supervisor well if you have all this the
solution that we propose is to use a
generic mechanism to add restriction to
entity remove and check restriction on
that entity so that's what data-driven
blocked entity pattern likes to do so a
small diagram of how it works so you
have the entity customer friend or
whatever you will name it that is being
used consumed in the controller
well that controller you would like to
check if that entity is allowed to be
used so then you use the restriction
management code you need to check this
well I guess the most of you that are
retaining this session are familiar to
the activity of design patterns so maybe
you notice that there is already a
blocked entity pattern so you wonder
what is the difference well the
difference is not much in the name but
the name the second name now tries to
suggest what is the difference in the
block entity pattern you actually have
to change the entity so you have to do
structural changes by adding a new field
to the today entity so you change the
metadata usually it's a blocked boolean
and the difference the data-driven
blocked entity pattern is that it's not
doing any structural changes but it's
just using data inside the table to
identify the entity's blocked or not
so the flow to use this one is like the
following
first of all other is
friction you can do that in two ways
either using events were adding calling
it directly into data restriction
management coordinate what is will do it
will actually add a line in a table that
will really be like related to the
entity you want to block and as long as
this line exists in this table it means
that entities should not be used in the
specific processes then the second step
you have to consume the restriction that
means you have to add some application
code if you don't have the code but
that's the same in the blocked entity
pattern now one will block it
automatically so there is not a platform
support it's just an application feature
so to to see if the entity is blocked
you just use the restriction management
code you need if it's blocked or not and
then after you've done with the
restriction you just simply call the
code unit restriction management or you
use events so what that will do will
just remove the entry from the blocked
table so then the entity can be used
with no problems as an example that it's
being used 2016 so you have in the
general journal lines you don't want to
allow posting if the account number is
not filled in while the account type is
set as customer so the first you see
it's a even subscriber checks if this
condition is met and if it's not met
then it blocks the usage of this record
and then the second one it's also even
subscriber it if the condition is
fulfilled it will just raise allow using
this specific record the consumption
part happens in table 81 if I'm not
wrong so there we we check if the entity
is allowed or anything post the general
general line
to summarize what is good and what is
not so good about this pattern so as I
already mentioned comparing to the block
identity pattern this does not require
any structural changes that might be a
bit difficult to do it's easier because
it's just some data new data in the
database it is we try to say that is
scaleable and receivable and reusable
and then they we provide the API for
allowing restricting the usage of of an
entity and the bad first one is that you
can only add one restriction so in case
you might need to restrictions on the
same entity right now is not possible
and the second bad part is that these
restrictions are global so if you have a
need of restricting depending on a flaw
what you want to make record being
realistic before posting or new or for
creating new items and the current
implementation is not possible but we
might be able to add some types of the
restriction in the in the North
implemented in the future
implementations so that's all for the
blocked entity pattern the data driven
block density pattern yes
so for the dotnet exception handling for
me personally the developer for our
messaging this is as best as it gets so
this is a perfect error message right
because you can exactly see what's wrong
if there are 500 and you get the stack
trace and we clearly concede it cannot
connect so I don't see any problems of
using these messages however the problem
is that our end users really are really
struggling if they are getting this
message is because exceptions as general
are not actionable to the end users so
we need to provide them a better message
so they can know how to fix a certain
problem and another problem that's
occurring by using the by drawing the
unhandled exceptions is the fact that
the code execution
which you would like to avoid in certain
cases thus you need to use the dotnet
exemption handling in C L so this is a
new way of doing it with the current
release so we can introduce the new
function which is called a tri function
and it's just the property that you can
set on the function and if the tri
function is being property has been set
then the function is going to return a
boolean he has it succeeded or fail then
you can just simply use it as on any
other functions and if it doesn't
succeed then you can do exception can
link or you can either decide to lock
the error or to redraw it or simply to
swallow it so it is up to you in your
scenario so the recommendation is to
only a cop select the code that is
drawing the arrow between the try
function and that is a good practice as
possible so you will see all of the try
functions in the object designer marked
with this tag on top now when you are
using it as I said you're just invoking
it and if it shows the false you are
able to process the fault
response and you're processing it the
same way as you have used before it get
last error and you can also get the
exception type so the good thing is that
it can allow you with user-friendly
errors and it's very reusable solution
in the previous version you would have
to add a code unit specifically to do
this you do not have to do it now and it
works with both dotnet and nav errors
now the bad and are really bad
limitations that we have and this is
really important to understand this
function was not written for
transactions and try method as nav tried
method does not know anything about
transactions and you shouldn't really be
using it for transactions because
currently it doesn't reverse them and we
have received a lot of feedback from the
community we are currently working on it
we may do something around it however
right now I'm really advising you not to
use this functionality for transactions
okay next yes so then the next one is
the activity log pattern actually this
is the simplest of all and some people
might ask why is this a pattern
well this pattern is actually wants to
be any V implementation of the audit log
pattern so when do you have to use what
you will want to use this pattern in
cases where you have to answer questions
like this what happened
I cannot reproduce the problem so in
2016 we integrated with many services
and integrated with services it's pretty
complex because you might get some
connectivity issues you have a
synchronous calls so you would like to
log all have one that happens while
communicating with the external service
also another scenario can be that you
have a long activity when composed on
many tasks that can be executed
throughout a period of time by a few
people and then especially in case when
it's this activity fail at some point or
even if it's successful you would like
to go back in time and see when a
specific action was being executed and
who did that data action so if you have
these cases then we suggest you use this
activity log pattern so as I said it's a
pretty simple one it has only two
objects for now it might increase but no
it's only two objects so there is one
table 710 is the actual container for
the logs and then it has a simple
function inside that allows you just to
log in activity and the usage is below
it's pretty simple in general you log
what was the outcome of the activity and
then some related some related
information what is the message
what was the activity that I executed
and who did it and what time
then the second to object is the page so
is the UI part of the activity log that
is just a simple filter view in the
inverse chronological order so you can
go and check what is the activity what
which ones were successful and which one
failed okay so to summarize pretty
pretty short one it is a generic
implementation and I would say that is
using a bit varying facade pattern and
then of course we provide the
out-of-the-box API it's pretty simple
one the bed well maybe it's not so bad
this table might become pretty big and
the data inside sometimes can be
obsolete if it's very well so right now
we don't have any way to be able to
delete this data but it should be pretty
simple to do it so this is and I'll
continue with the next pattern
it's the error processing error message
processing pattern so in any V 2016 if
you attended our yesterday's
presentation we enhanced the incoming
documents functionality quite a lot and
one of the functionalities we added is
the option to create documents
automatically so if you receive by some
means it doesn't matter electronically
you receive an electronic document you
are important in to an incoming document
and then he would like based on that
electronic invoice to create the actual
entity into nav so let's imagine well I
have to mention one more thing in this
pattern that I'll present we call it one
more error pattern and it's quite
frequently seen in in some of our
implementations mainly the past ones and
it's kind of like this so the user comes
and tries to create the document oops
there is an error so the error is more
or less explicit
but what is also missing there is no
actionable thing to do it
if the user will try to figure out what
is wrong so he will spend he or she will
spend some time to fix the problem so
about after five minutes tries again so
oops the same problem it's not very
actionable and then you have to figure
out what is actually wrong with this so
you spend again some minutes and then
you try one more time a bit afraid
oops already user at this point is
pretty pissed off and he might go she
might go to a coffee or something else
and then when comes back fixes the
problem and now she's really scared
so tries one more time err is low oops I
did it again so okay it's like I give up
but that's a pity because wait there are
only two more arrows left so most
probably you've seen this in other
implementations what can be done well I
said that we used one more error pattern
well that was a joke actually because
it's we can call it an anti-pattern
because one more error is in general bad
UX user experience and then as you saw
the test these errors usually are
generated by test fields calls into some
specific fields or long error messages
that they try to be explanatory but they
miss one important thing they don't take
you where the actual problem is so then
you need a common error processing
method so the solution we propose is
this error messaging processing so what
you have to do is collect
all the messages at all the errors at
once and show them to the user in a
single place so don't do one by one and
then another important thing is provide
the link to the page where to fix it so
make it a bit more helpful for the user
so the usage is pretty simple
so the pattern supports three types of
messages as you can see error or warning
and information and there are two ways
you can use this pattern it's for short
running processes you can use as a
temporary table so it's a short life and
it will not be persistent the moment you
finish your activity the data is gone or
if you have some batch activities where
a lot of things happen in the background
then you would like to see in case of
errors you would like to see them after
the batch processing ends because there
is no UI there so you can use this
pattern in a persistent way so it's an
example in the incoming document page at
the bottom we implemented this pattern
so you can see that they are all the
errors at one place and they are
actionable so you can click on that link
and it will open you the page or the
list whatever where the the problem
actually occurred we offer also let's
call it an API out of the box so you
have some helper functions that will
allow you to to log different errors and
then we also offer help us for checking
if there is any error and how many
errors in the last but not the list
there is a helper functions to open or
show the the pages and with all the
errors at once
the code is pretty simple and it is only
in three objects one is one table where
it's actually the
for the messages and the other two is
the page to display the messages the
error message is warning or whatever and
then for the linking parts of or the
actionable part of the we used to help
us that also Nikola I think so in the
Valium facet is these two code units for
the page management and data type
management so to summarize this is also
trying to be a generic implementation
it's a bit similar to the using the
variant facade and it's very much
similar to the activity log
we provide out-of-the-box a lot of
helpers the not-so-good part is if you
tried it we saw it in the incoming
document page yet the messages are
pretty long and unfortunately there is
no way at least in a web client to copy
that message for example if it says unit
of measure this is missing will be nice
to be able to copy that unit of measure
and when you open the the page where the
actual problem is just to paste in that
place we are missing that it's not
supported you might need some cleanup in
case of a persistent solution so in
general if you if you have activity of
many steps that will generate this
errors after that activity is finished
and you no longer need the related
entities when you delete the related
entities or repost them will be nice to
clean up these messages after you and
then there is the last one in case you
use the persistent solution it's a bit
tricky because yeah while you have
errors errors they do something they
just roll back everything including your
error messages if you have them saved
into the table so you have to do a bit
of tricky stuff there you have to copy
maybe to a temporary because that will
not be rolled back and then move it back
and persist it afterwards
so yeah that's that's all for my side
for now
and Nicola thanks so for the last part
is from us is the dynamic Seacrest page
and this button is about showing the
request page dynamically so if you
invoke a function like this show request
page through the code the request page
for reports should just pop up so the
question is why would we need the
request pages and the thing around the
request pages is they are perfect for
allowing the users to specify the
conditions so in case you have attended
to the workflow presentation you could
probably see in there that they're using
the request page to specify various
different conditions but as well it can
be reused for example in a scenario that
I'm working in for a company in Denmark
and I would like to send an electronic
invoice to the government so I would
need to specify the condition if the
customer is in Denmark and it is a
public sector then I need to send your
ubl so I could simply select here if
country code equals decay on the sales
header and it is public custom and and
do this so users are able to do that or
for example you could send a different
report if the user is if the customer is
spending more than ten thousand euros a
month and then send a separate report to
everyone else so the problem is that in
the past without being able to do this
through the code you would have to add a
very specific page or a very specific
report just to be able to take users
input and with the latest version we
have provided you with a generic page
that you can just surface the users and
get his input and you do not need to add
any additional objects to the database
so the page is going to be built
dynamically so as an option depending on
your scenario you can store the user
input as a blob in the database and just
apply it afterwards to see if it is
measuring the criteria or not
so this is the entire code that you have
to write to build a request page
dynamically so first thing that you have
to do is you need to provide it with a
page caption then you'll add the table
which is a data set and each field that
you are adding it is just surfacing as
one of the default options on the
request page so this is a nice UX just
tell them what is needed and for the web
client the problem is that they can only
add one additional field so in case you
need three or four and you want to
support the scenario on the web client
you would need to add the fields then
you just run it modally and you are
getting the view back from the request
page which is an actual user selection
so if you would like to have the
multiple records like collecting the
filters on because s and on the lines
that's possible as well however you need
to do some setup before so these are the
two pages in micro so Dynamics NAV where
you can go and add the setup so the
entities are the tables that we are
showing and then we have the request
page fields which are actually the same
thing as add field on the previous page
and you can see that on the dynamics
request page entities for sales the
other we have added the related table
which is a sales line which is
indicating that that table is a child
then the following code that you can
simply reuse as it is actually using
these to set up pages so we have wrapped
all of the complexity within the request
page parameter scalper code unit and
basically the code is following the same
flow firstly we'll build a request page
and then we will set the view if user
has already had some filters we will
assign a caption run it model e and then
later we will get the view from the page
and optionally store it as a block so
these are all of the objects that you
need to use to be able to reuse the
functionality so as I said everything is
wrapped within this code unit we have
added the new day
type which is called filter page builder
and if you're storing okay so thanks a
lot so when we planned this session I
don't know how long ago events did not
even work in the CTP that was
distributed back then so we thought we
were showing you something really cool
and smashing now now I have been to five
or six sessions and all of the sessions
here at Tech days have already shown
events even our end young session or web
services has shown events so the good
thing about it is you see how important
events are the bad thing about it is I
cannot avoid a little bit of overlap to
what you have already seen so I will try
to kind of handle events from from a
different angle but again you will
recognize a few things that you have
already seen so I'll talk more about the
concepts behind events I'll do some end
to end coding so it's it's tech days we
should do some coding here I will kind
of focus on why and when do we need in
events and how you can leverage events
in your verticals that is that is my
main focus on on talking about events
now why do we need events in the first
place what is the problem that we have
without events you know we have short
update cycles now we have like any
releases we have cumulative updates and
if you're doing software as a service so
if you're into cloud into repeatability
into volume business then a continuous
updates are a key to your success if you
have like 300 customers or 300 tenants
on the same code base and you do not
update within the cycles that Microsoft
updates you have a problem because you
will your software will appear to be
outdated quite quite soon now but
traditionally the CIL code
quite tightly coupled and modifications
that you do tend to have a large
footprint in the standard application
and that makes it although we have these
powerful tools like PowerShell as the
PowerShell dude here no he's gone that's
still if you have lots of like overlaps
in standard objects even with PowerShell
that slows you down in trying to do
continuous updates so that is a problem
which events are going or trying to
solve
so what is the solution we want events
to enable a more loose coupling of
methods we want to allow functional
enhancement without touching standard
objects and Hatton's hasn't that been a
dream ever since the 90s that we could
do that we always needed to get into
standard code and standard code meaning
Microsoft code on the one hand but also
in projects that we do on top of our
verticals into our own vertical objects
and that makes make makes update a pain
in certain body parts so we need to
decrease the footprint that we have
within the standard application and
that's what events offer to do that
makes updates safer and much more simple
and that enables painless it's been a
pain in the body parts enables painless
continuous updates
that's what events do and they also and
we'll see that they also facilitate
collaboration they allow you to work on
on a certain business process from
different angles with a couple of people
or even with external partners without
causing any overlap so in short what
we're looking at in the demo right now
is a property or a feature of events
that says you can leverage events to
implement additional business processes
without needing to touch standard
objects at all that's the angle from
which we will be looking at events right
now
and we have a demo to prove the point so
I've been doing a vertical and just just
for you and the vertical is a calculator
and now I'm afraid as you've seen in the
keynotes Thomas Stiles Burke had the
same idea so it'll be who's who's first
to go to market with that to be
successful let's let's look at what the
calculator does I can do three plus two
and that makes five great I can do a 3-2
and that makes one that all seems to
work now
let us assume that the state-of-the-art
arithmetic has just invented addition
subtraction and multiplication these are
the three things that arithmetic can do
and of course multiplication is a method
that is quite new and quite fancy so we
leave that out our standard pack only
includes addition and subtraction if
there is a customer who wants any of
that new fancy stuff like multiplication
he we can upsell to him he can buy a
feature pack that also enables
multiplication so we have a great way of
upselling and we'll see that
multiplication out of the box in our
standard vertical is unfortunately not
supported the operator multiply is not
defined for this calculator so we can
only do in the standard application we
can only do addition and subtraction now
how does that standard calculator work
we do not persist any data in that
calculator we just pass a few variables
on the fly so still of course we work
with a class that defines all of the
methods that my calculator can do if
you've been to one of our structured
development method
methodology classes or trainings you
know that I always promote that a class
must be a table this is an exception we
don't need a table we can declare a code
you need to be a class and this class
holds all the methods that I can do
there are four methods that my vertical
can do is calculate the complete input I
could have a longer term than than just
three plus two I could do fancy stuff
like three plus two minus one and that
would also work on the calculator so I
have a method that does calculate the
whole input then I have a method that
does calculate the expression that would
calculate three plus two first and then
the result of that minus one so that's a
single expression and then I have my two
methods that come with the to come out
of the box in my vertical and is that
they are addition and subtraction now we
will not look at calculate input but we
will look at calculated expression and
we will look at the addition and the
subtraction method let's let me show you
how that works so that you have an idea
I mean how this this whole business
logic operates that is the addition
method that is how the business logic of
addition works now of course you may may
say I'm exaggerating this a bit is that
really a method that I should declare a
cold unit and and and a function for
yeah of course not but still you just
must you must think that this could be
any sort of very complicated business
logic that that your vertical does it
happens that I've chosen a vertical
which does which has a very simple
business logic so that could be much
more complex I've just being very
adjusted been very lame in preparing
this here so what does this calculate
expression actually do when I call that
it simply looks at
what operator is being used and then it
calls my two existing methods which is
addition and subtraction by calling them
from the calculator class that is all
that my my calculate expression method
does now this if I would would need to
implement a multiplication method on top
of that like somebody has bought the
multiplication module from me in the old
days I would have just needed to change
like to modify this specific object and
then ship it to him and that means this
customer has a different database a
modified standard object then all the
other customers have so I would have
needed to code inside standard objects
and that is not good
now events allow us to add methods to
that and multiplication is that fancy
new upselling method that I that I have
without us needing to touch this
standard object here but of course if I
want to do that and we're gonna code
that now and it will show you how events
work we this basic method that handles
all my sub methods who do who do the
tricks for me needs to be rewritten
somewhat now the calculate expression
holds the concrete math methods and does
nothing else what I need to do is I need
to turn it into a method framework that
does the stuff that comes out of the box
box but is also able to do additional
stuff and now let me show you how we
turn this here into a method framework
that you can hit with eventing first of
all I'm
if this is supposed to be a framework
then my standard functionality and this
is all of the standard functionality
that that my vertical does needs to be
moved to a different function like main
calculate expression typo and I will
just and this is local and I will just
move all of this down here and I will
also call this with all of the
parameters oops sorry
okay so what I do is I call my sorry
does that sometimes main calculate
expression with all the parameters first
value second value operator result here
we go so that's that's the first part of
the framework then I'm going to wrap
this whole framework in two events
there's gonna be two events and they are
on before calculate expression and on
after calculate expression and these
will have the same parameters as my main
function now right now as you see they
are only normal local functions but I
will turn them into events immediately
so how do I do that
I just go into the properties of the
function on before calculate expression
and say this is an event publisher so
this functionality here this local
function publishes an event to the
outside world which I can then subscribe
to from out of this of this code unit
and now I get a choice of event type
business event or integration event I
will come back to that later this is an
integration event and not a business
event if I would like specify that as a
business event there would be no no
problem there would be no change of
functionality but there is actually a
big difference conceptually so my own
after no it's not a try function my own
after calculation is also an event
publisher and it's also an integration
event so what I let us close that
yes I don't need to calculate a class
anymore
I forgot that sorry about that
I don't have the I have not copied the
local variable that's what I meant
so
a local variable must go yeah okay fine
now I can rap my rap the events around
what I've been doing and say on before
calculate expression first value second
value operate operator and result and
then I can say on after first value
second value operator result perfect now
there is one thing that I need to do on
top of that and that is I want to know
whether the the the method that is
called has been executed from my main
calculate expression or whether it has
been handled by an external event I need
to know that so I wouldn't I would need
to have a local variable here that is
called event handled which is a boolean
and I add it add that to every function
okay and if the event has already been
handled by something external I just say
oops I just say if event handled and
exit okay now I need to of course
provide the parameter as well okay so
what happens now here is that I've
wrapped events around my out-of-the-box
functionality and I know if my
functionality has been executed from an
external event or whether it has been a
whether it still needs to be executed by
my main expression okay so now I can
save that that works as well as it as it
worked before only I haven't added a
method yet so three plus two should
still work three minus two should also
still work but I haven't added the
multiplication method yet so let's do
that let's take the addition method and
turn it into a multiplication method
so that is Racine let's rename that okay
and then I say this is now this will be
the event which listens to the publisher
like which listens to the on before
calculate expression event that I have
specified in my calculate expression
code unit so I need to declare this
method as a subscriber method so a
method that listens to the to the
publisher and kicks in when whenever the
publisher is raised so I also do that by
tweaking this event and I call that a
subscriber event and then I'm being
asked the question which object do I do
I listen to and that's code unit
calculate expression and then I get a
choice of the existing publisher events
in that and I want to pick on before
calculate expression from that and then
I get a prompt that asks me do I want to
get all of the arguments over from that
publisher event to my subscriber event I
want to do that yes
so now I have a subscribing event called
multiplication which has the same
signature as the publisher
event and I can use these parameters and
I say since this is only supposed to be
handling multiplication I say if
operator is not multiplied then exit
because then I don't want anything to
happen and if it has not exited exited
then I also want the event handled to be
set to true so that I know that this
subscriber event has actually handled
handled my event so what I have now done
is that I have not changed my framework
here but I have still added a
multiplication event so a new new method
that is being called when the on before
calculate expression is being raised now
look at what that does to my calculator
button okay
thank you very much that's nice of you
thank you for paying attention that's
what happens if you if you copy and if
you're in front of an audience as well
it was quite a bit quite well on the
weekend when I wrote that so I didn't
forget it back then thank you so let's
see three plus two still works 3-2 still
works and three multiplied by 2 is 6
isn't that isn't that great so I never
have gotten such an applause for such a
small functionality thank you very much
so but what that does is I have here a
business logic a business process which
is now not only a hard-coded business
process but it is it constitutes a
framework that events
be thrown in a few more bits and pieces
of information here the event publisher
must not have any code I guess you've
heard that before by now it can have
comments so like like great event a a
little bit something that makes more
sense will be nice but anyway but it
cannot have it does not tolerate any
code now I'm not going for for time
reasons I'm not going to add one more
thing the most coolest thing invented
and that is the division method that the
new mathematician has come up with the
the only point in adding that is to to
make you see that you can have unlimited
subscribers subscribing to the same
publisher it's not limited to one
subscriber but you can have unlimited
methods subscribing to the same
publisher so directly can be additional
division that can be power there can be
whatever mathematical operation you have
that can be added externally one caveat
and you may have heard that before also
the order in which all of the multiple
subscribing events are being executed is
unclear and cannot be determined
it might change like from instance to
instance you never know what's gonna
kick in first they will all kick in but
you never know what's gonna kick in
first this is not a problem here not at
all because all of my events have
different conditions the multiplication
event only kicks in if the operator is
multiplied the division event would only
kick in if the operator is divided by so
it doesn't really matter what what
sequence you have in these events but it
makes you think like if you you had you
don't know which order in which order
this will be executed so
if you write code that depends on
certain values being changed and then
changed again that doesn't help me you
cannot do that with events you have no
reliable way of doing something like
that
also what is quite nice one thing that I
meant to show you the event subscriber
has a set of parameters it doesn't need
to take all of the parameters that the
publisher offers you can pick only the
ones that that you want and it also
listens to them by signature and name
and not by order so I can do something
like that I can have result here
although I have a completely different
order in my subscriber and it will
recognize it's the same data type and
it's the same name and it will execute
that yeah anyway so it will execute that
although the order of of parameters is
different but as I said it listens to
names so if you rename that which is OK
in any sort of function that you do
normally so that that will be pretty
fine with with normal functions but then
it suddenly doesn't recognize the
subscriber parameter anymore and we get
a and we get an error then the
practically the subscribing event throws
an error you have to use you don't need
to use all the parameters but you have
to use them with the right type and with
the right name that's that's the caveat
here and that's that behavior is
different from as you know all of the
other parameters behave in an AV okay
now having said that I would like to
take the time I still have that time to
take a little step back now
have used events to implement we have
used the event pattern to implement
something that allows us to not touch
standard objects it is not strictly
necessary to do that by events you can
also use hooks like if you're hooked on
a version that is Navision financials
1.2 which doesn't have events events
need platform support for to be able to
work so it needs nav 2016 but if you
don't have platform support for events
you can reach the exact same effect by
using a different pattern and I would
like to show you that so just to to make
you understand that there are patterns
for every sort of a context that every
sort of environment that you work in and
you just need to choose the right
pattern so if we have we have an old
calculator here and just imagine this
it's Nevisian financials 1.2 we don't
have fancy stuff like eventing and this
old calculator does exact exactly the
same the same stuff old calculator three
plus two is five three times two is not
defined how does that work it works a
little bit differently but basically the
same it's based on a table that is never
persisted we need that this old
calculator table which has all of the
fields that we just passed as all of the
variables that we just passed as table
fields and in if we have this old
Edition form then it just uses the
fields of this table to do the the
mathematical calculation and we have
defined in this old calculate expression
a sort of on before calculate expression
I also have known after calculate
expression of just omitted that because
it doesn't really matter I'm not using
it I could use that as well
so we have without declaring events a
methodology of doing the same thing only
the code looks a bit different if we
first of all we need to implement a
record here and then this on before
calculate expression does something a
little bit different it looks into hooks
that you have defined somewhere and then
runs the code unit but it's also not a
lot of code it's it's just it's just a
few few bits bits and pieces of code and
let us we need to define these hooks on
on a on a page that has all the
calculator hooks we need to define these
methods I think it is like now we need
subtraction we need 805 so we define two
new hooks here old multiplication just a
second
and all division so we have defined
these these hooks and when I now run
that old calculator page I can suddenly
calculate multiplication as well and
this works completely without events so
why am i showing you that in a session
on events because this is also a session
on these own design patterns and there
are design patterns to facilitate what
we now do with events even if you don't
have platform technology to support
events that is possible of course events
are much more efficient they provide
additional functionality they are much
faster this is this is a bit of a slow
thing so whenever you have platform
support for that do by all means use
events so far for the demo I hope you're
gonna buy my new vertical it's I promise
it's cheap so we have seen two
extensibility patterns one with events
what you do is you design a business
process in a way that it becomes a
framework for decoupled methods then you
wrap the the process in publisher events
you have an own before process the main
process and an own after process and
then you enhance your business processes
by adding methods as subscriber events
that's what you do if you do
extensibility with an event pattern if
you do extensibility with that old hook
pattern in that context the
extensibility hook pattern you do the
same basically design a business process
in a way that it becomes a framework and
then you wrap your process into hooks
you have an on before process that calls
to relevant hooks you have the main
process and on after process and you
enhance your business process by adding
methods as as code units that you can
run with a record parameter and on top
of that you need to include new
methods in your hook list now I since we
have events I do not recommend to use
this hook pattern on half 2016 I just
wanted to kind of show you that there is
always a solution there are patterns in
each kind of environment and and context
like event pattern and the hook pattern
solve the same problem and you always
need to keep track of whether your
business process has been handled by an
additional method or not we have seen
the event handling thing and that is not
a pro a pattern that I have invented
Thomas has shown that in his keynotes
I'm not claiming authorship to that so
that is that that goes to Thomas or
whoever he has stolen it from I don't
know no no he's believed but so just we
were just going a bit deep there are
several event types global events
trigger events business events and
integration events I'm gonna spend the
rest of my time on the difference
between business events and integration
events the global events are encode you
need one and that declared encode you
need one as local integration so events
so currently in in my view and I'm not
Microsoft there are no real global
events it's just an implementation of
local integration events they will
probably or hopefully become system
events at some at some point there are
trigger events you can call into tables
and into pages generically without even
needing to raise an event you can so all
triggers in tables on before delete on
after lead and so on the usual suspects
have generic inbuilt events that you can
subscribe to this this is true for pages
as well and this is true for record
changing stuff in pages but also for the
normal page triggers like open page
query close page and close page and and
and this stuff and on new record
the code declared event publishers
business events and integration events
we've seen that all events are declared
as functions events cannot have code and
events cannot have return values best
practices here very important publish a
local function on the object where you
need to raise the event always keep it
local astonishingly enough we have seen
that from an external object object I
can see these local events if I specify
them if I want to subscribe to them that
that works but I don't want to have them
global because then I don't know from
where people might be addressing that
published event it always needs to be
local only raised and a publisher event
once never raise it in two places
only once and stick meticulously to
naming conventions otherwise you will
not know what what you're doing with
with what what kind of event you're
you're doing events subscribers that has
been handled very nicely by Tom by Tom
wind what I wanted to alert you to is
these concepts of business versus
integration events that is very very
important the behavior right now it's
almost identical
there is no difference whether you call
them integration or business events but
integration of events are like your
normal help us to avoid code
modification standard objects and there
may be subject to change over time you
can use them quite freely but business
events should not change they define a
formal contract they constitute
something like a public API to your
vertical or some at some time to
Microsoft standard currently there are
no business events in Dynamics NAV there
is no single business event in Dynamics
NAV
so when should you in your vertical
introduce business events it's pretty
easy when do you introduce them you
break your complete solution down into
encapsulated methods again those of you
who know our trainings on structure
development methodology know what I'm
talking about each method is a code unit
of its own with only one global function
each method is only ever called from its
class and that's the
table and then you go and define which
methods belong to which overall business
processes and you can use business
events to create an API that gives X
external access to your processes and
what that means what you will end up
with is a business event API and that
will allow you to differentiate between
types of developers or types of
development you may have Co development
that changes your structure and your
architecture that only your senior
product developers are allowed to do but
if you have you have junior developers
or if you're working with external
partners you may only give them access
to your business event API and they can
do additional development which is
limited to these defined contracts and
interface points that are constituted by
your business by your business event API
that in my view Microsoft doesn't say
that it's so clearly now but I'm talking
verticals in my view that is what
business events are for to define fixed
integration points to your software so
that you can say it can can tell your
partner's ok you can change or add to
what I do but don't mess with my objects
you can only do what I have defined in
my business event API and you can code
against that but that's it
to me it's and pardon that expression
and are done to me that is something
like an internal service because it
defines a fixed contract of course it's
not a web service but the analogy just
to to make that clear where is it used
events already used in a million places
for erm integration for workflow and of
course for nav extensions and if you
have who has played with extensions
already ok not so many if you do you
might find that it does not actually get
you too far right now but I am sure
although I am NOT Microsoft and I can't
promise you it's not a functionality
that Microsoft has just thrown at you
and will never touch again it will be a
very important feature in the in the
future that Microsoft will be extending
and working on and it's one of the
reasons why we have events because nav
extensions the the option metadata of
your vertical is agnostic of nav
extensions that's why you cannot have
extensions that change existing objects
okay so how can you interact of course
you can interact by extensions that
listen to events that's the good thing
about the interplay between nav
extensions and events extensions do not
mean a thing or just simply do not work
without events and with that I have done
more than I wanted to I'm sorry summary
has talked about events use passports to
protect the sensitive data variant
facade you can use for a very generic
functionality that is products why data
dream box entry you can block an entity
by using the data dragon tri method
logging and error message processing and
the Namek request status for capturing
the filters so for the last thing is on
this link here we are publishing all of
the patterns so if you go on that link
you can find all of the information that
we have presented on previous events and
this one in much higher level of detail
and for the last thing I would really
like to invite you all to go there and
to check it out and to leave us feedback
so if something doesn't work well it
could be improved we need to know also
if you like something we would also like
to know because in general no feedback
is the worst feedback that you can get
because it means that probably no one is
using it so in general we are also
looking for both constructive and
positive feedback on things that we did
also on this page you can find the
template if you have a patterning idea
or if you would like to contribute to
the project there is a template and
contact people so you can also get touch
and touch with us through the page yep
so questions t-shirts we have five
t-shirts to offer so we are running out
of time and if you're cut off
feel free just to come down and we can
discuss me about this multiplication
addition thing who was that here's a
t-shirt for you many might come to
publish extensions so your question is
it possible to publish an event in
accession is this event the if I publish
an event in the in my extensions can I
access this event afterwards and some
other code how did we get so if he
publishes the event in the extension can
it be used by the other quote knows the
rest but the rest dose doesn't know the
extension yeah but I could make an old
unit where I put all the public events
and then give this one to like my
partners yeah and they can raise they
can consume these events I don't I don't
think that that currently works I really
think it's very strict here that that
only the extension can call back into
the existing code but the existing code
does not know anything about these
things and make an interface that you
can't make carry can't do that probably
never can
let the micro you can even tell me maybe
I can repeat last year that was said
that probably there won't be a try-catch
functionality or the helper and stuff
and now we shoot at all so I was
wondering what else can be expected for
next time oh that that question goes to
Microsoft
