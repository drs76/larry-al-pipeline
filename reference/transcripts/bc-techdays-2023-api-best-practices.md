# BC TechDays 2023 - API best practices

- **Source:** https://www.youtube.com/watch?v=g7BhQf7q-Ko
- **Video ID:** g7BhQf7q-Ko
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 91m34s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

good morning everyone
here we are again BC tegnace 2023
but now in the summer so that's why we
don't have the blouse we do have now the
speaker polo shirt
so if you see those those green guys
there's no Muppets they're just uh
speakers and I don't know we also have
these wristbands I have no idea what
that is for but we find out I guess the
coming days maybe somebody doesn't find
out that we are a speaker based on the
shirts so okay whatever
um welcome
um
my name is Alan Young Kaufman for the
people who don't know me there might be
a few I'm from the Netherlands and in
this uh Nev or BC world for 21 years
um and always on the technical side
working as a freelance technical
consultants and a trainer
um and helping a lot of partners with
well getting ready for the cloud getting
their products ready and also a lot of
API stuff so that always seems to keep
coming to me in the Netherlands we also
have something that's called the this
Dynamics Community I actually retired
last week from uh the committee but uh
well I was a co-finer almost 13 years
ago
um and there's some whereabouts here on
the screen if you have the need to find
me later or send me a message
all right so
um what are we going to do I have a
number of topics today actually a
collection is not really a story like uh
building up something I've collected a
number of best practices and tips and
tricks for you when you deal with apis
and we start off with creating apis but
I'm not going to do the boring thing
like hey this is an API page and you
need to set a page type API and here are
the properties Etc that's a little bit
basic let's go with a tool that I use
quite often and that is the creating
customer apis with the wizard that we
have in the AZ Al Dev tools there's
actually a very nice tool where we can
generate files generate Al file objects
and there is a specific specific
mode in there where you can create API
pages and the nice thing with that is
that you can fill in automatically some
API properties so as you see here on the
screen we have the default API publisher
and default API Group and a default API
version so with these three you don't
have to type them in or it will do that
for you automatically during the
creation
you can also turn off field captions
which I think is very useful because
apis do not need captions
I mean
I know sometimes you will need a caption
in an API but just like normal pages
the captions are on the table fields so
there's absolutely no need to put your
captions on API Fields unless you're
using a global variable same story as
with normal UI pages so why not turn it
off for API pages and only add those
that you really need
and then what I always do I always look
at what is this API going to be used for
is it just a service to service
integration I do not even use API
captions I mean why would I only if the
API is going to be used in a UI page
somewhere like powerapps or a custom web
application then I may add captions so
they can be presented in that UI
including multi-language Etc
also application area not required in
API pages so we turn that off as well
and then finally and that is absolutely
powerful we can convert names
if you have a API that contains the
field number well in most cases it's in
the table called No Dot now the dots
cannot be used in the name in the API
field so you get a field that is called
no
but no is not really a good name for a
field I mean that has a different
meaning so we go with number but this
tool can automatically convert that for
us so I think that is a very useful and
I want to do a quick demo of this
so let me switch to
this one here
and close this one
I'm going to um
bring that in this one and then say
um new Al file wizard
from the AZ aldaf tools you need to
install that of course but I assume you
all have already
then there is not an option here for API
you need to search for adding a page
but then in the page we can switch from
page type cart to page type API
well it's going to be the an object name
so let's just say demo items API
and it's going to be the item table that
I will be using so as you see the API
publisher
and group and version are already filled
in
entity name and entity set name is going
to be something like
demo items and oh that is the entity
name so let's be single and this is
plural
application area will be ignored so
actually it could be removed if there is
Page type API
and then we can select the fields that
we want to have so I go with the number
field and go with the description
fields
and
whatever inventory field and some of the
system
uh Fields I want to have the system ID
included and System modified at
The System modified ad is something you
should always add to your apis that's
the best practice and then it should not
have the name System modified app it
should have the name last modified
daytime
so
um no filters finish it and look at the
results so automatically no is converted
to number
and System modified it is converted to
last modified daytime
and system ID is converted to ID
so that works and that is all due to
again the settings that we have in here
it searches for the expression this is
the name that he will generate based on
the field name and then you say okay if
that is going to be the name for line no
it's going to be sequence it is also a
standard a convention from Microsoft
knows going to be number no with capital
N at the end of something is going to be
number system ID is going to be ID and
System modified at it's going to be that
one
you could add description to change it
into display name for example or name
into display name etc etc
so um I think a very useful thing only
thing is when you add the fields you
need to think about the order the tool
does not allow you to reorder the fields
when you add them in the Wizards so you
better have the order already in mind
and you pick them in the correct order
otherwise you need to do that afterwards
like now I picked a system ID field
later so it was at the end but usually
the system IDs go into the top and you
need to add the odata key fields that is
also at this moment missing
so don't forget about that one all day
that key Fields is going to be system ID
and trust me if I publish this one it
will just work but I'm not going to do
that demo with a lot of other demos here
um so that was the first one
then I would like to dive a little bit
into the page triggers
the API
is a page
so there are a lot of page triggers
there and what I would like to to point
out is that those triggers are not
always cold let's say in the same way or
in as you would expect
so there's a different flow different
set of triggers that execute for a get a
post a patch or a delete I can promise
you there will be really some surprising
uh stuff there triggers that are always
executed for every request is the OWN
init and the on open page well the on in
it we usually use that on a UI page to
initialize controls for example but
in API page we don't do that so I only
write and use the on open page usually
so on open page it is you will see some
code in there when I come later to some
demos and the query close page and on
close page will never be executed so
nobody is requesting to close an API
page there's not a user is doing that so
um any code in there will just be
ignored
when we do a get operation to retrieve a
record that's quite obvious so we have
the on init a trigger
in which you will not be able to see any
filters that have been set on the URL
um so actually not so relevant for API
Pages then we get the unopened page and
in all open page you can read any
filters that you have set in the URL
including filter on a system ID
you can maybe set some extra filters if
you want to on the record and you can
also use that to initialize a temporary
table if your API is based on a
temporary table I will come to that also
later how to deal with that
then we get the on fines record which
could be alternative to fill and
temporary table I see a Microsoft apis
that they prefer to do with any on find
record
I don't know why I mean on open page is
good as well the thing is in on fines
records that might be
executing multiple times on open pages
only one time and then for every record
you'll see the on after get and of how
to get Curl record and on next record
so
um
what's going on with the screen
yeah I I noticed it's flickering but
okay
should be fine
I hope so
good um
so let me go
to postman
and
um just run a
get
working probably should do something
like this
yeah
are you still not seeing it I mean I can
help you in the back
okay so
um
let me then go into this page API look
API and there you will see what is going
on so this was a session we just did
um we saw on init we see it on open page
on find record after get after get
current record and finally on next
record
if there would be more than one record
it would use that and about the filters
if there is any filter let me
use that one as well I'm just gonna say
I want to get one record
and see what happens then
you'll see in on open page that I know
hey the system ID was filtered on that
value
so that's actually what happens when you
do a put a value between the brackets
um it will be a filter on the page in
this case on the system ID other metals
he mapped because of the old data key
Fields so the value in the URL is mapped
on the odata key field value
okay so this is a get and that is
probably
um not so
um
uh well surprising but then we also have
the post operation and the post
operation is a little bit different we
have the after the open page you first
get your own new record which you can
use to initialize a record uh of
initialized some Fields then you get a
validate for every field in the request
body so not for every field in the API
page but only those fields that are
defined in the request body and the
order in which they will be validated is
the order in which the fields appear in
the API page not in the request so you
can use any order in the request with
the API page determines the order
and then finally after uh the unvalidate
of all the fields you get an uninsured
record trigger which you can use to
complete a record maybe with some other
data or you could even call an a code
unit for example that handles the insert
maybe from a temporary table to a real
table
that is all possible there
so
specific situation that is a little bit
strange I will come to the also later
with the post operation I will show you
that a post operation also can turn into
a patch operation automatically
kind of so I do a post but I end with an
unmodified record instead of an online
search record how about that
so um
let me quickly
do that post
so that is the post is creating
um a record
and then
when I look here
I get some new
stuff that is this one here on in it on
open page new record field validate 2 5
7 and 8 and finally only insert so
that's clear I think so far
we get it
now the next thing
which is the patch operation
well there are a lot of triggers
what happens is that you get the usual
thing on open page but then you get your
own find records why is that because a
patch is always on a single record so uh
you have uh the system ID in in a
brackets in the URL so we first need to
find that record
then it's going to call on after get
record to get it they all have to get
Cur record and then you get on next
record no I don't know why it's can't H
in a repeater probably that's why
and then after our next record you get
again the on after get record and after
get Curl record for the second time so
if you have some code in on after get
record that is doing some heavy
calculation it's going to be executed
twice already here in this point
then we get a validate for the fields
but now something strange happens
only those fields that do have a changed
value will be validated
so if you have a field in the request
body that is
um having the same value as it is in the
the table the records then that field
will not be validated
it's not that you can force to validate
it in that way you really need to change
the value in order to get the field
validate
then you get on modify record
and then after that it's going to get
the record again and do again and on
after get core record
I don't know why actually because the
unmodified record is supposed to return
a modified record anyway but it happens
so that means that
um code in on after get record and get
cool record will be executed three times
that is a reason to not put a code in
all after get record avoid it as much as
possible and if you have any heavy
coding in there please do not do that
try to find another way or at least do
it one time get a counter or whatever
shall we avoid to do that too many times
okay
um
that is the patch operation let me
quickly show you that I was not actually
lying so I take this ID and
do that over here
replace this one
say send
there it goes
and then find out in this one here that
I have actually a new one
on in its on open page find again or
next and after get get cool
the validate of two Fields while
um here actually I have four fields
but only two fields did have a different
value so only those two Fields were
modified and then a modified record gets
record and get good again
um
then
we have the
delete operation
well we have again the same as with the
patch it needs to get that single record
that you want to delete so it's going to
be in an open page finds record then
again get get cool next get record get
curled record then on the lead but then
it stops yeah obviously the record does
not exist anymore so another get record
is not gonna work of course the on the
lead does not even return the record
I'm not going to demonstrate that I
guess you believe me in this
then um that post turning post into a
patch
that is a thing that I actually
discovered last week so I thought that
would be nice Nemo
um when you read the record from a on
validate trigger on new records will
still execute because that is before
validating the fields
but the on insert record will be skipped
and instead the unmodify record will be
executed
there is
strange
um and I found I found out because
I was actually playing with global
variables instead of fields
values and that is also something that
well it's a little bit unexpecting
unexpected so here I have an example of
that
uh
so here I have a an
um an API based on the customer table
and
um I have a field cush name which is a
global variable
yeah and what happens if we do this then
we and I thought okay I can uh in the
uninsure trigger get the customer name
and copy that to the record well that
actually did not happen if I call this
one
with just creating a new company
I get back nothing
see no ID no number and if I look into
the look
it's doing on open page on your records
on validate of that field
but they're nothing it's not going to
trigger the online search while I was
doing a post
well and yeah it's not that I figured
this out actually a partner called me
about this case
um so how could this be solved well in
actually it was pretty simple
um I could just say rect.name here
and if I publish this one
uh thanks God to this one man
if Microsoft can solve this then many
times you have to log in I will be very
thankful
come on
do it today yeah there we go
back to postman and do it once more
and now we have a record
so what happens and let me go to the
API triggers again
now we have the invalidate Chris name
and then I have to own the search record
again because now the record has a value
it's one field at least it figures okay
maybe you want to insert that record
okay but now something strange
what if I give a number in
um this one and what I then do in the
code
is
let's say here this piece of code
the record number does have a value and
then I say insert from the code
now this is funny
because you are in a post
um this is delayed insert it's enabled
of course on an API page
so what is going to happen
I would expect an error message
it should be already there
I get on number 60.
that value and if I look into the
look
come on
business Central speed up
go down
oh whoa into still this is the ill
inserts records but I already inserted
it in the unvalidate
hold that
get even more strange
what if I do something like this
I get the record
and now as you will see the ohm insert
is not executed it will be the
or modify
didn't I authenticate just a minute ago
you know the same thing with this is
that if I come back tomorrow
it just is Happy uh continuing and
doesn't ask me to re-authenticate it
asked me to re-authenticate every minute
or so but not every day
I don't understand anyway
let me
send this one again still number 60 is
not complaining about hey that record
already exists
and when we look into the look
we see that we get an on modify record
instead
but this was a post so it was supposed
to insert
maybe it could be useful for you I don't
know
um by the way we got back a 201 created
as a status so it might be a book but
actually it helped their partner because
they had an external system that was
only capable of doing get and post and
they could not do a patch so they needed
to find out the current records and well
this was a solution that was helping
them
all right
um
then something that I would like to
point out is using temporary tables
actually in the Microsoft documentation
um they say that paging becomes
difficult to do in a performant manner a
rule of temp is that you if you have
more than 100 records don't use 10
tables
I took this one screenshot from the
documentation
but yeah sometimes you have to have a
temporary tables
I mean it's not that you just can live
without actually uh I have to use it a
lot oops there was a little bit too
enthusiastic so what can you do well and
the tip here is that
um first of all the point is
um the problem with this is that you
cannot really use a server driven paging
because it needs to fill the temporary
table first and after that if you try to
do a top number of of records and Skip
or better we use server leaving paging
with the old data next page link Etc so
you say give me the next 10 or 20
records it always needs to load the full
set of data into the into the temporary
table
so what you can do is apply filters
yourself force that encode
for example fill data with a query
that's actually what I did here this is
an example from
an API that I created for a customer
and here what I do is I do a set range
in this case it was a fixed value they
gave it to me you should filter it on a
dimension code
um and what I he do is all the filters
and one of them is the get minimum date
filter and the maximum date filter
from the on open page I fill the
temporary table now if we look at the
code behind
then
let me find that one as well
it is doing something like this
if a function you retrieve posting date
from Filter so it must be in the filter
supplied but then I say well if the
filter is actually not seven
characters I say sorry I'm not gonna do
it you must Supply at least a filter and
it must be seven characters because it
must be in the format a year and months
with three characters in this case
um
so that was the the rule and with this I
forced them to have at least a filter
that reduces the number of Records to a
particular period so I'm actually
forcing the filters
and this is based on a GL entry buffer
table which is a table that is table
type temporary
and from the API page I call that this
guy get income transactions there I have
that query and then I have the mint date
filter and that is going to force that
and then finally this is actually a
query that's that I use in this case is
a query based on the GL account that you
could also filter then get a deal
entries related to that and then finally
get the dimension values related to the
GL entries so all in a query rather than
doing multiple repeats Etc and then
because I get back a nice query data set
I could easily filter that data set here
in the code this is the set ranges and
set filters it actually filters on that
query
and by doing it in this way I can ignore
that hundreds records limit that
Microsoft documents
Um this can work with a large deal entry
table pretty quickly
um okay then we have something that
people seem to be struggling with so I
thought well let's throw it in Bound
actions
bound actions are if you think about it
actually actions similar to what you
have on a page you have an action in the
action bar or maybe on the line itself
and that executes on the current record
so in an API page you can do the same
you have an action actually a not to
Define this in action but as a piece of
uh yes as a procedure I will show you
that
um and then that action can also return
data and you have actually two options
most of you who have been using bound
actions know that you can get back the
location header a location header that
points to the record that has been
updated
um that is done with something called
Web Service action context and there you
define actually a URL by supplying that
you want to get the URL for a page
which page is it the item API page and
for which entity so which record do you
want to have on the URL and then you set
also result code that it has been
created and that will then return a
location header I'm going to demonstrate
it
but another option is uh to use a value
to let the bound action return a value
rather than a location header
so I don't know about you but I get this
question now and then hey can I get a
sales price for an item for a particular
customer for a certain quantity
and yeah you might think okay I cannot
do that with apis you'll need to create
a a quite a complex API for that or I
need to go with Unbound actions well
actually you don't need it I'm going to
show you a function to get a price on an
item
um
and return the price to the caller so
um let me go to the code
found actions I have this item simple
item API the first one is this set
description
uh you see here camel casing by the way
that is for a reason because bound
actions always must be called with camel
casing
it has one time cost me half a day to
figure out um that that is the case uh
pen intended
um so if you call it like this with
capital S it's not going to work if you
define it with capital s in the
beginning you cannot call it with
capital S you still need to use
lowercase s in the beginning so for that
reason I use camel case already here to
make clear hey this is an API
bound action and you must use that name
well this is a very simple one set a
description on an item and this is how
we use it gonna find at least an item
and get the item ID
so the Athens disk
and set that to the
item id where is it over here
and call the
set description one
which is on the item API on a particular
record and then followed by
microsoft.nav so it's a little bit
nostalgic here I mean it's not BC or it
don't have dot set description
and this is going to be a BC checklist
20th century special table
and we should get back a 202 accepted
or 204 now content also okay 204 no
content and if I look into the items
it should have that description
come on
there we are
here we have the BC technique special
table now I should have opened this
before so you can actually see that I
didn't do this before but okay believe
me it works
so what about it
um location header I have another one
that is going to copy an item
so that is a function dot copy item
and when I do that
of course I want to know where is the
item that I now have copied what is the
system ID of that item or the number
well for that you need to get a link to
the new created item and that is
actually in the headers here
in the location header and there we get
a value complete value that I can use
use here
let's say
this and say there's going to be a get
and this is the record that we just
copied
including the number Etc
so the location header points to the
created record and that works
like this
we have a action context
do not forget to pass it by VAR
otherwise it will not work
um is a parameter that you do not
specify in the request it is in let's
say an outgoing parameter and well I
have this simple code uh get a record
um and a copy the record set a number to
empty and inserted and then with these
three these are the properties to
compose the URL so it's going to be a
page it's going to be this API page and
this is the system ID so you do that
with set object type object ID and add
entity key and then also a set result
code which is created
which is well don't see it anymore but
that was the um
let me
close this one and open it again
do the post again 201 created as you see
here so that is the two or one creator
that gets back from the service action
context
okay so what about returning a real
value
there's this one on the same page I have
a get price function and I Supply a
customer number and a quantity
I'm going to send it
I should get back a value come on
there was thousand point eight that is
the price for this customer for this
quantity
well actually
um
it is not well it is the case but I did
not change anything here
so
um let's do that
why is business General so slow today
somebody can turn it up please
so let's go with sales prices and say if
um
all customers order at least a hundred
the price is going to be uh 7.99
okay
go back here
and they are 7.99
so how does that work well actually
pretty simple
the only thing I do is I return a value
and then you get it in in in the caller
in the imposement in this case and the
way how to calculate the price I'm not
going to use that all the new pricing
stuff I just create and temporary sales
header and sales line and it let do the
work for me but that is pretty obvious
of course I hope you're all doing that
in the same way
um but this one is actually a key you
can just return a value which cannot be
combined with the
um the web service action context if we
also add this one to the parameters it's
going to
take that as a return and it's not going
to take this one
this actually works and well something I
didn't know for a long time only
discovered uh also a couple of weeks ago
so maybe you knew it already but I
didn't
then a small tip about versioning
if you follow Microsoft's way of doing
versioning you just put all your apis in
a separate app and then when you have a
new version of your apis you create a
new version of that app and change the
API version in all individual files that
is an option what is also an option is
to let an API be in multiple versions
in that case what you do is in the API
that changes you make a copy of that API
and in that API you say okay you are
going to be the newer version p1.1 in
this case but all other apis stay in
v1.0 so if they try v1.1 at that point
it's not going to work on all the other
apis but if you simply do this
API version v1.0 and view 1.1 then you
change one API and your other apis are
still the same this is the alternative
um so only copying the modified apis
rather than a complete app
it's up to you of course which one you
prefer
um actually in many cases I don't even
up version the API
because I in most cases I own the
integration as well like an Azure
function that is calling it and there's
no third party making use of my API
usually I own that API and the other
side as well in that case yeah you
actually deal with it you change the API
you change the other side and you can
continue but if you have apis in your
solution to be used by other partners or
customers then you need to think about
versioning and now you have two options
for that
um some magic relationship between apis
now if you have a relationship like
header lines or here as an example item
variants where one item can have
multiple variants we defined it as a
part just the normal way how we do the
wave parts in a header line page and you
point to the other API page which by the
way does not have to be an API page it
can also be just a page of a list part
um that's also possible and you define
an entity name entity set name on that
well actually only if the other page is
not an API page if the order page is an
API page you can leave out entity name
and enter set name here and you do the
sub page link and that's it and in that
case you can just do dollar expand
Etc
well this is possible to Define that the
part is not a one to many but a
one-to-one relationship
that is fine for example here item
variants
um sorry this one units of measure this
is the base unit of measure there's only
for one item one base unit of measure so
we Define zero or one and the result
will be in the request that you do not
get when you expand it you do not get an
array but you get a single object
however there's also something called
automatic relationship and that is
exactly what I want to
um to point out
um
and that
happens here in these two apis I do have
an uh an API for items
and in that API I have a few Fields ID
in a description
um item category and I totally code
and I have another one
which is the item category page
with just a code in the description
now the funny thing is that I do not
specify here any relationship between
them two I do not specify a part and not
specify that an item has at least or has
one item category or zero
but still what I can do is
expand it
so this is my API
and I can say expense item category and
it just works
so there's magic he is automatically
creating a link between the two apis
and the reason for that is that in the
table we have the fields item category
ID and the fields item category code and
both do have a table relation to the
item category table
and then when that is the case
the platform is going to find if there
is another API for that related table if
that is the case it creates
automatically the relationship
in previous in older versions of
business Central it would create it on
the first field that appears in the API
which means that if I do this and have
the code first
it's not going to work because the other
API was based on the ID the system ID
and not on a code
in the current version that is another
case it will say okay I find
um another API that is based on system
ID
and I see here
that category ID is actually in this
page and category ID this have a table
relation
to the table of the other API so
automatically link them you don't have
to create the part yourself
a little bit magic but if you know how
it works it can be very useful and
reduce you reduce some code
okay then
um
partial records something I would like
to point out is that partial record is
automatically enabled for API Pages it
knows the list of fields that you have
in the repeater and it will
automatically apply partial record so do
a actually behind the scenes a set load
fields
now that means that
um
if you have any other filter you want to
access from code for example here I'm
going to use a value ID and dimension
value code actually I copy this one from
a Microsoft API and those fields if they
are not
in the repeater in the API page will
cause a just in time load
that is something you should avoid and
for that reason in the unopened page you
should add them with ADD load fields
so because if that
partial record is not an option it is
there it is being used by the API pages
so be sure that if you have any code
that accesses fields that are not in the
API you use add load fields to add them
to the list of fields to be loaded and
your API will be faster your customers
will be more happy with it
a few tips about
reducing the payload which is also uh
well reason for performance uh for
performance reasons you can use dollar
select to reduce the Json payload
actually there are four demons in here I
will just mention them once and then go
to uh Postman
uh with dollar select you say I want
only to see these and this in this field
and it also works on the dollar expense
you can say from the expanded part I
want to see this and this in this field
only
if you want to do paging
not use dollar top and dollar skip but
you should use server driven paging with
the old data.mex page size header that
will return the number of records
including a link for the next set of
records with the same counts and then
repeat and repeat it over and over again
until you reach the end of the list
we have an accept header that we that we
can use to manage the old data tags that
needs a demo
and we can also navigate to a single
property actually also needs a demo so
I'm going to be here reducing payload we
close all the tops for now
um dollar select
so here I have customers as the standard
API and I tell him to only
um return the ID number digital name and
email
yep
you can expect that of course so let me
get a new access token
okay
why is that ah
that is the reason
here we are
so we have the ideal number of display
name in the email as we selected in the
URL but we can do the same thing with
expand this is a longer one don't try to
read it
um actually it sells invoices I tell him
to return a few Fields I tell them to
expand the customer and on the customer
I want to select only
a few fields
I want him to expand customer Financial
details on the customer
I want to have sales invoice lines as
well for which I want to have ID
sequence line type and some other fields
and on the sales in force lines I would
also like him to expand accounts and the
item depending on is its jail accounts
or an item and on the item please only
return ID number inventory
oh and please on that item also expand
unit of measure so talking about a query
yeah of course I should have that
this is not because the query is so
difficult oops the field
contains a value that cannot be found ah
so now's the data problem sorry for that
um that's funny let me just reduce this
a little bit
um
no I'm not going to do that just to to
so much time
it's apparently the data is not not
correct but the idea is that you can
combine it at least
sorry for that
um here I'm going to select customers
with uh only ID and number and I tell
him to only return three we have to
accept sorry if the prefer header our
data Max uh page size
should be three
oh come on
with all of them
okay so
um now I get a next data link
that
I can just click on and say
authorization is going to be
odd and used this token
so this is my next one
um and then apparently
I don't get them all okay
well the idea is that I should get three
again
not so nice that he's not doing it for
me
the next link let me put it in here in
yeah no this one is broken no value on
it didn't work so now I get the next
three and I can get a link for the next
three and
now I know why the other one wasn't
working because let header prefer was
missing
so I should have copied that one as well
and then another link and another link
until there's no link anymore that means
you reach the end of the list
so prefer is actually the one that you
should use with uh oh data Max page size
is three
then we have the um
direct navigate so I have here one item
why did he not store all of that
um and let's say I only want to know the
inventory for this item well you could
do dollar select
inventory but you can also say I want to
have inventory and then you get value 4.
and you could even go one step further
and say that you only want to have value
and then you only have four
so if you're interested in the inventory
of a certain item or whatever single
Fields you can do the dollar select to
have that field and then deal with
situation you can also
dive straight dive straight into that
field value and get only that value back
without any Json around it
then
maybe you
sometimes things think okay
okay now
I'm not buying it anymore
um here we have the standard stuff with
the odata E-Tech
and in the top and odata context did you
know there's a lot more oh data stuff
if we specify that we want to have oh
data metadata full
we get a lot more information
we get edit link we get a data type for
the ID
um well more information Association
links
you see that a lot more information
could be useful for example for
proxy generators that they know oh
there's something else Etc
you can also code it all the way you can
also specify sorry I'm not interested in
the oh data stiff so please
sent me none
and then we have a clean Jason without
all that old data beveling in between I
think this can be quite useful clean
Json which we can use
all right
um
the next topic is about a press practice
for monitoring your incoming web service
calls
of course what you should do is use apis
instead of all data and soap on UI Pages
there's obviously there's a a message
that is going out for a long time
already I'm not going to repeat it well
I just did
um well you should also try to reduce is
what is called aggressive calls you're
not going to call an a business Central
API 100 times per minute
I only did it in a test to uh to test
the performance actually
you should also check the queues because
the queue but in business Central is
a maximum of 100 requests
and five requests of the hundreds can be
processed at the same time so 95 will be
waiting in the queue until the other
five are ready and then a when the one
is ready takes the other one from the
queue now normal apis uh probably is not
running into that but imagine
um and a headache actually with some
customers they are also running heavy
power bi queries
so the web service call come in from a
power bi query some some user is really
hacking into it and it's this data so
that query runs for let's say two
minutes or whatever
and they have another user does that as
well another as well where you feel it
the number of five uh processing slots
are is reused to two so others and in
this case was a customer we're using
scanning devices which also integrated
with apis they only had two slots for
their API calls from the scanners so
they were going to queue up in the queue
and finally even run out of the queue so
you can you should check the time spent
in the queues and also fix non-200 HTTP
errors how can you do that well you use
the power bi based on telemetry
uh provided by Microsoft you can with
that power bi
um you can check out if your API code is
fast enough
you can check if your API calls are
getting queued up
um also on what the time of the day that
actually happens so are they called
aggressively or are they just spread out
during the day
and you can find out what is the
performance of your calls and what is
what other calls that do not return at
200 or 201 but return errors or maybe
um four to nine too many requests or
timeouts
Etc
these are errors you can just find back
in Telemetry and from
22.2 I think they also added
Telemetry data to find out if
um
Q entry so an API request in the queue
was actually timed out
because well it did not have a time slot
to be processed within I don't know how
long that this takes a couple of minutes
at least
but that is testing with telemetry
or monitoring what we also can do is
using Postman actually I do that a lot
to test the apis
Postman Rim time is based on note.js and
you can add scripts to postman
either before or after the request so a
piece of code that you prepare some
variables before the request and then
you get back to response you can read
response and save that into variables so
another request can make use of it
you can also in the in the test script
after the response check the data
is it still fill it does it contain the
values that you expected
and well that actually can be very
useful
so
um
let me
give you an example here
in Postman
foreign
in this case just a very simple one I
have a get
and the only thing I want to do here is
test if the return value is 200. so I'll
Define a test case with a description
and I tell him that I expect PM for
Postman Library response to have status
200.
and if I do that
and I look here
into the
tests
come on
actually
should go one step back here I have the
test results and it's a status code is
200 with green
and if I would say well I expected
actually 201
and also the description 201
and do it again it's a sorry false
it is incorrect I expected 2001 but I
got 200.
well how can we use that for example
here I have customers a customer that I
create
and in my test script I expect the
response to be 201
then I read the Json data response data
into radiation object and I I'm gonna
expect that my Json data is actually an
object
and not an array
then I have a schema a Json schema
well let's scroll down
these are defining all the fields that I
expect
and then I say I want to have the
response schema to be valid
this is Tiny validator that is built in
into Postman you should validate
radiation data against the schema and
expect it to be true so all the fields
that I expect are in the response
and then I'm gonna check the values so
in this case I'm going to create
something with display name BC
technology envelope Etc
and in the test I'm going to say okay I
expect my Json data display name to be
equal to that value
so let's see how that works out
and there I have my test results all
green
if you wonder about that schema because
that is actually what you use to
find out if all the expected fields are
in there so the structure of the Json is
is okay
actually generate that schema
I use this free I like free stuff
So I placed in an example of the output
tell him I'm still not a robot I wasn't
yesterday and here I have my Json schema
and that's it you just copy that
and you go into your test
and you paste it in here you say schema
is this value you paste it in there and
you have your schema and then you only
need to test if the scheme is valid so
you can just generate it and if you have
optional fields that you can remove them
from the schema if you read it it's
actually pretty simple
um
so
I've also used it in a slightly
different scenario
here I have a series of requests
and in the series of requests I want to
create a customer
I want to create an item
with some item name and then Price sets
the inventory on the created item
which I don't know at this point so I
need to get the value out of that item
post before
I call this one and finally create a
sales order for well the customer ID the
new customer ID that was created and the
new Item ID that was created
how does that work
well um
the funny thing is I cannot really
demonstrate it most probably because I
ran out of the maximum number of
collection runs
so let me see if I
still can do it
I agree I was I managed to run 26 out of
25 so
wow
actually
something went wrong
so maybe he's still not really working
got 400 oh that's also funny so what is
what is behind this oh my collection I
have a three request script
it starts with that on that pre-request
script I generate some random names
a random company name is a feature from
Postman so I use it a random product
name and a random price
when I run a collection it will always
execute this request script before
I put it into variables and those
variables will stay
will remain during the whole Rune of the
collection
so in my Post customer I can use that
generated company name
and I get back a company ID
let's see why he was actually not doing
it well here it now it works if I do it
step by step
so I have a uh a display name that
actually was generated by
um by Postman
I get back a company ID and with my test
script
where I test if I actually got back at
201 and if I get the correct schema Etc
I do one more thing at the end
after testing the response I also save
variables
set new customer ID based on the output
of this request on the response
and that can then be used in the next
one actually not in post items but in
sales order because here I have a new
customer ID in that variable is there
from the previous request
so in that way I can actually chain
request and have a complete flow of
creating a customer creating items and
Etc
and on everyone what I do is
set in this case the item id then use a
inventory well I don't need a test
script there to set something but I test
if it's actually set to that value
and then I run the complete collection
let me show you that it actually works
because I have written before
um
so this one here as you can see on the
timer was yesterday night
um
not sure if I can see the results
yeah so this is how the output looks
like
um creates it I get the response back
the status codes
etc etc so
pretty useful in case you want to run a
complete sequence
but there's also
pretty funny here
is when you want to run you can not only
run the request that are in a collection
you can also test performance
and say how many virtual users do you
want and how long do you want the test
to run
I cannot run this because he's going to
fail because I I actually am out of the
maximum number of runes 25 per month
because I do not have a paid license for
uh Postman and he didn't want to uh to
buy to buy yesterday night for 380 or
something uh I thought okay I just
explained but um using it for
performance could be a very cool uh tool
for you to find out if multiple users
can call those apis and how fast are
they
just from the outside not from the
inside and it would be very nice to do
this and then look into Telemetry what
is actually going on and compare all of
that
Etc
so
just uh some ways of testing your apis
with Postman
then
um the final
tip or trick or whatever you want is to
consume apis with c-sharp
if you want to
um to do that the first thing of course
is how are you going to authenticate all
that Azure uh or or Stuff Etc well
actually it's pretty simple uh you see
here I screenshots how I do that with
um the authorization called grain flow I
create first of all I I take the
Microsoft identity client package
install that in Visual Studio in my
application and then I use the
components in that package to retrieve
the O alt access tokens you don't have
to write any request yourself use HTTP
client or whatsoever you use the objects
that are in that identity client in this
case I'm using the client application
the public client application Builder
because in the example I was using I
don't have a secret
in that case it is a public client if
you have a secret is on the next slide
then you use the secret
client application Builder well actually
confidential client Builder
works the same after all but then you
provide a secret as well and then you
get that piece of code here I from the
public app say hey do you already have
some accounts
if that is the case
or sorry the first time it's not the
case I go down and say okay acquire a
new token Interactive
with the scope that I Define execute it
that will automatically in a console
application at least open a pop-up let
me log in and then return to the
application
and in web applications you can have a
similar Behavior because it then can be
combined with JavaScript it does that on
the client side
then if there was already an account I
say Hey try to acquire a token silent
because there might be a refresh token
in it so it's going to refresh that for
me
and if then it comes back and says sorry
UI is required for whatever reason I
called it a quiet token interactive as
well
and with that way I have it managed from
uh dotnet code to get a token
and I can use that token while
authenticating with the HTTP clients I
will show you the code for that as well
this is the other one for using the
confidential clients when you have a
secret then you use
um that Builder with DOT create with the
client ID and you supply the with client
Secret
that is also the one that you need to
use for service to service
authentication which is actually this
piece of code
confidential app dot acquire token for
client that's actually the client
credentials flow which is the service to
service Authentication
you tell him the authority which is
quite important because you must specify
a tenant ID otherwise you will not get
back a token
execute get back the results and you
have a token
um before I go to the code and and run
that so you can see that that actually
works
um
this is my way of dealing with the data
what I do is I create a c-sharp and she
have a greater class
and in that class I use
system.txt.json serialization and no
Newton soft has similar things but I
decided to stick with
um the dotnet core objects here and on
every object on every property I have a
Json property name
that Maps the output from your Json
automatically to that property in the
class
and then you can just serialize and
deserialize the Json data automatically
into that class you don't have to deal
with the Json like we do in in Al like
you have to read every single property
indication it's not necessary doing that
for us automatically
um but when we do I get
that gets of course on on a list of
Records on a collection that returns
actually not a single object that
returns an array of objects well that
array can simply be mapped as well
because we tell him there is something
called value in the output which is an
array so it is an array of customers
and by combining these two I'm actually
capable of
retrieving in this case customers
automatically
um so how do I do that it's here what I
am using is
um
a what is called an extension method on
the HTTP client called get from Json
async I tell him that I expect back I
type customers
of this URL
companies blah blah the company and then
customers
and then I can simply say for each
customer and customers.value which will
be the list of customers
so I only call that function get from
Json async I tell him I want to have bad
customers and it works
um
same goes with posting so creating a new
record in that case I use the function
post
s Json I give him one customer and it
will automatically convert it to Json
send it to business Central
it's pretty simple
pick I get the result back from the post
so what I do is on the result content I
shall read from Json I expect a customer
back
and it turns that into a customer object
there's no Json handling here all
because you defined it one time in the
class and it doesn't have to have all
the properties from the customer only a
few only the ones you're interested in
and
it magically does that for you
so I want to show you this code in real
life
um
[Music]
opening it come on where are you
there we are
okay if you now take a screenshot you
know my secrets I gonna and re-roll that
one in the other immediately after the
session of course
um
so
he or she that that public app you see
that confidential app client Builder
actually this application is going to uh
query my business Central say hey I see
two environments which one do you want
to open then I see companies which one
do you want to open hey I see this list
of apis which API do you want to see
which category
then I see some apis and then well Etc
so it builds it up from A to B into C to
D Etc
so let's run this one
um
and see if it still works and did so
last night
you see it opens a login prompt saying
Hey I want you to open to authenticate
that's complete you can return and here
it says okay I see in your environment
too
um uh environments in your under your
account I couldn't use the sandbox
then it says okay I found two companies
in that sandbox I'm going to use number
one
then I see a number of apis
um one of them is the the demo MPI that
I was using here in this session
um I also have the V2 API I'm going to
use that one number 18.
and then I get 76 apis found in the
standard API let's go with items number
six
get a question hey do you want to call
this with the locked in user or as an
application service to service
authentication both work in my case but
here's the data
so um
pretty simple say forward code actually
I mean
commits all of this
let's do this
um
and here you also see that code where is
it for the customer
this is all too many code actually to
explain
where is this here here's my create
customer code
um
that uses the post as Json
oops
and
he is going to send a customer and if
you go to customer you see here all
those properties being set
so no serialization no deserialization
Okay so
a list of
best practices that I use both in
creating apis and in consuming apis
with that
I have 10 minutes left for Q a
and I have these books that I can throw
at you
sorry
is it possible to debark web services in
BC
sorry say it again is it possible to
debug web services in BC
to do what debug or debug sure yes you
can debug apis absolutely yes
okay there's no problem you just use the
attach debug session and then you can
work with that yeah
doesn't stop on breakpoint it didn't
stop okay well it should so I
I tell you it's working and let me
quickly show you how
um
so let's take
um that API
thingy here
I have here some code
um on open page so I do a breakpoint
here
then
in my launch.json I should have
and don't have it right now so you need
to edit attached to a decline on the
cloud sandbox I'm actually using Cloud
sandbox here
and tell him to use my tenant
which is Cronus dot company
that's actually a domain that I own
and then I tell him to
um
debug without publishing
and I want to attach
to the cloud sandbox what is important
here is a break on next is web service
client
so now he should start and wait
so let's go to postman and
call this
host thingy
and there
my debugger is stopped so
it works thank you so much
but anyway
because I could now do another demo you
get a t-shirt
there seems to be different sizes but I
hope it fits
oh sorry
other questions
oh
they told me I can throw it so that did
the person are behind you
it's
the microphone is over there
guys you told me so I did
I think it's not working anymore
does it okay Troy yeah I hear it
is there a kind of rule when to use API
pages over Unbound actions or what do
you prefer in your daily business so
inbound actions or bound actions yes
well actually I was quite thrilled about
inbound actions because I thought well
and now I can do anything I want
and then you start thinking about it
for what purpose I'm going to use it and
in many cases a bounce action just is
enough
so Unbound actions only a few cases to
be honest and what are the cases in your
experience uh those cases are that when
you do something not really related to a
record
so
um
start a process well starting a process
online records could be a bound action I
really have a hard time to found a good
scenario for an inbound action
in most cases it's just a bounce action
that works in an inbound action yeah
I created a few hdmos but the real world
scenarios I still am looking for it
honestly
okay
let's switch so you you throw to me
you're good at that
and yeah okay I saw another one try to
be careful now
thank you have you got any comments on
transaction handling when
uh you've got say two simultaneous calls
for large sales orders to 300 lines
and making one right for the other
so you mean the transaction yeah without
within the API
yeah so every request on itself is a
transaction
so
um if you want to have let's say
multiple transactions and the one for
injection if that fill it should also
fail the others then you should use
batch requests because with batch
request you can send multiple requests
and say they all should be handled as
one transaction
search for isolation
I actually uh there's a post about that
on my blog
thank you
final sure was that so is there anybody
who wants to ask a question without
getting insured
you sir
look at me okay
I have a question about the arrest
response standard code
we see before that we test by Postman
for example the
200 code 201 code yeah but um I asked me
about
4Runners code and five under code it's
all all codes are
get
by Business Center in API
you mean which code we can receive all
set of codes over the rest standard
codes
um I'm not sure if Microsoft the
business Central returns all the codes
there are but just they return 400 for
1429 and all these things and these are
actually documented
is that what you mean you don't want to
know what I mean
yeah yeah
I'll show you I'll show you
actually
I have a nice page where you can
see what they mean
you can find out what every
HTTP status actually means
HTTP status Docs
so
here we have
400 for billion 404 not found
or
um
unauthorized
or I'm used
what that means
was another one with a oh here request
entity too large something so
just be found picture it explains what
it means
right
maybe it's also someone with cats I
don't know
other questions
you should jump
uh you mentioned that you had a problem
with the customer that request was
exceeded like 995 was the queue yeah how
have you solved that hahaha
we talked to Microsoft if they could do
something about it so now the thing is
that
um
we need to also teach those users that
well they have
um 20 30 50
people in the warehouse working with
scanners and if somebody adds the office
is going to start a big Power bi query
well
that is going to be
um uh intervened with the other says
that doesn't work together so they need
to think about it
it's not that we have to solve all those
use cases they also need to be trained
on using the resources in a good way
so if running big Power bi queries is
actually their needs maybe we should
think in that case to uh go with Azure
data logos other Solutions but they can
run power biome instead of querying
business Central directly
technically we cannot solve such a case
there are limits on what you can do
thank you
welcome
sorry
anybody else
you could have thrown that way come on
let me do that
look at him
So In This Confidential authorization
type you use a secret right to acquire
the token
and those Secrets have its own
expiration dates
do you ever consider some kind of
automation to refresh them and provide
them to the client or is it dollars will
work I'm so glad you asked
um the answer is no
um my recommendation is to not use
secrets
because Secrets expire
and of course you you must think about
it like um you can get back an error
message from
um uh Azure that says the secret you
were using is expired or incorrect
and then you could react on it but then
you are too late so you must know what's
upfront
now you could create two
secrets with a different expiration date
you store them both and say okay if one
expires I can fall back on the second
one and give a message to refresh the
first one
but the thing is that secrets are
actually
by means of documentation
for development only they should not be
used in production
so my recommendation is in production
you do not use secrets you use
certificates
and a certificate you can use a
self-signed certificate for that you
don't have to buy a certificate and the
certificate can have a 10-year
expiration time whatever you define or
30 years
the thing with a certificate is that is
actually
contains consists of two parts a private
key and a public key
and the private key you keep in business
Central and the public key is what you
upload to azure
so the public key is fine everybody can
see it the private key stays in business
Central and yes I have code that can
create a that key in Al code sorry the
the certificate in Al
that can create an app registration
upload that public key set the
permissions creates a grant the
permissions all of that so rather than
saying to the user end user hey you need
to call the Azure Port you need to do
this and copy your client ID and set
permissions and do this and this they
just say create app registration in the
application
they allow business Central to access
azure
must do that and it will create
everything for you including the
permissions including the certificate
that's exactly what we need for
customers
and I have customers working with that
it's quite some Cults to be honest but
it works
thanks
anybody else
uh final question because otherwise the
lenses uh this is lunchtime I think
shall do this
whoa
is there a way to debug a production
environment for example snapshot or for
web services yes okay yeah I couldn't
get it to work so yeah okay well I'm not
going to demonstrate that now sorry
all right well uh thank you so much and
um
if you have any questions you can find
me
and don't rest
