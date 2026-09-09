# NAV TechDays 2014 - The new Paradigm of NAV Upgrade Story

- **Source:** https://www.youtube.com/watch?v=p8uyZmVQHwc
- **Video ID:** p8uyZmVQHwc
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 99m53s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

ladies and gentlemen good after a good
day thank you for joining us here again
in this room uh would you please welcome
our next speakers it's uh please a warm
welcome for aida anka and bass
[Music]
hello everyone and welcome to the new
paradigm of nav upgrade story in
microsoft dynamics nav 2015. allow me to
introduce ourselves we are car rental
systems inc we are a distinguished nav
partner we develop solutions based on
dynamics nav for the car rental industry
our customers are already running on our
most recent solution based on dynamics
nav 2015
and we have customers spread it all over
the world
our biggest customer is actually located
here in belgium they have branches in
seven different cities
and currently we are working on an
updated version on our main add-on the
vehicle management and this updated
version comes as a reply uh from our
customers feedback
so we are now towards the end of the
development phase
uh we are putting in the latest the last
changes and we really like to roll out
as soon as possible an updated version
to to our customers and especially
directed it to the the one in belgium
so let me introduce you to
uh my vehicle management add-on but
before that
uh let me introduce you to my team
i imanka and together with bas and ida
who are all part of the nav development
team at microsoft in copenhagen but
today we are going to represent the nav
developers from the car rental systems
partner
so let's have a look of the on the
vehicle management add-on
i have now opened the rotary client in
now 2015
and if i'm going to departments vehicle
management
i open my list and as you can see here i
have
a simple page with
headlines and line formats some general
information about my vehicle
some service information when is this
vehicle last service
and also a fuel tracker
the main feedback from our customers is
that they would like to track the
service
for a vehicle and have an overall
estimate of what is the maintenance cost
for for a vehicle for a certain time
a second
feedback was actually in terms of
usability they don't quite use the
description field so this field seems
redundant
how i translate the customer feedback as
requirements for me to implement
is i was basically refactoring out the
service fields from the vehicle table
and have a one-to-many relation between
the vehicle entity and the service
entity
and i would also need to delete the
description field from the fuel
consumption
so let's have a look at the data model
from my development environment for the
vehicle management add-on
i have here the set of objects from my
mini add-on
and if i just look at the tables i have
already started implementing the vehicle
service table which is a new table in my
updated version containing the service
fields as well as
the linkage to
to the main entity to the master table
of my add-on the vehicle
table
and the vehicle table here is something
that i need to work on
so i will basically need to refactor out
the service fields from this table and
move them together with the business
data to the vehicle service table
let's try to delete these fields now
and save and compile my changes
and note here the new save dialog in now
2015 is decorated with a synchronized
schema
option
let's zoom in this option
and some background information in our
2013 r2 we have introduced the concept
of schema synchronization which
basically means
propagating the table metadata changes
to the sql table via the nav server
this process was done back then
automated
in the background triggered by any
connection to the nav server
in the current release the synchronized
schema process is done on demand so in a
more controllable fashion
and it is also done at a more granular
level you can either
change your uh
changes once you have done changes to a
table so per table level or you can
choose to synchronize all the tables
from your database as well as in the
past release so global synchronization
but since i have the option to
granularly save my um synchronize my
schema for a table that i'm changing
then all the dialogues once i'm changing
the table have been decorated with this
synchronized schema option i'm referring
to the
save dialog the compile dialog delete
also when i'm importing a fob and this
fob contains tables
so
you will see this uh this
option whenever
you make change modifications to tables
and deep dive within the synchronized
schema
i can now tell the server how i want to
synchronize my schema from seaside
i have three options and then you'll see
the the first option is now with
validation and this is the default
option
this basically tells the server to go
ahead and verify if my table metadata
changes can produce any deletion of data
if i'm doing additive changes such as
i'm adding a field or i'm renaming a
field
changes which are harmless to data then
such changes will not produce
will not impact negatively the data
the validation will pass and my changes
are going to be saved in metadata and
propagated to the sql table
if i'm doing destructive changes then
and i'm not handling them properly then
the validation will fail my changes are
not going to be saved and i as a user
i'm going to be prompted with a nice
explicit detailed error message of what
is my current operation that failed and
also in work around how can i fix
my operation
the second option that i can choose is
synchronize schema later
this means that my table changes are
going to be saved locally in metadata
but they are not going to be verified or
synchronized to the sql table
this option is actually useful if you
don't have an nav server connected to
your database
and the third option which is also the
most dangerous option
is synchronized schema with force
this option forcefully applies the table
definition changes that you have defined
in seaside to your sql table and doesn't
care about the data
so
this option forcefully applies
your changes and will potentially delete
your data
so use it wisely
for my example i need to save
the information from the service fields
so my option would be now is validation
let's try to click this one
and see what happens
as you can see i'm prompted with the
explicit error message of what is going
wrong
so my schema synchronization may
deleting may result in deleted data i'm
applying the destructive changes to
destructive change to my table and you
see here what what is the operation in
detail
but i'm also suggested
an example of code how can i work around
my issue
but note here the keyword destructive
change
so let's have a look
and see what else besides deleting the
fields is considered the destructive
change
going to go back to my slides
and as you can see besides deleting
tables i can as well
change the data type of a field change
the sql data type of a field decrease
the length of a field
remove a field from a primary key change
the id of a field all these are
considered destructive changes
and
they will be blocked
unless the nav server is given a
specific instruction how to handle such
changes
so basically to synchronize such a
change you need either to provide an
explicit upgrade instruction to the
server which nominates the table where
you are
doing such a change or do it the
non-recommended way to forcefully apply
uh
the the new table deficient definition
to the sql table regardless
of data
back to my example
so
the example of code which i am provided
here is actually the upgrade instruction
that i need to provide to the server
i'm going to save to my clipboard the
output of this error message and let's
go through in detail through this
upgrade instruction
it is
tied to my vehicle table the table which
i'm modifying i need to define
optionally an upgrade table id the
upgrade table id has the purpose to
backup the data from my previous version
of the table
and
a
table synchronization option
i will start with creating an upgrade
table since i want to backup my data
and roll back
my changes i'm not ready to synchronize
my schema yet
and note here that i start implementing
the upgrade table this is actually doing
the upgrade step one
in order to create my upgrade table i
will start as a template from the table
which i'm modifying so again from the
vehicle table
save as
i'll give it
an upgrade range that we use in our
company
call it upgrade vehicle
and i'm only interested in saving the
data from the service fields
so i'm not interested into the other
fields
i will keep the number field because the
upgrade table needs to have the same
primary key as the table which i'm
changing
and i will make sure that i don't have
here any
functions variables defined
since this table needs to be completely
empty
okay
i will forcefully apply my changes
because it is a new table so no data is
endangered
i have created an upgrade table so i am
halfway through filling in the upgrade
instruction
you may wonder where does this upgrade
instruction reside
in now 2015 we have introduced a new
type of code unit namely the upgrade
code unit
so let me create a code unit of type
upgrade
i will access the code unit properties
and set the subtype
to upgrade
and we'll start creating a function
within an upgrade code unit there is a
set of triggers that you can define
the trigger which is relevant for
upgrade step one basically the
preparation for the schema
synchronization
is a table sync setup
i'll refer back to the second set of
triggers
later in my presentation
so within the table since the tab
trigger you will define your upgrade
instructions
so in the section of code i will paste
the output of the error message i got
earlier
and just keep the line with the upgrade
instruction
i will also add
a variable of type code unit
which is the data upgrade management
code unit it is
a helper code unit which you can find
into the demo application from now 2015.
and let's try to save and compile this
code unit that is
call it nicely upgrade vehicle code unit
note here that i am prompted uh that my
get table think setup function uh
triggered
labeled as tablesync setup type has an
invalid signature
i have forgotten to reference table sync
setup this table actually is very
important during schema synchronization
it is a virtual table and the nav server
records all the tables ids which it can
find as modified
into this table
so i will add it to my function
and have a
reference to it
the layout of this table is basically
the table id which is changing
the upgrade table
which has the purpose to backup the data
from
the table that i'm changing and the
schema synchronization option
for this table so
i'll replace the placeholder with the
upgrade table which i have just created
and let's have a look of
on the modes that i can handle the data
from this table
i have here a slide
so one of the upgrade modes um upgrade
options that i can define when modifying
the table
is upgrade option check
this means that the server will try to
apply my change and fail if it finds
that my change
has a negative impact on data
for example if i am deleting a field and
this field does not contain data then
upgrade option check will be applied
so my
field update will be propagated to sql
if my field contains data
then upgrade option check will fail
and i will get an error message that my
change could not be saved
on the other hand upgrade option force
will never fail because it will
forcefully apply your table changes
regardless if you have
data into the fields or not so if you
don't care about the data again you can
use upgrade option force
for upgrade options copy and move
these are the options which back up the
data from
the previous version of the table that
you are changing so for these two
options you need to define upgrade
tables
in case of upgrade option copy
you will backup just a portion of your
data so your upgrade table will only
contain the subset of fields from your
original table
and the new table will still contain the
data remaining on the matching fields in
case of upgrade option move the entire
table will be
backed up
and
the new table that is created
is going to be empty
so we have designed grade option move
when you completely want to
redesign repurpose your table
for my specific example back to seaside
i have an upgrade table id
which backs up a subset of fields from
my original table so i will use here
upgrade option copy
save and compile my changes
i now have everything in place for
a successful schema synchronization
while deleting these fields
synchronized schema now is validation
okay no error this time that's good sign
i'll run the upgrade vehicle table to
see if the service fields have been
saved here
perfect
and i'll run the vehicle table to see
that the table still contains data into
the remaining fields
all fine so far
so i am basically done with schema
synchronization which is upgrade step
one now i need to move the data from the
upgrade table to the vehicle
service table so to the destination so
i'm implementing upgrade step two
for this
portion of code i'm getting back to
my upgrade code unit
and within my upgrade code unit i'm
making use of the other triggers
so i will create a new function
call it
upgrade vehicle service
and
within an upgrade step two i uh the
server will
handle the trigger is marked as check
precondition
or upgrade basically within check
precondition triggers you will put the
methods which validates that the current
states of your data into the database is
ready for upgrade step two
in the upgrade triggers you will put the
code which moves the data from the
upgrade table to
to the new to the new destination
tables or reinitializes the the new
tables so my function is of type upgrade
since i'm moving data from
my upgrade table and i have already
prepared the code for
for this so i'm basically iterating
through the upgrade table
records and inserting them into the
vehicle service records and in the end
good practice i will uh i'm deleting the
records from my upgrade vehicle table
i will save my changes
i need to add the variables
so i'm using the upgrade vehicle table
as my source of data
the vehicle service table as destination
and also an index
entry number for my vehicle service
table
all fine
let me now invoke upgrade step two so
the data upgrade step
i will do this from seaside uh invoking
the tools data upgrade start menu
i'm testing if my upgrade code works
super fast i only need to run one
message
so i will run now a vehicle service
table
all fine
my upgrade vehicle is empty good
and since i'm in this view i need to
remember that i have another requirement
to implement
uh this is the deletion of the
description field which is not used
anymore
from the vehicle fuel
table
so i will quickly synchronize the schema
with force as you saw
i
need to remember this when i'm checking
in my code
and i have to update also the pages but
i will do this very quickly
time is ticking
compile
okay
now i'm going back to rtc let's see how
my new pages looks like perfect so i
have here the general information of a
vehicle
the service fields have been extracted
as lines here and the fuel consumption
does not contain description
okay it looks like i'm ready to
check in this change list and our update
is ready
so i need to export my objects which i
have modified
from my database i have a script which
does this using the new nav development
tools
i will do this fast and quickly
okay
so
this is how my changes look like the
script is
removing the date and time uh values and
setting a new version list to the
objects which i'm
updating
and yeah my my work is done
so let's have a recap
of
the mechanics that we have exercised so
far
i was doing changes from my development
environment where i was basically
modifying the app
and at schema synchronization time the
nav server detects uh the changes that
i've made to the tables and for each
table id which i have changed
it records it into the table sync setup
virtual table
after all after it detects all the
modification
it looks at and scans into the database
if it can find any upgrade code unit
and from this upgrade code units that it
can find it looks into the functions
which i have defined as table thing
setup
because here is where my upgrade
instructions are
and then it goes upgrade instruction by
a great instruction and fills them in
into the upgrade into the table think
setup view to a table
at the end of the scan
it will know how to synchronize the
schema changes for
and how to handle the data from each
table which
i have modified
so important thing to remember is the
upgrade code unit which is the new type
of upgrade code using enough 2015
because this is the placeholder where
you run both upgrade step one and
upgrade step two and
both
such upgrade steps are running in the
newest version in the version that you
have modified
upgrade step one is currently outsourced
to the nav server so we call the upgrade
process actually as a single step
because the schema synchronization is
handled by the server and we only need
to provide an upgrade instruction to the
server how we want to handle the data
and within an upgrade instruction you
have the specialized triggers that you
can define so table thing setup makes
sense during upgrade step one schema
synchronization this is the placeholder
for your upgrade instruction
check preconditions will
run the methods which check that your
database is ready for data migration for
running upgrade methods
and within upgrade methods you are going
to
write and run your custom code to
move the data from the upgrade table to
the new destination table
so hey boss how are you doing i'm great
i have
checked in my code for the vehicle
management add-on i think we're ready to
release the new update for our red one
all right that's good news i think our
customer will be really happy with these
improvements and also with the fixes we
got from microsoft with the latest
cognitive update right
we did apply it right no no actually i
haven't done this i haven't seen okay
well no problem i heard that with the
new merge tools it's really easy to
apply such an update so let's
show how we can do this
switch to my screen
so this morning like every morning i
checked the nav team blog my favorite
website
to see if there was any news
and yes there was a new update was
released and in the knowledge
base article there was a lot of
improvements listed
for the application so i'd like to bring
our vehicle management solution with the
new features up to this update
and the new merge tooling for microsoft
uses the concept of a three-way merge
and it makes this a lot easier than
before i start doing this i want to
bring up this slide again it should be a
familiar slide by now
and it explains the concept of three
merge i just want to go through it one
more time
a three-way merge
is a merge that's based on three inputs
there's one
shared base and then there's two
versions that are derived from that
independently
so in this example there's a shared base
and our terminology is we call this the
original object
and it is changed in uh one derived
version that is the modified version and
we calculate the difference between the
original and the modified version
so in this case it turns out that there
was one field added it was added after
the phone number field and we record
this information in a delta object
then there's another modified version
and we call this the or another derived
version we call this the target version
and this version actually
merged the first name and last name
field into a name field so now we have
two changed versions
and we will try to apply the the delta
that we calculated between original and
modified to the target version
and this will give us the the result
which is the output um even though the
the first name and last name field
changed in the target version
and we added an email field at roughly
the same place in the modified version
we could we will still be able to merge
because this emerges not based on text
but based on the model that we
calculate from from these objects
so in the context of applying a
cumulative update the picture looks like
this
our vehicle management solution is based
on of 2015 rtm
so is the cumulative update that comes
from microsoft so these are the two
derived versions
in this
example i will
consider the our vehicle management
solution the target version in which we
want to merge the changes that we got
from microsoft with the cumulative
update
there's no uh like definitive rule on
you know what should go in target and
what should go modified it
it can be different from merge to merge
which way you would get the best results
it depends on what has changed and how
many changes there are
anyways the resulting version would then
be our vehicle management solution but
now updated to the cognitive update
released by
microsoft so to start doing this i will
open up
the development show
where i have all these commandlets
available
so
to do this three-way merge we need these
three inputs so one of the inputs is the
rtm source code
i have a database here
that i will use to
gather the rtm code
and when i use the new
development command for this that we
that is basically wrapping the fin
sql.xt that we had before
and i export from the rtm database into
a file and i name it rtm.text
and i will let it do that
this will take a little while
so i will take the opportunity to have a
look at the
at the archive that you can get from
microsoft that contains the cumulative
update
and when you extract it you get one
another archive that contains a full dvd
with the updated version but there's
also a separate folder that contains
everything that has changed
in the application
so there's a
change log
and it contains before and after
fragments of all the changes that were
made
in this case there were somewhere in the
between 400 and 500 changes made
there's also this file
that contains all the objects that were
changed
133 objects for this update
so this is still running so i'll just
open up another one
so what i also need is is the source
code from the cumulative update
and i'd like to use that as separate
files because that works a little bit
easier when merging
and i want to do the same for the rtm
source code so i will create two folders
for this
one named rtm and one named cumulative
update one
and now i will apply the split
commandlet that we've added
and i will
point to the file that i've downloaded
from microsoft containing all the
objects this text file
and i will
export that or split that into this
cu1 folder i just created
let's see is this done okay this one
finished so now i have a text file
containing all the rtm objects
i split that one also pretty much the
same
rtm.text
into
the rtm folder
i'll use this switch because i know it's
a little bit faster
for the sake of the demo the difference
between using this switch or not is that
if you don't use it we analyze all the
source code and then we will also break
if there's
things that are not valid syntax in this
case we will just
cut between all the objects and output
them into separate files
so what do we have now let's let's
inspect our
my working folder
so now i have a folder with the 133
objects from the cognitive update
i have a folder containing 4000
something obx from the rtm source code
and i have a folder this is our folder
with vehicle management
and that contains the source code
for our solution
and actually anka made a few changes so
and i almost forgot to to pull her
changes
we're using version control i assume
we all do right
who's using version control
okay it's maybe a little bit too many to
to give t-shirts for but
okay let's let's uh
so i will just pull her to see if
there's any changes made
ah so she made a few changes now i have
my
files updated here
so now i have i have all the inputs now
but
um
there's a small issue and i want to
illustrate that with this slide
so
we talked a little bit about what
happens when you when you have changes
in an object and then you merge that and
how these changes are are then
interpreted but you can also look at
changes at a higher level so if you have
a set of objects there might be objects
that are deleted or added and those are
also changes that you need to take into
account
for example
here you see okay we have an original
object
a couple of fields and in target it has
changed
but in modified our set of modified
objects this object is not present
so now the question is what should
happen
anybody any idea what should happen here
no
well
actually this will be a conflict because
for the tool there's no way to resolve
this without losing information
either
you you lose the information of the fact
that this object was deleted if you
interpret it as a deletion or when we
have an output without this object then
we lose the information about the change
that was made in target
so given this we know that if i have a
folder that contains only the objects
that were changed like my folder with
cumulative update one
and i have a folder that contains all my
objects that i have today and contains a
lot of customizations that then i would
get a conflict for each object that i've
changed and that does not it was not
changed by the cumulative update
so there's there's two ways around this
either you make sure that uh the folder
that contains your obx from the
cognitive update is actually a folder
that contains also all the objects that
were not changed
that's one way to do it the other way is
to
do it the other way around and to look
at your target and original folders and
filter those to only contain the objects
that were changed in the cumulative
update
i would choose the to do the ladder so
in powershell this is relatively easy i
can list all the objects from my
cumulative one folder and i can iterate
over them using for each object
and then for each of them
i
copy an item
with the same name so dollar underscore
refers to here for to the object that
we're processing here
and i copy it to
oops now i forgot to create the target
folder
so let me just do that in between
so i want to create a folder like a
version of the rtm folder that contains
only the objects that were changed by
the update
so and it will serve as my target folder
so i will
name it or as my original folder i will
name it rtm underscore original
and i would need to have the same for my
vehicle management objects
so i create two folders so let's get
back to this one
so now i have a set of filtered objects
in my rtm underscore o folder
and now i can do the same but then like
the short version
using some aliases percent uh it means
for each
uh copy
for my vehicle management folder an
object with the same name into
my vehicle management target folder
so now now we're really done now i have
everything in place to start the merge
so let's issue this merge command it
takes the original path
now this is my rtm underscore original
folder
i have
a modified folder which was the
primitive update
i have a target folder
and this is my vehicle management the
filtered version of that
and now i again realize that i forgot to
create a result folder so let's do that
quickly in between
so now it's reading from each of the
three input folders those 133 objects
that were still in there
comparing
original with modified
and then taking the difference and then
applying that to my target to my vehicle
management objects
so the result of applying this
cumulative update you see like a summary
here so there were 133 application
objects that we merged
they contained 457 changes
and then there were three changes that
could not be applied automatically
so let's have a look at what the result
folder looks like
so this is the result folder
um
and i want to talk a little bit about
this for example so here you see an
object that couldn't be merged
automatically
and you get one file that contains
the object as it was in target
with all the changes from modified
applied as far as they could be applied
without a conflict
and you also get a conflict file and
which is basically
the delta between original and modified
minus the changes that could be applied
so it's only the changes that could not
be applied are still listed here
so i can open it up in this case to see
what's in there
so this is an example of a code
modification change so
and the code modification changed a
trigger which was with the name code
in uh the target code unit 442
and the actual conflict and this is
interesting it's not listed here but it
says that the conflict is inlined in the
source
so for these type of conflicts we can
actually
take the original modified and target
code and
add that to the target resulting object
so this is the resulting object and now
we can look for a marker like this
and what you see here is that
in this section of the code where there
was a conflict we have all the three
versions available so in original we
were referring to some
table field
then in the modify we changed that into
some local variable
and actually we in our vehicle
management solution we added these two
additional fields
so now you can can with this information
you can start resolving this
you could do it here but there's a
better way and we will get back to that
later
um
because there's something else i want to
show you and it was also mentioned
in the session by mark
he called it i think something like the
ugly of uh code merch
and that's the the version list so let's
compare
uh my result think objects with the ones
that i had our vehicle management
objects before
i'm using this one of my favorite tools
kdiff it's free
so it lists uh it does a comparison of
all the objects now this is a way for me
to see okay what was actually immersed
in
let's take one example
so on the left
you see my code and on the right you see
the resulting code after applying the
update some updates were applied here
but let's take it to the interesting
part
and that's the the version list here
and it actually didn't change
and that's of course not good you could
call that ugly
we have a few options actually on the
commander to handle version lists but
they're not very extensive so let me
show them so there's a version list
parameter
and you can either use it to clear the
version list so then in your resulting
set of objects all the version lists
would be empty
and this might be useful if you want if
you have a process in which you
uh only apply the version list you know
like at the later stage when you release
for instance this is what we we do
internally for at microsoft
then there's an option uh to take just
take the version list from modified and
then there's an option to take the
version list as it was in target
and this is what happened here
so i admit that in most cases this is
not good enough
um
so what actually what do we want to
happen in our case
i have a slide for that
so this this table is
kind of all the possibilities for this
um and what should happen
now do some
fancy powerpoint stuff
so
um but
this applies this full table applies if
you have all the objects in all three
folders
but since we only you know we filtered
all the other folders to only contain
the objects that were changed from the
update
so that means that we are not really
concerned with
this
and this one
so the three three uh lines that are
left
there's another one that we're not
really concerned with
because this one says that um
you know basically it means that we got
an object from microsoft
and it modifies an object that we we
added so that is not of course not
possible so so this one is also not
interesting so there's just
um two lines remaining here two cases
uh one where we get an update from
microsoft and it updates an object that
we hadn't touched
and then we should just keep the version
take the version from uh from from the
cumulative update and the other cases
where we had touched the object that was
modified by the update
and then we should uh you know combine
this in a new way to get the new version
list
so
the way we support this and you need to
do a little bit of scripting yourself uh
because
uh we can't really predict all the
different ways you can work with version
lists and you want to use them and it's
very difficult
but you can use the output of the merge
command for this
so i will get back to this merge command
a new force now to overwrite the results
again but
i would not i would assign the result to
a variable like this
and now there's a lot more information
that you get from that so the variable
gives you all the the merges that
happened
we can look a little bit more into
detail because each
element in this set of of merge results
is actually a pretty rich object so
let's let's inspect one of them
so i just select the first one
so now i have my merge info it's like
this but i can inspect it further using
this get members
and what we see now is that this object
actually contains information about the
target object for this merge resulting
object the original object and the
modified object so let's look a little
further if i
query for the target object this is
information about that file and the
object it contained and the version list
all the object properties are listed
here too so now i can i could do like
this
so now
you know i know that from the output of
the merge command i basically have
access to all three version lists for
all three inputs and if if if i have
some kind of
you know script that can turn those
three inputs into what i want in the
target
then we have other commands lists to uh
to make that happen
so there is a small script that can do
it for this case and i built it before
so it's a basically a three-line script
it takes one of these merge info objects
and then
it splits the target version list on the
comma to get each of the segments
then it replaces the first part of that
with the one that we got from microsoft
and finally we put it back together
again on a comma and return it
so if i
pull this into my session
and i apply this to our merge info
object
then this is you know now the first part
is updated so now i can apply this to
all
my resulting objects
and
we use the percent and you now know that
this is for each
and then we have the command let's set
nav application object property
i want to set it on
the resulting object
and what do i want to set it to well i
want to apply this function that i
created
like this
so now it's it's going through all the
files in the result folder applies my
function that calculates the desired
version list and writes the file back
out
so it should only take a couple of
seconds
and then we have another commander to to
now inspect that again called get nav
application property
give it a result folder let's just have
a look at the version list
so you see this is actually what the one
should have been in the first place
so okay now import
done merging
i think let's import
uh we use the commandlet for this
it takes
wait we first want to join the result in
a single file we use the join commandlet
for that
it takes a folder file spec
and then we output to a file we named it
merge.txt
and then in the next one we import it
into i have my original
vehicle management database here
containing the object before i pulled
anka's changes
that is the database name
so now it is concatenating basically all
the objects from my result folder
into one file and taking that one and
importing it
it shouldn't take long
so now i compile it
also a new commandlet very easy to use
it will compile any object
in the given database that is not
compiled
and i will also tell it not to
synchronize any schema changes just to
make it a little bit
quicker so anybody an idea what should
happen now what will happen
maybe you remember that we had a couple
of conflicts so
did we forget them or if you forget them
it shouldn't really be a problem because
you will be warned
let's see if we get some red text here
let me open up
the development environment in the
meantime right
so these these were the three conflicts
that we had and they all failed to
compile
actually they were all co-conflicts that
were inlined
so i will go to my development
environment
filter on not compiled so there's three
objects here so let's have a look the
compiler will bring me to the place
where i need to do something so even
though you know we inline this and you
can import it
we made it so that it doesn't compile so
you know you're always warned that hey
you forgot something here
so okay remember what happened here we
replaced this line
was replaced by microsoft with this line
and we added these two so this gives me
a way to resolve this
i just want to keep the line we got from
microsoft and my two additional lines
like this
and now i can save it so this is a lot
safer than doing it in notepad
let's look at the next one oh this is
very similar i will resolve it the same
way
the final one
okay this looks a little bit more
complicated but let's not panic
these
couple of lines were replaced with these
lines in the update
but actually we put a condition around
them
so i would just uh
take the ones that were changed to and
put those in the condition
maybe we should have do some testing as
well but
let's just not do it now
okay so clean up
done
so um yeah i'm wrapping up now
first
let's export this in a fork that i will
give to my colleague later
so that she can update our customer
it takes the database name and font name
and i will put this one on on our
build drop share
so but before i hand over let's do a
quick
summary
and there's a cool way to do that with
powershell
i'll just grab the the history what we
just did
and i'll take the command line
and then i copy it here so then we can
have a look at it
so first we started out with preparing
our all the source code you know
grabbing the source from rtm we don't
see that part here because we did it in
another session so that's basically this
part
so then we synced let's skip that so
then the next step we filtered it to
only contain the objects that we got
from that were included in the update
that so that part happens here
next we did the actual merge this is
this part
uh well we did it twice we normally
wouldn't do that
and then we played around a little bit
with the merge info
and then we updated the version list
based on this new version list function
and then we looked at it and then
finally we joined the objects together
and imported them
compiled them went into seaside to
resolve any conflicts and finally we
exported the fob
and i think ida will take over from from
here
okay beth so the fob is ready
let me switch
okay i can see the fob in the drop
it's number one
oh we don't have we don't have the
picture
bear with me for a moment
okay
i think i have the picture hopefully
did you switch to one
that's number one
okay it's every time you switch
maybe we should try that again okay
no no
i'm waiting to
the fob to get trapped in my drop folder
i guess
it's taking a bite
it was working
it's right now
duplicates
okay
perfect
[Applause]
so maybe i duplicated
fantastic it take a while that was a
yeah
but
let me check if i have the fob
okay
so now i have my customer database and
i'm going to import the fob
yeah it's right there it takes a while
to get to there but it is here
and i import it
so this is actually
my biggest customer
and
yeah of course i need to replace all
and
i have seven companies within this
database that represent seven branches
that unconvention for my customer which
is running a car rental system
and right now i
i get into the import for
synchronization dialogue and the reason
is as ankar demonstrated i have a table
in my fob
so i have the synchronization option
that i can choose to validate and i
i will choose now with validation
because i want to make sure that there
is no destructive changes in my fob or
if there is any it has been handled with
upgrade code unit
it will take a while
so right now all my objects are getting
imported
and the validation will happen at the
end
73 percent 82 percent
and
yes done
of course i would like to validate now
just to make sure
so think is in progress
oh oh
seems there is an issue
let's let me see what is the issue let
me zoom in
okay
it seems like uh
when
there is something that
there is a field or something that has
been deleted so
it's i'm instructed to go to the
publisher and see the details and see
what is happening okay
that's exactly what i would do
let me close the magnifier
and i will go to the powershell as
instructed
i will run
think nav tenant
and my server instance is
and emote
check only just see
what is going on
okay it seems that everything is fine
no problem let me try again
okay
yeah i can see that i think uncle when
you wanted to
remove the description field you forget
to actually think on the fly
and
of course it doesn't matter because that
was
a field that we wanted to get rid of
and
the only thing is right now nav server
doesn't know how to handle that field
and i need to
add a line
to my table sync setup in order to
instruct server how to handle that
change
okay the code is already ready for me
it's just a one-liner
fine
okay let me close this and go to my
upgrade code unit
so you can see here that i have to
upgrade code unit one of them is another
one on the cost management that another
the person has prepared as part of the
updates and another one is vehicle
upgrade code unit that onco just
prepared
okay well i go here
design
and i will just paste this line
and since i'm not going to copy or move
any data because i just want to remove
the fill
then i don't need any upgrade table
so i'm going to remove that
and just table id would be zero fine
and then the mode is forced
because i want to force
the deletion
and hope that will take care of it
okay
yes compiled very well
and for many of you that i know you are
like hardcore seaside lovers we have ads
synchronization
option from the tools menu enough 2015
so you don't need to switch to
powershell if you want to run a
synchronization check
i go sync schemas for all the tables and
here i will run with validation
just make sure that everything was fine
yes i'm going to run the validation see
if i'm ready for my data upgrade
okay it is thinking
79 percent
250 out of 500 100
fantastic
so it seems like everything is going
fine
we just have a small little mistake from
anka that i catch it on my phone import
that was very good
and
now i'm going to
start to run my data upgrade so let's
get it started you know that in nav 2015
we have added
a menu item to the tools menu that calls
the data upgrade
so i go to the data upgrade
i say start
a confirmation do i really like to start
the upgrade process yes of course that
is the whole reason i am here
and you can see that i have a small
dialogue with different options on how
to run the upgrade
and
what is happening really when i
call this function
is the nav server goes and look into the
database
finds all the code units marked as
upgrade upgrade code units as anka
demonstrated and then within those finds
all check precondition functions and
upgrade functions and execute them
okay that's fine but the magic happens
here actually because i have
different execution mode i can run my
upgrades in different ways enough 2015.
one of that ways is the good old way the
serial way that we all know and familiar
with another way is parallel but i just
like to start with cereal
okay
i kick this in
and my data upgrade dialog box shows the
estate it is in progress
yes
and i think this is going to take a
while so let's see exactly what is
happening right now here
and
i have seven companies so
the nav server goes fine finds all
upgrade control
record units in each company one by one
then
within that finds the
functions that are marked as check
precondition
first run them if the run was successful
then goes and runs the rest of functions
that are marked as upgrade and iterates
that through
all the companies so here actually now
i'm running 42 upgrade methods because
in one of my upgrades code units the
cost management i had six
and in vehicle management i had
one
sorry i had one and in my cost
management i had five so i had overall
six functions upgrade functions and
right now i have seven companies so
they're going to iterate through 42
times
76 percent and actually let me
uh show you what happens now here
and
how my system is kind of utilizing the
resources
and you can see here that
it's between yeah 60 65 percent and now
my upgrade communicated so the cpu usage
was around 32
memory was average i was not utilizing
all my resources in my machine
okay let's get back
my upgrade process is completed but i
think now you wonder how you can see the
details of the upgrade process
and what happens really behind the scene
to get a detailed overview i need to
use the powershell so let me switch to
my favorites integrated scripting
environment
great
and i'm going to you can see here that i
have uploaded nav admin tools that
comes with nav 2015 and through that you
can get access to all powershell
uh commandlets that supports later
uh data upgrade so i'm going to call get
nav data upgrade and
what really happens when
upgrades is executed the state of
upgrade is saved in memory in the server
instant that running the upgrade
so i can query that server instance here
is dynamics nav 80 in my example and get
a detailed state
of how my upgrade has been executed and
actually i can have different views of
that i can get a grid view or i can run
it in the table i love the great view so
let's move with that isn't that
beautiful
so
look at here i have uh
i think the first thing you can must
notice that each upgrade function is
running through the session and all my
upgrade function
has been running through different
companies representing different cities
that i have
branches there
very well
but
there is one thing obvious here that
all these upgrade functions on are
running on one session that means if you
look at the start time
here they start at a specific time and
then it is completed then the next one
starts so it is a one-to-one
relationship i go to iterate through
each company one by one and run this
upgrade and um i was lucky today i had
no errors and everything is completed in
a serial fashion and you can see that it
take a bit of time
but that's not all it okay
um actually right now i want to show you
something else
of new capability
and for that i need to restore
and first i need to actually close my
development environment
that would be great if i do that
okay
so i need to restore my database
to the
state before execution of upgrade
toolkit in order to be able to
demonstrate that so bear with me for a
moment
and now we are going to explore the
world of parallel execution and see what
that really means
yeah seems like everything is ready
so i can open my development environment
again
perfect
and
this time
i'm going to tools menu my new favorite
option data upgrade start and this time
yes of course i'm going to keep it as
default so
enough 2015 we run data upgrade by
default in parallel
what does that really mean
let's see
okay
i just want you notice how fast this is
running and look at the use of my
resources it's hundred percent i am
utilizing all my resources in my machine
to run the upgrade right now
okay 50 percent
59 percent normally it
takes a little while to kick in but then
it kicks in 78 percent
83 percent
and 100 percent i just run 42 upgrade
function
in seven companies in parallel
okay
but i love to see the detailed state now
and see really what happened behind the
scenes
i get back to my favorite scripting
environments
again i would like to see the grid view
get enough data upgrade
yes
okay there are a few things to pay
attention here
look at the session ids
in serial execution they were the same
they are different here that means each
upgrade function
owns its own system session
and if you look at a start time all of
them is started at the same time so
upgrade functions are running in
parallel
with each other and in parallel across
the company all at the same time and i
really think this is amazing because
imagine it's like you have 42 employees
sitting doing upgrades for you across
seven
companies simultaneously and you're
utilizing all the resources on your
machine and as you go larger scale and
you have long freight function you can
imagine what does that really means
so this is one of the capabilities we
have introduced enough 2015 the ability
to run upgrade across companies in
parallel
but that was not all it so i'm going to
close this because i think one of the
questions that might come right now in
your mind
close my development environment again
because i need to restore my database
again
yes completed
i think the question comes in mind now
okay this was straightforward but what
happens if there was any error and any
failure doesn't the parallel execution
mess that up
let's see so in order to do that i need
to
um have like some kind of wrong data in
order to make my upgrade fail so i'm
going to kind of make a synthetic
failure now
here okay something happened
okay maybe i should just
zoom out
zoom in a bit more
perfect okay
zoom in one more time and then we are
fine
so
i am going to
open the windows client
in cost management upgrade could one of
the upgrade toolkits the upgrade
functions that i have is updating a
sales invoice
and it is dealing with a specific
customer so all i want to do here is i
go to my customer list
and find that customer customer 20 000
and plug this customer so when my sales
invoice calls to this and wants to
update then it cannot because the
customer is blocked
okay
i just set it to all
okay and i close my windows client
and now i'm going to
get back
to the development environment
this time
tools
data upgrade
start
yes of course
in parallel but you can see i have and
some other options
continue on error
let me just check that and see what does
that really mean okay
so my up
oh you can see that i have error of
course i produce an error now and i have
an error but does my upgrade is continue
i i actually because i choose the
continue on error you will see that my
data upgrade process will resume and
continue
even though there is an error and
you have two options in this case one
option is just
go by if default stop at failure or
choose continue on error then the
functions that can execute successfully
they will execute successfully and the
ones that fail they just fail
okay
you can see i'm on 97 percent and the
estate is suspended
because i had an error
so let me see
i can zoom in
and you can see a bit more clearly
so an error happened during the data
upgrade and in order i get a list of
error i need to go to the powershell
that is exactly what i will do
and get back to my very favorite and
most used command
okay look at this
so all my upgrade functions were
completed
and the only one was failed was the one
in company bruce must correct me if i'm
pronouncing it right
okay that one
that company so that was the only one
that failed and you can see the error
because the customer was blocked and the
rest were completed
so
now what should i do
okay
let me see i'm going to fix this error
so i go back to windows client
to my customer list
unblock my customer
get back to development environment
close this
tools
data upgrade and here i have another
option i have resume
so i can actually resume
only the upgrade function that failed
i'm going to choose that
and you see here i have even more option
either i can choose to resume
all the upgrade functions that they will
fail or right now is pending or i can
even customize i can resume and a
specific upgrade code unit in a specific
function and within a specific company
this as can be very much handy that if
you have a long list of errors and there
are some that are easy you just want to
fix so and then
move on with the rest
okay in my case i choose resume
yes upgrade is in progress
perfect
completed
quickly it was just one function
now i get back again
to my very favorite command let's
and look here 100 percent done all
completed and actually if i want to
sort by the start time here
if i go up
you can see that
only the upgrade sales invoice
is started in a later time when i
resumed and the rest were already
completed they remained completed
so this is uh actually focusing on the
two capabilities that we have on uh
in
enough 2015.
you don't need to restart your upgrade
after
running
hours and hours of lengthy upgrade
process and restart everything the ones
that are completed are completed and
then you can just restart the ones that
are failing and you fixed
okay
so
that was it but actually
one more point to mention and maybe i
can zoom in a little bit more then this
is more obvious
one more time
great
so
nav 2015 as i mentioned before comes
with complete support of uh
powershell commandlets for data upgrade
functions so you can start your
data upgrades in different execution
modes parallel or serial you can also
use the flag continuum error the ones
that i just use
you can also get the progress just in
the actually in the powershell
environment you get a progress part of
your data upgrade every time you call
git nav data upgrade or you can have
more detailed listed that we use it
frequently have it in a format table
or in a grid view that you just saw you
can also resume the data upgrade and
stop the data upgrade
and okay i think
almost done and i would like to recap
what i just demoed
so we had two execution modes serial
and we actually decided to
preserve the old style upgrade execution
but also we introduced a new parallel
way that significantly optimize the
performance of upgrade as you can see
and another thing to notice is data
upgrade is a
asynchronous process so you can start it
also for multiple financing
parallels so imagine having multiple
tenants multiple companies and running
the data upgrade all at one time in
parallel
but there is another thing that i need
to mention so if you want to really
utilize running the data upgrade
functions in parallel in their own
session
you need to design the functions in a
way that they are independent they are
not logging each other and they are not
expecting any particular execution order
but of course i understand it might be
exceptions for example very very um
popular kind of example can be the sales
header and you want to upgrade your
sales header before your sales line so
what you do in such cases you can just
write an upgrade sales order a header
function but just mark it as normal it
shouldn't be marked as
upgrade also upgrade sales line mark it
as normal and then you call that within
a upgrade function exactly as my example
in the order you want so it will execute
in order because nav server only will
look for the code units that marked as
upgrade and run them
and we also explored the resume
option the resume can resume capability
so when an error happens the functions
that are completed they are remaining
completed the functions that
are failed and the ones that were in
progress they roll back and then
they become pending and you have the
opportunity fixed
fix those functions and then rerun your
data upgrade without running the upgrade
the functions that were completed
you can also choose to restart a
particular function as i show you from a
particular code unit for a particular
company
and of course
we had a continuing error option that if
the error happens then remaining
function are executed
if they can successfully successfully
until the process is complete exactly as
demonstrated here and then you can only
run the
failing upgrade functions
that was exactly what i just showed you
as a demo
okay so we are
almost at the end of
of upgrades
for of car rental company
i think everything
went quite as smoothly and rather fast
and let's see
what's uh
nav 2015
data upgrades brings to the table so if
i want to overlap of first of all it
seriously simplifies the upgrade
environments because all the s
steps are performed by the latest
version of the product
you don't need to have
multiple instances of nsd and all that
stuff that we all know and we don't like
that much
so the upgrade period performance has
increased significantly you can run in
parallel across the company utilizing
all your resources
in the machine
and um and we have kind of delegated
this step one upgrade data upgrade to be
run by server as a result the amount of
code that need to be written is reduced
significantly
and of course both in the data upgrade
and code upgrade the big improvement is
it has minimized the number of manual
action that you need to perform so it
would be much much less error pro
we just see in the keynote what happens
if you have you know long list of manual
things that you need to do there would
be always an error
and of course we have a better
troubleshooting capabilities
for for example when you want to collect
and address all the
errors and then you can rerun just that
arrows that just make it much much nicer
for troubleshooting by the way now that
i mentioned that i forget something one
thing that you can use the serial
execution for is for debugging you can
easily run the upgrade in
serial activate your debugger and run it
in serial that would be possible in
parallel now that i was talking about
troubleshooting
and of course
it is not like we completely reinvent
and
devel
the design concept is very familiar for
you we have the upgrade tables or buffer
tables we have the upgrade functions
and of course we have the end-to-end
powershell aesthetic we can just do
everything that me and anka did here
end-to-end automated so it is fully
automatable and also for code upgrade we
have it's fully scriptable we have a lot
of scripts and you can do a
good amount of automation in that as
well
but of course the last and not least we
are providing the direct upgrade path
for your customers
from three versions from 2009
2013 and 2013 r2 you can find the 2013
and 2013 r2 merge upgrade toolkit in of
2015 dvd
and just last week we shipped with
cumulative update one the merge upgrade
toolkit for 2009 because we know many of
customers running on 2009 and this will
really facilitate for them to do the
data upgrades faster
and also for you it makes your job much
easier it will it took us a while to
actually make that
okay
thank you very much for your attention
today i think we did a decent job and
probably of development lead in the
yeah enough car rental
increase
solution is
happy
i hope so i hope the customer is happy
and they received a new add-in
so with that
please let me know if there is any
questions
[Applause]
yes please
just bring your microphone over here it
should be mike
yeah uh i would like to ask if there are
some building functions
that recognize
programmers can use to recognize if data
upgrade was already done or it's on on
side of programmer to to mark somehow
that this script was already executed
i cannot do that yeah so um for the
schema synchronization for example we
have the tenant states
uh which
tells you if you have some schema
synchronization pending
uh if you have save your changes with
option later this means your schema sync
is pending so your get nav tenant
commandlet will show you the that uh
your tenant is not
uh is in schema pending if you don't
have any schema changes pending then
your tenant will be operational
if you have
uh had an error in your schema
synchronization then your tenant will be
in operation with a
thing failure so uh for the upgrade step
one you can see what is the status by
calling get nav tenant and uh for
upgrade step two namely the data upgrade
uh either just demonstrated the get data
upgrade commanded
which also provides a detailed state
only the errors and
yeah you can you can call it for example
if you haven't called the data upgrade
before
um
then
get data upgrade won't show um
anything it will be empty yeah except
yeah
hello um i have a question about the
licensing if you work in parallel how
many licenses are consumed or it's only
one you need
by running in parallel um
the sessions that uh
uh you have seen those are background
sessions so um
uh they are system sessions so they are
not actually calculated their server
system sessions they are not
part of the limit for the customer
license and we have verified we provide
the full capability for customers to be
able just to run the upgrade
code so with customer license you can
run the upgrade scope no problem
in parallel or serial
doesn't matter
after upgrade should we delete upgrade
code units
yes that is a
of course that is a recommended practice
and
uh i think connor it was you we were
talking yesterday you have just
uh posted something in your blog some uh
and
uh interesting new
ways of doing that automatically but
really at the moment we don't do that
automatically
regarding the merge
tools how are
inline comments on the code handled are
they
do they give conflicts or are they
ignored or
like like you have an if setting and in
the end of the if line you have a
comment
a comment the
the trigger code is treated as text
so
i mean they're not ignored they're part
of the text and and you could get
conflicts on them yes
hello
uh according to the performance if i run
upgrade
without show progress is it going to be
faster and if it run it from the power
shell is it going to be faster
the data upgrade to me yeah the data
grid and there would be no difference
no difference no it would be as fast
in both ways because we are running uh
through the same we are calling the same
code
okay okay but uh because because of uh
of progress bar
if we don't have it let's say in the
reports the reports are faster so is it
same here or not
i'm not a hundred percent i don't want
to verify that hundred percent but to my
knowledge there won't be any significant
difference okay another question please
uh if
is it every every time a finish with
some function is it do it commit or not
would you please repeat the question
every time when a function is finished
is it do it a commit to the database
as asking because if we have a very
large database with very large tables
is it every time we finish with some
tables it do it the commit
okay that's because of performance of
the secure server
okay but that the functions every time
you commit on the
fly so every time you do that you will
commit we need to go to the database yes
okay so this is exactly like actually
before
when you were putting commit in upgrade
test uh toolkit step one then it was
committed to the database so we kind of
simulate this
some more questions here
do we have to
add permissions to the upgrade code unit
for example
changing entries
i can answer this
you don't have to
yes so the answer is yes you need to add
the permissions within your upgrade code
unit if you have there an upgrade method
which modifies the table that you have
specified
and while testing that
we are able to run
upgrade using the customer license we
have actually added the permissions for
those specific tables that
uh are treated differently
within the customer license
i have a question for bus um if you do
the
merge
then it seems that you recognize all the
fields the fields and also the
properties
is that right yes that's correct
so the the conflict i showed was you
know
a type of conflict for for the code in
triggers
but there's also conflicts when you
change a property or insert a property
and and they are treated differently so
there will be different type of change
so now you saw a code modification but
then you could have like a property
insertion or a property modification
so they're treated separate
one last question do you have the
properties of this version also older
versions in
the mechanism or only the latest
properties so um i think
um
we have probably most of the properties
back to 2009
except for the object types that were
retired like forms
so yeah it should be
the properties that you have in code
that that is accepted by 2009 the tool
should be able to accept that as well
there's a question
uh hi a question about the automated
merge process uh how good is it
when it regards to rdlc changes will it
do the same thing as it does for the
code and for the table fields will it do
anything for the rdlc or is this that
still a manual process
for nav 2015
rtm it was a manual process
but
of course if turbine here from reporting
team that can cover that in more detail
but for cumulative updates we have also
added that to upgrade process so it has
been automated but i'm not aware of the
full details you can catch it up with
turban but we have that in
cumulative object that was released last
week
thank you another question uh there are
a couple of comments in other sessions
over the last two days
about whether microsoft is likely to
allow the partners to actually have
access to all of the fields with their
licenses
because it obviously
makes a mess of the automated process if
you can't create the fields within the
protected range
below 50 000 is that a likely thing to
happen
i can't answer that question now but
we are very much aware of the issue mark
raised that concern also last night with
me had working dinner and some other
partners as well so we discussed about
that and
we take that feedback
thank you very much
hello
after step two when you do the data
upgrade is temporary tables deleted
excuse me the template the upgrade uh
table that i have used is just a normal
table
okay so you have to delete it manually
after uh yeah yes
and
what happens if you do not delete the
code unit
of the upgrade and you import like one
report afterwards
um
okay so we actually recommend to delete
your upgrade code unit because
the actual dangerous uh
code there is the tables in the top code
so um
the next time
for for your specific question
if i leave my upgrade code there and
then i'm importing a report this doesn't
actually matter
if i'm making changes to
uh
tables which are not in my table things
setup function this doesn't matter
either but if i'm changing the second
time the table which is in my table
think setup function
then
it will
my change will succeed or depends on the
case but the upgrade instruction still
still is valid uh for for the table but
the upgrade instruction is known for my
current change so the next time that i
will modify
the same table that is in with my
upgrade instruction then uh it will it
will the server will use what it can
find
so that's why um
it's important to to delete upgrade code
yeah that is a recommendation to
completely clean up after the upgrades
process once you have completed the
other schema thing or the data and
everything yes
when is the check preconditions executed
it's in the step two
it is on the step two and um of course
it is executed first so what happens uh
server goes find the upgrade code unit
then finds the functions that are marked
as check pre-condition execute them
first exactly like it was before and
then if that was completed successfully
then goes within that code unit and find
the upgrade functions
and you wrote that it is a tool from
2009 nav is it from classic client also
or it's only from rtc client
yeah it's a 60sp1
and 60r2 but
with the sql database
no but if you are using classic client
with forms and data ports
so you have the upgrade tool for nav
2009 r2
and if the customer is using forms will
it upgrade
um
yeah so we have the code merge
it will not upgrade the forms because we
cannot bring the forms over to a later
version
and for a data upgrade i think it
doesn't matter no it really doesn't
matter
okay thank you because it looks into the
tables
i have a question um how you're going to
enhance this toolkit because um we are
the add-on
creator we have the problem
you send the customer objects but they
don't
import it regularly so we often have the
case we have a version which might be
two years old and we have several
changes made and
maybe the customer has a version from
2012 and now gets objects from 2014
and
are you planning to implement a way on
how i can
recognize which version of the object
was imported and which steps
i have to execute in the upgrade
something like a conditional upgrade
steps regarding on the imported version
and the target version
hope you understand what i mean
again
and let me
recap if i understood your question
correctly so
you have different version of the
add-on in different years
and you want to
upgrade to the latest version was that
your question
and how i am keeping track of that
version
no no no
okay we have the problem um well when
you create an add-on and you have uh
regular releases you add one field
you delete something else you move um
fields from one field to the other and
something like that
and
if i have
upgrade phone version a2 version b a
small step i know okay i have to copy
this k table
and i have to transfer the data from
table a to table b
but
the question is if i'm going from
version a to version f for example is
there any way how i can
make conditional changes um do i know in
the output step how i um which version
was imported of the table you can take
it
um no the answer is like we within the
same upgrade code unit uh you cannot
handle two versions like from where
you're coming from
um
the the schema synchronization and the
whole process will be reactive so that
you will need what you will
know what what to build for uh depending
on the version that you're coming from
so you will see the errors uh but within
the same upgrade code unit you cannot
use the same one and say and uh apply it
if you want to uh
upgrade from version a or if you want to
upgrade from version b to the current
unfortunately
may i answer to the question
if you build a difference using git
between two versions the upgrades
necessary for this
are inside the difference so you will
always use the right upgrades
know what i mean
i think
what you would like to have if you would
like to have
support for different versions within
the same upgrade code unit
so
yeah the upgrade coordinate is not a
version version average at the moment
but but you could add the codes that
branches on like a version list yourself
yes you can do that of course but you
don't have a decorated function right
now that will support that
okay my question can you use a
parallelism for
recompiling the whole solution
yes
i'm not sure i mean i i've put this on
somewhere maybe i didn't put it on the
block maybe it's a good idea to put it
on there
i believe it's even one of the examples
on the dvd i will check this and then
i will you know put it on the blog
if it's not there but uh so you can
compile for instance one way to do it is
to uh to create an array that contains
the different object types and then
iterate over the object types so then
you know if there's like seven object
types you would have seven threads
compiling your application code
and
depending on how many cores you have
it can really be like two times three
times four times faster
the only thing you need to do is that
because there might be some race
conditions on the uh on the object table
that needs to be updated by all the
threads that you need to do one sweep to
compile everything that that didn't
compile but usually that's only one or
two objects
so yes that is possible thank you
i think that's it
okay
thank you very much guys thank you
[Applause]
