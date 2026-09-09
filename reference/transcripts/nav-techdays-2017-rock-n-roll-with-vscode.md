# NAV TechDays 2017: Rock ‘n Roll with VSCode

- **Source:** https://www.youtube.com/watch?v=ngEkLrmQZzA
- **Video ID:** ngEkLrmQZzA
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 99m15s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

good morning
okay
i i understand i mean it was
it is the second day of the convention
it is belgium there are beers and it is
in the morning i mean come on i
understand i'm eric wowted uh i'm a
partner of uh effective business
solutions uh belgium partner not too far
from here and i'm a partner at cloudy
ready cloud 30 software
and actually a proud colleague now of uh
mr mebuzzo
luke van dijk
who actually mailed me a few weeks ago
and specifically asked look eric please
next time do not
change my
title slide and i was quite offended
dude i never changed your title slide
never do that
topic of today
is
not al development it's basically
development with a certain tool called
vs code
i guess by now you know that it's quite
around the corner that we will be
doing development in this great tool but
this tool can do a lot more in
my opinion that has been uh showed until
today now a question who of you has
never worked with vs code and clap hands
no no just once
else is a lot of people that didn't work
with it so
again who never
never worked with vs code so
let me introduce you
this is vs code
nothing more than that
no obviously this is not vs code
this is a guitar would you be able to
play this guitar
of course you can there are strings in
that and you can play would it sound
good probably not really for this guitar
vs code to finish you probably need some
more stuff
and that is exactly what you can do with
vs code you can
change configure
and put together a tool set
around this great tool to fit your needs
how you want to play it how you want to
work with the tool and you can make it
exactly as you want um
and that's basically what we are going
to do a little bit today rock and roll
with that
tool so while this vs code
a lightweight tool uh vs is not visual
studio yes it is visual studio but more
like the family name visual studio
basically this is a lightweight tool why
visual studios definitely is not
multi-platform you can
do
[Music]
os development
or development on a mic os which you
might have seen yesterday i think in the
session
um
which
key strength of vs code is definitely
the extensibility
and
basically a lot of languages that it
support okay let's dive into that how
does it look like it's this it has a
menu
not really the visual studio menu that
we
have these zillion ribbons and buttons
well you have a simple menu you're not
confused
there is an activity bar to basically
easily
go to and and navigate to the different
parts of of visual studio code status
bar please do not underestimate the
power of the status bar
which is
quite good
a red status bar it indicates that
something is not good
basically
there is a text editor well feature
studio code is a text editor so luckily
we have most space there for uh edit our
text and there is the command palette
that's where your menu is not the entire
ribbon and you have to find and click
and use mouse and stuff like that no
there's a command palette you can use
very efficiently your keyboard to go
forever and execute whatever you want to
execute and you will see that hopefully
a little bit today as well so working
with vs code
means you put all these things together
and be as productive and efficient as at
all possible which means
first of all which i'm not going to show
but it will be very clear
during hopefully demos
you will work with files there is no
object designer
oh object design
you will have a directory which is
called workspace and everything in that
directory is your
project and basically your app that you
will be creating
you have the command palette you have
you can do
lots of configurations source control
integration debugger everything that you
expect from a development tool
and we'll start
with
source control integration
out of the box you have source control
integrations and you all know what that
is right
only a few people know what source
control integration is okay let me
explain you a little bit you need to
know
who changed what
when and why
who what when why
yeah
are you source controlling your cal at
the moment
who does not source control its
its developments at the moment
quite a few and that is normal because
in our c not normal this is not normal
this is development it should be source
controlled let's say
um but it's difficult
in
vs code is integrated so it's going to
be easy and you know what it is you need
to know who to blame so if
somebody
messes up you
can deal with that
yes there is an integrated
connection basically with git
you all know git git is like uh
basically built from an open source
platform and is now my the most used
source control management system there
is now there is a connection between vs
code and git only the connection it is
not integrated so um
yeah we'll go into that in a minute not
only git to support it there are some
other sem providers that is supported
that you can add by installing an
extension so if you're already on vsds
yes you can still use your
vsts now for this git support which we
will show a little bit today
it's basically just invoking git if you
have not installed git support
then yeah well there's nothing to invoke
so it's just that it's not that you
install vs code that you can just use
git no you need to install some more
which is basically with this url
download it installed it press next next
next next next next next next next next
next next quite a lot of nexts
next and then finish
um
then you need to configure it you need
to let know who you are you can fake it
a little bit i'm waldo i'm not adequate
in this case
so you can if you check in nobody knows
who you are um
but anyway you need to let you know and
there are the comments basically to
configure your user on your machine
and then you're good to go and from that
moment
git
can be connected the other way around vs
code when it runs a git command will
basically
um
able to yeah run that command
but still
in your workspace you need to enable git
it's not that you just create a
workspace that all of a sudden there is
git you need to initialize a git
response repository you might have seen
if you've done that there's a dot git
folder in your workspace which is hidden
true yeah it is hidden
that
usually means that uh your kit is being
initialized and yes you can basically
execute or execute all the git's
comments for your repository
the easy way to start with that if you
create a completely new
thing is
yeah if you are having a remote
repository remote repository is
basically git hub a good example of that
where you put your
source
in the cloud or whatever
the local repository is the one that you
have on your local development machine
the two needs to be synced and um that's
all part of uh of basically kit support
now to set it up is most easy thing is
just create a repository and github and
clone that back to your development
machine a less easy way to set it up is
create a local repository and sync it
create a remote and sync it up to github
that's a little bit more cumbersome so i
don't like that
so i usually just create a github and
clone back down
there are a few things here um which is
kit terminology like you have a
repository which is basically the
database of your source control
um if you have the remote which is the
key to part the cloud part where
everything is basically
synced
you have the clone
yet you can clone down into your own
machine and so on i'm not going to go
too deep into that because basically
there is a really good session about
that
at 1 30 uh of cern and jonas
who yeah is going to basically rock and
roll with source control management
let's clone
a repo so let's just assume
that we have some kind of github in the
cloud
from a strange guy and he's got a really
useful useless app that was ever been
created and you say well 36 commits yeah
that must be a really good app so
the only thing you need to do is copy
that url
open vs code
and
open the
command palette ctrl shift p we'll go
into the command palette in a minute
clone a repository yeah that's the
url and then i need to indicate some
kind of folder
i will take this folder
and now it's downloading the sources to
this folder
i open the repository done i'm
basically now i have created an offline
local
environment development environment for
this app and the remote is all basically
already connected so i can start syncing
up to github if i would like and are
able to do that
now this is an
al
workspace let's say this isn't an app
so i need to download some symbols let
me do that
and done
i'm ready to go
cool
now
you're developing on that and probably
more multiple people is developing on
that you might run into conflicts if you
both change the same object and you sync
it up
probably
maybe there are conflicts and also that
is integrated you can solve the conflict
kind of like looks like this
and when
yeah solved and
then yeah you can basically just
continue
uh one
remark on the git ignore this is a file
where you can add basically files
that you do not want to add into your
repository and i think it makes sense
for al development
to not include the app files
you can generate them by compiling so
you don't need to sync it up to your kit
well
yes it makes sense and then again for
dependent extensions you might want to
have that still in your repository so do
what you want there is a dot kit ignore
and
you can manage that like that
there is a common palette so now we have
something to develop
let's develop and let's start a little
bit with the command palette and i've
got here
um
an md file which describes basically
what i want to show
let me show that in a nicer way
so very easily set the command palette
ctrl shift p let's not spend too much
time on that contra 6p is the one
shortcut that you will use
a lot
i have heard that f1 works as well for
but for some reason i
always use ctrl shift p
and then you can start typing like
change language mode and look at that i
i type just four characters and it finds
that still
a while the characters are not like
attached to each other so there is a
really neat and fast way to search for
this and this does not only work uh in
in common palette it also works in
intellisense and all that and all that
so that is really nice now these are is
basically the common palette because
there is this kind of arrow oh what is
that a bracket
what is it i don't know what that is
greater than sight
that makes it the entire command being
searchable for um for comments to
actually execute something to give it
a job like merge or
push or sync or whatever
if i remove that bracket i've got
something else so basically i uh i can
search for files i can search for
symbols yeah
so that's basically the control p if i
press ctrl p
there is no bracket if i if i put the
bracket there manually i'm back in the
command palette yeah basically there's
just one way for you to search for
different things if you put that kind of
bracket you can search for that
those comments if you remove that and
you place a question mark you have an
idea on what you can search for as well
and what i really like for instance is
that i can search for symbols
if i press a hashtag
hashtag and then some kind of symbol
like
a table
and it's going to search my workspace
for a symbol
that
includes the letters that i just have
given in
and i can easily navigate to some kind
of code unit in this case just some
notification it opens the file i can
start
developing
that in my opinion is really cool and i
see a lot of you not giving you that
actually
you can search the files as well you see
i've got quite some files in my
workspace this is my workspace right
that is one folder and quite some files
and so false and stuff like that
you can search for any kind of file by
just removing all brackets and it starts
looking for files
so it's really easy it will look for
files also in subdirectories right so
looking it up or browsing
through your workspace it's really easy
using
this command palette
next configuration i can configure
the bejesus out of vs code
about all
little detail
you can configure
and let me go
into that
configuration and i've got a cheat sheet
for that as well
and let me show you
that a nicer way
so um first of all you have
configuration files now every
configuration is done in json files so
it's not like if you just click here on
the menu you get a nicely
[Music]
form like thomas would say
with check boxes
no
you basically get a json file so if i
open this if i actually click it
then you get a json file that you can
edit
the left part
are your default settings
the right part are the actual settings
that you have changed yeah so the
default settings obviously i cannot
change but this is i can
not edit this but i can search this
basically i can see here all the
settings that i would be able to change
on the right part are the ones that i
actually have changed so i have two
whatever that is we'll go into that in
52 minutes and 20 seconds
um
and i have here so a zoom level cool
that's that's nice so
there are shortcuts for zoom to control
plus for instance and that actually
works and if you see now on the zoom
level here
basically zooming means updating the
settings file
saving it
and it is being applied on
let's not zoom that much because the
screen is quite good
okay you see that i have some other
settings here which is not really that
important and i can obviously also
change the theme here let's not do that
one setting that i tend to to do
is uh what i
don't really like at this moment but
that's a personal thing
it's these this is an al file
and you see all these references
but this is one reference these has two
references
uh this is what is called the code lens
um personally this is a personal opinion
i'm not saying that you should do that
but personally i never look at that if i
want to see the references i can
look at the references with the shortcut
so we can easily
change that
i basically can choose like okay
i do not want the code lens and now you
see here that i make typos
that also the settings files and
basically all settings and json or json
sorry has got intellisense as well it is
a language and it is its development
environment so yes you have intellisense
into your settings
as well so i want to do this editor code
lens and i want to set that to files
i save that i go back into my al file
and my references are gone
one disadvantage is i might like this
for powershell so now i basically switch
it off for all my languages
well let's let's not do that you can
have language specific settings as well
and you can do that by
look at that a snippet
snippet and json files i have a language
specific
setting for the al language in this case
and i can basically just copy
or move this setting to the language
specific setting
and now i have
set it up for me
as a user
for this language i will not have code
lens
yeah
i like it
not much
it will get more complete
okay you have seen on the top right you
see user settings um i can have
workspace settings as well i don't have
any at the moment now these works
workspace settings are as it says
settings specifically for this workspace
like for this project i don't want a
debugger
it's a challenge
something like that it's going to save
that somewhere and by just
selecting this it basically created here
at settings.json within my
workspace within the dot vs code folder
of my workspace that's indicating okay
this is the specific settings file for
only this project while the user
settings they were
saved
under
my profile update a roaming profile
so it will live with me whatever i live
on this network basically
okay
so far for settings
we have shortcuts as well and we can
change shortcuts one of the
remarks i've heard
is well i hate the shortcuts of vs code
well
that's your right but you can change
them why not i'm so used to having like
f4 for deleting a line f3 for inserting
a line well
you can search for the insert line
insert line above you can press the
the pencil
you can change it to f3
or for delete line
you can change it to f4
done
and now you can simply use f3
and f4
and make it
your preferred
keyboard shortcuts you can completely
mimic cal if you really
really like that
okay what can you do more uh that's
snippeting
um
you can create your own snippets please
do that you need to do that it will
speed up your development a lot
now on the same uh place here i can go
to the user snippets and of course i
have language dependent snippets it
doesn't make sense and i can uh put an
um
what is it a json snippet in l
development and a javascript snippet in
in powershell although that makes sense
everything makes sense with powershell
so let's just assume
i want to have some snippets my own
snippets for al development and then it
creates basically an
al.json file almost almost a certain
place if you can find it out as well and
that's again on the roaming profile
it creates a language name in this case
l dot json which are your snip snippets
now just assume and let me open
this beautiful
al
file just assume
you don't like the
default tables that snippet that comes
with al
and there are a few reasons not to like
that
maybe you don't like
the fact that it creates triggers that
you don't use
and hopefully
you don't like it because of this global
variable that is placed there in every
single
snippet which i really don't like
personally so let's let's let's try to
change that now
the difficult way is to start building
this into a snippet
but there is an easier way you can
basically
find out where microsoft snippets are
you just go
to your user profile
and there was a vs code folder there's
an extensions folder there's a microsoft
al folder and in that there is a snippet
folder
those are the snippets that comes with
the product
with the extension of al development
you can change them don't
because next time you update this
extension you lose your snippets do not
do that
just open the table one
copy it
to your own al jason one
and i will put it here at the end and
you can see that i have been trying out
stuff
okay
i will put it in the beginning
and then you can start to change it i
don't like these triggers and i
definitely don't like i will i want that
bracket still but i don't like this
global variable done
i will call it something different
and
done i saved that and now i should be
able to
delete this and
[Music]
use my snippet which is
a much cleaner one
you can very easily it's a matter of
minutes to create your own snippets if
you see that you're always
changing the the the same things
on the default snippers create your own
snippets it will speed up development
and there is a lot you can do with
snippets um i don't know if you noticed
but let me just do this again
i can tap
between different parts of the snippets
these are placeholders and yeah there
are some syntax on that but it's very
easy to learn you see here place holder
number one placeholder number two i give
it a default and basically that makes
you tap
over the different ones
more than
you can do this as well uh if i i don't
know
yeah once you are out of the snip of the
top sequence there is no way to get back
into top sequence
either
re-insert your snippet so tap and a name
and you see here that i'm changing two
things at the same time so that is
possible as well
by simply naming that
see the same way
same placeholder same number okay
you can do more i've got the code unit
snippet here and i if i do that
you see that it inserts automatically my
file name
so if you have a decent file name
convention which is that i definitely
did not apply
you would be able to speed up a little
bit like that as well i just didn't
manage to exclude the extension just yet
maybe there is a way i don't know
last but not least which i really like
let me put that code unit back
i might have a repeat
the repeat loop and you see here this is
maybe my cust and again the same
placeholders and there is a choice so
you can include choices
so in this case i obviously definitely
want to do this
no no
okay it's good
you're still awake
okay so yeah you can do a lot with
snippets and apparently i have been
doing a little bit too much with
snippets so let me
remove
this weirdo so i can
recreate that weirdo again in a few
demos
ok
like that
those are the most commonly uh things
that you can configure on vs code so you
have a settings of json which basically
is either your workspace or your user
settings placed in a certain way you can
configure whatever behavior you have in
vs code on top of that you have the
keyboards you have the language uh the
keyboard shortcuts sorry uh the language
snippets and that's how you can make um
it
like it is the snippets uh it's not just
text it's more than that you can have
these placeholders tab sequence you have
multiple placeholders which we have a
multi-cursor kind of thing that you can
edit multiple things at the same time
you have these variables i've shown you
the file name but you also have a
selection variable so just imagine that
you select a part of a word and
then you want to activate a snippet well
with this word you can work within your
snippet as well
some editing hacks so while you are
using
vs code
you might want to be a little bit uh
you might want to be a little bit
efficient
so
uh here are a few shortcuts i'm not
going to show them all uh just a few
shortcuts that
can make your life a little bit easier
and there are a few beautiful ones like
if you have an md md file like this i
basically like to see it side by side if
i edit it um
this way and this is how you edit it i
might want to see how it looks like and
there was the ctrl k
ctrl k is
expects always another letter to be
pressed you see now the status bar like
hey ctrl k was pressed i'm waiting for
you for another
key
if i press v it doesn't do anything okay
let me try
again that was just a v
and now i've i get my
md file side by side this is much nicer
to see
whatever i'm i'm doing now that is not
that important but i wanted to just have
that side by side so uh let me go into
this code unit here
you probably know the f12 to drill into
definition this is normal we even had
that with cal but in cl when we did that
we couldn't go back
right
yeah
i can tell you you couldn't go back
to go back and especially you couldn't
go back to a previous object and stuff
like that now we have the alt and the
arrows
and you can go and navigate well however
you want so i can go back to another
object and i can't go back and back and
back and back and back so with the alt
and the arrows left and right
this is really beautiful so you can
investigate the code go in go in and go
to definition and back and back and back
them back and go back
and yeah basically go back
so i want to go back here what you can
do here as well is yeah peak instead of
already
go into that and some more
let's not go too deep into that with the
alt shift here
and
up you copy
stuff
and i luckily had my f4
so i can definitely
just remove that again
the ctrl t is also a really nice one uh
but what i really want to show you is
this uh selection of lines ctrl i if i'm
not mistaken selects a complete line but
if you do that multiple times you have
multiple lines that you're selecting now
in this case i'm selecting an
integration event uh you know that in
integration event first you have the
attribute and then you need to define
the procedure a procedure needs to have
the begin and the end and by default
looks like that you you have basically
five lines of code
which actually is just one definition of
an integration event or a business event
now i cannot put i think the
uh the attribute there but if i select
these and
press ctrl shift p i can join the lines
easily and now i still have the same it
still compiles but at least now i have a
decent definition of an integration
event
if i can do that on everything
let's not do that
yeah fiaco likes it obviously
um okay multi-selection thing um
it's really nice uh you don't have to
stick with only one cursor you have
multiple cursors and you can just place
them by pressing the alt key and start
clicking so if you want to really be
crazy you can just uh play press a
number of cursors here
and start
typing at the same time this is
obviously not useful but if i press my
cursors here i might want to add a
caption
which is yeah empty at this at this
point and and go from there
yeah
i hope you like that i mean this is very
good just okay
imagine that you are uh adding fields
and you have like 20 fields and you need
to add oh i forgot captions or oh i
forgot the application area
easy just select all these places
once you add the application area you
don't have to do it once and i copied it
over and messing up your formatting you
know this is really really nice
and changing for instance your symbol as
well i've got a symbol here editing
hacks
which is a function i can have a peak
well this is a
function that is being created here
apparently
and i want to rename that function now
here i call the function and i basically
have defined it in some other place in
another object with the simple f2 i have
a rename symbol and i can change it like
i'm going to call it editing hacks 2. if
i now peek you will see that i still
have three references all the occasions
of this one
symbol has been changed on all
uh all the things
and all the files so that is really
also i use that a lot naming is really
important and the tool gives you a
really
good way to rename if naming is
important rename is probably also very
important now be sure that
the f2 is definitely something
completely different than the ctrl f2
which is basically just going to select
all instances of this text within your
file
you can do that
let me just
try something out
this and we called here waldo
but now if i see the references i do not
have anything
so that is not good right uh you need to
have this um
other one
this is also a really nice one just
assume that i want to rename cust only
in the in this procedure i do not want
to rename it or not just maybe this this
code unit name here and not in the
entire
file then i can use ctrl d which selects
the next instance and i can keep
pressing ctrl d until i've got all of
them then i can change it
and obviously this change is accepted
because i basically changed the
variable and and how i call it so that
is really
really nice
i find at least
okay let me close this all down
and
let's see if we can do more
like
debugging
i was told yesterday that uh debugging
was showed so i'm not going to show that
too deep but um
there was one thing that uh i was told i
was not at that session for my apologize
but um
there was one thing that was not shown
that that is actually conditional
formatting oh it's conditional debugging
so what you can do here you can set a
breakpoint now this code unit is
something that you should never do
basically
it's
subscribing to the on after login it
will basically loop 100 silly loops
and assign the silly variable
100 times when you log in it's just to
slow down my demos i would be
completely before time so
what you can do here is you can put a
breakpoint
and you can make it conditional
so edit breakpoint i only want to be
here if my value equals 60.
instead of 100 times into this
loop it's only going to do
[Music]
yeah it's not going to do that when you
press ctrl f5
which i
now pressed
that is out of
yeah i always press ctrl f5 just to
avoid the debugger not that i want to
avoid it i just want to consciously use
it
okay
so let me see if it's going to stop
there
it's blinking here so probably did
something and you see the value is 60.
you can obviously add that to the watch
and the nice thing is there is a
complete skull stack even into a seaside
cal
good
that was the debugger must have been the
shortest demo of a debugger of all time
let's go into some interesting
extensions as i said we did the
configuration part of vs code but there
is a lot more that we can do we can
extend vs code and that's basically
yeah um
adding more functionality to be more
productive
one of the extensions that we all know
is the al extension the language
extension
of microsoft for
us supporting aol
but there are other interesting
extensions now what is an extension
some short theory
provides uh vs code for uh
more functionality
and runs as separate services so it does
not really interfere with each other on
top of note js it can include languages
like microsoft al but also debuggers uh
themes snippets colorizers
icon packs
and functionality many more but also
functionality now within vs code
obviously you can search for extensions
you can add them you can delete them you
can disable them
there is a complete management of
extensions
you can
download them from the marketplace or
you can just get a physics file from
someone and install that manually good
that was a theory go let's go into
practice
um
what i think
are
interesting
um
extensions now first of all snippets i
hope you all like snippets i like
snippets i think they rock you can
really
use snippets for being really productive
and there is a snippet creator i
basically did it
completely the slow way
again probably for time fling reasons um
but just let me show you another one
there is
let's just say did you ever create a
wizard
in ale
wow
this is
about the minimum wizard that you can
get and let me just show you
that it's
yeah some code let's say
there is a lot of that you need to take
care of you need like
the visibility of the groups you need
this media repository stuff you need to
have the banners on top you need your
buttons on the bottom right there's a
lot
to take into account now what you would
do is
let's
just say we want to turn this into a
snippet
and what if there was some kind of smart
guy
that had created an extension
and i can show you the extension
it is
the snippet creator over here
which you can basically use it adds
there is a contribution it adds a create
snippet comment
and what you can do is you can close
your file and
completely
be slow now oh come on
so this one ctrl shift p i want to have
my comment
command palette i want to create a
snippet
and there it goes i can now
ask or given the language and give it a
name waldo snippet
i can give the shortcut t waldo
snippet
whatever and a description model
description
and there you go
now let's have a look
at our snippets and it should have
created here
uh
the waldo snippet which we are able to
use if i remove this one
uh
here it is and it adds my snippet
this is really cool
in my opinion you need to change it a
little bit uh because best practice is
is that you uh yeah press
yeah this is one indent so you need to
like use the top to indent that so you
need to change that you can then again
easily change that because there's also
a shortcut alt shift
where you can block comment like if you
want to
have a
plot comment i say block selection yeah
so i can just change all this in
in backslash t and i would be able to
change this in
completely the wrong
shortcut
this one and backslash d and so on so
you can
quite easily turn this into a decent
snippet
all right
it's the bet creator
feature is create a snippet
there is a github
connection as well so
the
um
this is the one so there's a github
extension which basically connects to
your github quite like it
don't really use it in practice at this
moment because i just found out
but what you have is a lot of browse
possible possibilities
like i want to have my issues and browse
my open issues and it will look at your
remote it will should look at my remote
okay okay i have my f1 issue and now i
can open that issue and it will open the
browser but it knows the connection
right
your remote
is basically the github account
and that is where it is connecting to
so i have one issue here
that i just closed no i didn't close
that
uh all files are in root yeah and
that doesn't really make sense that's
that's absolutely true
that doesn't make sense i might want to
change that later on
um
okay
there's a lot more on the github i'm not
going to show you all you can create
merge and all that for pull requests
there was a complete pull request
management basically it opens the
browser on number occasions
the thing is it it does it quite nice i
just don't know why i want to do that
like if i have here
my cursor and i can open the
github open
open the file
and then it opens that file on github
but yeah but i i see it already why
would i want to open that on github
um which is not opening on github at the
moment okay yeah let's not go too deep
into that
we can't go deep into that and didn't
open
okay kit history that is a really nice
one and that is one that i i do use and
that is
um
yeah getting
whatever history that you have been
checking in
and one thing that i want to show you on
that
is the git log
that's basically a representation of all
your check-ins in some kind of graphical
way and you can see like that i've been
doing some changes on
today on last hour
last second change on some kind of files
uh and then you can obviously browse the
files or compare them to a certain
version or uh at the previous version so
you can see what i have been changing a
really nice way to
have an overview of what happened
basically within your workspace
in and and also who did that
it also adds here to commits
to the explorer where you have yeah the
same overview basically and the files
that you have changed
really nice
for
yeah your source control integration as
an addition at least and then
we have a really cool uh that we have
been using into practice quite a lot and
that is the rest client
and this client
adds the possibility
to easily call rest services
so i've got some examples here
where i have added
let me just show you the code that i
created
which is a code unit
and i want to publish this as a web
server so i have here uh the xml if i
include that into my al part it will
automatically create a tenant-based web
service based on that code unit
so there are three methods i want to be
able to test these methods that's the
idea and i can do that with this new
extension
the next one here is i have a query same
this query i have here again in xml that
automatically will
create that as a web service when i
publish this extension
and i've got this xml port which i'm
using in my code unit here
to yeah
call that as a web service
now how do i test that i have been
publishing this uh already i can do that
again let's let's hope it works if it
doesn't work you can all go home now
well it does so here it is
and my web servers just trust me on that
are published
now i have these rest files here as well
it's not al files it's http files
the http extension makes sure that the
rest
client extension understands whatever is
in that file at the moment
so um some examples i've got here azure
functions
the same measure function that vehicle
yes yesterday created
to
show you hello world or these kind of
things and you see how
that can be done i simply this is just a
text file i'll simply put get and then
the string or or the url
and that's it and on top of that i can
use
variables so i in this way in the rest
client i can use variables
the thing is it all the
services that i have here will use the
same variables it will read the entire
file
and these variables will be used so if
you have the same variable name five
times the last one is the value of the
variable that's something you need need
to get used to in the beginning
from the moment
so if i just remove this for instance
you will see the button sent request is
gone i can just say get and so on and
you see the send request appears
the rest client understands this text
file it's
compiling that basically and then from
the moment it thinks that it can call
that
url and it will do that then so
i can click that
and you see
it comes back with the web servers that
in this case vehicle has created as an
azure function
i call the same thing with a different
variable name and this is how you do
variables within the rest client
and it comes back with hello and so on
and obviously you can do this on nav web
services as well so i've got a few
examples here
for our page web service a default page
web service there is the job list
somewhere so
i just want to test that and here you
can see that that it doesn't work
or it does
so a soap request the old data request
yeah it took too long
let me
check that again
yes five six seconds for the uh
or data
request and obviously
version four as well which should give
me some kind of json here it is
that's all cool but the the thing that
you probably uh mostly do is calling a
web service
that is based on an xml port i hope you
do that at least
let me try to see where i have put that
here
so this is still my query i'm going to
skip that um trust me it works you have
heard that a few times yesterday
um there are some soap
some soapy quest that i would like to
show you so you you remember that uh i
needed to call a method in a code unit
and then i might wan i want to get back
uh the results of a certain xml port
well there i need to provide the header
for the soap
request
and that is basically how you do that so
it's a little bit more typing uh this is
all that that you need to foresee the
authentication how it's uh basically all
set up
uh i did put in some variables here like
for the method one
to open my
to change my soap action and so on
like that
that's the first time everyone anyone
asked me to zoom on after days actually
the screen is not big enough look for
next year
um
yeah there's a little bit more typing
but
the result is that i cannot push
anything anymore uh what happened
yeah here it is
so here you have an error
cool let's uh change
oh no no it is not an error i know what
happened i
raise an error within my function
that's what you do this right
um the last one is obviously the most
important one where i call the
xml port and here you can simply see
the result of your
of your call
really nice addition the nice thing is
that i can just make this part of my
of my extension and basically the
testing of the web server is part
of the extension as well
that is nice
all right so
you can do a lot with the rest client
sql server is the same error sql server
extension for vs code so i can basically
call sql server stuff
for instance
have you ever noticed that your data
disappeared if you didn't let me show
you
for the sql server there is first you
need to connect to a sql server so let's
first connect
and then i already set up some
connection profiles if you don't have
any
then you can set it up yourself then it
will not have any list here basically
and it will guide you through a wizard
to set it up so on a dev server i want
to connect and i want to
execute this sql statement
which is basically going to
show me the content of whatever or
execute the sql that i just do here
and that is actually
looking up
my companion tables of my extension
so
it appears that i have one companion
table for the customer for this
extension which is
the
app id of my extension
next
a union i also want to show all the
tables that i actually created which is
not a companion table but a normal table
as you can see here just some table
i can see if there is
some data in it
and there appears to be some data in it
and yeah
not really here
did i miss clicking i misclipped
so there's not no data in there let me
quickly add some data
i will run the web client look at that
how easy that is
we will show that in a minute
all right
i will add quickly some
data
and now
our sql statement should actually show
that
oh no that's that's wrong although
it is execute current statement
and there is my data some
um
i'm just going to publish my extension
control f5 let's just assume we did
we added the code unit whatever
i'm not interested in the client at this
moment i'm interested in the data so let
me execute
this one again
data gone
and
thanks to this sql you can easily find
out you have a problem
next
we will see how we can solve that as
well uh there are snippets uh in this
yeah it starts with sql and there are
the snippets like if you really want to
mess anything up drop the database and
so on
there's intellisense as well which i
really like
select star from and look at this
all my tables of my
nav database which is in docker and all
that so it's nice uh to have that and to
have a quick overview or whatever to
compile something that you might want to
test against
you can export as well so if i for
instance select star select
star from
customer
like that this table i execute this one
i get my customer table
and i want i might want to export that
as either csv of course not we are
totally into json
customers
i can save that and here you go i've got
a customer.json file and you can do
stuff with that i honestly don't know
what you want to do with that but
you can do something with that
right
sql
another one
create guit
you need that
why do you need that
you think
in al development
why would i ever create a good
app id yeah uh you can generate an uh a
manifest from uh from a comment
so let's not generate our own app ids
but when using
[Music]
notifications
then you need
createkubit like this this is a simple
notification but you should
[Music]
include
a good as an id of the notification
now what i did i
created a simple uh or i installed a
simple create guide where is it create
kubit extension and i can simply
be here ctrl shift p
create good it will
put it on the key on the clipboard i
paste it done you don't need some kind
of website to generate to do it and
manually
copy over the guide so what does this
extension do well
it creates a good
on top of that
um did you hear something about docker
these conventions
so some people yeah there is docker are
you familiar with docker
so you all have been creating your
docker images and
and using docker
somewhat less i'm not familiar with
docker and docker for me is something
completely new and at this point
docker
more looks like this for me
so it does help me when i go
and in search for some docker extensions
and there are two docker extensions
there is one docker extensions
that helps you create and do whatever
you want to do with scripting docker
images and stuff like that again
i don't know
on the other hand there was docker
explorer and that does help me so it
puts these things here where i can see
okay which images do i have uh which i
can play with here
locally which containers have i set up
and so on
so i have here a separate container
thing so apparently i've set up two
containers with probably the same image
and yeah i can do stuff from here
i can at least find out what i can do
with docker here like
having these statistics let's see
how
this docker thing is doing uh for me at
the moment and so on i can restart i can
remove
good one
i can
start stop and all these these kind of
things so that is
uh
nice um
so really if you are not familiar with
docker just install them in vs code and
manage it from there it's it is a really
easy thing uh so i said uh you have
either the docker extension and or you
also have the docker explorer which
i use most to just manage and restart
and delete especially delete
my docker thing if you want to know more
on the docker next session is completely
about uh docker it's about uh it's the
three guys that
made docker a reality for us you really
need to thank them
because this is
cool
although sometimes it still looks like
this
okay
yeah i cannot do i cannot do a station
without powershell so
and luckily um we have a powershell
extension within vs code and i tell you
now this is
let me just take no chances and
just delete this customer.json file
because i don't i don't know how big
that is and how what it's going to do
for
my further demos
powershell um we are very lucky that vs
code or actually microsoft is building a
powershell extension for vs code as well
that makes vs code so much more powerful
and this powershell extension gets
updated like every week
there is
unbelievable how much functionality has
been added now you have seen here
already i've got the console of
powershell just built within
my
what in my vs code and yeah what i would
use it for i think it's quite easy i
obviously used it for setting up my
docker stuff
and that might be part of your solution
right so having just a powershell script
to set up your two containers which you
might need for either dev or test
is just
it's just easy
the fact that you have installed the
extension within vs code makes it you
can also run it i'm not going to run
this one because it will remove and set
up my containers again but yeah this is
just part of my extension
which um
is really nice a few things i would like
to show you especially this the first
two lines here uh you already have some
uh settings within your al extension
well you can read them from powershell
you can easily rechasing files from
powershell and it turns the json file
into sorry an object
and i can very easily address
the different parts within either the
app.json or in the lounge that jason and
i
think
i use them in some occasions it's
probably in
in a different uh i think here yeah here
so i i want to i need the app.json name
for
my script in this case to work how i
structure this usually is that i have
one settings
script where i load my variables and
then a few other scripts
where i use my variables
so this is the one that i usually change
and um
this
is just a matter of of
of executing it now remember when we
republished we lost our data
that is not nice
so
let's see how we can overcome that so i
will load my settings here so i've got
my variables now in place and i just
close something that i didn't want to
close
i should have had already installed our
extension but if i didn't let's test it
again
it might end up in an error
you see that this is one script which is
going to publish an extension on a test
environment remember i have two
containers
one that i use for development purposes
this is the one that is in
set up in my lounge.json that means this
is the one that i publish my extension
to
from the development environment
i also have a testing environment and
that's the one i might want to keep my
data from so it successfully uh
executed let me see
and i have a script here to check my
data as well
let me just check if there is any data
and there is some data the people that
were sitting next to me
at
the moment i was actually entering this
data so okay let me just now create a
completely new extension i want to
upgrade my test environment and install
a new extension the way you do that
is you might want to update your version
of your
app json
then
if i would now build this extension and
publish it to the dev server i know
already i lost my data i just want to
keep my data
so let us try to build a new extension
ctrl shift b
and it should
yeah there is my new version of the
extension uh i can turn back to my
powershell and in my powershell i've got
an upgrade enough on tests which is
basically going to take care of my
container stuff
i'm using the enough container helper
here
uninstall whatever is there publish sync
and start nav container data upgrade
so
i select everything i press f8 i have an
error and hopefully okay that is not a
good error okay yeah did this uh call i
having the wrong
number let's just delete this one
and let's try that again
oh that is not gonna work
yeah it should take that file it's not
taking that file
build one more time
execute the settings then one more time
it should take the last or the only
version of the app file
which is this part last app file
let me see
what that is
this number three that's not good man
i did save the file but this is not
working
well let's not go into it trust me it
works
trust me it did work it doesn't work
obviously
okay you can do a lot with powershell
you know that i'm just showing you a few
things that don't work but there you can
do things that do work
and as i already have shown you there is
a lot of different types of file now
your extension is probably in al
it contains a lot of al files but that
doesn't need to be the only files that
there is in my extension there are quite
a lot of other files i've got like these
markup
markdown
files to describe whatever demo i wanted
to do i've got json files i've got this
http files got powershell files i've got
the sql files
and still
i can create a package file and still
let's hope that works
i can
publish that
yeah
so it can just be embedded into your
complete
extension
now there are some extensions though
specifically for the a language um like
d a l formatter
really nice one
where you can yeah format the al
language so just suppose there is
someone in your company but definitely
or not you that creates it code like
that let's say like come on this is not
readable well a
simple alt shift
f
turns it in diesel format
i can imagine that at a certain point
microsoft will include this in their own
extension but
at this point there is some smart guy
called erasmus
was that right pronounced or was is the
guy here
and he is
doing that that's a really nice one
another one
is
basically the a.l lint
you all know mark brummel he has been
putting some time into
yeah
watching over our code let's say and i
must say mark is not really happy with
me because i have been
apparently doing a very bad job
let me show you this
he says that i have a lot of problems
like hey you have unused variable here
and an unused variable there and there
is some dirty code unit here with
variable that is not and so on
the green lines here that's basically
his contribution to my code so you can
easily fix your code that is uh you go
to the alint
which i completely don't see it and you
uninstall that extension and your call
and your code is fixed
obviously not
it just gives you a nice overview of hey
you have a variable here or you have
used like if i would use reg here it
would call it hey you have used
hungarian notation that is not good
okay
on top of that it introduces
what he calls refactor what i call turn
into function
so if i
call this refactor he is going to put
these three lines
here on the bottom and put that into a
function
luckily we have this rasmus guy that
formats my code and there we go
everything is okay again
so that is the two functions that we
have with the al lint which is basically
a watching over our code a good
contribution is still in development um
but you can see people are already
adding um al extensions like i have been
doing actually as well um i have
created a crs al language extension i
this is a very broad name because i
didn't really know what i'm i was
what i wanted to do
basically i won't just try out
typescript and
it turned out that now i'm doing like
installing my modules
yeah why not um
but the other ones are quite useful like
i tend to use them
uh which is ctrl shift p with the crs
thing you find out which which comments
you have
and there is a runting
where you can run any kind of uh object
in a certain client even windows client
if you are not using docker at least
um but here just use for uh in before
the build
for for example the tablet client you
can select the types that is supported
by the topless kind to uh to run the
page 50 100
and it's going to open that exact page
it's nice one uh which i tend to use
quite a lot else you always need to
change the lounge
yeah that is a little bit more
cumbersome what i also have included
which
should work let me fix this
you see here this is all on
completely messed up this is not the way
how you should call your uh files
you need to include in my opinion the
object type the object name and also the
object id to have some kind of clear
overview of which object numbers i have
used
and for that
there is this reorganize all files
which
ask for confirmation and it's going to
put that in the objects
folder and code unit and it basically
put all the files in a structured way
called it all the same not all the same
but at least
like it should
and now you have kind of like an
overview like oh i forgot here on object
number at least that is that is a start
um
and that is
my extension basically now you can
contribute to these extensions please do
i know that erasmus mark and i are very
keen to learn what you think of it what
does not work what we should improve
and you can actually also do that on the
rest client and all these kinds of
things and let me quickly show you how
you can do that just go to your
extension that you're using and you say
mark this doesn't work just click on his
extension click here you will go to the
marketplace and then there usually there
is
some kind of here open issues you can
click to this then again usually is a
github and you can create an issue there
please do that i mean
it just makes our uh development live
for the entire community
better
or
you can create your own extension
did any one of you ever create your own
extension for vs code not for al
for vs code you did you do
the creator of the al uh extensions is
here
and indeed created an uh an extension
well uh you can do that
it's just a matter of uh yeah getting
your way through either javascript
uh
for vehicle probably that is not a
problem for me that's a big problem and
luckily there is also a way to do this
with typescript
um which is yeah what i think a little
bit easier at least for me
um don't the
how do you get started you install
node.js you need this runtime to be able
to either yeah get the packages that you
need to create your extension but also
to
debug and all that
you need yuma human is a code generator
and for yeoman
there is a specific code generated for
vs code extensions so basically you
start off with some generated um
hello world kind of thing that you can
start and change
um
into your own extension
so this is how it looks like so let's
try this out
and i really mean that let's just try
this out um
i will create a new folder i don't know
why i would do that just let me just
yeah i need to be in some kind of
folder let me let me try not the
downloads come on
i need a comment line
documents that's a good one
and the first thing you do if you
installed all that so node.js and uh yo
and you and yeoman that's it uh and the
code generator you can
call your code
yo code
and this is
going to start the oman and
it wants to generate basically code for
me
to start creating a vs code extension
and he asked me okay what do you want to
do you want to create a typescript code
uh veco would say of course not that's
not cool javascript is cool
um i don't create javascript extension
and you can do some other things here as
well so i will create a typescript
extension most of it most of the
extensions are created in typescript
basically typescript compiles to
javascript and that's then what vehicle
does what's the name of your extension i
will call it google i want to google
what's your identifier yeah let's call
it google our description of your sketch
maybe i will google
and what was the publisher that's waldo
do you want to use a git of course not i
want don't want to use git who wants to
use git anyway come on
and now it's preparing my
extension basically generating
the code
this will not
take too
long there it is
so i should have a google map now there
it is and i can open code
and this is where we
start
our very first extension is done
it is a generator it's generated quite a
lot so all these files uh node modules
which is basically libraries that i can
use in inside my development
and all that so as i said i want to
google
and just so i i want to define that this
extension will be used for
google
and
i start off with opening the
package.json this package.json is your
manifest
you see this manifesting is not an al
thing it's quite you
being used in in multiple environments
so here this manifest i need to define
that i will contribute to not only a
hello world
thing
but i will contribute some other
comments as well
so the first comment and i've been using
snippets here to uh
not to type too much
the first comment i want to add is a
search current word on google the idea
is i am in my
development environment
i
select or i'm on a word i don't know
what that word is i want to google that
word
yeah
so that now i defined that but obviously
i didn't write any code i just defined
to the manifest height this is something
that i will contribute
so that means i need to write code there
is something
called in the source of uh directory
there is a file called extension.ts this
is where your rock and roll is going on
right this is where you will create your
code and you can see there is always an
activate a function this is the function
that will be
called when you activate your extension
haha i need to activate my extension i
might want to define that as well in the
in the manifest and there are some
activation events here
and you see my extension will only be
activated from the moment i call to say
hello command well no i don't want that
i this is a google extension i want to
use it all the time so i'm just using
all events to activate my extension okay
so that will be called and now what i
want to do is write my code
this is going to be the most simple way
to write the code obviously not the most
structured way to write your code um
i might
i only have 10 minutes so i might not
have time to do
to dive into that
so
this is a first line of code basically i
create a new command
i registered that and the code that i
will be executing is open
which basically is a start in power cell
or
what is that in cio opening a hyperlink
basically
and you see that it doesn't really work
because i've got some
red lines here well that's because i did
not install this library it doesn't know
the open library so you might want to
add that library to your extension
and you do that with npm
which is the node packet manager because
i installed node.js i have this node
packet manager as well
and i can install the
opn
library which includes the open
yeah the functionality basically that i
need what it did now it added it should
have added let me refresh this
the opn library
to
my note module so now i can code against
that that is
number one
number two i need to
make sure that i have a variable
that
knows the oven so
actually the open variable i declare an
open variable and that is basically the
library from opn so now this open is
okay i will be able to call this
then i need some logic to get this word
and the idea is i'm on a word with the
cursor well select that word and use
that word as a search um in in google
and you know what i like internet and it
was
just plain old on the internet um
there is a get word function that i will
add and you see it's clearly going to
select the word and then
provide that word here as a return
variable you see
yes f1 sees okay you believe me
okay
done
let's test this
f5
builds my extension
and it says congratulations your
extension google is now active that's
already a good start
so let's uh create
a file
let's see
if our get word works ctrl shift p i
should have a google
search google
and there you go
google is searching for the word
i was
having
and it also selected the word basically
cool nah not cool enough
nah this is not cool enough
let's try something else let's search
anything on google
so i register a new comment search
anything in this case i actually want to
input from the user within the comment
palette basically with the comment
so i add that as uh
here as a registered comment but
obviously um let's stop this one
i need to add this as a contribution as
well so let's contribute here a second
one
uh which is search anything on google
and you see here that i'm using the vs
code appy to show me an input box and
with that inboot box i will basically do
the same as as i've been doing here just
opening
the url let's try that so i should have
now a second command
go to shift p google
something on google this is my input box
let's search for uh blah blah blah
uh
let's find waldo
and here he is
and this is the
most basic way to start off with
creating your own extension
it's a little bit more to it you need to
like include your readme file decently
uh obviously
describe your extension what are your
contributions how does it work for
instance for the rest client there is
a very big readme file but it basically
is a complete manual on how you use the
rest client extension you need that i
mean people need to know how you
how they are going to use your extension
package json which is the manifest
yeah main part is there that you need at
your contributions you can contribute
more than comment you can contribute uh
snippets as well
you can contribute um callers the
burgers and all that
one thing that i didn't do well is i
actually depend on this opn thing so i
need to add my opn to the dependencies
as well oh it's already there
okay
it's already there
cool
wouldn't know why it's already there
um so source directory gets your source
i put everything in the extension.ts
please don't do that that is just
not not the right way to do that
[Music]
not really clean
what you can do and let me show you
something else
a recent folder here so this is the code
from uh this is the a language extension
not saying that this is right you see
here that this
a lot more ds files and in my uh
extension.ts which is still the one
that's going to activate all my comments
uh well it's it's a little cleaner i
will call out to the different files
basically um
that
yeah that include the code specifically
for uncertain function but in any case
extension ds is where it all starts
let me skip because i only have three
minutes and i want to show you
this
now
this extension and
i i don't have any money in this but i
did
struggle through quite some stuff that i
don't want you to struggle with anymore
it is on github
so you can just download it and do
whatever you want with it and there is
already solutions for for instance
reading your uh settings in vs code
reading the launch.json
readingthe.js and using that as settings
within whatever you are trying to do
um it is a solution and thank you yonas
for uh how to call powershell um
this is there already as well um so
please don't put too much time in
finding out the stuff that is already
being put time in
let's be also try to be as productive as
possible the open url which idea i got
from tobias fenster
yeah there are as you can see already
quite some stuff um that has been found
out please download it look at it and i
have an extra download as well so
there's one quote of the previous day i
would like to show you
which is vehicle obviously who said
vehicle is absolutely my far most
favorite development environment beyond
any doubt
i saw during a session a big red cross
over the vs code thing
it didn't really mean that it was just
vs code for azure functions
if he could he
you would very much use vs code for that
i like to hear that especially from
someone like him like he has been like
diving into a lot of languages and if
you can do that with vs code and his
favorite tool is fierce code i think
that's a very good statement
which ends my
session on
did i at least a little bit rock and
roll this vs coating
[Applause]
and do you have questions i have
t-shirts
and i have nothing to throw so only the
t-shirts
anyone questions
let me see nope i don't have anything to
throw
oh
the throwing part is going
yeah here
excuse me
yeah so obviously this new environment
allows for building your own extensions
for your il as well sorry
so environment allows you to build your
own extensions for
while doing stuff overall yeah is it
just typescript that you can use or and
javascript for building extensions or
can you use like i know.net and linkedin
somehow into vs code to build extension
for managing al as far as i know it's
only typescript and javascript uh that
you can use basically because it runs in
in that environment
oh okay yes uh so uh i want one question
uh is there something for
all the navy code for nvs code can we we
use os code for to do something with all
the nav code not the ael code well uh go
to that session from cern that is going
to be on our 130. he uses vs code for
source control management the old uh
seaside very old c set
uh that we have so yes it is uh
absolutely uh
possible but not obviously to compile
right thank you
i don't have a question but more you
want a t-shirt a tip no
when you use visual studio code by
default it tries to open files as utf-8
encoding
if you're ever going to use it on
alt c side text objects
they are exported as oem
but if you accidentally save them in etf
octa you've got a big problem so be
careful with that okay i actually did
that and so yeah maybe yeah
it doesn't always recognize the encoding
exactly okay
another one but i want to throw this can
i can you have a minute i'm going to
throw this
yes got it
in all these sessions about visual
studio code
i've never seen anyone activate their
developed license
is that no longer really necessary or
something
uh again
where do we act when do we i need to
activate our developer license how do
you mean how to activate
to see the codes you and and the in the
older versions
before you
can open a code unit you need to switch
to your developer license
uh
or if it's not activated on the service
tier
on the database
but but now we we just open the code and
we download the symbols and
we can just see the code
like just like that is that no longer
necessary
yeah it is necessary to code against you
need the symbols yes but
if you need the development license to
download the symbols i have absolutely
no idea i never tested that with a
customer license
so i never had that question in my mind
either so
you can develop without the developer
license then
yeah but in the development environment
you can but you need the symbols and the
question there is you can you download
the symbols
without development license me maybe
thank you
the symbols that does not the simple
files does not contain the sources as
such it only contains the public surface
of the objects so the methods the public
methods the
fields so it's not the source files per
se you're downloading it's the symbol
what is preventing our customers from
trying to develop on their database
you still
right now you still need the
[Music]
developer license because the license is
checked on the servers you're only
running where a kronos license you have
the
demo license you have the 50 objects to
develop against
but it's a good idea to stop your
customers to develop on their database
i totally with you on that one
yes
yeah yeah
this work yeah uh do you think it's
still the device's idea to separate your
folders uh
just by the object type
why not
sure you can it's up to you i do
might do that
else yeah
i
why wouldn't it be a wise idea
to fill the research it's not optimal
look
it's the uh all code is separated yeah
by type but in the new environment
it's not only cl objects that's
all in there so maybe there's some
insights or guidance about it yeah
well
it's up to you you can put your code
wherever you want in uh
yeah i do understand i'm just
asking a question specifically for you
do you see any
different way of
managing your folder
no because basically this is how i put
it in my extension so this is the way i
would like to to do that yeah at this
point now obviously there was not that
much experience at with with with
building extension in this environment
so maybe we will come up with some other
way on how to do that i don't know um
i i this works for us at the moment
thank you
yeah thank you
anyone else
last question last t-shirt at least oh
thank you so much for sitting over there
yep
okay
i have one dilemma for this visual
studio code you have one dilemma with
fish code oh yes okay only one dilemma
that's really good uh does does does
this mean that we can forget for the
programming in development environment
with cla code
and
in the future we only
work with the visual studio code
i don't understand
um
don't understand the question
okay so
um i hear it again yeah what he's asking
if it's only going to be restored
in the future well the extension is vs
code so yeah that's going to be a vs
code only
what i tried to convince you about
that's that's really good thing
okay i understand that i just asked
would we development anything in
development environment with with cla
code or
other possibilities only with visual
studio code
to programming in the future
um i i don't understand the question
sorry um
are we ever going to use the old
development environment for the new
al development well no
what was that
what
is long term going away we are moving to
vs code for everything including the
base app right now the base app is still
developed using seaside um but the goal
is definitely to move everything to the
new language to al
only using this code
is this means that we are going to
develop reports in
visual studio yes for everything
everything yes
we don't have a timeline i mean we need
to
we of course need to be able to compile
the entire bazel app we need to have the
same functionality
and bmp i mean so it on all
aspects is a
experience which is sufficient
or better
only question for husband
i have no t-shirts anymore i will not
throw it please
i can try but people will get it
probably
okay thank you very much and yeah i'll
see you next time
