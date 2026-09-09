# Microsoft Presents: Tri-State Locking: Reducing locking in the runtime

- **Source:** https://www.youtube.com/watch?v=Z1avFd77I18
- **Video ID:** Z1avFd77I18
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 45m00s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

thank you very much for that
introduction so as she also said we're
going to be talking about trate locking
reducing locking in the run time and
we'll talk about that what that means uh
my name is mascom I've been with
Microsoft for about 8 years now I
started as a student worker in team and
I had this great mentor called ho you
might know him he was there for a long
time and then I moved to a new team and
this new team was uh the S runtime team
and I was put right next to this very
nice guy tooren and he kind of became my
new M I would
say yeah thank you very much I'm to V
myof I was with Microsoft from 2005
starting on the first server back in the
days and then I worked until 2019 way
through our multitenancy and enabling
every every old code from the seaside
days to to be able to run and worked on
most of the features in the S runtime
over the years in 19 I had like a little
journey outside of Microsoft to do a
similar cloudlift for another company
but 1 of April back again and it's good
to be back in on the scene in Tech days
this is my favorite place to to present
yeah and we're also happy to have you
back um just a little bit of a practical
kind of question how many people in here
by raise of hands were here last year
when we did a slightly similar
presentation about locking so you know
if you're you last year let's see okay
so it's actually not that many I I think
I'll go a little bit in depth with some
of how it was last year and then of
course go really in depth with how it
going to be in the future or the future
is now actually um and then one more
second thing how many people are
planning to stay for this second session
just by raise of hands okay that's
significant oh really nice okay so we
have a pretty packed agenda for this
first one uh we're going to try to make
through as much as we can uh the read
isolation thing only if time permits
right we have presented that for but
it's super crucial to understand this so
if time presents or permits we will also
do that Tom take it away thank you very
much and uh I'll start by introducing uh
why do we have locks and what does lock
means in a business application because
Lo locks is good but locks can also be
bad but Al is a s single threaded
execution and it can run on multiple
processes in normal places in code where
you want to do currency and you want to
keep people away you can do mutex
semaphor whatever you want to do to keep
people out but if you want to have them
out of each other cross processes and
cross sessions you need to do something
else and we use the database to do our
lock with to do concurrency control
isolation also prevent Deadlocks because
if two people take different locks in
different directions you easily end up
in situations where you will have a
deadlock and people in the end you know
no one can continue and we'll have a
exception and we'll die but but locking
is good because that's the way we can
can do uh consistent data balances all
these things but we need need to limit
the amount of time we do the locks of
course and uh especially mass will drill
deeper into those part of U in the
presentation so how big a problem is it
actually so every day we have u a lot of
timeouts uh lock timeouts uh 15 50,000
on 6,400 tenants on the daily basis and
some some is really bad and and you know
they have other issues and most probably
they they are using the system in a way
where they hurt hurt themselves by using
apis or other recurrent jobs so I think
that that's a Deo situation that is
specific for some but you can see the
amount of uh locks coming from poent
extension is 16 so that's a big place
for for others and you know appsource
apps has three out of
20 where the locks come from but that
means you know the most of the heavy
locks comes from the base system because
that's that's where a lot of the
complexity goes on and even though we
try to remove them we have more and more
traffic on the machines more and more
users in the cloud and that increases
the lock time out so it's uh it was
crucial to get some of the new features
that we're talking about through to make
sure that we can get locks even smaller
in in the
future so just to get your into Pace of
what you guys know about the locks we
made a little quiz I think you
introduced it last year mes with Nicola
and uh but let's try some some samples
out
here so what does lock table do
does it lock the
table oh that's nice people know it
doesn't lock the table okay let's let's
get one step further and then okay what
about do the now we run the lock table
it didn't lock the table what what
happens then when you run a customer.
find set afterwards we did the lock
table on the customer table
here I'm hearing a lot of right answers
so that's nice it locks exactly
all right now we lock uh on one variable
of type customer but we do a find set on
another uh customer
record it
locks all right next
one uh so the actual meaning actually if
you're looking at it it's actually an
instance variable but that's something
from the past lock table was made way
back in time it is actually a static
function you know so put a predicate on
on on a particular table it's actually
for all usages afterwards on that table
where where lock table is going to be be
applied and my my excuse for why we
didn't change that name is it's before
me and uh so now I look at you was this
and even 20 2005 is also before me so I
have the same
excuse but but you know we now
introducing more things to make it
easier for for the future also all right
another example
read after write you know first we have
a find First We Take a record out we
modify it now we do a find last on a
different record what happens now does
it
lock indeed it locks so as soon as we
enter into a right transaction it will
also lock lock on any table usage
afterwards
also all right another thing then okay
let's see if we can do some uh some more
stuff with uh uh analysis as often is
happening in business code is that you
also have to do some counts as well also
what happened on the count in the case
where we are also in a right transaction
right
now exactly now we have range logs they
they are even bigger and you're going to
go a little bit more deeper into range
locks afterwards also so we make sure
that we can log out more things in the
database all right this is one a little
bit different then also now we have a
delete
all and now we have a fine set
afterwards so we first deleted all the
data and now we do a find set what
happens exactly we we we we lock and the
delete all you know put put a predicate
and everything on it if you had like a
empty table and you do a fine set you
actually lock for all inserts afterwards
it's not just what you actually selected
on or what you used on you do a lock off
the table also if if they empty so
you're the only one that can insert
afterwards all right sample more we do
an insert insert fails but what what
happens uh after after the insert if it
fails exactly so we on the right
transaction again and locking has
appeared we have to change to right
transaction and that means that we will
be in in the lock
mode and the last
one uh flow Fields what happens when you
do a Cel field on a flow
field exactly uh there's some smart SQL
also that doesn't do it but most you
know be be careful when you do the range
locks uh and that's why you need to be
able to limit your amount of locks that
you will have in the
system all right so we use the database
for logging uh the behavior of the
rights is the SQL default behavior when
you do an insert or you do a modify
sorry an update uh so that's the default
Behavior but we decorate the the reads
so we can do read uncommitted read
committed repeatable read and and update
lock so that that that's our special
behavior on top of it the rest is
actually sequals the default behavior on
uh on on on using the database so let's
talk a little bit about what
transactions in Al uh is about and and
um every time you enter a function
you're actually already in a
transactional scope but talking to the
database uh and give and ARR arrange a
transaction start it's actually pretty
expensive so if you only come into a
place and you only run run code we don't
want to make a transaction so it's
actually a virtual transaction we have
in the runtime uh but we are ready to
promote the transaction for you when you
go on so as soon as you do any of the
operations they will escalate the
transaction I'll come a little bit more
into that afterwards and and that that
transaction will stay you know so you
can get rid of transaction by doing a
commit or leaving the scope in the end
and your locks will be held for the
period U that that until you commit
because uh you have to keep everyone
else out Al you do a transactional
commit to the
database so let let's look at a little
sample here
uh we enter a function inside
U Al first we run some non-transactional
code SQL doesn't know about us yet we
don't have any transaction started but
now we need to do a read from the
database so the first thing is that we
call the database uh and please uh give
us a read
transaction uh and then we do the read
afterwards and we uh select the
uncommitted uh in the beginning if
there's no only in the read State as
soon as we need to do any right to the
database we have to promote the
transaction to a right and now we change
the behavior
uh so we do the insert and get on and we
run more code and then we do a select
afterwards on the table now all the
select has the update lock at least
until we see some of the Tri State lock
that uh M will talk about afterwards so
some of the changes where you can
actually do lighter locks then you run
more code we modify the data and we have
the time stamp checks to make sure that
you don't have violations and got stale
Data before you trying to persist them
to the database when we leave the end
transaction is committed or if you error
out we do a roll back on the transaction
or you can roll back the transaction by
doing any error in the code and then the
transaction will be
deleted but be careful sometimes because
you know we looked at very simple
samples here we have a one record in
play we took a scenario here where we
used the posting of the sales order and
this is just one of the simple ones you
can make it much worse if you have more
variety of data inside the the sales SCE
you want to post but we're touching 25
tables so there's big opportunity to
actually go in and you know make locks
with others if you go and lock these
tables then you might end up in a
situation where you'll not be able to
post from other trads that's why you
often synchronize these on job cues and
others as well also but then you know
there's a lot of tables involved in many
of the business operations you end up
easily being able to make locks if you
touch the most use
tables so lock table not quite what it
is what it says but uh it is there to
help you you know ensure your data and
your integrity of the things in your
database but let's uh follow on a bit
for you and continue into two- State and
three-state locking thank you very much
so two-state locking or kind of didn't
have a name back in days this was just
the default locking for a very long time
um I don't actually know when it came
because it was way before me to do you
know I think that's the default behavior
all the way back to Finn xit days some
some of the audience still remember
phixa yeah so the native database so
probably from back then and then until
version 25 uh 26 sorry and right now you
could and you should maybe go in and
enable it for your tenants right we say
version 26 because that's when we're
going to desupport it um it kind of a if
you want to summarize it it's kind of
pessimistic locking for reads within a
transaction we'll discover that a little
bit more and as Tom said we we applying
these locking hints to SQL statements
only the one for reads we don't do it
for writes and then they affect the
table state of a given table in a
current transaction now let let me try
to set up a rule for you that's very
nice and easy I at least think to follow
um so if we have this two State there
two states this as you can see my
overwhelming creativity here with the
naming um so we kind of start off by
easily just saying all reads are done
with read uncommitted as long as no
rights or lock table has been done to
the table table state in the current
transaction there's a asteris there
there's a caveat the caveat is only if
you're using the default transaction
type now I looked in Bas app and I
didn't find any places that didn't use
that except tests so if you're using
your code it's going to be slightly
different I will happily explain it to
you not right here on stage but you can
come after we'll discuss it um and
afterwards when WR has been done and I
say all lock table but a little bit of a
you know internals thing lock table and
rights actually the same so when we do a
right delete modify insert delete all
modify all we anyway just call lock
table for you in two State locking so
they're actually the same just for two
State loging think of them as the same
but for the remainder of the transaction
any subsequent read will be done with
the update log hint against the same
table right a little bit abstract maybe
let's take an example right so we have
some code here very simple code I hope I
mean yeah and let's let's try to go
through it assume that no other code has
run when we enter this action so there
was no onbe action event nothing like
that just this is the first thing curve
find last what hint are we going to
apply here here right and and you can
say it if you can kind of guess it
there's only two so it's 50% chance you
get it
right okay I heard someone saying it so
yes read uncommitted right so after a
delete this is a a right so we suddenly
have to say Okay we did it right so it
cannot be won so now you have 100%
chance of getting it right so I'm not
going to ask you but yeah it's update
lock right so let's continue down into
the new function we have a new record in
we have a new variable you know it it
feels like everything is different
except it's still the same table we
still on the currency table we have done
a right and implicitly a lock table due
to that and therefore we go with rule
two and say update lock okay cost. find
first we on another table now right so
now we go back and go oh okay has there
been any WR or lock table on the
customer table no so we un read
uncommitted and luckily I wrote the
slides here correctly so that's nice um
Now read uncommitted recommitted what
that do mean update logs well let's take
a little dive into SQL and it's going to
be a simplified view because we could
probably do a 90 minute session just on
lcks and SQL and my manager told me he
wrote A F read a 500 page book on that
recently so maybe not for now but we'll
just cover the basics so SQL Server and
actually SQL the the um language has
this concept of isolation levels so we
have the we start off with the read
uncommitted also how we start off
reading it has no locks it does not
apply any locks it just allows you to go
directly ahead go crazy do all the fun
things and dangerous things so let's
take an example so let's say we have me
and tooren we each have our own a
session and you know toin came first he
also came to Microsoft first so it's
it's fitting and he went in read the
data
wrote into it let's say 42 right some
nice value and then I come and read and
you know I didn't do anything else in
the session so I just get to read read
uncommitted I read 42 and I begin doing
some decisions based on that meanwhile
toen you know he figured out something
went wrong right maybe he called random
do something and got a value and then he
bailed out because of that so he rolls
back and I'm I still read 42 but that
never existed in the database that value
was only there in a transaction so I'm
maybe now writing something somewhere in
another table with that 42 value but
that never existed so now you get
inconsistent data and this is called
Dirty read and all the conflicts that
comes after that however no locks were
taken so I was allowed to run really
fast and this is kind of an example of
where you actually sometimes do need
some locking because else you can end up
with this kind of behavior so how about
update lock update lock does not allow
any of this it's quite strict actually
there's no dirty reads because what
happens and if we go back to the the
other example again I about to read
tooren already wrote he wrote 42 I come
and I go ah okay I want to read that but
I get blocked because it's it's a
conflict so I have to now wait for
tooren to read or well so told them to
commit or roll back and I either get the
new value or the old value right
exclusive locks exclusive Lo is kind of
just a even stricter version of update
lock we only use that when you write to
the database um now this is what is
called a compatibility Matrix so we can
kind of go through uh on the left and
the right left and the Top Hand think of
that as two different sessions again me
and to session maybe and you know we
maybe let's say one on the
left your right um on their right and
then I'm coming there trying to read
with something and tooren has a lock up
there of the different types right no
lock well there's no lock shared it Etc
so let's try to kind of play through a
few scenarios so let's say we did a a
right both us me and toin both did a
right I did on the first row to did it
on last row and then we're trying to
read in the middle right we some random
value in the middle we're trying to read
and we are two State locking so tooren
reads with update lock first I come I'm
also trying to read update lock well if
we look at that one you look at U update
and you follow along until you find the
U update up there you will see it's a
red C Now red you know it's a it's a bit
a matter of perspective red can
sometimes be sh as negative but for me
it's negative because I get blocked I
have to wait for to but you could also
look at it as positive right because now
I'm going to get the right value it's
just about what you want to do but from
a locking standpoint this can give Lock
timeouts if Tobin's transaction is long
right um we can also take the first
example just if we're both reading read
uncommitted well no luck no luck it's
green it's an N no conflict we both get
to run
ahead one more thing so the one I showed
to you was kind of the the the nice one
you have to think about this is the real
one from SQL Server you can find it on
the internet uh you can sit and study it
most of these things we don't have to
think about because it's like schema
locks and stuff like that we don't
change the underlying table so you don't
worry about it but I just want to show
you reality which is a bit more complex
unfortunately Al fortunately so
SQL server has this optimization which
when I think I when I tell it to you I'm
not sure you'll think it's an
optimization depends on how you look at
it um SQL Server normally when we go in
in business Central we operate on a
single row at the time most of the time
right you call modify that operates on
one row you call get or you call find
and then you next right so we take locks
on a row basis most of the time so one
row like one modifier one luck right but
SQL Server due to memorry constraints
will after some amount of rows go in and
say like hey wait a second you're taking
a lot of locks that's costing a lot of
memory let's just go from having these
small granular logs and just escalated
it up to the table level so suddenly you
can lock entire table even though you
only read or impacted some amount of
rows and I think toin told me how many
was it 5,000 yeah so so if you you read
more than 5,000 and you know on big
tables you can pretty easily end up
reading more than 5,000 especially with
stuff like doing counts and stuff like
that um but yeah it saves memory so I
mean that's
nice so TR State locking and again you
know you can maybe guess where the name
comes from I don't know else you will
see it very soon you'll see the
creativity but before we do that let's
like like let's talk about why so we we
saw a little bit of introduction to it
from tooren with the crazy amounts of
lock timeouts that we see Based on data
Telemetry for our site and you I'm sure
you're looking at your Telemetry and
also seeing these kind of things I'm I'm
sure your customers also telling you
these things so we were kind of looking
at it and I looked at Telemetry and I
kind of tried to query around and like
see what is the type of statements that
are leading to Locks cuz I think most
people would probably think oh yeah it's
because you're writing something but
around 50% of them actually comes from
reading and if you then go and see like
why is that well it's because we're
reading with update lock and update lock
is not self-compatible so you know you
kind of easily end up blocking each
other um we also kind of found out
that we probably in general should just
reduce locking because we keep hearing
and I think also after last year's
presentation there was a bunch of of
people asking me about it and the funny
thing was that when I did last year's
presentation I was presenting two State
loging I don't think I called it that
back then I actually had the code for TR
State locking on my laptop somewhere I
couldn't tell you about it back then but
uh so it's here now and I hope that's
nice so we how can we reduce locking
well we we were kind of looking at like
a maybe we can just have less lock
tables we can just you know tell people
to not use lock table but I feel like
people knew that already I I think most
people when they used log table there
was kind of a they really wanted to log
it and they didn't care about most time
so and and we looked around in Bap code
and and just other code places we saw
that it's quite frequent that you end up
in this scenario where you write and
then you do a read later like I'm sure
you can not if you agree here or
something like that but that's a pretty
common pattern and when it comes to
subscri event subscribers you can't know
when you what stage your table is in
right because they might call lock table
they might do a right and then suddenly
your code that you knew didn't do any
Rights was you know suddenly doing it
right secondly we we couldn't really
tell people to not do rights anymore
like I I feel like basic Al code
sometimes have to write data you know
correct me if I'm wrong but you know
it's pretty necessary so we came to the
conclusion that it had to be done at a
runtime level so then is right we had to
go there and make some changes and this
is what what we want we did so we
introduced another state so try state
for three yeah and uh the way you should
think about it very easily is just that
we took the second state before and
split it up into two so now there's
three the first one exactly the same no
change you know if you remember it from
last time it's good second one if rights
has been done against the table in the
current transaction further reads will
be done with read committed right so so
this is different we'll come into what
read committed means I think it's on the
next slide and then if you call lock
table and we know you do that well maybe
not you but we know B app does that a
bunch of places because it needs to have
that behavior well don't worry it's
exactly the same we didn't want to break
you on that one right so if you're
worried about that don't be here uh and
the same caveat as before assuming
default transaction type right so let's
let's run through it right again just
I'll do it a bit quicker this time so
read uncommitted you know the first one
is the same there's no different right
so we don't have to check that one okay
delete we do a delete that goes to SQL
it writes takes a x loock and then we go
c. find first right let's go through
them it's not number one because we did
a delete number two if right has been
done yes right has been done but there's
no lock table call and in the code
internally it's no longer right delete
modify insert no longer call lock table
because I mean that would defeat the
point
I mean the name in there is I think is
transition to write or something like
that very creative I named it um so we
now do read committed right so find c.
find first read committed and I wrote it
correctly nice okay so let's continue
into the other method see how it behaves
there right is the same read committed
all the way through because it still
pertains to the table State not the
record State not the method
nothing funny like that okay and next
one is on another table state so it's
read uncommitted right okay lock table
you know I promised you there's no
difference from before so we go to the
third state we see update lock
right good so there's one new uh
isolation level I showed you so let me
just explain that one cuz it's a little
bit different than some of the ones we
saw before read committed it does not
have this problem of dirty reads or
uncommitted reads and it read the way it
kind of accomplish this is it places a
share block you know you saw those on
the compatibility Matrix don't worry
I'll show them again uh and and this
will allow it so if we take the example
again with me and toin right so tooren
goes in he writes to the database 42 or
whatever he writes and then I'm trying
to read that well I go in there I put a
shared Lo Shar log is not compatible
with X loog so I will have to wait I'll
have to wait for him to either roll back
or commit and I will either get new or
old value depending on that update lock
we already saw exclusive not we always
saw so if we go here and we try to this
is really interesting let's take the
example before with to he writes at the
end I write at the end at the other I
write at the start he writes at the end
and then the middle we trying to read
right so let's try to follow shared and
shared so D it's in right no conflict
this means where we could not read
before at the same time we can read
together we can both read this one right
so after right you're no longer taking
these uh self incompatible locks
blocking out each other what is even
more interesting is here look at s
versus U shared versus update is also
compatible which means if somebody comes
and
logs by using update loog you can still
read that now the person who's reading
with update lock wants to have a
consistent view of data that is
generally kind of perceived as what you
do with update you do not say I need to
CH well you kind of say you need to
change that if you want to but you need
at least it to consistent since you read
it but that doesn't mean I can't read it
it just means I can't write to it so
we're also kind of guaranteeing the
promise of that and I can read from it
there now of course when you have
someone writing I will be
blocked so the last kind of really
important SQL around thing here when you
when you're used to kind of lock table
and I think toin talked a little bit
about this the length of locks and and
length is like an abstract way to talk
about like what's the length of a lock
well it's transaction based right so if
you take it at the very start of a
transaction and then you spend a ton of
time doing other things like in this
case sleeping which is probably not the
best way to do it but let's just say you
did that I don't know 100 seconds or
whatever it is you're now going to be
holding that update lock for the entire
sleep duration blocking everyone I mean
no one would write this code but you
know pretty obvious however if we then
in this case we you read isolation
instead of wres
we go in and we read with read uncommit
uh read committed sorry and there when
you do the fine set the length of the
lock is only at the statement level so
when you go in and read you're going to
do select something something something
from blah blah blah and then as soon as
you return from SQL you are now
releasing that lock
allowing the people other people to
interact with that row while you're
sleeping I mean probably you doing
something useful but you know in this
case
sleeping um now I hope I convinced
everyone that you know this is great and
you just want to go and and have it and
you're happy and everything well well so
the way to enable it if that is you
right now then uh tenants created after
v23 have it on by default so you know if
you're a new tenant and you didn't
disable it it's there right now for you
and you're happy and everything um older
tenants they must opt in via the feature
management um from version 25 and on it
will be on by default for all
tenants from version but you can up the
out so you can just open the feature
management that's the first thing you do
and disable it until version 26 from 26
on this is the only way we're going to
be running now the optic rate is about
12% in sess I quer Telemetry and I got a
kind of approximate number it might be a
few percentage on off um but with we had
a lot of large on-prem customers who are
now testing it out uh you can read about
it on the internet there's some nice
people out there bloging about it I
think some of the
MVPs
um so here is the if you're not used to
the feature management page just go here
find uh enable Tri State locking in Al I
think it's called and switch it to all
users we recommend that you start off
right now and go and have some fun play
with it in sandboxes run all your great
tests apply your brain power to thinking
about your code
and you know if you have any problems I
mean come talk to me send me an email
and or told them and we'll we'll
probably look we'll look at it
promptly um so you know with all that
what does this mean to you what what is
the kind of takeaway around that if you
depend the first thing is if you depend
on lock table if you explicitly knew
here I need to have a lock a update lock
when after I read it's the same no
change everything is
good but if you don't do that and you're
just doing a right and you read Afters
the lock will be held for a shorter
amount of time reads well actually at
least read locks not write locks they
didn't change reads will be more
concurrent right you know they're
self-compatible you can read two of them
so you have four go test I mean play
around have fun because it's being able
in 26 for
so we have some time so I'm going to go
through a little bit of some kind of
examples code that shows kind of the
power these are a little bit harder to
read I I think you can read them um but
the idea is essentially to show the
difference between two and Tri State
locking where on two-state locking this
would not work so if you take the action
on the your right hand side my left hand
side and uh you run it under two-state
logging this would fail but under
Tri-State logging this doesn't fail and
the reason is that these finds are now
compatible good I hope that's
clear now this is kind of the core
change that we made and this is what you
need to think about when you're seeing
if you can do this if you can use this
with transaction length
locks when you're reading with update
lock you do not have to worry about
anyone altering the data between from
another session right so let's say we do
a right on some arbitrary row and then
we do a read read committed on another
row right we only have a snapshot of the
data we don't leave a lock on it so
someone else can come and modify that
Row in between this was not possible
with update lock CU then they had to
wait so this means you can get stale
data in another way this is
this is the kind of you know this is the
thing you know this is not magic right
you know we think this is a good change
and it's going to lead to way higher
level of concurrency but there's always
a trade-off and this is the trade-off
you have to think about that now you can
use read isolation to go in and for
example say I want to read now with
repeatable read which is also more you
know um which is also
more uh more concurrent than update lock
but it takes the SL looc for the
entirety of the duration so you can do
it like that and you can read read
isolation to do that if you want to but
by default that's not the choice we made
now when you let's take this example
that I've given here where you have two
sessions trying to
modify the problem here will be that
session two will come later and try to
modify but it has a stale view of the
data here the server will detect that
situation and throw an exception because
you're now trying to override data and
you had a old view of the data so was a
decision we made and I think that's a
reasonable
decision right and this is the code for
you can also do it in a single session
which is a little bit more interesting
uh I do think we have time to discuss
this it is when you go in and on three
different record you read data and then
you make the data not consistent on
another record
so you write to it but you we detect
that scenario however if you do it
through a
modify we don't actually know all the
timestamps of all the data you modified
so there we cannot detect that you're
modified so we just within the same
transaction so we'll throw an error
there so it's only if you do yeah I
think I lost some of you but only if you
do delete all in here you can end up on
modile you can end up in this scenario
so we can discuss it later if somebody
wants to know more about it we don't
think it's going to be a very prominent
uh
problem good we have time for read
isolation I think so let's just quickly
go through that we have talked about it
before but I want to show it off because
it's very related to this it's a way to
get around these kind of places where
you need to take some consistent locks
right so in version 22 and upwards we
introduced this new way to specify how
you want to read with which kind of
isolation level you want to read cuz
throughout the entirety of it we have
talked about it is per table it's not
per record it has meant per table and
it's runtime decided unless you call
lock table well in 22 we introduced the
ability to go in and say actually on
this record instance right now for my
next read and the ones after that on
that one I actually want to override
what the table state is I want to go in
and say you know I know I need to read
with the update log now
or maybe you want to read less you want
to read with recommitted now or
uncommitted you know that that's fine
because you have a specific scenario in
mind so that's what it can do it doesn't
influence other record instances like
lock table do uh and it only impacts
read we still don't put any hints on
rights so I talked a little bit of
repeatable read but that is one of the
ones you can select uh you can go in and
say we take a shared log again and we
take it for the the entire duration of
the transaction however you have to be
careful with using that one because you
can end up blocking writers and you can
also cause Deadlocks so it's good for if
you know you're both trying to read uh
you want more parallelism and you also
want to assure no one writes to it but
then you can plug other writers and
that's like what do you want
right so this is one of the kind of
patterns we came up with when we
designed this this is we call it
temporary heightening so it's like
instead in of doing lock table which is
I think how the code originally did this
or this is kind of a modified version of
basa code I took normally you do lock
table here you go and say lock table
find last okay everything is good right
but the problem is that now if you do
this very early in a transaction
normally they do every other read would
be impacted but now we can go in and say
hey just this read is impacted nothing
else later right so if you're for
example writing event subscribers that
has to do this kind of things we really
recommend you to use this this uh this
pattern of temporary heightening and if
you think about it there's also the the
opposite right temporary lowering right
goes both
ways um I would say it's better in
pretty much all scenarios uh where you
need to do it instead of lock table
unless you really need what lock table
does but it's very rare we found too
many people who really want that but if
you need it of course Do It um so we go
back to the quiz right that quiz I'm not
going to say if it locks or not I'm
going to kind of show the difference
right so there is quite a significant
difference here with you can now get
recommitted on some of these and if we
think about it it locks yes but for very
short duration and it's also a way more
granular lock a more compatible
lock
so get ready for tri state locking I
mean that's the main takeaway go and
test secondly for and getting ready for
us was actually quite easy I was working
together with B on this and in the end
there was no significant changes in
applications in basap to do this we
spent a bunch of time in the platform
making this work there's a few testing
platform a few app testing platform I
had to slightly change but in B app
there was no significant changes uh and
that's partially because they already
began using read isolation
and then consider using read isolation
for the places you need it to control
precisely how much you want to do
it good there's some resources here if
you want to go read more about it I did
a blog post on it where I go a little
bit more in depth with the philosophical
philosophical reason we have some
documentation on them is learn about
both features so go read
that I think we are have some time left
for Q&A if anyone has questions I'm uh
I'm I'm going to bribe you a little bit
here with the chocolates for whoever ask
questions you can come and get that
afterwards so uh I hope to get some
engagement yeah I think we have this one
I can throw it to you or to can do
it uh I have this question so lock table
as you show locks the table so doesn't
matter do use different variable or
whatever it's still
locked uh read isolation level for
example if we uh set it to update lock
does it lock the table as well or the
the parameter the the record yeah so
great question so when you say lock the
table the thing is the platform does not
have a big table in environment where it
takes a monitor lock or something like
that the only thing it does is it
changes the table state to say all
subsequent reads are done with update
loog that's what loog table does the
only thing it does right so read
isolation what it does is inste it says
on the rec record instance it goes in
and says remember the next time you go
to SQL instead of applying whatever hint
the table state says just apply what you
have in memory on the tables on the
record instance level thing so it does
not okay okay thanks anyone
else I think there that's a question oh
thank you to I was the
question oh
almost so um if I want to uh do a get um
usually that that won't do a a lock
immediately so is is is there a perhaps
an idea to make a get with lock or do I
just use readed isolation update lock do
my get and then go back yeah so I mean
get behaves exactly the same same way
when it comes to locking as find so if
you called lock table and then do a get
unless we can serve it by the cache we
will still go to SQL we'll apply the
hint so we'll apply update lock because
you call lock table and that will take a
lock so get can take a lock and get gets
affected exactly the same way as find
does by read isolation I I only want to
log this specific record not every read
that I do afterwards yeah so then you
have to use read isolation yes exactly
and that that should work perfectly fine
if it doesn't send me an email we'll
talk about it
yeah anyone else who has a
question oh over there
yeah oh
sorry um read committed Y what what's
the underlying mechanism that you're
using are you using the recommitted
snapshot isolation at the server level
oh so that's a very good question so we
we I tried to avoid talking about that
because we didn't really have time to
talk about it but yes that depends
totally on your SQL Server installation
if your installation has read committed
snapshot isolation running then yes we
use it when you do read committed if it
does not it does not right so in SQL
aure it does use it but on on if you on
I don't know if you're but for the ones
on Prim depends on how you set it up so
in Azure then by using this you're
actually enabling the recommitted
snapshot isolation is that correct yes
okay so then my concern here then is
that in order for that snapshot
isolation to work it adds 14 bytes to
every clustered index every record so
then if you're working with a very large
database your client database could
cross over the 80 gate limit and and are
they going to suffer cost then no
because SQL Server guarantee that well
okay so cost is one thing but going over
the 8K limit they do guarantee I know
functionally that's not a problem but
but there's a cost involved from from a
client perspective if if you cross that
80 gig limit yes okay so then it could
be a surprise to somebody that by
enabling this that they could
potentially cross no so they don't
enable it if you right now it is always
on okay so I'm sorry we ran out of time
but maybe come we can talk later about
that okay
[Applause]
