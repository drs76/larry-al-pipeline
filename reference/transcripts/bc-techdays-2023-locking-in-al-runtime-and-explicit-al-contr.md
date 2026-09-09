# BC TechDays 2023 - Locking in AL: Runtime and explicit AL control

- **Source:** https://www.youtube.com/watch?v=1Ln98czYXmo
- **Video ID:** 1Ln98czYXmo
- **Channel:** mibuso.com
- **Published:** 2023-07-07
- **Duration:** 43m46s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

so first and foremost thank you all for
coming my name is mascam I'm a developer
on one of the server teams and with me I
have Nicola hello everyone my name is
Nicola and I'm working on the
application side so I have been working
with this product for 15 years and I'm
an El developer so on today's session
I'll be representing user because I'm
using the things that Matt and his team
is building
the main reason why we are having the
session today is because we want to
introduce read isolation feature to you
guys and to tell you honestly this is
one of my favorite features so it's
definitely meeting the top 10 list
and I like it so much that I made a
small animation to explain why and I
hope that you guys will like it as well
so let's say that you have finished the
code and it has good performance and as
you know in life good stuff does not
last that long
especially if it is performance right
because the thing that is going to
happen is that somebody will write just
a few lines of code right it happens
and these few lines of code will be
sufficient to introduce a very bad SQL
lock
what does a very bad civical lock does
it basically kills performance because
that's what the battery clocks do right
in my career I was saved a few times
with by the checking GATE test that we
had also by the Telemetry that we set up
but we know from practice that some of
these end up to the customers and then
the customers start screaming and it is
not fun to fix a performance problem sap
right usually performance problems are
difficult to fix
with the read isolation the idea is that
you can fix performance issues with just
single lines so if you draw in the red
isolation and I made the visual
animation of this
you can make this bad upgrade locks
simply disappear
so it's possible to use for most of the
locks and it is going to fix the
performance
so we have used it for several fixes
ourselves so I think we did around 8 or
10 optimizations so far and it is very
easy to fix something that would be very
difficult to fix in the past
but it's easy to use as a feature but to
be able to use it properly you need to
understand how the Locking Works
otherwise you will not be able to use
this feature because it's a hype
decision feature so one of the desires
that we would like you to get from this
session today
is to be able to write a more performant
code
to achieve the goals we decided to start
with a quiz so let's have fun and if you
guys want to participate you can test
your knowledge if it is going to lock or
not
then maths is going to explain all the
theory behind the quiz
and then we are going to end with some
practical suggestions and patterns and
tooling that you can use so you can
optimize SQL logs
so for the quiz
the examples that you're going to see
are the examples that I was myself
confused at some point of my career and
I was shocked that it works like it did
because it broke my expectations
and even many internal developers are
confused so if you want to participate
we are going to show you examples of
alcode and then if you think it is going
to cause the sick lock you raise your
hand
if you don't think it is going to cause
a SQL look you don't raise the hand
and if you're not sure don't trace the
can't and we will count yours no right
all right so
okay so we are going to start with a
simple example so here we are having
very simple codes it's customer.log
table and the first question is when we
just run customer.log table are we going
to create any SQL logs here
so who thinks
okay I can see few hands raised up and
the thing is no we are not going to
cause any SQL locks at this point
because here we are just
putting the intent that we want to lock
the records now the second question is
are we going to cause any logs here so
if you think it will raise the hands
all right super thanks this was a test
question to see who's participating yes
so the logs are being to cost when you
actually read the date so just calling
log tables syntax does not lock it I
believe it used to lock it in the past
before SQL after SQL it does nothing we
just wait for the actual records to be
read
yep so it looks no
let's make it more interesting so let's
do on the customer One log table and
then let's
read the data from the customer too
is the data from customer 2 going to be
locked
okay I can see few hands and the answer
is yes it will be locked
and to explain this one is that log
table is not connected to a variable
actually it is connected to a table and
it is going to be active on that table
until transaction ends
in hindsight we should not have defined
it like this
the proper syntax should be like this so
if you can turn back time and implement
it differently this is what it actually
does so it runs on the Full Table not
the locker variable
okay let's get a bit more complex so
here we're going to modify customer and
no questions here regarding the logs and
the question is now we are taking a
different customer variable and we are
doing find last is it going to lock
all right you guys are good so yes
it is going to lock and the explanation
here is that as soon as you start a
write operation in nail it is going to
lock subsequent reads so it locks
exactly the same example but instead
find last we are doing account and count
is not no row operation is it going to
lock or not
and okay few cans up you guys you guys
are quite good yes it looks
so this thing I was really surprised
myself but basically any read operation
is going to do a lock and in this case
it's going to be a bad luck because this
examples usually cause performance
degradations
so we have this example and this is like
delete all
and then we are going to do a fine set
on an empty table so no rows are red
from the database so what do you guys
think is it going to lock or not
yes we can get a lot of hands excellent
so yes it locks and if nor also returned
the behavior from the platform is that
entire table is going to be locked so no
other sessions will be able to insert
until this transaction ends
in reality here we are actually having
two possible bad locks if you do delete
all on the empty table it can also lock
the entire table and if you do a fine
set on an empty table it can also lock
the entire tab
now here what is going to happen if when
we do the new customer that insert
so who does it think it will look
okay so the answer is yes it locks and
it is going to do an exclusive lock on
this customer record and the interesting
thing is that even if the dot insert
fails we will count it as a right
operation and we will start
locking every subsequent reads from the
customer table
now this is my favorite example
so here we are doing a log table on
detailed customer Legend entries
we are finding the customer and then we
are calculating balance on the customer
so is it going to lock or not
so the answer is
yes it does
so this is very confusing most of the
people say no because they expect that
we are using some kind of shift indexes
and things
no SQL will do the lock here so we will
lock the detailed customer Legends
and it is usually at that lock because
we can lock a lot of Records
now if you do do it like this so we do
the log table on the customer and then
we do the calc Fields do you think it is
going to lock or not
so some of you guys are really good
and the answer here is Maybe
because it depends
so if there was a bright operation on
the detailed custom legendaries we will
lock it
by another method if there wasn't we
were not
so here we might end up with the lock or
not
so you've seen seven locking examples
and one maybe and basically we have
shown you the most common cases that are
causing the locks
so with the desire just to share which
promise we have seen the learnings is
that the log table works until the
transaction ends and it's not connected
to the variable and starting of right
operation is going to lock all the
records right from the table
and it's especially impactful if you are
doing account calc Fields calc sums find
sets modifiers delete those they have
the potential to lock the entire table
if it is empty in these cases for the
bulk operations
and the right operation is going to do
an exclusive lock on the records
modified
now I'm going to hand it over to Matt
that is going to give you much more
insights into this
yeah thank you so um
we have to go a little bit back right we
have to go back to maybe University
maybe school you know Theory right back
in those days
um
yeah
um and and kind of so I think most
people have some kind of inkling or idea
that ale as a language is single
threaded right all the in-memory data
structures use dictionaries list
whatever are single threaded there's no
two people on two sessions interacting
with them meaning we don't need General
kind of semaphores new Texas in memory
for you to lock and unlock right because
you just can't have data races because
there's not two sessions reading it the
only place you can really have it is
when you go to the database so for ale
all the Locking we do towards tables is
relegated to the database so you can you
know it would be nice to say they handle
all of it but it's not quite true we do
have to do some manual handling of it in
the platform for rights though we we
mostly just let SQL Server do exactly
what they want to do so we just it made
a nice little SQL query that says delete
or modify or whatever it does and then
SQL will take the locks it wants to take
for that statement uh that will normally
be a exclusive block but I cannot 100
guarantee that because we are at the
behest of what SQL does here
um for reads however in the runtime we
make some decisions we and we apply
these hints that you can see here read
uncommitted recommitted repeatable read
update log
we'll go into depth what they mean a
little bit later but we will apply them
for all reads and this was what we also
saw with Nicola when we applied them so
um another aspect you probably know
about ale intuitively I would guess is
that Al code is transactional right so
all database operations at least are
transactional so if you write to a
single instance code unit that's not
transactional but if you write two
databases transactional so all the
database operations will be committed or
rolled back in once
unless you commit in you know in the
middle of well that's your own choice
right but it also means that when you
end up taking an update log either
implicitly or explicitly then that one
will be helped for the length of the
transaction so if you begin taking logs
early like listing example of posting a
sales order right so I just stood this
and
ah you can maybe read that I don't know
um so if this is in time order so this
was I captured every single method start
and end every SQL query and I visualized
it here this is precisely what happens
when you do a say posting of sales order
with bass app I don't know if you have
customizations you probably do
um and let's imagine the first thing we
did was we took a lock right now you're
gonna hold that lock for two and a half
seconds
now of course this was not super slow
I'm sure everyone knows of operation
that takes way further I have heard of
some of them my customers tells me about
it so you know sometimes someone have
things that maybe take 11 hours
you know if you take a lock on a crucial
table for 11 hours yeah that's probably
going to be a problem now
what kind of tables do well I should
have asked what tables do you think will
be locked this is the this is the tables
that will at least be attempted to be
locked when I say attempted it is
we don't know if you actually did go to
SQL when I captured this so if they had
gone to SQL after this this is the full
list of all the tables
um so you know
there's some quite significant ones
there I'm not sure of precisely which
ones are implicitly taking so you did a
right toward them and which are done by
log table I know Nicola told me some of
them some of them we should not look
it's expected you know so it is just the
side effect
s so again after the fact sometimes it's
really hard to tell if it should be
locked or not
so to understand these locks and and as
I told you the locks are held by SQL so
we kind of have to understand a little
bit about what SQL does and I promise
you I'll explain this now so these are
the two most important in the current
world and well 21 and down version 21
and down
being lower
um we mostly use these two and another I
know that there's one more thing if if
anyone use transaction type set that one
to anything like update or SnapChat
I have never seen it in real ale code I
checked all of our code it's only used
in tests so I'm not going to cover it
here if you are setting transaction type
yourself to update you will have a
little bit different Behavior we can
talk about that later if anyone is doing
it
I don't think they will so read
uncommitted this is the default way we
read we allow for reading uncommitted
data so dirty reads which means you read
someone has a session going they write
into the database you come and read it
you say oh cool data and then that other
session rolls back it errors so data has
never actually been in the database for
real has never been committed so when
you then try to read again it's gone
right so
this is kind of a choice that was taken
long before I started maybe it was back
when Nikola was there I don't know
I guess yes
and no logs will be taken right and you
don't even have to wait for update logs
exclusive locks all of that things you
can just continue along which is also
why you can get dirty data
now the other one is update lock this
was what we saw in the quiz a lot of the
time after calling lock Table after
doing it right all reads will by default
be done with update lock that will take
what's called a u login SQL and we'll
see a little bit more about what is U
blocks and s-locks and something like
that later
um there's no uncommon data so that's I
think good I think most people would
agree with that however
update locks will be placed on all the
rows you read
which means they will stay valid for the
entire transaction no one can delete
your data you locked but it also means
you're holding that lock for the entire
transaction so if someone else is trying
to read with update log or try to modify
it they have to wait for you to be done
um and then we have exclusive luck it's
the same as the update log just stricter
it will block other things we'll see
that
right now I clicked the wrong button it
wasn't uh it was my fault
so um this is I want to give you the
technical term here because then you can
Google it so this is the SQL Server lock
compatibility Matrix it specifies on the
First Column you're trying to come with
the and request the following type of
lock
like let's say it's a no lock s or u x
and then on the header row there's what
there's currently applied for that row
so let's take an example of this
together
so let's say you're coming requesting
with no lock so you're doing a readout
committed and you are trying to ask for
a road that currently has an update log
on it so this will be a n which means no
conflict this means you are not blocked
you are allowed to read that row and
continue on right let's take another
example something maybe that blocks so
this is brilliant interesting
because this is what we have when we do
log table both of two sessions doing
lock trim on trying to read we have
you're coming with an update lock and
there's already an upload the update
lock there it's a conflict this means
the ladder operation the one trying to
read now will have to wait for the
former to release their lock relinquish
it
um
yeah so you know I gave you the
simplified version there this is a real
one
um
I don't think I'm gonna go through all
of them or even a few more of them but
the reason why I brought this one is you
can see there's a few more things than
just update log there's range locks
there is intent locks most of the time
you don't have to care about it but if
you end up in a situation you can always
go back to this just Google SQL Server
lock compatibility Matrix I'll look at
these slides and then you can you know
match it like I did there and you can
figure out if it's compatible or not
good
now again you know there's many
complexities and one of these is really
annoying but it's actually for good
reason is there it's called lock
explanation lock escalation so most of
the time when you go down and you modify
a row or you read something you you put
a lock on that row right and and maybe
you do 10 and you know it's all fine you
lock those but at some point SQL Server
to conserve memory will go ah you have
locked a lot of rows now this is not
very efficient you're spending so much
memory just on having locks and it will
actually group all the logs together in
what is called pages so Pages like an
eight kilobyte data structure type and
it will transition from locking on the
rows to that entire page or multiple
Pages it could also be which means that
you can actually end up locking rows you
have never read as long as they're just
in that same page
we have seen some really interesting
bugs on this and so keep that in mind
and it can escalate further up
right
so now we're kind of done with the SQL
now we're going into kind of how the
runtime decides based on knowing SQL
these things so I made a very simple
rules that I hope it is which is reads I
don't read uncommitted
as long as no rights or log table has
been done on the table in the current
transaction I should maybe have
underlined table here because it's not
the record instance it's not the record
variable as we saw in the quiz which
might have tripped someone up it is the
entire table type so for example
customer or currency or whatever it is
and it's for the entirety of the
transaction if you re if you call log
table at the very start it's going to
persist throughout the entire thing
unless you do commit
right and then the opposite if you did
do a right we're doing update lock now I
think it's easy so let's take a little
example here we have some relatively
simple code and so let's try to apply
this right so so we haven't done any
rights yet this is an action let's
assume there's no on before action
trigger so any trickery like that
and we're just going to say which rule
do we apply well to me it seems like a
drill one so that should be a read
uncommitted and luckily it is I ran
through this code by the way it is
correct what I'm telling you here
um and then we do a delete and and maybe
some was tripped up by like delete but
that's not log table well the lead
actually one of the first things it does
is it just calls log table under the
hood I'm sorry to break it to you but
that's like the the dirty secret under
the hood right so when we do code.friend
first we of course go to the rules and
it to me it seems like a rule too and
that means it should be
of that clock right okay let's continue
along now now we're talking about
another variable another record instance
another method
so which rule should we apply well we
still did a right to that table so of
course it is
two
and then we come to cost define first a
new a new table we haven't touched this
table before so we can go again rules
it's number one there you go we don't
commit it now
you know I think these rules are
something you can actually kind of apply
to your code to some degree if you
really wanted to
but that's a bit tedious it sounds kind
of boring if you had to do that with a
couple of thousand aligns maybe more I
don't know
so in the version 21 we introduced the
ability to see which locks you were
holding in the current transaction via
Visual Studio code debugger so you can
expand this database statistics and then
expand blocks and then cui the syntax is
maybe a little bit weird here for some
people
um access that doesn't mean anything it
just means access type and then the next
thing is what type of locks it is and
then more specifically what kind of logs
from SQL it is so it's a key lock in
this case that's maybe a bit more
technical than what will they dive into
here but it's good to have it another
option is and I'm very sure you can't
read this but we added it there so you
can copy paste it for for when you need
to do Advanced analysis you know you
just execute your SQL statement and then
or you get able to execute it for you
right you run it and then you fire off
this query and that will return you
precisely the the locks that are being
held in SQL
for you this is actually what visual
Visual Studio code debugger does under
the hood whenever you hit a break well
whenever you expand that thing it just
fires the SQL query reads it and present
this to you in a relatively nice way
so Telemetry I don't think you have been
on a session without some people talking
about Telemetry especially if they're
from Microsoft and so I'm also going to
talk a little bit about it but
actually Kenny he did it better than I'm
I could do so
go read his slides they're right there
there's both a QR code and there's a
link there it's from 17 to 21 where he
talks about how can you find out who
took locks and who was a victim of a
lock timeout I really recommend you to
read that it's better than what I would
have done this and internally most of
our optimizations are done through the
Telemetry so we are monitoring Telemetry
and this is driving the optimizations
that we know yeah exactly so there was a
you know a question on Flow fields and
and at least internally that was one of
them ones that I that tripped up a lot
of developers I would say and it's is
this problem of like well what should
actually impact if a flow field takes
reach would read uncommitted or with
read uh with update lock and and in this
case it's it's the target table right so
this is defined I believe on customer
um and it's the balance right and and
because it's reading from the detail
customer inter lecture entry it is
actually that table state that defines
if we're going to read with read
uncommitted or update log
now
in version 22 we wanted to introduce
give you some more controller about how
you read Because previously there's only
really been one control that's you can
have higher isolation levels you can be
more strict you can take more locks and
that was kind of it right lock table or
do a right
um
but we found that for a lot of cases
it's like you might have done a write
earlier and then later in the
transaction you actually want to read
something and you might be okay with
saying I don't need the strictest of
guarantees here I don't want to lock the
you know the entire table let's say
you're doing counter or find set or
something like that so we introduced A
New Concept and this New Concept we
wanted to be based on a better way of
specifying it maybe some more control
over it so we decided to do it on a per
record instance basis instead of a table
basis
we're going to see some examples of that
also so it ignores the current Table
state
you know if someone had called ride a
log table earlier if you use this
feature it doesn't influence any other
instances so if you have a three records
it doesn't impact the two other records
there or the further ones in the future
um as I said earlier we only apply these
hints for read we don't do it for rights
so this one also only works for reads
so
um
we have already seen these two the read
isolation values you can of course
choose those two I'm not going to go
through them again but we also gave you
access to two more options and these of
course maps to the SQL ones right so you
can go in and say I want to read the
data I want to read it read committed
which means you don't have dirty data
anymore
and the reason why you don't have 30
data is you place a shared lock
on the table but only for the duration
of the read right so it's kind of a nice
way to say Okay I want some kind of
guarantees and I want them not to lock
two people too long
I think this is really the best option
you have and it is also what we
recommend if you're using read isolation
to kind of give a good guarantees
without locking people yes and in some
cases you may need to use the read
uncommitted we'll show you an example a
little bit later yes so because they
differ a bit Yeah but if you need this
idea that like data stays consistent
for a long time then you actually need
to place these locks for the entirety of
the transaction and this is what you can
get from repeatable read you can go in
and say Hey I want to have this lock I
want other people to also be able to
read from this row
but
I wanted to stay consistent for the
entire transaction and this is what
repeatable read can give you
um
it does again it doesn't do uncommitted
reads which is nice this is kind of the
option you if you really need this if
you really need your data stay
consistent consider using this
now if we go back to the practicalities
right and we go back to the quiz and so
if we would take a look at this specific
example right how could we make it
better right how can we eliminate this
lock that we have on the count
so if you replace this code with the
following two calls and this is single
liners so we have replaced the log table
with update lock and then we are finding
lost
and then on the second instance we are
being explicit and we are setting read
committed this way we are just going to
lock the last record on the customer one
and we are also going to not lock
anything on the second instance
it's a very good thing to specify it on
the customer too that you want to read
uncommitted because you may not know in
which state you are so just to avoid the
maybe state which may or may not lock
so this was a simple optimization that
is going to lead us into the pattern
that we have here so yeah
so so we we kind of have these two
patterns that we want to present you and
one of them is what we call temporary
heightening right so so you might be in
a situation where you need to go in and
say
I need to ensure that whenever people go
through this code they need to ensure
that no one else can read it right so
gln tree or like any of the get next
entry node does it for regulatory
purposes right you can have two of the
same entry now
um so the the way we previously did that
was this kind of log table way of doing
it finding the last one and then we're
sure nobody else was reading that and
doing this trick
um this has of course the negative
impact that like if we do this early on
and we then query the GL entry well I
mean and you know this could be done for
any table right but if we then query
something later we might end up taking
really white blocks right or we can even
see log explanation and then suddenly
we're locking everywhere right so the
new way to do this with um with read
isolation is to just be more granular
right go in and say okay I want to read
I know I want to read that one with a
lock guarantee right so we go in and say
okay I need an update lock on that row
just that one row we take it out and
then whatever happens later they will
have to of course also think about do we
want to read here with update log well
then they just specify that but there's
now the option for them to do it without
it just implicitly locking everything
so we the way we think about like read
isolation is that it's pretty much
better than log table for almost all
scenarios and there is a few places
where we don't really know about because
it has always been log table right so we
don't know if changing it here to read
isolation update log will break anything
because someone had depended on when
they begin reading they actually
expected to take those logs yes so
there's an interesting game there
so the thing that we would recommend is
that for all of the new code that you
write that you use this new syntax
because then you're very explicit of
what you're locking
and if you would ask us are we going to
replace this specific code in the app we
are hesitant to do this because we might
be missing other locks you know this log
table that we currently have is probably
locking additional things and if we
remove it we could introduce regressions
so for this reason we are Telemetry
driven and we are eliminating the worst
performance of vendors right
so yeah
so I would also if you need to replace
the existing code do it with caution
because it is unlikely but it can cause
regressions
yeah and and another thing about and and
I think both of them actually is very
very important when you think about
event subscribers because when we're
thinking about event subscribers you you
have some idea of the context you're
being called in right you you subscribe
to an event but you're not actually
really sure what happened before you
right maybe there's another one
subscriber maybe that event subscribers
the different way around we don't
guarantee order by the way
um so you know you don't fully know the
the setup you're in so you know if we
have this code and you do this fine said
most of the time it's probably fine
right most of the time you're probably
not locking anything right but you're
not one percent sure and maybe there was
an event subscriber that called
locktable just before you or maybe it
was a lot before in the transaction so
this is one of those things where you
can now avoid that right you don't have
to think about you don't have to be
worried about it you can just specify
your intent explicitly so we think for
event subscribers this is going to be a
really strong thing because event
subscribers aren't magical like I mean
maybe they they kind of are right but
they also just tail code right they
behave the same way there's no special
like oh transactions Works definitely no
they work the same way yes so we highly
recommend using the medieval subscribers
yep all right so
yeah so when we're writing this code we
had this little kind of a discussion
between us how should you specify that
you want to be able so we saw this from
the quiz right so here you know pretty
obvious behavior when you saw the
question you now have the explanation
maybe it wasn't obvious to start with
but when we came to rear isolation you
can't because it's specified on the
record instance and I really want to
point this out it's on the record
instance not the variable not the table
record instance right so if you pass it
by by the way it stays there and you can
still is useful
um
but how would you specify this on the
customer record instance if you didn't
like like how would you specify it right
because it pertains to the record
instance but we saw previously it's
actually the table you're reading on
state that defines it so so we kind of
had to say like okay flow Fields behave
a bit different than how we generally
say when you're using read isolation so
you read isolation that you specify on
the record instance also comes for flow
Fields so you can also override for the
flow field Behavior even though the flow
field has someone that's called log
table on it you can also overwrite that
with record read
what yeah read isolation
yes and this is a great addition and
many developers are simply not aware
that you can optimize the flow Fields by
simply setting them on the parent
records so it's excellent for avoiding
locks on the clock fields
for the question also that we had at the
beginning with two bad blocks and we
have been seeing this kind of pattern
happening a lot so we are going just to
go through it here as well the way how
we would make sure that these locks are
not happening is by simply refactoring
the code similar to what we have done so
we would set the read isolation here to
read uncommitted because we want to
delete all of the records even the dirty
ones right
and then we would check if the table is
empty and then we can delete all
because the problem with delete all is
that it is going to lock the entire
table if it is empty and read isolation
does not apply to write transactions
so here unfortunately needs to search
this check is empty before you call
delete all to avoid the table lock
and then this other instance that we
have which is doing fine set is still
going to use the read isolation from the
first line at the beginning even though
you did the right transaction it saves
the state and it is not going to do any
locks when it reads the date
so be sure if you want to change it then
set it above the file set
yep so this was the addition that we did
then we have the repeatable read which
is going to help you to keep the um
read isolation until the end of the
transaction so if you want to make sure
that this is going to last until the end
of the translation you should keep it
and yeah
that's a very short one yeah and before
you go on to telling people how to be
smart there is one little caveat that we
we didn't have a slide for but it is
when you have set read isolation
on a record and you then on that record
call log table I don't know why you
would do this but if you end up doing it
that's going to reset the read isolation
I just want to warn you so you know if
anyone is trying to do this and then
wonder why it reset that's just the
behavior it does it's similar as writing
a different level of read isolation on
the same record so we believe it is
expected yeah we asked the developers
internally what did they think was
reasonable and
this was what they felt was reasonable I
hope you guys agree
so our strong recommendations for you
guys after this session is for existing
code refactor as you need and do it
incrementally focus on the worst
offenders that you can find either from
the Telemetry or from testing for the
new code we strongly recommend to use
the read isolation don't use log tables
anymore
and also if possible in many cases it
helped just to restructure a few lines
to move them up so it's better to do
reads before writing to the table if
possible
also we recommend to Cache the read
results so you don't call them too often
and we recommend to try to write the
small transactions and in case that you
need to write a longer processing code
ensure that the code is re-entrant and
try to break it into smaller chunks
the things that we have introduced in
the previous few releases is ignore
commit and this can help you how to you
can write the re-entrant code
unfortunately we will not have time to
cover these kind of patterns in this
session so it could be a topic for some
of the following sessions
yeah and one more thing about I I was
talking with someone earlier over here
they were saying one of the reasons why
they're here is is that they sometimes
have this lock time out right so you had
to wait for a lock for 30 seconds and we
throw an error right bad performance you
know bad for the customer of course
um but one of the ways that you can all
if you need to take the lock right one
of the ways you can also do it is just
by making sure you hold the lock for a
shorter time right it doesn't always
have to be we avoid the locks 100
sometimes it's just about making your
code faster while you're holding the
logs and that's there's plenty of other
good resources to learn about that of
course but that's also a very important
way to get around blocks
all right so this was all thank you very
much for your attention
and we hope that you liked it
all right so we are open for questions I
think we have a cool little thing we can
throw around yes so I'll just start here
good hi do you understand it right the
good approach is just to specify the
redresolation for each read
you can well okay so I just want to make
sure so you have to do it for each
record instance right so if you're doing
let's say you're doing a you have a
record in a customer record instance and
in the same record instance you're doing
five reads then you don't have to do it
in between every single one the state
stays there for all of those reads now
if you call clear of course it will
clear it right I mean but I mean from
the like pattern perspective from the
writing good code so if you spray if you
make a habit to specify it for each each
read then you are conscious about what
kind of isolation you need right now yes
I mean that's what I would hope right
that everyone is conscious about what
kind of isolation level do I actually
want like put that into their mind do I
need this to be super strong you know
like for example that geol entry example
that is an example where some developer
out there had a really good reason
regular store reason in this case
probably the best reason uh that they
actually needed to have such a strong
guarantee now of course it can't be that
you I don't think everyone should go out
and always think about this every single
time
but
you know think about it in in kind of a
moderate amount like if you have a hot
path Cove that you're calling all the
time yeah be a little bit more explicit
there so one of the cooler abilities
that we got is that now you can think
about do you want to read the dirty data
or not that was not possible in the past
so you cannot ask like is this really
persisted or not yeah yeah so this is
the capability that you got so you can
start thinking about it when you write
the code
and I also wrote Kenny said that you are
going to switch to read committed is it
like a plan or is it just out of the
session sorry sorry if I the code is on
my laptop somewhere
um
I don't think we're going to guarantee
anything on that unfortunately but there
is plans in the future to look into can
we change what happens after having done
a right because as you know right now
the ride leads to update lock what if it
led to read committed instead we're not
saying we're doing it but think about it
tell me if you think it's a good idea my
personal you know thing that I super hit
is the fact that delete all locks the
entire table on the empty table or that
counts locks you know that's something
that is not expected but it's the
existing Behavior I would like that
fixed as well so any more questions oh
yeah
a simple one not not very clear to me is
there's only session contact so what
you're told about is not affecting any
other sessions no just so if you have
that lock that does not persist in the
other sessions with every read you do
but only in your own session yeah so if
you mean log table or doing a right yes
okay there was one and the other one was
are you considering to make this a a
setting on the service to you that you
could set my read would always be this
isolation level I mean you had a
recommendation on use this one then you
could actually also make a choice this
is what you could do on your service to
you that's a good idea I will take it
back home to my to my manager and ask
him if we should maybe do that I look
nice at him I I cannot I cannot promise
anything of course but anyone else yeah
we have time for maybe one or two more
if you are
want to ask something I can't see you
then
no I don't see anyone then if you have
more questions I'm staying afterwards so
feel free to approach thanks so
[Applause]
