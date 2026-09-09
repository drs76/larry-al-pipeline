# BC TechDays 2022 - Coding 4 Performance

- **Source:** https://www.youtube.com/watch?v=E3ADZsisFbE
- **Video ID:** E3ADZsisFbE
- **Channel:** mibuso.com
- **Published:** 2022-09-19
- **Duration:** 101m17s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

[Music]
do
[Music]
do
[Music]
ladies and gentlemen coding for
performance here is waldo
[Music]
wow so many people
do you all have performance problems
yeah i do as well by the way yeah i do
have a little bit of a performance
problem i'm going to apologize
uh in in front already i'm a little bit
sick so i'm going to take my distance
um so if i'm a little bit
talking nonsense
i blame me to that one okay
so yeah uh i'm waldo i'm
a blogger i i am i've been quite active
in the community but my main job
yes i do have a job um is development
manager at uh effective business
solutions you're a partner we are var we
are an isv
we are the var of risv
and yeah we we do have customers and
yeah
we tend to have some performance
problems as well and this
along with that experience and along
with aj's experience because this is
absolutely something that i compelled
together with aj
that we
let's say form some kind of
course
where i'm going to give now some
snippets from that course
to share some
performance problems and how to solve
them in the angle of code review but we
will we'll get there
you might have joined one of my sessions
in one of the previous editions of nafta
days and did any one of you ever joined
that
only one it seems
so i i tend to if i ask a question
please clap your hands if you agree uh
if you don't agree please don't because
they'll it won't make much sense
uh okay so uh do you know
what we are celebrating today
do you really think you know because i
bet
all of you are thinking like yeah 10
years of uh
of nafta days or pc take days i must say
yeah sure that's absolutely a very
important celebration for me personally
i'm a little bit better to celebrate
that's my son
my son's birthday is today
and i'm
oh
this is going to be on the recording
and i'm being bad that being here in
front of you not celebrating but i blame
my son he was one week early so we are
going to celebrate that next week
anyway um the goals of today
i'm going to try to
talk about uh in performance and my idea
or my goal is
to improve performance on the business
logic but also improve the user
experience a little bit that's a
difference
sure user experience is better when you
have a performance database but you
don't always need to perform a database
to have a better user experience we'll
get into that
but in anything
performance there is something that i
call dual ethical ambiguity and yeah i
call that nobody else calls it like that
i
did the search
not a single
find on google now i have these terms
not from myself i have it from my
classes in high school actually in
middle school i think it's like say 15
16 i always remembered it because i like
the concept but the fact that if you
take a choice to take any kind of road
you're gonna bump you're gonna bump into
some roadblocks any kind of win
has losses
any kind of gain has losses and that's
the same in performance if you are
implementing a certain pattern
probably
implementing that 100 of the time is not
going to be a good idea
it's all about
trying to understand which
kind of pattern of which kind of
solution might work in your case
and maybe that same solution might
not work in your case and even not at
that customers and it would have worked
at any other customer so
it's a little bit of understanding what
is possible and when to use that
or in other words
i'm not always right
but i'm never wrong
all right
um
the demo app um i'm going to
show you
lots of demos and um people will believe
in the amount of demos that i will be
showing you please don't please don't
but i'm going to show you a lot of demos
and i'll try to do that a little bit
more efficient so there is a demo up
there is
lots of snippets and i will be showing
you snippets and and executing those
snippets in the demo app and i think i
need to explain that a little bit
because to
to show you some performance problems
and maybe some improvements that should
be cool as well
um yeah i i
uh yeah i i did something
let's say
so it's going to be this up going to
zoom in because the screen is a little
bit small
is it okay
nobody thinks this is okay okay a little
bit
is this okay
so this is the demo app and you can
already see i will be executing from
this list and you can already see all
the demos wow
not all because there is a list that
scrolls down but in any case
what i will be doing and i'm still going
to be zooming a little bit up out
i will be basing my
examples on new tables
i could have come up with examples from
the real life and i'm explicitly not
going to do that because some of you
will understand but i won't
so i've created new tables
and
that's actually just
very simple tables
with lots of data you can already
imagine
what will happen there is some messages
and text in there there is some
quantity in there there is some grouping
in there there's a color and a color too
what's important there is that's the
same value i can already imagine some
will have a key someone won't have a key
and what will be the impact uh in
whatever i will be doing next yeah so
that's a table of let's say 500 000
records it's not that big
right but there's already an amount
where serious problem can can arise
i have a few more of those tables
and i call them just some extended table
one two three four and you can already
guess those are tables
that are extended
there's no magic there
so
yeah but we'll come to that
the demo app itself is this one so i
have a list of suites this is not the
business center performance
toolkit
um because yeah every run in the toolkit
would take a minute and it would be easy
to make 90 minutes that way but
you would be bored i guess so i needed
to have like fast
runs
and when i run a piece of code i need to
get some statistics and that's kind of
like what the app is all about yeah
getting those statistics to show you
what is going on behind the scenes under
the hood under the water however you
would like to call that
so as i said i would like to take the
angle of
code
reviews
and i really value code reviews a lot
all of you do regular code reviews
that is really good i really like this
response i didn't expect that but i like
it a lot
you know with code reviews and me as a
development manager i mean this is one
of the ways that i am able to have some
kind of glimpse on the status on the
let's say the quality of my team
if i wouldn't do code reviews i wouldn't
know how
person 8
or team b
is coding
and there is a lot you can check in code
reviews performance readability
maintainability security
and so on and so on
yeah and performance is
absolutely
something that you can check in code
reviews
yeah so i'm going to show you a bunch of
code
that in my opinion
you should be able to check during a
code review as well
there are some simple things
some less simple things
i try to put them in a list i didn't
really
succeed because you will see
when you
when i try to categorize them well
it's data access and some coding
but yeah
data access is coding and in the coding
part you will see some data access as
well so let's just say that i will be
talking about all these things uh during
this session that also means i'm not
going to be able to go in depth
yeah i'm going to touch of a lot of
things
um
just try to keep with me
so the first part the data access part
and let's dive already in to a few
snippets um
where are my snippets here
and i will start very slowly or very
very easy it's obvious that whenever you
do code review whenever there is data
access
that keys should be in place right and
most of the time we will look at like
find sets and all that but it's not just
with find sets and all that it's also
with a simple count for instance yeah so
what i did here
i have two snippets
these two here
i will compare them and you'll see here
they are pretty much the same
but i'm basically just filtering on
another
field and you can already guess
there on one will have oh sorry i'm a
little bit uh lost here yeah one will
have a key the other won't so if i'd
scroll down
one explicitly do not have a key and the
other one yeah has a key
and you can already guess let's not
spend too much time on the keys because
we all know those are important if i run
these
i get one sql statement 400 milliseconds
the other one
is
quite faster wow magic
you cannot believe
how many times we simply solve the
performance case with introducing a key
and i play microsoft i play microsoft
you make it too easy on us
because it always works whenever
whatever we do sorting on whatever we
can some index field and whatever we do
uh skelexums or whatever field we do
a query on and summing on whatever
it always works
but slow
if we don't take care about the keys as
a index field included columns and all
these kind of things i'm going to show
you a lot more cases
where
these things
might be
yeah
sorry here
might cause
some issues okay second obviously is the
find set let me just show you that a
little bit better
i have you i have here
a typical question do i need to use a
find set or do i need to use a find
minus and there was always a theory of
someone
yeah
so what i did i did some
cases here so there was a find set
and i loop 40 times and then i exit
because that's going to be actually the
uh the difference between the find set
and the find minus
and then
i obviously do the same with the find
minus and here
again the same with 100 loop and then
again the find minus with a loop of 100
times and then pretty much exit
if i execute those
and i'm going to execute them in batch i
like the batch thing here
the reason why this batch exists because
i want to have some averages
usually when you execute just a
performance case and you just have one
measure
that might be influenced because you are
like downloading a movie from netflix
over there then that doesn't make any
sense so you want averages in any kind
of performance case
so if we look now a little bit down here
that makes no sense
but duration is not something that i
care about
it's a number of sql statements just
imagine you have this find
set with a loop of 40 or a find minus
with a loop of 40.
i have the same amount of uh of of sql
statements one
it's the
more than x
that actually matters in the question
find minus or find set
so if you are in the performance in in
the case in a business case where you
don't expect to loop more than
50 if there's an average of 50.
then
find minus might
be a good use case
i would say you don't never know so
findset makes more sense
okay next
going fast the typical thing again
flow fields
on
pages
users complaining about slow pages
because they want a gazillion flow
fields on there
and
yeah i have some bad i have some good
you can already guess i hope you can
already guess that
not all of my pages are
are as good
so in this case i have a color table i
can already guess this color table is is
based on my big table and i have flow
fields that have a sum on the quantity
of my colors all right very simple but
one is
total quantity
zero let's say and the other one is
total quantity two if you look at that
at those two
then again remember i did not have a key
on caller so totaling on them will work
thank you microsoft will
but will be slow
yeah
back in the days enough we needed to uh
to create a sub index field
so
i see now a lot of people
uh that
have the reflex like oh i got a slow
page and i can tell you this is a slow
page i mean
it's going to be slow
that is slow right i mean a couple of
milliseconds is is slow
f5
let me see okay
one second even
instead of this one who does have
not some index field so if if a customer
complains about
performance and there is no key
whatsoever
don't just start
creating some index field yet
some index fields come with its perks
and i i'm going to try to show you that
with the other pages here i've got
countries and for one i do have a key
the other one i have a shift index i
will show that
so this one does have a key for total
quantity and you will see here total
quantity by country and country in this
table
it does have a key but know some index
field you see here country 2 has a sum
index field
that's how we use to fix that always we
still see that it's fixed
but the third one has an included field
an included field on quantity
now this is actually interesting and and
i hope that
are you aware of this feature
it's not that much
once this is fine
are you using that feature
less
because the only club runs
the thing is
in my opinion since the included field
and correct me if i'm wrong since the
included field
causes a lot less locking to maintain
than the some index field
then the included field is actually
option number one to solve
a slow page in this case and don't just
go straight to the semantics field
because that has higher maintenance yeah
and you will see here when i execute all
three of them
one
is going to be slow that's this one the
other one is blazing fast that's a shift
and the other one included column is
actually pretty good as well and user
experience is going to be fine
they're going to be happy you're going
to be a hero because you messed up first
and you fixed it later
but you're going to be a hero
look at this
it is
okay double as slow let's say some index
field but still quick enough and
sometimes quick enough might be a better
solution than the quickest solution
remember you'll be a nero and later on
when you have 50 million records you can
be another hero when you introduce some
index field
you go from iron man to superman
okay next case
collect fields
yeah i think this is an obvious one but
i see a lot of cases and not just in my
company actually not in my company
anymore because we do a lot of
code reviews but but actually in the
beginning we saw this still quite a lot
and
i see a lot of cases where this is still
forgotten that this exists
so the simple existence of
set of technic fields
so what i see a lot is within a loop
oh i need the cog field scout fields
pump lose it you
and not thinking about the fact and i'm
still i'm actually talking about the
dinosaurs among us including me
like oh yeah maybe
we can do that's better that better so
with the set autocad fields you will
only have one statement and i can show
you that if you would do this in loop
maybe you should have already done this
because it's going to take a while
so how's life
there we go nine seconds with autocalc
fields the important thing here is uh is
that you have an insane amount of sql
statements
as such you will have in the loop for
every
existence in the loop you will have a
sql statement to get that amount for
that record
does not make any sense that's how we
needed to do that in the past but these
days come on
you have these autocad fields you will
only have
one sql statement why this was still one
second because this was a very bad
autocad field there is still improvement
that i can make
but
it's already nine times better
yeah
this is
one not all but one of the things in a
code review that stands out directly if
you look at you look in the code review
and you look at the code and you see a
fine set you see within in within the
loop and collect fields and such any
calc fields that you see
might be replaced with an autocad field
makes all the sense in the world
but the first time i saw this it was in
our product and i mean
two minutes later i scanned the entire
product for all calc fields luckily i
didn't find too many
but obviously i mean
these are easy easy fixes and easy to
find easy to search for and
very important
okay what is also very important and
actually
as easy to track as what i already
showed but
apparently not
too well adopted yet is the partial
records
you know the set autocolic fields oh
sorry the set parcel records
the set load fields although
okay let me show you
now maybe before i go into that i need
to
explain a little bit on what i did
so i created these four tables we have
seen that this just some table is the
big table with 500 000 records but i
created actually four more the just some
extended table one two three four and
what i did i created also
eight
extensions so when i would go to my
extensions
you would see
lots of extended stuff here right that's
the i the idea is that i extend
um
yeah maybe show all of them
i extend table one two times table two
four times table three six times and
table eight eight times
so on sql server level you will get this
disaster that you'll have for table one
three tables
the original and two extension tables
and for table four nine tables
yeah and you can already guess if you do
not manage this
and i mean with manage if you do not
make sure that you access the data
as efficient as at all possible
uh yeah well at you that
can have an impact um so i have a few
performance cases here um and it's easy
i mean i've got my table zero the
non-extended table right the just some
table and i'm going to access that with
partial records and without and if you
don't know what i mean then let's just
show you a little bit of a code
so this is without partial records in a
code review you can easily spot that
find set no set load fields
yeah
and this one
is with set load fields and i will do
the same for every single thing always
set load fields of message which is a
field in my original table
and if i run this as a badge because i
want to have those averages
it's a little bit slower because i have
a lot of performance casing and
basically running all of them
you're going to see something that i
find very interesting
i i hope this works
yeah
so what do we see here
a few things table extensions yeah that
impact performance for every single
graph that is going higher than higher
so this one this one this one this one
that was the no partial records part so
no set load fields so it's basically to
do the same thing it's going to take
longer and longer if you do not
implement that load fields
well that's unfortunate
but if you do
then you look at the older ones here
yeah
and there is no performance regression
if you
efficiently and consistently implement
set load fields
so we have a very simple rule in the
company whenever you access data
get
findset whatever
you apply set load fields
always
and you apply set autocad fields
always
and we will look on the set range and we
will look at the keys and all that
obviously as well that's a little bit
less obvious in the code review
but
i mean
so then you have sometimes people and
partners let's say that
that implement some kind of pattern
that you have one extension with only
table extensions i call it a table
extension extension
and then you have all dependent
extensions that depend from a table
extension extension
which
i mean this is an architectural
solution
for a platform
kind of
thing and and architecturally that
doesn't make any sense
in my opinion just go monolith in that
case
i don't see
any difference in that
um okay
so i hope you can see it makes sense but
there is there is a caveat
that i will show you in a minute i think
yeah in a minute i there is more to show
and there is more to show
so yeah this this needs some explanation
let me explain you a little bit delete
all
i sometimes get a question like hey for
every find set should i
should i do an uh if is empty then find
set no
but that doesn't mean that you shouldn't
do that
for delete all and i would like to show
you a certain case that actually
happened in my company and it took me
some time to believe that this was the
issue
so let me
show you
i'm going to prepare my data what does
this mean i have one table there is a
record in there and
there is a wallow record in there
okay the use case here is
that this is a subtable
my main table has the key waldo and
well this is just a subrecord of
that wallow record
um
sometimes i would like to
i'm explaining it wrong sorry but the
use case is sometimes
in
i need to just remove all these records
and refresh them with new values typical
case of validation messages that that
was our case that we had validation
messages let's say on a document like
hey all of this is wrong in your
document but on release we need to
delete all these validation messages and
re-evaluate our document
and show new validation messages so
delete all
and insert that was kind of like the
idea there are more
of such cases than you think
that was a locking issue now to
illustrate that locking issue here
i have a start session by the way
it's a bad habit start session
um
[Music]
but i needed to illustrate two sessions
so i'm going to start a session which
will delete all waldos and execute
something big it will take 10 seconds so
it will just delete all while those with
the set range and delete all there is a
waldo so there is something to delete
yeah that's the case
okay
then
just to illustrate some kind of delay
i will do pretty much the same i will
delete all vehicles remember
there are no vehicles
yeah
and i will insert an aj
i know it doesn't make sense but believe
me there are more cases like this than
you think
yeah
what do you think
that will happen you can actually
already
guess
10 seconds i'm waiting that means that
my current session
so pretty much this one
is waiting for the sleep of this 10
seconds so the lock that it did for the
delete of the waldo
but then obviously either it's waiting
to be able to delete nothing because
there were no vehicles
or it is waiting to insert an aj now i
would wait to insert aj
but that's not the case here sorry
it was actually waiting
to delete nothing
yeah so it needs to be able to set a
lock to not delete anything
that's the actual case here
so the the easiest solution is obviously
setting is empty right
and if you just test for is empty and
then delete
it took me a while to figure this out
because i simply couldn't believe that
that was the case so if i will do this i
will just wait two seconds there we go
two seconds
i'm still
in that previous process of deleting the
waldos
but the aj is already inserted
long story short
whenever you do a delete all
check if you need to delete anything
yeah
we found five more cases in our product
after we discovered this
then
last but not least
something about bulk inserts
you need in the code review
remember that exa that it exists
because you can gain quite a lot of
performance out of it now there are some
constraints
when we talk about bulk inserts
meaning
you need to comply with some rules in
your al coding to make it work
and i would like to address one of them
in code but there are more we'll address
that later in an overview slide
and that is actually what i was at the
time
a little bit surprised of and i'm sure
there is a reason for that i'm not
doubting that
that it does not work
when your table has another increment
yeah now in many cases in insert heavy
tables i created not to increment
why
to to have less locking and all that
um
but apparently for insert heavy tables
like i will do here i mean i'm inserting
10 000 records
um
in an empty table and i will do that
three times once in a
table with no auto increment just to
normal key
another time
with auto increment
and then last but not least
and something that we
actually see in the application and
everybody knows probably the number
series and allow gaps in number series
well that is implemented by using this
number sequence it's the new thing that
we can use on sql level to request a new
number and it's not going to log and all
that but it's not important
so i was like okay instead of an
auto increment i'll use a number
sequence
let's see
so bulk inserts the idea of a bulk
insert is i'm doing 10 000 inserts here
and i'm actually just using 2 000
statements so it's going to buffer five
inserts and then send all the five at
once
that is how we want it to react
yeah
until we are using auto increment
and we have 10 000
separate insert statements
with 10 000 reads which is normal
because we get the answer back
and then
our number sequence
and you'll see here
12 000
sql statements
i will just explain what happens
so this is actually quite normal
and i might i should have expected that
back in the days but anyway i didn't so
this next this next number sequence
is going to request a new number 10 000
times that's 10 000 statements to sql
server
and then we have still 2 000
bulk inserts that we will have so it's
still bulky
or buffering
but it's not really
faster
long story short
insert heavy tables again i'm not saying
all to increment a number sequence
doesn't make any sense this is not the
case it's not black and white in this
case
we will we have
a case where
we need to insert a lot and we can do
that in sequence without
other statements
intervening in that case and if that
performance is important we need to look
at the fact that we can do that and we
can use bulk inserts and then
auto increment should not be a good
choice
or is not a good choice that's what i'm
saying so conclusion keys important
let sql server do what it's used for
do not over
declare keys but definitely do not under
declare keys same for sift um find set
yeah
we covered that pretty much uh for the
sifts
um
look at your autocad fields i think that
that that's where we got most of the
benefits
during let's say in
a code review
but definitely
when
there are some fields or some indexes or
calcsums or whatever that are slow
don't just start and create that some
index field try this included field
first on your index and then
look further on the zombie next field
for the set load fields yeah well use it
always
it's just too important
and as the last one here you see try to
avoid blobs on table extensions let me
show you why
this
is a statement
of eight
the same eight by the way
table extensions
with
set load fields i did do a set load
fields
but since i got blob fields on every
single table extension i sti i was still
getting
all my joints which pretty much
make
this statement slow
yeah so try to avoid blob fields
good good question would be and what
about the media offset fields
blame me i forgot to test that
yeah i can tell you
sorry
um
to delete all preceded by is empty and
for bulk insert i said there were more
constraints than just the auto insert or
auto increment field i do know from the
moment you have blobs or you do any kind
of get find modifier or calculation
pretty much any kind of thing other than
insert
is breaking the bulk insert yeah so
these operations where you want to
insert
well maybe just buffer in a temp table
everything before and then
use that temp table to create all your
insert statements so you can
have benefit from this bulk insert
okay a glimpse into the future since we
are talking about data access
you have seen in the keynote that there
is going to be a new
object type or let's say data type
being data transfer
now microsoft was not able to demo this
i am able to demo this
i'm going to demo this obviously they
were able to demo
don't do that
let's do that okay it's not easy to demo
i will i will show you why
i will show you why but how do i show
you hi
so for that i created
obviously another
container because we need
the next version of business central
and i got this data transfer type demo
where i've got some code and let me show
you the code so you can see how that is
going to look like for that i created a
new app
where is my demo here this
so
it is very similar as microsoft has
shown so we have a source and a target
and this is a classic move what we would
do like in this case we would move
fields from one table to the other the
very bad thing is that we in a in a loop
we need to get
the target and then move
uh
move the fields over i mean this is very
slow if you need to do this for 50
million records
same for copying rows
this is just an example source and a
target again but
yeah to insert pretty much
field by field and insert them in the
target table now sql s it was mentioned
in the keynote sql server is actually
better than that it can actually very
efficiently do that and that's where
this data transfer comes
in if i just show you that if i would do
a classic move
the first one that i showed
it does take some time
yeah
very many many many
sql statements and six seconds
again i didn't want to do this for 50
million records
you see why
the same for for the rows many many many
sql statements
but i would expect especially for the
rows that it's just one statement now
why is this after demo because
microsoft didn't want to enable this for
just execution i cannot just execute
this as normal code i need to do this in
upgrade and i can understand
because this is
this is not normal
data move i mean there will not be any
event that will be triggered there will
not be any trigger that will be
triggered
so this is a pure sql move this is as
you would write
directly to a sql table so yeah let's
only do that in an upgrade for now
okay um so yeah i had to create an
upgrade for that so uh what i did i just
made sure that i could execute these
these things in an upgrade code unit
that's why i do have this upgrade code
unit here not going to go too deep into
that all i need to do is make sure i
have a higher version
and execute this
oh well publish my
extension there we go
back to the data transfer type and now
you will see i can actually already see
here in the overview the 20 000 to 2000
statements but only one statement
for transferring what was that
for copying the fields and two
statements for the rose
yeah
a lot faster i would say
i think very good and
i'm gonna love this
next version
okay
let's go back to the original one we
will skip the
next
and i will go back here yeah so
quite important it supports fields and
rows it does not run triggers
i already said that but i cannot
say that enough i guess
that was the demo slide
and that was the data
access let me see at the timings
yep i have a problem okay so let's just
continue
in the next part a little bit more
coding related
performance
issues i will talk a little bit on
a little bit on queries a lot on events
and some more stuff
because events i mean there were there
have been a lot of questions about that
on how we should handle that so but the
first thing that i will talk about is
queries and you might say yeah queries
hey man that's data
access yes
true that's data access but then again
everything is data access we actually
can use queries to solve coding issues
and and that's actually why what i would
like to show you a little bit
let's go back up
and let's go into the coding part
so
a typical case here
where we that we can self
with queries what i still see that we do
not solve enough with queries the loopy
loop kind of thing the i need to have in
this case all customers from all
customers i need invoices from all
invoices all lines from all lines the
items from our items maybe the inventory
so we have this crazy
nested loop
and you can simply
obviously simply
solve that with a query and in this
query we have the same nest
customers sales invoice header and so on
but as we all know if we run this in the
web client if that still works
yeah
then this is just one flat table and
obviously this is also just one sql
statement instead of all these sql
statements that i might expect
from looping through all these tables
yeah if i would do this obviously we'll
have like slow and lots of sql
statements lots of
stuff going on and here i only have one
that's normal
do know
let me see
what i have
yeah do know that
indexes within
a query is still important
yeah
so
when we went from
the convenience of not using
a query to
using queries i saw that indexing was
that was the next problem in the company
so um
yeah
let me show you um so here is a simple
grouping query where i group caller
and i want some of the quantities and
this one is pretty much the same but
again i the unindexed color thing
yeah
and yeah that gives just a big
difference if i would run this query or
this one
the one without an index is just a lot
slower
yeah so make sure now in this case i was
while i was grouping on caller and i
wanted the sum of the quantities and the
fact that this was slow was simply
because in this table
i do not have a key on color
while on color 2 i do have an included
field so this included field is also
used obviously by the query
by the way the included field is used by
sql server not by the nst so
it's a normal thing that that is
slower or faster
okay that's all normal but that's a
little bit
sorry
a little bit
lost yeah that's better let's look into
events when we talk about events we can
talk about a lot we can talk about
publishers we can talk about
subscriptions and when subscriptions we
can talk about big code units small code
units single instance global variables
and whatnot how do our subscribers need
to look at but if you already before we
go there
how do i our publishers need to look at
and the question that i get a lot is
like hey publishers
if i have 6 000 publishers does that
slow down my system because i'm raising
all these events
let's test
so i've got here a simple test
where i have 1 million
of nothing
just a loop of a million but here a
million
times
raising an event
yeah
okay
a million nothing
takes nothing
a million events
takes 16 milliseconds
it's infinitely slower
but i can tell you if you have a million
events
that are being raised
you have other problems then you're 16
milliseconds
to be honest
i might look into your apps
or these kind of things or the amount of
apps
um but yeah i hope you can see you need
to put it in a little bit of perspective
go nuts on the publishers i'd say
yeah
it's a little bit of a different story
when we go into subscribers
because and i have a few demo cases here
you can already guess if you have no
subscribers that's pretty much the same
case as the publishers that i just
showed you so that is going to be quite
fast
in this case zero by the way any kind of
thing that you do with duration there is
always a deviation there's always
some kind of error
i don't know how you call it in in
english i don't know but
60 milliseconds could
could also just have been zero for
instance in any case
now i do have
uh and i will show this a little bit
better so this case is the same as what
we have seen but not a million but just
100 000
you'll see why
and in this case i actually going to
subscribe to this event i made sure of
that in my small subscriber now what is
a small subscriber
well
this is a small subscriber
i couldn't get it smaller than this
so if we do that
we get 250 milliseconds
you might say hmm
let's subscribe not too much let's not
subscribe i'm subscribing 100 000 times
here
yeah
so again if you have a problem with
100 or you find this 250 milliseconds a
problem i think then the 100 subscribers
are a problem or 100 000 subscribers are
a problem in any case
sometimes you see the statement like
yeah but you need to keep your
subscribers as small as at all possible
i was actually one of the people that
said keep your subscribers as small as
possible so what i did i created a big
subscriber
and what is a big subscriber
well yeah
6 000 line of
crap basically
still just a subscriber that doesn't
really do anything
but the idea here is i've got a big code
unit very big code you know 6 000 lines
i need to instantiate that from the
moment i subscribe so what happens
well
not a lot actually
278 milliseconds i can't say that this
is a big difference for 100 000
subscriptions
yeah
so
big subscribers small subscriber i would
say
then i called aj i said aj you have been
convincing me
that big subscribers is a problem and it
is not here is my here's my evidence and
he said like yeah maybe it's not a big
subscriber but
a lot of big variables in your
subscribers so i i tested that so
i've got here a global variable
subscriber
basically just an empty subscriber but
now in this case just a code unit with
unused global variables
and
i would say he was onto something
because now we actually almost have
double the amount of time
yeah now global variables
is not a good idea anyway
and
people have been telling me as well that
a single instance makes sense as well
now obviously because if i would make my
subscribers in single instance i do not
need to instantiate that code unit every
single time it's just already open let's
say
so i would expect that this one
would be faster again and yes so if you
compare all of them
we can see that
well
instance makes sense global variables
don't make sense so try to keep them to
a minimum
make the subscriber as big as you want
but please don't i mean there's also
something like readability
and if you have a 6000 line code unit
honestly
other things would have been possible i
think
or other
guidelines would have been possible this
is not the end of the story in case of
subscribers unfortunately
there was also something that is called
on modify
and pretty much on database
events let's say
but i'm just going to show you the
modify part
so
what it was quite interesting
um at least what i think um i i have a
few cases here
i have a modify all that i want to do
here and obviously same with the
built-in search when i do a modify all i
expect that everything is modified at
the same time one sql statement all
modifies that's why i do modify all
else i would loop
yeah
so i'm pretty much
modifying like 5 000 records in this
case
and let's see how long that that takes
a split second
four
but if i would execute this again it's
probably just one sql statement
there we go
cool that's how it should work
but
very big but
now i'm going to introduce a subscriber
so a subscriber on modify of this table
and i'm going to bind that subscriber
and what is my subscriber that's this
one it's a manual subscription
um
single instance and i'm not doing
anything actually just again
a very small subscriber okay
and you can already guess this is going
to take a while
and what it actually did and it needed
to do because it needs to execute that
code for every single record that is
modified so now my modify all is broken
as such
a modify subscription is bad
it's easy because it's easy to find well
you can i need to do something on when
when this field changes
or modify change the field or check the
field done
business logic works
modify all broken
yeah
it's a bad habit
to subscribe to unmodify as simple as
that and you can break on delete and you
can break on insert
because on insert you will break the
bulk inserts and delete you will delete
you will break the delete all
you might say well
well this is a manual subscriber so
let's not
subscribe so
i only break the modify all
when the subscription exists so i
minimize the problem
yeah that's what you think
so i still have
five thousand
modifiers while there is no subscription
on this table
to modify 5 000 records
yeah
binding doesn't help in this case
from from the moment you have even a
manual subscriber do you want to modify
of a table
it breaks modify all same for delete
same for insert isu that's that's one i
didn't test
does that mean that manual binding
doesn't make any sense
it sure makes sense so i have a few
examples here
actually one example
easy case you see here
i'm going to validate you can already
guess i subscribe to the on validate of
this field
but now i bind my subscription in
beginning of my business logic
i'm going to validate lots of stuff here
50 000 times and then i will unbind
that's what i see most
that's easiest
yeah
what is wrong with this
not easy to catch by the way in the code
review
well not too much is wrong with this
it's fine but
uh it's actually better to do
just in time binding what we call
now if you look into the binding itself
it's just something that i would like to
just execute when a certain value is
read for some reason
like this binding
or this subscription should only execute
on orders and not on invoices that's
usually what we do then like here like
if document type is not ordered and exit
yeah that's typically what we do in a
subscriber but what if
we would not do that in the subscription
itself but we do some kind of just in
time binding
where we would only bind where the color
is red
and then
bind so there's a lot of binding going
on here buying them buying them buying
buying them binds
only if
it is red instead of just bind ones and
unbind at the end of the code unit so
you might say this is slower
but actually that is faster
so this one
takes two seconds maybe yeah maybe again
there's always something that is called
caching and all that and this one
takes
less
maybe again so we have an average
of two wow
and you'll see here that the
just-in-time binding is a couple of
percentages faster again put this in
perspective please
if this is the performance gain you're
after fine
it is obviously something that if it is
possible why not
that's the only message that i want to
give here
okay
data types
this is going to be
an obvious one i hope so what i did here
to show actually
and we actually in a code review we look
at that
we really look at that
that the right data types are being used
so in this case i'm going to concatenate
25 000 ajs
but then 25 000 times
and here i'm going to doing the same
but
25 000 waldos now obviously waldo five
characters aj two characters aj should
be faster right
but there is not a world in any
dimension where aj is faster so let's
see
and prove that
no no
the message obviously is
that aj is never faster but
that you should take the right data
types now you're never going to
concatenate 25 000 i know that but it is
a good habit to start using the new
stuff the dictionaries the the text
builders
and whatnot
yeah
i got the same pretty much for a temp
table i'm not going to show you
why not
so i got here a temp table now
this there is a stupid
example here as well that i
barely dare to show you
but still i'm i am apparently um
so the idea here is should i use a
dictionary or should i use a temp table
and you can already guess yeah
dictionary but obviously it has its use
cases because in a temp table you have
lots of fields in a dictionary that's a
key value pair
so if you only have like this key value
pair and make sense to put in a
dictionary and work with that in your
code sure use a dictionary and then
you'll see that a dictionary
is
maybe i can make this a little bit
bigger
is a little bit faster
yeah
but obviously and that's the second demo
here for a complete record i cannot put
a complete record
in a dictionary
so
yeah how i solve that here then is like
when i'm looping the dictionary i'm just
getting the record
because the primary key is in that
dictionary it doesn't make any sense i'm
not going to run this this is awfully
slow
but yeah there are some use cases
obviously yeah
that's the only thing that i
like to say about that
now
the next thing
is
actually more important than you would
think
lazy evaluation
which
pretty much doesn't exist in
in business central
or in al
what do i mean with that now if you look
at this piece of code
if x
and i
then do something
but if x the left part is already false
why should i check i
why sorry
right and business central
is going to check and execute the right
part so in my case here the right part
is pretty heavy it is a very heavy sleep
the left part is a very easy
exit right
so yeah
it makes sense to fix that in an
institutive
honestly i've been checking my code uh
not just my code in the code review
quite heavily because of this from the
moment i see
a combined if
i'm going to check what is this second
part
and same counts obviously for or
which has a similar
solution
yeah
this is going never going to be fixed i
don't expect ever that microsoft is
going to fix this simple reason because
there are
places in the base app where microsoft
is using this feature
where the second part needs to be
executed for the business logic
to be okay
yeah
and maybe we do as well in our code so
if they would fix this
they are going to introduce quite a lot
of bugs in their code in our code and
they can manage their code but not our
code so
um
that was it so
i have some overview here query is
absolutely uh great in many cases but
definitely not in all cases one thing i
didn't mention is that queries is always
going to be executed on sql level is
never going to use your nsd cache and if
you would be able to use your nskt cache
credits are slow if you are going to
execute queries like in the loop and
execute that 25 thousand times you will
see queries are slow
yeah only use queries in the right
situations
publishers go nuts
subscribers
i think there are some things that we
can take into account
uh in general for subscribers and how to
handle subscribers small code units is a
good practice maybe not for performance
but definitely for readability and then
we have single instance and all that
that we can take in account
data types use the new stuff
lazy evaluation doesn't exist so
you cannot be lazy
pretty much
and having said that
if this was not enough and you are not
able to improve the performance of your
code anymore then maybe
you shouldn't and just improve the user
experience
and obviously what i mean with this is
background processing
yeah and there are a few
possibilities i'm not going to show you
any of it i'm going to trust that you
know all of them just also know
the downsides of all of them
yeah we have start session
the upside is is going to be run
immediately in my own user permission
and as my user
to downsize this it doesn't it does not
survive a server restart and it's run
immediately
which means if i would put a start
session in a loop
you know what i'm going to show you that
i've got in this case for the sessions
that is running
basically 40 sessions that is inserting
5 000 waldos on the table
if there's a reason why there is 40
initially there were 100
and if i would have done that i could
have gone home now everything would have
crashed done
yeah
if you cannot and
trust me you cannot
nobody can you cannot
um
i lost my clicker
you cannot predict where this
start session is going to end up it
may be next week yeah but next year only
five years this star session ends up in
some kind of batch or in some kind of
loop which means you're going to start
25 000 sessions
that you do not have under control in in
general start session is not really a
good practice we have task scheduler we
have job queue these are managed
services to queue and basically not
overload an nst
but even offload task class like this to
different nsds so you're not bothering
the client nst
so there are many many positive things
to not
many reasons to not use start session
yeah again
code review start session alarm
no
then obviously do not forget about the
page background task
um not going to show you
but the page background task yeah well
i'm going to show you whatever
so
i just have two examples here right
so this is what a bad user experience
looks like i have a role center and it
takes some time i just imagine this is a
role center it takes every single time
what is it
1.7 1.8 seconds
that's a role center this is not good
right you can already guess it's this
calculation here
that one complex colic
yeah there is a sleep in there
but it can also look something like that
that you immediately get to a page but
it takes a little while to show you the
complex calculation
it takes five lines of code maybe six
it's just you need to get used to coding
that i'm not going to show you that it's
not the intention of the of the session
but
please know that it exists and use it
use it on your effect boxes use it on
your role centers use it wherever the
user experience is bad
conclusion
i think we can say that job q makes
sense
now a lot of people say my job q is not
stable
i'm sorry to say if your job queue is
not stable it's your code that's not
stable
the job queue fails because the code
fails
it's as simple as that
and if you have some kind of service
that restarts your job queue every
single morning
you might have to look into the code
that makes the job queue fail because
that's the one that's failing
and our job queue failed as well by the
way
but it's our code usually
but anyway
good
tools
we did the coding part i would like to
talk a little bit on the tools part and
there are some questions
page inspector deburger business center
performance toolkit incline profile
event log bandlock
al profiler do you know these tools
cool wow
even more we have sql tools
the query store
do you know that
yeah nice
dynamic management views
not that much the sql profiler
okay and sql management studio obviously
as well so in general you know all of
these
so
flame graph
yeah
cool
periscope
yeah
i'm surprised
uh and waldo's pc preftool
what
you have seen it
all day all evening actually
so since you do not know them let's go a
little bit into those yeah
where do i start that's a good question
i will start
with
those
well
i also here have debugger
i'm going to skip that i'm going to
assume you know the debugger
the reason
why i had a debugger on here because
there was one little thing that was very
annoying for me that i wanted to show
you and how to solve that
now during the workshops last two days
somebody showed me something on how it's
a better way to show that and let me i'm
not going to
go into the debugger but do know there
is a debug console
yeah and if you would like to get the
sql statement
out
it's very difficult if you have like 10
sql statements in your debugger you will
not be able to copy and paste some some
of the sql statements that is something
that's not working but what is working
you would be able to say like
yeah in the debug console i cannot type
here but i will do that in a node
pattern no not in the notepad here
notepad there are notepad
if you would do like sql one or nine or
eight or six it doesn't really matter
and which sql statements you would like
to copy
and you would type this one in debug
console it will give you the entire sql
statement
now i have been using the debugger
simply to get sql statements i'm not
using sql profile anymore debugger is
fine it shows you the entire statement
i once had a statement of 9 000 lines by
the way
anyway
they're just a trick that you can get a
sql statement out of the debug console
while you are debugging and that you can
copy paste using sql manual do whatever
you like with it
but there is more
there is more and i would like to show
you this piece of gem
flame graph now who knows of call stack
call stack is a representation of
uh this code unit that's called this
method that's called this method that's
called this method and that's a call
cool we see that all over the place you
have a long-running query from telemetry
we can see the call stack from al cool
we can basically identify where it is
who knows the al
profiler
nice the incline profile
cool
that's pretty much all call stack right
with the what we see
is a a tree view of the call stack
but then you actually also know
the flame graph so let me just
show you maybe that
in in a minute here we have this help
and support and we have this analyze
performance now this
is a page
in the base app or in the system up
that means that this
is an action
with code
and this as well
so maybe we can
call this code ourselves so i actually
have been doing that during the demos
that i have been executing that
you haven't seen that but i've been
doing that now look at this i have an
example
post sales invoice or open sales invoice
page doesn't really matter i will take i
will take the post sales invoice um
if i browse to the right
i will just close this because this is
annoying
you'll see that i enabled
run performance and now okay
maybe not the best thing to show
analyzer
and maybe if i execute this code
it's posting an invoice cool
and maybe i just want to know more than
how many sql statements and how long did
it take maybe i also want to just know
the profile
and there it is
profile and we know this view
right
but that's not what i wanted to show
because that representation can be
better
what if we download the flame graph
hello
look at this
a graphical representation
of the call stack
in time
so this is not just call stack this is
basically a profile
yeah but now in the timeline
and the nice thing is
you can
drill down on some methods maybe search
on some and and such
this is definitely a nice representation
of what is going on in my code and a lot
how long does it doesn't take right it's
still a performance tool so how long
does it take to do certain kinds of
things for instance this sales post here
the real
time that it took was in this
method
so while you're analyzing i must say the
first time you see this
it might
be
awkward the more you look at it more it
makes sense i promise you
um
but there is more
there was this pyroscope thing
and as you see here as i said i have
been executing this along the way while
i was executing the demos so i have been
pushing some call stacks
to pyroscope as well including
hopefully
where is it
wait a minute i lost it
ah sorry here it is that is my
is the same
uh flame graph now the nice thing about
pyroscope if you don't know periscope
how i understood what pyroscope is
is that it's some kind of
server service where you can stream
let's say or send these
performance
of profiles too
so just imagine there was a service
that's constantly profiling you would be
able to send it to periscope and then
periscope captures that and then and you
are able to do stuff with that so
just imagine i i sent that now
but i'm gonna make my invoice posting
slow now
and i'm going to in post again
somebody touched my system
can already guess there are now a few
subscribers extra going uh well while
i'll post it
and i sent this to periscope again
yeah that happens by the way in the
background
okay if i go back to periscope f5
i now see here
for this tools flame graph demo let's
say i see two profiles yeah one fast one
you see the short thing here one slow
one the long thing here
so i am able to now investigate like
look the diffu
of this one
and i want left the slow one
i won't write the big one
and i would like to have a view
on what is going on and the flame
graph
is showing me
the red thing is the time that was added
or the methods that was added the green
is the thing that was taken away and
yeah you need to get used to it
but when you get used to that you see
that one
two three problems
here it was fast this one is replaced by
a long one long means a long duration
so yeah
just another tool
that might be interesting for
investigating
performance
conclusion
the debugger
um
yeah i didn't really do anything with
that
the flame graph
is absolutely not something that i have
invented i actually came across
torben
and he is the one that clapped
the second one at cleft
when asking about the flame graph
um but um yeah i came across twitter and
he tweeted something about should i
pursue this and then it was something
with flame graph and i was working on my
session at that point
and i answered yes
you need to pursue this
and pursuing means what torment actually
did is
he created a service
and
actually i just called that service a
service
to do two things to
uh take the cpu profile file that i
created with the running the analyzer
and it's going to convert that into a
flame graph
by using
apparently
brendan gregg's library to do that this
svg file that you saw the green flame
graph that's actually that
result
the same service of storm can convert
the alcpu profile to a periscope
file now this is a different file
similar
but different it's a folded file
and
then sending that to periscope is
basically just a web service call
if you would like to know more more
torben is going to do a blog about that
right robin
yep oof how does i need to do that
or you could have a look
in how it's implemented in
myperf2
now i've been
showing
this the entire session but i do want to
explain a few more things
about that first of all
the idea of this tool is not to compete
with the business center performance
toolkit
there is a complete
different approach of what i would try
to do in this tool is first of all
showing
and analyzing performance yeah
instead of
having
of orchestrate multiple sessions doing
uh stuff within my business central case
it's a complete
thing for me it's pretty much small
cases but trying to analyze that
yeah
now these easily run performance tests
the thing is
i can set this up myself i can do that
with coding
i would be able to just set up here pc
take days
and for instance say okay i want to
analyze let's say page
and just
hear this
run it
and page 22 is being run
and i get statistics about it sql
statements duration sql rows read that
was the idea
pages code units dot run queries tables
all these
object types easy to investigate that
was the idea of the tool yeah on top of
that
running these
flame graphs
profiles and and so on
so
it's not using test runners
so it's definitely different it does
have a setting for select latest version
you know select latest version
that is basically do
disable
the
nsd cache because in performance case i
would not want to be bothered with an sd
card so usually i will just switch it on
and i will always call this like latest
version when i run a performance gate
case
the performance profiling do know
i'm using
the same as the in client profiler right
that means and if you have gone to the
session of microsoft explaining the
profilers
they might have explained the type of
profiling that is being used by the uh
profiler which is sampling
and actually that means you're losing
data yeah you're with instrumentation
you capture everything but i cannot
start that
by code
so the only thing that i can start is
the sampling part but then you lose data
because every 100 milliseconds i will
get a sample of what call stack is
running and what duration yeah and
to mitigate that a little bit
i do set up my containers
a little bit different that's not this
one by the way
so i set the sampling interval to 1
so that i get lots of samples
instead of every 100 milliseconds
yeah
makes it a little bit
easier or to get a decent flame graph
and
analyzers
then there are a number of graphs that
are come basically out of the box it's
very easy to then compare scenarios and
all that
so that's nice run and analyze any
object and so on
now
there is a snippet for that as well
uh because there is some kind of
implementation of uh of an interface and
then using that snippet makes it a
little bit easier i'm not going to go
too much into that there will be blocked
about this
but
yeah
in any case it is available you can
download it it's just on my
on my github
i'm for a beer
you too
oh many beers
so before you go
i don't know if you know
but i am a 3d print enthusiast
i did not design this that's actually
where are you
okay he's not here so uh
did i now really forget the name
okay i forgot the name anyway somebody
designed this i just printed this in
multiple colors you can take one i have
a limited amount takes two hours to
print one um
so yeah i've been printing for two weeks
for all these so
um
so please take one i don't want to see
any of them anymore
so
if you have a question please now is the
time i do have t-shirts as well
yes
sorry i will throw this as well yes
is it the part important um the
um
when you have an if statement
and
it's an or uh if
um
a is like b and then an or and then you
met a
um
database uh
find set or something like this is the
um
the sequence of the statements important
or is every uh statement um executed
every state is executed so okay so when
the first um is false or something like
this yeah that was the a lazy evaluation
so every single part is being executed
okay yeah
yeah now you yeah
somebody up top
no okay
oh come on that is go stand over there
you talk about the loopy loop and
promoted queries
but you don't have changed company for
queries
do you think
microsoft will be adding that in the
future
uh
i can't say to be honest i try to avoid
change company as much as i can yeah me
too but um
is that i can't say i i don't think that
there's microsoft microsoft
[Laughter]
yes
to promote queries then he promoted it
so
yeah i think uh that needs some
investigation i think yeah i think
okay yeah can i throw it
in your examples i saw that you use
repeat
until next less than one less than one
yeah why it is
it's same like zero
oh that's a big discussion
uh well i i was thought that it is
better to test for an infinite amount of
values than only for one value
so i will stop means in school this is
how they taught me
right so i will always do
until next is
smaller than one
that's that doesn't mean if i see code
in the review in a code review that says
equal zero that i'm going to fail it
absolutely not this is just my
convenience
there is no performance related whatever
that has anything to do with that
so
yeah
oh yeah
so in general is it a good practice to
make the
subscriber card unit a single instance
good unit in general that's best
practice
yeah
but
only do that when you really can do that
single instance can work against you as
well if in your business logic that
would kind of like not make sense then
don't obviously but in general yes that
improves performance
yeah i'm going to peter
you knew this was the last one right
subscribers
i've been taught to not use
records of the complex types
var inside the subscriber procedure
i don't understand
that subscribers to not use complex
types as far inside a
uh
as a data type in
within the subscriber itself it's that
always always go into into a separate
procedure
because of the institution association
of the procedure does that make sense
that doesn't make sense to me not yet so
what you say a subscriber yeah you make
a subscriber make a local procedure in
the subscriber cannot take complex type
yeah but then then use the so the uh you
create a procedure for the for this
event subscribe
and then inside this procedure
a record type for example
local variable local variable yeah
so instead of doing that i always call
an another procedure where you use this
local variable
ah no i think you're taking it a little
bit too far
if i understand you correctly i wouldn't
do that
to be honest still it needs to
instantiate that at some point because
you're calling that procedure anyway
so what are you gaining not really much
because it wasn't so that this local
procedure would then some kind of being
transferred transferred into into a
global one because it is a subscriber
event
and therefore it will will would really
remain in memory anyway so therefore
memory usage would be
yeah you know what there is this tool on
github
where you can test these kinds of things
i honestly can't
i mean i would have to test that same as
the media set field by the way i need to
do that
uh okay
can i throw from here just for the fun
yeah
oh there you go
basketball
well though just a simple question
a few of examples that i've seen um are
um
maybe examples that should be sent to
platform team does that happen and do
they do something with it
i don't know
does it happen that's the first part of
this yeah well uh there is there is yeah
absolutely there is communication uh
absolutely uh
the platform theme was here so
okay so i've sent all of them
and there are notes
you you probably mean a delete all yeah
yeah me too
yes can i can i try are you sure
oh
yeah good one nice now you need to troll
that
um i've heard of a new technology called
the columnstore index and um i have not
received that
yeah yeah
kenny can you take that one
the ncci
that's cool so tomorrow there is a
session
but that's not
at 1 30 right
because 1 30 there was a bad habit
session
[Laughter]
you know but
the reason why i didn't talk about ncci
is simply because i have not found
and sorry kenny one single use case
where this was a performance improvement
and i'm not saying there isn't any
absolutely not i just didn't find it yet
and that is by the way to answer your
question also something that i have been
talking with the platform team about i'm
like okay we need to use this but in one
case i mean i can't see it yet
i've seen massive improvements with
included columns i've seen massive
obviously approvals with some index
fields but not the same
with ncci me maybe tomorrow that will
say much more all right i don't know
can i
anyone else
[Laughter]
i will go there
one two three o'clock
yes who was it
really
yes here we go yep
sorry
i wanted to ask i saw you
subscribe to the modify trigger i i
don't understand oh yeah the modified
trigger
you subscribed yeah but
what if you would use the table
extension or
extension objects
to use as a trigger not as a subscriber
so uh
question is on modify
on database modify basically
subscription instead of the table
exchange subscription good question i
didn't test that
and i'm not going to do any statements
on that but that should be a test in
this toolkit as well yeah
and yeah i'm going to think of it
my blog about that
do you think it would be faster slower
it would be better i think in in terms
of um
business logic because as such
if it would have been one code
customized base up right you would put
the code on modify of that table simple
as that while in this on modify
on general modify from a table
it's always executed you need to test
against 10 tables you need to guess the
test against the run trigger and you
don't have to do that on the table
extension that so that it is actually a
better place to put your business logic
in general anyway
no performance going to be well
except for this on modify issue let's
say
i don't i think it's going to be the
same
yeah
it's just code being executed or
modified so that
i would think to subscribe to the table
generic publisher i don't know why
that's what i would always use
exactly yeah that's a good practice i
think just for publishers
okay
anyone downstairs no yeah
okay
sorry the
single instance correct is it really um
an improvement we assume we are not
using globals any code in it
sure i know it's a best practice to use
a single instance but
is there an improvement if there is no
global variable
yeah performance improvement to use a
single instance or not really
it's going to be very minimal okay but
obviously there is going to be approval
from the second time you execute that
subscriber in your session that is going
to be a performance improvement it's
going to be significant are you going to
notice that absolutely not
but i think it's better local variables
it doesn't really matter right because
it will load
anyway yeah exactly okay
okay thank you
seven o'clock
so you said about that you are doing
code reviews and that you are
seeing certain patterns like um find set
maybe you want to use autocad fields or
things like that um
that you are checking that in code
reviews would it make sense to have code
analyzers for that that yeah yeah
yeah i'm not going to tell too much but
there might be next year okay another
tool
we're thinking about that and we is
vehicle but there wouldn't be anything
against that for having an info message
right or would there be
any reason not to
to have that
not that i can think of okay
thank you
yeah another one
i don't have t-shirts anymore you know
that right
you said that uh set load fields improve
the performance of um i think we can
remove the mics right uh or do we i
don't know
people seem to have gone no not really
okay oh yeah go you said that set loads
improves the performance of a
file set yep does it improve the
performance if you load a report
if you don't what if you load a report
oh in the report it's even more
important there was one screenshot that
i didn't show you but on the report uh
it's
auto
uh sorry set load fields by default so
any columns
or or will be partially record or
partially taken
but if you use other fields in on off to
get current record of on autocad record
those are not loaded and you have it
just in time load
so on pre
data item you should add load fields of
those fields that you will use
in the on after
get the record
okay see what i mean yeah so that
yeah that's maybe something like that i
should have tested and shown as well
good question
thanks
did you test data compression with
performance
does it make a huge impact on reading
writing
i didn't test it but it i i have read
reports that it does make an impact yes
uh that you should compress your data
base basically
yeah the the property on the table yeah
now i didn't test that and also these
are all fine tests actually
i should write them down
but yeah these are actually
yeah
exactly maybe next year just all
different tests
thank you
they're all gone
all right
