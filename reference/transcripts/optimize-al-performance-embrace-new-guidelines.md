# Optimize AL Performance & Embrace New Guidelines

- **Source:** https://www.youtube.com/watch?v=aqvUgL005OU
- **Video ID:** aqvUgL005OU
- **Channel:** mibuso.com
- **Published:** 2025-09-18
- **Duration:** 97m38s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Good morning, everyone. So, thank you
for joining this session in this number.
Really appreciate it.
So, first of all, it's really great to
be back after 2 years of speaking now on
Tech Days.
It feels fantastic and even more
fantastic to see you in this number. So,
this event continues to be like
the point for innovation, knowledge
sharing, and basically
for Business Central development uh
group together and share some knowledge.
So, I'm pretty excited to share some
fresh insights
uh with all of you today.
Whether you are basically experienced
developer or new developer just starting
to optimize your code, you will get uh
some
uh some tips which you can use. So, and
if you are experienced developer, you
will be familiar with some patterns.
Uh and if you come out with some few
tips, that's still
uh success for you.
So, we all know that L coding isn't just
coding and that's it. So, it is also
about performance, maintainability,
scalability, and everything. So, in this
session, we will go through that uh
those principles.
But first of all, before we dig deeper
into the details, let me introduce
myself.
So, my name is uh Stefan Sosic for those
who don't know me. So, I'm Microsoft MVP
now
uh focusing on Business Central
development on first place. So, through
my LinkedIn blog
uh
GitHub blog,
uh I am focusing on technical stuff,
Business Central development topics.
There are some also functional, but uh
more into development ones.
So, let's start with the details and
first examples and uh start optimizing
the code itself.
So before before we start, let's
introduce how we will perform the tests
with the results. Results are pre-run in
this case not to wait for some long
queries to execute. So we will be
using the toolkit itself.
So
I created little little toolkit here in
Visual Studio Code
which will we will be executing region
by region and then checking it out in
Business Central and then by each
example checking some charts and
checking how how it performed.
So that's that's first first thing.
Uh
So yeah, next thing how the queries were
analyzed. So with the SQL query analyzer
and they were catched with SQL Server
Profiler. So we will be checking the
demos, checking the times and then
moving to the queries how they look on
the SQL level and then we will see some
conclusions based on that.
All the tests have been run on two the
separate sessions. So and also without
user cash catching.
So after this slide we will
see how is that part done.
But the results which we'll see in the
in this session we'll apply
also for on prem or on or on SaaS
and the tests are verified on newer
versions. So I did the tests on BC 25
and 26.
Uh why I mentioned this? Because for
some some parts Uh, there is Business
platform optimization, which automat-
automatically does some optimization of
your SQL queries in the background
without you knowing it. And I will see
that in a bit on the first example.
But, uh, on the previous version,
well, I didn't test it, so uh, it's
possible that some of the feature you
cannot use on earlier versions.
So,
I already said that, uh,
we will be using the raw results, uh,
not uh, the cached results. And we are
doing that with, uh, before each call,
we are calling database select latest
version. And what will that do? It will
clear all non-locked, uh, records from
the client cache and also the current
session cache from the user. So, each
time we are we are
we'll be calling the database, we'll be
getting the pure performance between the
Business Central and uh, and the SQL.
So, you shouldn't do that, uh, on your
production environment, of course, or if
you don't know what you are doing. In
this case, we just need it for
performance. So, we'll be using that for
this demo.
So,
what is NST caching? So, benefit of an
NST caching is when you already run it,
uh, you fill the cache and next call
won't execute any SQL queries in the
background. So, you will have the
benefit automatically pulling the data,
uh, in milliseconds, uh, from the cached
results.
So,
for that example, let's just quickly go
through that one.
Uh,
I created like uh, just a simple loop,
uh, going through the customers, find
set, and that's it.
And that will be with NSD cache. So, we
will not be calling database
select latest version for that example.
And exactly same version where we will
be calling database select latest
version.
We will see now the results.
So, for this this results,
we have been creating
1 million customers to fill one large
table. And also vendor table, which is
dynamic. For some examples, we
had to do it with
smaller amount of vendors, some with
full. So, we will see that
on further examples.
So, two two tests have been run.
Duration is, of course, better with NSD
cache, because it is automatically
pulling it from what previously has been
pulled from SQL itself. But what it
matters and
is SQL statements executed. So, only
once
the SQL statement is executed, meaning
that once we pulled the data, and that's
it. Then we read it from the memory
buffer itself.
But with without NSD cache,
with with which we'll test further
examples, we'll be executing all the
queries again and again. So,
we will not benefit in this demo from
caching.
So, as you can see also SQL reads,
so NSD cache has just once on the one on
the first run. So, if we check NSD
cache, you will see that on the first
run it had
it needed
some more milliseconds to load, but then
it pulled just the cash from its memory
and that's it.
Okay, since we explained that one,
let's move to the
to the first example.
So, if you have been following me for
for some time,
I've written some blogs regarding
whether you should not or you should
write is empty before find set or vice
versa.
So, and actually we are This is the
first example where the BC platform
optimization happens.
So, when you
repeatedly execute find set,
you will be SQL will be creating stored
procedure for your you and after a while
it will wrap it around if exists and
then if you execute is empty before,
it will be redundant in this case.
So, let's first
first check the demo and then we will
move to the queries itself.
So, the code
is pretty simple. So,
we are again looping through the
customers here
and we are saying, "Okay, set range
country region code and if not customer
is empty then find set." That's it.
In the second example,
we'll be using
without is empty. So, we will we will be
looping through the code of customer
table and then just doing find set.
If find set then again some code. So,
without this part if not is empty.
How that that will perform?
So,
on the 1 million records here,
there is
significant difference just with uh some
calls. So, in the in these few calls,
there is a difference between
uh 1
2 2 seconds. So, but what is more
important and why why it happens is the
number of SQL statements because
because like mentioned, uh for is empty,
you will need additional query to be
executed before
uh find set, and that will be doubling
the the queries. So, find set without is
empty will take 3,000 queries in this
case.
And if we do it, same example, with is
empty, it we will double the amount of
queries. So, it can cause also the SQL
uh overload, and that will impact the
performance. And this is just one
session, one example. So, if you have
multiple user uh users and so on, so it
will be affected more.
Okay.
Uh so, this is on the full table.
What are the results on the 50 record
table? So, we will be We are using in
the background vendor table with uh 50
records. So, we still
benefit uh even though
uh it's a smaller smaller table.
And now you will see say, "Okay, when
when it is always empty,
so not 99% but 100% uh it is empty,
find set without is empty will be
actually a bit slower, but uh
when you have like uh the table with
100% is empty, so the those are rarer
occasions, and uh
I think you can benefit more if you use
uh just find set without uh is empty
because in most most scenarios, you will
have at least few times uh table filled.
And in this in this case, we'll be
executing the same number of statements
because on the one hand we will be
executing is empty statement, on the
other hand just the find set.
Okay, so let's analyze now
uh the queries.
So, here
here we are we are having uh sorry.
Here we are having the first
uh query which is for is empty.
And that one is checking is empty and
then followed by
uh find set uh procedure which gets the
data set into the buffer itself.
So, let's take a look now when we repeat
just the find set uh multiple time. On
the first run, you will see the SQL
Server creating a stored procedure
for your filter. So, and it looks
like this.
And after certain amount of running, you
will get if exists in front of the
stored procedure.
It is not in the same stored procedure,
so the new stored procedure is created
and wrapped around with if exists.
And that's basically the Business
Central platform optimization which I
was talking about earlier.
So,
how do I does the full flow work uh look
like? So, on the first run,
there is first query, just simple find
set, that's it.
On the second run,
we are executing that stored procedure.
On the third run, again the same, but on
the fourth occasion, like I said, now
Business Central platform
detects that what you are doing and uh
it optimizes your query automatically.
So, automatically new query is crafted
with if exists in front.
And after that, each goal which you are
doing, it will be executed from that
stored procedure. So, this this stored
procedure is 60, so it's not executing
anymore the old stored procedures.
So,
on graphically just displayed, so if it
is empty, we are checking with the
database, making the calls with the
database, then we move further. And if
you are doing
the find set, at some point it gets
wrapped with if exists, which
additionally sends queries to the SQL
database and causes overload and
performance downsides.
Okay. So,
let's move to the next examples.
So, set load fields, I guess
most of you use it, but uh
on most cases, maybe you forget also
some places to put it on.
It won't magically solve all your all
your problems, but it is really valuable
pattern which can lead to performance
improvements.
And what it does also, it limits the
number of loaded fields. So,
based on the queries which we will take
a look now, we will see why the
performance is just performing better.
In In most cases, you you just heard
that you should use like set load
fields, it will load just some fields,
and that's it. What we will take a look
on the SQL level and
see exactly what is happening on the
background.
Okay. For
this example,
set load fi- no set load fields, so we
will be looping through the customer,
checking
the place of export, for example, and if
the condition is
is true, then we will add it for example
example to the list and that's it.
In second case,
we will be doing set load fields, which
will load just the fields which which we
need
for for our logic what should happen
and primary keys will be automatically
loaded. So the customer I know you can
still use.
And let's see the results here.
So
like I said, the customer table is
a bigger table with 1 million records.
So if you are looping through
with
difference with this just optimization
with set load fields and without, you
will get significant difference. So in
this case more than 25 seconds here.
Number of SQL statements is the same. So
what is the difference now when we have
the same number in previous example we
had more SQL statements, so less
performance, but in this case same
number of SQL statements. So the main
difference would be the how SQL
statement is performed and
the weight of it. So let's
analyze
that one.
So
with set load fields, you are loading
all the fields from the table. So you
get
all the fields and if there are some
table extensions, you will get also
those fields from table extensions. So
if you are optimizing your extension
fully,
it can it can also happen that some
other extensions affect your performance
due to a loading those fields from other
extensions, not only yours.
But when you are doing with set load
fields,
you can specify which which fields uh
are you loading and prevent like
additional joins with additional table
extensions which connect to that table
and so on and so on. So, it's much more
optimized and lightweight query and it
just needs to read less data and then of
course takes
less time for it.
Okay.
So, let's let's move to the next
example.
So, with
find minus
or find set, what
maybe during the
upgrades or you find some old code, you
find into some occurrences where you
have
find minus and then looping through
and if you have more than 50 records, it
can cause
worse performance in this case.
Why? Because find minus will just load
50 records and that's it. And when next
statement is executed, it needs
additional call to the database to
refill the buffer. So, let's actually
use the next slide to better
understand.
So, with find minus
we pull from the SQL 50 records and if
we look through and
there is more than 50 records,
it the next statement, it needs to new
query to be crafted and sent to SQL in
order to pull the full data set. So,
that's actually one additional query
which will be taken and which you need
to take in consideration based on your
table size
and it can impact the performance.
So, for this example
find minus.
So,
yep, the same here. I did some changes
the last moment before.
Uh so, the find negative here, we're
just setting the the filters
then doing find minus
and
uh repeating
it true. And as the comment says here,
when when it reaches more than 50
records
and next is executed, you'll be pulling
again from the database. So,
and
with find set,
so you are loading the full data set in
front and you don't need additional
queries.
So,
let's see that
chart of the performance, so to say.
So, with find minus,
uh there is, of course,
uh worse performance and with find set,
since you are loading the full data set
uh and having it into internal buffer,
you are performing it better. When you
end up with 50 records and then needing
it more, there are there has also uh
memory real relocation to happen uh to
extend the buffer and relocate uh more
memory for it.
And the difference here is more into the
SQL statement. So, you see the double
number of amount. So,
this example was run into the loop, but
uh each time when you have more 50 or
than 50 records, you get one more query.
And let's let's see
from the query side how is that looking.
Okay.
So,
when you have
five minus,
you you load first 50 records. So, query
is just simple one. We are we will be
uh not combining too much of uh the
patterns together. We'll be just using
Of course, it can be optimized like to
use set load fields to get smaller query
and so on, but we'll be focusing just on
this example
isolated.
So, 50 records,
then you loop through.
It doesn't send any query because it is
internal buffer.
And when you hit
50 records, and then there is a need to
pull one additional record from your
data set,
it actually creates another stored
procedure. That stored procedure is same
uh
in some ways. The load and the fields
which need to be loaded are the same,
but it starts from the last record from
the previous query. So,
uh
the first 50 record
uh will be
uh thrown away, and then starting from
that point uh
loaded.
So, if you didn't so, basically, the
difference here is just the compare
between the the queries.
So, it's mostly the same, but it's doing
different things. The first one loads
just 50 records, and you should keep
that in mind when looping through
and keeping in mind which which uh table
are you working on. If it is always more
than 50 records, you will be ending
sending more more queries to your SQL
server and overloading it again.
Okay.
So, let's move to the next example
regards uh calc fields versus
auto calc fields.
So, what's the difference here? Again,
number of uh SQL queries and how much
you overload the SQL server itself.
So,
with calc fields and looping through,
each time you execute calc fields, you
will be sending one additional query to
the SQL in order to calculate those
fields and it causes SQL overload.
In second case, when you use out calc
fields,
imme- that's that statement is put in
front of find set. So, you get optimized
find set query, which we will see in a
bit,
uh which will automatically include the
fields which need to be calculated.
Let's first
check
the demo.
So, for this this example,
we'll be a looping through the vendor
table
with some filter
and then doing
calc fields of, for example, balance
and summing it too.
So,
simple example, that's it.
But, like I said, so each time when you
execute calc fields, you will be sending
additional query to the SQL and you will
be seeing that in a bit.
So, with set out of calc fields,
you're performing that query before find
set
and when find set is executed, it will
be optimized query. So, we will be doing
set out to calc fields of balance and
then looping through and adding that
balance. So, the end result is basically
the same.
How that looks when we take a look on
performance?
So, this this is just run
uh once and the difference is
significantly
because main reason is uh due to those
uh SQL queries.
So, number of SQL statements, you will
see here that it is like huge huge
difference in this case
uh
25,000
like uh
difference of SQL statements.
And how does that happen? It is just a
simple code, nothing else.
So, in order to understand better, let's
take a look
Let's take a look on the queries.
So,
there are few queries
here. First one, declaration and then
execution. So, let's take a look uh
detail look what those are.
So, first time
with the find set, you are
crafting find set query, pulling all the
data you need.
And then, first time you occur on calc
fields, you will be crafting the query
for the sum amount
from the vendor ledger entry, so on so
on. So, we need the balance
uh balance from the vendor table, and we
will be creating this this query.
So, each next loop, when when it
happens, so it executes that stored
procedure for each loop. So, if you are
looping 100 times,
just through simple find set, you will
be executing the queries 100 times. So,
you see now why it's causing
SQL overload like this.
So,
with find set, you pull the data,
and then, for each record which you
have,
you have again
to to point to SQL server
to say, "Okay, get me the data from
those fields which need to be
calculated."
And repeatedly repeatedly. So,
that that is what makes performance
down.
But when you are doing like out calc
fields,
you're just having one query. So, this
is the query, full query.
And you will see the second part of the
query, which is different from the
regular find set.
And if you take closer look here,
so it's again some balance from vendor
ledger entry, again the same uh similar
query which has been done previously.
So,
with out calc fields, you prepare find
set automatically to do the results
uh for for that field with that query,
with one just one query. So, with each
loop, you are not
mhm creating additional requests. So,
you are using the same internal buffer
which has been previously filled. And
that's it.
So, let's move to the next example. So,
I'm sure you are you are being coding
and then not being attention to much
whether you put in some procedure just
regular record or just with var or just
some fields. But actually, it can make a
difference.
And the main difference between
forwarding a record uh
through the procedure as a var will be
like transferring it with a reference
and not by the value.
And it can be beneficial in in terms of
the performance. But it it can be also
more beneficial if you ask yourself, do
you need really that amount of the
fields
or it is just easier to transfer the
full record and then work with it. Or
you say like,
let's transfer the whole record and then
at some point I will need more fields
with work to work with.
So, that can also have downside in the
performance.
So, let's take a look first on the code.
So,
first first example with record this in
the procedure.
So, we will be just looping through the
customer table and just forwarding the
simple simple procedure the whole
customer data set and that's it. So,
without var anything and we just use the
name field for example.
In second case,
so we are using
similar code,
but now we are doing it with var. So, we
are
transferring it with a reference.
And in third case,
we just forward what is needed. So, if
you use fewer few fields in that
procedure,
you can just forward those and it will
perform much better, which we will see.
So, here we will just call with the name
and forward the variable inside the
procedure itself.
So, let's check the results now.
If you check the chart,
first one is
just the regular record,
which is transferred by the value.
Then the second second column is
transferred with the reference and third
one we transfer
just the field, which we are needing.
So,
the number of SQL statements and reads
are completely the same. It We are just
talking about internal memory of the
Business Central and how is that
transferred from one place to another.
And
yeah, so in case you don't need full
data set, just use field.
In case
uh where you need to
forward whole record, think about it
uh and maybe it should be with file
record. The performance difference like
uh between
full record and just field
is so to say significant, but uh between
var and without there is a difference,
but you can live with it. So, you you
should also think about it whether it is
worth to put uh var in front.
So, let's let's move forward. So, here
we we was just talking about the memory.
We don't have any SQL queries to show
up.
So, what about now
calculating the totals from the loop and
with calc sum?
The main difference between those two
patterns are the place of calculation.
So, if you think
uh when pulling the data with uh loop,
you will be
uh focusing with summarizing uh all the
data on the platform itself, Business
Central, and when you are doing with
calc sum, you will be performing the
calculation on the SQL level itself,
which is much more
optimized.
So, let's check example for
that one.
So, in this case,
so we are having one one procedure.
Vendor finding uh looping through
and then summing budgeted amount, for
example, and that's it.
And the second example
will be
doing the same operation,
but but now with uh
setloadfields,
because that's a feedback which I got
like what will it be better than the
calc sum when we just load that field.
So, we will add that example as well.
And the third one
will be just the sequel part of
calculation. So, we will be doing set
range,
simple calc sum,
and then assigning that into total
amount. That's it.
So, first
let's let's take
a look.
So, here
we are having
No, sorry.
Calculating totals.
So, we have calculate totals in a loop,
which of course takes a lot a lot
a lot of uh time. But, when you do set
load fields, it's much much much better,
but still not best as it can get. So,
with
calc sums, you will be
sending optimized query to the sequel
and returning the value what you have
previously done in much much better
time.
So, if you perform this multiple times,
and then
take a look on the timings, it will be
much bigger difference, and you can
benefit from that one.
So, number of sequel statements in this
case same, but the difference is in the
query.
So, let's let's take a look on the query
itself.
So,
first query,
just just the loop, and you are just
loading the full record, putting it in
the memory, then slowly
so calculating all what you need.
The second one,
the second one, you have with set load
fields. So, you're just loading the few
few few fields which you need. And in
this case, you see it's much much
less less query. So, it's less weight
query much better performing.
But, when we compare that one to the sum
query which is
executed on the SQL level, it cannot
compete with that one. So, that one is
getting better performance
on first place by the place of
calculation
and so on.
Okay.
So, let's move to the next pattern.
So, if not insert, then modify. I'm sure
you have been using that one, of course.
But, it has a lot of downsides.
So, first of all, it prevents buffered
inserts.
So, that that one you won't
you won't be accomplishing if you are
doing buffered inserts.
And the second one which is mainly
responsible for the performance would be
the SQL error which is
generated on SQL server, then raised,
sent to the Business Central,
it parses it, and then second query is
created and executed.
So, that's that's the main reason. We
will see also the graphically
what happens. And it's main mainly due
to that reason of SQL error handry
handling. And the pattern is not bad.
But, if you use it on non-single phone
tables, it's so to say bad. But, if you
are using it for setup tables, so the
tables which are singleton tables,
it's highly recommended, of course. We
are speaking just about the tables with
some records in it. And you made mistake
and the first query just isn't
successful.
So, in this case, you try to insert, all
good.
But, SQL returns an error, which
triggers additional
triggers,
then parses on the Business Central
level level, and
only that then the modify statement
is crafted to the SQL side and being
executed successfully. So,
that first error makes makes a
difference. So, let's first take a look
on the demo and then
then see
how it performs.
But, the main question is is there
more efficient way to do it? So, there
is. So, we will see
in a demo.
So, let's first take a look on the code.
First one,
let's let's check
customer. We assign some anal, which is
already existing in the database.
Some name, and we try to insert. If not
insert, then modify. And I'm sure you
use that pattern
on on some places. But, actually, it it
can cause
performance downsides.
And what is the replacement for this
this pattern?
So, adding one additional query,
checking just if it is empty in front,
will determine whether you need insert
and modify. And now you will say like,
there is one additional query. Yes,
there is, but it is well much more
optimized
and better to execute that query than to
raise SQL error and then parse it on the
Business Central side. Even though we we
have here two queries, also for the get
statement, but get, since it is always
by the primary key, it happens almost
instantly. So, you will not lose any
more performance there. So, better to do
it like this, determine
which statement you actually need, can
it be inserted or not,
and then
then execute correct one.
So, let's check the performance side.
So, with if not then insert,
you will see a like big gap. So,
just
by checking if it if it is empty and
then executing correct statement, you
are performing it much much more better
since you are not raising any SQL SQL
errors.
So, number of SQL
statements and reads, so
we have a bit more
doing
is empty check, doing a checking if it
is empty and again then getting the
record.
So,
let's take a look on the queries.
So, from the query side,
when you are doing if not insert then
modify, so first you will be
crafting
insert query,
executing, then error like said is
returned to Business Central,
is parsed, then
corrected state correct statement is
crafted for the SQL and being executed.
So, and that's that's what we said makes
makes some time.
With
is empty and then correct statement, you
are just checking if it is empty and
that is select top one now, which is
really good performing query and it
doesn't cost much as you would make
mistake with
wrong insert. And then in the second
part, you will be seeing that we are
executing the modify statement since the
insert
since the record is already
existing in the database itself.
Okay.
So, but let's move to the next example.
If you are crafting some texts
and what are the difference? So, between
the text variable and basically the text
builder variable. So, mainly it is
how the data is stored in the
on the platform Business Central itself.
So, text builder is wrapper inside of
.NET.
But, text variable you can still use it
for storage of texts when you already
crafted some text and so on.
But,
text builder
that's data type by the reference. So,
similar what we did with the var in
front of the
in front of the record and without. So,
here we have the text builder which is
stored in the memory by the reference
and the text data type by the value. So,
each time
when you are assigning more
more more text into the value variable,
the memory needs to be
relocated and in order for new string to
be added into the memory
which requires new allocation of the
space so each time.
But, if you use text builder
since it is
by the reference and has a pointer to
the memory you just extend extend the
memory by itself and it doesn't cost too
much when
in order to to add multiple texts into
the same variable.
So, how how does that look? Let's first
check
the example.
So, the example is pretty simple. So, we
are getting all the customers,
then loop up sorry.
True.
So, the the example is
pretty pretty simple. So, we are getting
all the customers, then looping through.
And in first case, we are using text
text variable,
which is by the value. So, each time new
customer comes
to be added the name into the text
variable,
uh you will
be uh allocate reallocating the memory
inside the Business Central. So, that's
what is basically the downside mostly.
And on the second uh second example,
we'll be doing the same thing. So,
looping through the customers,
and then adding the names into the text
builder variable. So, end result will be
the same at the end,
but the performance is
lot lot lot better. So, we will be
seeing that one.
So, here,
as you can see, it's really big gap due
to that allocation, and it is not that
much that much of records and repeat
repeat repetitions. So,
if you are repeating it a lot on lot
places, lot users, so you can multiply
by by that even more, and the difference
is basically a lot.
And
number of SQL statements and reads are
the same.
And what we spoken about is just that it
is
uh the optimization of the platform, how
it is how are those variables stored.
Okay.
Let's let's move to the
next example.
Modification in a loop
versus creating a new variable.
And uh
maybe it's not fully fully clear from
the
uh title, but we will move to the code
uh in a minute. So, the first when you
are looping through,
you're getting on the first batch uh 50
50 records, then uh
first read is uncommitted, and when you
change it, it will change basically to
read committed uh query.
Uh
what is the code
example in this case?
So, you are writing the code,
and then
setting a range, for example, some
random name range on the name, doesn't
matter.
Then
uh getting the full data set,
and repeating until and changing the
address.
So, you done that plenty of times.
We are using the same same variable.
And
in most cases, maybe you didn't
uh didn't uh know that maybe it will
make a difference.
And but it will. So, what if you would
uh declare a new variable,
which you will modify inside your loop?
So,
the same variable, just vendor two,
same table,
and
saying, "Okay, that's that's vendor."
Assigning the same
address, too, and then doing modify. And
you will say, "Okay, that would perform
just same." And actually, it it won't.
So,
let's take a look on examples
here.
And as you can see, on the left side,
uh we are just executing it uh once.
And uh the left side was just with same
variable. And you was do it those uh but
it's still looping through. We have we
had the loop of the customers. So, it's
still looping through and for each each
one uh it takes uh more time than
declaring
uh the separate variable which will do
the modification do it the re-desolation
which happens on the platform itself.
So,
those are the examples maybe
you do in your coding, but you don't uh
don't think that uh maybe they can make
a difference. And uh all the separate
separate examples which we will show
are worth separately, but if you combine
them
together, you will get uh the best of
course result at the end.
So, let's
move to the next example.
Yep, but
here like check the query. Query is not
that that interesting. So, basically the
query for both both examples are the
same. Uh not not too much interesting in
this case.
You are just uh like we said
uh
doing it on the platform level or the
memory itself.
Delete in a loop versus new variable.
Not
to repeat myself, but uh it is the same
principle
with uh modify
which we had. And in this case delete uh
is not performing that much better
uh when you declare new variable, but
it's still a bit. So, we'll be
checking
the example.
And here
you will see like setting the range
again looping through.
And then delete.
And yeah, you will see for this example
it's pretty simple. You can use delete
all, of course you can, but
if you have certain conditions and then
or based on certain conditions to
delete, we are speaking just on this
isolated example whether you should use
the same variable which you are looping
through or just declaring the new one.
So in this second case
we are doing the same thing but
we are getting the vendor in the
separate variable and then deleting it.
So
actually
since we are having a
e and get query in front
it still performs
a bit better. Not not
not too much but yeah, we are speaking
about milliseconds here in this this
examples. So we can say double but
delete happens also pretty fast so it's
not not that that big a difference. Even
if you are
multiplying it on a lot lot places.
You can do it but the the more benefit
you will have when you are doing the
modify query onto the same variable or
not.
Okay.
So
let's continue
to the next example.
So how do you check
on some places maybe if the table is
empty or if that table has just one just
uh
non records. So are you using count zero
or is empty? And there is
a big difference.
So with this empty you're checking
select top one, which will be checking
in a bit the query and an examples. So,
for this we have the queries in for both
cases since the optimization
is on the SQL level itself.
And on the second when you are doing the
count, you're counting all the records
from the table. So, depending
how big table you have, you will be
performing better or worse, but you are
counting the whole data set.
So, for small tables, yes, there can be
a difference, but uh
not not that much. So, we are speaking
about
larger larger tables in this case.
So,
first, let's check the code.
Simple one.
That's it. Just vendor,
which had
1,500 records maybe, and checking if if
it is
zero, then exiting exiting. And in the
second example,
if it is empty, then exiting it. So,
basically both queries
are simple ones, but
the difference which we will see in the
queries is basically what is loaded in
the
uh in the SQL what is being checked.
So, first, let's check
the results itself.
And here you will see
better better performing is empty check
instead of of the count.
And for the statements, same number of
statements,
but you will get with the count more
readings. And that's what what was
previously said that with a count you
will need to take uh the whole data set
and check it.
versus is empty just checks if select
top now a one now and that's it. So,
uh much much le- um no almost no reads
versus reading how how ever you have
in the table records. So, in this case
we run it 500 times on the 500 the
records uh table and it had 500 reads.
And if you do it on even bigger and
bigger tables,
the difference basically in duration.
So, the benefit which you you will have
will be greater and greater. So, i- the
bigger the table, the better the def- uh
the difference between these two methods
is.
So, what's
what happens on the SQL SQL level?
So, when we execute the count, we are
doing the count
on the table and then reading the full
full table itself.
Uh so, in this case
20 records, but
uh with select top one you're we are
just uh we're just reading the one. So,
we are just selecting
uh the one checking if it is empty and
that's it.
So, that's main difference there.
What about temporary tables? So, do you
use the benefit of those temporary
tables? So, we will not have
SQL examples for this one since when you
are using the temporary tables, you
don't uh craft any SQL statements and
send to the SQL itself since everything
happens on the platform itself. So, no
SQL queries and the read, insert, modify
almost happens instantly. So, you should
basically use and benefit that from.
So,
we have a bit more examples here.
So, we just the regular table
created, then inserting it, looping it,
and then
deleting all the records. So, all
all the operations which you you can do.
So, we are doing it now.
Except modify. Yeah.
Uh so,
we are inserting, looping, deleting.
In the second example, we're using the
same table, just declaring it as
temporary.
And doing the same same operation.
Of course, that one will perform better,
but can we do do it further?
So, what What if we can declare the same
table as a temporary table?
So, the regular table
here
is just normal one.
Versus the temp table which has table
type temporary.
And we are doing basically the same same
type of the operation here,
but not declaring any temporary since
that table is already temporary itself.
And you would say like both are
temporary tables, no SQL uh statements
are executed, that must perform the
same.
Actually, not really.
Since So, let's check it. Of course, so
with normal table, we will we will be
getting
enormous result. So, that's that's
pretty pretty obvious. So, let's just
check the statements. So, we will see
that normal table each time it says it's
uh sends the query to the SQL itself,
then parses it and so on and so on. So,
let's just remove
the logs
from that first statement.
And then take a look here, just to have
because
the first one was
too big and uh we could couldn't see the
results from those two. So, if you use
normal table just declaring it as
temporary, you will get get the benefit
of the temporary tables, of course.
But, you can get one step further
with using your table uh is temporary
table.
Based on your needs, uh your processes,
uh
you will be determining uh whether you
should
and whether it fits your logic. But, uh
the difference is present. So, if you
are declaring the table as this
temporary, you will be gaining
additional benefit from the optimization
itself, which happens. And that one will
perform even better.
So,
we've spoken about temporary tables, so
the queries.
First one is crafting full query, uh
each query for each operation which we
do, insert, delete, looping with find
set, everything is executed. And this is
one with temporary. So, I selected all
the queries which happened in that
session, and we cannot find any
statement executed from the SQL server,
whether it is insert, modify, or find
set, which we was executing. So, nothing
happens on the SQL level itself.
And
if you're using the temporary tables,
maybe in In cases, if you don't need the
full data, you can use also the
dictionaries. So,
uh basically, the both both types are
virtual. So, nothing is get
nothing is on the SQL side. But again,
due to the memory optimization and how
the platform handles,
one way or another can be better
performing in some cases.
So, different scenarios, you choose you
need to choose by your needs.
So,
let's
check that one.
Let's first see the examples here.
So, we will be using first the temporary
table, but with some partial records,
just with some records from the table
in this case, and
and name from the vendor table.
And that's that's it. So, we are not
needing the full
full vendor virtual table.
And in the second example here,
we'll be doing exactly storing the same
data. So, and uh
and the name
again, of the vendor,
and storing it now into the dictionary.
So,
different different place of storage.
Both both as we said are virtual and
does don't send any SQL queries itself.
Then we have two more examples.
What if you need like the full and
complete record? So, in first case, here
we are transferring the full
vendor table, then doing the insert.
And on the second place,
we are doing the complete record, but
with dictionary. So, we go
go by the vendors, repeat, and fill the
dictionary table by by the values. So,
and this is this is
the part where the downside happens.
So,
let's check those examples
here.
So, first first two
which we have are the temporary table
with partial record and
director
dictionary with partial record. So, we
are not getting the full
full fields
all fields.
And in this case,
if you use dictionary, it will be better
performing than
temporary table. So,
based on your field numbers, how much
you need, you should decide whether to
use dictionary or temp table.
And in second example, it's
another way around and another way
around in terms of the performance. So,
you will be
getting the temporary table
with complete record versus dictionary
with complete record. And it's it's
performing much better in that case when
you use the temporary table with
complete record versus just filling the
dictionary because that will
cause too much overload
and
in the storage itself.
Okay. And obviously, here we don't have
we don't have any sequels. So,
since both both both are virtual.
Let's move to the next example.
Find first, then loop through. So, if
you didn't notice, but that's that's
also Code Cop rule, this one. So,
basically, what we have mentioned in
some of the examples is that you are
getting internal buffer size for just
one record
or
the cursor, which was in the vision. So,
basically, this this was from the old
days also
the downside.
And if you need more records, then we
are sending
sending additional query to refill it,
and then you need to reallocate more
memory also to it.
So, in that case, record which record
set which is following can be too big to
fit in the allocated already allocated
buffer size. So, memory reallocation
needs to happen in order for the second
query result to be stored.
So, find first.
Next, no record in the buffer. We are
reading it again from the database and
selecting
the next data set. So, let's do check
that
graphically.
So, you're doing find first.
SQL is returning just just one, and you
can still do it do the next statement.
But but when you actually do the next
statement,
the new again, similar to what we had
with find minus and find plus plus, so
you will get just the 50 records. In
this case, you will get only one record,
and you can still get additional ones,
but it will take one additional query to
fill
data set, and you will still be able to
continue working with it. It just needs
more time and more more calls to the SQL
itself.
So,
let's check the code
first.
So, here,
again, simple examples for better better
understanding.
Just vendor find first. We are getting
one record. We can still do repeat
until, no problem there. But when first
time next is executed you will be
doing the call to the sequel to return
the full data set. That is also
possible. You will still have a working
code, but uh
again, memory reallocation and one
additional query it costs you.
Find minus. I just put it so we have it
in the in the
comparison of the performance. So here
previously we mentioned you will load 50
records with the next if there is more
than 50. Again, you will need memory
reallocation and again to fill again the
buffer with different data set.
Versus just doing the find set correctly
according your your needs, correct
filters, sortings if if needed, and then
repeating and looping through. So you
are just getting one query from the
beginning and that's it.
So let's open the demo kit here.
And you see
how we go. It's basically
the order. So with find first one record
lot of memory
reallocation needs to happen in order to
store it and also one additional query.
So
let's switch to the sequel statements.
So in the first first two
examples you will be executing first one
like find first or find minus. And on
top when you
uh the end of the buffer, you need one
additional query to be executed. And
that's basically
the difference uh regards this this this
performance here. So, better to
determine
in front which type you needed.
Okay.
So, let's
continue presentation.
So, here what happens on the SQL SQL
side,
uh you will have
first select top one. You will get the
full full record uh loaded. And
immediately when you
uh execute next, it will say, "Okay, I
don't have next uh next record." But uh
similar to minus uh find find minus or
find plus,
it will start from that previous record.
So, it will not be that one
uh won't be loaded into the next data
set, but the data set is refilled with
uh fresh data which needs to be used.
Let's move to the next example.
So, the next example would be are you
using and whether you you are using is
empty or find set uh
find set, of course, I hope you are not
using before
uh modify all.
So, is empty is already checked on the
SQL level when the query is being
crafted. Also, in the same query, we'll
be seeing
uh that
uh the number of row rows uh which are
in the database table
uh are already checked. So, with find
set, you just perform additional
selection, storage into memory, and so
on. So, that's not worth at all.
And uh the locks which happen here
uh
are intent exclusive lock which happens
uh on the page same. and on the row
level just exclusive
uh lock
and modify all in this case just
performs all all those checks for you.
So
let's check
the examples here.
So first one we will be doing
if not is empty then modify all
by some filters. So first one just
setting name filter, checking if it is
empty, modifying all.
The second example we will be doing with
find set.
So loading additional
records in the data set and the last one
just simple filter and simple modify
all. That's it.
And how is that
looking on the performance chart? So is
empty
one additional query
which is already checked with modify all
uh and takes additional time of course.
Only modify all is just performing
much much better. And if you're doing
find set, of course logically you're
storing all the data set, you're having
also memory allocation and storage. So
it's performs
much much worse. So definitely never use
find set here.
In terms of statements, so we will be
seeing like that the last one just
modify all doesn't have that one
additional query which we had with is
empty or find set.
And that's
what here makes a difference. So the
first one
it makes a difference
uh due to
the query number and key query execution
and the second one due to the data set
which needs to be stored and allocated
into the memory itself.
Okay.
Let's move forward. So, filtering on the
flow fields
uh
is it the same or is it the worse as you
are looping through and then
using the custom filter on it. So,
basically, the filter on flow fields is
not bad as expected. So, you are
expecting that uh
it
does the calculation
and it actually triggers uh calculation
for each record, but it is not
uh not really bad as you are looping
through and it is in some cases good as
out calc fields and in some cases just
uh even faster.
So, what what we are spoken speaking
about?
Filtering
here.
So, customer setting filter by the
balance,
finding the set, find set, and then
repeating. So, we are
Yes, sorry.
Thank you.
So, we are
setting the filter
uh on the
calc field uh
and calculated field, which needs to be
calculated for each
uh each uh
record and then doing the find set and
repeating until.
versus
when you are doing out of calc fields in
front and then use it in the condition
itself. So,
basically, the the result is the same
and out calc fields is performing
uh also pretty good, but both both
results are not uh not the first result
is not bad as expect expected. So, it in
some cases like uh in my example, so,
when I when I run
nine of the 10 times, it was
uh it was like this. So it the
difference
uh the difference is really small but
with filter just on calc field it
performed even bit better in some cases
like this. So if not the same you will
get
even better result
on filtering it. So
don't don't be feared to use it
to filter on calc fields because it will
perform just as good as out calc field.
Let's move forward.
Lazy evaluation and I hope you are using
you are using the benefits of it. So
basically what when you are checking the
the certain conditions
in
your code it matters
best would be to exit early as possible
and this is what what I have been also
seeing when contributing
to business central open sources that a
lot of lot of developers are just uh
nesting the loops and executing all the
conditions even though it can be early
exit
and
you can optimize it quickly exit
whenever it is possible. So you don't
overload anymore.
So we have
some examples here when you need
combination of the the
combination of the conditions and when
you need just some
condition to be
executed.
Uh so in the first so in the first
procedure here
we will be using no a lazy evaluation.
So we will be
executing first condition then second
condition
and then
executing some code if that is true.
So the first one always returns true.
The second one returns true, but also
has some heavy duty code inside of it,
so to say.
And how you can do it better?
Like I said, so you can check always
your code whether you can exit it early
early as possible. So in this case
it also matters the the
position, how do you structure your
code. If you put first the heavy
procedure,
doesn't make any sense because you will
get again the slow slow results. But if
you determine which which conditions
will take less time
you can early exit and benefit from it
not executing all the conditions.
So how you can also do it is with a case
statement.
And here again, the order how do you put
the procedures also matters.
Whether you put it first heavy, so it
will be by the order.
So if we do the case statement just
other way around
first heavy duty one, so it will be
performing worse, which we will see.
So you can also do it
with in statement. And here again, it
always depends how you structure your
code and which which which procedure or
condition is checked first. So in true,
so it will be checking first one, then
second one immediately if it is found in
either of condition, it will
go to the code or exit. So in this
second example, I just rotated those two
and we will be
since this one is returning also true,
we will be executing just the first one
and that's it.
And we have two examples
with and condition. So when you need
both both condition
better to
do it like this.
And in this case, you will just run
the second procedure only when it is
necessary to do it. So in first first
case, you will do
first one if that is false.
Sorry.
You will in first case use
execute first one
and the second one and in the second
example the first one and if that is
returning false the slower one inside it
won't be executed.
So let's take a look
on the examples itself.
So we have
pretty pretty much of those.
So
without
lazy evaluation, you will get
more time and just do executing the
slower procedure.
When you have low
any of lazy evaluations with either or
case
with casings or in
or early exit like we have in the first
example.
So you will be
exiting it immediately and avoiding
executing slow slow procedure and that's
that's basically the point of lazy
evaluation. Similar to those to end
result with when you have two procedures
which both needs to be
true in order to execute some code.
Okay. So let's
move forward.
Changing the filters inside the loop. So
what will do that? So when you do that
in your code, it will invalidate your
record buffer which which you have
already filled in. And when you trigger
the next statement, the new query needs
to be triggered and executed to refresh
the buffer which you have. So,
uh
even though the first records are loaded
correctly, you will need additional
query to repeat. So, it sends just
unnecessary load for it.
So, let's let's check the code
here.
So, changing the filters inside the
loop, so we are setting
setting some filter, set range based on
the country, for example, then find set
looping through, and
we have condition. So, if, for example,
international shipping for that vendor,
we set range to different different
filter. And what it does, it invalidates
like full full data set and fills
another data set in in instead of that
one.
But you can do that just with some
temporary tables
like we we covered earlier and avoid
that one. So, you should not do that the
uh
to the reason that you will invalidate
the data set. So, you can still loop
through all the vendors,
then check change the condition, adjust
either save it into the temporary or
just mark it and then use it uh use it
uh below
to to do the separate operation for
those.
So, even though we are then using find
set, but on temporary, which performs
much better.
So, that that part this this part of the
code performs much better than previous
one when you're invalidating the buffer.
So, changing filters
here.
So, when you change change the filters
inside the loop, you know, we execute it
just just once. There is a big gap in
performance even though we have like
15 lines more, but those are everything
for temporary tables and no sequels are
being exchanged between Business Central
and the SQL server.
So, the first first one is performing
just better and uh number of SQL
statements is of course less than just
invalidating the buffer.
Okay.
So, here
what what uh we show. So, first the
query was crafted with correct filters
and everything. So, data set is filled.
And when you invalidate data set, you
set different kind of filters and
execute that again stored procedures
procedure which has been already crafted
for it that that filter, but the memory
is erased and filled with uh the new
one.
So, next one is empty or find set before
delete all.
It is similar to modify all, but it can
also have some downsides. So, let's
first just just check as we did for
modify all. So, is empty just
additionally find set
fills unnecessary record. We will not
repeat
this part.
And for
for the examples, so is empty before
all. So, we are checking if it is empty.
Then
Yes. Sorry.
We are checking if it is empty, then
deleting all, then doing some insert.
Then we are you are seeing that we are
doing insert after delete all.
And in the second place, we are doing
find set a find set then delete all,
then some insert.
And on third example, we are just doing
delete all and then insert.
So for first time,
we'll be doing that on the the table
which is never empty.
We all always fill it between the runs.
And in those cases, is empty before
before delete all performs
worse than just delete all. And if you
find find set, of course, it is just for
comparison, but I hope nobody use it
like that. So find set just loads
additional data unnecessary for this
operation. So is empty a or delete all.
So in this case, when you have the
the table which is never empty, you gain
the benefit and
benefit of having one less query and it
will perform actually the better.
But
So let's
return here.
So
what what is happening in the query? So
even if you have
you are doing delete all and the table
is empty, that one is checking if row
count count is actually different from
the zero. So if the
is any records in the in the table and
if so, delete all will be executed.
Otherwise, it won't.
But
So
just a second.
So is empty delete all.
Is empty query
just checking if it is empty, then doing
delete all. Doesn't matter at this point
to you, but
does lock behavior happen here? And
answer is still yes. So, it does does
happen. So, I did also some additional
test. So, when you actually hit the
table and when it that table is empty,
and you are performing the inserts
afterwards,
so it will perform
worse.
So,
we will be executing the same code.
Here it was.
So, the same same examples, not to go
through once again. But, we are doing
if not is empty, then delete all. So,
that that's important, that one is empty
before delete all.
So, let's run.
Oops, sorry.
But,
delete all.
Let's check that one, and we see the
duration now just delete all, that it
performs
less better than
together with is empty delete all.
Because if you hit the empty table, it
will lock it itself, and then with
insert hit,
it will take more time.
So, that's one thing which you need to
keep in mind.
And one more example for the end. So,
count one. So, how do you find one if
there is just one record in the table?
So, if you are doing count one, you are
performing, like we said with count
zero, you are checking the whole data
set. And if you're checking like on lot
of records, you are checking lot of data
set.
Uh, so with find minus
it's
uh, it's better. You are selecting
uh, 50 records and find first
uh, one additional query just to pull
additional record.
So,
let's check that code first.
So, first we have count equals one. So,
here on 1 million records is the
customer having just one record? Not.
Okay.
The second example is find first then
next. It can be a way. It will
give correct result, but with the next
statement like we said for the find
first you will just have one record uh,
in the data set. So, one additional
query to fill data set again.
And third one is with find minus where
you will pull 50 records in your data
set and then say, "Okay, let's go next."
And if that next is succeeded, then you
concluding that you have just one record
and that's it.
And uh, when we check on this this large
table,
the results are significant. And this is
just just one repetition a repeated. So,
if you are repeating it multiple times,
it can be
significantly uh, worse. So, I have been
also running it uh, with uh, 500 times
and we are ending it with 10 to 20
seconds difference uh, between
uh, count and then checking find minus
with next. Even though there is
one
additional
uh, query,
but uh, but the result in durations.
So,
uh, but the result in duration is much
better when you use find minus and next.
Okay. So, first let's check that one.
Here,
Count full data set, we said.
With 5-
we are up
With 5-
we are loading the fine first. We are
loading the first data set, then
completing it with additional ones.
And with 5- we are loading just the 50
one and we can check in the buffer uh
which one to fill. So, 5-
pull 50, then first record with next
check. Just check if the next one is
existing. Yes, okay. That's that that
means
uh
that's it.
So.
Uh
I would also invite you. So, since you
are in this this large number, so we are
trying to get there
uh more more traction onto into official
L guidelines. So, these L guidelines
have been originally created by
Henrik Waldo, AJ, and Jeremy.
Uh but
uh we are planning to bring some more
traction and involve much more customers
and partners, developers uh from your
your side to to get involved with it.
And that's actually, if we take a look
here,
uh pretty good. You can check docs, see
valuable patterns, and that will
increase by the time
uh we speak. It will be
uh more and more.
And uh also one thing I I think maybe
you didn't know, but it is under the
Microsoft uh repository. So, Microsoft
is the owner and uh it would be very
beneficial if we have one place where we
will define all the patterns and then
also for open-source contributions, you
will follow those patterns and then we
have
much less time to spend on reviewing
some additional features. So, you can
you are able to ship your features into
open source much faster
due to not getting that much comments
into reviews from other community
members or Microsoft.
Okay, since
since we are having some t-shirts
here
let's see if we have any questions here.
Okay.
We have four t-shirts. But questions we
can do more.
So,
I have two two questions. One is uh
that if it's about
Yeah, yeah, one t-shirt but two
questions. So,
uh about that if insert and modify
pattern and temporary records. So,
in temporary in temporary records does
it make any well difference
what
the same as was with real table
Yeah, yeah, basically the real table
whatever you perform on the real table
you will create the SQL statement and
then communicate the SQL server itself.
When you do with the temporary table
there is no no query SQL queries, no
communication between SQL server and the
the business central itself. But then
but then that if insert and modify uh
if insert and modify on temporary table
so is it Uh no, no, no. You that's
that's fine because again the main
downside for if insert if not insert and
modify would be the SQL returning the
error and then parsing it onto the
platform then returning the signal again
to the SQL server.
With another query. And another question
about the set auto calc fields and the
blob uh
fields. So, let's see if you
in the in the in the
repeat sentence, you only
will use usually use calc field on the
blob but only in certain condition. So,
is it better still do set auto calc
field on blob or
If the condition is really small and of
course the number
I I think still not because
depends depends on the condition. Like
if it is like just few occurrences
without set calc fields, you will always
calculate
but good good one. So,
you can avoid like loading it for
certain conditions which you cannot do
with auto calc fields and in those those
those points, I fully agree that those
makes sense to use just the calc fields.
Yeah, thank you.
Thank you.
Yes.
We can do our next there. Try.
So, when you compared the performance
between using the record
reference against
using a field as parameter, Mhm. and did
you do the test with multiple fields
too?
Yes, yes. Up to like so to say I I did
the test uh two three to five fields
uh being transferred and the result is
same. So, anything above that, I would
not consider because uh
it is just
the code is not maintainable. So, you
get the the the performance side better
but the code is just looks wrong. So, if
you put 10 10 parameters inside the
procedure and then it doesn't make sense
any sense in the code wise and in the
performance wise. But if you keep it low
like few fields
that's that's totally fine. Not only
one, but let's say three to five,
maximum five. Okay, thank you.
True it.
I will come back to Arthur.
Thank you. I have a question about um
query objects.
Um can you share any insights on um
performance and how secret queries are
created when comparing a find set to a
query object? Yeah, the queries uh when
you use the query object, uh the queries
which are crafted
are much different.
So, of course there is uh there is
benefit of it. So, even with the
calc fields, if you use the the queries
itself, it will gain gain more
performance uh than just to use uh the
regular one. So, it's different
different logic. We didn't didn't cover
that one here. Um how about the
difference on just flat query objects
when you just read one record without
any uh
flow fields on it?
Uh
how do you mean? Is there a difference
between a find set and a query object?
Do you have any insight on that? I mean,
if you just uh if you don't use any flow
fields Yes, uh for the first one, not.
For the uh repeating times, uh when you
run the query, it will be much much uh
better performing than find set, just
find set. Okay, thank you.
You have a lot questions, but
we will cover we can cover all the
questions, but
Yes, yes. Um I have a question on the
modification in a loop
where you're assigning to a
Yes. new variable. From a core
perspective, it feels a little bit
counterproductive. Have you any insights
on why it performs better? Yes.
Actually, yes. So,
inside the memory, since
especially for the modification, since
modification you are doing it on read
committed, so it needs to be changed to
read uncommitted in order to do the
modification, and afterwards to
continue. So, in those those terms,
that's that's the difference
when you are doing uh basically the read
and modify on thing. That is correct.
Yes.
Just not to do
Perfect.
Um my question is regarding using the
set current key, because I see a lot of
developers that is using set current key
all the time when they are using a find
set.
And how do you look at that especially?
if there is one key, and that one key is
primary key, that's not necessary. I I
see it if it's
If you have different kind set a
different
a different kind of
values that you're going to
it's it's worth worth setting it,
especially if you are doing it like
find plus, for example, and starting
with some order, whether you want to
load the records from beginning or from
the end.
It's better to use correct correct keys,
and then set ascending or descending,
for example, and that will perform even
better. But if you are using the set
current keys,
it can be better performing. That
depends on the case, basically. Not not
always is necessary, but in some cases,
yes.
From what I have seen is when people are
using it, but the find set always that
Not not not necessarily always.
Sometimes sometimes that it will always
in the SQL query behind use that order
by statement.
And and there you will have some miss
overload in the SQL because that it will
always start to
order the data
before it's just getting the data that
you just want and let the SQL handle
with the best key. Yeah, yeah, I would
start with without set current key and
then use the SQL insights from the
debugger itself because I had like few
few examples when I was working with VAT
statement lines when it is pulled but
not directly. So from other part of the
order order of the code. So it was like
loading one report like 20 minutes.
And it it had
it just needed one set current key on
that VAT
statement lines and it performed like in
less than 2 minutes. So it can be really
beneficial. But depending on really
scenario
and digging through like
on the on the eye you cannot see it. But
looping through the debugger then
checking the queries which are executed,
you can see whether it needs to be set
it or not. And then setting it
correctly, it can benefit a lot of
course.
You can you can
Do we have to to to break?
Yes.
You you can find me afterwards there.
Thank you.
