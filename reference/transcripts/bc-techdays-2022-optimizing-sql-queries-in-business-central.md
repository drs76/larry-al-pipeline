# BC TechDays 2022 - Optimizing SQL queries in Business Central

- **Source:** https://www.youtube.com/watch?v=XCmNHbZoCMU
- **Video ID:** XCmNHbZoCMU
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 78m52s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

foreign
[Music]
foreign
[Music]
foreign
[Music]
foreign
[Music]
welcome back for the second session of
the day in room 9 optimizing SQL
inquiries in business Central uh given
you by Milan Mr Vic
um give please give him a welcome
[Music]
thanks everyone
um it's great pleasure to hold call the
talk in conference like this first of
all I would like to thank the organizers
for this wonderful opportunity and today
topic would be optimizing SQL queries in
business Central
my name is
I'm BC developer from Croatia I'm
currently mainly working with Danish
company culinary partner I mean business
Central and navigation world uh four
years from now and I'm sure that I still
have a lot of to learn but I hope today
you will learn something from me
today I will be talking about in excess
I will cover what is the index why we
need it type of index
after that I will cover something about
clustering non-cluster indexes we'll
demonstrate how we can quickly calculate
sums and talk about considerations that
we need to take when using indexes and
we will take some new features in
business Central and yeah much more
let's start
uh I shouldn't that many of you know
that index is a quick lookup table for
finding records users need to search
frequently
SQL indexes are primarily a Performance
Tool so they really apply if a database
get gets large and indexing a table or
view is without adapt one of the best
ways to improve performance of queries
and applications
uh let's see what Microsoft says about
indexes and index
is an on this structure associated with
the table or view that speeds retrieval
of rows from the table or view an index
contains key build blah blah blah yeah
SQL yeah SQL Server supports several
type of indexes but one of the most
common types are cluster indexes these
are the index which is automatically
created with a primary key
SQL indexes are fast partially because
they don't have to carry the data for
each row in the table just the data that
we're looking for
this makes it easy for operating system
to Cache a lot of indices into memory
for faster access and for the file
system to read a huge number of Records
simultaneously rather than reading it
from disk
let's find a bit more about cluster
index
like said this is index which Define the
physical order in which table records
are stored in database since there can
only be one way in which records are
physically stored there cannot be only
one cluster index per table
by default cluster index is created on a
primary key column of course we can
create a table where primary key will
not be clustered
the following image illustrates
a logical structure of cluster index
this
sorted data structure is called a b tree
or balanced tree
B3 structure enables us to find the
queried rows faster using the key values
we have at three levels like you can see
the first domain is the root level
everything starts from it
and after that we have intermediate
level this level provides just a
connection between root and leaf levels
so SQL Server does not need to create an
the immediate level when we don't have a
much
amount of rows or data in our table
so we see that the lowest level is the
leaf level where
um cluster index
all of the data are stored in that level
meaning that
when we want to search for example for
Value number five or record number five
in the database when we're using the
cluster index we will just start from
the root level then we'll go to Left to
1 to 11 then to one to six and you see
we don't need to scan the whole table we
will just go from up to down and because
of that this cluster index is very very
efficient
other index type is known cluster index
yeah this non-cluster index is similar
to the index of a book
because index of a book consists of a
chapter name and page number so if you
want to go to some specific page number
of the book you don't need to go to
through all of the pages you just need
to look at the index and go to that
specific page so meaning they on
non-cluttered indexes data is stored on
one place and index is stored on another
place
so meaning because this data is stored
separately we can have multiple
non-cluster index in a table
uh
yeah I'll maybe just connect to
equal service to just show you
so
I'm sure many of you know about
SQL Server management Studio
and I'll just
take a look at
the tables
let's do it this way
sorry about that
okay I created some tables but we'll get
to that later I just wanted to
oh okay
but my apartment is closed I can
I think
something is wrong
foreign
not looking and let's see what is on my
screen
foreign
no
I want to
at the moment
sorry about that uh
I want to just to look at some table and
to see what type of keys we have there
for example on
again
perfect finally
thank you
the
so if if you look at the the demo table
that I created we can see that we have
a few keys
key is actually okay let's just
yeah I will just
do the slides maybe it's easier that way
just to be clear about terminology so in
field which has a unique value is
essentially a key however a key is used
to Unique uniquely identify a row in a
table while an index is used to sort a
group the rows in the table so key
should not be changed even if you can it
once has been initially set yes it might
be a reference to some somewhere else in
our database and index field however can
change fairly so
uh on business Central level on each
table uh secondary unique key was
created on system ID field automatically
that way we are sure that when we insert
system ID field we cannot change the
change it never but primarily we can
rename the tables
okay table on the keys are table Keys
defining indexing business Etc it is
under a key section on a table or table
extension so meaning key in business
Central is indexing SQL Server first in
section is primary key and it is
clustered by default of course we can
put parameter cluster to before so then
we would not have primary key to be
cluster we can add cluster to some other
field as well
um also about that system ID field that
I mentioned earlier it is not visible in
business Central Al so it's defined it's
created automatically on SQL server but
you don't see it here on the on that
screen
I'm sure that all of you knows that it's
possible to create a key on standard
tables as well the main trick here is
that we cannot combine standard Fields
with our customers uh
so yeah we will just be should be aware
of that
but before
we look at indexes in business Central
we should clear things
about Set current key it is used to sort
by specified Fields it will not select
which index to use it here it can help
with choosing the index because of the
Sorting but at the end of SQL Server
Matrix a different key based on
statistical distribution of our values
values in the field
um we can use
before we look at yeah so we can use any
of the filters parameters to sort by
even those fields aren't
aren't defined in the key section so
earlier in earlier version if we add a
field in Set current key which isn't
defined in
key section it will throw runtime error
but now we can add in any key whatever
we want from the table to to sort by
is the
one of the methods which system used to
improve performance and respond to
request rapidly
in a business Central system caching is
done on two levels we have business
Central several instance data cache and
we have SQL Server data cache so
whenever a user request a data from
business Central it first checks whether
data is available in the server instance
cache if not then it checks the SQL
Server data cache
and if not
there then go to the it goes to the
database to get the data we have two
types of cash stored in business tensor
server there are globalization private
cache so global cash is basically one
which is accessible to all the users
connected to the SQL Server
private cache is only accessible over a
transaction meaning
for a particular user for a particular
company this cache is cleared as soon as
the transaction is completed which cash
is to be used for which user depends on
whether the table from which the user is
requesting data is locked or not in case
it is locked private cache is queried
else Global here and we have select
latest version method make sure that the
data displayed is the most current data
in the data database also on SQL Server
K on SQL Server level we have two
commands drop clean buffers cache which
will clean the cache and we have three
process which will clean the store
procedures yes
I'm sure that
we all using our partial records because
this is a such a great functionality
that help us loading just a subset of
normal Fields when accessing a SQL based
data source
using partial records improves
performance of objects like reports and
data pairs but it's part of particularly
beneficial when table extensions are
used in the application
accessing the data source from mail code
is typically done using records methods
like get find next and so on without
using partial records the runtime will
load all normal fields from the data
source
foreign
we have
four methods available for
partial records this is a certain law
field that will help us to
initially set the fields that we want to
load and then after that for example if
we are in some subscriber and we need to
do some new fields from it we can just
use it load Fields method which will
just basically add new fields to already
existing ones that are set at in support
fields we have our fixed loaded and load
Fields method also there was one
particular problem with partial records
it was uh it would require all fields
that are used as filters in calc
formulas or flow fields to be always
loaded meaning even if we have in our
table extension sum
flow fields and even if you don't want
any of those fields partial records
still will do will be doing a drawing
and because of that we lose a lot of
performance benefits that we could gain
but fortunately this is sold in version
21 so the partial records would be even
better have it sold its two-part
solution like I
okay sorry
a two-part solution
it is
for calc field the direct solution is to
just in time load the fields needed for
filtering and flow fields for smart SQL
the fields will be selected for all the
filtering and flow field of flow fields
are selected for automatic
uh
partially we have a few benefits of
partial records I already mentioned some
of them but because the fewer columns in
select Parts there is a better chance of
the SQL Optimizer to pick an index also
less memory allocated by SQL Server will
be to execute the query
because of the smaller data set we have
faster data and transfer between NST and
SQL server and because of that
potentially
less IO and SQL Server to fetch non-cash
data because we are getting rid of
joints and less memory will be allocated
and one of the benefit is better
utilization of execution plan cash in
SQL Server
uh
I will just
switch to my code if I will be
successful in that we'll see
yeah okay
so just
I'll I'll not be measuring performance
because we all know flow partial
protocols will help us to gain better
performance I just want to
show what is the difference in the SQL
level in the query
if we have query
we find set with partial records where
we want only to load amount and start
date for example in our data set we just
wanted to do something with it and the
other situation is when we will not use
partial records and when we go
Edition we will see that this is the
first SQL statement where we only have
these few fields we have timestamp we
have primary key we have this
no sorry this is the first one without
partial records meaning we have we have
a drawing on our extension as well and
all the fields from the table but if I
go to now to the partial records we only
see
the fields that we exist for their start
date amount and primary key and system
fields
[Music]
when we are using partial records we
need to be extra careful to not trigger
just in time loading and this is
basically when we try to access unloaded
field platform will detect that access
field is not loaded then it will issue a
gate on the record and load the
requested field in the end of the the
and in the end it will update the record
with newly loaded values
error is raised if record has been
changed in the database before fetching
the just in time load so we should be
aware that delete uh rename and insert
operations require to all fields to be
loaded meaning that this operation will
trigger
just in time load if we use partial
records so basically we should mainly
use partial records with find get fine
setting and so on
covering index covering decks or
included column is
a new feature in business Central from
version 20 on SQL Server it is also
called covering index and it is special
because we have possibility to Define
extra field in index V2
values are stored only if notes and in
on index
so biggest benefit of that is it
contains all the field Fields required
by queries so when we are executing the
query we don't need to go extra to the
to this table to get extra data it may
greatly improve performance and the best
results are often achieved
by placing Fields required in filter or
drawing criteria
into index orders for example if we have
a statement like this where we'll
want to select description and
description too from item table where
item is okay and order by Optimal index
for covering index in our case would be
that we have item menu at the first
place is optimal seek then we will have
last modified date
on the second place on the index and in
the S the included fields we will add
description and description two columns
yeah
okay this was syntax how it look in in
business Central so basically if we want
to just include covering indexes we just
need to put those fields into included
Fields parameter or in into key
before yeah covering indexes was
declared we needed to declare all the
fields into into our key he
why not put included columns
do I have any cover in Guinness in the
first place if the included columns are
not
needed for other types of searches
keeping them out of the key list makes
for shorter entries and here the results
is less
index i o operations included columns
also can be data types that cannot be
index columns and currently we cannot
have more than 60 key columns in index
also if we put 60 currency to index I
think that we are doing
something wrong
they are a few use cases for covering
indexes and
first one is query object is great if
you want because we will just increase
the object cells a few fields that we
want we will add
order by closed if you want and then we
have filtering filtering situation so
another use case will be combined with
circload Fields this is actually the
main benefit of partial records in
circular Fields because cellular fields
uh just gets us a few fields that we
want and partial records can we can
declare declare those fields so meaning
meaning we don't need to go exit to the
database to get other other fields
and maybe it's a good thing to do to
revisit all of our
existing keys to check whether our
candidates to to be changed
to be covering
uh in the explosive view that is
basically in the in the index View
after unique cluster index is added to
the view we can add
more non-clustered index to it also it
is possible to create a non-clustered
index on a view providing more
possibilities to enhance the queries
calling in The View
that makes it actually this distorted
data so I don't know does any
who does any one of you knows what are
views exactly in SQL Server
can you maybe raise Kent or so I don't
know okay so okay I will go back
[Music]
index views are basically virtual tables
that are used to retrieve a set of data
of from one or more tables in a SQL
server but it will not actually store
the data it will just help us to our
query looks easier and simpler but for
example if you want to fetch the data
from some view we will just go to the
database and get the data still but
what's happened if we add an index to a
view I mean unique cluster index then
like we said earlier unique cluster
index is used to sort physical data in
the table meaning when we add the index
unique cluster to them you we will get
actually data stored in that index View
also of course it is possible to create
non-cluster indexes on a view providing
more possibility to enhance the queries
calling The View
that makes it actually yeah
okay
um
creating a unique cluster induction
review improves query performance a lot
meaning because we are just here grouped
values on a view and when we want to
fetch it from the data we will just get
it very quickly but the problem here is
when we we try to
one of the main consideration here is to
insert modify and delete can degrade a
lot meaning every insert every delete
every modify that we did in our bazel
table we also need to change in our
index view so even if we have a very
good performances if you're getting the
data we will have poor performances when
we are inserting or modifying a data
we can benefit from index 2 if the data
is not frequently updated if the
performance degradation of maintaining
the data and changes
is higher than the performance
enhancement of using this index to you
indexed view improve the performance of
queries that use drawings and Creation
in huge amount of data and are executed
very very frequently
[Music]
so why was I I saying that about index U
because some index field Technologies is
basically done on index U when we add a
shift key in our
table in in our key section in business
Central this is basically indexed view
in the in the SQL server and because of
that it is pleasingly fast when we want
to get the sums or some other
application but
but it is
very hard
to insert the data
also it was important to know that each
shift key that we add in business
Central table it is new new index view
in in a SQL Server
I'll just
switch into
come on
are you kidding me
yeah
okay thank you
um
I'll just on the
SQL Server
we have view section
and I will just filter them on if you
ok so we can see that
these two this is the table called demo
and we have shift key 2 and 63 that
means actually that if I look in the
if I Look Into My Demo table
in the key section I have to shift keys
uh one about with amount and one with
amount two so
so if we
select this
maybe I'll just use
okay when we look into that view
we can see that we have
Carino column we have start date we have
count as we have sums
and when we go back to the
to the code we see that in our shift key
we added a car no is in a start date is
a
indexes and it's a some index we added
that we want amount and what we
basically see in the
in a SQL Server that means for each
combination of car and all and start
date we will get some some amount and we
will get count so basically when we do
count operations on our shift index on
table it will be also very fast because
you don't need to go to the base table
to count all the rows or it don't need
to
about to go to the calculate all the
sums it will just need for
to do a few few songs from here and
because of that it is it is basically
fast
maybe maybe I can show some example in
shift
okay what I created is a demo table
which has a few fields and I entered I
filled five million of rows into into
this table
I have ah
card table and I have color tables as
well so when I go to the
business Central and if I go to the demo
demo list this is a page of My Demo
table
we will see all of all of all of that
data uh
what I did actually also
I created a
car total table on which we have
two
a few calc fields
and since on the page we will add a
total amount field so if we go back we
we see car total space that's here card
name field and total Mount field and
total amount is basically the flow field
to the demo table and because of the
shift key if we go to the
cars total
as you see it is blazingly fast I mean
we have 5 million rows and this
calculation is done in in a second
less than a second
also one one of the main problem one of
the main things when using a shift
indexes is that
when we using calc fields
function we should use it we shouldn't
use it in the loop meaning we should use
a
set AutoCAD Fields before find set so
I'll just I made also one
example
as well
what I did I created the two functions
one function is
we will go to each of our cars and we
will just fields of our amount in
in the inside the repeat statement
another example is we will use set auto
calc Fields outside of the fine set and
start
to go to the car
so awesome if the election card feels
compare called
cockfield was 77 milliseconds and set
auto clock fields
zero basically we don't even have we
don't even have any
I'll just try one more time
74 yeah
we see that that
set out the calc field is faster a lot I
mean in in this in this situation
oh
and this is I didn't say that this is
time we have a property on the key which
is maintain safety index it's
um it's true by default so we don't need
to put it
if we don't want to use the
shift index we can put it to false but
what if we put that maintain safety
index to force basically it the indexed
view from the SQL Server will be will be
dropped so it won't we will not have
stick leader so we'll just put it delete
all the all the key as well
uh we could if we put maintain safety
next to false and if we still have I
mean some index we we still can do calc
Fields but the time it will not use
index dual it will go to to the table
and it will be a lot a lot slower
ok ok ah
this
mentioned there are a few considerations
when using shift indexes we need to do
it optimally meaning
key that is defined and enabled for the
table I'm are maintained so when we're
doing inserts and modifiers since shift
indexes are based on index fuel
maintaining these shift index's case
performance overhead of course the size
of performance overhead depends on the
number of keys and some other fields
defined on each table
this is all maintained for only for
large table we don't need to use a shift
keys for uh
for a small tables or tables that are
only used periodically because yeah we
can use
um
alternative for um
for seed field is
included columns because we will still
have a decent I'd say performances and
we will not need to maintain we will not
need to maintain the the index due
because
included columns are just basically
non-clustered index in in the background
all of the indexes that I mentioned
is they are row store meanings all of
the data is
stored
horizontally
but there are column store indexes as
well that
that means that data is basically
store horizontally we can only have one
column store index per table but we can
add multiple fields and order in which
we add Fields is irrelevant so
the reason is that each column that we
add into our column store index is
stored separately and we will see that a
little bit later one of the easiest ways
to think yeah we will just store data
vertically
it is fast or it should be fast summing
column counting the number of rows or
yeah and because of the this is the
because of the advanced compression that
allows more data in memory if proper
filters are applied if also provides a
segment element elimination and later
bit we will see what's that about and
how how we can test it
it reads better off Rose and
Chrome Store data is logically organized
it's a table with row and columns and
physically stored in column wise data we
can meaning if we have five fields in
our column store index that will be
stored like this like a table which
where each column would be present one
field
and the cornstar index groups
rows into manageable units meaning each
of these units is called Arrow group so
we have a lot of raw groups but these
groups are either also some small tables
and each
we should have ideally one million of
Records in each row group to to comb
story next to be
optimized to be perfect but this doesn't
happen always and we also will see that
and we have we call segment each of
these parts of of our
corn star index uh this each row group
contains one column segment for every
column in our table so I mean each
column has one called cement each row
group and the column store index
compressor or group it compresses each
column segment separately and to
uncompress and and
entire column
the column store index only needs to
uncompress one column segment from each
row group if a segment is eliminated
that it means that whole row group is
eliminated
and we have Delta store as well this is
when we created a new
new when we've been setting a new values
into our table into our index they won't
be at the start to the they won't be
saved in the groups they need to be
firstly saved in the
Delta store and when we have enough
enough of the data then it will go to
the raw group to be to be compressed
uh
yeah to return the correct query results
when we using Corner Store indexes uh
clustered index combines results from
both the column store and from the Delta
store
non-clustered whole store indexes uh how
many of you heard about non-clustered
column store indexes
okay how many of you are using Google
Store indexes
no one okay
this is a new technology that Microsoft
induced and it should be um alternative
to Swift indexes
in contrast with saved indexes that rely
on the indexed views this
ncci or non-clustered columns or indexes
in business terms of use only the
non-clustered column store indexes
feature so there is no aggregated data
stored in in the non-clustered computer
indices all analytical queries are done
at runtime so because of that it should
be really fast we have some I have some
examples so we we will see
about it uh
we don't need also to worry about order
of the fields when we're creating
non-classical indexes because every each
of these fields are split separately
stored
with shift Keys any insert update or
delete operations to the underlying
table will introduce some database
logging because index use must be
updated as well the motive Keys like I
said we'll have will have more
maintenance and possible the more
locking problems
and that problem basically doesn't exist
you know in our case in non-clustered
non-clusters column store index
[Music]
also when we should using
current stored indexes we need to have a
very large table and very wide table
what does it mean it means that it needs
to have at least million records but
basically it should have more than 5 or
10 or 50 millions and it would perform
it will perform good very good but
also we need to have a big tables with a
lot of different columns because if we
have a small tables which are I don't
know under a half a million records or
so we want
row groups won't be compressed because
each row group is I said earlier we need
to have one million records to to be
ideally so
it's important to have a lot of raw
groups and to have a great
to good created index so we can
eliminate all of these segments to to to
be fast enough
also we shouldn't add string Fields or
highly unique values to the index best
would be if you have some integer or
date fields that can repeat from time to
time
and if we use non-clustered Contour
indexes on
tables that are updated heavily then it
will cause index fragmentation so we
won't have any benefits of of our index
uh like I said there are a few things to
consider do we still need it at all
meaning if we have a
not so big table we shouldn't use it
also we don't we won't gain a much
benefit if we add all Fields into our
home store index which should choose a
few of them and then filtering and
we we should test before we are
disabling shift and changing changing
into non-classical columns or index I
would just uh
show on the on the SQL server and on the
business Central how it is stored so
I'll just go here
I have a demo demo 2 table this is
basically the same table with the same
values as a demo table where we use it
to calculate the same shift values
I also have the and on demo 2 table I
created column store index where I put
card number amount and start date into
my current stores
I also have a page list page and I will
just run that run that page as well
so if I run my demo list page you see
it's it's pretty it's pretty fast also
because this is 5 million aggregation of
5 million rows and it is it is it's very
fast
again
we don't need to wait
no sir sure sorry
problem if we go to the
course
and here is the problem
we we need to use our non-cluster
Contour index optimally because you see
this is very very slow and
I mean we should have a really big and
reliable to gain such benefit because
and because of that I asked earlier how
many of you are using non-clustered
Contour indexes because
I don't I didn't get a very very good uh
very fast results with it even I have
five million records in a table and
I'll just run some queries some very
easy
so when I was talking about these raw
groups and segments when we look into
this table we will notice that we have 5
compressed
file compressed
row groups into our non-classical index
and we have one open the the first one
the first row is actually our date our
data store where we inserting a new
values and when it becomes big enough it
will just compress and go into one of
them
into one of the row groups
uh
I did some a small test with a shift and
ncci on performing insets and modifiers
so
if I go to the My Demo list
page
and I have a action to insert 1000 row
into this table and if I use it shift
index Limited
okay it is around one one second
but if I use
non-clutter column store index
this is 95 milliseconds meaning this
indexed view maintaining this index view
in our case is 10 times slower than
using uh non-call collector store index
so
yeah like I said if you have really big
tables will benefit a lot from
non-classical indexes because of these
maintained maintain operations
and
oh we can migrate to
two minutes
how we can migrate from shift to
non-cluster column store indexes yeah we
said why and we'll see how basically we
just should
declare column story indexes on our
table we'll put fields that we want to
replace the shift keys and we will just
remove the shift the shift key from the
from the table and yeah that's easy as
well when we
built when we deploy our app it will
take some time to create non-cluster
index and to drop the drop existing
Swift index
data compression
compressing table data saves space and
helps improve performances also these
are two possible data row compression on
SQL on SQL Server we have a row level
compression and we have page level
compression role level compression is
basically inference by converting any
fixed length of data types in our field
into our actual value for example if we
have some text 150 fields
and if you only have a field into it
that is 10 characters long when we use
the row level compression it will just
compress the field to put that to that
value and we also have paid level
compression which basically applies row
level compression and also add to a two
two other types
much more uh
we can add the data compression
parameter in our table
just as part and we have also
unspecified option unspecified option
just means that we will handle our data
compression on on SQL level so we won't
take anything in the business Central
level we'll just Define it on SQL SQL
Server level
um business
Etc online his page compression enabled
by default and
I think in most cases we should use it
as well uh on on-prem environments
there is a
procedural estimate data compression on
SQL I will not show you today but um we
can decide which type of compression to
apply on a table because when we run
that comparison that procedure we can
see what is the actual
size of data what would be if we apply
row compression and what would be if we
apply
page level compression and if there is
no big differences between those two of
levels then we should apply row level
because it's
a simple one but if there is a lot
differences between size of the data
then of course you should use page level
page lower confidence
data based locking controls
x is by multiple users to the same data
at the same time meaning to protect a
transaction against other transactions
modifying the same data the first
transaction put a lock on the data
that means that we should keep our
section as short as possible because you
of each of our translation is longer
than there is a more possibility that
someone will be blocked
[Music]
the transaction is done meaning
as I said table locking is not betting
as such but if we are it's crucial to
guarantee a consistency of data
table locks which leads to blocking
conflicts between two or more users can
be critical because one of these users
will wait until the other will need to
finish their operations and of course
more keys we have more time is needed on
right operations and blocks will be more
often
in Al there is a function called log
table which goes subsequent reading to
lock the table or parts of it uh SQL
Server is one who choosing who will
decide will be lock the whole table or
we will lock the only row meaning on SQL
Server we can lock the raw this is the
low lowest level of granularity of
logging possible and that means that one
or more specific rows will be locked in
the table and all of other data would be
free to use and Page lock will lock just
SQL Server page this is just a part of
the table and
so more lock more rows will be locked
and
the table lock of course will be log the
whole table I'll just make a small also
example
so what I did
on my items page I just
use item log table function and I'll
just get some item and then I have
confirm
and if I go to the
if I go to my items
okay are you sure you wanted to stop the
look this means
if we look in the code
we are now in in the line 21 where we
are waiting for confirm meaning our code
is still still in the
transaction it costs because the lock so
if I go with and login with another user
in business Central
and if I go
to the items as well
okay sorry
I need to change the company first
so if I go to the items
and for example this is the one if we if
you remember we get the item 1000 and if
I
select that item
and for example I want to change
description to write some test
description what would happen if I go
back
system will be
block system will not give us but if I
yes if I okay I stop the Locking now on
my main session and
yeah I wasn't fast enough so
it was already
it it gave me error that the session was
blocked but what what will happen if I
do this if I
look
and one more time and if I go with
yeah
and if I go with this user for example
to
record 1001 and if I decide to change
the description here
then
our description is changed as well
meaning we see that SQL Server use just
row level
blocking on this example there are a few
few things a few possibilities of
of that that can cause locks in business
Central one of these is of course
log table functionality another one is
if you use find set with updates for
other true parameter then it will also
raise a log table parameter and another
possibility is like this if we don't
have log table but if the to use the
users at the same time tries to tries to
block the the same code
uh
and
I think in most scenarios there is the
most reason for locking is just a
Bitcoin or bid so illusion this is not
right right in a good in a good way
uh there's a feature in
um business Central where we can see uh
database logs that was
happen on on our uh environment it is
important to know that if we have
multiple nsds and if locking happened on
different Dynasty then it won't be shown
here ah
also there is a new feature for locking
this is from version 21.
when we use Al debugger when we
debugging our code under database
statistics we can see a log section
where we we see logs that are currently
happening the main reason why we have
this as such a few features that we can
maintain a lock is because it's
difficult to identify which locks are
taken when we are in in online because
we don't have
yeah
access to our database so these features
could help us help us a lot
database based statistics
debate
times are captured and recorded by SQL
server and all these captured
information called waste statistics it
provide us assistance to resolve
problems that are related to the SQL
Server performance
basically what's happening in the SQL
Server you just call this the mosfet
States and it will
give us a lot of information what's
what's happening in the database there
are a few types of AIDS and
we have resource rates that occurs when
a worker requests access to research
that is not available because the
resource is being used by someone other
worker or not yet available examples of
research weights are locks latest
Network and disk IO
wait locks and electric weights are
weights on synchronization objects
we have external weights which occur on
when SQL Server worker is waiting for
some external event um
and specific types of fade times during
credit execution can indicate
bottlenecks or stall points within our
query similarly Highway times or weight
count server white can indicate
bottlenecks or hot spots in interaction
query interactions with server instance
for example lock weights indicate data
contention by queries and and so on we
have a lot of these types that
yeah that we need to check when we have
some of the bottlenecks in our in our
database
the missing index is feature on SQL
Server consists of two components
one of these components is missing
indexes element in SQL XML of execution
plan back in the SQL servers but and
second one is
Dynamic Metal Management view this
procedure missing index details which
can return us information about missing
indexes these are allows us to view all
the missing indexes and recommendations
that SQL Server C with this capability
our platform
will make data about missing indexes
available as virtual table so the data
can be accessed from from L code the
missing index feature suggests only
non-clustered disk based rows or indexes
and there are a few considerations about
it this was a lightweight tool for
finding that significantly might improve
our query performances but
what happens in the background well it's
because I mean the query Optimizer
generates a query plan it analyzes what
the best what the best indexes are for
particular filter condition
is the best indexes that don't exist the
query Optimizer still generates a query
plan using the least costly access
methods available but also stores
information about these in indexes
this feature enables to access yeah so
all of so we can choose what index what
index to use there there are no cost
benefit
analysis
so regarding the size or included or
included columns uh also key columns are
suggested but this procedure doesn't
suggest specify of order of these
columns also included columns are
suggested as well
but SQL Server performs this coins
benefit analysis only of the size of the
resulting index in a large number of
included columns are suggested
it may offer similar variations of index
on the same table and columns across
queries it is important to review index
adjustments and combine
where possible
also these suggestions aren't made for
trivial query plans so you to do all of
this limitation missing index additions
are best treated as one of several of
information that we have when performing
index analysis
uh when we are tuned non-clustered
indexes with music index suggestions we
should review
we should review the table structure in
other words before creating non-cluster
indexes on a table basin in a suggestion
we should review the table clustered
index
missing index may offer
similar variation of non-clustered
indexes on the same table and columns
across queries means yeah music indexes
may also be similar to existing indexes
on a table
for option Optimal Performance it is
best to examine missing indexes in
existing ones to overlap and avoid
creating duplicate indexes
there are also
a few useful links that can help
developers a lot one of these is akims
BC performance and another one is also a
performance developer
tool that
they can help a lot and since we still
have a lot of on-prem environments
on-prem projects going on maybe we I
also put the last link about how to set
up optimally SQL Server from on-prem
which is also helpful helpful a lot uh
yeah I think I finished a little bit
earlier
so if you have any questions here please
ask me
[Applause]
hi are there any advantages as to
splitting very wide tables into two or
more tables
so that's a very wide transactional
tables
okay are there any advantages to
splitting them into two or more less
white tables
so I think here we go maybe
are there any advantages to splitting
very wide table white you know large
number of columns into two or more
tables I think I think
okay
thanks I think not because then when we
want to insert or modify or do some
operations that we will need to do
double on two times
when we want to insert some record you
know then if you want to have
two tables for just one big basic table
you need to keep them
how to say
one-to-one meaning when you inserting
something in one table you should insert
also to another one
I want to know uh should we replace the
shift index with included columns or
should we continue to use shift index
better
uh I say that in most of the
cases we should maybe replace if there
is possibility to include the columns
because then when we will have a right
operations or modify operations it would
take a less time to
modifier insert record on included
Fields then on the shift key and the
read operations I should it shouldn't be
that that different
okay shoot for you
in the future will we have the
possibility to rebuild the indictions
and recreate statistics out of BC code
okay that's maybe a question from
Microsoft I don't know if they will
if
the question was about index maintenance
and statistics maintenance in SAS
and we are actually
um we have planned work to do that in
SAS automatically for you
so you don't have to we we have a
service from a sister service where we
would do it for you
okay
they might give you a shirt or
I don't have any washers maybe since we
have some time I think this non-cluster
column store indexes are should be a
really great feature but I saw yesterday
on all the session and I also tested a
little bit I cannot get a really great
uh early to get uh fast for example when
I'm doing some summing with shift would
be fast but with no cluster it won't
work even if I have five or ten millions
is if it's a I don't know should do we
do are there any secrets that we maybe
should in any other fields or I don't
know because I see that we should add
some integer fields or date fields or
but yeah it still won't work as
specified so do you maybe have some info
so the discussion is about non-clustered
column stores and shifts
I think there's something important
going on right now about
performance discussions that it's not
necessarily only retrieval performance
that you need to consider but also
insert and update and delete performance
so with sifts and especially multiple
shifts you you will get a lot of
maintenance for these
um like non-select operations and it
might be that that is simply too
expensive to have all of these sift
indexes for faster reads because you're
now getting locking and Deadlocks when
you do a lot of rides
and I think that's something that might
be not obvious in the performance
sessions we see people only demo the
read performance and never demo the
right performance so Milan here showed
the first example I have seen where
someone is showing what is the penalty
of having sifts on insert and he said
it's a 10x for one I'm sure you have
more than one swift index so try to take
GL
not in production but try to say TL TL
entry and remove all shift indexes in
ads and and not trusted column store and
add 500 million rows and then start to
see if your posting is smaller like
faster or
or um or slower and and maybe at that
scale this is where in CSI is really
shine and maybe we haven't seen that yet
because these Technologies are new to
the nav and uh NPC Community for for big
large tables
yeah and it's interesting interesting
that no one's still actually tried to
use it and I also but I also look in the
base table uh I didn't see any any usage
of ncci are we planning to do it
well there was a question for me
actually yes we are planning to replace
some of the sift indexes with BCCI or
nccis
there is also a small caveat if you're
running on Azure SQL on a small database
without much capacity I can't remember
if it's two cores or how the actual is
then the non-clustered column store and
this is automatically disabled so you
get absolutely nothing it's just a small
if you're trying this out on a small
Azure SQL database it'll have no effect
because it automatically turns off
because it's a Memory intensive
operation I think the overall guidance
is you should use nccis for tables where
insert modify
Etc that speed is important for read you
cannot beat the index view because we've
stored the calculation already
exactly because I
I use the nccy and I use segment
elimination and I mean I have 10
segments or so and I only read one or
two segments and still I'm uh I'm slow
so yeah I think we will never get the
same effect uh it's a shift but as you
said index and insert and modifiers are
much much faster
the
that's it I guess
[Music]
foreign
