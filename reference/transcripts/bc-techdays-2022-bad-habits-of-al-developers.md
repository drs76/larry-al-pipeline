# BC TechDays 2022 - Bad habits of AL Developers

- **Source:** https://www.youtube.com/watch?v=uEVUEo2pL-Y
- **Video ID:** uEVUEo2pL-Y
- **Channel:** mibuso.com
- **Published:** 2022-09-19
- **Duration:** 96m43s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

[Music]
ah
[Music]
hey
[Music]
hey
[Music]
um
[Music]
so
[Music]
oh
[Music]
ladies and gentlemen please welcome
vieko and waldo
[Applause]
[Music]
thank you thank you and welcome to this
session in the last
content slot of tech days 2022
uh i'm very glad to be able to start
this uh session and to to introduce
ourselves this is actually the first
time that waldo has agreed
to have me
in the first slot you know like it was
always at last while doing vehicles so
yes this is now vehicle and waldo
and viejo and yeah and well
so we are yeah are you happy now yes i'm
totally happy finally so uh again we are
viejo and waldo and we are mvps and you
probably have either seen us or read a
little bit of us and we have been
talking about bad habits
already and that was six years ago we
were here in antwerp and
it was about cl because back then we
didn't have ale
and even though i'm pretty sure we have
handled all of bad habits
that we introduced back then
it was six years so we all had a chance
to accumulate some more
so that's what we had to do this session
we did our best right yeah wait
absolutely so you know that we usually
when we ask questions in our sessions we
prefer that you clap so do you know what
you need to do
there you go perfect know that we're
multiple claps
one clap do you know what you need to do
right that's better okay good habit good
habit you could have it so i have a
story to tell
a few years ago
i bought a house
which wasn't finished
and i hired the builder to finish that
house for me
and
when that guy came he looked and he said
immediately
uh
this house was owned by a builder
and
i say yes how do you know and he said
well it wasn't finished builders usually
live in unfinished houses
and
also like chefs they rarely cook
extravagant meals at home they don't
have time to spend to build i mean cook
meals such as this at home
and the same can be said about us we
recognize
what best practices are
but we do not necessarily put those
practices those best practices into
action
so
develop
what
i recognize this introduction yeah
i did this introduction literally six
years ago but this is good introduction
i mean of course i did it but six years
ago but i found it on my booster
i mean yeah that must be good we are
teaching that we need to be repeatable
but we need to reuse stuff yeah yeah
okay i get that but i guess
i mean
all devils die hard maybe you should
talk about that okay that is true all
habits die hard
so
i have a story to tell no another one
yes but this one is not for me i
actually copied it but for my blog
so
let's talk about
this one
there was this experiment
they uh
this
yeah
they took five monkeys and put them in a
cage
and then they put a banana on top of the
cage and a leather
with a sensor so when you touch the
leather cold water starts praying and
then when monkeys saw the banana they
started climbing but when they touched
the leather there was cold water all
over them and then they stopped and then
they learned after a couple of times
that you must not go for the banana
because you will get sprayed by cold
water and then they take one monkey out
and put a new guy in
what does he do he sees the banana what
does he do next he starts climbing for
the banana and what the other four do
they beat him down because they know
what's going to happen and then the new
guy learns
and then he doesn't go for the banana
and then you know one by one you
exchange all five monkeys until no one
knows anymore why they're doing that but
still every single time you put a new
monkey in
he sees the banana he starts climbing
and he gets beaten down because that's
how they have been doing business there
since they can remember
so i that's all i have to say on this
topic about the folder structure
i think they got it
let's hear the claps
no other claps numerology
apparently
we still put quite some meaning in
object ids
so question who thinks table 18 is the
customer table
that's what telemetry says who thinks
tables 27 is the item table
nice
who thinks table 333 is the item nature
entry
thanks for proving my point
do you know the id of the global trigger
management
49 yeah that thanks for proving my point
it's a good number
so
yeah um as actually andre in this
session also addressed we should not be
working with ids as such in any way ids
are bad this
obviously
is bad
yeah
this
is completely ridiculous
and if you understand the joke
you kind of like prove my point
yeah okay
so numerology has many faces uh in a way
we are and and i see a lot of people
still uh
yeah putting object id's in for instance
files names because we remember them and
then we can easily find the file control
p and and start with the id
or compulsive object range is trying to
force
objects in a certain
range like i reserve 10 ids because i
need everything from the resource module
let's say
in that same id range
and even
to order fields yeah it makes sense to
be able to order my fields
because then i can see them
well no it absolutely makes not a single
sense oh sorry i'm in the wrong table
so if you for instance see this same on
the screen as a screenshot
that's what i see a lot and that's what
i have been doing a lot as well because
back in the days old habits um we were
uh this was the way to to sort our
fields right but they don't make any
sense anymore so i i could be just
putting the street in this case all in
the end and if i would be using that or
browsing
like this view here is just showing me
the order in the file the id does not
have any influence there right
same for here just a table ba ba stands
for bad habits not bamba
it's not bad anyway
thank you for messing up my keyboard and
this is just
an alphabetical order
ids do not impact
anything
so it's pretty much time
to abandon
the use of actually putting a news
and
object like this
yeah so
most of us came from cel world and we
had a lot of good habits
we
preached about some of those good habits
six years ago and those good habits can
easily become bad habits
um
a lot of people have simply taken
the a language to just be cl you know
with dark mode snippets and
but it's a lot more than that
so um
let's talk about this what used to be a
good habit
is not necessarily still good things
that we used to do back then because we
didn't have a choice
or we didn't have a better choice we
don't need to keep doing because maybe
today we have better choices like for
example this one
it's totally ridiculous to do this in in
the age of git but yes i've still seen
people yeah that's your code yes it's my
code but i wrote it six years ago like
it was future proof i knew i would be
talking about yeah that's true you copy
that yeah so you were a future few yeah
six years ago of course you see this is
bc tech takes 2022. so don't do this
like there is it's pointless git does
all of that for you it's just
yeah
uh then another one
do not yell at the compiler
what what what
i didn't catch that what do you still
have
of course
why not because it's a bad habit okay
then come on
i mean
another thing is i'll stop yelling it's
a bad habit to you well you need to calm
down
are you awake now
if they slept they surely are not
sleeping anymore management code units
like all those you know big fat code
units that you put all of your code in
that you do not know where else to put
then you have some management code in it
that's a bad habit because
it is lazy that's a bad habit it's a bad
it's easy come on if i put all my
business logic business piece
business logic yes in one code unit of
course i just need to be in one code
unit you just i can give it just one
number
oh give that number a minute and i just
can put all my business only there i can
just simply find that stop it stop it
come on
so yeah that that's a bad habit like
we should think of our code we should
structure our code
object ids should not be a problem i
know that a lot of people especially
i've heard a lot from
partners complaining about customers
wanting to have fewer objects because
they don't want to pay
for extra 100 code units or something
like that i mean
this is i don't know how i'd call it
sales driven architecture or
whatever uh
we should think we should structure code
properly we should make sure that every
object has a meaning we should we should
conform to the principle of
um
yeah well i'm
i'm a little bit losing myself i'm sorry
[Laughter]
we are interrupting each other too much
so uh single responsibility principle
and management code units violate all
that so
we should stop doing them they are not
really a good thing then another thing
is no extensibility
ten years ago six years ago maybe even
three years ago when writing cl code we
should we all
wrote code
without having to think how it will be
extended because the only way to extend
the code was to just go in there and
hack away
and we know that our code needs to have
event publishers and we should invoke
those event publishers but it's not just
about that for example enums we create
enums and then we make those enums
automatically extensible without
really managing that extensibility so uh
we should either not
make enums extensible or when we do we
should have our code to be able to
manage that to to be aware of
possibilities where other people will
extend it but not being ready for
extensibility is bad because your code
once it's in bc sus it will be extended
then another one is
we often used to create keys just
because people wanted to sort by keys
that's absolutely no longer necessary
and very similar to that
we used to add some index fields
because we had flow fields that's also
absolutely necessary for example this
one
where did you take it from
this one is actually oh i forgot
actually a key on one of the important
tables let's say the i i think the item
major entry um but please tell me
what is this useful for i mean this
isn't key
declared by microsoft which says i need
a key but i don't need it
as a sift but i do declare a shift index
but i don't need the shift index
and i declare a sql index but i don't
need a sql index because i i switched it
off so this is pretty much one two three
four five six lines of code
which i absolutely don't contribute
anything i did put uh by the way a
discussion on on twitter uh trying to
find out like does anybody know what why
this is for and
and the only conclusion two conclusions
actually first one maybe to avoid the
code cop
warning like hey you need some index
field
yeah okay uh second was
um a conversion that it was converted
from the old code base okay i can get
that
okay um i think i take the next one
so
um comment and forget that is also
something that i would like to to speak
but
actually i think i'll come back to that
later
yeah don't forget i'll come back to that
later
okay good enough doesn't mean good
what do i mean that well it's not like
when ships is able to float that we are
able
to use it to ship it yeah um so in a way
yeah compiling obviously is not good
enough we need to look into more than
just does it compile um yeah we should
can our team maintain it can it be
extended like vic also already mentioned
um does it conflict with anything else
in my system like i might have this new
app but maybe it conflicts with the
functionality of another app
do we want these dependencies and so on
and so on and so on now upsource comes
with its maintenance
uh we do not have releases anymore i
know if you uh uh unnoticed we have
waves now
and waves basically mean yeah there
isn't going to be a new number and we
are going to announce a lot in that
new number
but that doesn't mean it's going to be
released in the new number dot zero it
might be new number dot one and we kind
of like have this wave kind of effect
that every single
update
is like a big release
and then every single update
might be breaking changes or what we
consider to be breaking changes like
this happened
in my company
after the last update
20.5
all of a sudden
100 tests
fail minor update
yeah that can have obviously a lot of
reasons
data can be a reason you might say
your test needs to be data agnostic i
know they are not
but yeah data can be a reason
obsoletions i've seen a lot of
obsoletions of fields of procedures and
all of a sudden my code fails just
because in 20.5 they obsolete
some kind of procedure um or table or
procedure
options to anoms uh but we all uh still
know it i think the implicit explicit
with and all that and what that came
into count now how can we prepare for
that and yesterday i had a session and i
focused a little bit
on code reviews and that is important in
my
opinion code review
implementing that in your development
workflow and everything um in my opinion
it's one of the most important things
you can do
uh this is the only way for me to get
some kind of glimpse on what the state
is or what the quality is of what we
deliver to customers and as a product to
customers but i'm not going to take that
angle because there's a step before
code review which is simple code cops
there are a lot of code cops that you
can
comply with as a developer
already so my
advice would be
that you implement as many code cops as
you can find there are a lot out of the
box you can create them yourself this is
just a screenshot from what i have in in
the product yes we do have our own uh
code cup actually vehicle wrote it uh to
comply uh with
uh licensing we need to implement a
licensing component on every single app
so we have this code code to
foresee that we actually do that don't
forget that yeah and you can do that
yourself as well
if you don't want to comply with certain
rules then don't
pointless rules do not make sense and
you can do that you can again in
implement a certain file go toolset uh
to prevent that
and what i can also recommend and i'm
glad he's here is the fact that there is
now a linter cop it's not maybe going to
prevent you mistakes but it's going to
make you
coat clean
and i think that's as important as all
the other things as i mentioned
created by
what i call the history guy
do you know the
msdin365.code.history
oh come on don't you know that
look it up
the one repository i've opened on my
laptop every single time the all day
just to look up how microsoft
well messed it up
um
how can you use this code top so the
first step obviously is as a developer
you can
see what is going on in your own code
base but in ticd you can also check on
these cops right in your builds in your
validation pipelines you can check
how is your code acting
and it's not just against current we are
talking absorbers here so against next
minute against x major makes sense as
well and
they might have to fail in current they
don't have to fail in the next minor but
at least you have a glimpse on what will
be your problem in the next month
it makes all the sense in the world to
do that
and since we're talking about ci cd a
little bit we might talk also about the
d part
about the deployment part
um
does anyone know this
screen you know that screen yep you
shouldn't okay
this is a very in my opinion very
unfortunate screen because it makes us
let's say
not automate what we should automate
i actually saw this tweet not too long
ago
i'm just going to let you read it
um
it's very unfortunate because i i have
no idea if this was a serious tweet or
not i have no idea but if it was
i mean
it's not i can upload one app obviously
with this uh
with this page
but in many cases and i hope i'm not
alone in this it's not just about
managing one app in one environment it's
about managing like a gazillion apps in
gazillion environments if you're very
successful
so deployment is not just about your app
it's probably about managing a lot more
than just maybe just an app
that we created it's maybe also
deploying or having to deploy a complete
dependency tree in my and i'm going to
show that later in my situation we have
40 apps that we need to deploy and if we
deploy just
a subset we probably have to deploy one
two three four five six other apps to
basically deploy the entire new feature
that we created so it's not let's try
that with that page i mean that is
not manageable so
um yeah and on top of that it's not just
maybe
business central apps maybe also that go
along with
swagger deployments because of your
custom api that needs to be updated on
some kind of server that manages that
swagger
or azure functions and so on now
automated deployment can be done
both on sas
anton pren who of you have still
customers on-prem
of course i hope microsoft heard that
i mean on-prem is not gone
and we are doing al on-prem and we
should also automate the deployment
on-prem makes all the sense in the world
i have been blogging about that there is
a way to do that an easy way to do that
please do that
it's a free tool
so
it is possible
a deployment should not be more and not
less
than for instance in this case
a simple approval pressing that button
the blue one
basically should just deploy again not
one app but your solution
yeah
and i want to briefly show that not show
a deployment but show just a pipeline so
this is just an example of of a pipeline
where we would have a complete build it
builds me my apps whatever that is but
this deployment
is
pretty much
an approval jill in this case children
he is a consultant he doesn't know
anything about
the technical side of business central
but he knows a lot
and he does really good project
management and he knows when we can
deploy certain
functionalities and that's pretty much
what he did and in the background
it should it might look something like
this
uh just an example published you see
published published published three
published steps first one is publishing
the dependencies second one is
publishing the tenant extension because
this is a customer deployment
third one
don't you have everything yet no third
one is all the apps that are dependent
from my bartender extension
and you can just get that all
in one go
to the customer
but you can only do that if you automate
so
good i forgot do we have sound
that's a good question i have no idea do
we have sound
i mean okay good i need this sound from
pc3 so yeah
forgot like there's usually this
checklist before we start but yeah
this was obviously a non-prepared
session so
let's talk about this one i i like to
call it vscaan
do you know what that acronym stands for
it's easy visual studio code as a
notepad
so and i will tell another story
visually this time
copy that one as well
yeah from youtube
so there is a video from my country so
i've put the subtitles and
there is no sound
but there are subtitles
yeah there is no sound
it's just like it's okay it's too late
too late too late
a lot
i think they have to get the point yeah
i think you got the point
so
yeah
and by the way
this is this is a croatian movie right
these are croatians don't buy and
understand housing croatia
okay
so uh do your snippets
good for you
so you should be using snippets sorry do
you use snippets absolutely you also uh
just disable them like david does of
course david knows it how to do it
because i showed him
so how do we like
why snippets i know that there are
people let me hear who does not use
snippets
aj come on you need to clap here
yeah so i mean for example there is a
very nice one like i want to create the
code unit by waldo so i just say this
one and then of course i just assign an
object i need for ninja and like my
method is awesome
and it's do awesome
and yeah i'm my
in essence this method already does
everything it needs to do
yeah or like in my uh
with my previous customer i had like a
large number of code units had this
exact same shape so we had something
like this uh so we essentially just
assign some
stop talking action and then just
describe and then version and then just
put the code in and then in essence
snippets save tremendous amount of time
and
whoever says that they don't use
snippets and has strong reasons i would
ask to reconsider those reasons snippets
are easy to do
you can do snippets per project like for
example here i have
this snippet and i have that snippet
which i'm just going to show in a short
while snippets are really easy
and they do save time so please use
snippets
um yeah i've just said all that
the next one is keyboard shortcuts i
remember the old days when it was you
know developers took pride into how well
they could use the keyboard
so
let me
give you an example of
what is possible in in al i'm a lot of
you probably know but
we can really take the keyboarding to
the next level with vs code so here i
will first use a snippet
because i have prepared it so it's yeah
kind of you could say that this demo is
you know faked but it is not i've
actually done something like that last
week that's why i remind it reminding
myself to actually show that demo so
let's imagine i have these
eight variables that i need to pass into
this code unit as parameters so they
come from outside i need to assign them
in i mean this is
a typical task so here i have this
method which or function which i need to
call with them and okay i will just
paste them here then i will go do like
this
make eight cursors
then in essence simply go here delete
this last one
sorry i don't need to delete that i just
need to do this and then put them on all
in the same line format them then i'm
going to select all eight of them then
copy them put in into this
come here paste them once
and then just once again
do this
in
and
done
so
all of that
i mean i'm i'm done
for something that would normally take
me maybe five minutes maybe more or i
don't know maybe not five minutes but
you can be very efficient with this and
what i want to recommend is that
if you do not know all those shortcuts
there is this editor playground in
visual studio code go there and play
it will teach you these and a lot more
so that you can really be
efficient with those
then what i would like to talk about is
settings management we very often do not
commit settings.json into repositories
but that is bad we should be doing that
the reason why we do not do that is
because there could be some settings
which are let's say my user settings but
user settings belong to user settings we
have three levels of settings we have
user settings and workspace settings and
folder settings
and user settings are for what i want to
personalize for myself
and other things should be per
workspace or per folder and we should
absolutely be enforcing settings for
every developer in the group
so for example if there are extensions
that we want to uh to suggest we can put
that into the repo if there are some
settings like code analyzers should we
enable them like format on save for
example or some specific settings like
for object id ninja or for crs while the
crs extension you want to put them and
make sure that everybody uses the same
settings so this is something that you
should take advantage from and all
settings that do not have anything to do
with how the work
the folder or the workspace should
behave that simply doesn't belong to
settings.json and that's easy
then
another one extensions do you use
extensions
okay that wasn't enough claps but i'm
pretty sure you all do let me show you
let me prove it to you so there are some
pretty good extensions out there like
for example wildos extension or anjace
extension or david's extension or my
extension
yeah and there are a lot a lot
more other very useful extensions like
this one also very good totally
recommend to use it so there you go are
you using extensions
yeah okay
so what do others do
okay yeah
not much about it and yeah of course
comment and forget
uh
i really think i can come back to that
later let's go back to that later okay
yeah so uh tables extensions
as a design pattern i addressed it
yesterday in my session as well uh very
shortly and i would like to address it
here as well and unfortunately as a bad
habit and i know that a few people are
going to hate me now
because i do know that quite a few
partners implement this as a good habit
and why would that be a good habit well
simply because table extensions
well they cost performance yeah whenever
you create a table extension
um you basically add a new table on top
of another table and if you request some
data out of it it's going to have to
join and all that and that costs time
now what i mean with table extensions as
a design pattern uh let me try to
implement that a little bit with this uh
yeah
some graphics let's say we let's say we
have uh
four apps
now for apps obviously these are not one
in one big app no we have a decent um
let's say
you say
multi-application architecture right
camille yeah so and that's what we try
to
implement here as well and sometimes
these apps use some one or more library
apps because it makes sense that we have
these let's say
building stones that we can use in
multiple apps at the same time this as
such is
pretty good
um architecture but then there is a
problem because whenever we need like in
if we have to extend this let's say i
sales header and sales line in every
single
extension
and if we for instance have to do that
like not in four but in 40 apps well
then we have a lot of table extensions
obviously and that would mean that
yeah that we want to mitigate that so
what i then see as as a solution
at some partners well that is let's put
all these table extensions
into a separate app
depends from that app from the right
apps let's say and then we only have
just one
join instead of possible 40 joins
performance wise very good because we
gain performance architecturally
well questionable i guess
questionable in the sense of
it's actually just a shortcut
we are
solving a problem with the wrong
solution
a huge interdependency between all apps
as such
at some point it's unavoidable maybe now
everything is still nicely split in the
apps but at some point in some apps you
will use fields that are not meant to be
used in that app
it's unavoidable it will happen at some
point
if it's not this year then it's next
year or the year after yeah it's complex
you see too much
and architecturally it doesn't make any
sense
so i showed you this yesterday it's a
graphics and we'll try to explain a
little bit for the people that haven't
seen it this is actually a performance
test
um
you see here table one two three four
five or four not five
and
a test where i either test uh with
partial load or without
partial records
and you'll see here that indeed the
higher
stacks
they indeed
indicate that there is a performance
problems when we add table extensions if
we do not
take this into account while coding
because when we set these set load
fields
how do you say that consistently
then we might keep the performance
consistent as well and that's what you
see here with all the stacks the lower
stacks that are
pretty much all the same
yeah
so the worst case here was uh table four
and it had eight table extensions
um
yeah i just wanted to share this that
there is architecturally a solution
maybe add that table extension extension
or maybe there's a coding solution and
that is consistently implemented yeah
what i find quite interesting here
which i cannot explain so i'm going to
confuse you completely um
this
last two here the table four find set
with partial records
that's this one so that means i actually
just did and set load fields on one
field and there is no join but
this one
is with the just in time loading so i
use the field that i didn't use
in the set load fields
and
that actually is
faster and consistently faster
which i cannot explain
than
just a complete join
so what happens on sql server is two
statements one partial one with the
complete join
which is apparently faster than once the
complete join
yeah and this is consistent so
maybe some sql caching maybe some nsd
caching maybe a combination of both of
them maybe something else i have no idea
maybe you have
please tell me
sorry
single join there it is i have no idea
what that means
but
sorry i really don't um
but i'll continue uh it's almost the
same as and i mean this table extension
extension right
it's almost the same as developing
monoliths
um maybe monoliths is the next bad habit
that we might or can talk about
well if you do not know what a monolith
is well yeah this is a model it but
um that's not what i mean it's pretty
much like the code customized base app
or a pace up not code customize a base
app
many many many
functionalities in one extension which
you might have been able to split into
multiple extensions
now
it's maybe easier on short term because
you don't have to think about it
you don't have to worry about i have
this piece of functionality that i need
to develop where do i put it
in the pile the management code unit
so it's generally conceived as being a
lazy architecture but you cannot be lazy
for this architecture because it does
bring quite some problems because it's
hard to read it
takes a long time to compile your build
pipelines are a mess i mean
on the long term
this is not a good practice in a way we
need to
embrace uh dependencies but that's the
next slide apparently yes this is a view
on the base up it has now or close to
more than 7000 objects
16 000 publishers yeah it's quite a lot
in any case we should be embracing
uh dependencies
and this is something in this new world
from al which is actually not that new
anymore
that we need to get used to it's
if we really embrace dependencies it's
really easy to split into multiple in
multiple teams like vehicle is for
instance now building a next now not now
hopefully uh building an extension um
and he completely doesn't know what the
41l other extensions
do have to do
but he is able to build it because it's
an isolated environment and it needs to
be working isolated as well it's easier
to understand maintain extend debug
document replace
well
in my opinion there are only good things
that can happen with a
good
dependent workflow although you need to
manage that obviously because even in
independency architecture
chaos can happen
yeah you really need to manage that
i only make dependencies when it really
makes sense and i would like to
recommend that again devops we come back
to devils quite a lot apparently but
devops can help
right
and i would never recommend
to use any kind of automatic dependency
resolver what do i mean with that if you
would have like one big repository with
55 apps it's going to be a problem like
okay what do i need to compile first
an automatic dependency resolver can
pretty much
let's say loop all your adjacents find
out what the dependencies are make up
the the order itself and then start to
compile every single up in the right
order and that's
actually exists already and i think in
the container helper as well
but in a way especially in in in devops
that's maybe not the best way to go
because you know
when when that build would fail that
means that you have an extra dependency
that you need to take into account i
would always do
an
manual
dependency like in hardcoded dependency
in pipelines so that if i would add or a
developer would add a dependency that my
pipeline fails and the only thing that i
need to do is worry about it but that's
exactly what i want to do because i want
to manage my dependencies
and not just automatic stuff
so do use an automatic dependency
deployer what i mentioned before the
deployment part well you do not want to
worry in which order you need to upload
the apps
that's in the deployment process
something that needs to be automated
so in a way if we get this iss
back in picture
this is a modular system it's pretty
easy to replace a module add ammonia and
all that and i can tell you this modular
system you can also mess up
i don't think
nasa or anyone
would want to replace anything here or
maintain this
modular system right and that's kind of
like the uh the picture that i would
like to get to
this picture
might be spaghetti in your eyes
is it spaghetti in your eyes
uh this is actually our product i'm
afraid um
do i have that yeah i have that still
open so yeah i'm not joking this is the
actual 40 apps plus all the test apps
that we have and
the statement here obviously is yes this
is still manageable sorry i'm a little
bit
fumbling here can i just use this no can
i undo this no
yeah anyway um
the spaghetti that you just saw the the
what you should see is the limited
amount of levels from bottom to top
when it is wide that just means there's
a lot of functionalities that work next
to each other right when it would be
high
then you have lots of levels of
dependency and that's where yeah well
problems could arise let's see
it is absolutely something that we need
to manage and this is just an example in
the pipeline and it might not tell you
too much but what this tells is actually
this is vehicles up by the way and he
only has one dependency which is on our
licensing app and in the pipeline we
define that dependency not just in the
app json sure also in the app json but
also in the pipeline and tomorrow
vehicle says like but i need a
dependency on rest app it's not going to
be in the pipeline
so it's not going to work
and brit vehicles all
will
have to ask permission
to add that dependency and there is
a bad example you have
this may be a bad example yeah
okay
one of the sessions that i missed here
uh is the multi-application architecture
this is the first one that i will see on
my visual tv and yes there is me
visual.tv and you can access this on
this youtube channel and you you will
see everything
here mindless stuff so it's pretty much
time for you since it's about yeah and
should i come back to that stuff
nah now
i'll talk about microscopy later so
what is mindless coding well it's when
we write code without thinking too much
about what we are doing
and when when talking about mindless
coding let's start with this one
so application area all
yeah so well it's not that useless
at least microsoft has shown us like we
will be able to
not have to write code like this anymore
but we will be able to simply do this
which is amazing and i like it
sorry problem solved problem solved yes
but that's not the problem that's not
why application area is contender number
one for the most useless feature ever
this is
the fact that we just put all
we always put all and this will not
solve the problem
this will actually just automate it so
we know will not have to write it at all
and it's actually a very good feature so
who here always uses all
oh that's too much yeah
well
okay so i want to invert the question
let me see who consistently thinks
of all the possible application areas
and then puts them in action
okay well that was embarrassing but yeah
and that is the problem
application area is an amazingly useful
feature it has a purpose
and what have we learned from microsoft
just put all and now we will be able to
automate that
well at least what we will do is we will
save a lot of space in our repositories
because you know i'm pretty sure 85
of all ale code out there is application
area equals all so
now we will get rid of that so what
should you do
you should
think of application areas like for
example here we have application area
location so if there is something that
has to do with location
we can put a field
that has to do with that application
area it's out of the view for those
users who do not work with applica with
locations and you can do it with a lot
of things a very very useful feature
so
let's not mindlessly just put all
because that doesn't help too much
okay
another one
another
most useless language feature ever is
tooltips and again tooltips are not
useless
we make it useless
so uh
i can bet that like again
95 percent of all tooltips out there are
either exactly equal to caption
or contain text like specifies and then
caption
yeah so uh this is not really uh the
best way to use that language feature
there is this very useful uh tool by
andreas verkowski in his as azal dev
tools
where you could assign
tooltips to all
well
wherever they need to be assigned it is
smart because it will also look into
page where you have maybe defined good
tooltips so that you do not get
specified caption but get something
really really good out of it let me show
this or yeah do you want me to show that
yeah i do okay we'll show it then
so
um you might already have seen i think
that
andre showed this feature himself in
this session uh but what i particularly
liked now this is obviously a bad
example uh we are in a bad habit so it's
a good habit to use bad examples in a
bad habit session um but in any case i
have a new field here location 202 and
the idea is that i also add an existing
field that's already somewhere in
another page now if i would use andrei's
tooltips you see that although that
captions are pretty much the same the
tooltip is completely different so for
this one since i'm reusing the location
code right
on another page is going to reuse the
tooltip
as well now here the first you see here
that by default it will use
yeah the field name
if you would have a caption like this
and you would andre
would use andrei's function again it's
beautifully going to take that caption
but again
the thing that we should do is obviously
make this in a more useful uh
description that it is out of the box
yeah that's the idea
but i love this feature that we can at
least reuse tooltips okay so i mean
tooltip's really really good feature
please use it correctly
so it doesn't need to contend
in that contest
the next one
to validate or not to validate that is
the question or not that was a question
on twitter yeah that was a question on
twitter actually so there was there was
this discussion
i don't really know who started it but
it was it went for a long time and then
we discussed or people discussed
about
should we validate code or should we not
validate code and there were some very
valid points on there and then i said
okay well this definitely sounds like a
good topic for wallows and my session
and then waldo said yes
of course always validate
so we talked about it so next
yeah next stop well it's not that simple
ah no no no no no but it's not
complicated either
so let's think of this like a junior
developer writes a code piece of code
like this and it will not take a rocket
scientist to figure out that this is not
going to apply
so there is circular validation so we
get an endless loop and yeah so the
developer fixes this
so this loop is a problem so he does
this
oh godfield checks the current field
number amazing right no
because what is the i mean there is
so many problems about this but what is
the biggest one curve field number will
just give 0 if you're not calling this
from the page so it will not solve the
problem
it will again make put the problem
somewhere else so validations are
not easy
i want to make a point here i'm
definitely not going to tell you
do not
validate
and i'm not going to tell you always
just validate what i want to tell you is
i want to talk a little bit about pure
functions
if you're familiar with functional
development which is what al
kind of
at least from far
seems closer to than object-oriented
development in functional development
there is a lot of talk about pure
functions what are pure functions those
are functions that when called
they only operate on their lexical
context they do not do anything outside
of their lexical context in other words
they do not have side effects and what
are side effects these are
side effects i call a function but that
function does something else somewhere
else like modifies the global state
leave something in the database etc
and now
in al
anything that involves
events or essentially all triggers all
record validates all of these
have side effects so they are impure
functions please do not consider that
impure functions are bad or evil or
anything that's just how they are called
because of how they handle global state
or state or
resources outside of their lexical
context that's the only thing that's
impure about them they're not bad but in
al we have a lot of them
and my other point is that whenever you
are invoking an impure function you need
to be aware about that impurity you need
to know what exactly is happening there
and then developers who just write
mindless validate code they will
essentially
face problems
and why is this especially a big problem
in our world today
so let me let me first say we are now
living in sas world where your extension
can be deployed together with other
extensions we could say that we could
reasonably make sure that our extensions
when we write them and we want to deploy
them at customers on-prem we can control
all
code flow we know which other extensions
we interact with so we can inspect and
we can check and make sure that all code
flies nicely that there are no problems
around any of the impurities and
essentially any of the side effects
however in sas you cannot guarantee
anything like that
and there is a lot of mindlessness
around so routinely not invoking record
validate is mindless because you know
if even if there is no validation code
on the field somebody can attach a
validation code to that field and you
don't do not know also mindlessly just
validating everything can be a problem
and right especially writing code that's
not ready
for these scenarios is especially
mindless so my point here that i wanted
to make and why i really wanted to
discuss this this year is
that we should always write code
that will be ready
for validations for triggers for all of
that code executing so if we have
anything similar to those circular
validations we need to structure it
properly that under no circumstances in
no scenario we will suffer from any
consequence bad consequences or problems
with that code so
even though i still stand by what we
wrote on twitter
that you should validate
my point is we should also be sure that
we write good validation code
not bad validation code because in the
past we could afford not to really write
good validation code because it was easy
to control it's not that easy anymore
okay so
so before we go into that uh so you
pretty much agree with me correct yeah i
do just validate yeah validating so why
this 10-minute lecture jesus just said
okay yes like
anyway uh what actually i was pointed to
by someone this morning uh actually
jeremy uh this morning for uh
and i needed to show this because i
didn't know and i love it
um
is that you can add validations of
fields
quite easily so just imagine i have just
two lines but this could be 25 lines and
if i would like to add
validation to it there is this
extension from david to move this into
validate
so just to assume that validations are
obviously implemented correctly i love
it
had you anything else to add well i
think you can take over yeah okay
that's that one topic that you wanted to
do no i will come back later um
so um there is no low code
it's just someone else's code
nobody no okay
[Laughter]
so when we look into this power fluff
like
i like to address it to which is
obviously a joke i love power sweets and
stuff
i love powershell absolutely i think you
finally put powershell where it belongs
like low code
in your in your in your case it's no
code right oh that's true
now obviously powershell doesn't belong
in this list uh and we're talking power
amps power bi power automate all these
things all good the only thing that i
would like to address is be mindful
because it is not because you can that
you should
and it's also not because you should
that you can
but that is something completely
different apparently um
what you need to think about is this
power automation and we can apparently
and i'm going to watch michael magel's
session uh definitely as well because i
missed that one too
my main concern always have been
alm life cycle management am i able to
deploy my power whatever
with my business central app and what if
microsoft decides in busy sas to upload
or do upgrade my business center up what
happens with my power app
it's still going to work i'm i'm going
to test that
so there's much more than is this going
to work tomorrow when i've finished my
low code power app
is it going to work next week is it
going to work next month
am i going to be able to make this part
of my product and if so how do i deploy
that to the customers of my product
and these kind of things there is much
more than
just
being able to do something quickly
jeremy
he is the master in metaphors
he actually a few days ago he uh he
he said to me like loco this has the
ratatouille problem i was like
okay
yes absolutely everyone can cook and
should cook
but knowing how to make a good meal
doesn't mean you know how to run a
restaurant with proper health and
hygiene standards it's a nail on the
head i think
all right next
not minding permission sets
if i show you
this picture do you know what i mean
yeah
who of you
and obviously we don't because we are
developers we do not implement right but
at your company
is it a general
custom to set everyone just super
that's too much that's actually
embarrassing but i must say
in our company it's pretty much the same
there is a lot
that we push like uh to the let's say
outside of the project and we'll take
care of that when we have time let's do
the implementation
first
and then you start to like put
everything at the end that was something
you need to talk about at the end right
yeah
but
the worst comment
in my opinion
and apparently i'm a little bit isolated
in that opinion so i i share your
opinion yeah okay we are isolated in
that opinion
so the worst comment was this one
generate permission set
contains
current i don't even know how it is
completely current extension objects
why
and now we have two worst comments
we have one for xml and al
i never got that
but as a joke
i actually applied that to
one of our apps and what do you think
like how much time i would need to write
all that so time saved
but why how is this different than a
super
permission set i don't care like my
problem solved it compiles
al
so i don't i don't get it really i from
the moment and i i yeah sorry i don't
get it i cannot
say i don't get it in like 10 ways
so i don't get it so we need to give
ability for the users to properly assign
permissions uh so we need to think about
permission set and what i would
basically always do and we try to do in
our company is to first of all create
permission sets for every module i'm not
saying app but module within an app
and then at least have a read only and
not mean at least and maybe you can have
more
that's the minimum
and you cannot generate that
you need to consciously code that
yeah no testability
we did something special
um
i'm going to ask you a question and if
you look under your left oreo right
between the seats
when you look you will see no mic
because it's invisible
under your seat there is a sensor
and that sensors
your hand gestures
in our glasses
there is vision and ai and stuff
meaning
if you answer this question with a clap
we will exactly know
how many people will have said yes
who of you thinks testability is a good
habit
let me see
it's crushing the nose
i think that's a good one
i think we all agree
we need to do testability maybe a
follow-up question what if you don't
that's what the graph is yeah that's
what the graph says everybody applies
good habits so i'm just going to skip
all these slides um no maybe a little
bit on how to do testability we all know
we need to do testability luke has done
a session today which i'm also going to
watch because i also missed that because
we pretty much were
also rehearsing this one but uh about
unit testing and uh and and all that so
just a very simple thing i would like to
just share what we do in our company as
what i think might be a feasible
approach now we
try to distinguish unit tests with uh
integration tests very simply by we have
one app and one app has its tests so you
see there one repository with an app and
a desktop
and you basically just deploy all of
them together so you always have a test
with your
changes that you do
each change
gets
another test that is
usually the case
but
if you start integrating these apps
if you start to use one app with another
app
things might conflict
or simply not work or simply just act
differently
this is funny i get that but the same
exact thing can happen in
software
right
and so we just don't have to just uh
let's say
test the unit test our app maybe test
only the method in the app we also need
to do the
let's say
when they're all installed
right
so just a suggestion
create a separate app
and the only thing the app does
is be dependent from all other apps
that even is not necessary but your
pipeline should install all of the apps
all of the apps that make sense to you
to work together obviously
and then just run all your tests that is
step number one i can tell you a lot of
them will fail
not because of
the previous slide
maybe because of the simple things like
uh in app a you have this message on
after post in app b you don't but you
and you do not expect that message but
still you're running the post so rb will
fail because app a shows the message
and just showing a message doesn't mean
there is something broken it just means
that your test needs to be changed yeah
so in this app you would be able to
sorry
i need to go to the next slide you would
be able to
facilitate a mechanism and this is just
some code how we did this a mechanism
that you check that every test has been
run and if failed it might be disabled
that's actually the first two lines
disabled test
so in code we can disable a test and
replace the test with
a copy test to the test app
meaning
from this app b where the test was
failing we could copy that code to the
test app we replace it with our new app
a new test
procedure
and we obviously implement that uh
handler
message handle or whatever that we would
have needed to finish the test that is
in case that the test actually succeeded
all the or failed in case of that
shouldn't have failed but
obviously all the other failures you
will catch as well
in this case yeah
okay
recommendation obviously is build
testability into the core of your
development do not accept a single pull
request without a test there is no
reason to accept a pull request without
a test no whatsoever
every bug should be able to replicate
that in the test
and if you replicate it in a test you
solve it and you have an extra test and
you will never have that bug again
not a single pill request should be
without the test
not a single one vehicle i totally agree
so can i finally finally
talk about this
or
i think i'll come back to this later
really yeah
but
let me talk about something else
if it's hard in al
well it probably doesn't belong in ale
in the first place so how do we know
what belongs in ale and what does not
belong in ale
well this
belongs in ale
and this
does not
so a little bit about
things that do not belong in ale and
things that do belong in al
anything
that you can write
in a language which is more efficient
and especially if it has no side effects
like for example doesn't need any data
from business central doesn't need to
write
anything back into business central like
stuff like complex calculations like
any kinds of scientific algorithms like
i can give you an example that i've been
faced with recently this customer has
needed some very complex calculation
about how to cut metal bars
in the most efficient way to
completely eliminate scrap if possible
or at least minimize it
and
like a solution was of course go back to
al and hack it away or find something
and we have found a university in
germany that has built some it was
expensive as well but was pretty fast
and amazingly accurate
and yes it was difficult to integrate
but it was much better to integrate with
that than to simply write it in al
a lot of things we often just do in ale
because that's how we do things we write
al but it's not necessarily the best way
another indicator that something does
not belong in al is that it performs
better somewhere else like if you can
get like two three five times the
performance and it is critical well then
you should leverage it
uh anything that already has an http api
or that is easy to wrap
into http api should be considered
because it's so easy these days to just
go and write
an httpi call from al like
if you're in doubt like you have
something complex to work with
well put it into an azure function then
just call it from al it would be far
better in the long run and your customer
will be far more satisfied and
especially if you didn't have to
reinvent the wheel because trust me if
we went with calculating that you know
those metal bars we would probably just
reinvent a very bad wheel whereas you
know those
scientists at that university they have
sold it in the best possible way
another thing that is blazingly obvious
about not belonging to a al is anything
that's not cloud ready i mean we are in
2022. yes we do build stuff for our
customers on-prem
but like a lot of people still use
net interrupt but let me ask you your
dot net interrupt what is it it's just
code that you wrote in dot net so that
you can interoperate with it so why not
put that dot net code into an azure
function and then interoperate with it
using http rather than net much better
so dot net interoperability obviously
does not belong there i think we we
didn't say it last time but we did say
in one of our sessions don't net so
don't net
or also any any on-prem stuff like you
should really already have started
phasing that out it is possible it is
of course you have on-prem customers but
it's so much better to have to write
code to build things which are sas ready
you will be happy when you have that
and then finally it's not that
much about not belonging in al because
it's obvious obviously entirely al
but forking base app so that you could
customize the bejesus out of it so nah
you should definitely not be doing that
yeah i think that's that's it yeah are
you sure yeah yeah i have short talks
today apparently
do i interrupt you too much
many bad ways of code deprecation
well
is there a good way to deprecate code
basically i guess that's not a question
um i guess no there isn't uh but we do
can i switch maybe yeah please do
so
code is being deprecated and we need to
deprecate our code sometimes as well the
typical examples obviously are and which
are the ones that we uh love less
least
uh is anything that has to do with
schema right uh if we would delete the
field remove table
remove yeah function has nothing to do
with schema but also has
some deprecation going on there what do
we do
as such
we can obsolete the object and go
through a default upgrade process
or
other option
we can just delete the code
and use the force
i'm not
sure how you think about the dark side
of the force
but you have been or we have been asking
for it as partners and we got our way so
microsoft built this force into
the page that we love so much
and we are able now to force our changes
up until even live environments and i
would say
maybe not
the best way to implement that as being
let's say a habit
and since this is a bad habit session it
makes me sense to talk about that
so dangerous uh well unexpected code
removals obviously unexpected data laws
are broken dependencies
run time errors i've i have had i have
seen
situations where oh we pushed this
through with the force obviously but now
i need my data back
yeah backup restore whatever
so recommendations what i would do now i
do know
software lives sometimes you need to
refactor and i strongly recommend to
refactor makes all the sense in the
world but that usually also means that
you need to take away stuff and that
microsoft hasn't made that too easy
anymore um
so in general please never use the force
use the upgrade path as
much as you can
and i think it is possible to upgrade
your way to your refactored application
what i also know is that
your deprecated stuff will be there
until end of times if you do not act on
it
if you want to act on it
then act on it
not every single time you refactor a
small piece of code but maybe in one
bulk of an action that you just let's
say manually
once in a year
make time for removing all these
obsoleted fields and obsolete tables
and then you can just do that in one go
focus on that in one go you can
basically just prepare yourself make
sure there's a snapshot there is a
backup whatever but just that there is
just one let's say transaction
or process that you can
do
to clean up
it's it's it's
important to clean up
but if you would automate
bad practice which is the force and
using divorce
well
then you're going to automate the
possibility
that you might do something wrong and
that's the thing that i would like to
avoid i will never automate such a step
now in the
some people know i'm i'm also involved
in alps we ought we basically give tools
to automate stuff
through devops and that has been asked a
lot like would you please foresee an
option to automatically force
my app
i have a personal problem with that
to create a product
that automates bad practice
okay um
so please don't use the force there we
go
there's another thing as well that i
would like to address there's also um
let's say a clean way
to
refactor functions and this has been
done by microsoft actually quite a lot
and i just want to address that a little
bit this awesome piece of business logic
is obviously in hard-coded
uh amount of sleep now i need more sleep
or at least i need to be able to decide
how much i sleep
so
refactoring this is not just replacing
that
function no i should actually obsolete
the function and there is still
overloading so you can have like an
process and have both functions enabled
let your compiler make sure that either
it's obsoleted or not obsolete and
take care of the upgrade process
that way
it's just an example on how you could
handle in this case function
deprecation
that was it
that was the end of our session
actually
no no no no wait
i need to come back to that thing
oh yeah almost forgot
what was that i wanted to talk about i
have no idea that's your point
i know that i should have
sold it then let's just stop then
what was that
ah
i remember
yeah so
one day
i'm writing and a piece of code is
bugging me so i cannot advance i just
keep stopping on that it just
and then
i say okay i'll comment this out
so i can move on and i'll
fix this
i'll make sure it works later
and then while the calls and says oh i
have this big problem can you please
check and then i do and then another and
another and then a week later i have
this in my repo
and i have no clue
why i commented this out
so was it causing problems
was this unfinished work that needs
finishing was this
refactoring in progress
or was it i mean did i mean to delete it
have you ever been in this situation
no okay
sorry with you
only with me yeah well don't work with
me now you know
so uh it happens
and it is a bad habit like uh commenting
pieces of code and i've seen a lot of
commented sections
out there in repositories when doing
code reviews
there are you know hundreds thousands of
lines of comments in there
and that does not belong and i'm not
talking about those comments
which start with you know start and end
with some requirement
identifier that you know that okay this
was probably commented out back in the
old days but not yet refactored
it's simply that just commented blocks
of code
please do not do that that is very bad
because
if if it was
if it should have been deleted then
delete it
if it shouldn't have
then keep it open
if it needs refactoring then refactor it
or put a to do
or uh
for example this it's um
screenshot is actually very small but
it's exact same chunk of code
just with the conditional directive
actually here i would like to give
credit to to the group who attended my
uh
pre-conference workshop is anybody here
please clap
okay you are here so thank you very much
we have built an amazing component sorry
both of them yes both of them
i'm pretty sure there's some shy people
in here well in any case
uh we have built a component that can
help you with this
uh so preconditional directives for
example they are much much better at
this than commenting why is that well
consider this
you see a block of code which is
commented out and it can have been
commented out for millions of reasons
and you have no clue but a conditional
directive which says like if and then
something
that something will tell you so much
more
about why was it commented out or what
was the intention of this
and even if you want to come to back
come back to it later
it will still be far better i mean there
are other ways like you could probably
like write some kind of a cop which
rejects blocks of code which are
commented out long like larger than you
know uh
two lines or five lines but i wouldn't
even do that like commented code does
not belong there if git can tell us
what happened with the history we don't
need to retain the history in there if
something is useless throw it out if
it's useful don't comment it out that
it's that simple so
i think that with that we can really
conclude the session and
take the questions
so
thank you
[Applause]
oh thank you no no you'll kill people
with that okay
by before you leave we do have this some
goodies goody stuff again
first first wins we don't have shirts to
give that's right yeah we do it we do oh
okay questions
you give church altru yeah
i will not kill anybody with this trust
me yeah
let me hear that so
when you said that we should validate it
automatically validate
create
pipelines that validate against
against next versions so but what about
your let's say your own
extensions
basically if you have a few extensions
some of them have newer versions
different versioning strategies
so if some of your own extensions have
newer versions and older versions and
your other extension has dependencies on
them so you also should validate newer
and
later and why do you think we would have
multiple versions of an extension well
uh it's not let's say if you have kind
of like say library a library app and it
it it it maybe have uh let's say
okay it changes
[Music]
more more time than for example
certain apps so it has different
versions and library can say you have a
a lot newer version yeah and the
pendancy can be on yeah
uh good question good um give the shirt
yeah of course
so
um good luck
if i understand it correctly uh the
question is rather than you have all
these different apps how do you make
sure that they all work together right
and if i would
i mean i always test and build them
together
right so um if i would run the next
major that's going to be the next major
of all my latest versions at that same
at that same time
and that's how i pretty much try to keep
them
aligned let's say so as you said uh this
library app
they probably is not going to be changed
too much
right
so it wouldn't have that bigger version
in our case it does so all of these apps
they get newer version anyway
so they're all now on 20. whatever
version all of them and
30 of them might not have been changed
for for months
so if that answers the question
thanks
yeah yeah exactly
yes
okay well do you want to throw it
make it good
yeah i try
yesterday you were showing the
the table extension with eight
extensions to a table and you're showing
the performance and if you use the set
load field you could solve the problem
yeah but if you're extending a
table from the base app
then
the set load fields has to be
implemented all over the microsoft
standard code and it isn't
so
your recommendation about the
the large table extension app that you
wouldn't recommend
but would you consider when when you
have 40 apps
if you have
seven of those apps that are extending
uh we actually are in a situation where
there's nine extensions on the sales
otherwise yeah but but then all the
functions in all the encodings of
microsoft code doesn't use set load
fields that is what it is
performance and you can't prevent it but
if would you that's a good question
absolutely um
the only thing that i can say there is
ask microsoft and to put in cellular
fields and we can uh create pull
requests
next month i've heard
yeah absolutely
something to think about
but what can i say i cannot put code and
i should not put code in a base app i
should not that should never be a reason
to do a customized space upload
either
but yeah
but i do know that microsoft is more and
more mindful on these performance cases
and and there are actually have been
talks about on how we can
let's say
i don't i don't know how to say it in
english but
how we can let's say measure all of
these different cases and what is the
best approach then i would say let's
yeah microsoft has a job to do they need
to implement all these settled fields
but i'm not sure maybe that can have a
negative impact as well on other cases
and other extensions and all that so
i can imagine that
microsoft does that that you have this
just in time roads all over the place
and that is something that we don't or
might not want either although like i
just showed as well this just in time
roads
doesn't seem to be that bad no it's
unexplainable yet so uh but yeah maybe
that can be an approach at some point as
well
no no no
that did you give no i didn't i was
waiting for you to prove so yeah that
was the question over there
i throw let me go yeah
i couldn't
because it was that was first sorry oh
yeah it was different
so who who gets the t-shirt
let's vote okay well they said you so
hi so i uh obviously don't net right
yes um do you think web assembly has a
future or potential future in business
central development
uh the question is if i understood
correctly that
web assembly does that have a future in
business central well that is not the
same thing as dot-net because it runs
completely in the front end
now uh
i would say i have been embedding web
assemblies in uh javascript controllers
in the front end and that's something
that does absolutely not qualify here so
we are not violating anything i can say
that
even though i cannot give you like
blanket warranty on this but
it's something that will not change
microsoft will keep maintaining web
client for i mean
probably as long as there is business
central and i don't think that they will
do active steps to prevent you from
using web assemblies because there is no
absolutely no reason for that so that is
a good approach i would say if if you
have something
that can be stuffed into webassembly
that runs in the front end and takes
advantage of the computing power of the
front end which is also substantial
these days but completely underused then
it's a good practice so by all means
keep doing that but if we're talking
about backend.net
that's not good
i mean that's just not sustainable
and yeah by all means web assemblies are
okay thank you yeah and now if the
question was also about will microsoft
do something about them i don't know
maybe they'd put something in them i
don't see it coming but yes maybe
because they're very specialized in
general what they do yeah thank you
you're welcome
whoop okay
now there yeah
okay i cannot really walk that much
so we speak about
code control github and we also spoke
about um
management code unit not to
code units pick
then why do we use absolute functions so
we can
test
i think it's a question for both of us a
little bit
but
about obsolete functions
it's simply that you will
i mean i will not say never but in most
situations you do not compile your
extension against only one possible
runtime you compile it against multiple
possible runtimes and then when you
obsolete
your function you're making sure that
especially if you do it in the way that
wilder has shown
then you're making sure that it can
always be properly called
but for example what obsolete tells you
when when you call obsolete the compiler
will tell you
and then you know okay i shouldn't be
doing this
or
this is something that is being taken
out or
i mean it is a good way to message to
all of other people who are using your
code
that you are doing something about that
or maybe if you want to chip in with
something something else but
i believe that uh if you are isolated
then it's fine like you do not need to
obsolete it for yourself
you are obsoleting it for others who are
using your code or who may be using your
code that is the reason why you obsolete
rather than just delete okay okay thank
you yep thank you
okay over there
so uh a slightly less technical question
um i like tests and i think everybody
here likes tests but how can we convince
management that they should like tests
[Laughter]
i'm not going to be able to help you
with that because in my company
i i am part of management so that was
easy i was basically oh if you want to
do much if you want me to do my job
being on a knee test simple as that but
i have heard that before like you as a
developer you need to be able to sell
your work to your own company right
and uh yeah that that does i have no
make yourself management so yeah but we
should buy stocks
i mean it's absolutely stupid answer
that i'm going to give but if you
estimate tests in your estimates
and include them with your customer
proposals then
there shouldn't be a big problem i know
competitors might not do that so they
they will seem like half the price of
you
but
you know it will definitely end up
costing more in the long run i don't
know it's a stupid answer as i said but
it's difficult yeah
i'm not a manager i'm not a part of
management don't don't want to be so i
don't know how i would do that like i i
don't speak that language
in which you need to convince somebody
that a part of work is simply necessary
so how do you convince a builder that
you need a foundation
i mean yeah it costs so much money to
build the foundation
let's save a little bit on that
yeah
can you say it into the microphone
i think it's the same like asking your
manager if he
will buy a computer for you to make the
development
yeah
best is no don't ask if you don't really
need to ask
because it's on you to do your job uh as
good as possible and that's part of it
and as vehicle tell
that if you estimate that or include
that into the estimate
then then it's okay
the answer could be
but it was half
before and now you are giving me double
times for everything but
yeah
these times are changing and yeah
everything is more and more expensive
okay
anything else
okay oh now this is a challenge oh no
like spread out
[Laughter]
yeah okay almost almost nobody died
so while the you said you
you have 40 apps right 41 actually for
the one
how do you keep an overhead over all
those apps like the all the id ranges oh
it does not
i actually do
fieko does one doesn't want to hear this
but we do have a separate app
um let's say an excel sheet uh where we
have we have like well let me
5 000 uh objects an object range of 5
000 and i just assign a certain range to
a certain app
and if we do not have enough the next
range goes to the same up and you have
like a split range so we have a few apps
with a split range
if that
answers that question for the object id
and then licensing and do you have
apps that install the multiple different
customers
we always install all apps at all
customers at this point
but we have a licensing app as you have
seen that was the low level app all apps
depend from the licensing app and we
enable functionalities in the app
and enabling we had a discussion this
week by the way on how we do that it's
very simple we just make our own pages
uneditable
if it's not licensed so business logic
is all still in sync let's say but the
page is just uneditable so it's a tesla
business model you know you put all the
hardware in the car but then you need to
pay subscription to activate it yeah
okay and we all love tesla right
is that an answer to the question
yeah okay just throw it back
you next
yes next
yeah
that was it if that was it thank you
thank you so much
oh yeah sorry
you
