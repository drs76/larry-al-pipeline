# Microsoft Presents: Leveraging advanced design patterns for extensibility

- **Source:** https://www.youtube.com/watch?v=La5b7VcMhOc
- **Video ID:** La5b7VcMhOc
- **Channel:** mibuso.com
- **Published:** 2024-06-16
- **Duration:** 42m15s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

hello
everyone first I would like to thank you
all for showing up to there it is really
pleasure to see so many of you my name
is mar Alex I'm software engineer in the
business Central application team and
here with me today is my colleague and
LaRon yeah hello my name is Anders I
have been working with this great
product for quite some time and I still
love every day that I take into work to
work with it but welcome today we are
going to present you several topics some
of them are new some are old but not
well known I hope that you will find
them interesting and that you'll be able
to learn something
new uh first topic management code unit
anti Panter presented by Andre so and
the FL to yours thank you so we have
iterated through this and many others
have iterated through the manage code
unit anti patent several times this is
just a little short reminder
of uh is completely violating simple
responsibility it's hard to
maintain hard to read we still have a
lot in the base
app uh and there's Conflict by merging
them so why do we actually have those
code containers it think it goes back to
when we had the old architecture where
we have the develop environment where
you have to open an object so there we
just use it was good idea to have code
containers because you then don't need
to go forth and back now we can search
around and it works way more better we
will eventually deprecate those but we
will do the strategy the strategy is to
dehydrate them as we are touching areas
take the code out and put it into more
dedicated code units and
hopefully we'll get rid of some of them
down the
road we have new patterns new
capabilities as we have moved to a
visual code Visual Studio wonderful I
will just give a little uh sneak peek in
one of the things we have been utilizing
for this
release uh in called the orchestra
pattern here
is a drawing we will not go to to the
code in detail for this presentation
here but the idea of the orchestra
pattern is have a kind of should I say a
story board so this story will be this
is for the 1099 us tax thingy where you
need to have proof that the vendors
truly have sent those invoice to you so
you're not cheating that's the short
introduction to why we have this
feature the story is we need we need to
calculate some form boxes we need to
create some documents and we need to
print what is grayed out will come later
uh email and submit so each story have
its
contract let turn glasses on and for
each
contract we have implementation that
will kind of leave very well off to have
this single responsibility of
code I have another drawing if that is
more easier to look into and you can see
underneath here there is a link to
GitHub where you can take a deeper die
into the
code but again we
have the orchester containing the
story
the definition of interfaces and
component as as
well a little sample of how the contract
could look even though I'm not going to
show much code in this part of the
presentation as you can see it is
rather um build into set into building
brockets where it have single
responsibility and hopefully a
reasonable Okay naming telling what that
code unit and that fun function should
do so we have a single responsibility
principle here of
solid uh we keep the collections of
interfaces and contract in one place and
it's is also working very well with the
facade
around so you have implementation and a
facade and therefore you can
Yes again there I can see we have a link
to the
code so this is an example of
a new way of coding that we have started
to uptake here and this is presented
here for an inspiration for you if you
so want to follow that path kind of also
works a bit well with the factory
pattern but uh
if you are writing an app I know a lot
of you have done that already probably
also some test if you in the app have
internals you can
[Music]
use uh in the app Json to give your test
access to those
internal it will be recommended to also
do that in test Library instead of the
test so or do that create a test Library
and then the test and then they expose
you are to the internal to the test
Library so if somebody else extend part
of the app that is not internal then
they can also write
test Please be aware that internal is
not the same as non
debuggable so if you have sensitive code
sensitive things you should use that
property in your
appap and just to see how simple it
is there's this internal visible to in
the app Json where you in this case can
see that we have exposed internal
visible to the taste
library that will be room hopefully for
questions in the
end now I'll hand over the word to Marco
thank
you uh probably some of you had
situation where client ask you can I
have just three these values in the list
I'm not using the other ones or can I
have the value of x on the top of the
list because I'm using it mostly I need
to scroll each time to the end of the
list to get it or they have just some
options which are don't use and user can
be
confused actually this can be done
pretty easy and it is already
implemented in the standard code if you
take a look on any purchase or sale
document sub form you will see here for
example on the sales in some form that
we have two times field type and one the
regular
one and another one is a text we are
interested in this text one and as you
can see we have the table relation on
the option looka buffer table and the
looka page is option lookup list and
this table need to be filled in some
moment as it's temporary and it is done
on the any trigger of the
page and as you can see values like item
and g account are always there but
values like item charge resources and
fixed asset are added just in case
they're Inus in the system so the
purpose of this change was to eliminate
the values which are not in
use except that we have the part of cod
which is in charge for uh controlling
the values so what user can select or
type so autoc compation is also included
in this
functionality and of course we need to
have the synchronization between the
regular field in this text one as the
for further processing system use the
regular
one I would like also to mention that we
have the property values allowed which
can be used for this kind of situation
but it has
limitations as it can be used uh just uh
in the same app where the field is
created and also if you have some
specifics you need to qu
it uh if you want to make something
similar it is pretty easy I will
demonstrate you some
example here we have the general journal
and the field document type with several
options and if you don't want to use
some of the values or some users not to
be able to to to use some values you can
make your own uh lookup for for that
page and to do that you need to extend
option lookup type
enum create two subscribers and make the
page extension of the particular page uh
the only limitation here is that you
cannot set the order of the
values so I will demonstrate to
you so we have the option lookup tyum
and we extended it with additional
value and accept that we need to create
two subscribers want to
Define uh which field we want to for
which field we want to create the lookup
and another one to choose which values
we are going to use so we can Define our
some specific conditions for for this
part and of course we need to create the
page extension for the particular page
when where we remove the regular field
add our new text one and add some code
to complete the full logic and do the
synchronization with these two
Fields also this is not applicable just
on the Anum Fields you can use it with
different types of fields so for example
for the Cod type field you can also
implement this logic it is a bit more
coding but still it is not too
complicated here we have the service
order and for example we don't want to
use uh all locations for the service
document so we can make our own lookup
page and for this we need to extend
option lookup type we need to create new
temp table and new lookup page the good
thing that we can copy most of the code
from the original one and of course we
need to extend the p uh the page that we
are want to update this code uh will be
a code for this example and the previous
one will be available on the GitHub so
you can check it try it make your own
examples and now Andress we'll present
you the temporary table anti patter here
you are thank you thank you Marco so
something old but in a new Contex at
least in the new architecture that we
have now in SAS and also you have some
to on plan when we got the temporary
table two decades ago I loved it so we
could take a huge amount of data put
them into a memory offload that memory
to the native client the rich client and
then we wouldn't kind of uh impact the
other users at the system because we
have fre the shared resources do the
massaging blah blah blah on the
temporary and then when we are done
either exporting we're all good but but
in general it it was looking good we
were very hopeful about that we have
seen moving to the new architecture that
now you
take we also take a lot of data from the
SQL put it in on the NST but NST is now
a shared resource so it will impact my
neighbor or whoever performance
wise so a bit of performance impact then
we also have the wonderful subscribers
especially on before insert
trigger are you always sure that whoever
subscribed to an un insert on customer
always cater for if wreck is empty and
then bail out
it could be that somebody else have a
little code that do if comp customer
insert then I also need to see if I
should insert payment terms and
whatever
traditionally this is just sample code
we will have or others you will have
collect the
entries do something with the entries
and Export them
if I go a bit down here you can see you
will iterate blah blah blah there some
filtering oop boop boop and then we will
go
to uh somewhere yes we
take the entries and put them into the
temporary do something blah blah and
discount this is a a little issue we
actually have on manual applying of of
entries in our posting functions we will
hopefully get around to fix this
soonish and
then if it for instance not have been
applying entries but collecting
something to export for for VH or
whatever we will run the
export we could you could make that
pattern just slightly better by
introducing a temporary
table with reduced numbers of column as
well and the same code collect collect
collect and then export but down here
whoop whoop
whoop we are not transferring the whole
record but only the fields we need to
the vendor number the applied to amount
I think the entry number is already
there so we will have a very reduced uh
set of data in memory we could also when
we are fetching data with the from the
SQL Server we could use this set load
field so there again we will get way
smaller amount of
data so takeaway is try to to utilize
the table type is temporary and only
fits those fields and store them that
you need actually a good pattern for
using temporary record could be uh what
we used to name as buffer table posting
buffer you start collecting something
collecting something oh there's
something I need to post put it into the
posting buffer of type
temporary and then when you are done
collecting and want to post you take the
record the posting buffer iterate
through them call the posting routines
and clean
up that will also guarantee you don't
have any often hanging you know and make
sure that you when you are declaring the
variable that it's truly a temporary you
have the compiler will help you with
that so now I'll hand the word back to
Marco who will talk about manuals this
manual subscriber pattern thank
you uh one quick reminder uh when we are
creating the subscribers on the code
unit level we have option to set the
event subscriber instance and this
property is there to Define how the
subscriber will be activated we have two
potential values static automatic which
is the default one so with this value
subscribers are always ready and you
have the manual which we use when we
want to activate subscriber in specific
situation each time when subscriber is
called the new instance of code unit is
loaded in memory and it takes some
processor time and it because of that it
would be great to call subscriber just
in situation when you really need it
because of that our recommendation is
use manual binding whenever it is
possible and interesting thing that the
static automatic is the default option
because it was introduced just a little
bit be small time before the manual
option but in
general we should use
manual optional as default if you
can uh to use the manual option we have
two procedures that we need to call one
is buy subscription which is in which we
use for activating the
subscribers and unbind subscription
which we use to deactivate subscribers
when the transaction is done I will show
you some very Bas
example so as you can see just
I hope that you able
to see it we have very based procedure
which gets to number and Summit and in
in that procedure we have the
publisher and also we have the
subscriber for that publisher which
update the value of the number one if
it's bigger than number two and also we
have set the the property EV subscriber
instance to manual so when we for
example call
sorry this procedure without the binding
subscription system will just sum these
two values and return result
15 but if you call it with buy
subscription sister will call the
subscriber make the change of the number
one and present the new value as 5 + 5
is
10 so
we can set uh when the subscriber will
be executed and it can be very useful in
some situation for example here we have
the subscriber on the code unit document
print and on the publisher before
process print sales
order and uh here we set the language
that will be used for the report it's
dutch
Belgian so
this is the subscriber which will be
called just if he buy subscription on
this particular code unit
and uh as you can see without uh setting
the B subscription system will just call
report in the standard way how it work
but if you have some specific condition
we can set it and add the bind
subscription and unbind subscription and
uh print Report with some different
language and any other specific change
that we
have if you talk about the base app we
have the very interesting example of
manual binding in the preview
posting if you take a look on the
preview procedure in sales purchase
service and many other models you will
see that this procedure is almost the
same for all of them it is binding
subscription to the same code unit and
calling the general journal posting
preview and uh the subscribers in these
code units are in charge to uh do the
posting
process and general journal posting
preview is activating
uh the subscribers in the posting
preview event handlers and subscribers
in this c unit are in charge to take the
values from the posting procedures
actually to to collect all the Ledger
entries and store then me temporary
tables and even the general journal
posting preview is the main code unit
here he's doing almost nothing he only
uh have the common code related to the
all posting procedures and presenting
the values to the
user this approach is really interesting
because the posting logic is keeped in
the posting procedure and there is no
mixing between different posting
procedures on the other side all code
related to the collecting values for the
preview posting is stored in this
posting preview event handler code unit
so we keep our code cleaner and it is
easier to maintain
it uh in general using the manual
subscriber is very useful for many
situation where we have the some regular
flow and from time to time we have
situation where we want to make
something
different and of course it is we have
more control on the code
execution I would like to mention also
that the example that I show you can
check them on the GitHub and try and
make your own
examples and now Andress will present
the isolated events here you are thank
you
so again in the old days we have if code
unit.
run that's good for kind of try
something out and and swallow the error
so to speak but it can not collect all
the errors that you are
getting we got triy function fantastic
but there's a limitation with the white
sorry right
operation now we have got isolated event
love
it and it's just another
property when you
subscribe Please be aware that it calls
an implicit commit
after leaving the
event a very important
detail so a new
transaction it's good for doing
Automation and it is also good for doing
uh locking if you so want
to so let's go down over and see some
cod I will just flip here boom
so and thank you Marco for learning me
about manual subscribing because this is
used in this little test here there's a
little little code
unit that creates some uh some uh
customers and raise some event the first
one is having an nonisolated and the
second one is
having an isolated
event so if I go to test
yeah
just talk to bit so this is a very
simple little test it binds the
subscription if you look a bit down the
subscriber here that is just raising an
eror
so and this is a nonisolated
event so if you run this test code unit
you will uh on your code unit insert
customer after non insolated isolated
event that'll of course be an
error the error message
here all as we are used
to another
test again I try to keep the code here
very simple so bind the
subscriber insert this that will read
an event let me just say it here first
isolated event and insert
customer the isolated event we have down
here
just it is just throwing an
arrow so what is happening when I run
this
code the first isolated event an error
commit roll sorry not bail out but
continue insert the customer the
customer is
insert straightforward but
still and then of course we have a
procedure with a very long name insert
customer in isolated event and throw
error in nonisolated
event again we do
The
Binding we count the customers just to
see what is going
on and
here second isolated event and then a
non-isolated
event so we will get an error executing
this but we will also get a customer
insert again I think the error that will
come
from this one is insert in the isolated
event and the error will come
[Music]
from this
one nonisolated
event but again utilizing the manual
binding it's actually very good in test
imagine if you somehow leave a test app
and have a subscriber doing anything or
a lot static but have it more balance uh
sorry manual bound so it will only be
executed if you're running the
test
yeah and then is it time for GitHub
request it yes
I think we'll have room for questions in
the
end last but not the least gby went
requests one question for you how many
events we have in the B app please raise
your hand who thinks it is about
10,000 one two less more few at least is
raising the hand we have more than
21,000 events in the B app and how they
are used unfortunately more than 3,000
of them are not in Ed at all if you talk
about the SAS version highly used one we
have less than
300 and events with low usage we have
more than 3,000 of
them also very popular is handled event
we have more than 7,000 of
them and if if you take a look on the
chart you will see that with every new
version we are adding a very big amount
of new events it's something between 700
and
1,000 and interesting is that this
events with is handled pattern we have
more than 30% of
them speaking of each these kind of
events very popular as I said but
unfortunately in a lot of situation we
are using them wrongly
when they are introduced six or seven
years ago the idea was to use this kind
of events in situation where you don't
have developed some functionality or
part of functionality or the current
approach is not applicable in some
scenarios the idea also was to have only
one subscriber which will update the
handled variable and do the logic and in
case we have have several subscribers
only uh all of them they need to check
is it already handled and if yes just to
leave it and how we are using it today
in a lot of cases just to skip some part
of the standard
code that's not the greatest way of
using the
events and all of us we should make some
additional effort and try to create
better
events as a help we provided you a new
guideline a new request form with
several questions that you need to
consider when you are creating the
requests we divided events into several
groups by their value and we would
really appreciate to see more high value
ones also in in this guideline you will
be able to see see the examples of any
type of
events when you're creating the request
and you have several events related to
the same functionality please put all of
them in one request give us a short
description what your intents are it
would be much easier for us to
understand your need and help you with
it when I mentioned is handled events we
will probably be a bit more strict with
them don't get me wrong we don't want to
make you stop creating the event
requests we just want to encourage you
to create
more events with
a bigger value that can be used in
different situation with different
scenarios and applicable for many users
ERS uh this guideline will be available
soon on the GitHub and after you're
going through it and if you have some
questions doubts
please tell us that we are aware in the
fact that this is not the final last
version and we have a lot of space for
improve it but this is a journey and all
of us we should do our best to improve
this
process at the end I would like to thank
you all for your contribution not just
with the event requests but with other
accessibility requests ideas bu fixes it
is really nice to see that so many of
you want to be the part of this
extraordinary software so thank you
so actually it turns out that we were
talking to this a bit faster than we
anticipated so we have room for
questions there's this little thing we
can handle it up together with a mic and
two
T-shirts hand who wants the T-shirt oh
this is working um I had a question
Anders about the uh internals visible
um there is actually a v vulnerability
there because if I know the ID of the
app that is allowed to access it I can
create an app and access it that was in
the past is that still the case yeah
internal visual visual to in the app you
have will grant in this case uh the in
the test Library access to internal yeah
but then if I hijack if I create a new
app with the same ID and the same
publisher probably yes but so what we do
is when we build our app for production
we remove it from the app Json because
it's used for test and only for test
internal and yeah so but maybe it was
changed in the application or the
platform so but be careful with this
that's my message yeah it's a very good
comment throw it somewhere else
yeah that's a good comment we also do
that a lot even for our production app
so I will remember that thank you uh I
have a question about the events
subscriber or the code units we use a
lot of single instance code units to
prevent the loading of the uh software
so to say yes uh what is your idea on
that because now with a manual
subscription it looks more in time just
in time so would say I say yes in
general you can use both yeah and it
would be the best probably okay is there
a mix or is it like non preferable
or probably the best would be to use the
manual binding whenever it is possible
of course there are situation where it
is hard to use man binding but in
general using the single instance code
unit is something that I think you can
do in probably all situation
and of course if you can use the manual
binding in the same situation that would
be great okay thank you very much but
use single instance code Unity
carefully and do not use
globals of course if you can use the
code units with less procedures that be
also be good but yeah it dep thank
you it is this row who who is very
active has a
t-shirt um what what is Advantage uh to
use sub bind subscription if a code
should be called always so no exception
no um
condition
um I'm not sure that I get
you um so if um we have some event which
um need to call in all situations
without any check uh what the advantage
of using bind and unbind subscription I
think that advantage that is asking the
question you said should it be used by
all all time and are you damn
sure if not use manual okay so does this
make sense uh pause and say should I do
this and especially if you are doing
writing test which I hope all Engineers
are doing
nowadays please in the test always use
manual
subscribers as you might leave test
somewhere where it shouldn't
subscribe we out of t-shirts but we have
room for a question yeah uh so if I bind
manually and then forget or not even
forget but uh purposely don't unbind it
because I may need to do it again I
believe uh it unbinds with the life
cycle of the object that bound it but is
there any performance penalty to
that should it be avoided forgot to
unbind it and code unit is local it's no
problem at the end of transaction it
will be yeah I know
but I'm I'm actually not sure about I'm
actually using
it okay I will Che you definitely there
could be just a tiny bit but but the big
biggest performance gain that is not to
get a huge amount of data from the SQL
Server mass s them through with a non
index and so on and so forth but of
course a
little so this is just to follow on from
from M question um in
general uh manual versus binding is
their performance um difference or is
there an impact using the one over the
other not significant again think more
about how you build your code instead of
worrying about this uh on binding
binding will this impact performance
nonsignificant impact so efficient code
will will do the trick yes okay
yes one last
question from here and another in the
third row we have there this will be the
last question for
now I really love that you you have a
lot of good questions yeah fantastic so
so you you said uh regarding um use uh
special temporary
table but uh there is a downside because
I need to copy Fields do plan to to add
some like a reference to the main table
like a page where I can select the
fields and I don't need if for example I
change field in a main table and it
automatic changed in temporary
table well do you understand what I mean
to a construct where you have a
temporary table exposed in a page and
you want to manipulate change something
in that row oh I mean uh you you
suggested to use a pattern table
temporary but if I just create it uh it
means that I need to copy all fields
from hopefully not all Fields not not
all Fields but if I change some field I
need to duplicate it yes but again this
is It's a downside do you plan to the
potential overhead but the
recommendation that is to have temporary
table with as few column as possible but
of course if there is a reason for you
to have more or less the whole customer
table uh in a temporary record for
whatever good reasons then do that but
but just be aware that you shouldn't
have two million rows that you need to
copy or or 50,000 there not a magic
number but again pause reflect
Implement thank you all and with that
being said we'll hand over to the next
crew shortly yeah you can applaud
[Applause]
