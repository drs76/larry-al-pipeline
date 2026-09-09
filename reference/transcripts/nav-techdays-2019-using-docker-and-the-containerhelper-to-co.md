# NAV TechDays 2019 - Using Docker and the ContainerHelper to convert your C/AL solution to an AL ...

- **Source:** https://www.youtube.com/watch?v=NKqYa3Oyi3Q
- **Video ID:** NKqYa3Oyi3Q
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 92m24s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

okay welcome to this session my name is
Freddie Christiansen I'm a Technical
Evangelist and with me I have Nicola and
I'm a senior software developer with
Microsoft we are going to talk about CIL
2:00 a.m. we have like a few objectives
here we want to show you the big picture
how do you get from from one world to
the other this morning in the session
from that was called I think the road
from cl2 al they took they promised you
that this session was going to be with
sharks and with crocodiles and that's
actually not true we had to Twitter
picture with those creatures but we
decided they were too dangerous to have
in the session so we left them out we
will however have a several in here so
and and Nicola will do his best to avoid
a Hindenburg disaster I think we're
going to give you an overview of how to
get from a CL code customized solution
to a AL solution in 15 and we're
actually going to demo the all the steps
in that we're not going to go in detail
with the text to Al Alex already did
that this morning we are also not going
to go in detail about the parameters in
that we are however going to convert the
code and upgrade the data we're also
going to talk about the obstacles that
are during this upgrade process and why
you should yeah
consider the different options you have
and in some cases why you maybe should
wait a month or two before actually
going there we're also going to discuss
the pitfalls and of course since I'm
here I'll tell you that you can do
everything in darker you don't have to
do everything in darker though all that
we're doing here and I actually will
spend just a few minutes to demystify a
few things in darker and say well
everything we're doing in darker is
exactly that you do it in a VM
in any other machines we've just created
a number of yeah helper functions to
make things easier when you're using
darker and then everything is prepared
for you in Java before we go into the
session I want to highlight one thing
hashtag bcal help we actually decided
that this hashtag should be kicked off
here tech days like and hashtag where
people could write questions and the
community could answer like there's a
hashtag called sequel help doing the
same thing and we wanted to kick it off
here and I send out an email to the MVPs
that they should kind of be ready to
monitor this hashtag and somebody then
started to use the hashtag and since
then we've actually had a lot of
questions so introducing is the wrong
word but the slide was created for this
purpose so I didn't want to change it
but use it
hashtag PCL health answer questions ask
questions it's not Microsoft standing
behind that it's not us or support that
is answering all the questions there but
it is a common place where all you guys
in the community can help each other
getting help for Business Central and
here with that I'm gonna give the word
to Nicola thank you for it so if you're
going to start with the big picture and
as you probably experienced it yourself
there are many questions that might
confuse you with the latest release
right so one of the commonly asked
question is how do you update the latest
version how can we get into the cloud
what's happening with this system
application how can we convert the code
and what the consequences of this are
and what is discontinued and if you're
feeling confused it's not you many
people are feeling confused and the
quote one of the pardons he framed it
the best he said there's so many bricks
right now that is really hard to see
where each piece fits right so it's
really hard to see the big picture so
we're starting with the big picture and
we will answer this question what was
this continued first because that's
this question so the things that got
discontinued is CL we have replaced it
with Al and with that we have replaced
seaside with vs cot it's the last
release for the Windows client was the
previous one right now we're in the web
client you may hit some issues with the
client side dll's
there will be a session tomorrow that
will show you how you can refactor the
code if you're using any client side
Delos the last thing that was
discontinued is the XML profiles we
could replace them with al profiles and
there is a documentation topic that can
help you have to move away from this one
we did a systematic refactoring us you
probably know and this is not a
discontinued thing but it is the
additional work and we are planning to
discontinue the integration management
or integration records and we want to
replace them with the system ID because
we are seeing a lot of performance
issues we have also heard from the
channel that you are experiencing some
performance issues if you are using
integration records however this was too
big change to try to rush it in the last
few months and to give you the
opportunity to adopt so we have
introduced the system ID and we are
doing a stage deprecation of the
integration record and we will show you
how does the system ID affect the
upgrade as well so basically this was
the entire picture from the
discontinuation now for the other
questions the easiest way to explain
what is happening in the applet is to
use the journey metaphor right so we are
going to start going to a journey and
the most important part is setting the
destination and the destination of
course is the cloud right we would like
to get as many of you in the cloud as
possible it is nice in the cloud the sun
is shining and this is how the ideal
architecture in the cloud looks like so
ideally you would extract all of your
customizations into the extension right
Microsoft would ship the base up we
would ship the system application and
you would be shipping your separate apps
this is the ideal architecture because
this scales really well if you think
about the incident just by looking at
the stack trace we can tell who to blame
we can easily route incidents right if
we are having their attack like this the
second thing that we are promising if
you get into the clouds we are going to
do the upgrade automatically for you
and you will only hear from us if the
things stop working right if you're
getting these exceptions now for the
next picture let's see the higher bigger
picture and if the cloud is the last
stop of this ugly journey majority of
our partner channel and users are on the
ground right and we should model the on
trend releases as the mountains I think
it's a good metaphor because nothing is
stable it's nice it's something that we
should be feel proud about right see if
you see on the left we are hearing the
14x mountain on the right we have the 15
X Mountain and the 14 X is living in the
land of CL and al and 15 X is living in
the land of Al only right if you take a
look at the picture really carefully you
will see that 15 is a much bigger and
badder mountain than 14 and al is a
bigger and badder al then on the fourth
inside if I didn't convince you to
operate you should definitely update
because grass is greener on the other
side so that's simply not the character
so for the update the thing that needs
to happen is that first you need to come
to 14 then from 14 you can go to 15 so
it's a two-step upgrade and forth from
15 you can go to plot if that is your
desire we will not cover the step 3
today that is going to be cut in details
in the session tomorrow which is called
migrating te your users of the cloud so
today we are staying on the ground now
there is an important consideration
before you updates the 15 and if I would
say air L is I would finish the sentence
with amazing and I mean if you've seen
this like interfaces right I mean that's
going to be awesome it's going to be
like when we got the events but better
right so if you say that L is a Superman
then the question is what is its
weakness right what is the Kryptonite
and there is one thing that L does badly
and that's sequence
Kimmo changes and that's going to hit
you in the object so we would highly
recommend that before going to 15 you
make sure that you do not have any
breaking sequel schema changes
this may sound hard because if you look
at the object there is thousands of
properties right and some of our
internal developers were confused in
this one but in reality it's not because
we store very few things on the sequel
so this is a table definition here and
if you take a look at this we are
storing table names you're storing field
name type and length if applicable and
we are storing primary keys so these are
the only things that you should not
change on the table if you would like to
have a good experience with moving to 15
and Beyond supporting the breaking cycle
changes is not on the backlog we are not
looking it at it right now
and this is important thing to say to
you guys because if you operate with
breaking cycle changes you will probably
waiting for a while for us to come up
with the feature that is going to help
you to think it out
al is doing excellent job with making
sequel changes because we have this
trigger in the upgrade and that is
something that all of you guys have been
doing for quite a while so L is
excellent at handling these changes so
do make sure that the schemas are
compatible before you go to 15 if you
updates to L and you still have some
breaking cycle changes and your on-prem
there is a way of to fit because you
have the direct sequel access you can
force sync the changes and we have even
some every piece writing some custom
tooling to help you extract the fields
automatically and to think out of these
however unfortunately there is no
official tolling offered by Microsoft so
if you did additive changes like adding
tables or adding fields to the existing
tables as we are going to show to you
today that's completely fine and we have
a good office story here
now so to summarize when you're updating
to 14x make sure that sequel schema
contains only additive changes we highly
recommend that you minimize the number
of modified objects and we are
recommending if you want to go to the
cloud to renumber twice we arrange and
rename if you want to get to sauce now
we are looking into making green
numbering and renaming easier going
forward so the team is currently looking
into if this is going to be possible so
we will come back to you with the news
if and when we are going to implement
automatic remembering and renaming so
that was all about getting up to 14 and
now if you would like to get to the step
number 2 now bits of 15 in the past you
were able to simply technically offer it
right but the problem for 15 is that
there is no landing place right
you can evoke the technical object and
convert the database but you need to
build an al app right so the thing that
you need to do is that you will need to
get the boat and basically need to find
the bravest and smartest people
available I'm talking about the
developers of course and they put the
developers on the boat and you ship them
to the land of fail right before our
grading and now these people need to
build the landing the plane right the
simplest thing you can do is just simply
convert to L right
you've seen the trolling and fred is
going to show you the drawing you can
easily convert CL 2 it's very simple and
you can update to this one but we are
not recommending this we are
recommending refactoring to the system
app and that should be simple so base up
should be using the system application
and you can seen in the presentation
from earlier today if you're having any
problems you can submit feedback on the
github maybe even the pull request and
you can make this thing simply
reflecting the system application needs
to be easy to do and the hardest thing
to do is to actually go to this
architecture which is the ideal
architecture and that is the highly
recommended where you have extracted all
of your customizations in
so this is the general area now I'm
going to hand it over to Freddy to show
you how we can climb the mountain I just
have the last request before I start and
that request is if you're doing this
don't go by boat
that's bad the thing that you should do
is that you should use the proper to
dock with docker right so Freddy's going
to show you now how he can convert okay
thank you
when we want to move from 14 to 15 and I
think Alex already mentioned this in
this morning session as well you kind of
have two options right you can either
convert directly like take your app
convert it all to 15 and then start
refactoring there if you have a lot of
modifications might be hard you might
not be proficient in in 15 your
developers might be used to see al if
you haven't taken up event-based
architecture yet then that might
actually be a hard journey to go
directly to 15 and then start
refactoring over there you can also
reflect on 14 so it looks like this
right if you have 14 there's a number of
things you need to do before going to 15
in order to make it a clean experience
when you get to 15 and in our case the
small sample app that we're going to
show today actually is already clean so
we did all the 14 work and then it is
easy to convert it of course a lot of
you guys will not be in that situation
but you need the no sequel breaking
changes as Nicolai talked about you need
to clean up properties in code like Alex
talked about this morning you need to
move code customizations to events so
you don't have a lot of code
customization modifications in different
code units no modification of optics in
the system app if you have modifications
of object in the system app it is much
harder to uptake the system have changes
when you get to 15 right so if you have
modified any of the things that was
moved into the system app in 14 remove
them before going there it's it's much
easier noted Littlefield no deleted
controls no code modification I think
I've said that five times or whatever so
and then if you're done with all of
these things did the due diligence in 14
then the road to 15 is easier if you go
to 15
first I mean take your app convert
everything and try to as soon as you can
make everything go through text to Al
and then mangle everything over here to
make everything compile your journey to
15 might be easier but then you have a
lot of work to do on the 15 side so how
do you determine which road to take so
it looks like this right and then we can
do a race here and see what actually
wins and I'm pretty sure that in the end
the amount of time you're gonna use
whether you take one or the other
solution o wrote it's kind of the same
so how do you determine and I think it's
more about your customers or your your
solution if you have customers running
on 14 who wants to stay on 14 for
another year then do the work on the 14
side while they are still running and
and make sure that you prepare the app
to get to 15 while they're there if you
have a customer saying I need to go to
15 now because of I don't know what well
then the lower solution might be a
better option for that customer in the
end I don't think the difference between
the time consuming time consumed for
both the solutions is that big what
we're going to do now is to take you
through a journey like what I have on
this laptop is a solution a very small
solution that Nicola created for me I'm
of course running my service GN talker
but I have my database placed on the
host and the reason for that is of
course that
I can now replace the docker container
which is running 14 with the docker
container running 15 and do all my
upgrade when I'm done converting yep let
me show you what I have on this laptop
and - just a few things to tell you what
darker is and what darker is not
switching to my laptop I have a
production web client here we'll start
that and I'm gonna connect to my
production environment having my
customers list and one of the things
that my small modification is doing is
adding a reward point system and a gold
customer system to my to my customers so
what I'm gonna do here is actually give
this guy 50,000 points and I'm gonna
make him gold the entire idea is that in
the end of this one we're gonna run this
in 15 and see that he still has his
50,000 points and he's still a gold
customer so that's our 14 let's have a
look at the database
this one is sequel management studio
running on localhost as you can see we
have a one database actually the only
database in my production a lot of
tables some of the tables are have a
dollar to read after it that is of
course a table extension where some of
the fields is placed in that one and we
can go into the tables and see what's in
there and what's not if we wanted to do
that let's have a look at some talk I
think so what's the difference between
running my service here on my host here
all running it in darker basically
nothing in darker a docker container
this is just like a VM it's just like
you don't have a GUI you don't have a
remote desktop but it is a virtual
machine where you can connect with a
command prompt or PowerShell and go into
the file system inside that one we have
darker container code talker
image is out there with all our all the
versions that we're running from now
have twenty sixteen to the next version
of Business Central and and you can just
by specifying the version you want you
can get that version and run it so it is
that simple let's have a look at a few
PowerShell things and see what we
actually can do so I said it's like a VM
and it's like the service is running
inside of that one on the desktop when
I'm running a darker container I'll
actually have a few shortcuts and I can
double click one of these this one is
opening a command prompt inside the
container so I'm not connected to that
virtual machine and I'm looking at the
filesystem
inside the container I can do the same
with PowerShell this one and what I have
with PowerShell is I already have all
the commandlets and everything that
you're used to in nav loaded so I can
say ctrl C here and paste that here and
say enter I did not
okay so instance is not okay let's see
if we have actually stupid okay
I'll do the other one then enter and
have container here and say my prod
inside of this one I definitely have
those commands loaded I thought I had
them in the other one but anyway and now
I should be able to run this one
did you know should before I said okay
now I'm kind of not knowing it okay that
worked that's fine
Saved by the Bell so what get nav so
every user has been doing for the last
ten years or so is to return the users
in the in the database right get nav app
info will do exactly the same or will
return the app info so what I'm running
here is standard powershell commandlets
for nav and/or business central because
i'm entered the container and i'm inside
that context and I have everything
pre-installed and the server instance
variable it's already set for me so that
if I have a look at what that is here so
ever instance that is nav in a 14
container and if we look how the 15
container looks a little later it is PC
so what about all these scripts that you
can do compiled objects in nav container
import objects and all of these things
well in the end all of these are just
doing the same thing as you see up there
invoke script inside of a container and
then using the existing functionality
the only thing I'm doing inside of these
high-level things kind of packaging
things that figuring out okay what
service what what authentication
mechanism is he using then I'm making
sure that everything is working with
that and in the end I'll end up calling
compile navigation object with the right
parameters for doing that in a container
if you don't want to use all these
high-level command that's because you
can't figure out or you can't really
understand what they're doing it is
totally okay to use invoke script in
container and then just write the
partial yourself do exactly like you do
if you would install the service tier on
the host so see darker is a mechanism
where you very very easily can get an
installation of any version of business
central or nav running on a machine
within a few minutes and that's
basically the only thing you need to
know there are of course things that
that can be hard to make run but we'll
try to help you with that with the
container helpers well when spinning up
containers compatibility issues and
stuff like that we are trying to to make
that work now before I do the actual
demo I'm gonna show you what I'm gonna
do first convert to Al extension we
talked about the two different options
here
you can convert from v 14 to an
extension and then you are in a good
place the only thing that we need to do
in the code conversion world here is
that we're going to create another
container which is a 14 developer
container then we're going to import our
objects into that one we're gonna
compile the objects we're going to
convert my modifications to an al app
that is done by extracting deltas and
taking these deltas and sending through
the text to al tool again there's a high
level command for doing that in darker
but again you can do all of the same
things if you don't use that high level
command just by using invoke script in
the container maybe you're running into
problems with the high level command
then that is an option as well we're
gonna create our way a project by adding
an app JSON file to that one thing Alex
told you the same this morning as well
and compile our yield project we have an
app file and now this app file can be
installed but wait a minute why should
we install it well let's see the demo
here first and then figure out whether
we can actually do something more with
that the first demo I'm going to do the
CIL - al conversion and the powershell
for that we'll see here
import objects to nav container compile
convert modified objects to al then we
are creating the app JSON file by taking
a template and setting the ID name
publish on target and then we're going
to compile our app and last but not
least I'm just going to open up the the
folder so that we can see what actually
happened inside of that folder so let's
mark all of this and press f8 to do all
of that and give it some more space here
so I already did create the container
because it takes a few minutes so it's
not doing that I think it's probably
creating a session to that one so that
it can import our objects the rewards
app code text file import those into the
container and then after that it's
important to compile the objects because
exporting to new syntax is actually
different if you have an compiled
objects then it is if you have compiled
objects meaning that if you don't
compile the objects you'll get a result
that is hard to compare with other
things so usually this goes like
lightning it's gonna be exciting if it's
this slow all the time but let's see my
laptop
probably knows that I'm on stage so
compile the objects and the next thing
is convert to Al and then it should do
the rest of the things maybe there's no
connectivity issues I'll look at that
when I give
I don't pass there
I think my laptop decided to slow down
so that everybody could follow exactly
step by step what's happening so it
export the objects with the filter it
figures out what objects are actually
modified creating keeping the Delta
files now it has a folder with all of
these things and then it will run the
tech trail to that reading the new
objects to text files so that it's going
to create a table and page extensions
for the modified files and then running
text to Al for only the files that that
were there created the al files adding
the app JSON and then compiling the app
so maybe I should just getting a little
nervous on our last demo because that
one accident take some time this one
shouldn't take so much time but anyway
we will we found out downloading symbols
and compiling so the compile app in BC
containers actually going to use the
container and compile the app inside the
container so it's going to give the
source code to the container and then
run the compiler inside the container
and the reason for that is not to
contaminate the host so the more you
have to extract from the DVD and add on
the host the more your host becomes a
machine where you only can run this
version on so this is the output of the
first one right we have our App file
here that's my app we have all the
source we can see that we have some code
units a table reward provider and we
have a table extension for the customer
and a table extension for the customer
card which is kind of fine we can
install this one and see if we can get
going on that so if we do that then our
data upgrade the new table will be just
fine we can actually map a new table if
we do data upgrade from an existing CA L
solution into an new base app with a new
extension we can map the new table from
or the existing table from the new table
you had in your CL solution to a new
table in an application we cannot do the
same with customized tables right so
what we wanted to have get out of this
was actually a companion table like I
showed you in secret server management
studio a table that would extend the
other table with those two fields that
we actually created here and we don't
have that functionality right now I
think the team is working on that and
within the next
a couple of releases I was specifically
asked not to give a date we release the
functionality so that you can actually
transfer those and get a tape extension
out of that as well probably from AL -
al but then the road is just that's
that's not so we're not gonna do this
what we're going to do instead is have a
look at the other solution now if we
have a solution like this one where we
had our customized base AB we'll add
fields let's have a look at what happens
if we do code customized solution to a
code customized solution in al the steps
or that one it's kind of the same we add
a we create a developer container with
that version of business central that we
want we import our objects compile our
objects then we'll create a 14 to X
baseline right now we have the entire
app we have everything that we want to
merge with 15 so we create a 14 X
baseline that means that we take all the
objects of that version of 14 precisely
as it was before our modifications was
added and we export those I know we have
already imported our objects but we can
still export the baseline by specifying
use baseline or you could do it when you
have created the container of course
this means that we'll have a project
with all the files in al then we're
going to create my base app in 14 in al
then we're going to create a 15
container and create a baseline in that
one what we want to do now is to do a
three-way merge of that and that is done
by taking the folders there and
comparing them as you might know there
are a lot of things that has changed
between the 14x baseline and the 15 X
baseline do we really want to compare
everything no we don't we actually only
want to compare what we modified and
since we didn't modify the system app or
since we didn't modify a lot of things
in our case we only had two objects that
we modified while we're creating our
baseline
we actually specify a a source file
destination pattern that puts all the
modified folders in files in one folder
all the new files in another folder and
all the base app folders all the basic
files in in a third folder that means
that one we want to do this three-way
merge will simply take all our
unmodified 15 x files and say that is
the result of the basic folder then
we'll take all the new objects directly
from our 14 folder copy down and then
we'll do a three-way merge between our
baseline our modified base app and the
15 X base line you might think that this
is undoable and it's tricky but you
actually can when you export the base
line from 14 you can use the text to Al
tool from the 15 container which
actually then will format the AL code in
the same way as 15 and it will put in
the spaces correctly and everything and
you do the same with the my base app
meaning that that this the the structure
of the files will be identical and it
actually in the case of the very small
modifications we have is pretty easy to
merge let's see if we can get some more
performance out of this laptop I didn't
change anything but it's switch to this
one actually think I'll get this one and
then we'll have my 15 X my base app and
let's demo that go over to this machine
we're gonna see PowerShell again the way
that you structure your files is you're
creating a file structure function here
in PowerShell to specify what objects
goes where and then you call a function
called create al project from a
container again it is only a high-level
function which basically just goes in
and exports things and does a lot of
gymnastics with the
assisting powershell commandlets i'm
gonna do the same with a 15 baseline and
the same with the with with my base f
the only difference for the 14 container
as I specify use baseline which direct
my high-level function to take the
original files that I created when I
created the container the same with the
15 container here and for the 14 base my
base app I just specify that I want the
objects as they are so they are actually
going to export the objects and create
it out of that now pretty sure that all
of that has already run so I'm not gonna
wait for that but I will run until this
point so the baseline creating the
baseline for all of these things was
very very fast and the reason for that
is that I already staged that so I did
that up front
normally it takes some time the next
step which shouldn't take any time of
course take some time and what I'm doing
there is I'm preparing my merge folder
and I'm copying everything from the 15
container and then I'm copying my
objects from the 14 containers has
talked about and then I'm gonna call the
a three-way merge tool called caitiff 3
which is free the three-way merge tool
which is free so there we are
Katie of 3 starts up and it tells me
that I have two files that is different
and I need to merge those so that's the
customer card I don't know if I can zoom
in on this one I can can you see what's
that probably the customer card table
click this one to do the merge on that
32 differences let's have a look at how
that actually works so the only thing I
did in in the middle folder that is my
modded modified 14 X source in the left
folder is the 14 baseline and on the
right folder is the 15 baseline and we
can see that in 15 they changed the
tooltip I think and let's click the
to find the next difference this is our
fields right this is the two fields that
we added in our app which is not in 14
base and it's not in 15 base the result
down here actually adds the fields to
that and since they are formatted as 15
because we use that tool that's actually
fine now search for the next difference
that's an application area changed in 15
and it actually says that if the things
are not changed in a and B then if C
changes it that becomes the result so we
can go through this but it actually did
exactly what I wanted to in all cases
I got my fields added to the 15 source
I'm gonna save that I'm gonna do the
same with the customer table click here
navigate down find yes that is our
fields that that got added here save
that and now we have our customized so
now I got it
a customer I converted everything to a
code customized solution and that might
be fine right
but actually if we look at how data
upgrade would work with that then in
this case the new table would just be
part of the base application and we
actually had no good way of moving that
out to a extension table afterwards the
customized table kind of works the
fields are now in the base app and I
actually can do data upgrade I also can
do data out great with a new table but
I'll now be in yeah stuck in a world
where this new table belongs to the base
app and how do I move that into an
extension so maybe there's a third way
maybe we can do a I know we talked about
hybrid before where hybrid was between
CL and al but right now what we can do
is we can talk about some things that we
might if
in the bass app and put the rest in an
extension the things we want to keep in
the bass up in order to do the data
upgrade right now would be the
customized fields or the customized
tables customized tables that means that
if you have added fields to a table
leave that in the base app but put all
of the other things in an extension that
has a dependency on your base app and if
you don't have a lot of code on that
table that then has a dependency on the
rest of your extension that should work
if you have code or if you have things
that depend on the rest of the the
extension in your modified table
refactor it out into code units or
whatever two things in 14 before taking
that journey so that the only thing you
leave in the base app would be these
customized fields and as I said in the
beginning we will have a way within a
few releases try to move those out to
the extension in a at a later time so I
don't have a race with that one but this
one becomes a little lengthier process
in the code conversion process kind of
the same we create the dev container
we're importing the objects we're
compiling the objects we are creating
the baseline doing all of these things
as we did before
we are however only going to merge the
table modifications we are that's the
only thing we put into the modified
folder then we're going to convert the
modifications to an al app that we did
in the first step remove the table
extensions and create a project and then
compile that one now that actually
should be something that we can later
and I'm pretty sure that this is
probably going to take more time than
our and I want to wait for so we might
want to in a moment
continue our presentation and then get
back to the demo after that let's run
some of this
yeah every so it does kind of the same
things as before it is exporting all the
base lines to different folders than
before and then we have the only thing
we need to merge now is the table
extension and when we've done that then
let's see what's happening here
we'll merge our with deleting if
everything there we're merging our or
modified folders here and after that we
are compiling our base app then we are
converting our modified files and
removing anything that has named table
extension let's go here and I'm just
gonna say save to this one because I
know it's fine go back and say yes to
that so what's going to do now is
compile our app and that's going to take
a few minutes and it's going to convert
the modified objects and then create the
extension that we want to use afterwards
the reason why I'm stopping here is to
try to figure out whether it's a good
time now to switch over to presentation
and talk a little bit about and then let
my machine work on this piece for a few
minutes and then get back to that one so
we will do that switch over to our
presentation the thing we can do when we
see that in a moment now is we're going
to get two apps out of this right we're
gonna get the base app and we're going
to get the the our extension as an app
as well and of course the extension has
a dependency on the base app that is for
us and demo some of that but it's still
running and for the data upgrade now the
new table will just flow over because we
now have the new table in our extension
we have the new table in our base app
and that can easily flow over and become
the new extension table when we do it
the right way
Nikola has taught me to do in the last
few days and our customized table will
kind of work because it it keeps the
fields in the base app and we can we can
manage that because we can move them at
a later time with that I'm going to give
the word to Nikola for a few minutes and
then get the word back when my my laptop
is complete alright so basically let's
pretend that Freddie's laptop is fast
and that it's over in a few minutes you
will see that Freddie has climbed the
mountain right and this was supposed to
be a proof that he did it but now we
know it's fake right so you think that
we are going to do in the next demo that
is going to follow is to update the
tenant in docker and to run the test to
ensure that the code is correct and you
can let me know when the update is done
because I can talk through what is going
to happen during the upgrade now so as
you've heard if you have added tables we
can move this automatically the only
thing that you need to do is to make
sure that the ID and the name matches
and then when the update is happening
during the sync step we are going to
move the tables to the instructions
without you having to write any upgrades
to be very geeky if you take a look at
the sequel definition the thing that is
going to happen is Freddie will show to
you is that we are going to add a grid
to each of the tables that got moved and
that is basically how the tables are
getting moved from crl to ale now we
have a problem that we cannot move the
tables from one extension to another so
if the table ends up in the base up
currently there is a deliverable that is
in progress which will let you to move
the table from the base up to any other
extension that you want using the
similar mechanism in reality is going to
be renaming this good and updating view
method metadata objects we are looking
into easing up this requirement then
that the number and the name needs to
match so we would like to give you an
ability to automatically remember and
rename because that can be a difficult
process right and ideal if you would
like to move it to the RSV range or Pte
range it should be easier in general so
the team is currently looking into if
that is possible and how much is it
going to cost now the part which is bad
is moving field to the table extensions
and if you need to do this one right now
this is the process that you need to do
so you need to mark the old field as
obsolete you need to introduce a table
extension get a new name and a new
number and then you have to write this
CL code which is doing the loopy loopy
right it's going to do the for each and
copy and move the field one by one and
basically this is really bad
and we got the feedback from the
partners that said like we have added
around 200 fields in our three solutions
and we cannot possibly renumber and
rename 200 fields and that's why the
team is currently looking into
automating this process however if you
would like to get into sauce with your
extension this is the thing that you can
do right now it has one small caveat and
that is if the table is big these psycho
ledger
can operate up to 800 thousand records
otherwise we would have to do something
special to make it run so this for each
upgrade is not working gracefully with
circulars yep and as I said the feature
is coming so we are going to eliminate
one of these kryptonite problems that
you are facing in the operator so one
very important feature that you will see
is the destination apps for migration
and this is a new server configuration
and the main purpose with this one is to
resolve the manifests so if you are
having an old 13 app which is targeting
the CIL it is still going to continue to
run so in this server configuration
you're going to put in all of the apps
that were part of the CIL base up in the
past and you can even add the extensions
that haven't been the part of this year
base up and the second feature that this
functionality does it is going to
publish and install is going
and obviously all of the apps
automatically during the upgrade for you
it's not going to run the install
trigger because the app was already
there you have just basically converted
it from CL into L and this is a very
important feature that was added this is
the example of the old manifest file the
platform version is still valid
application version is basically gone
there is no CL but all the apps are
going to continue to work if you have
marked them as destination of migration
how should you update the app so start
nav data abit only updates the apps that
are marked for the migration if it is
not a migration app you should first do
the migration update and then you can
publish all the other apps sync them a
call is slightly differently named
command with which is called start nav
app data update which is going to
average that specific app now one
additional thing that is going to happen
during the update is that we are going
to move the integration record ID into
the system ID and the thing that will
happen during the sync step is that on
each of the tables we are going to add a
new column which is named dollar system
ID and it's of a type grid and then we
are going to loop over the entire
integration records table try to find
the parent record if we can find the
parent record we are going to use that
value and set it on the record
preserving the integration ID if we
can't we are going to generate a new one
and we have updated the application code
so now the integration ID for new
records and the system ID are going to
match we did this because if you have
synced out of the integration IDs to the
external systems by using api's for
example we cannot basically break your
unique keys and if we would do that that
would have unforeseeable consequences so
we are preserving the system and this
the system ID functionality is really
cool because you can see how you can use
it here you can get by system ID that is
fetching the record
you can find the record by system ID by
setting a range you can give it a system
ID when you are inserting then you need
to say insert root row and then we are
going to use that system ID when you're
asserting and you can use it through the
record roof so it's pretty powerful we
have implemented it on the api's and we
are currently working on refactoring CRM
sync and other integration mechanisms to
use this one instead of the integration
record all right
so Freddy is the demo ready yep or at
least it I think I got some more speed
into my computer so just show you so I
actually already started the upgrade
process it's not completely done yet
the result of the other process we did
was to create a 15 my base app and a 15
my app the 15 my above course contains
all the files to show before including
my app file in the output folder so in
here is my app and the table extension
is gone because I deleted it before I
compiled that one the first one I
compiled was of course my base app this
is my base app source and if I go into
the base app folder here I'll see the
entire 15 base app if I go into my
modified files I'll see my customer
table modifications or actually the full
customer table merged with the base app
and in the my folder there's no my
folder because everything else is in the
extension so this is my my hybrid model
I of course compiled the base at first
copied that over and use that as a
symbols for my own app so I now have a
base app and an app that depends on that
base app and I can do exactly what
Nikola talked about before I already
started but while that is running that
we take you through the powershell for
everything that Nikola just said so
we're gonna start after the other one
here on the upgrade process the first
thing we want to do while 14 is still
running is to
install and unpublished all the apps
that is done by running the PowerShell
script inside of the container that I
talked about before getting have info
and uninstall name app get never been
full and unpublished all the apps and
get all the simple apps and unpublished
those as well now we have a database
with data and all the apps have
disappeared and we're kind of ready to
to do the conversion then the
destination files apps for migration is
a set of apps that we don't want to use
for migrating our CL database to 2:15
and we set that in the config ray or in
the custom settings file and I'm gonna
show you the trick to do that the first
thing I'm gonna do is actually remove my
production container here
that is my 14 container and after that
sentence I am NOT able to use my 14
container anymore I could of course
restore my backup from my 14 and then
set that up again if I didn't manage to
do the entire upgrade the next thing
I'll do is to create a new production
container and it very much looks like
when creating the other containers the
only difference here is that I'm
overriding two scripts the setup
database and the set of configuration
the thing that I need to do in the setup
database before I start the service tier
I used to need to call invoke nav
application database conversion so the
service here or the the container
starting and then it sets up the
database and it invokes database
conversion and then it tries to start
the service here I also need to do some
settings in the config file and I do
that by overriding the setup
configuration file again if I didn't
want to do it here I could start the
container and I could reconfigure the
service tier afterwards and then restart
the service here
and I could point to my my database
after starting the service T of course
by doing it this way I'll get a
service tear running in a container and
I it's it's just doing the database
upgrade for me if we go all the way up
to when I started that container will
actually see that some point in time
during this one it says invoke database
conversion right right there and it's
doing the database upgrade there and
setting everything and then starting the
service to you later then after that at
this point in time we'll have a fifteen
container starting but we don't have any
apps in that one
and as Nikola talked about we then have
to publish the first thing we do is
publish our symbols our system layer not
our system application and then the
destination apps for migration that's
the same apps as before just for where
are the apps actually so that they can
be installed and here we are calling
publish nav app standard command for
doing that for all these applications we
are now restarting the service here and
as Nicholas said when this works
then we are in a good place and it
actually worked
basically this reset step is the good
test because if restarting of the
observers works and you don't get an
exceptions it means that you have done
the things properly it's it's a really
good test for sanity check if the object
has succeeded or not next thing we do is
to take all the tenants run through the
tenants and to sync nap tenant on those
since this is a multi there's a single
tenant one it just returns 110 and and
that's default and works fine better
also we're gonna run a multi tenant
container then we go through all our
destination apps again do the sync nav
app on all of those and then we do the
test Navin and database schema to check
whether the database schema is fine
and last but not least the invoke data
upgrade which is a function that we
actually added here which is doing what
Nicola said start nav data upgrade for
our for is that for the apps or is that
for start nav they
which one this one the invoked data
upgrade function yes so starting
half-day target is only going to upgrade
destination observable migration start
nav app data upgrade is operating that
specific app it is for the other apps
that we have yes yep and the last thing
we actually want to do is to run the
tests one of the one of the apps that we
added for for upgrade was the Microsoft
test upgrade and we added that earlier
on so that we could collect information
about the test and if we run that one we
should be able to see whether our data
upgrade was successfully completed and
it looks like everything is green so
that's good I actually should be able to
now start my production web client here
and have a look at logging into this one
to see if we're lucky that our customer
still has what they had I mean all the
tests are passing so the master is
destroyed help and support will now say
that we are running 15.1 application
that's because it doesn't upgrade the
application number there when we do yes
you need to set it manually
so basically application number in the
database you need to set it yourself
trust us yes I think you can see that
this is the 15 app and we have the 15
and if we open the cannon group customer
will see that they still have 50,000
report point and they still a gold
customers will be lucky yes good job
so if you can go back to the script just
you know this is good this is a good
demo so you flood the refreshes the
databases so if we look at the database
now right
you open secret server management studio
before we did the upgrade so this is
kind of the information and then I right
click this one and say refresh then
everything now or not this the system
have things but everything else or not
this the system layer things but
everything one of the tables below has a
gooood behind it that's because it
belongs to that app now and we can see
that some of these are the system
happened some of these are the base up
and I guess the table that we added in
our extension would have our grid on it
right correct so we actually managed to
get everything did you want to show the
yes so one thing that I wanted to show
you as well if you open the table right
and you take a look at the columns you
will find the system ID here and if you
query the table definition basically you
will see that for this one right this
one should be empty but let's pick one
of them here
we should have generated the system idss
quits so you can see they all go to the
values one important and interesting
thing to show you here as well when it
comes to the testing for this test nav
database schema this one is actually
going to tell you if we have
successfully moved all of the tables see
if some of the tables got left behind
this step is going to fail so that means
that your ID and the name are basically
not matching yep cool you have some more
slides yes and then we'll open up for
questions
so let's switch so we hope that we got
excited and that he wants to update the
tenant but before operating the sapling
the last thing that we are going to do
is to go through some theory so the
first question is where is the object
orkut and we got this question a lot and
the difference between the previous
version and this version is that upgrade
toolkit is now included in every app for
base up you'll be able to so this is a
system of definition sorry and you'll be
able to find it in the specific folders
and we are keeping it close to the code
that is upgrading this has a consequence
that it stays as part of the app and we
are not removing it so it's always going
to be there and we highly recommend that
you follow the same pattern and put the
average close to the cortadita updates
in the folder in the base up we have
placed it in the upgrade folder because
we have 6451 objects and it's going to
be hard to find the object code units in
so many objects in so many objects and
the row that you are following is that
if you have a separate area we're
introducing a separate code unit so it's
easier to read the order of the
execution of this code units must not
matter that's the only criteria
otherwise we are putting it into the
same code unit the main update code unit
is update base app so that's where the
most logic is going to help on Prem you
can open this one and customize it in
sauce basically we are the ones that are
owning it and if you need anything we
will have to introduce events
then the structure of the object code
units it has three types of triggers
it's the exactly the same as the
extension v2 right we are checking
preconditions on database then we're
running on upgrade triggers and then in
the end we were running on validates
triggers and per database is always
going to run per company and when it
comes to the execution order we are
first going to far all of the track
precondition triggers first of all the
base up the next national accession B
and we are following the dependencies
that you have described in the app that
jason then we are going to follow all of
the objects triggers for all of the
extensions that we have and then we are
going to far all the validate triggers
so basically that is how upgrade is
being executed so applet can go wrong
right and let's say that in this case we
have done a wrong first-name and
lastname split and now because we have
multiple versions right we heard about
it late right we have 15 14.3 14.1 right
and now the question is how you're going
to fix this one because there is a lot
of customers there is a lot of data in
the customer table right and we
basically split this field in the wrong
way if we are using versions this is
going to be extremely hard because we
would have to introduce these build
numbers because that's the only way to
distinguish and now if I would like the
port the changes back to the legacy
branches I have to update the minor
number and get the build number when it
was introduced and also to the 14.1 and
you can easily see that this thing does
not work because will this code really
work I have no idea probably not right
it's really hard to build a mental image
what is going to happen if the end user
or partner comes with a certain build
number and is trying to move to another
build number he's going to be really bad
so version number simply would not work
for us because we would have too many of
them like there is it would be a see of
version number
we have around five or six of red code
units in the base up it would simply be
untraceable and unmanageable for us so
as a mitigation you're using early
attacks how many of you have used the of
the attack so far can you raise the cans
so very few people does we are going to
continue advertising it the update
attack is having following structure the
first thing is the three-letter company
prefix then we are using the unique ID
for us this is a TFS ID and then we put
the human readable descriptions you know
what it is about and the last thing is
the date when the change was written so
we can see how all the object code is
and if you would like to use it in the
production you just check if the object
tag has already been set do the upgrade
and set that we do not recommend hard
coding it we recommend that you just put
a simple gutter function which is
returning a string because if your hard
coding it across the app it is rather
bad so you shouldn't split the magic
strings around here we use the TFS ID
which is something that we recommend
because if I copy paste this number here
on the previous slide I can easily in
the TFS get to the change list see the
pull request see who did it see the
comments only on the pull requests so
it's very easy to track the things that
went wrong in reality the whole system
is just the table and the key is the
company and the tag so for all of the
methods that are per database they are
going to have company blank for all of
the methods that are per company they
are going to have a company here so if
we go back to this task where we have
splitted it wrong and if you hurt the
upgrade stack here it's very simple to
fix I need to add a new update stack
which is now named correct and I need to
check does the updates tag for splitting
it in a wrong way exists or not if it
doesn't need to fix otherwise I can just
do a correct split so this is really
good because it is also keeping you our
log which operate methods you have
executed on a certain customer so it's
quite easy to do the fixing
and this is brilliant because it is very
simple to copy paste the code across the
versions right we can even jump the
upgrades and this thing is going to work
we recommend to it that you store it in
the designated code unit that is just
storing the tags that you have in the
system because as you're deleting the
usages you can just delete one of these
gutters and then the compiler is going
to tell you where it was used so you can
easily clean up your code and this
system has one major flaw and the
weakness of this system is the new
companies or if you're installing your
extension for the first time so if
you're doing this you need to register
all of the objects tags and that is what
this event subscriber is linked so this
event subscriber is ensuring that the
object tags are inserted if for example
you create a new company
there is also method which is called sat
all update tags which is going to
register all of the existing applet acts
in the system making sure that the
things do not break so if you have
written the object code and you're ready
to update the famous last words of every
developer is it's safe right this code
cannot fail the proper question is what
is the worst thing that can happen right
so what is the worst thing that can
happen during the upgrade it actually
has a name and the name is Hindenburg's
now this is not something that I
invented it's a part of the program
which are gone which means that many
developers have faced it so you can
search for it right and the Hindenburg
is a catastrophic this need to
destroying bug so you have updated your
customers few days have passed they were
happy and then you get the customer call
and they ask you where's my date right
and then many people will say let's
restore from backup but the problem is
you can't restore from backup because
they've been using the system for three
days right and if you restore from the
backup you're going to lose the three
days of work so the only thing that you
can do is merge the date and now the
open question is how many databases can
you merge is it five is it then 100,000
because if you're running it in sauce on
a scale it can be really difficult to
manage now what to do about it
the thing that I recommend is designed
for operates think about a bridge
whenever you're doing your feet just
think if it is upgradable and have the
disaster plans in place tests that you
can actually restore from backups we did
all of these things I highly recommend
keeping the update called small and
simple our golden rule is like five
minutes code reviews if it is longer
than that it's not because if you're
trying to run is simple line of code at
the large number of databases and
customers it's it's simply not going to
work and regarding testing it is
important if you check that the correct
data is written so that we didn't
execute the upgrades and didn't get the
error and we need to ensure that we
can't run that we do not run the
operated twice to give you an example of
the Hindenburg with our application so
let's say that we decided to go through
the loop a loop you have red code and
remove these fields from the base up
right and this custom we had 50,000
reward points as ready set to it and
let's say that customer has spent them
right and now we are running the upgrade
the thing that is going to happen is
that we are going to set them back if we
don't clean up the obsolete fields and
it's very easy to get into this
situation and this is the example of
Hindenburg because now we have to
restore and merge so it's very easy to
copy over the fields the second example
is the IRS object code and this is the
actual production code so here we are
actually upgrading the numbers up right
five becomes six six becomes 7 7 becomes
eight if you run this one code voice it
is going to be impossible to say what
was the 11 and what was 12 and if you
run it 12 times everything is going to
become 12 in the Android so we need to
ensure that this code does not run so
now recommendation is use average tax
don't trust the architects as well if
you can add additional safety checks
like here
the world customer should not be set to
true and they shouldn't have the reward
points right
you should error out because even the
object tax system can have the Box and
test it and the last thing is register
for the new companies and for the fresh
app installation by using this trigger
data fusion we have a execution context
API that was added for 14 and this is a
really cool functionality which is
giving you an overview in which state
your code is executing so to give you an
example if you have something that is
not safe to call during upgrade like
printing checks through the web service
if the update fails we're going to
rollback sequel changes we cannot call
the we cannot roll back the calls to the
outside web services basically that
thing is going to stay right and we can
incidentally call this one so what
should you do you can make it safe by
using this API you get the execution
context and if it is different in the
normal you can ask it is my app the one
that is triggering this and we should
definitely not be doing the purchase
post in our app right so I wanted to
fail the outlet here and I want to stop
and then we are going to move the
tenants back to the old version and stop
the data of it otherwise if anybody else
is doing this we should probably log so
we know that something bad happened and
we can diagnose and exit and this is the
way how you can defend calling the
sensitive code during the update so let
me just check the time because this
monitor turned off yes I have we have 15
minutes and this is the last thing so
basically you can follow the screw
through the update and these are three
architectures that you can have ended up
and if you would like to end up in the
cloud if you have ended up on the top
architecture there all of your changes
are in the extension you can easily
update if you're in the middle
architecture we will let you into the
sauce if you're a large vertical
solution and we already have any number
of large verticals that are running in
the cloud the reason for this is because
it is really hard to manage the
difference
oceans in with this architecture so we
wanted to keep the number of the cloud
solutions in the offering and if you
have ended on this one even though we
can technically support it and the cloud
can host it we will not allow anybody to
move into this cloud and currently we
are working on the functionality which
is going to help us and to enable you
guys to move like even in sauce to the
sunshine cloud where we can maintain
everybody and the life is going to be
easier for all of us if you would like
to take the step number three this is
the session you would like to visit
tomorrow these nice guys are going to
show you how you can migrate the
customers to the cloud and manage them
there and the last thing which are kept
the best for the last what about the
sauce the sauce up great right if you
have the extension if your extension is
working you don't have to do absolutely
nothing the nation apps for migration is
going to fix it if it is broken we
recommend it to have clcd you should
already know otherwise we'll call you
you should fix the issue you need to set
the dependencies and you can publish the
new extension when we get to these
dependencies but which you have
specified we are going to automatically
upgrade your PT or your app source
extension this is the docker builds a
link if you - so I'm gonna update that
blog post which is in the deck will and
update it information about how to get
to the different pills I think most of
it is still true even though it's 1/2
years old but I'm gonna update it so
that I'm absolutely sure that everything
in that one is correct
and yeah so you'll have the link in the
deck as well
yep and for the last things is like
compatible builds and version numbers
and this is important so we are going to
end the session with this one so the way
how we work in Microsoft is that we have
a branch which is called master and this
is where the latest code is coming and
this is the insider built that freddie
is shipping
so when it comes the time for the
release we are going to branch out the
release and the first six numbers from
zero to five they are going to be both
Sasson on-prem releases then when the 15
comes we branch out the new branch and
then the sauce moves to that one and the
14 is now being used for prom prom only
cumulative updates now the thing that is
extremely important to understand here
is if we do a bug-fix here let's say
that we did the bug fix in November
right we will port it to 15 and we'll
port it to 14 it's going to be released
when we branch for the minor right now
the thing which is going to happen is
that if you try to update from this one
here to this one here you're going to
undo all of the bug fixes and portal
features with it so the only way how you
can update is if the lines are going
this way so these lines are okay but if
the line is going in the different way
basically you're undoing the bug fixes
that it'll be clear for everybody that
yes so our recommendation install is
update the latest compatible Cu because
it's going to contain all the bug fixes
if you want to try this one out use 15.1
it contains the most bug fixes that we
have and check the numbers you cannot
upgrade something that was released in
November to the target build it was
released in October and we have talked
to the team that is publishing the CIO's
and now therefore every Co that we
release they're going to put the minimum
target number in DCU article so it's
going to be very visible what is the
minimal target number this you can
operate them please also note on that
part
let's sometimes we might release all of
the community of updates for the
different branches except for one
because might have a park that is
stopping us from releasing that so you
cannot always just take latest to latest
you need to make sure that it is the
latest compatible see you the
interesting thing here is that all of
these like red
cumulative updates they're usually
delayed to the
drum releases because it is sauce and it
takes more time to release so it's going
to be a few weeks delayed compared to
the unplanned release so we have created
a big update deck that you can go and
visit
so basically when I was doing the
presentation for directions had too many
slides I have cut them out and we
started compiling all of the stuff
related to upgrade and we have placed
this one as a get cut project so on this
github project I invited to go out check
it out right read it and you can ask
questions for clarifications or just
write something if it's wrong sure input
our documentation team is going to take
the deck at the end and it is going to
operate in the documentation so I highly
recommend to check this link here we
will also place some powershell
commandlets which are going to make the
object easier and with that one let's do
the summary so refactor away from any
breaking sequel changes before moving to
air it is we are currently working on
the functionality to move the fields
automatically you can move the tables
and we are looking into the numbering
and renaming automatically to make it
easier write the object code in a safe
way slowly and the docker is taught to
go if you would like to automate your
testing and speed up the process and
everything you saw today during this
demo will be on my blog for this block
comm where you will be able to find
information about like being able to run
the entire demo into end probably
sometime next week
alright with that I think we have like
10 minutes for questions and I think we
have t-shirts for the first few
questions asked so who wants to go first
we are there
in in the presentation you showed before
you were moving some fields on the
customer table and actually making a
hybrid can you see when you look in the
table in the sequence level that it
still has the original app ID next to
the customer table so and you actually
see that you have modified the base app
for this table no it's because when we
as a partner we where we are changing
customers are moving between partners
and if we come in as a new partner and
we look at that we will think this is a
standard 15 yes is there any way we can
see that it is it is a hybrid no because
a Mexican premiere allowed to use the
Microsoft Publisher name and you're
allowed to use the Microsoft go it force
us we are requiring a difference so for
sauce you need to change it okay so
you're allowed to use they do it and
that was actually why we you also said
we had to change the base app ID the app
ID wasn't changed when you opened
basically no Prem on premiere will not
be able to see this no so we have to be
very careful about this because we might
not know that yes yes Eric writes in his
book Erich Hoeber one of the MVPs for
Canada wrote a book and in that one is
be careful and have the source code for
the apps that you installed correct and
that is needed here you cannot come in
as and as a partner take over a customer
who don't have the source code but it's
the same as the existing code in C
alright sincerely would not be able to
see which fields have been added by
someone else and in regards to data
upgrade would you these days
suggest to go to the partner is V app
and wait until the upgrade for
customized tables is in place or go for
a hybrid and take the the data upgrade
depends on your timing and depends on
your scenario you can drop the by
afterwards we can discuss it in details
because for these questions the answer
is always it depends right because on
one side you will spend some time
refactoring and doing some additional
code in the other case you will wait
so it really depends but yeah basically
for these scenarios I think it would be
the best just disgusting I have a
question about prefix we should use for
table extensions and for fuse we for us
to use a three letter prefix but if
you're upgrading a customer we are
renaming the field because we don't have
the prefix at the old solution and so we
can could not upgrade it to the
extension because we are not allowed to
rename the field what should we do in
this situation the question is are you
on pram or are in some Ram on-premise
basically have the direct access to the
sequel right yeah but lately customer
wants to go to the cloud we need to
rename it you need to wait for this
functionality rights so you can either
do the workaround on Prem and rename it
by using this custom tuning okay none
supported ways wait for the
functionality for us to allow you to
rename and renumber right so these are
the two only options you can see you
know to add the fields and then do some
data upgrade to the correct copies the
value and if it's a new installation you
can also have all the new customers in a
correct way right and support the old
ones okay
okay yeah hi how will it deal with the
events that you've published yourself
and they have dependent upon oh that's a
good question so if you are having
events and events subscribers right I
would recommend that you marketers the
destination up for migration because if
it is a destination I'm up for migration
then the events listeners are going to
be turned on okay yes so they are going
to execute the during upgrades because
if you're following this other you know
like you're publishing never sinking
never than operating now that then the
events may not fall exactly
okay
I was slightly terrified when you showed
what I think you called a hybrid base up
or something along those lines in sequel
you refreshed it and every table had
changed its name where do we go from
from every table has changed his name
into every table is now back how would
the are normally called we say balada
GUI it on the end it's your future for
that so the question is can you remove
the go it from the table name right yeah
yeah I'll say okay path from you can't
because like once you have added the go
it right all of the 15 tables are going
to contain the go addendum yeah so they
will not be in any tables without the
good so the only tables that he have no
good are the ones that are coming from
the platform itself yeah so these are
these system tables that exist when you
refreshed every table with my base up
every table adequate so they don't seem
to be any future we we used Microsoft
base app ID meaning that once you revert
to the normal base app and actually move
your customized field into your
extension when the feature is ready then
the hybrid model will actually be future
safe right that was the reason for not
using the putting everything into a
customized because then our new table
would be post fixed with the base app ID
and you there's no good way to move that
into an extension afterwards yes this
was the reason why we took the new
tables into an extension right away and
left the fields there and the fields can
be moved into table exclusion afterwards
because if the only thing that you end
up after refactoring is added fields
through our tables you're going to be in
great shape
because then that table is going to keep
its own guiit right and the only thing
that we will introduce when the feature
is done is the new table with your two
fields and a new good right yeah and the
old table is just going to stay in place
so basically the best architecture you
can get is just leaving the
feels all waiting until the features
there so that you actually can get
everything into table extensions right
away and then they move for from 14 to
15 and a clean extension is by far the
cleanest solution you have other
questions or should we go and get a beer
it's a loaded question I know that you
should test database schema and you said
if it fails it would fail if table would
would have upgraded correctly right if
the table was not moved yeah so what
should we do then you need to check this
table because that means that the either
a name or the ID does not match okay
so basically you need to resolve it
either by fixing the AL definition or on
14 if you want to get rid of that table
you can sync with force right because
that track is actually comparing this
equal chain schema with the object
metadata and it's going to find the
extra tables and orphaned tables and you
need to basically see what happened
right did somebody wrote the wrong Yale
code or is it the table that got left
behind right you probably need to roll
back and start from scratch
yes some do go upgrade process right
it's not likely that you can resolve it
and continue yeah basically if you got
any issues on the upgrade right she
needs to restore back from backup start
from scratch okay you cannot touch the
upgrade process because it's not a smart
idea
other questions oh you see if we can do
that job yes I have a question so we
have a little customer which has all
fields in custom range and wants to go
to an extension how to do it without
remembering what would be the best
immigration customer where you have a
customization and you want to move them
to the cloud or as a pity but the custom
extension not as I see I didn't get that
so cd1
so you can have a custom extension yep a
cloud yeah a Pte personal service
extension where you have to be in
between fifty thousand hundred yes yeah
and if you have a if you have a
customization right now where where you
have used your your partner range you
have to renumber them in order to get
into a Pte range and move them down to
the Pte range that has to be between
fifty and a hundred thousand yes the
problem is that you know like he needs
to renumber on-prem right and renumber
inconceivably is a bit difficult CL is
really good that renaming right because
he all works with numbers
al works a bit differently l is quite
good with names and it ignores the
numbers as such so basically if you're
on premise you would either need to wait
for this feature that is going to do it
automatically or you would need to see
how you can work around your way from it
right you would either need to write
custom update code try to tweak the
object metadata and sequel with the
direct axis or simply wait for this
which
and if IDs match in the extension and in
CL yes so you cannot publish the
extension per class fields already
exists no I think you can you can I so
the question is if you have the same IDs
yes you need you need to give a
different name yes how different yes the
way how you could do it in CL as a to
step up grid is that you would introduce
a new name and a new name on CL and then
you can copy it on the extension right
when is thought but you would need to do
a multi-step update for that so I mean
in general unfortunately not because
we're blocked with this feature which
will which will help us to renumber and
rename yeah we don't have a good story
but time's up
thanks for listening so thanks a lot
