# Planning table indexes for the best performance

- **Source:** https://www.youtube.com/watch?v=-dadVb3I1BA
- **Video ID:** -dadVb3I1BA
- **Channel:** mibuso.com
- **Published:** 2025-08-07
- **Duration:** 94m00s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Ladies and gentlemen, welcome to the
session about planning table indexes for
the best performance. Please give them a
warm welcome, Alexander and Stefan.
Thank you very much. And so, yeah, from
my side again, hello and welcome to our
session.
In the next 90 minutes,
Alex and I will try to explain to you or
give you an overview about what table
indexes we have at our disposal in
Business Central and what we can do to
achieve a little bit better performance
on our queries.
Hi. I want to join Stefan in saying
hello, good afternoon to everyone. Uh
welcome to our session and thank you for
coming.
Uh few words about who we are. I'm
Alexander, Microsoft MVP.
Uh I work as a solution architect for LS
Retail. And among other things that I
do, uh
I'd like to like emphasize one thing, uh
what I like to uh define as making the
application run faster. Let's say. So, I
work with performance.
Uh behind this QR code on the screen,
you can find
my blog, where I also write about
Business Central development and mainly
also about
around the same topic, Business Central
uh with SQL Server and performance
questions.
And this is pretty much what we're going
to talk about today.
Okay. Um yeah.
My name is Stefan Maron. I'm a freelance
BC developer. I'm uh also BC uh MVP
since last year. Um you may know my
GitHub project, the uh code history on
GitHub, and also the sandbox history. Um
occasionally, lately not that much, but
I try to pick that up again. I do code
streaming, live streaming on YouTube,
just explaining concepts as I go. Um
yeah, and you can find me on Blue Sky,
on Twitter, uh on my blog, and uh yeah.
Let's get started.
And to start with a little bit of funny
note,
I'd like to introduce the session with
this
quite famous now quote by Michael Swart,
who is a SQL Server expert, used to be
an MVP in SQL Server sometime ago, and a
while ago he
coined this phrase, which has become
famous by now, I believe.
If you're using over 10% of what SQL
Server restricts you to, you're doing it
wrong.
And this applies, very strongly applies
to indexing.
And one word
I would say even 10% of what SQL Server
restricts you to when it comes to
indexes is even too much. We can create
up to 1,000 indexes in SQL Server.
If we have 100 indexes on a table,
probably we're definitely doing it
wrong.
So, this can be like a punchline of our
presentation.
So, that way when we when we talk about
indexing, when when we talk about
performance and planning the indexes, we
should consider it from every point of
view. At every time we add an index,
we may improve performance of some
data retrieval query, but on the other
hand, we're very likely to break
something and slow down insert, for
example. So, with this in mind,
we'll start.
Okay, one word of caution right away. We
have, I think, over 60 slides. We don't
have any demos because we don't have any
time for demos because from now we'll
we'll start talking a little bit faster
to make through make it through all the
content we have, so it might look a
little bit like this.
So, just
it will be technical from now on.
So, this is the agenda we came up with.
First, we'll talk a little bit about
indexes in general, what it is, why
even, and some some ups and downs
um, to indexes, so we get all on the
same page. And then, the main part,
we will go through all the index types
we have at our disposal in Business
Central, as I said in the beginning.
There are quite some of them. And we,
uh, will talk about their ups and downs
as well. Give some examples as good as
we could, um, to give you a feeling of
which index can be used for which
scenario. And what is it good for? What
is it bad in?
Um, afterwards, I have a small section
for, uh, yeah, trying to explain a
little bit the way also I we created the
the examples. How to, uh, check the
index yourself, whether it's used or
not, whether your query fits to the
index you created or the other way
around.
Um, and at the end, we'll just sum up a
little bit, give some general
considerations when it comes to
indexing. And then, we'll just wrap
everything up again a little bit, so
you, uh, you don't leave confused more
confused than you came here in the
beginning, maybe.
Uh, I believe most people here know what
an index is.
Like, how it works, when it is used.
But, I still believe uh, that it is
worth spending a few minutes to recap,
let's say, speaking about the very
basics. What is an index? Uh,
and basically principles of index in the
table.
So, in the most broad definition of an
index,
it's a any data structure that supports,
uh, faster data retrieval, data access.
Uh, one we talk about an index, most
common understanding, the most common
most commonly used type of an index is a
B-tree,
tree structure,
like which is implemented in SQL Server
as a B-tree.
Uh, we can think about this index by by
an analogy.
Uh, imagine it like, uh,
alphabetic index in a book. Think about
an encyclopedia. Uh, when you want to
find a word
in a book, uh
you sure don't want to leaf through the
whole book, read the whole content of
the book if you want to find the one
word.
Uh you can open the alphabetic index
where every word will be sorted by by
the alpha in alpha in alpha alphabetic
order, uh and the index will point you
directly to the page where you can find
the word that you need.
And that's the most common analogy and
it's uh pretty much accurate, I would
say,
when we're talking about one kind of
indexes, uh specifically B-tree index.
But as we will also talk today, not
every index is made equal.
Some indexes are based on different data
types, different data structures
intended for different types of
workloads,
uh
but uh still the basic principle
remains. An index is a data structure
that facilitates data reads.
Uh that
Exactly. And this is uh one picture I
came across which pretty much explains
it a little bit better. So,
um
we when you you you need to think like
he said uh of a tree structure. So, we
have that uh entry point and then it
gets more detailed the more levels we we
get down in that tree structure. And um
how big those pages are and everything
that's internals we don't really need to
care about, but as as as you have more
data, larger keys, this tree structure
will grow.
So, um when we when SQL Server starts
searching for a value, it will always
start uh from the highest value from
from the leaf as you can see in in in
the picture maybe. And then now if we
take an example and simulate just how
SQL Server looks for a value, if we take
57 as as our sample value, it will go
through the through the leaf it's it's
looking at.
It will uh
search in ascending order until it finds
a value greater or equal than the one
it's searching for. And if that's the
case, it will go one level, uh, deeper
and continue until it can find that
value it's looking for. And then on the
right hand side next to the 57 on the on
the lowest on the lowest level, you see
that B1C1 thing? That's basically the
reference to the main table to read all
the different data, the remaining data
for that specific record because an
index does not contain that by default.
So, when do we want to use indexes? Uh,
uh, Stefan just showed in his example.
Well, obviously, when we want to find we
want to want to find some specific piece
of data, pinpoint a record in a table, a
small subset of a table.
Like getting a customer record, uh,
filtering, uh,
few records in a table, searching.
Uh,
So, in this case, instead of, like the
book example, instead of, uh,
scanning, uh, reading the whole table,
comparing every value with what we're
looking for, we can use this the index
structure to quickly descend to the
value we're looking for.
It works perfectly, uh,
in when we need to aggregate a small
amount of data. It's, uh, we can think
about it again
as a special case of the first example,
uh, when we're on a calc sums
expression, for example.
Uh, and we need to summarize just a few
records.
Basically, in the back end, what
database engine needs to do is find
those records that must be summarized,
read them, and calculate the amount.
This calculation can also be based on an
index.
Uh,
flow field, for example, can work can
work on the same same base.
Uh,
we can consider, uh, sift views even as
a special case of an index. We will be
talking about it as well. It's not, uh,
exactly an index, but
we'll talk about it a little bit as
well. And that can can facilitate reads
and aggregations very much.
Sorting or whatever we need to read the
data in any order in any sorting any
ordering other than the default uh
primary key.
Again, indexes can help here.
Okay. And then
just to get again everybody on the same
page, we have the we have two words
we're we're we're juggling with, which
is keys and indexes. And both mean
something and maybe something different
in SQL Server versus Business Central.
So, in SQL Server, a key is not an
index, but an enforcement constraint
basically. So, we can have a unique key,
for example, which will enforce that a
certain column stays unique in SQL
Server. Um and an index is the
tree structure we showed before, which
improves performance of data retrieval.
Now, in Business Central, a key is
basically an index definition. If we
mark it unique, it's also a key. So,
there the confusion starts maybe. And
then the primary key in Business Central
is both. It's a primary key constraint
and a clustered index by default. So,
just so we
have that on one slide at least.
All right.
And a little more about keys and
indexes.
Uh as was just said, that one special
case of a Business Central key is the
primary key key because special uh in
it's I mean in the sense that uh
every primary key in Business Central is
a key and an index at the same time.
There are more like these.
Uh
first of them is
of these kind of keys is system ID,
which is an alternative identifier of
our table row. All right. So, it is also
a key in the sense of SQL Server unique
uh constraint.
And it's also an index. So, by default
in every table in Business Central, we
always have
two keys on SQL Server side, which is
primary key and uh
system ID with uh indexes built on on
these keys.
Uh beside these two, we can always
create any other key
uh just by setting the unique property
on any Business Central key.
So,
every other key except primary key and
system ID is always an index.
Except these two, all keys and indexes
are the same time.
And if we set the unique property on a
Business Central key, we create again
index, which is a key at the same time.
Uh this will help us enforce the
uniqueness, ensuring the uniqueness of
the
uh of the value within this key. Uh
and basically works with an index as
well.
Okay, then two more words we need to
talk about first. Uh we have seeks and
we have scans. Now, the seeks, as the
word uh suggests, is it it's searching
data and it's not scanning everything.
So, seek uses the index structure like a
binary search. It's fast because it can
make use of the index of that tree
structure and jump to the desired data
uh opposed to just reading through
everything and searching it that way.
So, it's it's really using the index.
But it requires selectivity, so we have
to have like a filter rate or something
to even be able um to have a seek on SQL
Server. Now, and scans is the opposite.
That's the
if if no seek is possible, then SQL
Server will do a scan. That can either
be an index scan or a table scan, but it
will read through everything and figure
out what it has to find that way and and
not select what but can through the
index.
Yep.
Oh, well, so far so good. We're talking
about very positive effect of indexes.
They definitely help us
increase the speed of data retrieval or
the finds.
Uh but uh every good thing has its
reverse side, right? Indexes have a flip
side as well.
So,
when we talking about indexes, we need
to consider not only the how much they
improve the speed or increase the speed
of data retrieval, but how they impact
on
uh other aspects of database maintenance
and data updates as well.
And in this sense, indexes can't have
negative impact as well. First of all,
on data updates. Any insert, update, or
delete operation has to update,
respectively, all the related indexes in
on the table. So, that's one thing we
need to think about.
Uh
whenever we have an index, uh we have a
higher uh
probability of locking
issues and session contention.
This problem is to some extent mitigated
in Business Central because in Business
Central every index is always unique.
And so, we don't have a chance to insert
we don't have the possibility that two
concurrent sessions can update the same
value of an index when they insert
different entries, for example, because
index values are always unique. But
still, it's not 100% ruled out, and when
we're talking when we understand when
we're talking about wider understanding
of an index and include CIFT, for
example, in this case, this can be a
major problem when we're talking about
CIFT views.
Indexes can consume storage, which we'll
also
uh talk about and show an example here.
And finally, indexes require
maintenance. Not something we need to
care about
uh when we're
uh
when our Business Central instance runs
in the cloud as a service in SaaS, but
still uh maintenance jobs consume
resources, can uh create resource
pressure, and slow down concurrent
sessions.
So,
not everything is so perfect.
Will it switch?
Ah.
Yeah, the button.
And then, before we jump now to the main
part, just a short recap on the on the
introduction. Um, indexes, we create
indexes to increase read performance.
We get faster data access, but we have a
trade-off of uh, slower writes,
maintenance, size. So, we we need to
consider
um, when to create that we we need to
decide from from case to case whether we
want to create an index or not. If it
gives us enough benefit to live with the
with the trade-offs. So, that's now the
main part, going through the different
index types and figuring out what
they're good for.
First one, row store indexes. That's we
have columns, so this is row store, and
the clustered index, aka primary key.
It's the first one.
There we go. Mhm.
Uh, so, when talking about clustered
index, it's not that much about uh,
pros and cons, benefit of the clustered
index, if we should use it, or if we
should not use it. We just don't have
any other option except, yes, we have
it. It exists.
Uh, although
in SQL Server, it is possible to have
uh, unordered heap tables without the
clustered index, it's not the case for
Business Central. There is always the
clustered index. So, we're talking here
about the clustered index, just to be on
the same page, uh, we will be referring
to these
concept uh, multiple times throughout
the presentation,
uh, just to introduce what the clustered
index is and when it is used.
Uh, essentially, clustered index
is the same B-tree structure that we
were talking about, uh,
with one important difference from every
other index. Leaf nodes are these uh, of
the clustered index, leaf nodes of this
tree contain the table data itself.
Basically, clustered index is table.
Uh
It defines the physical ordering of the
data in the table. And since the data in
the table on the on the hard drive can
be sorted only in one single way,
uh the clustered index can be only one.
So, in Business Central, there
there is always only one clustered
index. There must be one, and of course
there can be no no more than one. Always
have a clustered index.
Uh clustered index is the one that has
the property clustered set to true
usually.
Although we can it's not mandatory
property, right? We can omit it. And in
this case, if we just don't specify this
property value clustered or even if we
explicitly set set clustered to false in
every key, uh then the default first key
in the list will be the clustered index.
Uh
uh there is some
a little
like
misunderstanding here, I would say. But
sometimes people think that moving the
clustered index to some other key, like
not the first one, by by doing this we
change the primary key, which is not the
case. It's not It's not correct. We can
change the clustered index, but we
cannot change the primary key uh
of table. Meaning that the first key in
the list is always the primary, but the
clustered index doesn't have to be
declared on the primary key. It's just
the default value.
And the clustered index, when is it
used? Well, assuming that we have the
default setup and clustered index
matches the primary key, whenever we
call a function like get
retrieve the value, it will be searching
the database on the clustered index.
Right? When we
apply a range range filter from value to
value, if this range results in
large number of records being retrieved,
uh which constitutes significant portion
of the whole table data, then
uh
the search is likely to be on the
clustered index, too.
So, these are the cases when the
clustered index is used.
Exactly. And now, one one example, I
mean, a pretty basic code, we just get
one item. And then, I hope this is
readable. This is an execution plan for
if somebody didn't see an execution plan
before, which is basically the way of
SQL Server telling us what's happening
under the hood. It's possible to
activate this. I will show later uh how
that works. And what we can see is
basically that uh SQL Server uses
clustered index six,
two of them, to retrieve the data,
because all we do is get that record
from the item table. So, it will uh go
through the main table, and because we
don't have set load fields, and we have
probably some table extension on the
item record, it will also read from that
extension table, and then merge them
together, and uh give us the result. So,
that's the clustered index index seek.
So, it doesn't need to do scan here. It
can use the primary key, because we give
the primary key value, and do a seek,
which is uh not even that bad.
And now, uh still row store indexes, but
now the non-clustered index. So,
everything that's not the clustered
index will be non-clustered indexes,
basically.
And it looks like this.
And now, we're coming to some some more
interesting. Uh
essentially, if uh Stefan just
introduced,
every other key uh every other index in
the table, which is not clustered, is
basically non-clustered, unless we
decide not to maintain the index at all,
not to create an index at all, and set
the maintain SQL index property to
false.
Why would we do that? But, yeah, we can
do. Maybe we want to create a 50
50 without an index. Okay. Uh we can do
it. Uh
What differentiates
uh
the non-clustered index from the
clustered index is then the clustered
index itself is the table data. So, when
we dig down into the leaf nodes of the
clustered index, we find the table data.
While non-clustered indexes will have
pointers to the clustered index,
actually pointing to the data.
I think we'll see that later. In a
picture.
Uh a SQL table SQL Server table can
contain up to 999
uh non-clustered indexes. Business
Central limits us to only 40, but even
this 40 is a large number.
So,
uh we can we can even here we can apply
that uh Michael Swartz rule uh 10% rule.
If we create more than four, five
indexes, maybe it's not strictly no,
but something to think about if we need
these indexes.
Uh
when these are used, uh well, basically
all the examples before that we were
talking about,
uh
non-clustered indexes used when one to
facilitate searches by non-primary key
fields.
Right? When we filter
any table opportunity entry in this
case, just selected randomly,
uh
on the opportunity number, this is
likely to end up
uh in a non-clustered index seek. When
we want to filter data, when we want to
sort, when we want to extract the data
from a table ordered by any field other
than the primary key.
Okay, and then how much faster is it
actually to use an index uh seek instead
of a scan?
And um yeah, the the red one we're
seeing the red line, which is pretty
linear, it goes just up but with the
number of records we have in a table,
that's a scan. So, if we if we need to
search through all of the records in a
table, it will just get lower as like
the more records I have in that table.
The index seek on the other hand, the
bottom line, the blue the blue line, um
this is more of a logarithmic increase,
so it it still increases with the number
of lines I have in the table, but it's
it's not as sharp and not as consistent.
So, it slows down the more records I
have. It still goes up, but not as fast.
And then, um,
obviously, uh, not only the number of
rows in the table play a role, but also
like how many rows actually the the
query returns. Also, the distribution of
values. So, there are many factors
which, uh, brings us to our, I think,
leading word in in the in this session,
it depends a little bit. So, you need to
try. Um, yeah, and
much
storage hardware and probably a bunch of
other factors as well. So, but in
general, if we can make the query use an
index seek instead of a scan, it will be
faster and it will not be as dependent
on those factors as the scan is.
And the more data we have in the table
and the more data we select, the more
difference, uh, we will notice.
Exactly. And then now we we have a chart
of, uh, how inserting is affected by
different types of indexes. So, the
lower bar, the blue one, is basically no
indexes. And now I need to look at the
bigger picture. So, we have just over 20
seconds in that example in the, uh, demo
table we we came up with.
Um, and now if we add five or even 10
indexes, you can see that the times go
up to over 50 seconds. So, we have like
more than double of time, uh, it takes
for inserting the records just by adding
indexes
and not even like having much logic
behind it.
And again, to add another it depends in
this case. Uh, these test results are
reproduced in a single session.
Uh,
the inserts were done in just in one
session and pretty much sequentially.
This, again, very much depends. Like,
take it with a pinch of salt, of course,
this picture. It doesn't mean that,
well, whenever you add an index you
time will be incremented by a certain
amount. Uh, it depends on how these data
is distributed very much. If you are
inserting
values sequentially or randomly
interlacing interlacing order, but we
can think about it as a rule of thumb
take a as a rule of thumb that's say
that with every added index
in a table, the insert or update time
can increase by 10 to 20% sometimes. And
again, then it depends.
Yeah, and slower updates essentially
mean increased probability of update
conflicts and lock timeouts because if
if a session is running longer, it will
take that like it hold will hold that
lock longer and then other sessions have
higher probability of hitting the same
records at the same time, which will
reduce and lock weights.
So.
Okay, so
just now we talked about one
negative effect of having an index, but
on the other hand,
having an index on a field on a table
does not necessarily lead to the
to the improvement or
like faster data retrieval or at least
not in the sense we expect it every
time.
What I want to show here, what I call my
one counterintuitive example, is where
adding an index on a table
does not lead to the expected result.
So here you see
pretty simple query.
It's an aggregating group by query that
selects data from a table which I called
my table with indexes and this table has
fields dimension value and amount. So
basically in this case, I want to group
amount
from this table by
summarize amount by dimension value.
And despite the name of this table, my
table with indexes, actually right now
for this test, this table does not have
any indexes.
Dimension value one is not indexed. I
run the table pardon run the query
uh and get the results.
It takes the query to complete like
around 260 milliseconds. Okay, but I
know that
right now my table is not indexed.
But indexes are good. If I add an index
on the dimension value one, uh it should
should improve my query. It will be
faster, right? Let's see.
I add an index on the table and the
query runs almost 2 seconds.
Why? What's going on here?
I expected it to be faster. Instead, I
see it's many times slower.
Actually, to answer this question,
uh we need to dive a little deeper and
answer another question.
What does faster mean?
Uh
well, you may say, "What a weird
question I'm asking right now. What What
do I What do you mean faster? We just
measured the time, take the time when
the query started, when it ended. That's
the execution time. We compare this time
for multiple queries and one that has
shorter run time is faster."
Well, yes
uh and no.
Because it's This is only one way of
defining faster.
Uh
and this uh in this case, we prioritize
the complete query execution time from
start to end.
Uh we can instruct the query optimizer
that we want to prioritize complete
result over a partial interim results.
But there is another possibility,
another way to do to define faster. And
another option is
prioritize prioritize faster interim
interim partial results.
In this case, uh the query optimizer
selects the execution plan in such a way
that the partial results
uh can be returned immediately, as fast
as possible, so that Business Central or
actually uh
this is pretty much an abstract example.
Any client receiving data from the
database can start processing the data
immediately while SQL Server still
continues running. The query is still
running at this time.
Uh this way it allows to parallelize
like the workload between the client and
the server.
Partial results can be made available
pretty fast, but on the other hand
this can be contradictory to the first
and the overall query execution time may
drop uh or
sorry
on the contrary the time will increase
performance will drop. Uh so query will
be slower actually.
And these two options pretty often
contradict each other and result in very
different execution plans.
So now back to the question
uh
why my query slower
how does Business Central define if
faster?
And in Business Central faster means
exactly the second option. Business
Central is in this sense goes that
second of avenue of prioritizing interim
partial results. So in every query that
is generated from
uh AL code that is sent from Business
Central to the SQL Server
there is this option fast 50 added
which means that we expect the SQL
Server to to return the first top 50
rows as fast as possible while the rest
of the query uh well we don't care that
much about. It can be way slower.
Uh
that's what I was talking about and the
query result will be total query result
will be received later and slower. Uh
and in case of my index on the table
when I added the dimension index on the
dimension one
uh this index allowed the SQL Server to
uh run a seek operation or actually it
was scan really on the
index that I just created and returned
the top 50 rows very quickly.
But overall time
well
is not so efficient not so great
compared to option one.
Uh compared to the non-indexed
query. And this result, by the way, the
result is something that we can
reproduce on
SQL Server 2019 and later
with
uh
parallel
uh
batch mode execution on row store.
Because in this case
uh when I run this process on a
non-clustered non-indexed table
this results in a parallel execution
plan. And the cluster of scan of
scanning of the clustered index in
parallel threads can be much much
faster.
But on the other hand, these blocks,
these interim results, we have to wait
all the time until the query is
completed. So, you see in this pretty
much contradictory example, we see that
we need to understand what it means
for us and for Business Central
architecture and for for SQL Server what
it means to be faster. Sometimes even
adding the index
we can counter an unexpected result.
Maybe from the
point of view of the general
resource consumption of the execution
cost,
the clustered index scan will still be
more expensive in terms of CPU time,
input output.
But if we look at it from the
total query execution time from start to
end, well
it's still way faster.
That means it depends again, right?
It depends again.
Okay.
Continuing, well, we'll continue in the
same area. We're still at row store
indexes. We're still at non-clustered
indexes. But now we talk a little bit of
what covering indexes are and how it
con- connects with included fields
property which we
got not too long ago.
So,
this is the chart I I promised you
before. So, on the right-hand side,
right-hand side, we have
a non-clustered index which contains
just the the index definition, right? No
details, just the nodes, the the index
column we defined to be able to search
for the records we're looking for. Now,
if we have a non-covering index, what it
means that
the query SQL Server has to go through
the non-clustered index, find the
records we're searching for, and then it
will need to do a key lookup
and look into the clustered index, the
actual table, to retrieve the connected
table data with the the additional
columns we need, which are not defined
in the index. Now, as soon as we add
included fields, or if the the the index
fields itself supply the data we need,
then we can eliminate the key lookup
completely
and save a lot of time, actually,
because then the the non-clustered index
has all the data we need to
have our query return it to us
basically. So, it doesn't have to read a
second time into the actual table.
Okay, so speaking about the covering
index
uh
just well, I
if we try to define it, it will be an
index that can provide all the necessary
data for the query from the
non-clustered index itself without the
need for a key lookup for for lookup
into the clustered index. And in its
sense,
uh covering index is not some kind of a
special type of an index, something
abstract. It's always a covering index
for a certain query,
because something that
uh provides all the data for one type of
a query will not work for a different
query, right? Uh so, clustered index is
always Oh, pardon.
Covering index uh
is always a covering index for a
specific query. And in its sense, uh we
can say vice versa, the
query will be covered by a specific
index.
As we will show now in a couple of
examples,
uh when we plan a covering index
uh
can look at to
at our structure of our code and the
resulting query. Those fields that will
be filtering on and will be present in
the where clause of the query should be
index present in the B-tree structure,
while everything else basically all the
selected fields, everything present in
the select clause
can be added as included fields. And
this why
uh covering indexes are often associated
with included fields because
practically this is what included fields
property is used for, right? When we
want to provide all the necessary all
data necessary for a kind of query,
uh we can add everything into well, all
selected fields
into these included fields.
Exactly. And there are a few things to
note about the difference between find
set and the query object in Business
Central. Now, we need to be careful to
not say query without object if we mean
the object because it get confusing.
Um so, the find set function includes
additional fields in the select clause.
So, first of all, we have obviously
all the fields we define in the set load
fields.
If we don't define set load fields, we
we just have all the fields, but that
would be hard for a covering index.
So, we we define set load fields, we
have the fields we define there.
We have um system fields, the timestamp
basically in I think it's row version in
AL.
Um we have the system ID, the created
by, created on, modified, and so on. We
have uh fields which are filters
supplied on, the primary key.
We have fields that the runtime decides
are necessary. Maybe we had a jit load
and it added a few more fields to to the
select query. Maybe there are even
subscribers with different functions
adding fields to the loaded fields we
defined. So, it might be possible to add
fields at runtime. So, for a find set,
we never really know what fields will be
selected. So, it's virtually almost
impossible to have a guaranteed uh
covering index.
Now, with the query object, it's easier.
We have the columns we define and the
primary key fields. That's it.
Nothing more. So, it's way easier to
define an index with with included
fields to get a covering index for for
query objects than it is for for for
find set.
Same goes obviously for find first and
find and find last, all the other ones.
And a couple of examples here. For
example,
that code snippet,
let's assume I want to select uh
set of like bunch of records from value
entry table.
Uh well, first of all, I want to select
I want to apply filters. Obviously, I
don't want to select the whole table.
So, I set filters on the source type,
source number. And these are the fields
that I want to be indexed, present in
the B-tree structure. So, this is what I
uh
what I define in my key. Uh just picking
a key from the value entry table itself.
Uh but for this specific example, I
don't need basically anything else in
the index itself besides source type and
source number. And then I want I have
the list of fields which I want to
select, which are will be in my select
clause. These are in invoice quantity,
amount, discount amount, whatever. Those
will be the fields that I can keep only
in the leaf nodes of my non-clustered
index. These will be included fields.
Uh
and to illustrate the difference uh
that Stefan was talking about between
find set and query object, uh if I run
this uh
if I run the find set from that code
snippet in the previous slide, you see
on the left-hand side here, yeah, thank
you.
Here on the left-hand side we we see the
key look up exactly because find set
will add
uh certain number of fields
uh which I didn't expect to find there
probably. Well, I did but
they're not covered by this index.
Uh in this sense uh
this index that was supposed to be maybe
could be covering for this query appears
to be not not covering because it's not
sufficient to retrieve all the data.
When I run a query object on the other
hand, uh define the same columns and the
same filters
here on the right-hand side, we see a
pretty much different execution plan.
It's only index seek.
I have a sorting as the most most uh
expensive operation here which can be
again eliminated if I change my query
and uh add order by property sort. And
then the sorting can be removed as well
and be even faster. But even like this
uh
just removing the key look up and
provided data from the covering
non-clustered index, you see
uh we have pretty good performance
improvement already.
Uh in this example, I don't even have
this good covering index. It's kind of
an imperfect index. My data that I want
to select is split between two indexes
actually. So, I select data from item
ledger entry table which I filter on the
item number. And I have two like not not
I but uh these are two keys from the
base application as well.
Two indexes uh with the item number
field
which is indexed and present in the
whole B-tree structure uh
and the data that I want to select,
document type, document number,
location, quantity. Uh
But this data is split between two
indexes actually. So, there is no one
good covering index that can provide all
the data for me. How will Would
Well, not bad, actually.
Uh
same situation, similar.
Uh when I run find set,
uh
the database engine still has to do a
lookup into the into the clustered index
to to to
to retrieve the data. If I replace it
with a query object, well,
of course, now I have two separate index
six because there is no index not single
index that can provide all the data that
I need. And in this case, uh SQL Server
has to do this hash match building a
large hash table uh
to collect to to join all this data, but
still it is more efficient than the key
lookup.
Okay, so that's an illustration of a
covering index and how we can use it
actually uh with
uh query object
versus uh find set.
So far so good.
Covering indexes are really good and can
be really really good performance
booster. But what we need not forget
when we're talking about covering
indexes
uh is the size
uh space it consume.
Uh usually when we build an index,
normal non-clustered index without
include field, we include three two
three four fields, right? It wouldn't be
really huge because uh the more fields
we add to an index, the less efficient
it becomes.
In case of
covering indexes, pretty often we need
to add a large number of fields
to the index as included fields. And
this takes space.
Here, let's say, I have a table that had
like
2.77 GB of clean data without indexing.
Uh
adding just five fields to three indexes
on this table increased the total size
from
three like close to 4 GB uh sorry, from
a little over four 3 GB to almost four.
21% growth. Just five fields in three
indexes. And this can be quite
expensive. We know that
space
like storage space is not really cheap
in SAS in Business Central. So, this is
something we need to take
into account. Covered indexes can be
good really good performance booster,
but it requires some space.
I need to keep an eye on it.
Okay, now let's see an example for for
covering index. Um
Here we have is a very simple query at
the top GL entry. We set GL account
number and posting data as the fields we
want to receive from the database. We do
set range on the account number. Now,
imagine this would be a parameter
whatever not hard coded of course and we
do a find first. Now, the key we want to
use for this or we envision that SQL
Server would be using is the key number
two GL account number posting that,
right? Pretty simple.
We don't even need the included fields
we have here because the the key fields
itself would already be covering.
Now, if we look at the query that
results from
that
piece of AL code from the find first, we
see
we see this. I've tried to format a
little bit so it's readable. And we want
to have GL account number and posting
date and the all the other things which
I highlighted in red are things we don't
really care about. We don't want
timestamp entry number all the system
fields. I don't know where source type
is coming from balance account type. I
don't even know. And we don't
necessarily want to have it ordered by
primary key either because who cares.
Um
So, the thing is in order to fulfill
this statement on SQL Server
in the execution plan, we see clustered
index scan, which is basically reading
the entire table because there is no
nothing that can really uh yeah, serve
this kind of query. Now, if we
look at
the same representation of data
retrieval basically with a query as we
explained before. So, I'll I'll do the
set range on the GL account number, top
number of rows one because of the find
first, open read, and the query
definition says just the two columns I I
care about, and I also set the order by
for the the same fields I have in my
index defined.
Then, the query looks like this.
I just have top one again. I have the GL
account number at the top, posting date,
entry number because primary key will
also be read.
I do have an order by still, but it's
the same as my my key basically, my
index I created. And then, the execution
plan looks like this. I have an index
scan without a sort operation, without
anything, which is
blazing fast. Now, it says 0 seconds
because I don't have much data,
but uh
yeah, this makes full leverage of the
index in in this situation. And
basically, AL-wise, there is virtually
no difference that's happening. Except
for Well, I have another query object,
but in terms of of logic, there is not
not really any difference.
Now,
let's get started on SIFTs.
It's getting more and more interesting.
Now, we're at SIFT.
So, I said already in the beginning that
SIFT is kind of very different different
type of beast in Business Central. Uh
it is not an index as such, right? But
still, we need to talk about it, of
course, because uh in
uh on our minds of AL developers,
uh SIFTs are so closely associated so
tightly bound to index definitions, to
the keys, right? And besides, it's a
very good
like very common very typical way of uh
facilitating aggregations in in in AL.
So, of course, we can't uh let it sleep.
We need to talk about SIFT as well. So,
if it's not an index, then what is it
actually?
SIFT is in fact an indexed view.
See, the word index is still here. So,
we need to talk about it.
Uh
It's It's an indexed view and you
If you don't know what an indexed view
is in SQL Server, you can think about it
as
a kind of a table which is
automatically updated, maintained by the
database engine.
This table
it is actually stored table in the
database. Practically, almost in every
account, it is a table with some
caveats.
Uh quite important which
I'll be talking about too in a minute.
Uh This table contains aggregated data.
All the summaries, all the sums, counts
that will be include will include in the
SIFT definition.
Uh These aggregations are updated
uh
whenever
uh whenever we update any data in the
table where the SIFT is defined, right?
So, if we we have a SIFT defined on a
customer ledger entry table.
When we insert any new record in the
customer ledger entry,
all associated SIFT views will be
updated as well. We don't usually delete
or update any records in entry tables,
right? But if we were to
uh
same way, the database engine SQL Server
itself will will take care about
associated SIFT views. All the data is
always pre-calculated during create,
update, delete operations.
And this way, we're pushing
all the calculations from the read side,
all the aggregations from the read side
into the right side.
Uh
And this makes SIFT so efficient in
reading aggregations because there is no
calculation when data is retrieved and
read. All this calculation is done when
data is actually updated.
On the other hand, the same fact makes
it so bad for updates.
Here we will see in a minute.
Uh and functions like count, calc sums,
or calc fields
uh can take advantage of the sift views.
So, when we have
a
good uh
sift defined on the table, when we want
to calc sums from the same customer
ledger entry, let's say.
Uh the query will be actually directed
to the sift defined on it automatically.
We don't don't don't have to care about
it. We don't have to think about it. It
will be done under the hood behind the
scene. We don't even know what's
happening.
Uh
and just to illustrate what it is, we
can indeed uh or even open SQL Server
Management Studio
and look at the data
in the sift. Can run a query against it.
See that all the data is stored. It
contains all the calculator every for
every combination of vendor and posting
data, it will have
can uh store a combination a sum of the
amounts and even the count.
This way, functions like calc sums or
count can retrieve data directly from
this table.
Yeah. Now, uh how fast is it? So, when
when we run a calc fields with the
filter on one single field on the very
left side, that uh big blue bar here is
the field is indexed. So, it's not even
the no not indexed. If we put that on a
slide, then we don't see those bars
anymore. Uh so, we have an index, and
that's the blue bar here. Now, if we
were to add a covering index with all
the required fields, then we already go
down to the red bar here. And I think
this is in milliseconds, so we are at 50
milliseconds then. And then the sift
keys
even take it one step further and bring
it down to the to the yellow bar here.
So, we we I think it's almost half the
speed half the the duration again of a
covering index.
So, in in reading it really outperforms
everything. Like if we have that fitting
SIFT index, if if we need to do heavy
reads on a table, heavy heavy sum
calculations or counting, the SIFT key
will make that blazing fast.
Now, let's look at the other side.
The
Now now the writing
and updating. Now, this is this is the
chart now inverted.
Um
how long it takes to actually insert
100,000 rows with and without SIFT keys.
So, now the blue bar is actually without
indexes here. It takes about 10 seconds,
11 seconds. Um
The red bar is with
five SIFT views.
So, we already take it to 30 seconds and
then with 10, we almost go to 50
seconds. So, an increase of almost 40
seconds or what is it 400%
by adding 10 SIFT views. So, we really
should be very careful with with adding
those kind of read improvements because
we will see the the the downsides on the
writing. And there you really need to
decide
based on the use case and then again it
depends on your use case. Um
what is happening with the table. If you
really have
frequent writes to that table and want
to increase performance of one read
operation, it might not be worth to
really go for that super blazing fast
SIFT keys and maybe
use a covering index or something to
improve it but not cut so heavily back
on the writing operations.
Yeah. Uh
we see that inserts we see if can be
pretty slow.
But I would argue that
these slow inserts are not even the
worst problem that can happen when you
have multiple shifts. They're actually
it can be just a part of a bigger
problem.
And the bigger problem is the frequency
of these dreaded message.
That your session
was deadlocked with another user or a
similar one there
there is a lock timeout and your session
was interrupted. You know.
The risk of running into this scary
message increases many fold when they
have multiple shifts especially in
environments with multiple concurrent
sessions with multiple updates where
there are many records inserted updated
in parallel sessions.
Why is happening?
I said already that
shift is all almost a table almost a
table. But there are significant
differences.
First of all
the way business the way SQL Server
handles locks
on the one updating shift to is much
more aggressive. So instead of locking
placing a lock row by row when inserting
indexes what what what when updating
indexes you will see granular row locks
that can be escalated yes there is a
risk but in case of shift
SQL Server will be acquiring range
locks.
Which have
Oh oh.
Like result in this case resulting in
much higher risk of
conflicting locks from multiple multiple
sessions. Add this to the fact that
locks will be held longer because just
because of
slow
the duration of the update itself
duration of the insert it it will be
much slower more aggressive locking and
we have a recipe for disaster.
Just to give you some context I have a
couple of examples here
of these kind of disasters.
Uh case one
a user a user
customer running 50 sessions
uh 50 concurrent sessions posting
around 10,000 transactions a day.
These transactions are more or less
evenly distributed during
throughout the day. It's not of course
completely equal. There are some spikes
like rush hours, quieter hours, but by
and large we can say more or less even.
And there are let's say 10 to 20
deadlocks per day happening sometimes.
And there is another case.
190 sessions running concurrently. And
what's making it worse
uh
these transactions are not posted like
equally throughout the day. The total
number of transactions is around 16,000
which is not
hugely different from the first case.
Like same order of magnitude. But what's
worse in this case and it
these transactions
can be posted in short spikes. Like
during the day it's
completely quiet, nothing is posted and
then literally
thousands of transactions posted within
minutes.
And in this case of highly concurrent
environment, see there can be hundreds
of deadlocks.
And all of these deadlocks happening
like on two tables
which are touched in every transaction.
Every transaction inserts
uh certain rows so so
some records in these tables. One of
these tables have
six fifth views and the other one five
five fifth views
five fifth 50 views.
All of the deadlocks happening on fifth
views on these tables.
Deleting these fifth views resolves the
problem. Completely zero deadlocks after
this.
I'm not saying that
in this case I didn't delete all of
these
to achieve this result. There was still
one fifth view left on every table the
most important, the most crucial
for reads.
And having even one sift view instead of
five and six on each table
resolved the situation.
I don't want to say that
one sift view is a safe haven, like I
can say
uh
define only one sift view on a table and
it's secure. Of course, again,
I don't know what time
we're repeating this for how many times
I'm repeating this, it depends. It
depends, of course, on the intensity or
the number of parallel sessions.
It depends on the data distribution, how
many distinct values in every sift view
you have.
Uh we can easily construct a sift view
uh that will be deadlocking on every
session every time.
But on the other hand, if you have
uh like millions distinct views in a
sift view, prob- probably it will be
safe.
But
e-
for me, like a
rule of thumb, if I need to declare
one, two sift views on a table, still
okay. More than two, probably we need to
stop and think about it.
So, from this perspective, from locking,
sift can be
a source of lots of problem many
problems.
Okay.
Again, example time. Now we have GL
entry.
Um
again, I believe it's almost the same
query, just not a find first, but a calc
sums instead of the amount column. And
as we can see in the resulting SQL
query, now we're not even querying the
uh the table anymore. It it says
something about the table, but then we
have a long guid and we have a a V sift
key two. So, that's because we we're
using the the sift view, the sum index
fields from the defined key number two,
uh instead of reading from the actual
table.
And then we can see in the in the
execution plan, again, it there is
something about cluster clustered index
seek, but
we have a view clustered append. So,
that's the indicator that we're we're
reading from the from the SIV view, but
as as the name suggests, it's an index
view, so there is a clustered index on
the view, and we are using that one to
read.
Just so you know what you're looking at
if you see those kind of execution
plans. And then also if we check the key
definition in SQL Server Management
Studio for that key two on the SIV view,
we can see that the primary key columns
for that clustered index are GL account
number and posting date just as defined.
So, it's everything's there. We can
everything check and look up, and that's
how the the runtime when you do calcs
sums at like any query which is
fitting for for SIV index will
automatically redirect and read from
that structure from the SQL Server
instead of referring to the main table.
Now, non-clustered index column store
non-clustered column store index NCCI.
That's I think one of the newer kids in
the round.
Let's see what that is about. And there
is a quote
we grabbed from the documentation. So, I
don't know who wrote it. It's just
Microsoft. And Microsoft saying that the
non-clustered column store indexes is
envisioned to be the successor of the
sum index field technology.
Which means more or less we don't need
SIV anymore because we have the NCCI
stuff.
And uh
in in this part we will have a look at
if that's true or not.
Yeah.
Uh
And here probably before starting to
talk about the impact of column store
indexes how they can be used, we need to
to explain probably what it is because
it's not so common
uh not so well known.
Uh
in the introduction part
I already said that not every index is
made equal. Uh, they are designed on
different bases on different data
structures and for different workloads.
And column store index is exactly that
kind of kind of index which is not based
on our customary usual
tree structure.
Actually,
a column store index
I mean, the the name suggests that we
were talking all the time about row
store indexes. Now we're talking about
column store indexes, right? So it's
fundamentally different.
Fundamentally different and
fundamentally what what is actually
fundamentally different that there is no
structure that supports
uh, fast six
seek operations inside this index.
Uh, and what makes it column store is
because every column that is added to
this index is
uh, stored and accessed by the database
engine separately and independently.
You can think like I tried to illustrate
this with this
uh,
series of bricks.
Uh, it's called what column store index
is. So what when we add the set of
columns to the index, every column will
be indexed or compressed and stored
separately. Uh,
that's one dimension of this index,
column.
On the other hand, it has the second
dimension which is row group.
Row group can be
Row group is actually the set of values
from this specific column added to the
index. And each row group contains up to
1 million or actually uh, it's
or 2 to the 20th power, I believe. Uh,
that number is slightly over a million
values.
So whenever we define this
column store index, we keep adding
adding adding values to the table up to
1 million 48,000
576.
These values added keep uh uh
keep adding in the row group. Once we
reach this number, row group is
completed, sealed, done. It's stored.
And the database engine continues with
the next row group. So, in this case, uh
The next brick. Like in the in the
in the in the next brick called index.
So, in this way,
uh we end up with this kind of segment
structure. It is each kind of what I'm
calling brick here is is called
officially a segment. A segment of an
index of a column store index is can
consist of two dimensions, a column and
a row group of 1 million rows.
Uh not rows, actually values from this
column.
Uh what makes it
more efficient compared to the classic
uh indexes is uh high degree of
compression.
Like now we're moving to the next uh
slide of pros and cons of it. Uh the
high degree of compression,
independently stored values of each
column. So, whenever
uh we query some values uh from a table,
we always have uh limit uh we query it
to certain number of of columns. And
every column that is requested uh
uh by the query will be extracted and
read independently, and nothing else
will be added. Those queries Oh, sorry.
Those columns that are not included in
the query will not even be read and
touched because every column is stored
separately.
Uh
database engine SQL Server employs uh
advanced segment elimination techniques
that allow us to allow the database
engine actually to limit the number of
the segments which will be read uh
during
uh the query execution. And this also
can improve performance uh by limiting
the the amount of data that will be
read. Uh I already mentioned the high
degree of compression of this index, and
this also results in
of course
less data stored on the hard drive and
fewer input output operations, fewer
disk reads. So, that's also
So, if I may rephrase with my own words,
if you if you imagine you have this
column chunked into blocks of a million
records, first of all, you need to have
many records to be able to have multiple
chunks, but then SQL Server with magic
is able to eliminate some of them. So,
now with that index in place, SQL Server
does not have to read through all 10
million rows, but maybe just four or
five depending on how efficiently it's
it's working.
rows, for million rows.
Million rows, sorry. Sorry. Four four
five 10 million rows. So,
yeah. So, it can eliminate some of the
those blocks and then read a little bit
faster because it doesn't have to read
all of them all the values from that
column.
And why I emphasize this not for rows,
but for million rows, is because now
we're slowly coming to the cons,
like downsides of the column store
index.
It doesn't Already I was talking about
this that it doesn't support seek seek
operations inside the index. Every time
we query something from a column store
index, it has to do at least one segment
scan. Meaning it reads these million
values from a segment,
the whole segment must be decompressed,
and these million records will be
analyzed
to to find the
record we're searching for inside this 1
million.
The value.
The value we're searching for,
values.
So, because of this,
column store index is not really
suitable for small
queries
that extract specific small subset of
data pinpointing certain record certain
value because
as a minimum Well, we're talking about
large tables here, right? So, as a
minimum it will have to scan at least 1
million values in a column.
Uh
So,
as I said, in a minute of column
segment elimination technique can make
it
uh much more efficient, like compared to
scanning the whole table, of course.
But, on the other hand, there is
a downside, like probably it's a
So far, it's a bit of problem on the
business central side.
Uh uh
Columnstore indexes are not ordered.
In SQL Server, this problem is fixed in
the latest versions in SQL 22
uh and 24 onwards.
Uh
columnstore indexes can be ordered, but
so far, it's not supported in Business
Central, and this means that
our data
data that we store in the columnstore
index
is not sorted, and whenever we insert
the data, with time, our values our
records in the columnstore index will be
spread through all throughout all
segments, and segment elimination, this
magical technique that SQL Server
employs, uh becomes less and less
efficient with time. So, when we have
all the data spread throughout every
segment,
uh elimination cannot happen, and
actually,
query executed against the column uh
columnstore index will have to read the
whole table anyway. So,
uh maybe there is still a
So, there's some some development to do.
There are like two scenarios where the
columnstore index is really bring a
benefit if you have lots and lots of
rows, like many million rows, or lots
and lots of columns, and you have a few
columns index, right? So, it doesn't
have to read the entire like if you if
you have a normal normal select
statement, and it reads the entire
table, or it scans the entire table. In
comparison to that, the columnstore
index will just scan that one column
instead. So, if you have many columns
and many rows, then it really comes in
handy, or can come, depends, right?
So, on the positive side of column store
index, its impact on like uh again,
we're returning to our uh all the
charts.
On a third side, it its impact is not as
dramatic as when we have row store
indexes or let alone shifts.
Like
back to our benchmark we're inserting
100,000 records and adding five or 10
fields to a column store index
increases by respectively
7 8% each time. But
the reason overhead, yes of course for
index maintenance, but it's not as big
as in case of row store indexes.
And
when we can use and when we should not
use this index. Let me start from
the note part the negative part first.
When it's not
applicable not suitable.
First of all, if we want to find
specific data pinpoint like small subset
of data
of table rows.
Very likely it will not be used at all,
just ignored.
It is good for aggregations for large
aggregating query, but again it's not
the kind of aggregation query when we
run calc sums let's say in loop every
time extracting small subset if you just
a few records. It will be just grossly
inefficient in this case.
A covering index like have a comment
here a covering index will be much
better option in this case.
This code snippet that I'm showing here
is exactly
an example
of when
a column store index is likely to be
very very inefficient. So I have my
table same table with index with my
benchmark table
and the list of dimensions. I just loop
on list of dimensions and run calc sums
in in a loop.
The table itself has 1 million rows and
every call of calc sums summarizes
around 1% of all the values in this
table. So every every time count summary
is called in this example,
around 1% of all table data is
retrieved and summarized.
So, we see
uh
this is timing.
How long it takes to calculate this way
to run this query
first without any indexes at all
and with with column store index. You
see, it's just marginally better than
having no indexes at all.
Here in case you don't see here here
that that that these are the other times
and we are in milliseconds, so this is
18 seconds.
And here we are at the Cif key, I
believe.
Yes,
see in in this case when when we run
multiple queries every time extracting
small small piece of data from a table,
well don't even look in this in this
direction. Uh but we can continue
building up on this example and
I continue developing. So, here I'm
running this example on I think it was
on my uh
Docker container with SQL Server Express
which doesn't support parallel plans.
Anyway, this was single threaded
execution. Definitely no
multi-threaded, no parallel plans.
When I run it on a developer edition
uh with max degree of parallelism set
set to six.
Heh.
Well, it becomes
even more interesting because now uh the
execution with column store index is
much worse
than not having any indexes at all.
Actually, again, it it when we look at
the total execu-
total query cost from from the point of
view of input output and CPU consumption
CPU time.
Uh this may be more expensive compared
to the column store index, but the
execution time from start to end will be
will be slower is likely to be slower.
Uh
What happens and why? Just because
uh
the uh the query optimizer considers uh
the
class
clustered index scan to be expensive
enough to trigger the parallel execution
plan.
While uh columnstore index is a little
bit cheaper, it's not so aggressive, not
so expensive, and it doesn't exceed the
parallel threshold for parallelism. It
still runs in a single thread.
Uh I can play along a little bit
more
and set the threshold for parallelism to
one, as low as one.
Sure, not something we want to do in
production.
And if we're running in in SAS, not
something we even can do, right? But
just for the sake of a demo, I can do
like this. I set the threshold for
parallelism to one, and now the picture
changes dramatically, because now my
rowstore index read is much more is much
faster.
It's much faster than reading the
uh clustered index uh without
non-clustered indexes, and it's even
better than having the rowstore index,
which is close to a covering index.
Uh because in this case,
uh when
uh it's it is an illustration of the
fact that uh columnstore indexes are
designed for parallel processing. So, in
this case, uh the optimizer decides that
again, now in this situation,
the query cost exceeds the threshold for
parallelism, and we can run the parallel
plan.
And when it is processed in parallel
threads, it's rather efficient. So, we
can't use it in production, as I said,
not something we can we can do, uh drop
the the
threshold for parallelism so low, but we
can draw some some conclusions from this
fact.
Actually, when
columnstore indexes can be efficient,
can be used. First of all, we're talking
about large tables, talking about the
millions of rows, first of all.
Uh the query itself must be expensive
enough
uh, to trigger parallel execution.
Uh,
and
the query should return like is expected
to return. It's not something run in in
a loop. We prefer query that will return
multiple values in a single run. Group
by typically typical group by query. And
this is what we see here. This kind of
query we define a query object uh, which
run a group by SQL query. It's likely to
to satisfy these requirements.
So, as long as we have these
requirements
like uh, matched
running a large table, expensive query,
group by, it runs uh, retrieves all
necessary data in a single column store
index scan, it will be really efficient.
It will be this efficient actually.
Uh, here we have row store index and the
column store index
is
much better, almost like more than three
times faster.
And it will even close to sift, still
not reaching the sift performance, but
on the other hand, if we
balance uh, everything uh, positive
effects on uh,
on the data aggregation and much much
lower impact on the inserts,
probably it looks like a good option.
Okay.
The last one and then then we get to
some examples. Um, and there's a really
short one. It made it into the slide
this morning because we we we realized
we we we missed one.
We have now the full text index, which
is basically the optimized for text
search property. This will also create
an index on SQL Server, which is called
full text index, and it's there for um,
for making natural language search or
keyword searches effi- more efficient.
And um, you can do some sort of wildcard
filtering for entire words.
And it will um,
it will increase those kind of filtering
wildcard filterings, and it's not so
heavy on on update operations either.
So, it's it's a very good option, but
still it has a performance overhead, so
you don't want to set that on just every
text field you have in your table to
make the nice full-text search in the
list view better because it does have an
overhead. But, yeah, that's all we were
able to fit into the slides, so let's
continue with um
yeah, how to find out whether your your
query is actually using like SQL Server
is actually using an index you created
for your query.
So, there are different
different questions you need to ask.
First of all, it depends on the data
structure you have
whether you have
nicely distributed values in the column
you're filtering on or if you have like
a boolean with basically two options and
90% of them are true and just some are
false or the other way around.
Um whether you have lots and lots of
records in your table or you don't have
that much, just a few few thousand
records maybe. And also the query cost
itself. So, how's the query constructed?
How expensive is it? Does it pay off to
have the key lookup essentially or is it
just too expensive to do the the
matching between index and table, so it
just reads the table instead because
it's faster that way.
Um
and the idea is if you want to repre-
reproduce and test this in your dev
environment, you need to create good
demo data. First of all, enough demo
data, and then also you want to try to
match the data structure as good as
possible as it is in production. So, if
if you have
dimension values in your table, for
example, which are basically distributed
equally of all the values, you want to
do that. If you're heavy on certain
values, you want to simulate that as
well. Try to really simulate the real
data as good as possible or even take
real data
and just multiply or whatever.
Um
then for date fields, are they random or
is it like a posting date chrono-
chronologically
increasing over time? You want to really
uh
simulate that, right?
And then how you can actually check
this. So, first of all, with the
debugger we now have the option to
really look into the SQL statements that
were sent against uh SQL Server and I
think 95% of the time it actually is
what happens. So, you can you should be
able to use that. So, you want to do
breakpoint, of course, on the statement
you're you're you're expecting or you
want to look into.
You need to step over that statement and
as soon as you step over, you can look
at the debugger on the uh on the last
executed statements. And don't ask me
why
SQL statement number nine is the last
one
in in that case. I think you can
configure how many you want, but the
last the late the last one of the
highest number is the latest statement
that got executed. So, you need to grab
that. I just ran that through my uh
through my formatter and then
uh you end up with a query like this.
Um and depending on how much values
you're filtering on, you get those kind
of parameters. So, you just need to
replace this in SQL Server. Strings are
just like in AL with single quotes, so
you can just in insert the values you
were actually filtering on because
that's uh not part of the query you can
actually receive.
So, that way you can you can connect to
uh your SQL Server on in your Docker
container, whatever uh with SQL
Management Studio, Azure Data Studio,
whatever you prefer, and you can
activate the execution plan. There is a
like a predicted execution plan one and
the actual execution plan. And this one
you want to activate. And then once you
uh run the query,
you see the execution plans like you
uh like we showed you before.
Now, this is uh
one other thing you can use to find
missing indexes in the system. SQL
Server has statistics, and statistics
over
executed uh queries, basically.
And it
can recommend to you if uh indexes are
missing to create them. And that view
got exposed to us in the web client. Um
so, we can actually have a look at what
indexes are missing. Unfortunately, we
do not see the impact because SQL Server
also knows the impact of those missing
indexes.
Knows I would be careful with using with
using the word knows.
Predicts.
Yes. Estimates.
It depends. Um
so, you can uh you can get some hints
from that table of what indexes might be
worth adding to your tables.
Um so, you can have a look at those, as
well.
And then,
No, it's it's too small on that screen.
Yeah. That's um
telemetry. So, you can also have a look
at your telemetry events you you're
receiving, whether there are
slow-running SQL statements. So, maybe
from your extensions,
um you see some some queries here, other
queries, uh basically, which are running
slow, which means exceeding 750
milliseconds threshold. And then, you
can look into that. Maybe it's AL code,
maybe you're missing set load fields,
whatever, but maybe it's also missing
index you might want to create to
increase that performance.
Yep. And then, we have some more
examples, I believe. Do we have time for
examples?
Uh well, we can show some examples, or
we can switch to Q&A.
Uh this uh well, we can show these
couple of examples
which which kind of index can be used,
what kind of code we run, Uh
uh uh uh
what execution plan will be generated,
what you what index will be used. Uh the
first one you see
uh
just the the very simple one, the
simplest possible probably. Uh we set a
filter on a detailed customer ledger
entry to filter on the customer
and the entry type.
And we have a suitable key for it for
index entry type, customer number and
entry type. And here uh
yes, uh this is what we expect this
index to be used. And indeed, yeah, it
is used.
Uh
SQL Server runs an index seek on on
exactly this index
to find the data we need.
Uh there is one a little more
complicated, more interesting example.
So, what what here uh I select data from
GL entry
uh
filtered by GL account number and the
posting date.
Uh which kind What kind of index
uh uh
would I want to create to facilitate
this search? There are two actually
possible candidates if we look in the
base up. Which one of these will be
used? One has GL account number and the
posting date, and the other one
two fields in the reverse order, posting
date and GL account, and dimension set
ID as well, including this field.
In this case actually, what what happens
in fact on this data,
the SQL Server query optimizer prefers
this key 10.
Right? Just because
uh key Oh, pardon, key two actually. My
bad, sorry. Uh it prefers key two
because simply because it's smaller.
And it requires fewer uh input output,
fewer disk read operations.
But in fact, why I was so drawn So, my
attention was on key 10 actually because
key 10 could be
more efficient for our searches if it
had only two values posting date and GL
account.
Uh
it's because posting date if we have
data posted throughout long period of
time.
Right? Uh and GL accounts normally,
especially if company is not too big, we
have uh not not too extensive chart of
accounts. Maybe a few dozen
distinct values. While posting date uh
distinct values of the posting date grow
with time. And if the company has been
operating for 10 years, we'll have
hundreds of distinct values in this
field. And in this case
uh this field is less selective and
preferred to be
in in the front of the index and will be
more efficient. Although exactly in this
case, performance difference can can be
marginal.
It depends.
All right. I I'm not I think we'll skip
that example because we want to get to
the general considerations, some some
things
uh just to wrap it up slowly. So, more
is not always better actually, it's
often worse. So, you want to create your
indexes uh
really and test them to be sure that you
really need them because if you create
them just in case, it really can slow
the system, probably will. So, um we
when planning indexes, we should
consider updates as well as reads
because
um if your table sees like if if you
have some statistics around that will be
open on Fridays or just on Mondays or
the end of the month just once or twice,
uh then it might be not as worth it to
create an index to speed that up
compared to the writing and re and and
updating that happens on a daily basis
all day all day long, basically.
So, we would we should use query objects
when developing just to be able to get
the most most out of those indexes to
not create so heavy indexes to somehow
make it a covering index or something Uh
because we can predict the resulting SQL
query in a better way.
Um
and then
some recommendations of what kind of
index preferred in various situations
when we are searching specific records,
aggregations of course, table joins
might also
uh
pre uh
benefit from indexes, but again it
depends you need to test this really.
And um
some there there are some
uh fields which are uh
the no the fields which are filter on
that way should be at the beginning of
the key. Alex just explained that we uh
that it sometimes the more selective
field at the beginning makes more sense
than if it's somewhere in the middle. So
the the the order of the keys is also
important.
Um you might not want to include fields
which are which have the same value like
as I said if you have a boolean which is
uh like 5% cases true and otherwise just
false, it doesn't really make sense to
include that but same goes for text
fields. If they're all just all empty
and there are a few values in there
which are which are filled then the the
index can't really make much out of it.
Um
you can try to combine filters for
several different queries into one key.
That can work but doesn't always work.
You need to test it.
And then
decide as I explained against or for
index usage based on whether you're
writing more than you're reading or the
other way around.
And that's it.
And we have a few minutes left. Thank
you very much for your time.
The first dessert.
And the microphone.
Hey, an open question.
If you don't work on SQL like on premise
at all and you only work on cloud, can
you still
um
plan your index when you don't have an
full access to
all the statistics, uh you know,
long-running queries are not always
the ones that show the bad indexing
problem?
Yes, well
an open question as you said, yes. Uh it
may become more difficult, uh but still
there are tools that you can use. There
are index suggestions, there is
telemetry. Uh locking telemetry,
deadlock telemetry, long-running queries
telemetry. And after all, when any
situation when I need to analyze
something when
difficulties uh even when I collect
after I have collected telemetry data, I
try to simulate the data.
Run I have like scripts that will
generate data similar to what customers
are running on. After all, uh pro
like performance problems do not depend
on some specific data, right? On the
specific customer. Likely it's
uh
the
patterns in data we're looking for and
patterns in data access sessions. I use
VCPT to simulate the workload and it's
and and
like capture its performance problems.
Well, yes, it's more difficult, but we
still can do it.
Uh there was next question?
I have two questions. Uh first
What what t-shirt?
In first controversial example, uh you
said that
when it decreased performance, if we add
another field to index uh will it work
better? So, it covered the index or it
still
can't work parallel?
No, it it's not decreasing performance,
I would say.
Uh it increases the total execution
time, total run time start to end. But,
uh
SQL Server
query optimizer doesn't evaluate
queries, doesn't estimate performance
plan based on pure execution time,
right? It uh
estimates based on the execution cost,
which includes total CPU time,
input-output cost, and many many other
factors. And plus here we have uh
that fast 50 option, which takes
precedence. So, whenever uh
I think adding I don't know the exact
answer, I didn't test, but I I think
adding another field would not help
simply because
uh
Okay, it depends. It depends. But, uh
just trying to replay this uh scenario
in my in my mind, I'm thinking that uh
it won't have that
big big impact because
uh here preferred execution plan would
be still scan the non-clustered index
and read top 50 rows as fast as
possible. And that's the premise of this
longer execution time. The back uh
because we still need to run on the
non-clustered index and then do the key
lookup. And it can cannot be
parallelized. That is the issue.
Uh the the like the shorter execution
time for the clustered index scan is
because exactly because that execution
plan can be parallelized. It contradicts
the fast 50 option, cannot be satisfied
cannot satisfy the fast 50 option, but
it can run parallel parallel threads.
That cannot be done for non-clustered
index. I guess
Like so far I'm guessing, but I think
no, it would
But, in this case it
will not access primary key at all.
Primary index it just go by this covered
index.
No, it will it will it will be index
seek and key lookup, yes.
Okay.
And second question, this NCCI
index, how to specify it in BC? Is it
new property or
Well, it's not so it's not so new, but
yes, it's table property.
It's a property on the table level where
you just define the columns you want to
be covered want to have covered.
Okay, it's something new or we can
already use it.
It's you can already use it. It's yeah.
It's been there for for quite some time.
Yeah,
use it.
Okay, thank you.
Up there.
I'm not sure if we need to take the
questions to the front because
Ladies first.
Sure.
Yeah.
What would be your general
recommendation for buffer table that
um
generally has a lot of rights per day
like let's say 1,000 clients, but at the
same time based on specific criteria
being updated by users in the business
central
and being like because it's a buffer
being copied to another table.
But buffer table you don't mean
temporary table.
It's actually stored.
Yes, on the physical server.
Uh the recommendation well, I believe
the recommendation because these tables
should be
I would say optimized for
faster rights. We don't expect to read
or aggregate any data from this table.
So
I mean the users will be reading the
data and updating certain things. So
they will be
like yeah. So they will be read by the
users the end users.
Okay, well,
sorry sorry what what I I'm going to say
sorry for what I'm going to say, but I
want to say it depends.
What do you what depends probably what
users want to read. If it's a buffer
table
like many records inserted in this
during the day and maybe in heavy heavy
right load, I would try to minimize the
indexes at all. And then I would look
what kind of
read operations what users look for in
this table. Is it some kind of specific
rows they want to update? I I believe
you you mean they want to update
something manually, right?
Yeah.
Well, then it's up it can be optimized
Well, maybe
Well,
depends on how they search again.
Filters
uh
We don't want to add index or to
facilitate all kinds of filters, right?
On every table because this will slow
down all our updates.
But maybe some most important like
Okay.
Uh they don't want to access uh record
records inserted months ago, right?
Probably index on the date first of all.
They look for to to be able to filter by
the date. But try to minimize uh
overall number of indexes here.
Okay.
I have one last t-shirt.
It may be there.
Yeah.
Someone in the back?
Uh index performance is a lot of
dependent on the fragmentation of index
and is there any
um
future plans of Microsoft of
letting us
know more insights about fragmentation
and
uh
the possibilities to
actually do do some maintenance on it.
I I think I know the the answer to that
one. Uh
no.
Uh and and the longer answer is uh
Microsoft's taking care of the platform
and we should not worry about um
the the the underlying structure too
much. It they have the routines and
everything that figure out when a
rebuild is necessary or maintenance job
and they will execute that on
as it's needed. So, the the plan is not
there to to dedicate this to us
in any way.
Too bad.
Sorry.
Okay.
We're out of t-shirts, but okay. So,
yeah, we're done with this.
Thank you very much.
