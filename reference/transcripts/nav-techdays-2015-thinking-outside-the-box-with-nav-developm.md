# NAV TechDays 2015: Thinking outside the box with NAV development

- **Source:** https://www.youtube.com/watch?v=R4xfmbjiKOw
- **Video ID:** R4xfmbjiKOw
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 94m33s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

so actually my name is waldo
oh no it only it only uh
takes once um okay thank welcome
all of you and apparently there's quite
a lot of you
so that doesn't feel good on my nerves
at this moment
thank you in this session on thinking
out of the box now i
had or i could spend one slide
on introducing myself and i actually
going to introduce
my wonderful team because i have to be
honest i
am not uh well though if i wouldn't have
my my team behind me and this is
actually actually not all of my
developers i couldn't find a decent
picture of a few of them
um so these are it's actually my team
and
the things that you're going to see
today is
them and me always a little bit thinking
out of the box
now i'm a development manager so this is
my team and
the nice thing about development manager
is the fact that
they can do the job and i can explain it
to you and get the credits and so
that's nice now i would
like to try something as well now
instead of because
there are quite a few people here
instead of
raising hands when i ask a question
let's clap hands
right so let us try that
are you enjoying nafta days yes
no no only once okay we need to practice
this so are you enjoying the
nafta days yeah great where are the
women oh my god we are totally in the
wrong line of business
um now at a certain point
do you know this guy
i'm actually a real fan of discovery
channel i mean i'm a real
guy let's say i like women i like
survival shows and i like cars so that's
and this is one of the survival shows on
the discovery channel and this guy is
actually made me think of like
okay uh he was actually uh
in some kind of show and eating spiders
and and running over trees
jumping into ice cold water and these
kind of things and
he said on a certain move the ad you
always have to think
outside the box
and i said we survive every day
thinking outside the box doing nav
development right
yep so that's actually
that guy is the reason why you all are
here at this moment so
okay a little bit of an agenda i'm not
going to spend too much time on this
this is what we will do today i think
it's quite clear
first thing the little blue guy
powershell
i'm have been involved in some power
shelly things
lately so um i've been blogging about it
as well and so it was unavoidable that i
was going to talk about powershell today
as well so
first of all twos two uh i have to say
sorry for two things
sorry that my big face is on there and
sorry
that i have to talk about powershell
again
i'm not going to talk about powershell
on what is the basics and stuff like
that
i'm more going to talk about what can i
do
with powershell actually how do i use
powershell
on a daily basis and i hope you will
learn
one a thing of two first of all
i guess you all know the ise
yes that's good because that is the
visual studio for powershell
right that is the c side for powershell
it's
quite comparable now because ise had uh
the intellisense and we do have
intellisense in the
code designer in nav as well so it's
really comparable now so
but we can extend we can build on top of
the ic and make it even more our own
and and do stuff with it so let me try
to show you that
so i created a few code samples uh
the first thing that you can do is use
this kind of variable
in powershell in the powershell ise the
dollar psise
is actually a variable an object
that controls your id environment so
you can do stuff with that you can go to
your current file
so in oa and i'm messing this up now um
you can create a statement like get item
from my psi
the dollar pseiz dot current file dot
fill path
get me the item in this case
i'm getting my current
current file give me the directory
and put it in the variable script root
what this is actually an alternative of
the ps
script root do you know the ps script
root
that is actually a variable that only
exists at runtime
in powershell it is not usable when
you're actually just debugging a script
or running one by one
because the ps script through does not
exist this is an
alternative so there's already one use
that we can use with the psiz
now what we can do as well is
let me just load this line because i
need that we can use the ps edit
vs edit is going to edit in
ise a certain file actually i'm just if
i do this it's going to open
this script my mouse is really not
working with me
so open this script in
ise hmm cool i can control
the ise environment a little bit doing
powershell
okay what can we do more we can write
code blocks
this is some kind of code block a block
of code that we can put into a variable
and this and we can execute that
variable like if we put
a code block into a variable we can
execute this
variable which is actually going to
execute
the uh the other code that was in that
variable
cool let's just store that into our
memory and
see what we can do more now in this
psise
we can do like we can go to the current
powershell tab
which is actually my current run space
that is running at this moment
yeah um now we can go the add-ons menu
so in this run space
this menu here it might be an ise
environment
the sub menus oh just these sub menus
add one oh i can add my own menus cool
call it hello world execute some kind of
code
and with a with a shortcut key
so let us execute this one
and here we go we have our own
menu button in our in our id environment
this is extending already right
yeah that was
an intentional what we can do as well do
you know the autoexec this is
intentional the autoexec
dot but in the members dos yes we know
that that is actually a file that's
going to be executed from the moment i
enter i actually
start my pc right not really anymore
because we don't use those anymore now
we want to run some code when we start
nav or
when when we start this this environment
this is environment so this is what the
profile is all about
now this dollar profile never call your
variable pro dollar profile
because dollar profile is kind of like
deserved they're reserved
so when i execute this you'll see if i
execute this one
you'll see you
don't see anything actually uh that it
points to
some kind of files on your system in
order i
in in any context like if you're the
profile for all users all hosts the
profile for all users current host
and so on right so if you
create a file on this place within this
name
this is actually your auto executable
right so i could create a file like that
i'm going to remove it first and then
create
that exact file so i'm creating a file
with this on the all current all users
current host
and i'm using this ps edit to edit this
file right
so here is the right host here is the
the file
and i'm just putting right host hello
world into that
i'm saving it closing it
so if i actually open i can completely
close down my environment if i open it
again
you'll see that some code is executed
being
the yellow world cool i can control
the moment i can i log in or i open the
id environment
i can add menus i can do quite a lot of
stuff
doing this right
next thing is you'll see that i've been
struggling here with my prompt
now this is because my current location
is quite a long location
this is not nice you can control your
prompt as well
in fact every time that it shows your
prompt is going to execute
the prompt function and you can override
the prompt function
so if you just create a function like
this this prompt this is going to output
the ps nav take this rocks then i will
never have this
location anymore and i will always have
the prompt like enough take this rocks
cool now we have seen how we can extend
the ise now let's show uh what i did
with this
um when you're creating uh of doing
powershell
um you're creating scripts you're
creating files you need to save them
somewhere you need to name them
somewhere
sometimes you're creating stuff twice
you have duplicated code
it is like any other language things you
need to take care about things you need
to structure
now in terms of powershell i make a
clear distinction on what is
a function and what is a script
there's a screen that clear the strings
as a function is something really
modular that you're going to use
multiple times
in any kind of language a function isn't
that right
a script is something that you will
execute
once in a while but but it's going to
use your functions
and stuff like that in my opinion a
script is
a temporary function that will at some
point be a function
at some point in time now um
what i do with my
functions to make them always available
for me in my environments
i create them into a module it's quite
quite easy to do
what you actually do let me close down
my environment i have my module over
here
so what it is is just a set of folders
you name your folders
a certain a certain way and basically
you just oh sorry you just put all your
files
being one function that's how i do it it
doesn't necessarily need to do it like
this but i put one function in one file
and i named the file exactly the same as
a function
so i can easily find always my functions
right so i have a few functions uh i
even already started to categorize them
and in my folder i've got the
you see these are all the ps1 files
which are basically just
powershell scripts and i have one
module script which is also a script
that is going to be run
when you load the mounting module yeah
so that's the psm1 file
and what this is going to be run when
you load the module and what am i
loading when i'm loading the menu
basically
just all my function
this is going to get all the child items
which is a did get all these files
and run them so all these functions get
run into my
run space and made available to me so i
can use them
yeah the next step is actually making my
module available
for my entire environment making
powershell
know where my module is basically this
is an environment variable
and you have to add this path to the
uh yeah environment now
you can obviously script this as well so
what i
did is i created a few scripts to
install my module so basically what we
need to do what i need to do is just
take this module
put it somewhere now dropbox is going to
do that for me so that's also
automatically
so put it somewhere and then run
first of all the module install
which is quite easy this is just
editing the environment variable you all
know what environment variables are
there is a module a ps module path
variable as well
and you have to add your path your
current path i'm using this ps script
root here
because that's where my path is at this
moment now
i'm adding that and i'm adding that to
the current
variable in powershell as well so it is
up to date at this moment then i'm going
to
import all the modules once and
from that moment my environment will
always know which functions i have
when i open my environment cool
run done next
i have here kind of like create
profile in ise which means okay
extend my ise because i want more than
what you are giving me
right
okay open please
and what is this it's just going to
check if my profile already exists
if not then create a file if it already
write a warning like okay if there was
already a profile i added my stuff
at the end and what is that stuff just
code in a text this is a lot of code
and i'm just adding this code at the end
of the file
and then opening this file in my iz
to show what it actually did so let me
execute this
here is my profile file i can remove
this right host
this hello world i don't need this
comment
i'm going to update my prompt do
something that is meaningful for me
and i add some kind of functions to my
sub menus right so if i close down
my ise now and i open it again
i will always have an updated id
environment
i can just run easily enough
modules i work with nav i can
open my scripts folder i can do stuff
what i
actually am doing daily this is my ic
environment and this is actually running
two scripts
next something that i really need to
address is ise steroids who knows i see
steroids
not too many so this is good because now
i'm teaching you something
ise steroids is actually
the thing that you just saw that i did
but then multiplied by twelve hundred
two and
two hundred and five or something by a
lot this is
for me the tool to use when you're using
um yeah the ic of powershell
and you will see it's going to load now
and you'll see it says oh good afternoon
eric
who doesn't want the tool that says good
afternoon to you right
and you'll see here that the ise is
adding lots of buttons lots of
functionality
to my ise environment i mean the iec
steroids is adding that
it even adds a separate menu for my
my comments and what i definitely like a
lot
is this refactoring add-on that it has
as well
when you're writing scripts you have a
lot of options
to do and you can very simple thing you
can either use one
single quote or a double quote for a
string what should i use
ise is going to learn you what you
should use it has got refactoring um
capabilities it can even fix your script
you can script everything and everything
works
and then you can fix your script and it
will structure how it should be
structured
uh for powershell i
really like this one what i like as well
is what i'm going to show you
during the next demos quite a lot so i
will address that
when i'm when i'm using that so this is
your personal
powershell assistant or your personal
powershell consultant
by this well worth the money it does
cost a little bit
it has been written by an mvp who gives
it for free
on mvp so i didn't have to pay for it
so it's well worth the money
no but that's actually the reason why i
cannot tell you
what you should buy different kinds of
price tags
just check out their website and see for
yourself
next when you start creating your
scripts always as i said
think in reusable functions i'm going to
show you a few of them
that i'm actually using daily
hola
and i'll start with the basics
um invoking a sql query this is
if you are able to invoke a sql query
you can do a lot with powershell so what
i did is i created one function
that very simply invokes a sql query
and gets all as many uh
default parameters as possible uh so i
have to
give as less default parameters as
possible like
in this case i can just invoke a sql
give the database name and sql query
done
and even i do not have to give a
database name if i don't give a database
name it will execute in the master table
table so it's very easy i can execute it
and hopefully it works i do need to run
i think enough 2009 so let's
execute it again now what i like about
the invoke sql as well
is that it's going to build me an object
so all the fields
in my table will be properties in my
object
so i can access the result
and just take one property out of it
these are my company names
right if you can execute sql you
are able to do a lot next
if we can execute sql we can take a
backup because
essentially backing up a database is
executing a sql statement
right so that's actually the next level
and we are taking backups all over the
place
how do you take backups is it with
sql management studio manually or is it
with
powershell less people with powershell
so let me actually just show you and now
i'm showing you an ic steroids function
go to definition how cool is that
not that cool apparently um
so this is just one of one of the
functions and what i'm doing here if
you're managing backups
the thing that you always are have
problems with is finding the folder
where that
user from sql is able to put the backup
right like you you cannot access this
folder why not i can access the fault
yeah actually the user cannot access
this folder so
always a problem you are always sure to
um to backup to the folder where sql
has uh the setting like the default
backup folder
right so i'm getting that out of the
registry
let me just close this one i'm getting
that is this readable by the way
yeah it is i'm getting that out of the
registry
and just performing a simple invoke sql
to perform that backup it's going to put
that on the default
location i know this is always going to
succeed and what i'm getting back
is an item being the backup file
and i can work with that like backup
database move
to the location i want to do
okay if we can do that we can obviously
we should
also be able to restore backup this is a
bigger problem
did you ever try to restore a backup
with
powershell
not that many this is not easy
and it's definitely not easy but now
restoring a backup
you have to take care of the logical
file names you have to take care of the
physical
file names and it should be the new
database name not the old database name
right so if
by default if you restore a backup the
backup files is going to be
the original database name and you don't
want that
so that is a thing that again the
powershell can take care of
and what i'm doing here is i'm going to
just select yeah there's also another
thing you have to take care of is where
does the database files need to be where
does the log files need to be
right so yeah you want to have this
in the sql server settings so it's going
to get that
out of sql in this case it's just a
server property
you can query with uh again the info
sql for the uh default database part
and default log part then it's i'm going
to
construct some kind of sql statement
where everything is in like here is the
physical files
here should be the physical files the
physical files should have this name
and the logical files that have this
name
i notice that i'm not really executing
anything
so let me
take the backup
and restore it as well you'll see that
the invoke statement has got some right
host like are you
invoking now this to the database to
this database and stuff like that
so you can really see what's going on in
the background
now always when you create functions
to create something always create the
functions
to destroy it because
there is something called rollback which
powershell does not know
if you have this kind of script and you
were able to do this
this is committed and that there were
five databases created
you might want to script also like a
cleanup thing
to destroy what you just have done right
so i have my
drop sql database if exists and just
let me remove this database that i just
created
now okay we have these basic functions
these building blocks let's go one step
further
we have what we would like to do is have
an easy commandlet to build another
environment
being restoring a backup being
also create a service there and all
these kinds of things
so let me show you this one
this is actually quite easy still it's
going to
um get let me try to find
it gets the backup file so it's going to
restore the backup
then create a new nav server instance
um then let me just execute this and
then it can do that in the background
um then i'm going to get the server
account
that the service account and make them
the db owner
which is kind of like a good practice
so make a db owner also that is just
invoking some sql
and then there are a few options
obviously when you create a new
environment you need a license as well
so there's an option to provide license
and update the license in the database
there is an option for report sharing
who uses sport sharing
so that means who use does not use poor
sharing
okay who do not does not use nav
because either you're using or not um
now port sharing is definitely not
something that microsoft
is going to recommend and you should use
that
by for your own uh i for your own
concern
but um we are using it really
really uh a lot and we do not have any
problems
just yet i'm touching wood there is no
wood here
i'm touching wood maybe tomorrow there
is uh
there is a problem in port sharing
department
so i also have an option to start a
windows client here so it's asking me do
you want to start a windows client oh
yes
start it as well um
no that's actually the same now as this
one
as you can see i i can build even
further on this like okay now i've got a
function to build new environments
what about copying environments i'm
always installing a default instance if
i take the cd
the one thing that you do is you put it
in your dvd drive
no probably you don't but you execute
the setup and you install a default
environment
but sometimes you want to test stuff and
you want to copy this environment and
then
all the manual things start like okay
let me manually take a backup then i go
to the
administration console create an
instance and all these kind of things i
need actually a service account
blah blah blah why not
use what we already have and just read
what is in a certain server instance
like which database is this what should
i backup
okay back this up create a new server
instance
and continue with that yeah i cannot
show the definition just yet um
but basically that is what it's doing
now again on top of this
you can build functions like convert and
multi-tenancy if you doing demos and
you have to convert to multi-tenancy
it's always the same thing
export the application remove
application update your
server configuration and and all these
kinds of things so again
you can build converting into
multi-tenant
environments as being just a simple
function
yeah not going to execute
all of them because it's just going to
take too long but as i
said when you create stuff always
create a function to remove it as well
so
that's what i did here as well
the remove nav environment quite
an interesting one because it's going to
check all the databases for instance
also for a multi-tenant environment and
you have multiple tenants and the
application database which
needs to be moved but if you execute
this on a live system yeah
then you're in for a treat
okay
you can not only build your own new
functions you can also
and now i have to pick my words do i see
someone from microsoft i don't actually
you can also fix decrementals that
microsoft built
for instance um
did you ever work with getting a certain
configuration
from a certain service like to get
enough server configuration commandlet
not too many people um let me show you
this
there is
uh i need to wait a little bit until my
yeah they are dropped okay so
this statement and i just can say okay
get me all these my configurations from
my default instance
execute this and you know this right
this is actually the output
what we have in the xml from uh
well for the server xml now
we are definitely never interested in
getting this entire xml you're usually
interested in one
specific thing like let's just say we're
interested in the multi-tenancy part
like is this server instance
multi-tenant so what i would like to be
able to is
that's why you want to get to it
straight away
yeah sorry i'm very bad in
searching in these kind of things here
this multi-tenant key
false is actually i would get i would
want to get in my powershell
script straight to the false like
if false then do this or if true then
get tenant
right it's not that easy
because i should be able to do something
like this
where key equals
multi-tenant f8 zip
nothing and it should work
now the thing is this commandlet is a
very good
example of how to not build commands
actually
what you can do is and i'm going just
going to show you the solution
the thing is that it is
actually just showing an xml
and if you export this xml or if you
you are using this xml as an xml you are
able
to get let me just execute this first
to get to the
do i remember this i don't
sorry for this
you can get to all the nodes that are in
your xml
with a little bit of search you can find
out that actually your
true stuff is in there
and what you can do is
filter in there
so you can get to this kind of false
kind of thing
if you just place this between bracket
get the value
and here is your false variable now this
is quite
complex so you should obviously turn
this into a function
now what i did and with the help of
someone from the community
um i turned this into
a function that is called get enough
server instance four
yes i have multiple versions um
now get now serv instance four i i
actually
was thinking like okay if i'm getting
the server instance like the state
i might also be interested in their
configuration and why
is this two commandlets it's like it's a
one-on-one relationship so
why not having one statement giving me
everything
as you execute this one you see that it
gives me back
everything but in an interesting way
like if i put this into a variable
you see that i can access this as being
properties
well maybe not
uh maybe it helps and i actually provide
the server instance
you can see all the points that i am
interested in so i can just
take the multi-tenancy part and this is
a much nicer race to work
with configurations of your server right
so not only you can create your own
bowling box you can even fix what is
already out there
yeah now
obviously the one thing that we want to
do with powershell is upgrade
is it not so but
upgrading is a lot a lot a lot of
building blocks
and for everyone it's about
different uh on on which building blocks
you want to execute
when and how i'm going to step through
this
because i notice that i'm already over
time
not even all of the session
the goal is to automate as much as
possible
imagine that you have a script that you
can
feed with a backup file
and some kind of text file with objects
or not even you can even get the objects
from the backup file
you run the script and
about 16 minutes later you get a backup
file
with an entirely upgraded database
with data and all that would be cool
if we want this i think there's three
steps first of all we need to merge
and if we need to merge yeah we need to
automate quite a lot like exporting
stuff we need to create deltas apply
deltas
we need to
worry about the conflicts if there are
any conflicts if not can just continue
we can we need to worry about first list
and so on
now this merging thing is only one small
step
in fact this merging thing is maybe only
three minutes or four minutes
it's all the red set is actually taking
quite a lot of time
and upgrade as well like creating your
fob file
this is a classic upgrade path by the
way
now creating a fob file might be like
create a sandbox database
because i can only create a full file in
my new version so create a new
database temporary load my
merge result into that compile it export
it again i've got my
fob file then the data upgrade needs to
take place
which means restore it in the modify
unlock the object convert blah blah blah
blah blah blah now i've put this into a
script
and it works and this is the output
i obviously i can show you anything i
want but
i can guarantee you it works um
so there is a script that does
everything it's quite an output because
it's going to do quite a lot actually
building databases exporting objects
uh merging and all in the end you see
here that it's actually also
performing the data upgrade deleting
tables never forget to delete the tables
that were actually deleted in for
instance the target
instance right and
and all of a sudden you have
a result now this result it took 951
seconds
about 16 minutes um
we should go faster 15 minutes are we
happy with 15 minutes no yeah no one
yeah okay a few also i skipped this
um now there was
a person called gunner justin is an mvp
as well
you actually he's i don't see him
he brought me to the idea like okay but
you can use the power of multi-tenancy
let me try to explain in the one slide
i'm most proud of because it took me
only two and a half hours
to build this one
so what we can do after that we did
emerge like the merge is still the same
export merging and solving uh version
list but
what we can do is try to com avoid
the um the conversion of the database
because the converting the database to a
new version is taking quite a long time
let's try let's try to avoid that
what we can do is we take our target
environment and we're going to copy that
we got our copy command
we can import a server license we can
restart it obviously then
import all merged objects
compile we do not care about data in
this one so just compile
force and make sure it works
then using multi-tenancy
things so we're going to convert to
multi-tenant being
yeah two databases at that point having
our applications separately
from our tenant data we just destroyed
the tenant data
we don't care about that now we have an
up-to-date
application compiled
so ready to start our data so we can
restore our modified database which is
actually
our development database that we try to
upgrade with data
development our production database with
data what we can do
is also this one just remove the
application
this one is outdated so we don't care
about the application
and we're going to mount it to our new
application
obviously this is not really compatible
so what we can do we can import the
upgrade code units
we still need them obviously sync it
so this sync statement is going to take
these upgrade code units into account
and then start the data upgrade
yeah and then the only thing you need to
do is
just dismount because you started with a
single tenant environment
the result should be a single tenant
environment so you need to convert this
kind of thing
this kind of thing into a single tenant
environment
and you can do easily do that by
exporting the application
into an existing database so you can
just export the application
to your tenant and now
drop this database and you've got a
result this
i also worked out in some code
i'm briefly going to show you the code
it's the upgrade part mr no sorry
it's the goal faster
so what we have here is basically
a function that does it all
i didn't put too much time in
structuring this function so it's quite
a long one
so all these steps that you have seen
it's just
one after the other
we save eight minutes
so actually we gain 50 of our time
right so i think this is a cool option
but
only an option when uh you're fifth 2015
and higher
if you need to do unicode stuff you need
to do a different dimension stuff
obviously it's not a part of this uh
this this
script can we think of one more step
that we need in our upgrade scenario
do you think we covered it all is this
automating everything that we
want to automate anyone
clapping is not going to help you now
what
as well but testing is actually just
running in
a code unit you know you've seen it
actually one more step is downloading
downloading your uh your update
how do we download it's quite a manual
step right
it is finding some kind of blog
article which mentions the uh the
comment of update which is the best blog
ever no no no it's the nav team blog
the nav team blog mentions the
cumulative update
right so you could look into that
then find the the knowledge base article
on this
then request the hotfix then select the
hotfix
and fill in your email
who open your email
and find the link and click the link the
email
looks something like this
all right this is an email and you see
here a link
that you can click and it's going to
start to download
can we automate this
okay you already know so i can skip to
the next topic
we can automate this now let's have a
look
at this link because this link
provides us some data
and we might get this data
out of this kind of website so
this is actually the website with all
the platform
updates this is actually where we fill
in our email address and
request the hotfix right now
we have this this table here and uh if
we compare it
with the link uh there are there's some
data that is not in this table like
this number here do we have that yeah
it's this number
cool we have this number here
and it's not really in the table so and
i should have the data
somewhere to be able to compile this
link
yeah so what we can do
this is a trick of one of uh of my
developers by the way i did not
really did not
we can go into source of this
website so let us check
if there is any usable data here
at a certain point there is this thing
do you recognize that what is it
what it's jason
it's not a person now jason
is a way to describe an object
now let's break this down let's
look at this json thing you'll see that
actually all the data
that you need to compile
sorry that you need to compile
this link is in the json part so no you
cannot read
maybe the visual part but you can read
the json and definitely you can read the
json in code
code when you think of code you think of
powershell obviously
now what my developer did he built uh
this into
a bigger tool uh which we also
built actually easel on the fly from the
moment there is a comment of update
and these all pops up and we can use
this easel in our
virtual environment now what camille did
is camille sachek you know keane from
ibuzzu probably
he built a powershell
commandlet with actually just the same
trick
and let me try to find this power cell
command
if i'm having internet then
i'm lucky so let me
just run the function and then
run what it's doing it's actually just
performing all the steps that you need
to do to
do this so it's actually going to just
check if it is working
to the blog from the blog to the
knowledgebase article knowledgebase
article is going to read the json
or the request hotfix it's going to read
the json
compile the string and start downloading
so this is a script that you could use
in some kind of server environment with
daily monitoring
your or the blog right
now you've got everything now you have a
building blocks
you can come in the office in the
morning and
monday morning having a mail saying
hey there are three conflicts on the
late list
commoditive update of the uh download oh
was there a comment of update oh yeah
there was oh you tried it oh i've got
three conflicts
let's solve them or there were no
conflicts
and a database was created with these
credentials and everything
on it all the building blocks are there
let's stop this one
so powershell key takeaways
only 20 minutes over time
i think we can do a lot of powershell
thinking reusable functions extend
the thing and do not be afraid of
powershell
use it in your daily life i'm using it
to pack up my music
to backup my um my movies my home
videos to a folder where my kid of two
years old kid
can watch the movies is
in front of homemade movies that we that
we make
powershell can can easily do it now
one question did you like what you see
would you like to uh get your hands on
these functions
well from today it's actually already
online
and you can actually access all these
functions
already on github it is on github quite
a lot of people are taking pictures now
it's good share your experience one
disclaimer
there is no support whatsoever
but there are a bunch of tricks
that you can use and if you
obviously hook into github with github
then you can collaborate and share
experiences and
we can be a whole happy family
powershell family for nav
extensions this is the only decent logo
i found
about extensions i really wonder
what they were thinking for naming these
things extensions actually
extensions okay in short what is an
extension
um i think when we talk about extensions
and i shouldn't be calling it apps but
i'm going to
calling apps because explaining what
extensions are
is by just referring to apps
think of being able to
install multiple apps in your nav
environment
so this app should create or is going to
create some
stuff in uh
in your environment like like create
fields or create modifications on pages
or create extra code and business logic
but if you have multiple
apps extensions it's going to create
multiple changes and
you should be able to install apps or
extensions
and uninstall one by one and so
it's kind of like a complex
thing but basically what we what
extensions are
is an upgrade safe modification to your
database being
able to install and uninstall uh
a modification now what is a
modification modification is a delta
so extensions are based on deltas
if you do not know what deltas are
then i will show you in a minute
i will try not to repeat what thomas
already did this morning now
what do we need to create an extension
again powershell oh no
well though again powershell
yes i'm afraid so now we have
multiple powershell commands for
for creating extensions in fact we
have powershell commanders to create
them
an extension is basically an fx file
and to deploy them yeah you have seen
this
now to do this
you need a manifest a manifest basically
is going to describe
your extension always think
global like if you're creating an
extension you're putting
in on some kind of website somebody does
downloads it it needs some description
what does it do
what prerequisite does it have what are
the
dependencies these kinds of things but
also who is the manufacturer oh it's the
fact that why don't trust effect
these kind of things um oh it's
microsoft no
um so that's a manifest
um what's in the package in the navex
file as i said
it's deltas it's not a fob it's not a
text file is
deltas is a text file but it's not the
object text file it is a delta it
describes
what you have done for development
okay now let's create a simple extension
i'm going to go over this really fast
because i heard i was not in the keynote
but i heard that you already seen this
is that correct okay okay so i'm
going over it really fast
usually when i say that it takes two
times the time but anyway
as i said there was two steps yeah
first of all let's open the development
environment
i created already a development
environment for my simple extension it's
called
simple rental extension so there is no
developments
just yet and i'm importing this uh
this text file which means i have
been developing the item i added
a rental item field
and i changed two pages
okay so what i can do now and i will do
that in one big step
is i going to create a working folder
because i'm going to export
delta files and stuff like that so i
need a separate kind of folder that is
going to manage that for me
this is my folder and now i'm creating a
manifest
i'm creating my deltas and i'm creating
my
um my navic's file this navics file
contains the manifest you see that i'm
pointing to the manifest
contains the deltas you see that i point
to the app files which
contains my delta you will see that
in a minute here are my deltas now and
the path where it needs to create the
navex file
and here is here is my navic's file okay
when you have that that is your app your
extension
so when you have that then you can
publish it step number one publish it
making it available
in your testing environment this is my
is going to be my testing environment
which means do not make it available to
users yet
just make it available for
administrators to install it for the
users
first step this one is
going to do quite a lot it is creating
it's checking
the prerequisites and the dependencies
obviously am i able to install this
in my case there are no dependencies
whatsoever
then it's going to build a sandbox
database it's going to build you a new
new database
why does it need that because else it
would change my resulting database
which is not the idea and so it's built
a new database it exports the objects
it's going to
apply the deltas import the objects
again
compile it and then you've got it has
got the metadata it needs
to for the application to work with
um let us see if
it is done now publishing can take a
while depending on how big your
extension is now what we can do is just
install it
and installing shouldn't take that long
now we can check it like uh okay what
which are
all the tenants or or the apps that i
have installed and you see that i have
installed the
um no sorry
i should do that with this one
then i installed the rental extension
now this is also a commando that you
have
but i personally didn't see the use just
yet
for the get enough tenant it should show
you
all the apps that is on a certain tenant
but it's not really giving me the
information on the app so
what i'm using is the get enough info
and you can use that in two ways
either you just provide a server
instance and then it's going to show you
the published apps
or if you provide a tenant is going to
provide you the installed apps on the
tenant
it also works in a single tenant
environment you just have to provide
the default as being just default tenant
and now i can just show what
i want to show being
almost i lost my water in somewhere who
took my water
um
so here it is so what i did is i created
a new field and i added that to pages
so let me check in my test environment
whether this field exists it does
the rental item field and check in the
dev environment if the field exists
so i mean in the id environment of my
testing environment right so i shouldn't
have any change here
and i don't so there is not one i
changed object
and if i go and check table 27 you'll
see that there was no
table or field 50 000. so
the application is aware of the field
but actually my development environment
is not aware
of the field and we want it like this
yeah
okay let us have a look at the more
serious app
let us try to have a look at the more
serious app
okay i shouldn't have closed this one
hola that's normal
right close to my id environment which
means my run space is empty again
so this is it showed me somewhere
some kind of box yes
the dev environment from this
application looks unlike
this now uh it's a little bit more
objects
that's what i mean with a little more
serious uh rental app
these are 70 changed or added objects
so there is quite some business logic
that was added and hooked into
the default application now this is the
default application what we did
is also a rental extension we added like
a new filter on the
on the role center which filters our
rental items
we have added some actions on the
default page which is going to like
being able to buy rental so this calls
out to our new
environment which i can simply
going to use now let me just show you
this
create a purchase order now this is
obviously calling back to default
functionality creating a purchase
purchase order
and i can receive a purchase order as
well and when i receive a purchase
orders can actually just
post it it runs through the item ledger
entry posting
and i hooked into the item leisure entry
posting to add some
entries in my rental uh entry yeah
so that's why we have some amounts here
so there is some hooking into default
functionality going on there is some
changing of pages going on there is some
visualizations going on as well like we
on the customer we have
a map which is added and part of the
extensions um and
yeah we also i'm not going to show you
everything so
it's actually basically trying out what
is possible with extensions
and building this there were some best
practices that we
ran into that would like to share with
you
so best
practices first of all
when you're doing extensions
always work in an isolated development
environment
know that you only care about the deltas
you do not care about any virgins you
don't don't care about any localizations
whatsoever you
care about what you are going to change
on a certain system so never start
developing an extension
in your ongoing development environment
of a vertical for instance
that doesn't compute you should be able
to
create a delta what is going to be the
delta for your extension
yeah so it should be isolated always
let me just check if i just stole
everything yeah probably um
always test as an extension this is out
of experience believe you mean
never expect that an extension is going
to behave like it would behave like
normal development
very simple example business charts does
not work
in extensions we were developing the
business charts in our extension lost
three four hours for building a cool
looking business chart and then we built
an extension and said
you cannot use business chart you cannot
use any add-in
yeah so always when you test test as an
extension
new function on tables it's not possible
you cannot write
any code in existing objects
yeah that means you cannot you can add
uh actions you cannot add code to it
so in new actions on existing pages
you should call objects
so call a code unit or call page
report no reports
so you need to know your limitations and
best is you need always test as
an extension now again power skill can
help oh no
it is again yeah powershell can help you
doing this uh by the way also part of
this uh of the module
i've built some scripts around
extensions and
together with a colleague by the way but
about everything is together with
colleagues
um so what i have here is
some kind of settings what i sometimes
do to structure
my my powershell is if i'm if i have
multiple scripts
i have one extra script to have to hold
my settings because all these scripts
is going to use the same settings yeah
so what i'm going to talk about is
building your environment
and creating your dev environment
so i've got my settings script here i'm
talking about the rental extension
a certain initial app version is going
to add versions
to the manifest automatically so it
finds already a manifest and it can add
a version and you have a new version of
your app
but start let's start by building our
dev environment you have seen all these
functions already building and copying
and these kind of things
that's actually what i'm using here so
basically what i'm doing
is create three environments being
where is it the original modified and
targeted
environment so i always have an original
where i compare it because i need deltas
then i have my development environment
and i have my testing environment and
this testing environment i'm going to
convert to multi-tenancy because i want
to test in a multi-tenant environment
for two reasons you should always test
in a multi-tenant environment
because it should work in the
multi-tenant device but also
i noticed that it builds faster in a
multi-tenant vibe
something to do with the sandbox nothing
that i can explain
why that should be faster than building
in a single tenant environment
it's just i can convert it to a
multi-tenant so just that how i built my
my development environment for uh
extensions
so that can be built and then our main
script
always when you want to test see it as
an f5 in visual studio
you press f5 to test right
here you can have a build script that is
your f5 which is actually also a
f5 that is going to create your navex
by exporting and let's just execute this
so it's going to
export all the original if
it didn't already do that in this case
it already did that so it's going to go
fast in this case
it's going to export to modified all the
modified or only
the ones that this have the modified
flag
if it already exported the rest of the
objects
then it's going to compare always all
objects because i do not want to forget
any
compare create deltas and basically
is going to
create a navex file and from the moment
it has got a navic's file
it can start deploying it now obviously
this
first needs to check okay is this
already in my
this app already in extension sorry
already in my test environment
then i need to uninstall it and it
should be doing that yes
but because it only already found it and
then publishing
my new version and then after that
install it
opening the client and i can test
visualizations you have seen our
map now custom add-ins is not possible
default add-ins aren't even possible now
this will be fixed soon
you will be able to use uh all the
default add-ins that come with the
product
really soon in one of the next comment
of updates now
so you need to be creative one example i
can give you you have seen the map
does anyone have an idea what that was
it was actually just a picture there was
a service online on bing by the way that
you can use
and you can uh send coordinates and it
will send you a
picture back that you can import and
do it like that so it's just calling a
web service and importing a picture
so it can be creative to do your
visualization you can work with the cues
that you have seen
as acting like a role center kind of
thing
upgrading an app obviously when you're
talking about
app or extensions i should be calling it
extensions
start calling it extensions
you should care about upgrading now how
is this upgrading thing
going did you did
thomas talk about that during the
keynote
no okay let's talk about it a little bit
now upgrading no i don't want to open it
we trust waldo
when i add data in my
newly created fields or newly created
tables what happens when i uninstall the
app
or uninstall the extension let's just
see
let's see what data that we have in our
simple extension
so here is our testing database and our
simple extension
just had one extra field and let's put
data in that field
let's take two so what happens
i'm going to keep this open that happens
if i uninstall the app
and for instance just install the app
again so in this case
you can notice i just refresh it
errors like there was something wrong
because you updated the page
now my field is gone right now i'm going
to install the app again
and my data is gone what actually
happens when i uninstall an
app by default it's going to put the
data into
some temporary tables on sql server
i can show you whoa these are big items
um
so my qa environment should be let me
see
this one and
let me think
okay not one table actually
well there are normally nav app tables
um that is going to build on the fly
from the moment that you
export or uninstall the app is going to
put your data into the table now
the idea is that you install the app
again that you're going to get the data
out
yeah and this should be coded you should
foresee
some kind of upgrade code unit
so let me import this upgrade code unit
start the development environment and
let's see what this code unit
looks like
now first of all what i did is this was
my first attempt like
okay i have my rental item filled and in
this case i had another field as well i
think
no yes no yes so i had my
my rental item field and i need to
restore this rental item field
now the thing is first you need to
create a code unit that has these two
functions publicly because when you
install it
it's going to call these functions one
function per database another function
per company
and then you're able to call
the record ref of the archived version
of the the data
you can even check the version of the
data let's
not go into that now when you have this
record ref
this record is not the item table so
we're not able to get our set table
kind of things in fact this records ref
only have
the fields the key fields and the added
fields that you just added
to the table so it's different that
means that you need a loop
you need to loop the fields and put them
one by one
in back in the original data
this is obviously manual and if you
forget one field
your field is gone
so what i would like to suggest this is
out of the box thinking like so i have
to provide some tips
what we did is um we provided
we have built uh two functions
one for new fields in existing tables
and one for new tables yeah
and we just are going to loop
everything that we have in a certain
number range one for fields looping all
these fields in this number range
or one for tables and now you can build
some kind of generic
function that is going to
not really yeah it was one that is going
to loop fields and and
go into that let's not go into the code
but one thing one other
tip is use the all object instead of the
object table the object table is not
aware of your new
added fields edit tables yeah
you can use all object and that table
is kind of like a virtual table which is
aware of
these newly added objects
basically what i said now i like to end
with telling you what is possible and
not possible today
and i added some things
on the on the left column because the
right one was bigger than the left one
actually um
there is not too much possible today but
you can already
build if you take the the the rental
extension into account
you can build kind of like cool solution
but you cannot use xml ports you cannot
use web services
you can use web services when you can
publish web services based
on newly created objects in your
extension
you cannot use queries
reports you cannot delete objects
like creating a simple nav with an
exchange
so this these are things you need to
take into account before you start
obviously building an extension i think
and also yeah sometimes you need to take
a step back
from decent design like not using
uh add-ins but also decent code design
like not being able to create a function
on a table
we don't like that obviously but in my
opinion
this is one great step to effortless
upgrades i think we can expect a lot of
things in the
in the future regarding extensions and
i'm quite excited about this
so let's hope
that we will see a lot
more in the future i see that i have 16
minutes
so let's continue to the security part
now
questions
what user is executing code
when you think of just just any code so
we have a nav service there and that is
code being executed
which user is going to execute this code
who thinks it is the sql server
service account
okay i should have put another question
on this one
who thinks is the user account of the
user that is logged into nav
in 2016. so who thinks is the user
account of the user that is locked into
naf
who was the more i asked this question
the less people it will uh
will clap who thinks is the nst service
account
okay who of you oh what should it be
who if you think it should be a local
admin
who of you thinks it should be a domain
admin
that's a trick question and you're right
it shouldn't be although
that we notice that a lot of you people
of a lot of us let's say are creating
actually administrators as being the
service account because that's a
shortcut
i'm traveling troubling adding a service
account to this
service and i need to fix this
immediately
let's just add an administrator and i'm
on
that could be really a problem when
these guys
come into play
let me i'm going to show you something
that is a trick which you should not use
but which shows you why you should take
care
of your own customer installations on
this
again my opinion now let's
open our default
environment this one
and look
at this code unit notice
that in my environment
i'm the lazy one and just went through a
shortcut
and i used administrator for my service
account
actually you do not have to imagine i'm
a lazy one that is
quite a safe bet now
see this code one liners quite easy
actually just executing net commands
yeah with net command you can add users
no don't take pictures
you can add users you can add users to
groups you can even add users to domain
groups
if you have enough user rights
so if i execute this and notice that i
only have two users at this moment on my
system if i execute this
and i'm going to do that with powershell
because i'm
that crazy
just execute this code unit 50 000.
you'll see it's done the reason why i'm
executing with
powershell is going to open
an environment which i don't want to so
it's done now let me check this one back
you see that i created a user and even
this user
is an administrator i can create my own
administrators i can create whatever you
assign to the service there as being
the user uh
as as having the right so if you create
a domain admin
as being the service instance i can be
domain admin if i want to
i can log in with this user in my in in
this server and i can do anything
with this user but now maybe you do not
see the issue here but think hosting
i think that you have a number
of customers in a hosted environment and
this hosted environment has got server
instances
being domain admin i can in my
environment for my customers
upload the code unit at myself
a domain admin and and can
access about any database on that hosted
system
would you feel safe with your own
environment
no claps means no not safe right
help next topic i have 11 minutes
it seems that i'm gonna get there um
did you have uh do you have products
who of you have a product who of you
have got a
certified product certified for isv so
all of
those of you have created help
those of you should have created help um
now this help thing we don't like right
this help thing
come on we need to have a certified
solution and one of the requirements is
have an online help and this online help
has changed since 2013.
it's it's really online help like uh
now it's html and the robo thingy that
i've been using is completely not used
anymore now
another developer in our company had
actually quite a great idea
which i would like to share the idea
from
um i'm going to share this blog as well
he's blogging
all over the place and i really like his
blog um let me
show you this um
oh i'm going to to ask this question
i hope you have a manual for your
product
yeah so this manual is in word
yeah obviously when we have a manual
we should be able to convert to the
online help and actually word
is quite flexible in doing that
and this developer i'm talking about he
was actually
he has been spending not more than four
hours
on creating this great designed tool
not let's not go into the design but
let's go into the functionality
so what it does actually it reads a
certain word document i've got this word
document here
which is actually our own manual of our
own product
right what it's going to do it's going
to
save in the background obviously so it's
going to read the html so we can save
word as html
you can read this html you can even read
this html as xml
yeah and when you're in xml you can do
quite a lot
like going to all the head through all
the headers
like there is an h1 and h2 and h3
you can even set levels like okay how
many levels
do you want to have and the only thing
it needs to do is take the entire header
out
putting that in a separate html
file and then adding some kind of header
which is copied from a default help file
from microsoft
and some kind of ending so it's just
pasting that between these two headers
in html
and done and it's going to create let's
start this one i should have started it
already because it takes a while
now what we need as well is not only the
html files we also need
the table of contents now again this is
done with headers
in fact all the headers and a certain
number of
levels within the headers we can browse
through
so what this tool is going to do and i'm
a little bit struggling with the uh
with the resolution here it's building
this
table of contents so all we need to do
is take this
piece of xml and put it in the table of
content file
of the help server yeah so what we have
after
this tool has run is a result
being all the images that were in the
word document
being all the all the html files
and being the table of content and the
result
that could be let's
look at the help could be something like
an extra option in your
help server and being able to
yeah be having the levels that you just
exported
let me just show you this one you see
the pictures there's even references to
all
sub domains of this kind of things
so
four hours and you've got a help
that is certified this goes through
certification like uh
easily and you do not by the way need
the the
the help per field you don't need that
don't spend time on that if you don't
want to if you want to obviously
do spend time on that but this is
enough we built this especially for
being certified
the downside is if you have this all
customers want this as well
so now you need to actually maintain
help service on customers as well so
anyway i guess this is a is a positive
thing
the last thing i would like to end with
i've got six minutes
uh is nav mgt this is an in-house tool
but it's actually
what i call a box of outside the box
thinking
this is actually the the brain child
of of one of my developers
and about all prototyping that he does
he does in this product
we're using this internally what it
actually does
is it manages all navs for us
now i'm just going to share the ideas
it's about out of the box thinking i'm
not going to share
how to code or how it's actually done
um so what we have and what you have
probably as well is customers
who does not have customers okay that's
oh you
you are customers right um
but and these customer either on-premise
or yeah even actually i should
look into nav installation if you have
nav installations it is either on
premise
it is either on a laptop this one or
in the cloud separate pc anywhere
right and what we are trying to do is
manage all these installations on the
central place
what we did is built that enough
management thing
what is that we'll go into that uh if
you have time now this enough management
yeah if it needs to be able to control
stuff
it needs to be able to communicate with
that stuff
so what it uses is the service bus
you're all familiar with the service bus
it's just a thingy on
azure that we can use to easily
communicate with devices
or stuff or
pcs that also connects to this service
bus
so basically what enough mgt can do is
use the service bus
to manage all these things through
what we call a cloud connector so
we are building cloud connectors for all
the different customers that we would
like to manage
this cloud connector is small piece of
dot net
that is actually communicating one thing
with with nav
on on the on the one side but also
back to nav management
this case now it comes communicates to
nav management
with web services so it's actually
when you think of it nav management is
going to
consume its own well
let me try to show you a small
bits and pieces now i really want to
like to show you this because
it is a great example of out of the box
thinking
and again it is a tool set
is prototyping all over the place like
can we do this can we do this
can we do this and apparently this
developer can do quite a lot
um yeah
first thing i'm going to show is like
our clusters the worst
naming ever but our clusters is actually
our own environments our internal
environments we have 166 internal
environments which is basically all
our customers and our products
um let me go to our product
and what we can set up in nav
so as you can see it's all built in f
and we
create new dlls if we cannot build
enough
and here are our environments so we have
multiple environments for instance for
a certain
product now this product easy to
explain is an environment is a release
when you have a new release we have new
database new database new environment
right these are our environments
and obviously we have dev environments
and all that as well
now when we want to set up a new
environment
it's we give it a build number always
manage our builds
at some point in some way
and we set up the nsds we
do this all in this environment in nav
right so we create new nsds we create a
new sql server
we tell sql server like offl we tell
this setting like okay take a backup of
this
instance and restore it on this instance
and create a new environment for this
uh so for instance so if we set
everything up
i cannot show you this but we have this
fully
automated install then it's going to
push everything
and do the things that we just told him
to do this is for our own internal
environment this is where it all started
actually we want to migrate from a
really bad environment to a
really good environment which was uh
virtual so we had to migrate like
a ton of databases to a new environment
this is something that we needed to
script in some place and that is how
this actually
was born now one other great thing
uh is that we manage our customers
with it so we are in connection with
lots of
these customers and that means we can
push the installation we can monitor the
installation we can
get alerts of it like if the nas is down
it will notice it the cloud connector
will notice it and give us an alert
through web services and
it will pop up here and these kind of
things
lasting our consultants is using this
tool as well but they are using
another role center so using this role
center
a very slimmed down tool in fact
also some kind of connection points to
all these customers so we have
they have access to the same
kind of customers but for a reason
that they should be able to log in and
that was a time that we tried
to have some kind of default way to log
in at the customer because every
customer has
another way to log in there and we want
one way
and we already had some kind of cloud
connector and some kind of connection
with that customer
so why not build some kind of remote
rdp protocol from us
to this customer and when when we start
this one it's actually going to open a
port at the customer
random board open the board at our place
made the connection
and basically log in
to to the customer now this can take a
while because the first time that you do
this
and i should have done this before the
session then
yeah building dlls and all that takes
takes a while i've got
20 seconds
but i'm done actually just to uh oh my
god
just to resume uh or to go over it this
is the things that we do
with nav mgt and a few resources
as i said i would like to mention mike
knowles blog
okay the rdp is open now so it made the
connection and we can open rdps
we can now actually open rdps with any
customer that we would like to connect
to
every one of this on nav manager we can
have the rdp connection as well
now resources i would like to mention
the magnus block it's not
mango's blog by the way it's magnus
blocks really
take that one and two if you don't know
it yet really read it it's
good tips and tricks it's good out of of
the box thinking
uh i would also like to call vehicles
block there's no tips of vehicle that
i've shown today
but the e is the mastered and out of the
box thinking if you
if you ask me um
the powerful tips again uh powershell
scripts are on the github
and obviously if i blog i need to
mention that as well
i do not have time for questions
so all these t-shirts are mine
no really if you want to stay okay let's
have a few questions
five at most and i prefer yes and no
questions
is it possible to install two extensions
side by side
using the same ids now
yes so if you're creating yeah the same
ideas but it's going to create
ids automatically so it's going to be
different
anyway
yeah let me sorry um okay
questions because everyone is leaving
it's not going to work i will be here
for half an hour or more
just ask the questions
come over and i will just answer the
questions right then thank you
for attending the session
