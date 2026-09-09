# BC TechDays 2022 - Git under the hood

- **Source:** https://www.youtube.com/watch?v=DK9TUTSK-3A
- **Video ID:** DK9TUTSK-3A
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 110m08s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

ladies and gentlemen welcome to room
nine for the next session get under the
hood and please have a welcome to wacko
babish
okay
thank you and welcome again to techtase
2022. it's amazing to be here again I've
really missed this and
I'm really glad that I can uh be here
today with you and present this topic to
you
uh the topic is called get under the
hood and I will say a word or two about
why this topic and then just for
introduction my name is viejo babich or
Vehicles whichever you prefer both are
equally probably complicated I've been a
member of this community for a long time
I've been delivering sessions here and
you who know me from earlier know that
I'm I've usually presented stuff on The
Cutting Edge of of things
so I I guess I got demoted this year uh
let's take a look at why git it's it's
very interesting like why am I here
talking about a 17 year old concept and
this this really does feel good uh bad a
more strange
um I did an experiment couple of years
ago with directions I I proposed the git
session just because you know they asked
for more content and I just said okay I
can do this without too much preparation
and I didn't expect it to actually cut
into the content and it did and after
that session I got quite some comments
from Partners asking for more saying
like can you do this for us can you
repeat this can you whatever and then I
started doing webinars maybe some is
there anybody here who has been to my
git webinars just clap your hands or
yeah a few of you yeah so I've been
doing this for for like intensively for
a year and some now and what I've
realized is that even though this is
2022 and the the product is 17 years old
now already
um it is still relevant because we are
all using it and we probably are not the
best kind of users of that tool so when
trying to explain
with pictures and you might know that I
like showing pictures
um let me say that in our pockets All of
Us carry a device that looks like this
and this device has more computing power
than NASA had at its disposal when they
put the man on the moon every one of us
on this device we have at our fingertips
access to far more information than Bill
Clinton had through all of his
intelligence agencies at the height of
his presidency
and yet statistically speaking what are
most people using this well watching
videos of cats
and when it comes to git we are not too
far from that like git is a powerful
tool it is an amazing tool it can do so
much for us and one of the goals of my
session is to demystify git to uh to
bring it closer to you to make it a Part
of Your Arsenal to make you a better
developer because I don't see git just
as some dummy content tracker sitting
out there and keeping track of the code
that I write I actually see it as a
development tool and it helps me in my
everyday work and I hope after this
session you will see it in the same in
the same way
so that much a little bit about why git
and then let's start talking about what
is git I think that always the best way
to describe a product is if you ask the
product to describe itself so git says
this git is a stupid content tracker
and if it sounds silly to you this is
actually the first thing that you will
officially read about git if you go to
gitscm.com which is official git website
there is further down like a definition
that kind of tells a little bit more
what git really is and let me read it
git is a scalable fast distributed
revision control system with an
unusually Rich command set that provides
both high level options and full access
to internals wow a mouthful and
um there is something that I would like
to highlight in this slide that is that
git is actually a command line tool and
I would like to break a conception that
many developers have that get some
service running on your machines
watching over your files and your
folders it is not
it only reacts when you invoke it when
you call a command then it does
something for you but it doesn't keep an
eye on your code or anything it does not
care only when you care enough to ask it
will care enough to answer so how do we
ask git to do something for us
well uh again if you ask git
documentation about uh what kind of
commands are there in git there are two
kinds of commands there are these nice
shiny commands that git calls porcelain
commands like things that you might even
know like git clone git push git merge
stuff like that and then underneath we
have other kinds of commands that git
calls Plumbing commands stuff that you
probably never did like uh you know git
reflog get cat file git hash object Etc
so these are those you know dirtier
commands which are
running completely deep under the hood
intended for the tools to call them but
you know both of these kinds of commands
serve the same purpose ultimately which
is to you know take you get a picture
it's just that these here are you could
say user friendly and these other ones
are more for professionals
so uh
now that you've seen that we have these
two kinds of commands let's try to see
what is the most common thing like of
all operations that git does
invoked from any of these kinds of
commands what is the most common thing
that git does
so uh to be able to answer that question
we really need to go deep deep down
under the surface we need to to dive as
deep to the bottom as possible and see
how git actually works was that Waldo
okay that guy so at the bottom of things
when you when you go all the way down it
is actually a dictionary and when when I
say dictionary I think that all of you
should be familiar with what a
dictionary is like we have these kinds
of things in Al like a dictionary of
text Boolean or dictionary of date
integer or or dictionary of good decimal
so every dictionary is a key value pair
collection
where key is unique obviously and there
then there is some value which kind of
depends on that key so talking about git
and knowing that git is in its heart a
dictionary
what is he and what is value forget so
let me start from value let's take a
look inside of this dictionary value is
any sequence of bytes and this is really
important because there is one other
misconception about git that it's
actually not good in handling binary git
handles everything as binary forget
everything is binary your text is binary
it's us
that have problems with binary when when
we do strange things but that's
something that we can talk about later
in in any case forget everything is
binary every value is a sequence of
bytes that's how it gets these
um values in that dictionary so if this
is the value then what is the key
the key is sha-1 so uh what git does is
every single time there is something for
it to store in that dictionary it will
actually first calculate sha1 so how
does git do that let me start by showing
you first demo there is this command
called git hash object one of those you
know
professional commands that run deeply
under the hood you probably will never
need to call this command yourself at
all but trust me it runs it all the time
so
let's take a look at
this
screen here
I'm just going to hack a little bit into
git and I'm using git bash for this and
I'm just going to type Echo and then
where's Waldo
and then I'm going to pipe this thing
into git
hash object
and I'm going to use standard input
because hash object otherwise works with
files so I'm just redirecting my input
to this and then I get a sha one or a
hash so this string is converted into
this hash and when git stores this
string if it needs to store that string
in inside of its dictionary it will be
first
converted into or actually hash will be
calculated and then git will handle it
and if I for example go here and I say
like um
something like right here
and then run this it's a different hash
different sha one and then if I repeat
the first one
I'm obviously going to get the exact
same one that I got the first time
because for Shawan algorithm the same
input obviously always gives the same
output
and now something important here is you
can see that here I have Powershell open
as well and I earlier said that git
actually operates on binary level not on
text level let me do exact same thing in
Powershell to see who is better
Powershell or Bosch
Echo where's Waldo
and then I'm piping that to get hash
sorry
git hash object at standard input
and when I run that I will get a
different shot so why is that
uh and you know if if you try it on your
machines you might get the same but if
you run Linux or Mac OS you might get a
yet another shot so how can it be that
the same input
provides the same output when it
obviously doesn't well it's about binary
because bash works on utf-8 level which
is uh not injecting anything whereas
Powershell works on unicode
utf-16 little Indian and then inject
something at the end which Bosch doesn't
and that's why you will get a different
input a sorry different output because
it seems to be the same input for you
but on binary level it is not
however let's take a look at this file
the file contains exact same content so
if I do with do it with file because
file is on binary level exactly the same
for bash and for Powershell so I will
just go from Powershell I will say git
hash object
and then I will pass this Where is Waldo
and I will get this familiar sha which
starts with five two and what's that
whatever
and then I will do the same from Bosch I
will just do git
get hash object and then where is Waldo
and I should get the same because on
binary level this is the same file so
the point here is is that uh
with this algorithm with this approach
git is always able to identify equal
content equally on absolutely every
machine out there so if every of us in
here in this room had this file on their
machine and they would process that
through git we would all get exact same
Shah and this is very important so um
I've said that git is a dictionary but
it's git is not just any kind of
dictionary git is a persisted dictionary
so it actually has this Dash W which
stands for dash dash right which allows
you to actually write or commit or not
really commit but I'm apologizing don't
blame me I'm full of good terminology
and I cannot yeah so git hash object
Dash W will persist whatever input is in
this uh in this dictionary so let me try
to do that I will just run the same
command and add Dash W and it fails why
it fails well I can run some git
commands like this one without being
actually under git Source control but if
I want to store something in gits
persist the dictionary I actually have
to be inside that dictionary so I need
to initialize this repository so I'll do
it do this I will just say git init
and this is now initialized my
repository and an invisible folder has
appeared in my uh in my uh demo one
folder in this case and let me actually
make it less invisible I will just do
user settings and then files
um
ignore
no it's not ignore yeah exclude yeah
apologize
fast excluded I will just delete this
git
and when I do git appears here and then
if we take a look inside this git we can
see a lot of things and I do not
recommend that you really modify
anything manually but we will spend a
lot of time in this folder just to
understand what is going on under the
hood so when I have written this object
there is this objects folder
I I haven't written anything yet
actually I've just attempted to write
but when I try to write again now that
git init has been executed and I'm
inside of a git folder when I run this
now this has been written and if I
refresh this I can see that there is
something in there
and let's not yet talk about what that
something is and why it is like that
let's first try to see and understand
how this git hash object works first of
all
it takes the content so in our case this
is where's Waldo followed by this
line Terminator
uh and then
when when we execute git hash object
what git does is it takes that content
and then attaches a short header to that
content in this case it says blob
because it's going to store a blob and
then it says what is the length of the
content being stored
and then it attaches a
this ASCII zero character or Unicode
zero character as a delimiter and after
that it attaches the rest
and then it calculates the hash not from
the original content but from this
and then when it has hash it wants to be
efficient so it actually compresses the
content everything like the header and
all
so when it's done what it does then is
it splits it splits the hash into
takes the first two characters creates a
folder if it doesn't exist and then the
remainder of sha is the file name and
then it stores
the content compressed content into
that file
so um
let's take a look at
this a little bit so now we can see that
we really have this file here 52 and
then the rest exactly as we expected now
we know why this happens and and what
will happen if I for example change this
and I say Where's Waldo right here
in the front row
and then I go and
so now that I have this file where's
waldo.txt and when I run this I would
expect that of course this would be
overwritten I would just I don't need
this anymore because files this and
so gitude overwrite but it does not it
actually creates another one
okay let me try again let me let me say
like okay
sleeping
and then I run it again and of course I
will get another one so here I have a
yet another
blob object in my uh in my git
repository so uh why is that that is
because sha is yeah Shaw is
an identifier it is the identity of the
content so when git calculates sha it
knows that there is no possibility I
mean there is theoretical far remote
possibility that yeah some
under some very unlucky circumstances
there would be the equal shot it has
never happened and probably never will
uh we can discuss that in Q a uh so when
git calculates shot it knows that in the
entire universe every other object will
have a different sha so it can really
relate this Shah belongs to this content
and vice versa they are
they're just connected they are they you
you cannot detach one from the other so
when you save a new object or store a
new object in this git persisted
dictionary it will always create a new
entry in there because it's always going
to be new sha for new content and all
shots remain for the old content so all
objects in this dictionary are immutable
this bond between sha and content is
unbreakable it is always it's forever
and there is a name for this thing this
thing is actually called content
addressable storage and it is not the
only thing out there that employs this
principle and it is just a lucky
coincidence that when git was being
invented uh this content addressable
storage was quite a hit because of the
financial industry that had exact same
requirements and then Lino storwalls who
was designing it actually chose that as
an amazing principle and the
consequences of this choice to design
the system like this that everything is
identified by a sha and then you have
this unbreakable bond between the Shah
that actually tells you the content are
so far reaching that you just cannot
imagine how much optimization can happen
because of that for example I save
another file elsewhere in the system but
if it's the same content guess what git
doesn't need to store it again because
it already has it it's the same shot so
no need to store it again you push
objects to remote remote knows the shot
okay no need to push that object because
it's already there and others as we will
see as we go so this is a little bit
about this git persisted dictionary
let's go on
let's talk about this not so stupid
content tracker
um one of major misconceptions with Git
is also that it monitors your code as I
said earlier like people
often think that yeah I'm working in
Visual Studio code the moment I change
something git tells me okay look at this
this file is new or this file was
deleted or whatever and then you think
that git is monitoring your code but git
isn't it's Visual Studio code that
monitors so visual studio code has a
file system Watcher running over your
entire repository and then when
something changes it actually runs some
git commands underneath and then parses
the output of those commands to present
them to you in a friendly way but this
is not git doing these things it's it's
the tools that do those things so git
does not really monitor your code let's
take a look at really what is happening
inside git there are three areas where
git happens
this is the first area this topmost
level where you have files that you see
and we call this working tree or working
directory of I mean both are equally
equally good
so this is just files where you can make
any kinds of changes that you want and
git doesn't really care that much
because it doesn't monitor anything in
there
what git cares about is this invisible
folder which we actually call a local
repository that's where things happen
forget
and inside that local repository there
is another thing it's actually just one
single file which is called index and we
know it from Visual Studio code AS
staging area and this is what it
actually is in git also calls it that
way when you read documentation not
Plumbing documentation but you know
those porcelain documentation
um then you can see that this is really
called staging area so what is the what
is the correlation between these three
what is happening when things change
well as I said you can do things in the
working tree you can change content in
there but git does not care only when
you ask git
questions like git status for example
then it git will go and try to see what
do I have in the working tree what do I
have in my local repository and then it
will update the index and then it will
present the contents of the index to you
actually not to you but to vs code which
will then translate that to those
staging area or working three file
changes that that you see we will see
just a little bit about that but not too
much
so
as I said git doesn't do anything
automatically it is never triggered it
is always only invoked so what really
happens during staging I will just open
a demo at this stage
so let's start with
this one
I have I have this same working
directory which I I've presented just a
moment ago so there are three we call
them dirty files because they haven't
been committed and because git status is
run in the background we we can see this
so we can see that
we have three dirty changes in here
and then uh since I want to know what's
happening inside the git folder I can
see that there is not even this index
file that I've mentioned or No Object
files this is just a freshly initialized
repository so everything is dirty so let
me actually just
um store these let me put them into
staging area so let me stage these files
what happens when I stage these files so
there are three files as you can see
and
um I can see that now I have this index
file it's a binary file you can I mean
you can read it I don't recommend that
you hack through that uh there are ways
how you can inspect its content that are
less intrusive but then let's take a
look at this objects folder we have two
objects in there so why two what do you
think
well don't don't try to answer uh it's
going to be difficult to moderate the
discussion yet so we have three files
and and two blobs well that's easy again
I have this readme file and I have this
games file which has content where as
well though and then I have rules for
this game whereas while though where I
have written nothing else but just the
title of the game so far and these two
files are exactly the same content so
git doesn't need to Hash them twice or
store them twice it is it knows that
this is the same blob
so it is efficient
good so essentially this is what we get
we get exact these two blobs I'm just
using first four letters of sha because
that's minimum that you can use with Git
whenever referring to shots you need to
use I mean you can use the whole sha
which is going to be 40 hexadecimal
characters but you can only use the
first four
so we get these two
so what will happen I mean here I have
shown commands that have been executed
there is no git stage command it doesn't
exist this is the command that has been
executed to actually get these files
into the staging area
uh so we actually had to tell git that
we intend to store these files when we
next commit
and then let's take a look at what
happens when we really commit this into
the repository so I will just take this
and I will create a commit I will just
type A commit message first commit an
amazing one and I will commit that and
let's take a look now I have five
objects wow what do you know
so uh one of these five objects at least
should be familiar this is this one
commit and most people have only known
Shahs from commit because they think
yeah git attaches this shot to commit
but that's all actually get touches shot
to a lot more things than commits it
attaches shot to absolutely everything
so let's take a look at what these five
things really are
so
when we take a look at our local or
working tree git first translates that
to number of subtrees in this case two
sub trees one for the root and then one
for this rules folder and then it also
creates this commit object and then we
can see that this commit has its own sha
every single tree has its own Shah and
every blob has its own sharp and let me
plumb a little bit more through this
repository now that I have these objects
what I will do is I will just ask it a
little bit about these objects I will
just do git cat file and then I will
start with this familiar one this is
this
um five to
six four we know it's where's Waldo so
yeah I need to tell what I'm interested
in so I will say just tell me the
content pretty print so it will just
print this is the contents of this blob
and how do I know it's a blob simply by
asking for the type so type is blob
good let's take a look at other ones I
know already from the slides that this
A8 is another blob so these these other
ones like F9 B4 F7 they are they are
something else so let me actually start
with this uh B4 so what is this let me
just
actually not before I was go with this
9f
so 9f and then whatever the rest is 3 8
and
9f yeah
okay
there we go it's a commit so good I know
that this is a commit object and then
let me pretty print this commit object
to see what's inside and now I see that
inside I have a tree object and I have
some properties like who is the author
who is the committer and when was this
authored and committed and I also see
the commit message good so I see that I
have this three three called B4
something so let me just cat file that
so just say
uh cat file b496
and then pretty print sorry type first
this is a tree object and then when I
pretty print I can see that it contains
two blobs and another tree which I could
again uh cat file to see but it's a tree
with another pointer inside so what we
see like this you get c's with different
eyes to get this thing actually looks
like this
it's a hierarchy of objects where at the
highest level we have a commit
which has its own sharp and this commit
points to a single tree which is the
root of that commit and that tree has a
number of pointers to other objects in
there where for example in this case we
have 0.2 pointers to blobs and one
pointer to a tree and that tree points
to exact same blob
through another
um another pointer name which is this
where's waldo.txt so this is the
contents of the Commit This is what
happens inside and as I said git hates
duplication git actually wants to be as
efficient as possible so what git will
do is git will always do this thing when
it if it says that there are two files
with different names but exact same
content it will just use the same blob
and just point to it from two different
trees you could have a million copies of
let's say app Json all the same in
million folders it will only store one
three one three and and one blob if it's
all the same just copies of the same so
git is really efficient when it comes to
that
so uh as you can see it is not that
stupid after all
uh so we have seen that the the index is
a blueprint for the next commit it
defines what is it that we are going to
commit operation creates a commit object
which always points to a single tree
which is the root of that commit
trees are catalogs of pointers to other
blobs or trees and git hates duplication
good
now that we are
going a little bit up we've seen at the
deepest level what git is in a little
bit higher level let's go to this
probably highest level that we see as
users that git is a revision control
system
so what does it mean to be a revision
control system that means that you need
to have at least these four capabilities
you need to be able to manage changes of
data over time
you need to be able to identify
differences between different revisions
that's why it's revision control system
you need to be able to isolate changes
that are happening
and you need to be able to integrate the
changes that have happened
and git satisfies all these it just has
its own terminology of that so git
manages history of commits
uh it also is able to identify
differences between these commits it
allows isolation through branches and it
also allows integration of these
branches so let's take a look at how
this happens let me again go deep down
into git
to see what is going on so let's imagine
I have this other commit so I will go in
here and I will just
add another game I will just say
Monopoly I'm ready to define the rules
for that game
it doesn't really matter Capital
lowercase whatever I will just now stage
this
and commit this as a second
commit
and yeah let's go into git folder to see
what happened let's just take a look at
at this level so first thing that we
have is the new commit object obviously
and this commit object obviously also
points to a pair uh sorry to uh to a
tree because it it has
it has its own root of its own content
that it stores but it also points to a
parent so it is unbreakably connected to
this parent again uh Shah for for
example for blob sha is calculated from
the contents of The Blob for trees Shah
is calculated from the list of those
pointers inside the tree
and for commit Shah is calculated from
everything from uh not just
like from from from blobs and from uh
from trees essentially what you what you
get when you pray the printer commit
that's what defines a commit so Shah is
calculated from that and now
um You might ask a question like why are
these two different because it's the
same root like I have exact same files I
didn't change so why did The Shot Change
well it's easy because in this case I
have these two which are exactly the
same so I didn't change uh one file and
I didn't change this three that points
to uh to rules but I did change
games.txt I've added something so there
is a new sha for this new blob and I
need a new pointer and since there is a
new pointer I also need to change the
shaft of this tree so this is uh this is
how this works
um good then let me address some more
common misconceptions about git
a lot of people because they see how it
behaves from Visual Studio code or from
devops or from GitHub or wherever and it
seems that git stores deltas
and it you think that git tracks changes
because that's what you see in Visual
Studio code but this is actually wrong
git does not do that uh git actually uh
candle snapshots
uh it it stores snapshots it tracks
content not changes
and then you could say uh well it's
potato potato like what difference does
it have well it has a lot of difference
so
um let's take a look at this picture
I have quite a little bit of mess I have
two commits but the first commit is this
and this is the snapshot
at the moment of committing and then I
have the second commit which is the
snapshot
of my working tree at that moment and if
I add another commit
with some more files and changing files
around maybe I reused some existing
files maybe add some more new files but
this is going to be a snapshot at that
moment of my working tree at that time
and this is what git stores essentially
every commit is a snapshot it tells you
exactly what your working tree looked at
that exact point in time
that's what git stores so you could say
well that's not true I've seen this like
I've I've seen this everywhere in
git lens uh in git graph in devops in
GitHub wherever you go you always see
this yes that is true but that's not
because git does that
git does not track changes it's us who
track changes you know humans are really
really bad at handling snapshots just
watch this on YouTube in a week or two
and you will see that you are uncapable
of handling 60 snapshots per second that
are happening in front of your eyes but
what you do perceive is a change
and we are good at handling change so
git tools present that change to us not
because git stores it but because we
want it that way so it's always good
tools that translates
these snapshots into changes so that we
can easier understand and follow them so
all of git tools
do that
there are very few tools I've seen that
actually present you the contents as
they are that would be unmanageable it
would be very difficult for you to see
what exactly happened so how does git do
that well it calls this again a method
or or a command called git diff git diff
works out the differences between two
snapshots and it also takes a massive
advantage of sha-1 again another
optimization and whenever you want to
know what changed git really needs to
calculate it again every single time you
ask for it you get new calculation and
most most often it's the same results
but you can tweak this command at least
when you when you're running it from the
command prompt so let's take a look at
how git diff actually works let's take a
look at this simple snapshot of of a
repository we have first commit and
second commit for you it's very
difficult to spot the differences by
just looking at that they look quite the
same
uh it's you know just like those two
spot differences you know children
pictures
um so what does git do first it goes to
the root and then it checks the Shah to
see if the Shah chained changed if the
root shot didn't change then it doesn't
have to check anything else because then
everything else inside is exactly the
same here it says that okay this is
different so it will Mark that for
further deeper inspection let's go to
the next three next three has exactly
the same shot and then git simply
decides okay I don't need to look into
it it can contain 70 million files
get simply by checking the Shah knows
that yes that's the same content in
there so I don't need to inspect file by
file so it skips it goes to the next one
so yeah sha is different also name is
different so I really need to look into
this very deep good so now it knows that
it has out of three trees it has two
trees to check so it goes back to the
first tree and then Compares this and it
says okay object ID config same sha
nothing changed I can just go on and
then it says app.json differential so
this is a modified file now if if we
want to see the contents of the
modification we can do that as well git
diff can tell that as well but let's say
we are doing it on a higher level just
on a tree level so we know this is a
modified file inside of this second
commit then git stops processing this
tree because it has done it and then it
moves to the next three it has here we
have the same shop but different name
so what happened well
a rename operation you just change the
name of a file or move the file in this
case to a different folder but you
didn't change the contents the contents
remain the same so git knows that this
was a rename operation
and then we take a look at the next one
okay this is different shot it doesn't
have anything like that so it says okay
this is a new file new sha new name this
is a different file
so it records this as an addition and
here it sees different sha something
that doesn't even exist on the right
side
and the name that doesn't exist so it
knows yeah this is probably a deleted
file and this probably is the keyword it
never knows for a fact what what git
diff does is a very educated guesswork
in most situations it is pretty smart it
can detect everything that happened
exactly as we want it to be recorded but
sometimes it will give you wrong answers
that's just because you can do things
like for example you can take the same
file you can rename it
and change the content at the same time
and git might not be able to tell you
that this was actually
a rename plus change content it will
just tell you where you deleted that
file created this new file and then you
lose track of that so git is not all
powerful because it doesn't care about
changes it simply cares about snapshots
and it will do its best effort to
present those snapshots as a set of
differences to you so in this example
here we now have a change set as some
people would call it which contains
three or actually Four changes one
modification one rename one addition and
one deletion but that's not what it sees
that's what just it presents to us
because we are better with that
good now let's talk about branches a
little bit
branches are used to isolate work
between developers so when I work
and when you work we usually do not want
to trample over each other feet so we
simply typically start a new Branch so
we let's not talk about branching models
and best practices no let's just talk
technically about branches
so a branch simply isolates your work
from your colleagues works
and in git branches are also pretty
smart pretty efficient so what is a
branch let's take a look I will just
open another demo
and let's take a look at the contents of
the git folder we know that git stores
stuff in here and some of that stuff
like index that's binary and we also
know that these objects are some zipped
objects you could really unzip them to
see what is in there and then see that
they are exactly what I described uh but
where does it keep branches is it also
objects like you could assume especially
if you come from TFS that when you
create a new Branch it actually
duplicates everything somewhere else so
that you can work on an isolated set of
changes that's not what git does so a
branch in branches and gits are stored
here in refs GIF also refers to branches
as references or heads as well we will
see a little bit more about that so refs
and then inside refs we have heads and
then we have this master head so when I
click this master it tells me this so
what is this a Sha good well what does
this sha point to well I can figure that
out because I know how to so I go to my
terminal I say get cat file
and then I say pretty print or actually
give me a type of that and then I type
the sha006cc or just C and then it tells
me this is a commit
so I see that I have a file which is
named as my branch which contains
simply the idea of a commit
and that's the branch that's all there
is to branches in it
if I for example do this like I create a
new Branch so let me do that I will just
go in here and I will type
git Branch feature zero one
and what happened I just have another
file here
with exactly the same contents as Master
because they are currently pointing to
the same commit if I click it graph I
can see that
through both of these branches are here
good
so what happens when you commit well
get simply advances
it changes the contents so let's take a
look I'm now inside I'm going to check
out into git checkout feature
zero one I'm intentionally using command
so that you can see that this is what is
happening when you click around Visual
Studio code
I'm not saying that you should do that
absolutely no no benefit of that I just
want to tell you that this is what's
going on this is under the hood session
so that's why
um so I'm now in the feature branch and
let me do a modification I will just go
in here and change this to version
0.1 and I'm going to Stage this and then
update version
and commit that so let's take a look at
feature Branch so I commit this and this
file changes it now points to the Sha of
this commit
and that's the branch so if I keep
adding commits like this git will simply
update this file that's all there is to
branches and then let's imagine that
Master has advanced like somebody has
merged their work into that and then you
are ready to merge your work into that
what happens you create a merge commit
and then you delete this Branch so
you've simply deleted that file git
doesn't need that file anymore we will
talk a little bit more about deleting
branches so in git branch is nothing
more but a name for a commit nothing
more than that it's just it's small file
with the only contents of that file
being Sha of the commit that that Branch
currently points to
so that's a branch
so how does git know which branch is
current well apart from having these uh
branches in here
inside of heads it also has this file
called head and let's take a look head
says
refs heads feature zero one
so it's another pointer so let me check
out to master so git
check out master
this is what happens so I've changed
branch
while it is somewhat safe to you know I
could go in here create a new file
called whatever and then put the Sha in
there it would work and I could delete
it it will also work this is not
recommended don't just a few more things
happen when you check out into Branch
not just like change of this in here but
yeah let's not go into that you should
generally not be hacking in this folder
even if you know what is going on it's
not recommended so um but that's that's
all there is to current Branch so when
you add a commit
then
like for example now we are in the
feature branch and we check out the
feature branch
the the only thing that changes is
contents of this head
file apart from yeah git synchronizes
the index get synchronizes the working
tree as well that's why I'm saying like
do not touch that file manually so uh
but just contents of this file have
changed and now it points to something
else and then you add a commit
so you commit something what does git do
first thing that it does it looks into
head and then it sees okay head points
to feature one and then it simply
advances feature one
to point to that new commit and that's
all that happens so that's how git knows
what which branch is current
so let's talk a little bit about the
concept of detached head maybe you've
heard of that can I see did somebody
hear of detached head have you ever seen
this
ugly looking message you are now in
detached head mode blah blah something
scary yeah uh so it's not scary at all I
mean it's git could completely work in
this detached head mode so what is
detached head as you could imagine it is
simply when this head points to
something other than another reference
or another head or another Branch file
when it simply points directly to a
commit so yeah I can do that so I will
just go to this detached head demo and
let's take a look at the history that I
have
so
in here I have three commits so I will
just
select this one okay it's eight zero
something eight zero nine D whatever so
let's open this head file and let me
just through the terminal say git
checkout and then I will just move this
file around and I'm interested in this
number in the in the shot so I'm
checking out to 80e9 and then I get this
um check out yeah typo check out and
then what happens is that head file
changes it points directly to a sha I
get this message here that says you are
in the detached head mode bla blast
whatever and then I'm working in this
mode so this mode is not scary this is
nothing to be afraid of this is a
typical thing it's typically something
that you could do for debugging like for
example you know that something used to
work over the past 17 commits you did
but you're not sure exactly where you
can just attach heading to each of them
and figure out okay this is where I
broke it there is even a git tool for
that git by SEC that can do it
automatically like it just keeps
checking out until it figures out okay
this is the branch or sorry this is the
commit that broke whatever you broke you
need some unit test for that but yeah it
can it can do that for you so
that's the touch head that's that's the
mode and that's what it does so what
happens when you commit when you are
into the dash head mode because you can
do that exact same stuff happens git
first looks into the head file it says
okay I'm in detached head mode so I
simply need to update the contents with
the show of this new commit and now I'm
there
and then if you want you can create a
branch from that point or you could just
you know exit the detached head mode
just decide well I don't need this
commit at all so we move out of that so
this is detached head and now let's talk
about deleting a branch what happens
when you delete a branch we have seen
already that when you delete a branch
simply this file disappears so that is
easy because in this case we delete a
branch that points to a commit but that
commit is a part of our history of our
main line we have Master which has two
parents because that's a merge commit
and now we see that yeah this commit to
which this Branch pointed is inside the
history so it's safe to delete but what
happens if this is the case so you
didn't merge the branch and you decide
to delete
well um okay let me let me demonstrate
quickly
I'm going to go into
this demo where I have exactly this
situation I have Master which is
Advanced two commits ahead of Mike
Branch so I want to delete this feature
Branch so I'm let me do that I will just
do Branch sorry git branch
Dash d stands for delete and then Branch
name feature zero one and then git will
complain it will tell me no no no no no
no no wait if you delete this
what happens with these two commits take
a look
they are not a part of the history so
git is smart enough to tell me wait
I want you to consider that you are
really sure that what you are doing is
correct and the same will happen here if
I just do delete branch and then choose
feature one
yeah I get an error message which tells
me the branch feature one is not fully
merged to delete anyway and if I say yes
delete Branch what will happen is this
that I should use the capital D in here
and when I do this let's take a look
gone
so commits are gone
so branch is gone and these commits are
gone so I don't see them anymore in my
history
uh
well the same thing would happen for
example if I'm in the detached head mode
and I've done one commit to see okay
what would happen if I like I've
identified where I did something wrong
let me try to quickly fix it by doing a
commit there to see if this would be
better and then I realized nah really no
so I'm just going to abandon this commit
so you just exit out you check out into
your branch well this commit
it's gone
so this is the situation like you have
those dangling commits so these commits
are not deleted we call them dangling
that's the official term they are still
in the database they are not deleted
they could get deleted eventually but
git is going to preserve them for you
for a little while so let's take a look
about recovering commits git never loses
anything
if you ever perceive that you have lost
something that's just your perception
well this is at least not immediately
true so get my delete stuff for you but
not immediately never immediately you
have ample grace period as you will see
and also you can recover from all
situations unless of course you are
hacking through this git folder which I
said do not do that at home so let's
take a look a little bit about how can
we
recover lost commits there is this thing
in git called reference log and again
it's not the same thing as log it's not
potato potato it's completely different
thing git log is what commands like what
tools execute when they present the
graph to you so you will see the history
of commits on your main line or whatever
your current branch is that's git log
git reflog is reference log it keeps
tracks track of changes to heads all
heads which is all branches so whenever
a tip of the branch changes which is
typically when you commit something
reflog will keep a track of that so
let's take a look at this situation here
I'm now in this repository where I've
just deleted the branch
and I've seen two commits in there but
they are not in here I only have these
four so I will do git reflog
and I get this list this is not history
this is history of changes to tips of
branches I can see here how I was
switching between branches which branch
to what branch at what time uh so this
is this is the reflog they're they're
deeper ways to look into that it is a
plumbing command but it can be even more
Plumbing than it is so what I can see
here is that I have some shots which I
don't see in this list like for example
this one so this was a tip of my head
and this was the tip of my head at some
point in the past but I don't have these
commits in here
so let's take a look at now I know that
I can detach my head into them so I do
git check out and then this
um
for example
6695 and look at that
I'm somewhere checked out into a commit
directly which was lost but it isn't
lost because it's never lost never is a
long time so let's let's not talk never
but these are the things that you can do
so nothing is really ever lost in it
uh we have another way of of identifying
things so let me now check out back to
master so get
check out
master and again this was detached head
state so this commit is again lost kind
of but it's not so there is another
command it's git
it's not it's file system check
fcsfsck and then you do this lost Dash
found
and will tell you that you have one
dangling commit but why one when I know
that there are two like I've seen that
there have been two like reflog has
shown too well because the only really
dangling commit is uh that first commit
the other one is referenced by that one
so it's not really lost if we recover
this one this one will be automatically
recovered because it's referenced by
that one so
um reflog will give you one view over
what are your lost commits and file
system check lost and found will give
you a different view of that but both of
them will help you identify where did
this content go so this is a little bit
about how you recover so steps to
recover actually let me just say a
little bit about garbage collector yes
git will clean up for you but not just
like that so any dangling commits are
left for minimum of 14 days
but if they were ever tip of the head
commits like they were ever ever like
commits to which a branch has pointed
they will be kept for 90 days
that's that's the duration for which Kip
keeps reflux and after 90 days git will
clean up reflux and when it cleans up
reflux these commits are up for grabs
they will be garbage collected
but until those 90 days have passed you
still have a chance to get them back
uh git will automatically run garbage
collector I mean you can call it
directly if you want but git will do it
for you
every time you do fetch when you do
merge when you do rebase and there are
some those you know Plumbing commands
which will also do it for you but they
are not that relevant because you're
most likely never going to to call them
or even your tools
and git also allows us to rewrite
history
um so
git allows us some ways of manipulating
this stuff that has happened in the past
we can for example reset commits we can
amend commits we can interactively
rebase we will talk about that as well
but what is important to understand this
is never modifying history you cannot do
that with Git you can only ever create
alternate histories
one of the properties of every commit
object is the timestamp
so there is no chance that by modifying
history you would ever end up having
same shot because time stem has changed
and timestamp is hashed so this is
always going to just be alternate
history even though you may perceive it
as a real history so uh let's take a
look at resetting you could think of
resetting s git undo so what does it do
it actually moves the head pointer
backwards
and it is useful for example when you
when you commit something and say ah no
I shouldn't have then you fix it or
maybe you want to correct some commits
so you undo and then correct and then
commit again or maybe you want to remove
some commits from history then you just
reset do some changes and then you get
rid of some comments that you didn't
want to have or maybe you want to squash
like you have five commits you undo all
five and then just squash them together
again into one commit we will see about
all of these shortly but let's take a
look at this git reset command so let's
imagine that we have a tree that looks
like this so we have this branch that
points to this dip at the top like this
a00 a0 commit and then this is my head
and then I can do something like git
reset and then sha and I tell get to
look for that shine the history and when
it finds it it will actually move my not
head but my Branch because that's where
I currently am and it will this Branch
will now point to this Sha but this is
also there is an easier way so instead
of just writing shy you can just do it
in steps like git reset head tilde one
so what does this stand for head stands
for car and branch in theory you could
just do that with any branch but I don't
see the point
and
tilde one means one commit in the
straight line
taking into account the first parent
like this is strictly speaking what it
does there are other ways to Traverse
the branch or the history but this is
the the most common one like just undo
the last commit and then it does what
happens then is that you just get one
dangling commit and something else
happens as well so let's take a look I
will just open a demo here and I will
demonstrate
okay
this reset head tree so I have this git
graph I have these three commits every
commit has added one file so this has an
edit file first second third and I will
open my uh working tree here and then I
will just do git reset head tilde
three and press that and what happens is
that git has actually put these into my
working tree
so whenever you do this whenever you do
git reset it moves the current branch
and then of course it dangles these
commits until you maybe perhaps just
move the head again back to the same
position and takes the contents and puts
them into the working tree
and now they are there and you could
also do it like this you could say git
reset head tilde3 whatever dash dash
soft
this will put them into staging area
or you could just say hard of course it
will just get rid of them so they will
just stay dangling and then there is a
way to directly modify commits so for
example you could
um you realize okay I made a typo in my
uh my commit message I want to correct
that so you can amend a commit or you
can you realize oh ah that was this file
which was on staged I want to make that
part of my commit as well so you do that
or modify some properties like I want to
fake Waldo I say like okay Waldo
committed this just because yeah there's
some in there and I don't want
anybody to know that it was me so yeah
well I'll do and fine now commit amended
different author yeah it never created
it never actually changes the last
commit let's take a look I'm going to
amend a little bit so uh I will say that
I have
this
amend demo where I already have a commit
in the database so I have committed this
and now I have some more files but I
realize I've forgotten about this file
this should have gone there and then I
just say commit amend
and then it asks me what is your commit
message please and I say well I'm fine
with this so I will close this and then
what happens is I get this first commit
with second file in there and I say yeah
fine I also want this third in there and
I will just do this I will just say uh
first commit
different
message so now I've specified the
message so it will not ask me again so I
do get staged amend and I can take a
look and I have this message and
different content but this has not
changed
the original commit it has added more
commits to the database and just kept
the other ones daggling dangling so if I
had this situation and then I decided to
amend and then I decided to amend again
I simply get new commits and the other
ones are dangling maybe I will want to
recover them maybe I will not want to
recover them and they will be garbage
collected eventually so this is simple
simple history modification there are
other ways what is important to know is
that all of these things are only safe
before you push
because they are destructive they
actually modify what your history looks
like so when your history is up there on
the remote you cannot do these things
anymore
they are just not compatible git will
never allow you to move your tip of the
head on the remote backwards well I mean
there are ways of course but they are
all hacking and recovering from people
who do something and I will show you
what that something is with the big
caveat so any destructive changes are
automatically prevented by git and then
you say okay but this is my Branch I
know what I'm doing so yeah you can do
git push force and then git push force
will simply send whatever contents you
have to send
if the Shahs are already there it will
not send the shot but it will update the
tips of the branches on the remote
without checking so it will just if you
push your Brand's Branch let's say
feature one and you have reset three
commits it will simply update the tip of
the branch in there without checking is
it safe to do so
so it could feel that you have solved
your problem but it might not be the
case so I'm not saying that you should
ever do that
yes if it's only your branch and if you
know exactly what you're doing this
could be safe I mean I have been doing
that I will be doing that but I'm saying
be careful with that don't just
routinely do this so it's better that
you do not do destructive changes in the
first place
so a little bit about these uh this
revision control some takeaways first
branches are just pointers they are not
adding overhead to your git system git
never loses anything at least not for a
while lost commits can be recovered
at least for a while and you can freely
rewrite history before pushing so you
can manipulate what you are going to
push that's why it's there so you are
working like what I'm often doing like I
I do a lot of commits this that and then
before I'm about to push I just look at
that and clean up if that there is a
mess that I I don't want to be there
like why why do I need in my history
some fumbling between some files where
that's not relevant but this is
something that you can just do before
pushing like after you've pushed
whatever is there is there let it stay
and let's talk a little bit about
integrating changes so what is
integrating changes what is integration
and actually continuous integration is
about this kind of integration this is
well colloquially we call it merging
I've merged my Branch my branch is
merged so we just say merge but merge is
just one of many ways how you can
integrate changes between different
branches so what really is integrating
well you have let's say a Mainline
Branch whatever you want to call it
and then you have some other branch
which contains some commits that somehow
need to end up in there that's why I'm
not showing those you know lines what is
the parent whatever and you simply want
these commits to be part of those
commits so that's integrating branches
and then let's take a look at the ways
how we can integrate branches the first
way the most common the most obvious way
and also probably the most intuitive way
is merge this is what git will do unless
you tell it to do something else so what
is merge imagine that you started from
here this is Master branch and then you
Branch out into a topic branch and then
you advance by two commits and of course
you know Master Advanced because other
people have been committing their stuff
and merging their stuff so you have some
more commits in there that you don't
have in in topic Branch so what you do
when you merge you in fact create one
commit with two parents
so it points to two different ends and
it essentially combines two histories
together into one and from that point on
both of these parallel histories are one
history that's the point of integration
it combines histories
good that's the merge it's as I said
like the most intuitive one really easy
one to follow
uh and these are the commands when you
merge you typically delete the branch
and this is the best practice
two things that you should never do once
you have merged your branch
you do not continue from the Old Branch
you can do that safely only if you have
first merged your branch into Master
using fast forward but I mean just
delete and create another Branch with
the same name for all I care
but never never continue developing from
the commit that was the parent of the
merge commit that's how you get repeated
conflicts and issues Downstream
and in other workflows
other than merge workflows it can be
especially especially dangerous another
thing that you should not do with these
topic branches is branch of them
because that's another recipe for
disaster we can see about that
let's talk about another way of
integrating changes this is Fast Forward
have you heard of fast forward
yeah okay uh do all of you who put your
head hand up know exactly what fast
forward is
now there are fewer hands up so what is
Fast Forward I mean we often hear that
or see that or git was able to fast
forward what is this I don't have a clue
but let's take a look it's nothing
special so let's imagine that you have
added two commits
to your branch
and in the meantime nobody has added
nothing to your main line
so what can you do I mean there is no
need for a merge commit there is only
one straight line of History so you fast
forward Master Branch to Simply point to
that last commit that's fast forward
because there are preconditions under
which git can do that that's that there
is only one single straight line and you
are on that line already so you just
just fast forward this and there is no
need for an extra commit extremely
simple and this is the cleanest
situation so you actually want those
situations they are your friend whenever
git can fast forward you should be
happiest because there are no conflicts
with fast forwards this is just you know
just advancing because everything that
is happening on the main line is already
in your branch
let's fast forward very very simple and
then there is this funny one
um okay I'm showing commands when you
fast forward you also typically just
delete that Branch because you don't
need it
uh there is this interesting one it
again depends on your branching model so
some branching model models want this
like for example git flow I will not go
into qualifying like is it good or bad
if it works for you that's fine but git
flow actually wants this to happen
and the devops for example allows you to
configure your pull requests so that
they actually demand this so even though
it's possible to fast forward
like in this situation you actually want
to do this
why because you want to see that another
Branch was integrated at this point into
this Mainline Branch so you get a commit
which contains no information whatsoever
except parents because yeah like it just
integrates histories well it does
contain a lot of information because it
does contain tree and everything but it
is just you know it contains exact same
content as this fast forward just
another Shah because yes we wanted
another timestamp and another whatever
just because we wanted to see that it
happened it is legitimate I mean
especially for some branching models and
that's what merged with no fast forward
policy really means so even if it was
possible to fast forward you decide not
to you just decide to create a merge
commit because you want to see that in
your history
and of course you would again delete
your topic Branch because that's the
best practice and now we get to the
really interesting one rebase my
favorite
so have you heard of git rebase
do you know that it's dangerous
yeah of course it's an ugly ugly scary
Beast don't play with it so what is this
rebase what does it do so let's take a
look at this typical situation like you
do some development your colleagues do
some development and then you are ready
to merge
and then instead of merging like
creating a new commit on top
you go back to the base your base is
that point from which you branched off
this tree and then you simply cut off
that Branch at that point
and then you take that branch and put it
on top of the tree
that's rebase I mean that's what at
least it feels
that is going on but if you have been
paying any attention whatsoever to
anything I've said especially in the
beginning of the session you know that
this cannot happen
because the commit has just gotten a new
parent and it cannot happen
like that cannot be because commit
always stays attached to the same parent
so what really did happen I mean
logically speaking that's what happened
but speaking about storage on git level
this is what happened you had this
situation to start with and now I'm
adding numbers or identifiers a b c d so
that we can see what is going on so we
have this C and D commits on my feature
branch and I decide to rebase git cannot
cut that Branch off and attach it on top
what it can do is it can Replay that
branch
so it simply does a git diff to figure
out what was the difference and it
replaced it and then another and replace
replace that on top and now I get two
copies of commits so C Prime and D Prime
which make it look as if I have just
worked on top of that point so that I
could possibly fast forward later that
is what typically happens when you do
this you simply fast forward the master
branch and get rid of the topic and then
it leaves these two dangling commits you
don't need them anyway anymore they are
merged you should just forget about them
so that's what rebase does
and now let's address why people
perceive that this is dangerous so let's
roll back a little bit and let's talk a
little bit about merging imagine that
you have this you have master and topic
and the correct workflow is that you are
merging topic into master so you do git
checkout Master then git merge topic and
then you get delete topic if you want or
not
but exact same results just with
inverted parents would happen if you do
git check out topic and then git merge
Master you get exact same histories and
it doesn't really matter from which
angle you did that once that you fast
forward your master or top or delete
your topic it's exactly the same just
you know left and right side are flipped
semantically speaking it's not strictly
the same but content wise it's exactly
the same so when you do merge no problem
I can do it from this direction or that
direction I'm your man I know what I'm
doing it's fine but with rebase that's
not the same thing so imagine that this
is the clean thing where we had those C
and D commits which are now C Prime and
D Prime and I don't care about C and D
anymore they are dangling I don't care
about them I have integrated my work
into my main line so that was the
correct way of doing rebase but imagine
that instead of me
doing git check out topic and then git
rebase master
I do git checkout master and then git
rebase topic
what I what did I just do I killed my
entire history and created an alternate
history and then I've you know like my
master in my local repository now
contains a history which is nowhere to
be seen in remote I cannot push that
and of course yes this is dangerous so
and if you have this situation then you
are well screwed so that is why it is
dangerous of course it is dangerous
because that's not the same thing it's
just like the chainsaw you know uh is it
dangerous yes I absolutely agree totally
dangerous tool I wouldn't myself want to
handle it but you know if you're a
master of that tool you know that you
this is how you hold it fine but if you
want to do it like this well of course
it's just going to cut off your fingers
so completely up to you that's what
rebase is and that's why it's dangerous
it's actually just powerful and that's
all some flows like trunk-based
development where committing to master
is totally expected from you to do this
is the typical thing you do you just
rebase all the time just remember never
rebase from Master onto something but
from something onto master and that's it
let's talk about squash what is squash
again I have these A and B commits I
don't need them as a and b because it's
too much information for my history so
what I can do is I can squash them into
one so I have a b Prime which is
essentially replay of both commits as
one commit and contents of my tree are
going to be exactly the same as over
there just remember one thing that I did
not address here is that all of these
operations can involve a conflict
if your contents conflict with the
contents of the branch onto which you're
rebasing or into which you're merging or
into which you are squashing you will
always have to handle them anyway
so I'm intentionally not mentioning that
not to complicate things it it is simple
because I just want to explain what
those different ways of integrating
really do but remember conflicts can
happen that's just not address them here
so this is squash you simply just
to take two commits put them together
put them on top and that's that's it and
then we have another one which is
Interactive rebase
so with interactive rebase it is very
similar to rebase except that we want to
take full control over the replay
process so depending on which tool you
use when you start Interactive rebase
your tool will present you with some
choices so if you like for example this
is git lens an amazing extension for git
for visual studio code that I really
recommend
it will give you this nice graphical
overview if you don't have git lens it
will just be Visual Studio opening that
file that you have seen like when I was
committing it put this commit message
file with some comments and some
instructions in there it will do the
same for this for uh interactive rebase
so what does interactive rebase allow me
to do well you say that you want to
rebase on to some specific commit or to
or onto some specific branch and then
it presents you with the list of all
commits that would be replayed
and that it then it allows you to do
changes to it like you can decide to
edit a specific commit or you decide to
drop a specific commit or you decide to
modify the con like message or you
decide to squash some commits together
like you you get the full control over
what is going to happen so for example
in this in this case I have uh one edit
so it will replay this bottom commit and
then it will stop and allow me to change
the contents of that other commit which
is being replayed so very very powerful
tool really even more powerful than that
you know chainsaw but also very very
useful uh so with Git interactive
rebates you typically end up with
scenarios like this like you take some
contents of your branch
put them onto another branch and then uh
then you move on and then of course you
would just fast forward your master and
then you would get rid of your topic
Branch so and then I have one more
which is cherry picking so I believe you
have heard of cherry picking
uh cherry picking is also a way of
integrating changes from one history
into another history so uh what exactly
cherry picking does well
um first of all you are in the branch
into which you want to cherry pick from
another branch
and then you say I want commit a from
here and then it advances your head
immediately and then you say I won't
commit C from here and it again replace
that you don't take those commits you
replay them so that's why we have a
prime and C Prime in in this case that's
because uh we have simply just decided
to
replay them we cannot just change the
parents so those are the ways how you
can really integrate uh with different
branches in git and that was all that I
prepared
so we have 15 minutes left for QA I
thought that would be
just about enough
if you think not then we can stay longer
but
yeah I'm not going to commit to that
so
thank you for attention first
good morning Waldo
okay
so which git pains do you have yeah let
me start here
we often use chirping
just just sorry uh do we have a
microphone for audience when they're
asking questions
we do
so let's just wait until it arrives
um
I don't see it here so yeah
why are you git pulling out
foreign
okay there is no microphone so I will
just repeat the question it is yeah
yes I know I know that I try I'll try to
not kill anybody because like once I
almost did so hello
does it work I don't know okay okay
right so uh we often use chirping I
don't know why it's
you know somebody told us that
um
but but in 50 of the time I get
enveloped object when I try to cherry
pick and try
well what kind of object do you get an
enveloped object invalid object yeah
okay no clue why it is
well I really cannot tell you what are
you using to cherry pick are you cherry
picking a bit command line online so
you're in devops and then your command
line I just have a nvs code and then get
your pick sure which I get from Devils I
don't know but I could say like if you
cherry pick a merge commit I would
imagine that you could get some mess
yeah that's not what you should do you
should not share a big merge commit okay
they are not intending to be
cherry-picked and sometimes it works
sometimes doesn't no that that can
depend I I guess but that's not a good
practice that's the only situation where
I can get that you could a consistently
expect problems
because merge commits are not they don't
have I mean they do have content
themselves but it is just content that
they they are essentially just conflict
resolutions when when you look at the
git diff perspective but you don't want
to cherry pick from them because it's
very difficult forget to determine what
exactly changed because it has two
histories
it can have three I mean you you can
that's okay I'm not saying it it easily
can but uh never cherry pick from from
merge commits cherry pick from commits
other commits like normal commits like
those
inline commits yeah I I can imagine that
could be the problem but without seeing
the exact message like the exact
scenario I cannot see them then doing is
going going into the uh pull request and
taking the individual commits and then
yeah but then I need to replay all of
those commits instead of doing one well
then you can do interactive rebase if
you have more cherry picks to do like
instead of just doing one by one you do
interactive rebates and you just say
this this this not this and
yeah
uh yeah I need to give shirts out so
yeah yeah
um
I have three shirts
by the way uh
let me let me see let me hear clap your
hands if you're using object ID Ninja
okay good if you do you want the sticker
for your laptop
okay then come after the session here I
will that will be giving stickers out so
uh yep and there was the question sorry
there was a question over there yes
exactly so uh try to survive
yep okay
and yeah let me hear the question and
then I'll decide okay sure he tried uh
when we start to use the git uh for
example also the merge the CL code in
txt format for example but also in
business Central we try to use this
approach we create in a single
Repository
three branch that we you always open not
not delete it anyway and we try to use
the the three branch level developer
test and production for example but we
uh we met uh difficult because in
several case
we have to uh
resolve more conflict because
we we are
say six seven developer that we try to
attach commit the same Committee in the
same time in the single branch now I
understand why
is this the wrong way but I yeah an
excellent question it's an excellent
question yeah so absolutely you deserve
the shirt
okay and let me address this question
now so uh there are many different
branching models what you have described
is a branching model I'll take the mic
uh a branching model describes how you
should create branches when should you
create a branch when should you delete
the branch when you should integrate the
branch and how you should do all that it
also this describes in into which
branches you can commit or cannot commit
and different branching models do
different things and require you to do
different things but not all branching
models are equally good for everything
so uh I understand that a lot of people
are struggling with finding the best
branching model and let me help
everybody who is still struggling the
best branching model out there is the
trunk-based development there is a
website called trunkbasedevelopment.com
with no dashes no nothing just drunk
based development read it I I honestly
recommend like for me this was an
eye-opener
uh in that branching model you have one
branch called master or main or whatever
you want to hold trunk it doesn't really
matter
and everybody locally Works in that same
branch and then when you do you either
if if you use a workflow which requires
pull requests then you just create a
very short-lived Branch to create a pull
request but otherwise you just push to
master
and if it looks scary like you say like
what is this guy talking about well let
me just tell you this Google has three
repositories for everything they do
one is for Android one is for Chrome and
this covers for five percent of what
they do well the 95 is you know Google
Docs Google Maps Google search Etc
80 000 people commit straight to master
every day there
and that's why they are efficient that's
the most efficient model like no test
branch no I you can do them as like but
it's so much easier if you don't like
your your pipelines don't require an
extra Branch just to be able to run a
pipeline you don't need a branch for
that but you will have extra work to
maintain that branch and to resolve
conflicts on that branch and the more
branches you have in parallel like those
Perpetual branches the more work you
will have to solve the problems that you
wouldn't have if you didn't have them in
the first place and then you know if you
use the rebase workflow I did not show
conflicts but conflict resolution is
much different between rebase and
um and merge like a lot of people hate
rebase because you let's say you have 15
commits and there are 20 commits on the
master and you now need to rebase and
then bomb conflict so you solve the
conflict continue bomb conflict you
solve the conflict bam third conflict
fourth conflict fifth conflict yes
that's how rebase works it will conflict
out on Commit level well whereas merge
will conflict out on the merge level so
but
that's why I prefer rebase yes maybe I
have more work but this is really
focused and I really know exactly what
I'm doing I pray for having like one
small conflict per commit and then I
resolve it rather than having 75
conflicts across you know 300 files and
then I need to spend like three hours
merging so rebate is cleaner in that way
and then it gives you this much easier
history to handle so I really recommend
like read about trunk-based development
good companies do that Microsoft does
that
so talk to them like ask them how do you
branch
they don't not well they do but not like
not like they're not so Branch happy
like the rest of us are
yes a question
thank you and a possible shirt of course
and many times when I try to it's not
maybe git but after the match and
putting everything into devops I get
sometimes there are multiple merge
Branch detected
I have no idea why
oh
can you can you please can you please
repeat like what exactly do you do
um it's it's just my pull request to the
test Branch or Master branches it never
it sometimes happened when a lot of
developers working in the same branch
and I think there is some issue with
some Comics yeah well the only way to
work in the same branch is rebase
workflow you cannot work in the same
range without rebase workflow otherwise
you will just have a message always
match everything beef but don't merge
rebase rebase yes you cannot share a
branch without doing rebase I mean you
can of course just if you if you if you
want to do a lot of different branch
different branches every developer has
his own brand but then we have to match
it into the one yes so you will get
conflicts probably all the time because
like if let's say five of us are working
all on the same object and touch the
same
place in that the first one that got
gets merged is happiest because yeah no
conflicts but the next one will get a
conflict and we'll have to resolve it
okay so I have no uh issue with the
conflict because I can resolve that but
then I have some kind of issue in the
devops which is this multiple Branch
based detective well then I would say
that probably a devops is set up
incorrectly like maybe you have too many
branches to handle there I don't I don't
really I would really need to know more
about your your branching model but I
mean everybody can just figure out like
every time you hear a question with
problems there are always multiple
parallel branches involved there is like
not that many problems when there is
just one so I would really recommend
like everybody who experiences merge
issues or workflow issues when there are
multiple branches like I've seen people
having like maintaining I don't know q a
branch test Branch pre-production Branch
production Branch development Branch
Master Branch nobody has a clue what
they are and maintaining all that just
what amount of work on necessarily so I
mean if it works for you who am I to
tell you not to do that I'm just trying
to tell you look into how other people
do things like I think that you know git
is 17 years old uh SCM is you know like
probably 40 50 years old uh continuous
integration is almost 23 years old 33
years old this year
I mean let's not reinvent Wheels let's
take a look at how professionals do that
like how Facebook does it how Google
does it how Microsoft does it how
Twitter does it they all have one wrench
and then yes you can have release flow
for example what Microsoft does then you
just have a release branch which is
short-lived or midterm lived which you
maintain to maintain a specific release
but it doesn't quite work with uh with
kinds of products that we develop if you
develop an offering let's say something
on SAS where customers can come to your
website and then obtain a business
Central that you control and that you
maintain like Microsoft maintains their
sauce then release flow is amazing like
you have trunk and you have released
branches for each release which you
support for a while cherry pick from
Master something that needs to go in
there and then at some point it reaches
the end of our end of support and then
you delete it or or archive it but other
other than that like most of those
multi-branch approaches just cause extra
work with without that much extra
benefit so yeah I will give you the
shirt because you are re-emphasizing the
point
I'm out of shirts but that doesn't mean
that you need to be out of questions we
still have two minutes and 13 seconds
left by the way uh
let me do it like this
catch
and catch
and then catch up there and then share
those stickers because it will be
difficult to do that in here yeah let's
let's hear more questions so I don't see
where the mic is yeah just throw it over
there
thank you uh I wanted to ask about well
about how git stores the big files
because I know that for big files you
usually get a lfs extension is used
and what happens when that extension is
is that full file still stored here you
mean when you say extension is yeah I
mean like a single step file yes well I
don't know if I would keep Al apps in in
git especially if you rebuild them
because then you would get conflicts
which are very difficult to solve
because they're happening so one thing
like when I said that git is fine with
handle binary and we perceive that it's
not why did I say that well git doesn't
really care what your content is it just
sees binary but when it sees a conflict
then it will inject some text messages
in there and that's what breaks the
binary stuff
so git is fine with with binary as long
as you can make sure that there are no
conflicts on binary level and I'm pretty
sure I'm not sure that I would really
keep binaries in git like for apps
well uh there are better places
well okay in I I'm not saying that like
you can have artifacts like images like
audio files like stuff but then you
should probably just not you should
organize your work that it never
conflicts so it is fine to have large
files in it
uh it is what what is not good is
changing them too often
or having conflicts on them so you
should structure your workflow to never
conflict out on that so let's say you're
handling images like you have a 500
megabyte Photoshop PSD file in there
you know that if you have five people
modifying it at the same time well you
are absolutely not going to be able to
handle that but if you make sure that
one person can do that then
it requires some you know soft approach
like some I don't know power PowerPoint
oh sorry not PowerPoint but the
SharePoint or some teams or some you
know whatever
like can I please just have this for me
for the next half an hour and then you
do that but yes conflicts on binary
level are
a big problem
what will be a big problem is if you
really have a 500 megabyte file that you
have modified it will eventually need to
be pushed
and that's 500 megabytes to push so my
question is does it really need to be
there maybe like if you have those files
you can get them into your repository
with some scripts from some other place
which is not necessarily under git
Source control that's how I would
approach if I really had a massive
amount of
uh binary files which I need to handle
because they do cause transfer you know
like push and pull or fetch they will
just uh but it's not also a binary file
for example let's say translations file
or a really big big uh yeah exceptions
well with translations you'll you will
definitely get issues you will not get
that many conflicts I mean conflict
happens when you get the change by two
developers from the exact same spot
and yeah git will sometimes like what I
prefer is keeping empty lines in git
like between logical things
because when you are changing something
you're typically changing one logical
thing so if I have like let's say table
I have a table some people will do field
field field without lines in between I
will add lines in between
because git is much easier to detect
that like I add a field and you add a
field if there were no spaces in between
it may it will always see this as a
conflict but if there are spaces if
there are circumstances under which
depending on like the surrounding code
it may see them as just two legitimate
additions to the same spot and will not
cause a conflict so
um I mean translations are just long XML
files which you know are not well
structured for git so if this if you
change two consecutive translations yes
you will get conflicts but I mean that's
the life
that's just a part of work so
thank you you're welcome
um
okay we have yeah sorry
survived
uh why would we want use or need to use
rebase
why do we need so if we are working in
trunk-based development
uh
imagine five people
committing to the same branch
how do you make sure that there are
least conflicts possible
by alerting them off of a conflict every
time that you can
the worst kind of conflict you can
handle is emerge
commit conflict so imagine this like
look commit something and Simone commit
something
and there is a conflict between them so
they resolve the conflict in the merge
commit now you want to merge and your
conflict arises from their conflict
resolution that's a nasty one to resolve
so in
in rebase workflow you don't have those
you simply have very clear conflicts
which are just you know very obvious and
very direct like on Commit level here
you don't know where does this conflict
come from is it from Simona's work or
from looks work because one commit has
two parallel histories and git diff
cannot tell you the the straight answer
because how does git diff know what is
causing conflict it doesn't there are
two histories to consider whereas when
you have straight line you have one
history to consider that's but that's
you know for trunk-based development I'm
saying for trunk-based development
attempting to work
with commit sorry merge commits all over
the place it's just not going to work
because you will have more conflicts to
handle which are not real conflicts
so in trunk-based development also
another prerequisite is that you need to
commit often you cannot like work on
your brains for two weeks and then
commit you you commit five times per day
or once per day but not once per week or
once per month they're no long-lived
branches in in trunk-based development
or long-lived work so there are other
problems with that like how do you make
sure you don't break things but they are
not a topic for this but when you're
working in this straight line when you
have narrow small commits uh conflicts
happen not that often because if you
let's say you change two files and
commit and Simone before he starts
working on his next change just that
gives get pull rebase just get whatever
wherever he is on top of whatever if
there was no conflict then most likely
they will not be because there was just
a small commit even though he might
change the same thing that you changed
if he does that he will not ever see the
console he will just see the oh change
done by Allen I will just change to what
I need and done nice and clean with long
living branches with with you know a lot
of merge commits it's very difficult to
uh to make sure that you know you don't
have to merge merge conflicts
or resolve marriage conflicts because
that's that's where git is really
clueless like what this history that
history
it can give you some best best guess but
that's where you know I often get asked
in in my git courses why do I
continually get the same conflict like
I've just resolved that and then I get
the same one like why that's why
like you have merges all over the place
you continue working from your branches
you Branch off your topic branches and
then you you know like like if if you
want I no I cannot anymore because I'm
off but I I did prepare some q a because
if people ask I'm ready to present but I
really have a nice flow like what can
happen when you Branch off branches like
I do a topic branch and then I do
subtopic branch
and then I decide to kind of that's just
a mess when you take a look at git
commit level at tree level
it's just unbelievable what's going on
there and it's it's not resolvable so
that's why I'm saying like if if you do
this and you do git rebase with smaller
Focus commits you will experience far
fewer conflicts than if you just do long
living branches it's just statistics
people
like if you if you create 50 commits
over you know two weeks and then you mer
like and there are 10 of you
you know and all of you have done 50
commits in 10 week in two weeks there
are going to be conflicts but if each of
you does five commits a day
nah most likely you will not get because
I've just done one commit to push
rebase
I mean chances that I will hit into
conflict with you are so much smaller
I mean every time you you need to
resolve a conflict that's just wasted
time
just wasted time
yeah
anything else I see a lot of you are
still here so not hungry
you're going to get out of food
yeah yeah yeah thank you I was like
wondering a little bit how it works like
on my file level like you said like a
branch is also just like a commit
like how does git handle like the
difference between like a normal normal
commit and like a branch branch is not
commit branch is a file that just points
to a commit points toward me yeah it's
just a pointer
it's extremely lightweight it's not
cheap because of that you know branches
cost
branches create distances between you
guys so they they cost in terms of
possible merge conflicts but they are
just so lightweight so impossibly
lightweight just small short file 40
bytes long
contains just a pointer to a commit and
that's it so and if you create like a
new like a new mask like a new current
state of affairs then it creates just a
new file and it's like on top or
something like that so when when you
when you fetch what git does is it does
two things first it takes a look at your
head it points to master let's say then
it goes to remote and says Okay I want
to to get everything that happened on
master and then you you know your Shah
where you are that shy has to be in
history of remote if it isn't then
somebody get pushed forced
so in in most scenarios it will just be
fine Yorkshire is in their history so
everything that happened after that Shah
it just ships you those commits those
blobs and then it also ships you heads
like all the branches that are on there
and that's what happens it just stores
those files locally for you so that you
know what our other ones yeah
well
okay I think or are there any okay there
is another question two questions
um how would you deal with
confidential or sensitive data that has
been pushed to a repository and
committed of course well if it's really
that confidential then I just say like
stop your work everybody just if
possible get this repository offline so
that nobody can access it because the
moment you say people stop work
everybody will just pull because what is
it so important so okay just joke jokes
aside you you get push Force
so if it's pushed you simply you undo
stop everybody
correct it like you rebase it out of of
your or you cherry pick it out whatever
like there are millions of ways most
likely you if it was last commit just
get reset head one and then get it out
and then push Force to to kill it on the
remote because dangling commits on
remotes are not going to be fetched okay
so there is no chance that somebody will
just fetch that but if they know Shah
then they can they simply create a
reference to that and fetch that and
yeah
so uh git force and then of course
somebody will have a problem because if
they continued working and you have
forced some other history then they will
just have to kill that branch
and then re-fetch that branch and then
maybe just replay it or rebase or there
are things to do but this is how yeah
you're welcome
um there was another one yeah
so how would you deal with deployment
from one trunk based into different
staging systems like you have an
internal revenue you have different
pipelines I probably don't need
different branches maybe I do I'm not
saying it's wrong I'm just saying it's
probably far more work so depending on
what exactly you are doing like I can
imagine that when you are deploying to
multiple different systems you're
probably supporting multiple different
runtimes like 18 19 20 whatever no I
mean um different code versions like you
have the production for the customer
then you have a release for the customer
to test new features then you have an
internal test to test the newest
developments that the customer shouldn't
get
yeah so uh
it well
their Concepts in CI and CD which like
for example you have things called
Canary release you have things called
like dark launches you have things like
feature Flags so if you have one trunk
then you can control with feature Flags
like you build all your code but not
necessarily everybody can have access to
that code
so there is a feature flag with which
you can control if somebody can use that
or not like that's what Windows does
every all the time or Visual Studio code
or business Central for that matter like
you will get you will get code released
this is called Dark release where code
is out there
just you cannot
use it until you as the owner of that
code like flip the switch and enable
that code so that it suddenly becomes
active but I that is one of the ways
like you you don't do it on Branch level
because
branches are an obvious way because they
seem the easiest but the problem becomes
like when you have like you as a
developer do a change and then somebody
else on your team also does a change and
then if you run into conflict and you
need to deploy this to multiple branches
it can be easily multiple conflict
resolutions and especially if you don't
have a very clean flow like I must first
merge here and then here and then here
and if somebody just merges there before
going here and there and then I mean
that will be a mess
it can work I'm not saying it doesn't or
whatever I'm not criticizing people who
do it like that I'm just saying that I
strongly recommend that you try
different approach you read how other
people do that and and that's all I mean
with branches it is always more work in
the end it always ends up being more
work maintaining different branches
making sure there are fewer conflicts
it's it's not easy
so yeah
that's that's it I think we should
we should we should end thank you very
much for attention uh enjoy the rest of
the conference and yeah see you around
foreign
[Music]
