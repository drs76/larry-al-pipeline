# AL Development for OGs

- **Source:** https://www.youtube.com/watch?v=dxmutcQcEh0
- **Video ID:** dxmutcQcEh0
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 93m30s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

[Music]
[Applause]
all right so AJ we got our Applause so
we can just go yeah we see we can go so
uh thank you for pronounce pronouncing
it okay it's OG's not ox or something
like that
um so yeah welcome uh to our uh session
uh I'm Waldo this is my
co-pilot yeah you see what I did there
right so that means anything I say can
be wrong yeah you're you are allowed to
be wrong thank you so much I mean I'm
good at where are we heading at we are
heading to software that's helping us to
be okay to be wrong right that is what I
see that copilot is all about but in any
case uh we're going to talk about uh
some Al development changes uh for ogs
OG's being original gangsters or
originally this session was called for
dinosaurs I can tell you uh look does
not like to be called a dinosaur and I
get it a dinosaur is extinct we are not
extinct okay we still matter so we are
still some gangsters I I like this I was
almost extinct yeah yeah yeah you know
what happen we have been doing these
sessions a few times and in Bangkok we
had a stage this High and AJ he he
decided to fall off of the stage well I
think he pushed me off so for throw if
he makes a move please engage yeah I
will try to be as far as uh as as you
can I mean okay so
uh one one uh request if I ask a
question I only see like 10% of the
people if I ask a question instead of uh
hands or whatever clap once for yes
don't do anything because clapping for
no would be weird
okay okay okay okay okay so how many ogs
do we have here how many people uh let's
say have uh five years of
experience 10 years oh 15 years you see
I'm still clapping my hands 20 years wow
years
24 what okay there are you you seem to
be in in the right in the right
session um so I think we can all agree
that things have changed and we need to
prepare for that future right uh so yeah
source code the language development
environment devops uh file what what not
things have changed even BC
Behavior has changed and for some that's
a little bit uh difficult to graas
sometime so few more questions first of
all who of you back in the days when
let's say Seaside Cal there are enough
people here that worked with Cil who
upgraded each customer every single
month W
no no way I don't believe that maybe
yeah maybe but I mean only a few only
one uh or two do you now know what waves
stand for
it's only just a few you mean I I I mean
these release wave One release Wave 2
2024 release wave two that we are
heading at are we heading at that yes we
are heading at that um I mean that's
just a Microsoft way to say every single
month we have a big release we announce
it only twice a year we call it a
release wave and then we just ship the
first version like 10% second version
10% third version 30% and I I don't know
if you noticed but about every single
month we could have breaking changes
breaking
changes also something that we need to
get used to a new
thing well waves break on the beach
so so who I'm a co-pilot I'm allowed to
say stupid things yeah yeah and and and
you feel fulfill that need
um so uh who of you back in the days Cil
development who of you did custom
development everyone obviously this was
what made
Cil strong and and Powerful we called it
Simplicity I think we all now see it as
stupidity who of you did back in the
days C code
reviews oh that that come on to be
honest who of you did code
reviews okay that's as much I heard
that okay that's good but not all of us
I didn't and also code reviews I mean
how do you do that if you don't have
Source control decent Source control how
do you do code reviews you just go into
a text file after exporting it from the
object design and then I mean search
like gazillion lines of code right it
was difficult to
do who of you did automated testing back
in the
days who of you is doing it
now okay much more that that's a good
thing that's a good thing and I I really
think we need that we need to live in
this new
world we need to do something like this
every single month we are being upgraded
every single month it it could
potentially be a breaking change by
Microsoft and I mean what is a breaking
change anyway if Microsoft breaks my
test all of a sudden that's not a
breaking
change because it's my test but in a way
it's a breaking change it's a breaking
in Behavior if Microsoft breaks tests
like their test or in the test framework
it's not a breaking change because it's
a test framework and they are allowed to
break test
framework but that's a breaking change
so what is the breaking change anyway so
we need need we need to prepare and and
you can already guess yeah this is what
that session is all about so things have
changed um and I'm going to I we are
going to have a co-pilot uh so if things
that are less important I will ask my
co no it's not that's not true sorry um
but I'm I'm going to yeah to go over
some uh points first point is how to
look into source code it was easy back
in the days in C we just open object
designer we go in uh in in in the object
we can change whatever we like we can
even do that in live environment do we
miss
that oh come on no we don't miss that
that's a stupidity part uh of what we
were able to do but obviously now we
don't have that database anymore we
don't have that easy access to um to to
to the source to Microsoft Source
anymore and there's so much Source every
single month there's a new update there
are like 150 apps from Microsoft how do
we do that so is anyone familiar with
this okay that's not enough so this is
already a good point is of you that's
familiar with this uh repository is are
you familiar with this
one less and this is actually what you
really need to look into um this is
actually a new repository I think it
exists for copilot two months three
months months months yeah something like
that I I like it if he's going to give
the answers to the
co-pilot um so uh Stefan Maron also
present here he has a session also I
think about uh validate uh
statement uh he created actually an U
repository where he exports all source
code from Microsoft pretty much every
single day
because every single day we get a new
version of of code I I don't know if you
know but and on PC SAS every single day
updates are being pushed yeah so you
have like a new base up every single day
multiple times a day even yeah we get
that all in this repository you see it
here I I have uh a GitHub uh uh
repository so basically just this link
uh you can simp simply clone that and
and use that I did that um and I must
say I I talked to uh sorry I open this
one I talked to Stefan yesterday because
I I I just cloned it and it didn't
really work anymore as as before like
there is there is a lot of branches
every single version SL localization is
a branch meaning you can really go into
the code the exact code that uh your
customer or you are working
with um so um and he he he pointed me to
a description online if you would uh
clone this repository there is a read me
to do partial clones as well so he
actually describes on how you can
decently use this I did that since
yesterday and now finally I can back go
into source code and do something like a
compare between what you see here
between like version 20 4 and V Next and
version 24 yes indeed V Next we can look
into what's upcoming we can look at next
minor we can look at next major v25 is
already in this repository yeah
unbelievably interesting so what I did
is uh in git lens a simple uh compare
let me zoom in a little bit because the
screen is a little bit small um and you
can look into whatever is coming obvious
obviously app Json is being updated from
24.2 24.3 in this case that's next minor
but you can look into code I'm not going
to go too far but you can you can really
see what's upcoming if you requested an
event you can check if it's upcoming
which release it's upcoming maybe next
minor maybe next major and all that
definitely something you uh can uh look
into go
pilot yeah let's switch so um
as you can imagine we uh just not
randomly but we picked a number of
topics so we're going from left to right
um exis
modifiers how many of you do know what I
mean with exess
modifiers that only a few in the same
place a good place that's that's good so
exis modifi we actually had that in C
already for a long
time um we know that a function when
that is not marked with anything it is
public and when it is marked as local
it's only local to the object that is an
access modifier we change the access to
that function with the word
local okay I would have like the term
private I would like the term public for
the functions that are public but okay
that is historically um and that is uh
probably never going to change
but there is more around exis modifiers
that we can do today they can be defined
at different levels we can Define them
at object level field level and Method
level um we can mark it as internal
which means only the app itself can
access it and no other apps which means
if we Mark our stuff as internal app
Source will not consider it breaking
change if you remove it not talking
about Fields here because fields are
still when you remove them still need to
be there as obsoleted because that is
removing data but removing uh functions
from code units are when they're marked
as internal are not considered to be a
breaking change which makes it easier
you don't have to obsolete them first so
this function here is only accessible
from inside the uh my own app and not
from
outside and we can do that on object
level as well now the whole code unit is
not accessible from the outside only
from inside my uh app which means that
that uh internal procedure you see here
is kind of duplicate the first do
something is actually also internal so
when we Mark a whole object as excess
internal it doesn't make sense to have
another internal procedure inside
it we can also do that on tables we can
have a table internal uh maybe Mak sense
if you have a setting table or some
table that you just do not want any
other app to make use of you mark the
whole table as internal and nobody can
access that
data you can also do that on field level
say hey uh this field some secret is
something I want to keep secret want to
keep inside my app so I hide it from
other apps that can also make a lot of
sense to do it like this so you see we
get more and more possibilities
here we can if you want make internals
visible to other apps uh usually test
apps so a test app can make use of or
should make use of our app of course
maybe you want to to have a dependent
app on App Source but as wo told me
previous time there are people that are
just removing your app then and trying
to create an app with that app ID that I
found so they can get access to your app
yeah you really need so how many people
are doing that here in the
room not too many not too many that's
good I do that but anyway uh it's just
it's it's a danger and you actually see
it as as a warning as well it is not
recomend recommend to publish an app on
App Source any anywhere actually even
not a ptef that has internals febles to
true I'm not saying you shouldn't I mean
for test apps we we we do that you need
that if you want to work with internal
procedures you still need to test those
procedures uh but it's a good practice
that when you build your app you compile
you build for however you do it that you
remove internals vises first and then
build your app and that's the one that
you release or at least if you put it on
app Source like this do not think that
you will then really stop other apps
from getting access because it is not a
security boundary that is actually the
message that's the message there is also
a local access modifier what I do here
on in this screenshot is that that some
secret field is now marked as a local
field and this locks or excludes anybody
inside my app so no object
can really access this field anymore not
even inside my app only the table itself
can access that secret and why would I
do this maybe because I want to
encapsulate how I Implement that some
Secret in this case is just a text but
who knows what is in that text it could
also be a key for key V it could be a
key for isolat storage whatever so with
the getter and the setter I make sure
that I implemented my way and I can also
change the behavior in the future and
not break anybody else because everybody
can use the get set secret and set
secret so this is also a possibility
that we have now with the ex's modifies
then we have protected only for objects
that can be extended that is basically
tables pages and reports which gives uh
access to your uh own app and the
dependent
app global variables by protecting it
you're basically giving it yeah exactly
instead of making them internal nice
word choice yeah in fact it's it's
inherited from net there you have the
same thing yeah so that makes it okay
yeah it's it's that makes it okay yeah
in my world yes okay so here we have um
an a page with some variables that are
marked as protected meaning you can
still not see them from the outside
world well could you even with global
variables but they are accessible from
the page
extension and that is actually what it
is about so you don't need to have
functions inside that page that set
Global variables Etc that's the ID with
protected
VAR and then we are to my
pilot code cops okay uh who of you is
using using Code Cod code cops are we
really are we really using Code cops uh
okay other question maybe who who of you
ever uh migrated your code from Cil to
Al and then switched on code
cops you like your
output I think many people of many many
of us actually just disabled them again
because uh it made the compiler very
slow you had like a
list of errors and and the next warning
or error you really didn't see anymore I
mean it was the one too many kind of
Errors so um yeah but yeah we didn't
have code cops at all back in the days
uh and that has been quite a change we
we should get used to that in fact I I
really would I would recommend to switch
them on and comply with with them at
least most of them yeah um I if you
don't know what I'm talking about you
can easily switch them on in the
settings file I usually just do it per
workspace that you switch it on in the
settings file and I set them all like
this code cup pendant extension cup and
UI cup and obviously a separate setting
to uh enable that yeah and you see here
already this is actually what happened
now when you migrate your code and you
have thousands of issues and maybe in
hundreds of or or tens of of code cops
fixing them is something you should do
because a code cup or a warning in a
code cup is only interesting when you
have
none because when you then create a
warning or you create an unused fa or
whatnot that's when you will act because
that's what you will see because all of
a sudden you have a warning yeah
your your co-pilot has a
suggestion yes can I make a suggestion
to you yes okay so because of
performance reasons it is better to
switch off your um background uh code
analysis depends on how big your
extension is yeah that is true so it's
actually in the uh performance guideline
to switch it off because of performance
that's this setting a background code
analysis and you can even set it on file
these days days so you actually only
analyzing your current file that you
have opened if you have an extension of
thousands of file files I would not
switch it off but I would at least set
it to files at least that whatever
you're working on that's that you get in
foreground at that point
okay uh but in any case do know um that
when you have these thousands of uh
issues don't give up you need to fix
them and to eant fix them what I would
say let's bend the rules a little bit
Yeah switch like have an analysis on
what all of your uh issues that you have
switch them all off like this one this
is one that I will keep in my Cod rule
set by the way I don't like Microsoft
deciding I name my variable I will
decide how I name my variables um but
yeah it's a simple rule set file you can
set up and you can simply uh again in
settings uh well refer to it what I
would suggest all of the settings you
have if you have thousands of warnings
put them all here and switch them all
off so you don't have any warnings and
at least the next warning you'll see and
you have a working list this is a
working list you can switch them on
basically by removing one rule set or
one rule one by one and you can start
just very efficiently fixing all the
warnings that you have you can focus on
all unused variables and then you can
focus on all next issues that you have
yeah that's how we did that and it was
actually quite efficient there is also
something that's called
pragmas be careful I mean this is this
is nice that we can give special
instructions to the Cod to the compiler
uh but you shouldn't be switching off
code warnings too much with with the
pragma you really need to have have a
good reason to use this one of the
reason I can think of is for instance
for opsolutions if you have an
Absolution that you still cannot fix
just because your code doesn't allow it
yet then you would be able to switch it
up temporarily a pragma in my opinion
it's always a to-do for later you need
to have pragma lus code at some point
that's clean code a code uh Code full of
pragmas is not clean code
so well you already asked the question
how many people are testing so that is I
think quite okay mhm but what is
actually
testing what mean what is testing well
it's kind of having criticism well uh
now it's called testing um before it
yeah it's called different right so it
just depends on the
context um
automated testing actually saves time it
doesn't cost money it saves time it
saved
money um try to sell that to your
manager yeah well I tried I tried to
sell that internally and the way how I
did it was just by saying okay Fe 24 is
around the
corner um all customers will be upgraded
to it in the next two weeks and and then
somebody said well but shouldn't be test
yeah we should test but go go
ahead okay um long story but at least we
have now automated tests so um all codes
should be or must be tested before you
release it and that needs to be repeated
for every single code
change all those tests need to be
consistent like you always testing in
the same
way and when you do this we have this um
way of testing that is kind of your
let's say your insurance policy because
then you know when you release the code
for the next version of your software
the next version of business Central it
will be right it will be working that
doesn't mean that customers should not
do some acceptance testing if it works
as they expected I mean you can write a
test and a test might still be wrong
because you're testing this the the
wrong thing you're not testing how the
customer would expect it to work but at
least that you the test you right is how
you think it is going to
work um so test driven development will
mean you write a failing test where you
start with then you make sure with the
code that the test passes and then
finally refector the code maybe um you
need to put something in and structurize
the code in a different way um that's
all fine as long as the test pass that
is how it works um even if I have to
refactor some code that is already there
for a long time uh where we don't not
have automated test for yet I start off
with writing an automated test make sure
the test passes and then I start
refactoring the code that makes sure
everything is still working
maybe before we continue uh because I
know it is a problem who of you have a
problem in convincing your management to
do automated testing you see that that's
for me like an insane amount of people
uh one or two would be fine this was too
much and uh maybe I mean I don't know if
it's a tip or not but I have been I mean
we were're fortunate enough to be able
to convince uh internal to do automated
testing at this point we have about like
eight or nine th000 tests uh for our uh
product and uh what I do uh I send every
single bug that we avoided because
that's what I want to know what did we
avoid you don't know what you didn't get
you cannot report the time you saved
because it didn't happen yeah but at
least you can see like hey I had failing
tests and it was a bug maybe because of
Microsoft I reported look this is what
we saved uh maybe of your your own code
changes hey look that is what we saved
and at some point um I I had this uh
previous days I I I I used this example
as well we had uh by simply adding one
field to a table uh in a customer
extension about 100 or 200 tests fail
just adding a field to a table and you
might wonder like how on Earth can a
test fail well simple it's uh it's it's
it's transfer fields and I had all my
copy document stuff
failing and by the way there are like
there are more
than more than 100 copy document
combinations that you can have and they
all failed in my opinion so and not
opinion what happened so I keep on
reporting that look this is what we
saved this is what we saved and and and
that is one thing and the second thing
is uh at some point uh you can also
report the time you actually only need
four upgrades we're upgrading every
single month and it shouldn't take too
much time and if you can compare that to
back in the days we're all ogs we can
compare that to back in the days look
what time that we save for for uh for
upgrades that might be like maybe a tip
as well I keep doing that like look this
is a good thing automated testy we do
that and this is what we gain from it
maybe uh we should have a session at a
partner conference to convince all those
uh non convinced partners I I hear it
too often like yeah but management
doesn't want to want to pay for that or
yeah or customers doesn't want to pay
for that when I'm like yeah but we are
in this ever changing world we are in
this always upgrading every month kind
of thing and you want me to do a good
job and not
test I don't see
it all right so breaking changes another
reason for us to do automated tests
actually so breaking changes
um what we or what Microsoft is doing
and what we should do is that code is
always obsoleted first what Microsoft is
doing in their code is that they
obsolete a code and then after at least
12 months sometimes longer the code will
be cleaned up so you find something in a
code like uh like this um what you see
here if not clean 20 uh Obsolete and
then replaced by um funny thing here uh
now you suddenly need to need to know
what is a list of a dictionary um that
really redesigned this piece of code
create dim what we are used to for
decades sometimes uh features are being
uh deprecated or
replaced um that is also
documented documented in different
places to be honest because there are
deprecated features in the application
there are dicated features in the
platform in the system whatever there
are different places where deprecated
features are being
documented uh so here we see that uh in
2 years from now API V1 will be removed
um the funny thing is that it says in
the title removed and then in a column
moved removed or replaced is being
replaced so what is it going to be
replaced or removed uh anyway in this
case it is actually replaced by V2 um
already a long time ago but okay um API
V1 will just not be there so um will be
removed it's like sales prices no it's
it's already deprecated for a long time
it's not removed redesigned feature on
hold on hold your horse about price
module so we also have um this one um
deprecated feature this was announced in
2023 relas W release Wave 2 so half a
year ago schema version for custom apis
from schema version V1 to
V2 and in version
24 it was already applied so this was
not a year in advance it was half a year
in advance so just saying that in this
case they did not just break a feature
they also break the promise um to have
it one year in advance just saying
sometimes that happens so you really
need to pay attention and this schema
version was is a bad thing actually
because it breaks all your um
Integrations with custom apis including
power automate Stuff Etc at least I have
heard a lot about
it um then we have uh redesign features
so they're going to replace something
with something else sales prices was a
module that they promised to uh
replace well that was a bad promise that
was a bad promise and they are still
promis
it sometime it's in the I don't know
distant future it's going to happen um
you were begging them to to to keep
sales price right I still think it's the
worst idea ever to remove all sales
price so many people think uh like that
I'm quite convinced that there will be a
like Anarchy uh or some kind with any
kind of pte extension for customers that
developed their own extensions on Old
sales pricing and are totally not into
testing and continuously upgrading and
all that things and now all of a sudden
we remove that and automatically upgrade
to new version n no I don't think I
don't see it and then we have this this
one you see here on the screenshot
called GL entry aggregations when
posting invoices and you may think
that's not from me but what's actually
behind it is the new invoice posting
engine and the new invoice posting
engine means that they take a serious
amount of code out of code unit 80 and
90 I'm just saying 80 90 here for the
ogs because you all know what that is
they taking out the code of sales post
and purchase post and put it in a
different code unit which they call the
invoice posting engine including all the
events that they originally had in code
unit 80 and 90 meaning that it breaks
all of your uh event subscribers to well
most of them to code unit 80 and 90
because you know need suddenly subscribe
to a different code unit and to make
that easier for you um the uh events
that they passed into copied into the
other code unit are not exactly the same
of course not why so this is not this is
an example where it wouldn't be a
breaking change it would be so yeah so
this is an example where you actually
read to need to read very carefully what
is in the description what does that
mean for me and that really can
recommend you to do that um and then oh
horror the invo posting engine was uh in
the first place only uh available for
sandboxes to be enabled in a feature
with feature management so you could
develop for it but it only worked in
sandboxes and then it's going to be a
feature that is going yeah yeah
customers can enable it in feature
management can you imagine that that a
customer switch it on while you were not
ready to support it well that is a
horror scenario so be careful with all
those uh uh documentation read it and
really think about it how can I prepare
for it how does it really uh touch my
code affect my code Etc and maybe you
need to support both old and new feature
which could be a reason for the prma
because if I support a new feature I do
want not want to have the messages from
the obsoleted code because I support the
new one already but hey yeah the old
stuff is still there so then I put a
prma around reason for a PR yeah and
then we have sometimes have new features
um so yeah that can have an impact on
your customization so Microsoft as a new
feature said we have new terminology for
project management so everything that is
called jobs is now called projects in
the UI so any Fields you have that is
related to jobs should be renamed to
uh or at least the caption uh renamed to
uh to project well that's quite an
impact of course on your code and
sometimes these kind of features are
also enabled with feature management not
this one that's just they upgrade and
they get a project
everywhere
so for breaking changes test test
everything yeah next topic performance
question do you care about
performance do you know what locking is
do you
really people not sure about
it a little bit less uh so uh a few
things uh when we talk about logging and
and business Central I mean wow things
have changed things have changed finally
yeah I'm going to just touch some Basics
uh uh business Central out of the box if
you just read it does dirty
reads okay so kind of like meaning we
are reading uncommitted data that's how
it is did anyone ever care no we didn't
it's how it works and we don't really uh
are are let's say are that uh focused on
it like oh you should be dirty uh it's
fine nice thing about un uncommitted
threats is that we can
read even if the data is locked yeah
okay read committed would mean that we
cannot read the moment that the data is
locked we need to wait until the data is
unlocked and then we can read and while
we reading we are locking in a shared
lock so we can kind of like let multiple
people read at the same time and
committed data but at that point again
another the transaction is not able to
write yeah so we are locking at that
point that's a read committed okay so I
think we need to be happy that out of
the box everything is read
uncommitted and then we have update lock
that is pretty much uh from the moment
we start to write uh we are locking
until the end of the transaction uh the
resources that um that we wrote okay we
can do other things we can basically
push uh business Central to lock until
the end of transaction even then you're
just reading yeah okay now we know this
let's do a
quiz so uh when you look at this
fantastic piece of
code
which let me just I mean it's just three
steps if I do just a read operation in
this case a fine last yeah that's as I
said out of the box and read uncommitted
yeah and then down the line there is
some kind of right action like in this
case an insert at that point and I'm
talking here preion 23 you very
important yeah not version 23 or
later um
then all of a sudden uh or or uh after
that right onaction uh we are still in
that same transaction there's lots of
code and maybe there are some kind of um
subscriber event whatever other app that
is hooking into our code and does a read
operation uh on its own preion 23 this
code would it be read
committed nobody okay read
uncommitted no that's an update look
like for 25 years and more maybe uh this
is how now vision nav business Central
worked yeah it was actually what I call
a pessimistic
log because that's as pessimistic as you
can get was not really a problem back in
the days because I mean we owned all the
code it was in the database we could see
it we could read it and now we don't
really own all the code with all these
apps anymore we don't really know who is
uh subscribed to events anymore so yeah
again back in the days we have log table
okay so pretty much the same this by the
way is good practice back in the days we
couldn't say like find last true to lock
the last record if we would modify that
last record we would set lock table and
then find last and then it would lock
that table so that would throw an update
look question what would happen on the
get again after in the same transaction
who says update
lock exactly both of you were wrong oh
were right
yeah so again pessimistic locking yeah
until the end of the the transactions
from the moment I have one lock it will
just lock anything I read in that same
table okay that's how it has been for as
long as we could remember up until
version 23 so things have changed since
version 23 um this get is going to be a
read committed so out of the box we have
much shorter logs and by the way can I
just show off this uh visualization
again I mean I'm really proud of that
but in any case uh it's going to be a
read committed now meaning the shared
lock meaning multiple people are able to
read this resource including me and I'm
only locking this for the amount of time
that I'm reading it not until the uh end
of the transaction much shorter locks
much less locking Behavior yeah uh lock
table
again this is what we wrote We converted
the code to version 23 we know that in
the fine last it's going to do an update
lock but who thinks now in uh in the
last uh statement locking Behavior has
changed version 23 so who think still
thinks it's going to be an update
lock yeah
exactly if we now use lock table
anywhere in code we're going back to the
old days
yeah lock table was a good practice back
in the days lock table is bad practice
and when you look at the code now if you
have lock tables in your product in your
uh pte I would strongly advice to kick
it out yeah you are going back to the
old days by simply uh and uh doing lock
table we have a solution for that it's
called read isolation with read
isolation I can do stuff and doo I see
you this is a wrong example but it kind
of like uh shows what that you can even
uh overrule when you're in that old mood
so again I do a loog table and find
class I know that's going to be an
update Lo and then I set read isolation
to something else in this case read
committed and I overrule for this
variable the statement to read and
committed so even in that loog table bad
thing you can overrule it to a good
thing yeah um where where is this
significant just imagine that the first
two line is in in an extension that you
don't own you cannot change that code
but at least your own code you can still
decide on how the Locking uh isolation
or the read isolation needs to be yeah
this is actually a very important change
uh that has happened since uh then now
I'm I'm showing this with f so this
basically when when you think about read
isolation you think about find and get
but reading is much more than find and
get this is an example is empty yeah uh
as empty is like a very cheap statement
on SQL server but is it really if is
empty if it's not empty you're still
reading records and it's locking those
records yeah I would even claim that
most or at least a lot of the um of
Deadlocks that we have and lock timeouts
that we have have is because of his
empty it's because of calicum it's
because of counts these are three
examples of things that we don't really
think about that it's also re operation
it's absolutely re oper operation and
back in the old days it's gone lock as
well yeah and that is just a very
important thing uh to to remember so
things have changed once again we are as
ogs yeah this is a very important thing
we need to understand in my opinion so
uh before version 22 uh we had this
pessimistic loing and then in version 22
we had this ability to do read isolation
but only that so manually we could
overrule that isolation level and then
since version 23 we have it yeah I I I
have that in slide as well so I call it
pessimistic locking then the the real
term is two State locking we have two
states of locking back in the days
either it was update lock or read un
committed yeah
then we have the read isolation good
practice I would even claim whatever
read isolation or read that you do any
kind of read gums up until find find set
find last get even uh up until is
empties always provide the read
isolation always you are the developer
you know what you're going to do with
that
data and if you don't maybe there is a
job offering in sales
sorry uh trate locking that is the new
uh um let's say behavior that we need to
enable by the way if you're upgrading we
need to enable that in the feature
management but when enabled uh well then
uh business Central behaves differently
it will lock less it will do shared
locks it will do read uncommitted and so
on uh and so on only this upgrade uh we
we basically cut down dead locks about
90% simply by this
upgrade no
joke okay there is an entire session
about this on Friday if I'm not yeah
Friday at 1:30 uh that handles this uh
Tri State locking in full and it will
obviously go much more uh into detail
than I just did there is more in terms
of performs have have you ever heard of
partial
records come on yes you you heard about
it and we talk about partial records I
mean back in the days when H when we had
this uh this um uh companion tables was
called every time we had a new table
extension there was a new table
companion table to the original table so
if you have five extensions all
extending the sales header you had six
sales header tables and while reading it
would join all of these tables and you
can already guess the more tables the
slower it got so a solution was
implementing set load Fields there we
have
it I would even claim every single read
operation you need to provide set load
Fields if you went to my uh performance
session like a few years ago I have no
idea how many years ago that was was
anyone there oh a few okay I handled
this actually in full I will have a
screenshot about that as well and you
could clearly see that having uh said
load Fields was a big performance
Improvement you could even see that you
if you weren't able to predict what
Fields you had to load and you would
turn into a jit load just in time load
like get me all anyway although I
already got a few of them that it was
even faster still than not doing a set
load Fields so set load Fields good
practice Yeah is it still a good
practice I would claim yes this is a
screenshot from back in the days same
screenshot that I used uh in that
session and you could see and will try
to explain um so this great test is a
test with two table extensions and the
two table extensions with no sorry no
table extensions and no table extensions
with setled Fields this is two table
extensions uh four six eight table
extensions so the more table extensions
I had slower it got if I didn't apply
set load Fields yeah
now since version 23 things have changed
uh also that is one of my favorite new
features we don't have all these
companion tables anymore so Microsoft
now combines them into one companion
table for extension objects and just the
main table for the main object yeah so
we have at most one join and joining two
tables together and then you might say
like okay I don't need set load Fields
anymore yeah you do you still do you
still do because you're getting all
those fields every single time and you
don't need them so uh this is just
having multiple uh table extensions
pretty the same as this one the same
test applied to version 24 I think this
is uh or version 23 uh and you see you
need to look at the scale the scale is
much bigger here uh and that it barely
is slower but it's still twice as fast
when you set Lo Fields so please these I
would even claim always set load fields
we already have set load fields and read
isolation that we need to provide with
every single read and then there was Cal
Fields gal
Fields yeah are we going to do it yeah
of course let's do it let's do it I
would claim and he is going to overrule
that claim that you won't never need GIC
field statement anymore are you sure
about that oh oh I didn't expect that
question are you
sure uh no I'm not sure um okay so I'm
going to say one word blob blob yeah uh
so a blob field sure if you need to
calculate a blob field in an autal
Fields bad idea especially in in in in a
big list so sure for blob Fields use Cal
fields for any other just use aut calic
Fields so now we have three statements
that we really need to look at for every
single read operation yeah
next we have uh data access intent do
you know about
this that's not enough absolutely not
there is a lot that we do in Pages apis
uh that actually is just reports that's
actually just meant to be read we can
set the access intent to read only so
that online it will just read in an a
secondary note it has not really been
working the last couple of versions so
uh doesn't really meted for this version
but it's a good practice to apply that
in code and do know you can overrule
that you set the intent in code and you
can overrule that in the
app now getting all this now just
imagine devops
yeah the this is a lot of code changes
this is we have been going through some
phases as developers right um so yeah
you should implement this code review my
question
right in in the beginning of the session
you need to do this code review code
review gives you quality code review
gives you a
moment you can check these things we do
code review every single pill request
all pill
request all of
them sure we don't look at the 1,000
lines of code in the pill request but at
least we can filter on all the finds and
all the read operations and see they
provide uh the sorry read isolation all
the reads did I provide read isolation
did I look at the G Fields do I find the
G fields did I change any any setting so
code
reviews is for me one of the fundaments
to get quality on your product and annoy
your developers right and developers I
mean it's it's one of the things that
gets me to see what level my developers
are and if they need extra uh knowledge
or
courses or whatnot yeah and in this
everchanging thing I'm I'm talking
version 22 version
23 24 I mean it's always a different
thing we need to look at so you need to
constantly change all these behaviors so
yeah it makes all the sense in the world
now uh there is a tool set for
performance obviously Business Center
Performance to Kit I want at least 50
hands now that knows it oh okay there
were a few not that many I did uh a
course about Business Center Performance
to it the last couple of days uh I
really think this is I
mean is going to change our way on how
to prepare for performance issues uh but
we can be uh ad hoc as well with the
performance uh analyzer we all know the
inclin performance
analyzer okay that's good uh teach your
users and teach your Consultants so you
get dat to analyze from the moment there
is a performance problem yeah you might
not know the BCP to mine but you do know
Telemetry and if you don't tomorrow
there is a
session on Telemetry by a weird
guy uh yeah your
turn right so that's quite a
story
interfaces uh actually almost don't dare
to ask how many of you are really into
interfaces not so many as I would expect
it's also based on the small survey that
Chris did earlier um so yeah when you're
looking to know what interfaces are
maybe you are curious um then yeah you
get some statements on the documentation
uh in a in a example like this code with
the I address provider and stuff uh um
and that you have a polymorphic way of
calling objects um that implementation
depends on an object and whatnot it's
kind of a let's say a little bit
confusing or at least a lot to take in
and even when it comes to combination
with enums people are struggling how do
interfaces code units work together and
how is that related to enums so instead
of doing
um uh 25 slides about it I decided to um
go with some examples in
code
um let me zoom in hope this is readable
for everybody in the back can you see
it okay perfect thank you so what I have
here is an um piece of code where um was
as an example and this one is a setup
table that um gives the user the option
to store files even on on either on on
Dropbox or Google drive or SharePoint
and there is an option here um so the
user can choose one of those three
obviously there need to be some extra
settings attached to that but that's not
what the example is about um and I have
a um connector code units for Dropbox a
connector code un Google Drive and one
for SharePoint and there we have very
simple implement of saving a file
getting a file or deleting a file and
the same as uh goes for Google Drive and
the same goes for SharePoint and to
choose which code unit should be called
I have a file connector code unit where
based on the um the
setting um I say well if my option is
Dropbox call that code unit and Google
Drive sh on same way so this is already
a little bit of structured code maybe as
far as we could get back in the C days
and maybe you were even proud of it that
you built something that was structured
H like this I mean I've seen worse code
actually so um the question is actually
how can we extend this how can we um
make this code better I can promise you
at the end of of the demonstration
there's just going to be one line and
not uh this whole uh piece of code um
you want to say right yeah it's
what you what you heard right I
heard so
um come
on I'm trying to have a story I mean I
can push you off stage I mean this is
quite fine pretty close pretty close now
so um what if you want extend this what
if you want to test this what if you
want to well um let's first look at uh
extending
um for example with an event we add an
event on before save file um and then
somebody else some other app could say I
have an integration with a different one
and I overrule your setting um so I said
it's handled to true in fact this whole
on before with is handled is something
you see a lot in the Bas app to me this
is an anti pattern this is not a good
pattern um because this pattern could be
abused by all other apps overwriting
your piece of code um they're not
respecting each other's uh uh existence
so U they think I'm alone in the world I
said is handled to true and you have no
idea who actually did it Etc so you
cannot really control
it um so the question is how could we do
this in a better way well the point is
that um this option field cannot be
extended back in the days in C when you
had access to the source code you could
add uh a comma to it and add another
option simple um I guess you all
remember the practice second that's good
practice that was a good practice always
I mean 10 I guess you all remember the
report usage table with the usage field
with I don't know 25 options and when we
wanted to add another option to that we
added 10 commas who did that exactly 10
exactly right yeah 10 yeah we all did 10
commas and then we added our own option
and then at some point because why did
why did we do that because Microsoft may
add one other option to that list as
well right so they had 10 uh places to
fill then gaps then Microsoft came along
and they said well we're going to add a
new option to the uh usage field you
know what they did they added 10
commas that really happened no joke
there not a joke it's anecdote and I
asked them why are you adding 10 commas
they said well maybe the partners have
added an option there no yeah okay stop
thinking for partners just do your thing
and we'll manage we have your back real
think for you this really an anecdote
that happened I don't know how long ago
but Shores is born right yeah anyway so
um we have these days instead of options
we have an enum so let's go with uh
enims so I have now an enum here with
the three options I added a non option
as well um and I made this enum
extensible meaning that I allow other to
add their own values to the enim so the
table is now based on an enim instead of
an option and how does that look like in
my code well slightly different I don't
have an on before I just follow my own
three options and if none of these
options and none of these values were
actually the case I call an onsave file
so some other app could then take it um
see if it was their option yes or no
most probably they don't see any other
option anyway so only they can see their
own option and mine of course so it's
slightly better but we are actually not
there yet um the point is this whole
case
statement with if this is the option
then call this and this and this that is
actually your red flag that's a flag
where you should think hey wait a second
I could have an interface here a case
statement is an indicator
that you could apply an interface and
why is that you're going to make a case
against
Case exactly a case against the case so
what I can do here look if you look at
the code here it is save file save file
save file they're all have exactly the
same signature the functions same
parameters even the same name I mean the
same goes with a get file the same goes
with delete file all exactly the same so
if we look at those um
code units they look the same they have
something in common yeah they have the
same public interface what you say they
all have messages yeah they all have
messages yeah exactly I could have made
one code unit maybe uh so they have the
same interface the same public interface
and that is where the interface comes in
so going to change this to an interface
I need to
reload which I had a shortcut for I can
really recommend that so I have an
interface and what is an interface an
interface actually you could say an
empty code unit there's no code in an
interface and only the definitions of
the uh procedures the functions that you
want to have um the name of the
interface I was happy to see the fincent
this morning in the keyote was also
using the same name and Convention
starting with a capital i that is what I
do in net world so I can see where
Vincent is coming from um I and then the
name and I don't waste space so no
spaces in the name intended so um this
is my interface this is how my code unit
should look like now well the idea is
then that in my code unit I can say this
code unit implements that interface that
means if I specify this that I must have
exactly the same functions I may have
more but at least the functions defined
in the interface should be there so as
soon as I uh delete one of them I get an
arrow message saying hey your um
interface does not your code unit does
not implement the interface member save
file so it must be exactly that well
what is the benefit of that that is um
in my
code I can have an
interface and the interface itself if I
look at I file
connector then I see delete file get
file save file I see exactly those
function so in fact I can just call the
function on an interface object however
if I do it like this I call it on the
interface then uh as the first line here
this line is going to throw an error
because it has no idea to which code
unit it needs to go to there's still a
code unit that really implements the
interface so calling it directly on an
interface that is not initialized with
um if a code unit behind it is going to
throw an error that the interface is not
initialized so what I do here is I
assign something to that iFile connector
interface and that is a function I just
uh put it into one function so it could
reuse it in the other um functions as
well and this function is returning an
interface but what it does here is
reading the setup and then say well if
it is drawbox I assign this code unit to
I file connector and if this code unit
is not implementing that interface I get
an error message saying hey this code
unit cannot be assigned to the interface
because it's not implementing the
interface so I cannot represented with
an interface
variable so I have a function still with
the case statement but at least I have
now one line of code to get my code unit
and then on that interface I call the
function of and it will then be executed
by theod code unit that I assigned
here now this case
statement is something we want to get
rid of because this case statement still
requires an event and this case
statement is actually the link between
the enum values and the code units that
implement the interface for that
particular enum value so actually this
is the link between them this the magic
what we're actually going to do is to
delegate the whole case statement to the
server to business Central in the
background and that is possible by going
to the enum and say hey enum you
implement that file connector as
well and then for each value we must
Define that the implementation of I file
connector is going to be drawbox
connector so what we actually doing here
on this line is saying if there is value
drawbox then the implementation of the
interface will be this code unit so
instead of the case statement we link
those values in our definition and as
you can imagine we do this for all the
values and if somebody extends the code
unit so extends the enim they have to
provide their own uh inter their own
implementation for the same
interface so let me um get rid of this
and just switch let me go to inum with
interface
um no I want to come on do this
come there we
go and look at the enum with interface
so this is how it looks like um and now
I have for every value said well this is
the interface I have even this is the
implementing code unit I even have a
default implementation for those that do
not have an implementation they go to no
file connector and then look into the
code unit it's all different I only need
to assign my enum field to the interface
and a whole case statement is in fact
now done in the background by the AL
runtime looking into the values hey this
is the interface you're looking for this
is the code unit that connects to it so
that implements it and here you go
automatically so after all um I have
still two lines of code but I could
actually write something like this
success is get file connector do save
file file name oh this is deleted file
come on save file there we go
so just one line of
code pretty easy isn't
it the point is then this iFile
connector does not have a value not have
a state I I'm not using that as a
variable so it depends on how your code
should work maybe you should call
multiple functions on that interface in
that case you should not go with the
oneliner
so there's one thing left here and that
is
testing what if I want to test this code
what if I want to uh mock the response
that comes from that code
unit well this function here is now um
responsible for getting the
implementation I want to reverse that I
want to tell save file use this
interface and then I'll actually use
this code unit for the interface so if I
pass in this as a
parameter rather than letting him read
which code unit it is then I reverse the
dependency to the calling party and for
a test function that would be ideal
because then the test function can say
hey use this mocking code unit that
actually mocks the response that you get
from uh Google or drawbox or whatever
because we're not going to test really
the API we're going to test how you
react to whatever drawbox can come back
with and that is uh the final part here
inversion of control so here you see the
save file where I insert iile connector
as a dependency dependency injection
this is actually called um so I can just
call it on this on this one I still have
the save file itself as the default one
so all my code my normal code works this
function is still um responsible for
getting the default implementation but
test code units could call this one with
a different implementation for this um
interface and this is what we call
inversion of
control and actually there is another
session in the same time slot with sorry
for that but discussing this session
from Veo I can really recommend you to
watch the video of that session because
it will really worth it and now at least
you probably understand what it's all
about okay so there's a little bit more
to uh interfaces in the next version we
are able to extend interfaces and in uh
the keynote you already saw the keywords
is and as for testing and casting so not
going to uh d into that um you have seen
that this morning so I can switch over
to our
pilot name
spaces ever heard of
it using
it
honestly honestly come on so you are
already using name spaces in business
Central okay that's that's for more like
it so yeah namespaces in business
Central now we have namespaces who of
you thinks this is the solution for
object
IDs it is not sorry
to um and it's never going to be and I
strongly believe we're going to have
object IDs for a long time but maybe
it's going to be a solution for
something else like prefixes right
because uh this uh namespace thing is
actually just there to logically uh
group and Order and uh our code in code
yeah
um mainly now to prevent um naming
conflict so sorry I'm not showing that
just yet so if we go a little bit into
code what should stand out of this uh
piece of code is I'm just created a
customer table were we ever able to
create a customer table no but we can
now so uh basically we can now put
object in our own namespace which I
obviously did and namespace OG demo
Waldo namespaces and yeah that's
probably going to be the next part like
how are we going to name our Nam spaces
and this gives us some opportunities
just to show you a few things if I would
not put this object like in a namespace
or would Define a namespace obviously I
have a problem because there is already
a customer table from Microsoft right um
and if you then look like in in this
case um oh yeah that is the other way
around if I would Define my new object
as being in a decent Nam space Dino no
OG we are
OG's um then all of a sudden you see now
I have a problem with vendor I cannot
use just the vender table anymore I
really need to Define where that comes
from because I'm in this Nam space
space yeah I just made that up um in any
case it will tell me like yeah this
Fender is is not there and I can include
uh the usings and basically it will
discover like where do I have a vendor
table oh in this names space and you can
add that names space you can even do it
a little bit different like uh if you do
not want to use the
usings you can just do something like uh
the fully qualified name uh right into
the name space vendor. vendor ven V yeah
umti and if you would really like look
into Microsoft they really
go wild use use things I guess um and I
went yeah went crazy on the Nam spaces
but that is actually the next uh
question that we need to ask I can I can
uh imagine a world that this is going to
be mandatory that we need to use ra
namespaces I can imagine that at some
point there's going to be a code
cup that says hey upsource cup like hey
yeah there's no namespace so there's no
up for you uh so we need to look into
how we're going to do that and that's
why I didn't really believe that anyone
or at least not too many people are
already using namespaces because we
really need to think this through how
are we going to organize uh our code now
all of a sudden because changing in
namespace is going to be a breaking
change you have one chance you can only
organized ones let's say so think about
it yeah there are some some guidelines
some premature guidelines uh here and
and I'm honestly don't know yet myself
uh what would be a good guideline like
my company. upname do
something or or why why company. upname
uh I don't know uh we'll
see but if you decided there are I did
some put some uh links on here uh
um there is an an article from Microsoft
uh that uh if you would like list all
your objects in an Excel and you would
tie an object name or or sorry namespace
to that there is a script that will add
the names space in all of these objects
of Powershell script if that works for
you um not for me not at like at least
not yet um and I mean I I provided this
blog post that I ever did like to easily
find find an object name uh in vs code
for you to find kind of like do a find
replace I don't think this going to work
either I just wanted to put my blog
somewhere I guess in any case there is
going to be uh a session on Friday again
from Microsoft that dives deeper into
Nam spaces and there is even in the
title and never dare to ask so maybe
there are some uh answers to questions
we even didn't we we didn't think of uh
in a way last topic of the day
and I think we will have time the whole
day well depends a little bit it's going
to be noon
soon um so devops
um let's dive a little bit into devops
and when I talk about devops I'm not
talking about Azure devops this time do
and does anyone
remember oh wow yeah we're OG's
right so this was kind of like I think
one of the most used
uh solution to do um let's say Source
control in Cil to do any kind of control
of source in
C yeah and yeah well om is old and we
not using that anymore um but we still
have devops or at least an approach to
do collaboration automation continuous
integration and delivery and what we I
what I mean with that is the
collaboration part we need to have some
kind of system that tracks whatever we
need to do change control we need to
have some kind of automation wow we need
to have some kind of automation that
does automated stuff like validating
remember what I said like code review
maybe we can automate that a little bit
implementing code cops is a form of code
review yeah you see here P pcpt Business
Center Performance 2 Kit could be an
automate an automated part that runs and
basically helps you predict performance
problems yeah so we need to have let's
say let's call them
pipelines wow I'm really messed up in
my automation here anyway um continuous
integration so we need to have these
build remember that I said like these
internals visible through is May or
internals visible to is maybe not a good
setting you might want to remove that
well then we need some kind of stins
let's call it a build build that build
changes and whatever builds our app the
way needs to be built like signing as
well is part of the build yeah and we
need this continuous uh delivery uh
publishing app can I ask who is who who
dares to say the truth are you
still uh uploading your app through that
page upload
app yeah yeah there are quite some
people still doing that and actually the
goal should be that you don't that
should be
automated so yeah devops uh can
certainly and I'm again I'm not talking
Azure devops I'm talking about a system
that can help you uh do that a devops
like Azure devops is actually some kind
of remote and it's all starts with your
repository yeah you need to set up your
repository somewhere let's call it
GitHub let's call it Azure devops but it
needs to be somewhere and on some kind
of system that can do stuff with that
yeah and when we can do stuff we do
stuff and I I just have a few examples
like next majure remember we are going
to upgrade every single month so we
might want to be prepared for the next
month not just the next major also the
next minor yeah and these are all the
kinds of automations that we need to be
able to set up yeah code cops there's a
lot to say about code cops I said
a little bit another bit would be that I
showed you a settings file maybe you
should not be setting that up with a
settings file it needs to be pushed it
is an policy from the company that sets
which code cops needs to be uh met with
that's not a setting on on a workspace
setting on the workspace is a setting
from a developer yeah so you should
actually set up as a policy as part of
the pipeline hardcoded thing like just
an example here you that that you decide
these are the code cups this is my rule
set on some kind of uh central place
that all my pipelines download the same
rule set so I comply with all the same
rules yeah how I my pipeline acts which
when I fail meeting one of the rules
what what is a warning is that really a
warning
no a warning means that I did Dirty code
smelly code
so I'm not allowing that so what do I
want to do when a pipelines gets a
warning of my compile I fail it's a
warning in a code cup is a failed
compile yeah so dependencies a lot to
say about dependencies as well and and
all again things you can set up as a
policy dependency in the app Json is for
the
developer dependencies in the pipeline
is for the policy I don't want my might
develop to just add
dependencies this is a conscious
decision you need to do that on on a
higher level on a design level an
architecture level needs to be validated
if just someone can add a dependency and
the pipeline says well there's actually
dependency I will take the
file then you're going to end up with
spaghetti again adding is dependency
needs to be a very conscious choice I
would also do that within a pipeline
yeah breaking check changes AJ uh talked
about that but how do we handle that
again in an Automation in the pipeline
simple actually install the previous
version of the app install the current
version of your app make it upgrade and
see if it works if it doesn't probably a
breaking change or maybe your upgrade
routine doesn't work yeah these are all
things you can do in your pipeline AB
Jason I told you about internals visible
too but there was actually a lot more
think you need to set up as a policy as
a policy for your app how do you handle
versions you shouldn't be handling
versions as a developer it should be
handled on on a much higher level and
just push that it shouldn't be like
these resource exposure policy it should
be hardcoded on policy level let's say
which is uh the pipeline same for
application Insight key I want to manage
that not app per app I just want to
manage that for every app my my company
we have 50 apps for one product honestly
I'm not going to manage that on on app
level that's that's too much time
internal visible too we should have some
kind of way to handle that again all of
these is app Json you can script that in
whatever like in Powershell it's just
Json manipulation um pre-processor
symbols a very good example uh at some
point when you start to use
pre-processor symbols which makes all
the sense in the world well yeah then
one pipeline might want to build next
version the current pipeline might want
to build the current version and maybe
another pipeline might want to build the
Belgian or the Dutch version which might
be the same code base but different uh
processor
symbols and then uh yeah I have no idea
what I meant with this but you can track
source build metadata as
well I really I didn't I don't remember
so um automated test an obvious one AJ
talked about that you need to test
obviously just having test and being
able to press the Run button doesn't
make any sense you need to do that in an
automated way maybe every night maybe
every build um very simply what what we
do is with the 50 apps we build one app
and we run the test for one app and
every night we install all apps in one
environment and we run all all tests in
that environment from all apps so we
kind of like have the isolated test for
one app and we have the it's not really
an integration test but the test when we
integrate all apps in one environment as
well it's different context so and gives
you much more possibilities and and and
fileb backs and this is just one of a
screenshot and how it could look like uh
in devops um another thing bcpt uh do
not underestimate the power of preparing
for uh performance issues it's actually
quite uh doable these days this is a
screenshot of of of one of the customers
that we have been following up uh not
not that's not true this is an example
where I intentionally messed up so you
could kind of like what the idea is that
you follow up you basically run a Cod
unit every day yeah and this Cod unit
tracks how long it took to run that code
unit let's let's let's take it as an
example posting an order in this case
and it will count the amount of SQL
statements I had yeah and I do that
every day and my developers are
developing and at a certain point they
add development that adds an amount of
SQL statements to that posting of an
order you would like to know that
because you probably did quite a
significant change in performance bad
one so this is just how it could look
like and how you can end it up bcpt
helps you setting up a scenar scario
like that helps you to run that every
day helps you to send it to Telemetry
all you need to do is get it from
Telemetry get it in some kind of powerbi
report add the metric to it and you are
following it
up okay
Swagger um just I think one of the last
ones um just a possibility you would be
able to do so as well we are building
stuff in the pipeline maybe not just app
files maybe we can also build a Swagger
file that describes our AP
are custom apis that we developed in uh
in business Central yeah which is
obviously quite interesting for uh your
third parties or what whatnot um that
you're working with okay obviously also
deployment does do does anyone remember
fob files obviously uh anyone everyone
remembers fob files and we had to
manually deploy fob files I even hear
sometimes I really miss miss the days
from fob files it was easy to just
deploy a part of uh the developments
again it's not Simplicity it's
stupidity really if we were deploying a
part of the fob files we were deploying
a part of the problem or probably ending
up with a databit that didn't compile uh
uh completely anymore anyway we got rid
of fob files we have apps now and we are
able to deploy apps in an automated way
we are able to do that on SAS we are
able to do that on Prem automate it get
rid of that one page and and update I
mean we have these 50 apps I don't see
myself uploading 50 apps like every
single release
to some uh
some it's done we're
done okay so there are solutions for
that uh Al go for GitHub out of the box
solution from Microsoft on obviously
GitHub we have alaka they here uh we
have
I'm here um so yeah and in terms of
hello in terms of uh the session OG's
there is
um yeah a lot more to talk about so
maybe we are back next year doing the
followup of uh of the
OG other topics that we could talk
about man we have minus no we have one
minute for questions I need to throw
this at least once can
I
uh I didn't understand this part with
the Cal Fields you meant you mean that
uh we need to use how to Cal Fields
instead of Cal fields or what exactly
okay um if you do Cal Fields it's always
a separate SQL statement always C fields
means select some from a table yeah
could be an index uh or an index view
could be a table but it's always a
select sum set autocal Fields means that
you will automatically C the same sum
while you're getting the rest of the
record so if you set auto Cal Fields
right to uh to before a f set it will
have a big statement being F set and the
sum in one SQL statement and it
especially shows when you do that like
uh when you start to Loop if you already
have all your sums you only have one SQL
statement right if you do Cal Fields
it's a select sum sum sum sum sum sum
it's like the many the amount of Records
plus one def
find amount of SQL statement that you
would have so that's why I would always
push for set autocal Fields even in a
get you combine the two the sums and and
the one record or the find first you
combine the two instead of just two
State uh two statements
yeah you have here over there you had
some very interesting examples about
interfaces is it possible to uh download
this um
repositories do you mean the uh demo
interfaces
repository the code the code yes the
code um yes there will be available or
is already available need to check yeah
yeah there will be on my Gi Oh
so I have a question about automatic
release of pte apps so releasing them is
easy but how do you know any way to
unpublish the older versions of ptfs
because now we are kind of making a mess
of a lot of old versions in client
environment of all the PT app ver yeah
yeah you can do that with Powershell I
mean it would uh get me too much sorry
is API for that because don't know there
is I mean in ah you mean BC SAS yeah BC
SAS I'm not I don't know by heart
because I I also don't know so yeah uh
that's that's a good question um yeah I
don't know sorry thank
you so that um repository with the demo
interfaces it's available on my
KP anyone else
okay and here as well I was the final
question and Qui um it's been a while
since I've wrote a rule so would it be
possible to write a rule that always
checks for uh set aut coock fields and
uh set load Fields before and find set
yeah I I didn't touch the custom code
cops uh but it is easy not easy it is
definitely not easy but you would be
able to create like for any kind of read
check whether what checks you did did
like read isolation and set load fields
and all those kind of things yeah that's
absolutely possible yeah
yeah the lter cup would be a good uh
custom code cup uh for that and I think
you if you would suggest that also
Stefan Maron and and arur I think are
managing that I would I mean it's very
doable
absolutely anyone else anyone up there
come
on nobody
okay then thank you so much
[Applause]
