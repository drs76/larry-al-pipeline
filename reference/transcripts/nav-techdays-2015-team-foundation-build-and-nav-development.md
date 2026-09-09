# NAV TechDays 2015 - Team Foundation Build and NAV Development

- **Source:** https://www.youtube.com/watch?v=4_zW_9twHas
- **Video ID:** 4_zW_9twHas
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 96m40s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

so welcome to you all thank you very
much for coming here in this big number
of people
after lunch of course don't fall asleep
keep on your spirit at least we will do
that for you also um
today or this afternoon our session is
about team foundation build and nav
development a couple of years ago i was
here to
talk about tfs using for alm
purposes this is a step further some of
you might have joined the workshop of
camille who did
no one oh sorry yeah yeah yeah yeah
we're only 15. so that's a comparable a
small group and some of
you followed my workshop
yeah
okay so uh for those who weren't the
most of you this is for sure our next
step we will discuss some on on the
beginning parts of it but let's first
take this start here and introduce
ourselves
we call ourselves
sometimes the bodybuilders today we call
ourselves the team builders
myself luke
you might know me from some of the blogs
and in this context in our team i'm
longshanks
you'll see why and be sure i'm not mr
mubusso so i'll don't send meals for mr
mibuso to me but do to him
next
my name is kamil sachek i'm from czech
republic and i'm mvp since 2005. it
means more than it will be more than 10
years
um working with the navy since 2001 and
my latest focus is on building an av
database on tfs
and my name is siren clemenson i'm a mvp
from canada
i've been an mvp for a couple of years
now and
i'm really excited about presenting to
this many people
so
let's go guys
the other way sorry
this will be the agenda for today
uh i'll give you a short well a
relatively short introduction to source
code management to set the base because
that is the part where
camille will step in onto you could say
the build part actually the core part of
today's session
you need that
and well let's get to that at the end
it's a
certain part of the show to
make a summary and we'll have a question
and answering at the end so
write down your questions and
we'll hope we'll have enough time left
to give you serious attention uh to give
you the room to
pose your questions so let's go to
source code management
why should you use source code
management
why do we use it there are a couple of
reasons for that and to be honest from
my perspective but having been teaching
tfs related workshops i know there are a
lot of other perspectives but there are
a couple of reasons why i don't use
let's say traditional enough development
having a centralized database and that's
where everything happens so one of the
reasons is why was a change done of
course you can track it with any other
change other system so you could say
basically the requirement we want to
record that in a system like a team
foundation server it could be another
one
what does that change actually contain
so it's not only the why but it's
what has it
been what is the code change as such
so who did it you could say it could
feel like a big brother and in a way
yeah you could use it like that but it's
more the other way around
if you know why who did it and what he
or she did and something went wrong you
can learn from that you can learn from
each other also having the possibility
to see hey
somebody else did it like that why
where did the change actually go so
you can track where it change
yeah let's say the flow of the change is
going so you change somewhere in your
system
your whole structure of code and you can
bring it somewhere else
and last but not least in this list is
what changes have been applied so
history-wise you can always refer back
to the
change you've done a year ago or
whatever so
you have a full-blown let's say
a register of
these kind of
matters in your system that's a
the main reason you could say why we
started to use this
kind of system
so
um
why should you use it now or why should
now be a point to start using it
considering it
investigating it of course
enough as such is moving forward and a
lot of things are changing
microsoft is in that sense sometimes we
feel like that imposing things up on us
you have to go to the cloud you have to
or you could say the other way around
you get the chance to go to the cloud
however
nevertheless how you look at it it
determines part of your
development practices so
can you deliver your changes or your
software as such
on time
with the speed for example of the
cumulative updates we get are you able
to get your
add-on your solution
upgraded after the last cumulative
update before the next one
with the managed service or you could
say the whole azure paradigm or the
cloud paradigm are you able to
provide your
solution to your customers on a regular
basis
and there is more to manage than enough
enough source as such we have powershell
which
we have seen a lot uh
that's also
source code and how do you manage that
how do you version that how do you
version your code for your client
endings
from let's say
a net perspective it's an everyday work
using visual studio and team foundation
server together from let's say the
standard nav practices most of our us
are used to it's not that common but
okay how do you bring these two together
on a
versioning system the same applies in
general for net components
so
um
let's say this is a bit why you should
be doing it um i'm using this schema to
tell you more or less a bit how the
system works uh camille will show a
short demo on this part also and later
of course use it when showing and
talking about the build system so the
source cost management is all about a
central
code repository which is put here on the
right side
in
our setup we're both or all three of us
using team foundation server as a layer
up above it uh camille and i in our
situation we are using team foundation
serv or team foundation version control
system as our code repository in the
case of camille he is using git
microsoft has built an in a connector
from team foundation server into git
you could also say this story applies to
another kind of system like perforce
or well many others probably but not
that well known maybe to me
it's all about having a central
repository where your code is and that's
the truth it's not a central database
development database but it's the code
repository that's where everybody hooks
into that's where everybody syncs to so
there is a bit of challenge of course
this central repository you will copy
with this update action to a
local workspace and local could mean
really on your laptop as a developer or
on a virtual machine so
you draw a copy from that and as that is
a local file system it's not yet your
database so your development environment
you could say
so we need to sync these two together so
get the data the the object files being
text files into our
development database and there is what
we do the work and if we finish with the
work we update our workspace and from
our workspace we will update check in
the code that's the
wording for
team foundation server checking in or
pushing your things into the central
repository as git calls it so this is
actually the basis of
the whole source code management and the
basis of what
camille will show with the build you
have a central repository and let's say
workspaces where you
copy files from the
repository and start using them
this is what we call developer isolation
we share the fact that that we want that
i know some others do think differently
on that but that's a personal or a
company choice this make enables you to
really
develop in parallel without touching
each other's code
so i can start developing something on
code unit 18. camille can do something
at the same time on his local copy and
later on the system team foundation
server or git will help me to merge
these things but they're stored as two
different versions so i i can propagate
my change
or camille's change separately i can
propagate them
two together so in the sense of
releasing or bringing to another branch
in the system
so
come here yeah a short demo
time for showing something live not only
the presentation here
please switch
no the other way around now yep okay
thanks
what do you see i'm not you again not
see
yeah now it's okay
let it be don't touch it
that's a
graphical user interface for git
that's
it's a git extension because
there is many
clients for git on
on the market you can select what suits
you more
i selected this one because
yeah i think it's really simple to use
and you can extend it it's open source
it means i
changed something to extend it as i need
it
the main part is
history of
our databases of our development you can
see there are
different branches for different
customers or our products
with some
comments for each each comment which is
inside
there is
who made the change when it was done
there are even the informations about
how the build of this change
was finished if it's okay or not we will
talk about how to
we can manage that
and of course i have some information
about
the specific commit specific change
which is there there is some comment on
that
even when i
select one
some other
change here
i have a link for the requirement on
which
it was based or created for for which
requirement from customer for example
i can see
the difference
it means very simple way how to look at
what my colleagues did in in the
database which changes were done
i can see of course change of the of the
header and i see a he added some actions
and some variable that's okay for me i
can review this change
and maybe give him feedback that sorry
that it is not okay change this code or
yeah that's a nice nice solution for for
the
for requirement
and of course i can see the
result of the build here
if i need it
sometimes of course something is red
and i can blame the the guy why you
broken my builds there and like i see
okay there are some errors with
importing objects and
maybe arena renamed tables or something
like that
that's the
client we can use
um i will show you
how we are using it
first
things is
i have some requirement for example on
my tfs
i will go there
i'm using visual studio online for that
i can look on my work
i see
that there is one user story
that my or some finance departments
want to block new item card when it is
created until someone will fill the
product
posting groups
some consultants take that created two
tasks
first to block the item when it is
created and second task is
don't allow to unblock it until the
posting groups are filled in
i'm developer i take that tasks
and i will go to the
git extensions and i see okay
i need to work on that i
for example want to start with my
database because i i want to develop it
locally on my machine
i don't have central database for
development
uh i don't have the database on my
notebook now okay i just click create
local
and
yeah that's
what
sometimes happen
each time when you prepare something
and you don't restart your computer
that's the case
and something will stuck somewhere
just try it again
now we are yep
it seems that this these two days in
antwerp doing something
just waiting for uh for tfs to return
the results now
i just enter where i want to create my
database
and the script will
yep will not do it because i'm not an
administrator yeah
i need first to to
be another administrator
again
open that
go there
wait for the tfs to return my my results
of the builds
because we are online
speed of internet is not so
high we as we want
and after the results will be there
i will i hope last time try to create my
database locally
and now yeah it's starting to work
first
it will restore some database from some
some backup
then it will create service tier for
this database import license into that
update my objects on
on the on the database to be on same
level as the repository with same
objects inside the database
and after that's
finished
i can start develop it should take
around two minutes
of course adding me as a super user into
the database because i want to test it
uh yeah
the user is already there there are
errors but we can ignore that
uh i
yeah doesn't matter i'm still there as a
user
now it is try importing some fob file
with the test suit for example first
to have the test suit there going
through the all the objects in
repository comparing with objects inside
the
table of the database objects table
and importing only what's different
of course after we compare the objects
we need another
go and check if there is something
deleted in the objects because
yeah i'm comparing just the existing but
i need to find out what was deleted in
my repository for example to delete it
into the database
but still we are now up to date
and i can start to develop i just click
see site
it will find
the correct version of nav on my system
and run the the development environment
and connect me to the database to the
correct database
i can really
forgot where my database is and how it's
named doesn't care about that now i
start to develop
of course
i will create some new code in it
i will use of course new features of
2016.
first i need to set the blocked fields
on creation of the item
it means i will create function block
item on the insert
it will be
subscriber on table 27
i think everybody knows that what's
table 27 here yeah
do you know the number of the bicycle
okay
on before insert
yes that's all
and
to not write the code i prepare the code
already here
i will just push
the code here that's all
first i will check that i am not working
with temporary table because events are
called even for the temporary tables
don't forget about that
it's dangerous
and then i i will just set the field
block that through after
when somebody create the the item
it will be
blocked and then i will create another
function
check posting groups
on
unblock
of course it will be again subscriber to
table 27
this time
on
after validate event
of the field blocked
i will put second part of my quote here
again
checking if i am working with the
temporary table or not checking if i'm
going from block to unblocked
and when yes then i will test my two
posting groups fields if they are filled
in if not there will be error
and the user can't change the the
blocked field here
while you're doing this uh camille
you're only working at this moment in
the nav database yeah i'm working only
on the nav database
nothing else i created or
processed two tasks i have assigned
and just save save the
the objects on my local machine it means
i don't care if somebody else is working
on the same
objects
this time i created my own but
yeah
if i change some existing i don't care
about that right now
i'm done i just close my
my client and go back to the git
extension client
and say okay
i want to
synchronize
nav to my git repository
it means i just click the button enough
to get
and again there is some powershell
scripts
publisher script which goes through the
object table compare everything with the
files on my local file system
and will export only the changed objects
and again we'll check for deletion of
the objects to to handle the if i
something deleted in the database
and this is stored locally as you said
it's still locally yeah working with my
data
my
database and my local file system
we have
30 minutes to 30 seconds to finish that
i think it will be quicker of course now
i could just manually export the objects
it will be much faster
but if i'm working and doing some more
complex changes
yeah i don't care which objects i
changed the system will will find it
itself and there's an additional thing
to that there because enough if you
this is just a simple code unit but what
happens if you change
the name of a field yeah more objects in
the problem yeah the problem is if you
are
renaming something
you touch one object but codes changed
in many other objects you need to to
have this in your mind
uh in this case i can click uh
not any nav to git but nav to get all
and it will take all the objects export
them
uh splits the big
text file to to small one and overwrite
all the the objects it means git will
find what was changed everything for me
and will automatically offer me
committing these changes you mean get
well this define find out that there are
only five objects influenced because
yeah because i overwrite all the files
and he knows what's changed from the
last commit okay and we'll offer only
that
we are finished only one coordinator was
exported i was just going to say you
just have the only thing you got to be
careful about that is if you're doing
deletions
at the same time as you're doing renames
because the deletion will not be picked
up if you do an all yeah
the process will check the deletion
after after that too oh you have built
that yeah okay
yeah i was thinking about that
he's called keen
that's true
now what we can see that
on the commit button i have number one
it means one object was changed
it's new new object okay
i will transfer it
first time seeing this dialogue for you
i will describe what we can see here
the
top left part is a list of changed files
this one
the parts
under that it's what i want to commit to
the to the git
right side is all the changes which are
inside the selected file
here we have description of the commit
uh i am using some template i will
override the template
in a while
and then i have the commit button to
commit this change to my local
repository or i can even
directly push it to the server
so the difference between commit and
push that is commit just puts it into
your local repository on your machine
while push pushes it up to the central
repository yeah yeah
exactly
but
now i can see that i have two two tasks
here i
finished
by this change number 35 and number 36
i don't want to have them in one comment
because i want to to to link one commit
to one task and second
commit to to second task
git allows me to do that that
i will just select part of this change
this second function and i will say
i don't want to commit that and i say
unstage
and now we can see
into my commit
will go only this this part this this
object with one function
and still in my directory is
change
of these objects
prepared for committing
you lost one begin sorry you lost one
begin in your other file oh yeah
then again i will just
select
this part
and on stage
now it should be correct
camille if i'm right if i understand
right you want to split these two big
although they're very small and it's of
course like a stupid example in a way
but you want to have them as separate
features stored in your system so like i
said before that you can
decide whether you release the one or
the two or both of them yeah exactly and
to see okay for this task are
did this change and for this task i did
this change because some
relations there and that also
becomes important at a later point so
this is just standard source code
control or management
and
very often if you have multiple tasks
you check them in one
what if the customer then asks at a
later point can you give me tasks that
and that i want that promoted but i
don't want this one promoted because
that's not good yet
so if you don't do the check-in
you don't do the check-in separate
it becomes a lot harder to manage what
you do deliver to the customer what you
build on at a later point
i just between that's uh committed my
first change
i will commit my second change now i i
have only a second
function inside it and i'm using in
commit a hash and number of the work
item on the tfs
commit that
and now you can see in my history i have
two commits here number 35
and i can see the difference here of
course for each of them
and
i'm still working locally yeah
but my development branch
which is used for uh putting
finished development
uh to to separate what is finished and
what's on my local machine just in
progress i need to to merge it there
i will switch to this this this
branch
okay now i'm in this branch and say okay
merge into that
this change which i made here so before
you do that camille can you just try and
explain what the uh
what the train wreck over there on the
left side is yeah
uh
this is very nice feature of git that's
showing you the tree of your history if
you have some some
version of something
you are continuing in this way
doing some change and then you go go
back and
create another change here you you split
the tree
and you can build on these and split on
split and split or join and merge them
back yeah that's all about
splitting and
and merging together
different versions
and i click only merge into current i
have some setup here doesn't matter i
will just merge
and everything is automatically merged
because there is no
conflict and now i just only push all
the changes to my server
and i'm finished finished with this demo
so
yeah
so that's the the source
management part in the sense of how do
you put your source in the system uh of
course
like you saw part of
this setup has been automated and in
that sense it becomes part of your
everyday
habit everyday work
let's say apart from the list what we
would like to register in the system in
general you could say what are the
benefits of the system
that's the way we experience it is first
of all of course it's a matter of
securing your code whatever happens you
have a centralized database
with git you have it could have it more
distributed before you put it in a
centralized database with dfs the setup
is i'll get to that in another slide
also tfs is a matter of centralization
you set up the structure there and
everybody hooks into that with git you
could start up distributed separated
from each other and decide later that
you merge everything into one
centralized branch but nevertheless you
secure your code there
apart from the fact if you would say
i want everything to be the truth as a
truth in a centralized system and from
that we build our databases or we have a
centralized enough database and we use
that repository to make a kind of copy
of it
both
is as a purpose to secure the code
one of the things is that you have
history at
hand i know
quite some partners who have built
something up on sql server triggers so
when changing something in the object
table that you create a copy in another
table etc that's also for history thing
wise but
systems like tfs already have that in it
you don't need to take care of it or
maintain that
and you have a lot of possibilities to
easily compare and and look longer
histories etc
one of the things uh
i surely do i know
cern and and
can we also strive for that is
what you release or let's say the other
way what you build either a bug fix or a
feature you put it in one chain set
that's the goal so you have that package
you could call that the delta file you
which you could put wherever you want in
your system or when you want to go and
release it one other thing is
automatically part of the system in this
that you can easily roll back you have
committed
and pushed a change or as you call it in
on tfs you have checked it in and then
you find out this was wrong you can then
easily roll back that whole
chain set and
well get back to where you were
another thing is
through this which is a not
let's say a deliberate thing of the way
we work here is that we have text files
going outside of the system is that you
have a better overview on the code my
experience is that i have a better
understanding of the code we have around
our company while if you sit only in
enough database it's like opening one
window and then you see only half of it
i and i'm
often having the role of a merge master
i have every code almost in my view so
next to that the system also supports
the fact that you
ask each other to do code reviews
so code improvement is a benefit of
using a system like this it makes it
easier i don't say it you can't do it
differently but it helps you a lot
i already mentioned tfs and git and
camillus is using git
both are used by many so if you build
your systems yourself of course you're
free to do that but you maintain it
tfs and git you can profit from
experience and and and and
new requirements brought in by many
others and there is a lot of tooling
around it also available
both systems are apis so what you want
to automate and which is things which
are not standard available you can do
yourself
okay
well
it's not rocket science in the sense of
totally new it's not a a a kind of thing
with
advanced
powershell as such you can do it the
system is simple
but
well i would see it's like a friendship
you cannot do without it i mean
i've i tell in my workshops every day i
started with
working with tfs i open up visual studio
and there's always and it's not yeah you
won't see it but internally there's
always a smile on my face i'm
well
very happy with it
the last part um
let's say the source code management and
then when you really well camille showed
you actually already part of the build
thing but then we go into the details of
the build
put git and team foundation version
control next to each other what are the
difference why should you choose it well
first of all as i mentioned tfs is a
fully centralized system you have to
build up your structure there and
everybody let's say hooks into that it's
not like that you build up something
locally and then you can easily
hook into the centralized system now
you can by copy and paste but you have
always
built up the system centrally in my
situation working mainly at an end user
we have one product we have one group
working on it on the other hand if you
have a team
working with different kind of projects
which might be related you don't know at
first or you expect them to be somehow
related later you can start with git
a bit more easier in that sense that you
can start locally and then later on
decide to combine these two yeah
of course both have have history at hand
that's one of the
main parts which is a an added value to
the whole system um branches is a thing
we will not discuss it specifically here
i've
used i use it in my workshop
but it's a very powerful thing of saying
okay this is our product and we need to
do something now
probably mostly building a feature so
let's take a branch of that and start
working there both
systems help you to do that with git
your have
more let's say
unrestricted
situation
everybody could do things locally and
then later decide to put it in the
system in tfs it means you have to make
a branch in the system it's there start
doing your work but you can always
decide in both cases by the way to
delete it and work finished get rid of
it
as
tfs is very close to visual studio it's
highly integrated so
anything you do from a net perspective
is
let's say fully
linked to tfs
with
git there's a partial support on tfs if
you want to use clients that so you have
visual studio for your source code
management with git you have a couple of
other possibilities also i will only add
one thing
microsoft is now really trying to catch
up with the git
integration to visual studio it means
you really with each update
could expect more and more features for
git inside the visual studio itself
it means really there will be changed
changes and you can really see them in
visual studio 2015 already going that
they will be adding each each update new
and new features there it means
it's just about now but in the future it
will be on the same level yeah i think
the
i think one of the reasons uh
look and i really love tfvs yeah uh it's
because we old
and and we're from microsoft i do know
that
git is old too yeah
we used to be
of course in the end it's what fits you
best yeah and these are two examples i i
mentioned before also as a source code
management system which is a very neat
one too but it's up to you
we're just mentioning it here um feel
free to ask us if if later on you think
we need some more information it's not
the purpose of this session to really go
into that part and maybe uh it's not
only about what fits you but maybe what
fits your company because maybe you have
different parts of your company working
with c-sharp code or another code and
they are already using some system
true yep why to use new one
yeah okay
now we're really into the build part
yeah
lights out
the build part which is the
main focus of this session
for this we
first need to say something about the
architecture of the tfs one question
who formula is using tfs now
yeah a bunch of people
who already heard about tfs
yeah thanks
who is using tfs only for work item for
alm part not source code
only
managing work items there
nobody
really
look there's one over here
your workshop is yes
there are only 15 people there
okay first the architecture
you need to have tfs server first
it could be online
as
i am using during the demo but you can
use on-prem tfs server if you want
doesn't matter it's on you if you want
to keep it manage it manage it or or not
then
tfs server is using some sql database to
store the data
during installation you can use sql
express or you can use your own full
full version of sql
you are you already have somewhere
then we need some client to access the
tfs to for example push the
changes or
changes of the source code there or
change the templates
we are using during the builds
tfs have own web portal
which you can use to access the work
items the the history of the objects
history of the beards or all these kinds
of things could be done through tfs web
portal and of course it's more and more
extended with new features to plan your
work and so on
then there are two two additional things
to connect tfs to project server or
sharepoint
of course we will not talk about that
that because it's really out of focus
this of this session
but last part is build controller
which is managing some built agents
and
we will focus on these parts we will use
tfs server
we will use some web portal of course
short time we will use some clients the
visual studio or git extension and we
will talk about the build agents or what
they are really doing
okay how it works we already saw that
it's a variant of what already look show
us it's the central repository center
our git repository in my case i have
some pull action to to download it to my
local system work with it update the
local repository and then push to the
server
so what what
that's the development isolation yeah
this developer isolation yeah
is there an option to do this with uh
let's say
i'm using it like that but like i said
there are many of us who still or who
wants to continue working with the
centralized
developer database i i
would think about that i see eric for
example here
he's using centralized database
for development
yeah we can use that for centralized
development too
just by accident i have prepared that
for you
if you have centralized
database development and you already
have some version control system which
produce text files somewhere
it's not a problem to push these text
files to the git repository
and you have the central git repository
and you can work with it as
in case when you are using the
development isolation doesn't matter
from where the the files are coming
yeah
and over the centralized
repository we can
create new process which take
the objects from there
or some some other data
will build the database for you we run
for example some tests or do something
else
and then return back some results which
are connected to the central repository
so so we're now going to focus on the
upper right side i guess yeah exactly
but
first
we can do of course the same for tfvc
yeah okay not only for the git you can
see now the same picture for tfvc
when i will go back you can see that
nothing really changed there it's only
about about the naming
it's still the same process
stay same building blocks
and we will really focus on this part
now
all right
but before we go to some demos and more
detailed things
question is what does it mean to build
yeah
what does it mean to build an av
database
because we need to think about that
sorry
compiling
what
where
yeah
it's it's only the middle part of that
because to be able to compile you need
to to have the objects in the database
you need to create a database somewhere
and
for example to import something on
compile you need the service tier even
there
unlicensed
maybe external libraries
add-ins
yeah it's a bunch of
things you need for that okay there are
the steps as i uh see them
you need first to prepare your
environment
if it means
create virtual machine
install nav there install something else
there it's on you
i will take it in simple way i will only
create the
database from some backup i already have
some secret somewhere i have already an
av on the machine
we have i am not not building from
scratch
i will create the database first
then i will create server instance for
this database
i will install external components on
this server to be sure that i have all
the dlls there in correct version
and i will import my nav license to be
able to do all the things i need
second step is to update the objects
inside the database because the backup
is maybe old maybe there are no all the
cumulative updates because i made the
backup yesterday and today there is new
cumulative update and this cumulative
update was already downloaded by your
automatic script to download that
from the
blog article and
it's already somewhere stored and maybe
your product is already updated
during the update we first import the
some fob file
question is why i'm importing first the
fob file
you know that
everybody hit that yeah
yeah exactly new fields new objects
yeah maybe
the backup is really old and new
cumulative updates are adding fields
adding objects you can't create them by
text file
then i imported all the text files
inside my repository to this database
and compiled these objects
the all import of text files
i think there are some exceptions you
cannot import
how do you handle that
by importing the fob file okay but then
you exclude them from the import like a
menu suite
uh
yeah
of course it's just about the process if
you hit some exception yeah i can
i can't import
when you suit
then you need to skip it all right yeah
and you need to import it through the
fog file
next step is to
test the database because why we are
doing that we want to know that the
database is okay it's working everything
is inside
working as
i want i didn't break any standard
functionality now we have 15 000
automatic tests in test suit
you can run them
okay it will take four hours to finish
you don't want to run them manually on
your machine
yeah use the build for that
it means
yeah but first
which test to run
maybe it's part of your builds
build process to find okay i change
these objects i need only run this and
these tests because they are affected by
by these changes
then we run the tests
and we are going to next step we need to
produce some output
and again it depends on what is output
of the build for you
in my case it's
test results
i want to see the test results of course
somewhere and
see the history of that then i need to
create fob file because maybe i will
just take the fob file and import it to
the customer database and customer is
updated maybe
and then maybe we can create and publish
netflix file
because we are creating extension
i don't need to do that manually the
system knows from where i am going
where where i am now can create the
deltas create the extension and just
provide me as a result the extension
enough x file
and then if you want optional step to
deploy this output somewhere for example
to update some database somewhere else
and and so on so so now we have a kind
of recipe or the ingredients of the
recipe exactly okay that's the steps we
need to follow to
to cook our build okay
when you cook your build
one of the things
that is always
surprising that is it takes so long
because i got to import all the objects
are you importing all the objects every
time are you importing just some of them
so the differences here sometimes i
don't have enough time to cook a
whole whole food
sometimes i'm using some
prepared things and of course i can only
import changed text files changed
objects and compile only them
when i need only quick quick overview of
it all is okay and i expect that when
i'm releasing somewhere new version then
i'm importing all and compiling core
only yes so that's always a good idea
when when you are when you're building
or you are ready to deliver that is to
do the entire build from scratch
uh a mom's cooking always tastes better
i mean
but
when you do the entire build from
scratch you catch things you wouldn't
catch otherwise
when you're just importing changes i
mean this microphone it's micro
wave
food right
you do it fast
it doesn't import all the objects that
might be somebody has done something
that you didn't catch it was a field
name change there was something that
changed that you didn't catch
and so when you do bills and you do
releases it's always best practice to do
an entire build from scratch from the
standard database
of course you need to import whatever
add-ons you have that you don't have
permissions to insert but do it from
scratch
now we have the process but what about
what we need to build it
at all what we need to build first we
need someone who will build that in our
case it's tfs build server
i'm naming it bob
because everybody knows who who is bob
dan because bob is building for us and
he needs some tools first powershell
scripts
ask eric he will he will help you with
the scripts if you need
bob
of course we need some build template
which is describing this process we
already
saw on the
on the powershell above a powerpoint
powershell power bi power everything
yeah okay
powerpoint
then we need build definition which is
instance of the template it's it's
specific built uh setup for some
specific database
then we need parameters for this build
because we need to know what to build
where to build when to build and so on
and then we need something which will
trigger the build which will start the
build for us
okay about the powershell scripts
uh
we need for the each of these steps we
need to need powershell because
powershell is really doing the job for
us
and where to take them because really
developing it it could take a long time
first you can do it yourself if you want
if you have time if you have knowledge
or you can use some which are already
there
you can use one from my project on
codeplex
uh it was
it is there already i think more maybe
around the
year
[Music]
or you can use
scripts which
eric already published
because they are all the
steps you need you can create the local
environment or something like that you
can build the scripts from these these
functions there
and look
watch my blog because
i want to blog about how to create all
the things and
all of you who attended my workshop you
already have the scripts uh i will
publish them on my blog uh in next
few weeks
okay
first something about the build template
what we
have
as an option to create a build template
first
there is version of of build template
which is done in xaml
xaml it's a
xml
format
it's used by a
microsoft workflow foundation
it's based on the windows workflow
foundation
it have some activities creating complex
workflow you can have repeat until try
catch
if then else and everything inside
uh
of course there is no
built or prepared powershell support
in these activities there are really
really limited support for powershell
just run them through the command prompt
but you will not see
all the results in your build then
of course the build agent for example
template exists only for windows but
it's not limit for us we are still on
the windows only
uh in tfs 2015 there is a new build
system which is named tf build 2015.
it is based on web and script
or and scripts it means you are
developing the template on web portal of
tfs
and you are just adding some scripts
there which will be run on the agent and
the activities there are defining each
step and there is only linear linear
execution of these steps
and there is native support for
powershell it means you can use your
powershell you will see all the outputs
errors warning directly during the build
without any other
customization needed or something like
that
which one should i choose
which i
which to choose
it depends on what you are expecting
from the results uh xamarin is here for
a long time but it's more more
complex and
harder to to change
uh the tf build 2015 is really easy to
create and use but it's too new and it's
not
connected to everything around for
example some reporting is not using it
for example the git extension is not
connected to that don't see the results
of this build but it's question of the
time but it's really easy to use if you
are just starting and you want to
something to use use the tfs
tfbo 2015 if you have
if you want to have all the
complexity use the example
but i think it seems to be clear that
microsoft is is making the move
so that the the future will be the
powershell or the tfs build 2015.
so
if you're just starting out use tfs
build 2015 if you've already been using
it for a couple of years you are
ensemble right now so you probably have
some complexity that might not be
available in the new one yet
so you can start moving it but
the the reality is that that
that's the future anyway
tfs built 2015. so exactly
and
the tf build 2015 even have the native
support for github repositories it means
you can build a
source code which is saved on github for
example and it has support for different
platforms but yeah
we
don't care about that
how it looks like
yeah it's
you can see here it's the summer
template in visual studio
it's um it's somehow a visual
programming
when you just just drag and drop the
actions and connect them and
set the properties here or you have the
tf built
system with the different steps
creating
importing
running exporting publishing until you
are done
just short very short demo
oh sure
please could you switch me
number six i guess i'm not allowed
anymore
no surely number six here we are in
visual studio uh there is the
my
xaml template
which is really really long in
and you can see all the steps here
i'm running some coordinates
i'm running
compile import and so on but still it is
just running some
powershell scripts here yeah
you can see it's visual basics
you need again something to write the
expressions
now cil code c sharp visual basic yeah
it's
zombify
definition and now we have
even the
tf builds
definition
yep
not there i will open that
sorry wrong
and you are really you don't need the
visual studio to create these
definitions
and they are just looking like that
really different steps different scripts
here
and
you have just some
settings here variables and so on you
want that's all what you need it's
really easy to start with that
that's the demo
yep
about some build parameters we need for
the build
we can select if we will have them in a
template as a part of the definition of
the build
they are defined by the template
they are configured when you are
creating the build definition or you can
define them when you are queuing the
build when you are requesting build
something for me or you can have the
parameters saved in your files which are
a part of the repository for example in
some xml file which i'm using on most of
for the parameters
because
when you want to change them you just
change them save the the change of the
file push it to the server and the build
will use them
there are the examples of the parameters
which i am using for of course the build
server needs to to know where is the
sequel server how named the secret
database uh where is the backup where is
the fob file where is the license file
to use which version of nav it should
use and all these kind of things
you need to store and tell the the build
camille these are these are typical
parameters you've set into your template
yeah because this is specifically enough
but there's a part of course which is
let's say default
tfs
where you
let's say let the system create a new
number for the build so every build has
an identifier
yeah of course there is some standard
standard parameter
built name which i'm using
in the in the templates and i don't need
to touch them i just use the result of
this build name uh
build name in my scripts to for example
name the fob file which i am producing
okay
parameters demo just really short again
here i have my parameters in summer
template
which test coordinate compile drop
for the last build the drop server
varies of if i want to force import it
means i want to import everything or not
in xaml i need to add some metadata for
each parameter it means there is some
metadata parameter i can add my own
parameter here name it somehow put it
into some category
describe it and set some additional
parameters
that's what i need in the xaml template
when i go back to the
tf
2015 beards system
i have
just variables here
which i can create i will just name them
just put some default value and that's
all what i need
because
in my scripts
i will see them as a
environment variables
it means i can just directly access
these variables in my scripts and i'm
done
that's all about the parameters
how to put them into your your template
then we need some build trigger
which could be manual it means you must
trigger the build to to run
you need some button to push that
you can have continuous integration it
means it is building each commit each
change that you push to the server it
will take it build it and
send you back the result
or yep for each commit and checking
or you have rolling bills it means it
will take all what it was not built yet
and will build it together and after
that maybe
after one hour it will again take
everything what was there and build it
for that
then we have a gate check-in
it's currently only 40 fvc but i can
expect that it will be for get there too
but
it's hard to explain i don't know how to
explain maybe you shall not pass yeah
that's that's the explanation of this
uh because
here you have
your change
build process and tfs server and if you
don't
pass the build you will not get to the
server with your changes that's very
good thing how to prevent your product
be
broken by different changes of your
developers
if it will not go through the
build process correctly it will not get
into the product at all
and then we have shared you scheduled
nightly builds for example if you want
each night run all the tests and see the
result if everything is working
on your product
just look at that
how it looks in visual studio
again
when i go
to the part where i want to
define
new s3
this server is not access accepted
i need another one
did you notice the really nice name we
have here for our
online version
you mean the ms9
thing enough or
yeah it's very
taking some time here
but
yep we are getting there
i want different one i want the git
i am here i i have builds here
and for example if i go to the
definition of this build
i have some triggers here and manual
continuous integration rolling rolling
builds i can select after 60 minutes
maybe i won't
take the batch
um i can schedule my build as i want and
the same thing we can see on on the web
version i can select continuous
integration
batch or not
or i can schedule it for some time or if
i will not set anything it will be the
manual version of that
that's all about the triggers
build demo
yeah we are going to to look at the at
the result
of the build because uh on the beginning
i made some change
and now i want to see
what
was done
in that
so we don't have a drama with a wrong
you'll be waiting for this now 15
minutes or whatever this is what it's
all about we just just some talking and
chit chatting first first i will go to
the my git extension client actually
first we got to run the entire build
which would take the next five hours so
you have time
now i i use the differential build only
to build
the new change here
i will refresh the view
wait for the results from the build
server and you can see that there is
green everything is okay it takes
three and a half minutes to build the
database for me
it means
the database already existed
objects were there it only updated the
new object there compile it export the
pop file for me and everything it means
all is okay i will go through to my
visual studio
first
i will look at the at the work items i i
had
for this this work
i can look here and i see
that
this work item is associated with some
commit i made that's the first
connection i have work item i have
changes it's it's connected together
then i have associated some build with
this work item
i can see there
there is the my build
this work item is part of this build
because
there was some commit during the build
which was built on my build server
too much builds everywhere
okay now i will go to the builds on my
tfs
i will look for
my definition
it's this build
i made 36 minutes ago
and the result is succeeded
run for three five
minutes
uh there were
few commits
connected to that because there was one
merch
and the two commits which were put
into this merge yeah i can see the
commits here
no test results and i have associated
work items even here i can click and
look at what was built in this build
i can click every everywhere and look
for example which changes were made in
in this this part and i can see it was
coding
50 000 and edit this function here
so bearing in mind that slider head with
the y and what whatever this is actually
a next step to it where you can
through the system see we've built a new
version and what is part of it or what
has led to that build
exactly okay
when i will go to another build i made
few
weeks ago
for example here you can see that
i have some warnings during the build
but it's just about waiting for the
service to to stop
and start but there is some error
message that 71 tests were not past my
build
it's why the build is
partially succeeded only
it's true
it was okay but not fully
all was imported all was compiled
but the tests
there were some fails
in the tests
so now we can go hunting for whoever
broke the build
yeah yes of course
i can hunt him because i know that it
was this commit
and it must be part of this committed
change it means also it's you yeah of
course
and this build is only for czech nab
2016 the release version and i can see
on even the test results here i just
click i see the numbers how long it
takes but even i see the test results
here for each of the tests in test suit
and of course i can find
through the future
come
is
failed
and i
i can see the tests which failed
on the server and i can go there and i
can see even the error message from nav
why it failed
and now from there i can create back in
my
work item system assign this back to
somebody please look at that correct
this this test or correct this why it is
failing yeah
and
we can go another
sprint in our scrum for example to solve
this this kind of things do you have to
do that manually for all those 71 or you
have also automated that
the bug creation the tests the bug
creation
the bug creation
could be automated for the build if if
the build failed i can receive uh back
for the build but if i want to create a
bug for specific error in the tests i
need to do it manually now but of course
everything could be automatized because
tfs have ep api which you can use and
maybe you can use the api in a way
like
rntn show you and because the api is
open you can use it maybe directly from
nav if you want and quite often if you
if you have multiple fails in in your
tests
quite often those those failures
they are caused by
one or two things
so quite often it's it's a valuable that
somebody actually looks at the system
instead of creating 71 bucks and
assigning it to all kind of different
developers that all look on the same
issue now
so quite often it's it has value to
actually review your your test test
results
and and and
create your box based on uh a manual uh
review of it yeah exactly that's all for
my build demo and now it's
your turn that's my turn so i i do get
to speak today
yeah
first of all i think we should we have
20 minutes no no no first of all i think
we should have a hand
thanks
so camille has worked on with this for
years and uh for a long time i think at
least
two three years two three years now and
uh it's
luke and i we were we were already doing
a lot of uh source control and talking
about it a lot and when we heard about
all the stuff he was doing we just had
to have him in here
uh it's uh it's i think it brings it's
kind of it begins to end the
the entire circle of why we why we're
doing things
so
what does the future look like for all
of us in here
microsoft is delivering product faster
and
faster um
they expect us to
do the same
if we want to do
[Music]
what microsoft is hoping that we will do
we are going to be doing
delivering faster and faster we're going
to have monthly releases or updates to
our customers or to our multi-tenant
environment cloud storage or cloud
solution
but we also are expected to deliver
really high quality
especially if we come into the multi uh
these the cloud solutions and and the uh
multi-tenant solutions
it becomes a really big um
big issue if if we don't test our
software properly
and then there's of course the cost
the cost of
of our competitors
are always going towards zero
maybe not zero but at least they push it
down right
we need to be competitive
uh if we wanna
in the one-off solution market
which this still covers the still deal i
have lots of customers that are just
one-offs we run them all through to the
system
but especially when we want to start
putting pushing the cost down we want to
be competitive competitive in the
in the multi-tenant market
cost becomes a real real issue
and
using source source code management
using tools like build using tools like
test testing tools bringing it all
together
automating it
that's that's the whole foundation of of
bringing the cost down
if we don't bring the cost down we're
going to be killed by everybody else
so we've got to bring the cost down we
cannot bring the cost down without
automating we cannot automate without
doing proper source code management
so automation is the key here
to to do everything that we want to do
to to be competitive in this market and
that's why it's very key
that you all think about this you all
start working on in this direction right
so what do you do today
gary
so
question
do you secure and protect or manage your
ip
how many do
expect you there was one there one out
there
few round few places
so the rest of you you you basically
have your ips stored in a customer's
database
is that the best place to have your ip
stored
or do you have a few databases around
the company to float around
probably not the best place to have a
store
the ip that you're especially when you
get into cloud solutions the ip is one
of the biggest biggest assets of your
company
and
you have to treat it as a big asset
not that it has to be locked down
but it has to be secure the knowledge of
how you grew your product and how you
got to where you are today is
huge huge value to your company
so
it's not putting it behind bars
but
mr potato head can can live with being
behind bars a little bit at least we
know where we have it we know where we
have the truth the truth is what we have
in our source code
system
and it protects our data
so
manage all your code
i guess
you just answered that before if you
don't manage your code
you don't know how you got to where you
are today you only see
the current version you never see
how you got there and you you you have
no way of learning from what
how you got to where you are today
source code management
is is huge
for training your internal developers p
i i always call it source code
management
and i don't like when microsoft
sometimes they use the source code
control i think control is such a
negative word
it's source code management you're
managing your source code you're helping
your developers by doing code reviews by
letting them do code reviews with each
other
you help them become better developers
every day
when you can only see the latest version
of the product you're working on when
you can only see
what the state you are in today and you
have no clue how you got there you have
no clue what the latest change was
you you don't have really a chance to
to to learn from it
so
right we're not pushing here yeah
so that's important the other thing
that's important that is don't create
too many systems
your you have things like nav is just
one side of this
but you have
a powershell
it should be always source control
managed
i saw my source code managed
you have javascript we have mr
powershell mr javascript sitting over
there in the corner not paying attention
but
they should they should pay they should
they should manage the the the source
codes that they do
because it's part of the ip of the
company
the other thing
is
we talked about this one
constant developer improvement
code review i mentioned that already
and then there's how you're testing your
deliverables
are you
having
the manual developer
sitting there
in somewhere in the in the corner or
tester do you have a dedicated tester
that sits in the corner tests all day
tests all day never does the same test
twice because
since you can't remember or that
something has gone wrong
you have to document your
your testing you have to put it into the
system right so we get the test done
again and again if something has gone
wrong once it's going to break again
later
might as well test for it
so i love my little dog there
so manual testing the other thing that
is manual testing you have no way of
having resources enough to do testing
standard testing today is 15 000 tests
it takes about four hours so it's a
little time consuming
but how long would it take to manually
test 15 000 things and how many of those
tests would be done wrong because you
missed something or you didn't think of
something the only way to test that
amount of of do that amount of tests on
your software is to automate
and source code management again it is
the foundation for all of this
source code management if you don't
manage your code
you don't improve it
you cannot automate it
and you don't learn from it
i think that's last night wait we have
one more i have one more yeah so
it's yours
so um
we have
over the years i've i've
first of all think this is an important
message you should all go home with this
message if that one one slide you should
take a picture of that's that one
of our slides at least
so
over the years i've i've had different
books recommended to me to to read about
doing
cleaner code doing
things like agile
there's no way
microsoft wants us to be agile that
wants us to be faster they want us to be
bringing things better to the market
and there's no way they can do it we
have to do it
it doesn't help microsoft becomes agile
if we are not
because we we we will never be able to
deliver
on what
the vision is for what nav should be
doing
so two books i would recommend if any of
you
have time to do reading is these two
clean code is a great read
that i really have enjoyed a lot
it it gives a lot it's it's c sharp uh a
lot but don't worry about that it's the
the the
philosophy that's presented in it is is
is very very powerful
and it's and it's the same message that
you will you'll see a gary and
cloud ready software over there that
they present
on a regular basis
so that's for developers if you are
a product manager
then you should probably be trying to
look at
creating agile in your create an agile
environment for your developers
and the principle of development
product development flow
is is an absolutely i'm only halfway
through it right now and i'm just uh
it's it's insane how well it represents
um
the things we've been doing wrong for
years and the things i've been doing
wrong for years so it's a great book
it's a great read and i
can recommend it very much
enough about books by the way i don't
get any royalties so i'm just seven
five
and any questions i was three seconds
too early
you timed it very well thank you very
much questions
fire away
there's a question there you get the
cheese shield already but if it's crap
you have to give it back
oh
okay is it working
working okay
i have a question regarding
okay build
how effectively
build management can be used to
manage the
customer
let's say customer delivery
management when you have at a regular
basis
to create the forp files uh with
description of changes and send them to
customer because we for us for instance
we have some customers which have quite
sophisticated their own i.t stuff and
they
are
putting all the
let's let's say they are working with
the production database by their own
they are not letting us to connect its
yeah
if i can answer sure
i think if you have develop a customer
which is really uh maybe developing own
customizations or maybe just managing
his
update of databases or have first the
test database and live database i think
very good tool for it is the git
because it's distributed it means they
can have the repository on their site
you can push the your changes there and
they can update their database from it
through the powershower when they want
and if they are creating own
modifications they are just
could commit them push it into the
repository into separate branch or
something and you can
take this branch and merge it into your
development environment and this kind of
things
git is allowing it means it's just about
setting up how to work with that
how you will use the branches the
repositories and how how we will manage
our all this around yeah and i think
also one one point to take here that is
that you should never ever be developing
in a customer's database you develop
locally on a
with code isolation internally in your
company
and you deliver
finished bills
to the customer period that's your
policy but they apparently have a bit of
difference
isn't it yeah but that's his question
about it we understand perfectly what
we're saying but he wants to be tweaked
a bit differently i guess i guess so
yeah
which one
you have to run with the t-shirt i have
a question about saving the text files
do you think it's better to save the
original text file or just save the
delta files so only my changes
so it's better to save the text files or
yeah or only the delta of the my changes
i did yeah yeah so
yeah so we always save the entire text
file and we use powershell to do the
export of course in the current version
of nav
you have to be careful because there's a
country there's different
sides of
what you call as different size
because yeah regional settings you can
export in with different date formats
and different time formats that get that
really messes up the the system
however all of you might have seen the
initial presentation uh or the keynote
by microsoft did you all pay attention
to the end of it
did you see the text format they were
presenting
it looked different
it was not completely the same we're
used to
so maybe there's something going on
there i'm not completely sure but i'm
just guessing here but from a source
code
perspective you're you'll always have to
save your full file it will create delta
inside otherwise you don't have any
relation between the two i mean
absolutely a delta file from cumulative
update one is totally different probably
than from cognitive update two so you
don't build up
a comparison whatever so inside your
source code control system code
management system
it's always a file and it internally it
creates a delta and i i will add to that
from git point of view
git is internally saving only the deltas
his internal deltas of the files
and if you want nav deltas
you can generate them
as you wish because you have all the
history and you can just
make the delta from any point to any any
other point you don't need to save the
deltas
you can generate them
so i really like what you've shown and i
see the positive effect we can have with
source code management but we're a
customer we are working 10 years with
when we how to handle all the changes we
already made
to to start with a source code manager
yeah
was it a question yeah
it was question how to handle uh if you
already have uh some history and you
want to start with with
the version control
if i understand it correctly
very good point will be if you have
where you started at least
if you have the basic version on you on
which you started to build
your current system
you can make first
first history for first commit the
this base version of nav and second will
be your current state and then you can
continue
step by step and if you have a system
already you might automate it to get the
previous
versions out and then one by one comment
because if you have that you can create
the delta and apply it to new version
and you can upgrade
through this system
good we have a question over here
luke
thank you very much for the idea in
using tfs online
you said the
code ip is
something very valuable very precious
and what about putting the code in the
cloud uh how safe is that do you think
maybe we could also have some legal
compliance stuff about that
fully depends probably also on your
country
maybe there are different legal matters
set there on the other hand yeah i
from that bigger perspective i didn't
have to make that choice but let's say
generally it's like putting things into
the cloud has this is the same issue and
if if from a country's perspective i
don't know germany
for the netherlands i'm i don't know
about but i'm not fully in the know but
i know that between some countries in
europe and germany for sure they're more
reluctant as a country to do that so
inform yourself what legal matters are
and especially with the customer it
could also be a matter of the branch
like banks have totally different
requirements at that level than let's
say
chemical operation or whatever yeah
was there a t-shirt there's a t-shirt
over here there's a question another one
hey hey it was the girl that was asking
the question you have to
yeah
i had a question for you
yep
you mentioned in the beginning that
when you rename a function
that is not seen as a change when
exporting did you find a solution for
that
only only uh
solution
which i have now is just that the
developer needs to push different button
to to really export all
in this case
because the git will take what really
was changed and will then show me only
the the difference in the all other
objects which are
somehow connected to this
it means maybe it will take longer time
to export all all the objects to the
text file but i will be sure that
everything is
committed
i see all the changes
i actually do that in
my place
we always do everything i don't want two
buttons because people don't they forget
they did something so i just push
everything every time it takes 30
seconds longer
it's not really a big big deal
everything and exporting one file
no it's exports into multiple files
because when you push it in to
source code management you you export it
as uh import push it as motor multiple
files so you can see 30 seconds between
uh
all objects and one object yeah it's
nothing
when you do it with powershell i need
your computer um
yeah that
for example my button is really
exporting everything to one file then
splitting it to the repository yeah i
don't know if you are really by one by
one exporting or even
exporting all to one and split it there
yeah
it's much quicker of course yeah i don't
remember what i'm what i'm doing
but i'm doing one of the two i'm still
doing it manually
there is nice question or
yeah
last question
last one here sorry offline
i wanted to know if microsoft has any
plans towards team foundation
integration or git
and how we should name our objects uh
so that in future versions we don't lose
all our history because we need to
have a different file structure or
rename those files
we don't either
for the naming file if you use the
merge utilities by default it will use
the first three letters of your object
and then the id of the file of course
you're free to choose now
but that's the default set that's the
internal
that's also the the thing i'm using
because i was used to that there are
different ones but typically this is
what microsoft uses
yeah so use the standard naming of the
powershell tools that
would be my recommendation absolutely
and also
what the future brings and what uh
right now where we have the separation
between the database and the workspace
and we always have to synchronize the
two
is annoying um
i don't know maybe i read too much into
the uh the keynote the this did you see
the keynote
yeah at the end where they where they
kind of showed uh the the
the build engine or the
compiler
it seemed like it was
it was a different text format that i'm
pretty sure about
but
they said it seemed like they were
editing straight in the text
so maybe that's the way they're going i
don't know i can say that right now
because they have not told me
but
uh
fingers crossed fingers crossed we have
asked for it for a few you look and i
have asked and talked to them for a few
years about that
and
it's one of the things we really wanted
to see we also wanted to see one fixed
text format
so the text format doesn't er depend on
if it's exported with check
code page or check the date settings or
me in north america
so we don't have to set up our computers
with the same regional settings in order
to avoid conflicts down the road
time is up
already unfortunately thank you very
much thank you very much thank you
