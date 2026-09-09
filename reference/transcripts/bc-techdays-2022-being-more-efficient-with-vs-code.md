# BC TechDays 2022 - Being more efficient with VS Code

- **Source:** https://www.youtube.com/watch?v=q7pr6l60B34
- **Video ID:** q7pr6l60B34
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 80m19s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

foreign
[Music]
foreign
[Music]
Tobias Fenster and David feltoff
[Music]
Welcome to our session being more
efficient with Visual Studio code
you can probably imagine because for
most of you it also will be similar how
much fun it is to be at an in-person
event again so really really gracious
for or thankful for all of you turning
up and being able to talk to a real
audience not just into a camera or
watching a screen so thanks a lot for
all of you for coming
um yeah as I said our topic for today is
being more efficient with vs code so we
will share with you a couple of Tricks a
couple of hints show you a couple of
demos how you can maybe work faster work
easier with our beloved development
environment Visual Studio code
but first of all I want to introduce
myself
my name is tobia sensor I'm one of the
managing partners of 4ps in Germany I'm
also a Microsoft Regional director and
MVP for Azure and for business Central
and if you want to follow along what I'm
doing you can find my Twitter handle my
LinkedIn handle and also the URL for my
blog
and I'm extremely happy that David has
agreed to talk together with me so I let
him introduce himself yeah hello my name
is David feltoff I am developer and yeah
I don't have all these titles but I
still like to be in touch with the
community for example by creating the vs
code extension air code actions and you
can also find me on Twitter or LinkedIn
whatever you like
great so the agenda for today
um what we will talk about is a couple
of things as I said that allow you to
work faster to work easier to work more
efficient in Visual Studio code and the
topics that we will cover are Snippets
configurations regular Expressions a
couple of recommended extensions and
their usage and in the end we will show
you how you can build your own Visual
Studio code extension if all of this is
not enough and you just need something
else something different
but with that I want to hand it over to
David again for the first section about
Snippets
exactly so I want to start with Snippets
and want to show you what Snippets are
how to use them and how you how we can
create our own
and I would describe Snippets as code
templates with some specific
placeholders so we can insert a bunch of
code and directly Taps wood and enter
our variables just the way we would like
it and there are already quite a bunch
of Snippets for whole objects like code
units or for smaller parts like page
fields or repo data items whatsoever
um but we are in detect days and I would
like to directly jump into the demo and
show you what Snippets are
so yeah you are seeing my vs code and
now if I start typing for for example in
TV Port I get a few Snippets suggested
and then I can see what the Snippets
would insert
and decide what I want to what I want to
use and then I can select a snippet and
jump through the specific placeholders
in the text here
and yeah go on and I think Snippets are
a good way on the one hand uh yeah two
of course you don't waste the time on
writing codes that yeah
that can be pre-populated but also if
you are inserting reports that or
objects that you're not maybe that
familiar with maybe you missed for
example that there's a windowing section
that we can work with and something like
that
but
the Snippets suggestion is quite noisy
because there are already quite quite
much Snippets
and we can clear that up a little bit
and keep it clean and for that we are
using the command in that snippet that
shows all our
Snippets that we do have
from all the extensions and so on and
you see that the scroll bar is quite big
so I'm searching here for TV port and I
get the same suggestions like an
intellisense and here I could say for
example I don't want to save the snippet
for model so let's hide them and the
report layout I also don't use that so
yeah just hide a few of them and now if
you are using intellisense again it's
much cleaner and uh yeah so it's a
little bit it's better
the next one I want to do is I want to
create a test code unit now and the
first thing I want to do is that I want
to insert an ID
and what you see as well that's the
Snippets yeah they are at the top and of
course I want to it's a d and just want
to hit the space enter and have the ID
with me
so I think there's a setting for us Al
developers that we can or should have
always activated
and we can find that in the snippet
suggestion
and here it is the default one is inline
we could also say that we do not want to
have Snippets at all but we can also say
that we want to have them at the bottom
that's the one that I prefer
and now hitting again the intellisense
the Snippets are at the bottom and our
IDs that we want to insert now are at
the top and we simply can add enter and
go ahead
but now let's say the snippet is it's
already good but we are doing it
differently in our custom in our company
so we want to adjust it a little bit
just so that it's sweet sweets our needs
um for example I'm clearing the
description I don't need the it's
initials also on one trigger we are not
working that much with a variable
storage and so on so I can remove here a
little bit
just to have it more clean
look
maybe I also use the live will be assert
that's that's
more up to date
yeah and so on and so forth so you get
it
and now I can simply select everything
and with an extension I have installed
which is called a snippet creator that
helps me to create Snippets directly on
the fly so let's do that
and I open the command bar and say
create Snippets so that's a command
coming from that extension
and then it asked me a few questions for
which language it is honestly uh yeah
obviously for AF
then I have to give that a snippet name
which I enter
and now it wants to have a prefix that's
the one that we are seeing in
intellisense so I will use t-test code
unit
and gives it some description
okay and that's already it and now at
the bottom right corner we see that the
test code unit was added to the AL Json
and that we should edit it to you using
it using the command configure user
Snippets that's what I'm going to do now
I go to the configure user Snippets
there it is
and here I can find my aljs and where
the test code unit snippet was inserted
and let me just quickly remove this one
okay so this is our test code unit that
we just created so we see here the name
we see the prefix the content of that
and the description
and now we have to adjust it a little
bit
to have these placeholders and so on
because we of course don't want to
insert all the time the code unit 50
106.
and for that I'm jumping to the
documentation from the obvious code
and there we see that we can in the tab
stops with dollar one dollar two and so
on and the last one is always dollar
zero where we can end the snippet mode
with
and we can all can also in the
placeholders by using curly brackets and
then then the placeholder followed by a
colon
or we could even use choices or
variables whatsoever
so I will do that
and I want to Sid
let's use here the placeholder
and now we do have
let me close this one
now the code unit name should be changed
in multiple places and there we want to
make an Excursion for the multi-cursor
functionality from vs code where we
simply can always click with Ctrl D we
can select or add multiple cursors at
the next find match position
so we have no four cursors in place
and have just to enter one times the
dollar two and I can leave that with
Escape
furthermore I
don't want to get a get rid of all these
four spaces there's another multi-cursor
functionality which I can use which is a
control shift l
that simply matches all yeah matches of
the fine set so I don't have to go
through them one by one and now I simply
click one backslip once backslash t
and that's it
um yeah furthermore I forgot one thing
that we want to edit something like
backslash T oops t
feature
and then we do have some feature
description here
and then we want to
start creating our procedure so that's
it that should be it for snippet let's
try it out
um I don't need the one from the from
NAB anymore so I can again go to my
snippet
and
hides this one so that my intellisens is
again clean and I only see the ones that
I want to insert but even if it's a
hidden from intellisense I could also
use it using this way that it is
inserted so that would still be possible
but no test code unit I only have mine
left
I am entering an ID
my test code unit
entering a feature posting sales orders
and now I can directly start and create
my test procedures
okay so uh for for now I will stop here
and go back to the presentation
and uh yeah here for you to read or to
look up the link to
um to the documentation of vs code for
the Snippets and what we did was we used
the snippet Creator use the configure
user Snippets command afterwards to
modify it
yeah we use the dollar one dollar two to
add placeholders
um we saw that we can use placeholders
for these tab stops we could also use
variables like the clipboard
can add choices so that we get a drop
down with some specific values and
there's also a possibility to transform
the text that we are entering we will
come to that later but for now just as
an info that is more to come
okay furthermore we I showed this one
just on the Fly that was a add selection
to next find match with the control d uh
or the select all equivalences or find
match with the control shift L and there
are further possibilities but I won't
show them at all you you can read it up
okay I think that was it that was my
first part I will end up over to you
thanks
um so next next topic is configurations
um David has now shown you how you can
create code basically faster change code
faster
um and we will now look look into how we
can navigate that code that we've
created faster
the first one that I want to show you is
that we can use fast scrolling
so you can see here this is um just a
regular page and if I scroll using my
mouse wheel you can see that I have to
do a lot of scrolling to get down here
if this is a large file it could be
easier to just hold down the ALT key and
now I'm scrolling only once and this
brings me right to the bottom or to the
top in this case now this is just a
quick and easy way if you know that you
have to cover a lot of ground using your
mouse wheel that that will make you
faster
another thing that you can use oh yeah
and that was already in the demo another
thing that you can use to navigate in
your files and even in between files is
the go to symbol in file Ctrl shift o
and also the breadcrumbs which you can
activate with Ctrl shift and the dot so
how does this look like if I'm in here I
can hit Ctrl shift and O and there you
can see that I now have all the symbols
that are in my file
so I can just go down here or I can
start writing and find the right place
so this helps me to quickly jump into
the right position that I want to go to
the other thing that I can use is Ctrl
shift and plus and this as you can see
activates the breadcrumb feature on top
of Visual Studio code here so I can now
hit the right arrow you can see here
that this now gives me a tree so
compared to the thing that we saw below
it's not just a list in which you can
search but instead this is a structured
tree that you can also use to navigate
into the right places so now if I go
down here you can see that I have moved
down in like line 50 and it's also worth
noting that if I hit Escape I'm still
back into the cursor position so that
way I'm not directly jumping there I can
just kind of preview and then I hit
escape and I get back quickly into the
position that I was before
the other thing that I want to point out
here is that by hitting the left Arrow I
can also change between files I can even
change between folders and so on so this
can also be a very quick and easy way if
you don't want to you know open a
different file move your mouse over I
personally am a heavy keyboard user so
it's nice to have that way to navigate
in your files very quickly and then open
them and and again
um yeah navigate to the right symbol
that you want
and the last one probably a very easy
one but still very helpful is Ctrl G
which allows you to go into
a line so if you get an error message
and it tells you that it happened in
line 50 then you have a very easy way to
move here
also to keep you oriented I want to
point out above here this is a
configuration setting called sticky mode
which allows you
um to keep the basically the breadcrumb
as well available here so if I'm
scrolling down here it changes as you
can see but then for longer procedures
or the layout section like here I can
say keep track of where I currently am
at
now you might say dude that's shortcuts
that's not configurations and of course
you are right
um but the thing here is and that's the
reason why we put it in here that those
settings or those shortcuts actually are
also configurable so there's a default
list but you can also add your own
shortcuts or change them so if I open up
the list of keyboard shortcuts I get the
full list here as you can see I can also
search for them for example reload
window then I can see okay that's the
one that I wanted to have but I can also
hit the
shortcut oh
if I don't mistype
plus here
um
and control is spelled like this yay
um so now I have the the control B
shortcut so if you only know the
shortcut but not the name you can also
search for that and then of course you
can change it
so I want to have
this as a shortcut that works I can also
do things like oh
change it again
things like Ctrl C then it tells me that
18 existing commands have this key
binding so I'm also notified if if any
changes are happening
um and then you can also
see if we go back to the full list that
there are commands that don't have a
shortcut
or might have been deleted can't find
one here so then I can also add my own
shortcut if I want to Define one for for
a specific action
and what's also interesting if we take a
look at that is that those
configurations can be synchronized
across machines so if you have maybe
different environments you have
different I don't know VMS laptops you
get a new laptop whatever you don't need
to manually set all that up but instead
those configurations can be synchronized
and it even recently got a feature
that's called profiles so you can have a
profile for Al development or profile
for Powershell a profile for c-sharp
with different settings different
extensions different configurations
which also helps to unclutter and make
sure that you're really working in an
optimized environment
and just to quickly show you if I go
into the settings here I can say turn on
settingsync and then I can select the
things that I want to have
um synchronized settings keyboard
shortcuts user Snippets and so on I can
select them log in using I think GitHub
authentication or a Microsoft account
and then I have them synchronized and if
I move to a different machine I can
synchronize again and I'm up and running
again
same for the profiles and you can see
here I have a default one and a PC tech
base 2020 I can create rename export
import the things that you would imagine
but the main thing is that it helps you
to have different setups different
configurations extensions etc for the
different environments you might work in
um another thing that helps with working
faster in con are a couple of
configurations and we could basically
have talked about the different
configuration settings for I don't know
45 minutes 60 minutes so we only
selected a couple of you
um very recently also added is the new
merge editor
to show you how that looks like
um you can enable it
by searching for git merge and then if I
select this then it will use the merge
editor for example here I have a
conflict now I can say open in merge
editor and now I get a nice little
overview I can see the different changes
let's say I want to accept that one
I can see that this has actually been
automatically been merged but I can also
undo the merge
and then let's select that one and now I
can see Zero conflict remaining except
the merge and then I have done my merge
I know there are really great merch
tools out there but maybe for a couple
of easy mergers or for those people who
haven't used a specific three-way merch
editor before this could also be a nice
alternative and as you've seen the
default is still the inline view okay
now I don't see it because I've solved
the conflict but the default is still
the inline View and then you can open
the new merge editor if you want
foreign
another thing is the format on save mode
I guess that most of you are familiar
with the format on safe which just
triggers the auto format when you save a
file but then you might run into a
situation where your format settings are
maybe different or you have an old code
base that is not completely formatted so
if you make the change and then you save
it will format the whole file for you
unfortunately there are settings here as
well so if we go in here
search for format on Save
then we have the format on save mode and
that explains very well what it does the
default is to just format the full file
you can have only the modification but
that requires Source control so if you
have Source control it will identify the
changes based on the source control and
then only modif format the modifications
the changes that you make and the other
option is modifications if available
which means if you have Source control
it only formats the modifications if you
don't have Source control then it
formats the full file
then we have the simple file dialog as I
said before I personally am a heavy
keyboard user so when I do something
like Ctrl o to open a file it's nice to
have this simple
um
file browser here where I can just use
the keyboard to go into directories to
move back out to start typing and then
it moves around so for me that's a lot
faster but also that's a setting
called the
quality simple file the sample dialog
which is by default disabled then you
get the standard operating system file
dialog but you can also enable this
simple dialog
okay that's it what I wanted to show you
for configurations now we go into the
regular expression session and just to
briefly share with you the history of
this session David had entered into a
different conference a session about
regular expressions and I voted for it
because I really wanted to hear it but
unfortunately it didn't get enough votes
so I asked him if he wanted to join the
session at or if you should try to get a
session in Tech days unfortunately he
has agreed so this is not a Content that
we would have otherwise missed out and
I'm very happy that David will show you
what it was
yeah thank you to be yes
um yeah I cannot hear you chewing yet
but maybe we can change that I want to
show you what regular expressions are
and how we can use them and
um yeah I would describe or what can we
do with regular Expressions is that we
can search a specific pattern in a text
in this pattern that we are searching
for is described by the regular
expression
and besides simply searching for it we
are also able to making more powerful
Rex we place or search replay scenarios
and yeah that's that what that's what we
can do with it and
um yeah I know that there are reasons
that there are images like this in the
internet uh and I can understand that I
mean
um this at the bottom
yeah this one
uh it's a totally valid regular
Expressions
um and if you have no clue about regular
Expressions what they are that might
scare you and I could understand that
but
um
I think we don't have to be so scared so
there are only a few things that we have
to learn because they are simply special
characters and these special characters
Define groups traveler classes
um quantifiers or something like that
and I want to go through through that
with you with a with an example that
should be familiar with you so I want to
find all table definitions so all table
Yeah tables with ID and that end with
that name
so I will switch over to the base app
and now I want to go with you yeah you
see it
um I simply search for table and then
here is a flag or an option that we can
set which is called use regular
Expressions I will do that
and you'll see it still works so that's
also a valid regular expression because
until now we are not using some special
characters
the first special character that I want
to introduce is a DOT which is a white
card so with that we are searching for
uh so we are matching the table one of
customer but we are also matching the
equal sign or the N of table name
and that's obviously not the thing that
we are that we want to do so we only
want to allow digits digits as next
character
and that's where uh chair Vector classes
come into play
so with that so we just Define them with
using square brackets and then in these
square brackets we can Define which
directors are valid as an extra Vector
so we could say
um ABC then only ABC is valid we could
also Define ranges Like A to Z uppercase
A to Z lowercase
or zero to nine
but we could also make a blacklist that
we say all characters are allowed but uh
not uppercase A to Z so that's what we
are doing if we entering the carrot at
the beginning of the chair vector class
so obviously what we are going to do is
we
are entering 0 to 9 and now we
don't want to have that now we are
finding all tables and the first digit
of that so that looks much better
um that there's one more thing I want to
uh say about javecto classes
if they are recurring ones like a digit
for example there we have synonyms for
that so uh I could have also used the
backslash D in this case because it uh
yeah says as well that it is the zero to
nine
but there are other yeah
um familiar or other
shortcuts for example the backslash W
which stands for any word character
vector or the backslash s that stands
for any white space character so yeah
there are a few
shortcuts for share Vector classes which
look like these
okay so we are still matching the same
now we want to find out or now we know
that table IDs have more so they are
longer than one digit so we need somehow
to say that
they are multiple of them and that's
what quantifiers are for so we could add
a question mark that would say or would
mean that the digit would only be there
zero times or one time
and obviously the one that we are using
or that we need for now is a plus sign
so I already will add it here
um but I could also use a specific
amount if I yeah enter these in the
curly brackets that would also be a
possibility but not needed for now for
us and what we could also do now is we
could use the backslash W so any word
space share Vector one or multiple times
to find
for example auto match
I think I'm missing a space here yeah I
am so now I'm matching a table 18
customer already
so that looks good for now but uh I'm
also matching this one's obsolete reason
or some text inside here
that's not what we yeah want to do we
only want the table definitions and they
start always at the beginning of the
line and uh that's why I'm introducing
now the anchors
so if we put the carrot at the beginning
of a regular expression that means that
the line has to start with that one
so
I'm putting it here at the top at the
beginning of the vehicular expression
and the other occurrences are gone so
I think we are coming closer
but now you might say okay David but
there are other table names for example
the the sales line or country slash
region or cast dot Ledger entry or ship
minus two Edwards you know what I mean
so uh even so what we tend to do then is
that we are making a white lace approach
and try to do something like this quote
followed by a word space a word
character or by a space or by a minus so
something like that
um
I wouldn't do that because I don't know
maybe there are other table names
um that that I don't yeah have in my
mind yet so better would be in this case
to use a blacklist approach
simply to say
um we have the ID
followed by a quote
followed by one or most characters which
are not a quote so we remember that we
can negate the character class
and if you are doing that I would simply
paste it in here
what
say what it is now we are matching
um the the other tables account dot
scheduled and so on
so that looks also good but now we do
have
um
yeah now we do have uh we are either
matching the customer table so with all
quotes all the ones with quotes and
that's where the the all come I will
turn off
screencast mode
um
yeah so
um what I can do is with all so with a
pipe I can combine these two regular
expressions so I can simply put a pipe
between them and then I'm matching
everything
but there's even a better way and that
is the last one I promise
um if we that we can use groups and
these are the things that we can do with
normal parentheses
so our first option is the one with uh
just virtual vectors the other option is
the ones with quotes followed by one or
multiple characters without a quote
followed by a quote
and so we can combine them in a group so
we made a group around it and inside
that we put the pipe
and now we are matching all the tables
and there's one more thing with um with
the groups that's uh yeah nice the same
they capture the text inside that and
yeah what I mean with it is what I want
to show you in a in the replay scenario
just for the fun I will do a the
parentheses our group also wants ID
and then I've prepared some text here
which I'll place
inside this one and you can see
one window
something like this
so what you can see is that in the first
group
which we can refer with dollar one
there's plus the ID inside and the
second group
uh we have the name and in the group 0
there's a whole match so everything and
we just we can refer to them by adding
in the replays text the yeah dollar
integer
so with that you can replace uh some
text and refer to a part also of the
matching text and that can also come in
handy
okay
um and what you can maybe do with it for
example
is
um
yeah it was basically shown as a
keynote today but I want to show it
nevertheless we can open the editor now
the search editor in vs code with all
the matches and there I can say as well
select all matches which I do have here
and then we are having again the
multi-cursor functionality and I can
copy all these
uh yeah all these occurrences and then I
can for example
go here
enter permission set tabs wood
and then I could
paste it in everywhere
and then I say here I want in the BC
Tech days dot AF I want to do a
replacement
I will move the cavity at the beginning
because that one
is not really at the beginning and then
I can say I want to replace it with the
table data
dollar one equals yeah full permissions
doesn't make also don't want to say that
you should do it but I just want to show
the possibilities that we do have oh
dollar one was the ID
but you get what I mean of course I
should have entered the dollar to dollar
too
so uh there are quite some nice uh
possibilities with wagax and visual
studio code
what can we use it also
um yeah where it also comes in handy is
for example if I want to search for
libraries
um for test libraries so let's say I
want to create a procedure
and there I want to create some sales
yeah line or order
header
something like this don't know oh
Microsoft calls them
and the wild card here is not the best
one I should have better say that I
allow everything except an opening
parentheses because then I would be in
the parameter section as you can see
here somewhere
so I will change that
I think if we say
everything except opening parentheses
and now I'm I find multiple yeah
libraries for Microsoft they that
already create
um something with with sales
yeah create sales line with all possible
types create sales order items working
and so on with the contact with the
discount
so
I did not know that all these procedures
were there and so with the regular
expression we can search for them and I
think that also can come in handy just
so that we don't have to reinvent the
wheel in these cases
okay Switching back
that was our demo so we created a
permission set and showed with that the
vergex replace functionality and also
that's a relevant test Library procedure
we found some
and that should be it with regular
expressions for now
next topic
um will be the recommended extensions
and before I start with that I mean they
are already quite a bunch of extensions
and
yeah that's not all and that's just from
the AL perspective so I mean there are
other vs code extensions that are that
are coming in handy but
um yeah before I want to start I want to
say thank you to all of these
contributing and so if I can't show
everything in our demos our time is
limited right
so um I focused on how we can do things
faster in our workflow yeah that we are
doing
so first topic is create or extend
objects faster
and there we do have the object with
that functionality from the AZ aldaf
tools
also at multiple Fields functionality or
even from from Al object ID ninja the
assign ID is a multi-user weapons
so let me switch to my project here
and let's say I want to create
what's going on there I want to create a
new
a new Wizard
that's the file wizard from the Aza Dev
tools
and we can create multiple objects but I
think where it really is a great one is
for pages
because
there can say I have an object name my
customer list
and I have a customer
it is of type list
some application aware category yeah
just use this
and it should create tooltips
I go on with next
I will sort them by ID so that I have
some most relevant things here in place
directly I mark them move them over to
the selected fields and I click on
finish
and what we see here is that the page
Fields have a tooltip and it's not just
the specifies the blur it has some
meaning and
yeah so where how does it do it it
checks where the recorded number is on
other Pages as well and takes that we
use we use this this toolted
but it might be that the tooltip is not
really the best one what I could do then
is click on a code action and say we use
tooltip from other Pages same extension
same functionality but in this case I
get a selection on from all pages where
it is without tooltips and then I can
say yeah maybe this one is the most
descriptive I will take this one
for example
and
yeah so that's if you want to use two
tips and nice functionality
furthermore if we are now we now want to
extend a specific page and we want to
add multiple Fields there as well and
let's say we want to add them after the
number then I'm placing my cursor here
at the number field
using again the code action and there it
says add multiple fields
and it's again the same functionality
and I can select some some things here
I could even search for some yeah a low
line discount for example
and I see that I have sweet selected
click OK and they are added after the
workout that number field
so I think that can save quite much
typing and uh just using the commands
that we do have here
furthermore I said the
object ID ninja from from yeah vehicle
is here
this one unfortunately it does not work
right now that's a that the wizard is
working with the ninja but I think
that's yeah
coming pretty soon and
um yeah what we see here
that
the object are denanger suggests another
number and that might be because Tobias
and we are working on the same project
but uh he already creates in his Branch
or in his his local repository he
already used the pages the three pages
so
um I should better use the the one with
the three at the end just so that we
don't have any ID conflicts
and yeah it's as easy as selecting it
from the intellisense so also a very
nice tool
okay
clean up your code faster
um same extension is it a Dev tools has
much features for that so
um I think I wouldn't get them on the
page all so I just stopped here but uh
with Once through his with me and you
can see what what it's capable of just
to know a few things we move with users
we move with usage the sort variables we
move unused variables and parentheses
and so on and the most of them you can
also add on save so if you are saving
the fires and then the variables are
sorted and so on that you don't have to
think about that one
we could also
disable some warnings if it's fine for
example that in this case there's a
warning don't know a case for that but
um then I could uh yeah simply click on
the code action and say disable it this
time then it surrounds it was a program
that it says program warning disable
this line and directly after it it
creates another pogma where it restores
the warning again
and if we want to have more code cops to
come play with to keep your clone even
more to keep your code even more clean
uh you can use the lintacop business and
business Central intercom extension
and yeah with that you there are I think
10 15 words something about that
um to comply with these as well
then I do have navigate faster uh I
thought about showing the object
Explorer now but we all see it in the
Keynote
what's that there's something else
coming but
um yeah for example the object Explorer
from from the azair dev tools is easily
shown as clicking on on the app file and
then it's here
but there's another possibility which I
think is not that well known which I
want to show as well and that is a
object Helper and they can simply click
Ctrl shift o
in where while I'm coding here I simply
click Ctrl shift o and then the page
pops up and I can say I want to go to
the sales line and it directly opens
this one for me so I think that's an
easy way to not use a mouse click on the
app file or even the things that
Microsoft will invent that's also a nice
solution to to navigate through the
symbols
okay
then how can we code faster I think
there we do have a few conversion things
so there's already something in the code
and we can convert it
for example we can convert options on
the fly to enums so we are using them in
another place in the code as well then
we can convert it to an up enum and then
we are able to use it at other places as
well
we can create interfaces based on code
units so that's also a nice
functionality and saves you quite a lot
of typing
you can convert text to labels you can
and extract procedures whatsoever
I will show that shortly to you
so the first thing I'm showing is a
create interface I simply go on the code
unit and on the top line I activate the
code actions and there I do have an
action which is called create interface
it suggests me a name it simply puts in
a iPhone interface at the beginning
and then I do have my interface with all
the procedures parameters and so on so
yeah assets that can save you quite a
much of typing
the other things I want to show I said
we can create an option
we have here an option on table field
and it's yeah it's a member site that
has successful member prefix and the
caption is a caption suffix I mean sorry
and in between there are some some
options that are missing but
nevertheless I can simply say we've we
Factor this one to an enum I give it a
name
and I'm going to go
so it identifies uh ideas correctly the
the member correctly the captions
correctly and so on
and then I can go ahead and use this
enum at other places in the code
another thing was the extract procedure
I can simply go in the repeat until Loop
and say I want to extract this one to
another procedure
so that's that's the code action I'm
talking about
to something
in a loop
and what you see here is that we it
recognized that the customer
was used before and afterwards
and so it has to give that over as a
parameter
but the amount for example was also a
local variable on that do something
procedure but it was only used in the
code that yeah we extracted so it moved
it down to make it as local as possible
furthermore I could here click on the
message and say this one should be a
label now
that is my new label and also screencast
models
not that good okay hope that's better I
could create that some variables are
Global afterwards and it places them at
the weight
position according to the Microsoft
style guide for for these things
and so on we can create we can add
parameters and whatever but I won't go
too much into detail due to lack of time
and then last but not least we do have
uh the create variables there are two
extensions basically that are doing that
and
um yeah we can also create procedures on
the fly or something like that and
I will show these ones with you together
uh by by
completing our test procedure snippet
so I will go to that
um I think he would where was it here it
was
so we stopped here
and
I want to create now a test procedure
so the S already is snippet but I think
that's not
um yeah
it does not match R1 needs directly so I
will clean it up again
simply remove it create a new snippet
for that you know it
create snippet that's fine
hey
test procedure
now the prefix so that was again the
thing that we see in an intellisense
the test procedure
BC Tech days as description
and now I show you how our
test procedures are looking normally
so we do have something like a given and
then customer with special setup
and then we do have here a prefix create
and then nearly exactly the same text as
above in the given uh just different so
just uh with a tasker case
and after that we want to add procedures
power meters
and want to stop here at the end at the
end of the procedure to go directly
hit enter end yeah so can we create and
snippet for that as well
let's try this I will create a new
um so we I will create a new snippet for
that
again a a language
snippet is so it has a name which
doesn't matter the prefix is more
important
snippet description doesn't matter as
well
for my case
okay and now we modify them
again in the AL Json
and I have to scroll down a little bit
this one we can see isn't the best
here I'd have to remove these now it's
fine
and maybe it can also
at the tabular here
so
now I have to specify the procedure name
if I want to create a new test procedure
and then I directly stop at where I want
to create my first given statement right
and now what is more important here is I
want to create my given
um yeah I want to create a snippet for
this one
so obviously here I want to create my
description of that given
and now I said I want to have here the
exact same text but we want to slightly
transform that so that there's Pascal
case afterwards
and then we can go to uh we want to use
parameters and stop it at the end
okay so we said we want to transform it
here slightly
let's go to the Microsoft documentation
and see if that's possible so we see
here we have a variable section
and then we do have a variable transform
section which is looking good
but as I had the first look on it it was
quite uh yeah it was not that easy for
me to understand that so I want to go
with use word once
so that you understand or that you know
how to read that and that you can create
it on your own
so here we do have the extended Packers
now form
and I want to go with you step by step
forward so we already knew a tab stop
can be created by Dollar followed by an
integer dollar one dollar two that's the
thing that we are doing all the time
but I could also do this one
dollar and transform
I will copy that
to have it here
and then let's look how the transform uh
is explained we see it here at this part
and I will copy this text as well as we
are also using it I was needing it let's
say it that way
and we see that consists of a regular
expression now luckily we know how
regular Expressions work
um and then it is followed by another
slash and then there's either a format
or a text so the text would be the same
way we can replay something with uh yeah
but in our case we just want to format
it because here we see the format part
there we can say that it should be in
Pascal case formatted
and the last part would be options this
is uh yeah this is a
regular expression option or regular
expression flag but we don't need that
for now
so I
already copied that now I need to format
part
but I now need only this so you always
see here this or and I know now that I
only need this part
because here we specify the integers
that we want to so it should be exactly
like the given description
um but it should be transformed by
Pascal case
okay and now let's create our result
so we do have
dollar
curly brackets
like this and then the integer so we did
it and now the transform part is is
coming next
and that looks like I will simply type
it here format options
just because I always forget to
how it looks like then and the format
should be now we oh
before that the WebEx is a thing that we
want to match the dollar one thing from
and we want to match everything so I
simply put a wildcat uh the white card
as a DOT sign and then I add the plus so
that it matches the whole given
description that I entered there and now
this one I want to transform to using
Pascal case
so let's see how we can do that
it says I should should enter a dollar
sign followed by a curly bracket
followed by an integer and this integer
is now the group of the regular
expression and we remember that in the
WebEx group 0 there's always a full
match so I'm entering
the the zero in this case then a colon
is followed
and after that I should either
use you up case or down case or
capitalize or whatever of course we want
to do
um we want to use a pascal case
so I paste it in here and Then followed
by a curly bracket
okay then the slash followed and then
the options followed as I said we don't
need them so let's throw them away so
this is our wizard
luckily you just have to do that once so
we don't have to look at that ever again
and I will paste it in here but now
let's see what we can do with it
we move my comments here
and uh yeah maybe
I will also
copy the text I can do that with yeah
there's a functionality for that that
you select something and then by by
using Ctrl shift and up Arrow or down
arrow you are creating the uh you're
duplicating the lines that you just
selected that's what I just did
and now I'm
creating either when scope the when part
and here the Zen part
then
should be prefixed with verify
and the one part should not have a
prefix that's how we defined it in our
company
okay so now let's try and
see what we can do so I want to create a
test procedure
um first of all I'm using my snippet
from the BC Tech days that's by the way
is a description and that is the name of
the procedure I did not go into that yet
because I think it's not important
um first procedure
next tap directly Place me to the
position where I can start creating my
given wins ends
that's what I'm doing now I say t given
customer with special setup you see
until now it's really the exact same
text but if I click now on tap the
transform will kick in
and it makes that to the Pascal case
and now I can enter my parameter
tip once again I'm at the end of my
statement and I can create my next given
sales order of that customer
I will hand over the course as a sales
letter and the customer
and we'll go ahead to you when post
sales order
hit tab transform kicks in
and I will do that
and now I will say afterwards there's a
sales invoice header that I get returned
and then I'm using the next one the tzen
and say verify yeah sales header is
posted and don't know what I should yeah
let's say I put into that the sales
invoice setup okay
so I have the skeleton for that but it's
uh everything is wet
not that good but we can manage it so
now I go through it and say this one
should be a variable I use the code
action for that and that says add local
variable customer
because that name directly matches with
the table name it directly adds it
without further questions
then I go to the sales Setter same thing
here I added and the record is added
furthermore I will go down to the sales
in my setup same play
Control Plus enter and now I already
have the variables but not the
procedures for that but I can do the
same here as well
use the code action create procedure for
that one and if we look at that we it
knew which uh yeah table type it was and
so we have the customer here ready
can do the same here for that procedure
create procedure create sales order go
ahead and the sales address also
populated
and now let's try if it also works with
this one because there I do have a
return value
uh create procedure post sales order
enter and also that's working
okay so yeah you can imagine that it's
working here as well so that's how we
can and why is I don't know a way how we
can create faster our code and
furthermore we have it always the same
way so
um yeah there's all test cases would
look would look this would look the same
and yeah I think
that's
end of my session or end of my demo in
this case and I yeah
hope you could follow
next part is um that we can maybe in the
future work even more faster with GitHub
co-pilot but that I would like to
give yeah hand over to you to be yes
thanks uh great demo just when you
thought the extended background noise
form would no longer be a part of your
life it came back to haunt you so um
coding faster using um
GitHub copilot sorry as um David already
mentioned that's not working for Al yet
but fortunately our last part is about
building your own extension so now
you've seen how you can create Snippets
you how you can use configurations how
you can use regular expressions and so
on but maybe there is still something
that is missing from Visual Studio code
and you absolutely want to add it you
want to create your own extension
um that that is able to do something
special that is not yet there and what
that means is that we're moving away
from Al and into typescript for example
and the good thing about that is that
GitHub Code Pilot copilot works very
well with typescript so I want to take
the opportunity to use that but first of
all what is GitHub Code Pilot well I'm
old enough to remember and I guess that
some of you are too the time when you
had to type in everything so there was
actually no help you needed to know what
you what you wanted to do and you needed
to type everything
I also still remember the conference
when finally intellisense was introduced
in Seaside
um well known in other areas and we were
really happy because now we got help in
creating our code
and since then actually not a lot has
happened in that area maybe intellisense
got a bit more clever you can configure
it as David has shown and maybe it has
better option Snippets and so on and so
on but still you basically need to know
what you're doing in a way
the next step for that is to use
artificial intelligence to propose code
to you and that's actually what co-pilot
can do and that's when you can really uh
yeah create code with rocket speed
because now copilot uses as I said
artificial intelligence it looks at
other similar code areas and other
similar code and makes a proposal for
you what you might be doing in the next
step so this is something that really
helps you to get an idea as you will see
in a second you can just create comments
telling it what you want to do and then
you get a code proposal the thing I
really want to stress is that this is a
code proposal it doesn't actually mean
that it is right so even with something
like GitHub co-pilot you as a developer
are still in the responsibility of
understanding what it does and verifying
that it is actually the right thing that
it does or the thing that you wanted to
do it helps a lot but you can't just
keep it use it blindly you still need to
understand what is happening
okay so this is GitHub Code Pilot to get
back to creating your own Visual Studio
code extension
the things that are possible are listed
here and I actually copied that from the
from the documentation page you can do
things like changing um the look with a
color or a file icon theme you can add
your own custom components and that is
something that we will do in a second
you can create a web view so the more
complex things like for example um the
the explorers that we've seen in a
couple of places you can support a new
programming language if you want to
define something or a debugger and then
you can also put Snippets into
extensions as David has shown Snippets
can be extremely powerful and I have
shown you how you can synchronize your
own Snippets but maybe you want to share
it in your team or share it with other
colleagues and then you can put them in
an extension you can have extension
packs which is basically just a
collection of an extension and to make
the list complete you can also extend an
extension so if you have something that
works well but you just need to add a
little thing that doesn't mean that you
have to recreate it from scratch but
instead you can yeah just extend an
extension
what I also want to mention is that this
is a quite complex topic and what I will
take you through in the next couple of
minutes is really only the bare minimum
where we're just scratching the surface
um but to give you an idea how it works
I thought it would be nice to have that
demo here
so how could we work even more
efficiently um with your own extension
well at least for me what is the most
efficiency blocker is distractions so
wouldn't it be nice if you could shut
down Outlook in teams but still get the
important notification and the reminder
that there is actually a daily stand-up
or whatever that is happening but
removing all the rest of it
unfortunately this is currently not
possible at least for the best of my
knowledge in Visual Studio code but
maybe we could create something that
could look like this
so what we're doing is we're adding a
new component here
which is basically giving me the
information from my calendar
from my mail and from my teams and as
you can see here I have just created
random dummy data so I don't want to go
into contacting Office 365 and getting
all the information but what we will do
is we will create just just random dummy
data
okay so um for that we want to be using
a scaffolding tool so a tool that
creates the Bare Bones of your extension
so you don't have to set up all the
files in that which is a tool called
Yeoman and the command is Yo code as you
will see in a second and as I already
introduced we will be using GitHub Code
Pilot
so let's see how this looks like
I'm in Visual Studio code again and the
first thing I want to do is just run
your code
and here I can select which kind of
extension I want to use I'll use the
default just typescript
the name is the 0365 viewer
the identifier
is something very similar
the description is something that I'll
skip for now I want to initialize a git
repository
um I don't want to bundle the source
code I'm going to use npm and now it has
created a code for me and it is running
npm install to fetch the the required
dependencies
so with that we have everything that we
need and it asks me if I want to open
Visual Studio code to just get started
with coding I hit enter
and now we are in here
and because I've done this before it has
opened up the files but yeah let's um
take a look
in a second okay so this is basically
just the bare bones um with basically
more or less an empty extension the
first thing I want to show you is how I
can Define that I now want to contribute
something else so we have the
contributions that you can see here and
this so far is just adding a command so
now I could run this and call the
command hello world and then this would
do something but what we now want to add
is something else and for that I have
prepared a snippet that I've called
contributions
so what we're adding is a view container
that is basically the full block that
you've previously seen with an ID and a
title and I don't have an icon so it
will be a blank icon and inside of that
container there will be three views the
calendar view the mail View and the
team's View
so with that we now have defined that
those things are there
but of course we want to show data as I
said I don't wanna
um
go into contacting Office 365 but
instead we'll just create a data
provider that creates dummy data
and
so that we don't have to do everything I
have created The Bare Bones of that um
as well as a snippet so you can see here
it extends the tree data provider
because we want to show a tree it has a
couple of default features that you can
see here it has a function that creates
that gets the data and this is where we
will create our random data and then we
have defined an enum and we have defined
a class that shows the actual tree item
so
what we want to do here is first of all
we don't want to show always the same
number instead we want to have a random
number
and for that I'll just type in get
random number
between one and let's say seven
and now if I hit enter
this is where copilot kicks in so it
makes a proposal in this case and offers
that it will create a variable called
count because probably if it's a number
then I want to count something and it
shows me how the random functionality
Works in typescript and I think that
that is actually a very good example of
where copilot is great because creating
a random function is something that is
not very complex but still it works
differently in all the different coding
environments that you use so to have
something like this that just gives you
the easy things in the right syntax in
the right way I think is is quite
powerful
so I'll just hit tap and accept that
part
now you can see here I also have a
Boolean that is called Showtime so if
you remember the sample I want to have
time for the calendar entries but I
don't want to have time for the other
two so we'll make an if here
and
if it's showtime
and then we want to have a random time
no that's not going to work
let's see if this is better okay so this
is um just a random time
and
actually yeah now it um creates the
hours
it creates the minutes let me scroll
that up a bit
and it even creates the seconds I don't
care about the seconds so I'll replace
this with zero oh zero
and then let's say
ah
let's say something like
around the minutes to
next
15 because probably I only have
appointments every 15 minutes let's see
and again this is creating the code for
me
this is maybe slightly more complex so I
might need to understand what this is
actually doing but for now let's accept
it at face value
now we want to convert it into a local
string
um
with 24 hour format
and that one also does it you can see
here it uses the default of En us
because probably copilot was trained a
lot on us code base but still yeah
that's something that I can live with
and then maybe make the change that I
that I want to make
so we have the local time
um
and then we probably need to add this
into our data
and there you can see it's now already
recognizing that we have a
that we have an array called data and it
offers me to push in a new element o365
data with exactly that time screen it
recognizes what the different parameters
are and here it goes a bit wrong because
if I just accept it it will tell me that
there is something wrong so let's
remove that part
so this is if I have time now let's see
if I don't have time what happens there
and again if I'm waiting um it offers me
to do the same thing
actually I forgot the for Loop
okay
so you can see here that it now would
offer me to create a for Loop
um we have basically already created
everything in that for Loop
so let me
cut and paste that one
okay
and then we have the same here
and here it does the same and you can
see here that it again guesses at what
I'm trying to do but still it doesn't
understand that probably now I don't
want to have the
um the date string in here so let's
remove that part
and
we we also need the
name so
let's get a random string of
10 characters
and again this is creating a random
string of 10 characters for me
so we will use this here
to show first the date
and then the random string
and
something like this and if we don't have
a date
then we actually
just use the
random string
okay
so this is it um and it turns it in the
end so now we have our function that is
used to create the random data heavily
inspired by um The Code Pilot Copilot
now we need to
call this for the different data types
that we have so let's say
um
sorry naam
lost track
okay yeah so again copilot is helping me
out and it basically says that
um if the type is calendar
then I will get the data with the show
time and if it's the other types um then
it will return the other ones
okay so with that we now have the code
that gets the data if it's a calendar it
also shows the time if it's not a
calendar it doesn't show the time
um the last thing we need to do is now
that we actually call this functionality
and for that we go into the extension TS
you can see here that this is some um
initialization data I'll just keep that
for now
but the thing that we also need to do is
um we need to call our providers and I
have created the first sample of that
one so it's the calendar provider it's
called with the calendar type and then
it creates a tree view called calendar
with the calendar type again we can use
the helpers here to add our Imports
and that should be fine and now of
course we need the other two options as
well and here I'm waiting again for
Copilot
and this time I hit Ctrl enter which
gives me suggestions and there I can see
that it would offer me to create a let's
put it over here
you can see more it would offer to
create the mail provider and it would
offer to create the teams provider so in
that case just accept the solution go
back in here and now my code in the
extension TS is finished
now let's go in here why is this red I
actually don't know let's see if I'm
missing something
oh yeah I put the data provider
in the root and it should be in the
source and it automatically offers to
fix this
okay now we should be good last thing
now is that
[Music]
um
we need to change the activation you can
see here that this extension would only
be activated if the hello world command
would be called but instead I want to
show this on my view
and I called it
0365 viewer
okay
so with that it took me like 10 minutes
to create it with heavy usage of copilot
now let's see what happens if I hit F5
to run this
and it's building yay
what did I miss
okay the GitHub co-pilot file is still
open that is something that I don't know
why
um sometimes happens for me if I open
the proposals then it somehow thinks
that this is something that it also
needs to compile and that has failed now
let's see if I close this and restart
and hit F5 again
where we end up
building its opening
and now we have our new view it has
calendar mail and teams but no data
that is not exactly what I was hoping
for
edit the providers
I've added the activation
huh
that's actually a view container not a
view
so let's use the view Instead try again
and basically what happened is that it
the activation event was not triggered
so it never really activated the code
and instead it showed the empty
extension
and see what happens now yeah now we
have our calendar elements we have the
mail we have the teams
um with the random characters and so on
that we expected and I can now see that
I should have put the um random
generator into the for Loop and not
outside of the for Loop but anyway um
what I wanted to show you is that
actually creating your own Visual Studio
code extension is not that difficult you
can use Yeoman as a folder to create the
basics you can get help from things like
copilot and then you can create your own
extension
um in any way that you need
okay so that's it
um thanks a lot for watching thanks a
lot for um listening to us and now we
would open up for questions
[Applause]
any questions do you have questions ah
here okay
that's good first row will be a short
one
uh do you know how to manage memory with
vs code because when you're running
large projects or let's say you have a
base app opened near you even with uh
code cops disabled let's say you've used
the search on the base app and it caches
everything and it
stores that the memory and RAM usage is
right you know how to probably release
it without closing or reloading the vs
code yeah
do you want to answer
um maybe I can give my two cents to that
uh I think I hope that there will be a
little bit better better if Microsoft
switches to the.net core that it does
not take that much memory
um yeah but yeah I think they're just
there are a few properties that we can
set don't remember them now but there we
can say that it should one in parallel
something like that so there are a few
things that we can set for the in the
settings for the a language Json but um
yeah otherwise I think there's not that
much to do yeah and I think there's a
reason why if you look at the system
requirements for doing base app
modifications it says something like 32
gigabytes or even 64 gigabytes of memory
so I think to a degree we will
unfortunately just have to accept that
okay okay
other questions
am I seeing you can get also get a
t-shirt of course
and no other questions it seems like
okay so in that case thanks again David
thanks a lot for sharing the stage with
me and uh yeah have a great great rest
of the conference was it that's good
yeah oh okay
foreign
[Music]
