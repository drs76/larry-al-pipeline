# NAV TechDays 2014 - .NET Interoperability in NAV 2013 R2 for Mere Mortals

- **Source:** https://www.youtube.com/watch?v=C9k5ZSktq2k
- **Video ID:** C9k5ZSktq2k
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 102m57s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

hello uh good morning and uh welcome to
Tech days once
again my name is Vos laab uh and today
I'm going to present to you a little bit
about how to use net interoperability in
Microsoft Dynamics and in some practical
real life
scenarios uh I'd like to start by asking
who is here first time on Tech days okay
quite a lot of you good
uh and may I see other hands in in the
air like how many of you are still not
using net interrupt
regularly regular like you know if you
develop every day and then like you
don't kind of declare a net variable
every day that I would call irregular so
so who does who does a net per
day okay a few of you I'll put my hand
down
so in the last couple of years uh I've
presented here at Tech days various
things about net and my sessions were
always called black belt so it was net
intro black belt and like web services
plus net intro black belt last year Luke
asked me okay can you do I it's okay you
have this black belt thing but can you
do the beginners thing so last year I
did net for beginners and net black Bel
thing and then look said can you do
something like in between like for mere
mortals he said so I said well okay I'll
do something like that so uh who is
meere
Mortal okay there are more people
declaring net every day than being meere
mortal but so here's this mere mortals
presentation this is why it's called for
M Mortals
uh I've introduced myself a little bit
so uh apart from me being Vio slavich
I'm also an MVP I'm blogging on v.com
please visit the blog most of the stuff
that I'm going to talk about today has
not been presented there yet but
everything that I talk about today
including all of the examples are going
to be posted there today soon after the
presentation before 8:00 in the evening
certainly uh what are we going to do
today so this is not going to be a
theoretical session you can download any
of the previous sessions uh from mbuso I
intentionally do not want to start
explaining how to use net so this is not
going to be like step bystep thing from
the beginning like how to declare a
variable where to look for variables etc
etc instead of that what I want to do is
essentially arm you with some additional
tips and tricks and tools that you can
put under your belt and actually use in
your daily life uh it's difficult for me
to to to tell like these things are
useful from net these things are not
because you know in real life they are
very ious scenarios that you will
encounter and various needs that you
will have to meet so I have picked some
examples which are explanatory enough so
that you actually can understand how net
interoperability operates and I've also
taken some examples which are cool
enough so that you can see wow I can do
these things now which you probably
couldn't do before uh so here we are
going to cover a little bit about arrays
I will quickly explain why then about
strings then uh about regular
Expressions file system file system is
important um surviving different data
formats which I I believe is kind of
relevant for us the Erp people then uh
how to convert between types A little
bit of that also how to handle B 64 this
is probably both useful and useless
example because many people do not know
what pay 64 is but I will explain and
for all of you who do uh you will see
how easy it is in net and finally uh at
this point I will stop doing stuff
primarily or actually exclusively in
clal up to this point everything will be
just seide and clal then I will move to
visual studio and I will tell you how to
use it like a pro so how to actually how
to properly do certain things in C so if
you're not a c developer you can still
do things right without having to think
did I do it right is it is it right a
better way so uh this is going to be the
content I'll start with
arrays and uh this is obviously not an
Asian Chinese proverb but uh my position
is that even though I've heard that net
arrays are complicated they are
unnecessary my position is that a net
sorry a cal developer needs to
understand net
Aras
um so why do we need net arrays I mean
we do have arrays in in C so the reason
why we need net arrays is because they
are all over the place so if you take a
look at the symbol
menu a lot of net methods just take
arrays as parameters or they return
arrays as return values and if you are
not able to use them then it means that
large part of net is just out of your
reach so you need to be able to know how
to work with net
arrays uh when creating a net array in
CL which we will see pretty shortly uh
you have a very simple pattern so you
declare an a variable of a type array
and then the syntax is this essentially
you have to call this create instance
method do not forget to assign it to a
variable of type. net array and then two
parameters it accepts first is the type
of the data that you have to create
there is this get. net type function in
C which helps you with that and the
second is how many elements you need so
it's different than in CL in CL you just
set Dimensions property and there you
have your array in net it's a little bit
more complicated so for example here if
I want to create an array of date times
then I simply call this create instance
get. net type I can pass a constant of
the type that I want so this zero DT
stands for blank dat time or for example
blank string stands for blank string so
if I want to have an array of strings I
can have get. net type blank string and
then the number of elements so uh that's
a little bit of uh arrays so let me
declare an array for you so I'm going
to create sorry a new code
unit and then create an array so a scary
thing about net is that every time you
have to declare a net variable you have
to start with net and then you have to
press F6 to get the assemblies list and
then once again and then here you have
to choose the correct one and this can
be scary because there are so many of
them and then it it requires some
scrolling and looking or which version
do I choose and then I select this one
and then here okay where is array okay
it's here so now I have declared it uh
my life hack is essentially help
yourself so uh there is no magic in
declaring this variable so it's just
string
so just do something like that where you
have common types and then when you need
to create a type of something just copy
and paste it will work just fine so you
skip that part of trying to pick the
correct assembly Etc so
that's just a little hint I'm going to
abuse it today a
lot system do oops this is a slide from
last
year yeah I will I will repeat some
stuff so this is going to be probably
the the only thing I I will repeat from
the last year so system. string is there
anybody here who never ever in your
projects had to handle
text so many of you okay uh
I expected so so uh we have Text data
type in in CL we can use it to store uh
textual information obviously uh with uh
nav all up to the version 2013 we were
limited to 1,24 characters per variable
in net we can have up to 2 gigabyt of
data within a text
variable uh but this is not the most
powerful thing about uh system. string
which is essentially the same thing as
text uh system. string is a class in net
which allows you to call many different
functions which are not available in Cal
so in Cal uh text is not a class it's
essentially just a value type it's a
it's a variable which can hold a value
and if you want to do something with
text such as for example take a
substring you have to call another
function in net nice thing is that uh
everything that you have is an object
essentially even though it's not really
it may be a value type but still it
behaves like an object string is one of
those things so string allows you to
directly call into the functionality of
string like taking a substring turning
it to uppercase turning it to lower case
or doing some funny stuff which CL
simple cannot do so U I'm immediately
going to show a demo which will
demonstrate both uh Power of the string
variable and also how to use arrays so I
will start with paring a The Limited
string so
um let let me start with this array I'll
call it array
of the
limiters and I will declare a variable
of type
string so net and again I'm just going
to use this string from
here so quick
you don't have to instantiate a string
it doesn't require a Constructor pretty
much like in C so here I will start with
hello everybody and welcome to
Tech Days
2014 enjoy your
time
okay so this is my string imagine that
you need to parse it in into words has
anybody ever had to do something like
that okay now many more uh how do you do
that in
Cal yeah you spend a lot of time
like in between 15 minutes and an hour
depending on your proficiency and
everything but you will have to write
some code to do that so uh let's start
with uh taking a look at what string can
do for us so there is a function called
split
and this split returns an array and it
also accepts as arguments just a second
this array of strings or array of
characters which are separators so I can
actually not look for one single
separator I can actually look for many
different separators and then split the
string into words which come out of um
of which whichever value I have so I
will start with declaring another
variable it will
be
character and then I will instantiate
this array first so I will say array of
the limiters
is create instance get. net type of
character this is my
variable
and I need to have coma space
exclamation mark and Dot so I will have
four elements in my array so here I will
say character is first let me start with
space and I will put a value array of
the limiters set value character at
position zero arrays are zero based in
net then I will just copy this three
more times 1 two
3 I'll have dot I'll have coma and I'll
have the exclamation mark I'll put them
on different
indexes and here I have my array of the
limiters I will also declare array of
results so this is another array here I
don't have to instantiate it I simply
can say array of results is string dos
split and then I pass this array off of
the limiters into it I'll save
this
yeah
thanks okay good and the last thing of
course to show that it really works so I
will declare an indexer
so uh I'm simply going from zero
to
length of the array minus one and then
do you see this probably not
right okay I'll remember to do that so
uh what I do I iterate from zero to
length minus one and then I get the
current value actually the value at the
current index I'll save
that
so and I will run that to see if it
actually
works okay I have to reconnect the
server happens occasionally when you
close and open the laptop
so
hello everybody okay spaces are not end
welcome to Tech Days 2014 okay so enjoy
your time okay so okay it it didn't
quite react well to those situations
when the two the limiters are together
but uh I could really see that any of
those blank strings they were not spaces
they were just blank strings I could
then remove them if I wanted to but my
point is here so this is a simple way
how to use uh a method such as
string uh to actually uh to actually do
something which might involve much more
time in pure CL and much more debugging
also not to mention Reinventing the
wheel um another thing that we could do
for example is find an extension of a
file name so imagine has anybody ever
had to find an extension of a file name
okay good so how did you do that you
probably looked for the Dot and then try
to find the last one and then everything
that remains is uh the extension so in
Cal we
can essentially yeah I've uh I've
violated my own best practice so I will
start with
it new code unit demo
to yeah yeah yeah yeah so it's a keep
making those
mistakes so I will start with string
and ah and I will copy it again so
here's my string and I will just say
that my. file dot is strange dodl do
zip so what is the extension here
zip yeah so how do I get to this uh zip
it should be easy if I take a look at
string uh let me make it smaller I have
this function called last index off so
it will tell me what is the last index
of a specific character that I'm looking
for so uh if I actually show here it
expects the character so I can say I'm
looking for this specific character I'm
looking for the last index of that one
so uh here uh I will say
that message
extension of this file name is and then
string do substring okay and then
string. last index off and then
dot let me missing one
more and let me run
that
sorry I didn't
understand behind the message what is
behind the
message yeah yeah but I have uh I have
put it there so um so this is the the
code and this is the result so it tells
me the extension is zip now this is not
to say that this is the correct way to
get extensions from file names I'm going
to give a better one this is just to
give you an idea of how to use this
system. string it is uh like
manipulating strings and Text data is a
very frequent task that we have to do in
our uh regular lives as
developers and it is easy to reinvent
Wheels all over and all of them are
already invented at working pretty well
in net so this is a couple of smaller
examples which are not that important
but good to just give you an idea of
what net is and what it can do for
you the next thing is regular
Expressions so I want to talk a little
bit about them so regular Expressions
they look ugly they don't look quite as
regular as the name suggests but what
they do is they allow you to analyze the
content of uh of text has anybody used
or done something with regular
Expressions okay good so uh typical
things where we use regular Expressions
is to verify that the user has entered
the correct stuff like the phone number
matches the schema or that email address
is valid or that I don't know
um you can search for example you have
large amount of text you can select all
of the email addresses from there you
can replace things in there so these are
typical tasks to do with regular
Expressions so again if you do that in C
L uh without net without any regular
expressions or similar it's going to be
a tedious task it will just waste a lot
of your time so let's do this simple
detection of email addresses let me
verify if all of my customers actually
have correct email
addresses so I'll start with creating a
new
demo so I'll start
with reg X class it's
net and I'm going to
copy
this so at this stage let me just
shortly explain Constructors
Constructors are variables uh sorry
methods which create instances of
classes so in net we need need to
construct or instantiate every single
class that we want to use unless they
are static uh so if you have a
Constructor you usually need to call it
first so here I will construct my
instance of regex class so it accepts
one parameter which is string which is
the regular expression that I'm using so
here I'm going to use the regular
expression for valid email I've prepared
it earlier so
this is what it looks
like
oops okay don't try to read that it's
totally unreadable and let me start with
customer so
if there are customers I'm repeating
until there are no more customers and
here I want to check if customer's email
address is valid let's take a look at
this re regex and the method that it
provides so here we have this is match
method this is match method returns a
Boolean it accepts a string and it tells
us does this string matches the
expression that I'm looking for so I'm
going to use that so if not
rx. m is
match and then
c.
email then
message this does not appear to be a
valid
address
c. good so if I run that
so this does not appear to be a valid
email
address okay and blank one okay I'm
going to get a bunch of those blank ones
I didn't skip those but I could
so this is an easy way to detect for
example email
addresses another thing uh where you can
use regular Expressions is finding and
replacing so for example imagine that
you have a piece of text such as this
so I'm going to declare a text
variable which
is
again so here I have a couple of email
addresses I want to replace them with
something I want to hide them for
example this is a web page I just don't
want my email address to appear there
for spam avoiding reasons so I will
start again with instantiating a
regex I will use a different pattern
because this pattern matches the whole
content of what I've uh provided what I
uh want to do is actually
use the inside of text pattern so
actually I can do it myself it has
back SLB and back SLB at the beginning
and at the end and here what I can do is
message and just show the result of reg
x. replace method so again there are a
lot of overloaded variants of this
replace method what I'm uh going to do
is use this one which is a simple one it
accepts a string that I want to replace
inside of and here what I want to
replace any match with so here I will
just say email
hidden so once again I'm zooming
in so this text contains two email
addresses I'm hiding
them okay I'm I'm missing something
again I'm not good at parenthesis
obviously so okay
running that and it will show this so
both instances of this email address
were hidden from from the text it could
find any so it does it didn't find this
specific one it has just found any email
address and then replaced it with
something else so this is regular
Expressions again uh useful Nam space
with a lot of useful classes in uh in
net and another area where I want to go
today is handling files so we often
handle files so we save files export
stuff into them we read files read data
from them uh
and cl as a language is fairly limited I
mean yes we can uh create files yes we
can open files yes we can create
temporary files in temporary folders but
for example can we create a folder or a
directory uh with pure CL not we can no
we cannot uh or can we actually uh do
many of like let me not theorize too
much let me just go into a demo and show
a couple of things that you can do uh
what I'm going to use here is couple of
classes I I will start with uh file and
file info file class allows you to
access files without context so it means
if you have a quick operation to do on a
file you use the system.io file class
for example you want to just append a
line of text into a file you do not need
to declare actually open a file then
right into the file then close the file
in three operations you just call one
operation and it does everything so this
is for example system. i. file and then
you have system. file do io. file info
which provides you some contextual
access so if you want to repeatedly
write to the same file then you can use
file info very similar with directory
and directory info so you can create
directories just as a single command
like just do this and then it it doesn't
remember any context and then you have
system. path which allows you to
construct paths analyze validity of PS
and and similar so let's see couple of
demos uh typical things that we often
might want to do is like creating a
directory structure then appending text
to a file and then checking if a file
name contains valid character vors so uh
without regular Expressions so I will uh
start with a new
demo so uh I start with uh creating a
directory structure so I will
declare variable of type directory. net
I don't think I have actually exported
it here in my cheat sheet oh I
have so so I'm declaring system.io
directory and let's take a look so it
has this method called create directory
and it accepts a path that I want to
create uh please see that uh there are
no Constructors in there so what does
that mean if there is no Constructor on
a class it means the St the class is
static which means you don't have to
instantiate you can just start calling
its methods so here I will do just that
I will go and call this create directory
and then let's
see what do I have in my
dis just let me take this thing away uh
so here I have this temp folder which is
blank so imagine that I want to create C
Temp and then
subdirectory and one more final one I
promise and then leave it there
so you don't even have to recurse
yourself as you would have uh to do in
for example shell in older days so I run
that and let's take a look did it comply
so I have subdirectory one more final
one I promise simple and now let's let's
append some text to uh to a file so here
I will declare variable of of type
file.net I will just quickly change
directory into
file and let's take a look at what file
can do for us so it has append all lines
for example and append all text so
depending on what exactly we want to do
uh we may use one or another so I will
start with this append all text so I
will say file. append all text and then
specify the file let me take a file from
this directory
and then call IT Tech days.
dxt and what I'm pending here is hello
world oh yeah it should not be called
file let me call it net file it's not
that I like Hungarian notation but makes
it simpler so let me run this
I run this piece of code and the file
appears you see create directory didn't
fail for me because directory is already
there why should it fail because the the
purpose of this command is just to make
sure that directory is there with the
full path that you specify and here I
have this Tech days hello world and if I
call it again it will append the text
here so another hello world I could if I
wanted to I could insert line brakes
it's up to you whether to insert or not
so
uh that's how easy it is to handle files
and finally the last one how to check if
a file name contains valid characters
this is also something that you
frequently have to do like in any setup
page where users have to enter file
names you have to check if the file name
is actually correct so let's do that uh
as well so here I will declare one more
which is called
path.net and it's of system.io do paath
type
so it
has
this method called just a
second to minimize not close so it has
this get invalid file name characters so
this path does not check if the file is
valid but it tells me which file
characters are
invalid Okay so
uh obviously I will need an array here
so let me do that I will declare an
array so
array.
net let me take the array from
here array of invalid
cars so I will say array of invalid cars
is path dot
actually let me just do it like this and
get rid of One path get invalid file
name course and then I will use the
string type to actually verify if any
string like for example here I will have
Tech file name which will be text and I
will have string which will be do net of
type system. string
so file name is is this a valid file
name Dot
dxt and then
message
is
valid so here I will print the file name
and then let me check H how do I verify
if I if uh if this file name contains an
invalid character I just go and call
string index of
any so this index of any tell tells me
the first index of any of given array of
characters so I'm looking for index of
any and then array of invalid
cars
okay save that uh
sorry larger than zero
so I will run
that and it tells
me
oops sorry let me
see yeah I didn't I didn't specify what
string is string is file name y so I
will run
that and it tells
me
that is this a f valid file name it says
yes don't expect
that yeah I will I will uh
put this back slash equal and
colum yeah
yeah yeah yeah sorry that's true
thanks so I'll run that
and it says this is not a valid file
name let's see if it can actually detect
a valid file
name is this a valid file
name and I run that
uh I'm I'm obviously missing something
obvious I will fix this and when I
upload it to my blog it will be correct
so yeah
so it should be like this if it yeah
exactly this should be let me see run
that this is valid yeah
and here I put a back slash and the
column
and no yeah okay that's true I
keep thinking in CL terms
where zero is strings are one based and
net they are zero based uh okay I
intentionally did not prepare any demos
I wanted to do everything here so that
you can see how easy it is to write net
I didn't want to appear with like aund
of examples and then just show them like
this is how to this or that and
obviously yeah I make mistakes anyway uh
let's move on let's uh move to another
typical thing that we might need to do
as uh as CL
developers and especially as Erp
people have you ever had to handle dates
or numbers in different formats and not
being sure like which format that was
like importing text files and then like
you are importing opening balances for a
new customer and then suddenly some
numbers seem to be multiplied by
millions some by 10,000 some by hundreds
so it all depends where dots are if
there are any spaces inside what are
spaces etc etc etc so uh CL isn't
particularly good at handling uh date
time and number information in different
uh cultures as we call them in net so
when you run CL C code it understands
your own local culture which is your
local Regional settings in in Windows
and it can interpret numbers in that
culture if you want like for example
your decimal separator is coma and you
get a text file which has decimal
separator as dot you will not be able to
interpret it correctly so depending on
what dot means in your Regional settings
it might work by multiplying numbers not
really randomly but it appears random or
it might fail all together so you would
either have to ask the customer to
supply the files with a different format
or you could just ask them okay what is
this format that you're supplying in and
if if they tell you in net you can
easily fix that because in net you do
not have this problem in net as long as
you know which culture the format
belongs to you can interpret numbers
and and dates so uh let's just do a
quick demo what I'm going to do is I'm
going to show how to uh read formatting
of numbers and dates in different
cultures so here I've cheated a little
bit I've prepared a page so this page
has three Fields the first is called
culture the second is called text the
third is called result result is
non-editable and then I have just put a
one actually three lines of code in the
validate uh trigger on the culture field
so here I'm essentially creating a
culture from users's input and then I'm
clearing the result and text everything
else is uh I'm going to code now so what
I want to do is essentially when the
user let let me run the page so when I
run the page this is what I get three
Fields my idea is when the user enters
the culture name like en nus and then
enters some text that here in the result
we see uh that text in the correct uh
actually interpret it correctly as date
or number
okay so to do that I will declare
actually I do have certain uh certain
variables declared I have date time and
I have decimal actually I don't need
those those experimenting so uh here
this date time and decimal they are net
date time and net decimal uh apart from
being able to hold a
number they have a a very interesting
function called parse so if I take a
look
at decimal and then parse it can accept
a
string it means piece of text and it can
translate it into a valid datetime or a
valid decimal and it it works similar as
the evaluate function does in CL however
it can accept an additional parameter
which is the culture actually it's uh I
format provider interface which is what
every culture info class has on itself
so essentially if you create a culture
info based on the identifier and you
pass it into this parse uh method call
it can translate essentially any valid
date or number format in that culture
into normal date time variable or
decimal variable in Cal so let's do that
here I will start with uh dates and
times so here I will say result
equals and then date time sure I can
type
it date time. parse and then this text
and I'm passing this culture info into
this
method so I'll save again um
I need to format that of course because
I'm I have this result which is
text so I will run that and here I will
start with a
simple like nus and here I will parse
the following text
so so it parses this as 1st of January
of 2014 this is simple this is obvious
let's start with some uh some funny
strings like for example I will take
this you will see immediately what it is
if you
cannot so I'm
using uh E lgr I think that's the
correct
one let me see yeah so e lgr stands for
Greek in Greece Greek language Greece
I'm pasting this Greek text and it tells
me what what this is so it can actually
really understand any kind of format
which is a valid Greek format in this
specific case or I can start with uh I
can take a
Russian so I can take this and then I
can say Russian Russia and then paste
this and it gets interpreted as a
correct date time also if I do that with
with numbers it's essentially the same
thing so it's uh only more common that
you will have to interpret those so I
will start with result equals format
decimal. pars and then text culture
info so I'll run that and let's start
with
RM C it stands for Roman Switzerland and
then
this number format so it's an uncommon
number format essentially it reads that
I can take an even more Uncommon number
format such as for example okay this is
fairly common actually so it's Norwegian
I'm I'm skipping Norwegian but I'm
taking this fary Iranian which uses SL
as decimal separator
so is it f a r yeah and I'm pasting this
number and it correctly interprets it as
as the number so essentially uh those
built-in functions in net obviously can
help you with a lot of typical tasks
that you have as a developer needless to
say you can use the same way like
formatting you can call two string
method and then show the data in in in a
specific culture or a specific language
easily so if you want to for example if
you're if you're selling internationally
you can and you need to send an invoice
let's say uh to Iran and you need to use
this Iranian number format then you can
actually have your numbers formatted
correctly it's not just that you can
have a language installed for them so
that it can print be printed in that
language you can also now format the
numbers and dates in that language so
that it's fully understood by that
culture
um let's move to the next topic it's
streams who uses streams regularly like
daily okay but they have not as common
as as text and as other things but
occasionally all of us need to do
something with
streams streams allow us actually
streams are very simple because they
allow us to handle binary data
regardless of the storage medium so in
calal or in in na natively we can handle
storage mediums of blob files sorry blob
fields or storage mediums of files and
uh net has more it can even have a
stream which is unrelated to storage
media also in Cal what we have is two
kinds of streams uh in input stream and
output stream whereas net doesn't make
that difference at all net uh actually
says I don't care if you input or write
you can have a random access stream but
you can write and read essentially you
can read and then manipulate the data in
that stream and then pass it on for
further processing so this is how net
approaches streams and also it has
different types of streams not just
based on uh like file stream for
handling files it can it has for example
compressed streams that can compress
data Etc so there are many different uh
kinds of streams Inn net nice thing with
streams is that they fully map to CL
streams so it means that just the same
way I use my string variable
interchangeably with text and I was
assigning text constants to string
variables um you can do the same with
streams so any in any place where we
could use uh instream or outstream
variable in CL you can now use this uh
memory stream from uh sorry any stream
from net I'm I'm mentioning memory
stream because it's easier easiest to
use and I will do some uh demo uh demo
here for example I'm going to download a
picture from the internet and I'm going
to store it in a blob
field so let me try
to
download now have Tech days actually
so this is a good
one so I'll take
this uh let me write some
code so uh
first how do I read a picture from
internet I don't need a stream for that
obviously what I need is I need a class
which can download data from internet
there is a class in net which is called
Web client so I'm actually calling to
declare this web client
class
so web client.net and then system. net.
webclient I will start with
instantiating this web client so I call
it
Constructor the next thing would be to D
download um to actually download this
image that I've found on internet uh to
download an image I need to pass the URL
it's not just a plain string uh URL is a
class so I'll take this URL class
and here I'm actually it's URI class
it's system. URI so it's URI
is I'm constructing one again I'm
calling it Constructors I'm const
constructing it from string and here I
will pass the address of the image that
I've just found on internet so it's this
one I'm pasting it
here and then the next thing is to
download this image let's take a look
how do we download so I'm zooming into
this uh web client class it has download
data this download data it returns a
bite array bite array is one of the most
common types of arrays in inet when
handling any kind of data you will
you'll just need to use it a lot and a
nice thing with bite arrays is that it
can be easily turned into a stream so
you have array of bytes which is
essentially binary data that you have
downloaded you can just convert that
directly into a stream so let's take a
look how to do that next step what I
need to do is a stream to store this
Spiner information in so I will declare
uh memory stream so it's MST
stream.net I think I don't have this one
oh I do
so this is my memory stream it's system.
i. memory stream type so I will just say
mem stream is should Now call the memory
stream
Constructor and I will pass this byte
array uh when I was detecting invalid
file characters I have I have created a
variable of type array of invalid
characters in net you don't have to do
that actually I could have skipped it
there I'm skipping it here intentionally
so I don't have to declare a variable I
can directly call the method web client
download data so it downloads the data
and returns it as binary stream uh as as
a array of character byes so here I'm
just passing this URL and essentially
here I have a memory stream which
contains this image which was downloaded
from the internet the only thing I need
to do now is essentially to store it uh
in the database let me
use for example
item
1,600 so I'll declare
item very good
item so I'll do item
get I'm getting this item and then I
have uh item.
picture. create out stream I need an
output stream to write into which means
I need a stream variable so I will
declare an
outstream variable so again let me zoom
in it will be simpler
so here I have created an outstream so I
have a stream that will allow me to
write into my blob and I have my memory
stream so what I can do there are two
things I can do first thing is simply
copy stream
and then say that I'm copying into outre
stream from my M stream so this will
compile okay other thing will compile
too so I can do
mream do copy to and then out
stream both will work okay and then of
course I need to do item.
modify so if I go to my item now and
take a look at its picture it should be
blank so picture is
blank then I run this small piece of
code nothing seems to happen but when I
click this there is an a tech days so
this is also a very simple example of
how you can uh use streams in net how
you can use streams in scenarios which
are kind of unfamiliar to us but
somewhat
common so essentially uh this binary u a
bite array is something that you will
get for many different types of data
like for example from accessing files
you will get bite arrays you can get
bite arrays by uh using encoding for
example if you're using different
encodings you can switch between
encodings like we have text in Windows U
let in one code code page that you want
to turn into for example a utf8 code
page you will use B rates for that as
well also I will use B aray in my next
example here
so one common thing is to change between
data types such something like
converting uh let's say strings to Tech
uh to to integers or integers to Strings
etc etc we have evaluate in uh CL which
allows us to
translate text into anything or not not
really anything any simple CL type like
for example string to buan string to
date time string to decimal Etc uh in
net we can convert literally any value
uh built-in value type into any other
built-in value type so this convert
class is really evaluates Big Mama
because it can really do um anything let
me just declare this uh
variable so I will start with demo 7
and of course
demo
7 so here I will declare
convert.net I don't have that one so I
will just declare
it the regular way so I'm going to
mscore lib and here I'm looking for
system do
convert there it is
so if I take a look at what convert can
do for me essentially let me Zoom so I
can convert to Boolean and then it has
all of those overloads like from decimal
to Boolean from date time to Boolean etc
etc and then it has that for all
built-in simple data types like U common
thing is like converted converting for
example from integers to booleans it's
something that for example U cbas
languages do natively c fails set so you
cannot convert like they are just
incompatible you can use this for
example like zero would be false uh non
zero would be true so this is uh this is
an example of this convert class why I
find this class really interesting is
not those convert methods which are
occasionally useful uh why I really like
it is because of these methods it has
from Bas 64 string and to base 64 string
let me see who has ever needed to do
something with Bas 64 okay Bas 64 in
essence is the mechanism which ensures
that you can put binary data or or
convert binary data into text in such a
way that it can be transferred easily
over internet and unambiguously so it
was one of the reasons why it was
invented was for example the pop
protocol or SMTP protocol for handling
emails when you attach an image to an
email what happens in the background
because this is a a text based protocol
it gets converted to base 64 what it
means is that you take binary
information and instead of chopping it
into eight bytes you chop it into six
bytes and then you have 64 possible
values and then essentially uh each of
those 64 possible values maps to s key
character which means that you get
binary data which is larger in size size
than the original one but is textual in
such a way that you cannot miss it
doesn't include any funny characters
like any local characters in your local
homepage or any system characters which
could confuse the clients so this is Bay
64 you can use it for simple encryption
because regardless of what you encode in
Bay 64 it always does the same algorithm
and it always looks encrypted even if
you put text which is text like plain
ask it will still appear encoded so it's
a very useful thing to do and uh now we
can do it easily with uh with net with
this space 64 so what I'm going to do
here is I'm just going to take this
picture that I had uh downloaded right
now and I will encode it as Bas 64 and
then save to a file so here I will start
with um
item again I will get
this item I will do item C fields
picture just in case I get the wrong one
okay so I'm getting this picture now I
need to get this data out of this um uh
out of this array uh sorry out of this
blob let's take a look
this uh two Bas 64 string if I take a
look at this two base 64 string what it
accepts is a by array okay so again our
old friend so let's do this let's
do convert to base 64 string and then we
need to pass a bite array from this
picture how do we do that again we use
streams here I use instream
so I will
do item picture create in
stream and then in
stream and what I need to do is I
essentially need to convert this
instream into by array how do I do that
because if I take a look at the instream
variable
it doesn't have any methods but I know
that memory stream does so what I can do
is I can declare uh mem stream which
would be a
net let me just quickly hack it here io.
memory
stream so I will just do a simple
assignment mem stream equals in stream
okay
and then here I can do mream and then I
can call the get buffer method this get
buffer method gets the bite array out of
the stream and here I have this string I
can actually declare another known one
so
file.net
system.io do file
and I can write file. append all text
and then C
temp
image.
dxt and then I'm
pending
this me see what's the error here yeah
right
and file will have the same problem
yeah
so net
[Music]
file net
file if item picture has value so let's
take a look it should write something
into my temp
folder so here
I will run this and wait for okay I get
an
error let me just do this then
don't know why
but I'll I'll stop there really uh have
26 minutes to go I will return to this
demo when I complete other important
ones I uh
sorry didn't I do that I did oh you mean
C fields versus has value I've blogged
about that couple of weeks ago actually
you should do in you could you should do
that in nav up to version 2009 I think
and then they switched it which makes
more sense so cul Fields takes
everything from the database and if you
just want to check then you do Cal sorry
has Value First this is not the problem
the problem is
uh somewhere in here so it's
um it's um oh me stream is stream.
memory stream thanks whoever that was
yeah I didn't instantiate my stream but
I'm not quite sure if that will it it is
okay thank
you obvious thing so here is my B 64
encoded image
okay so this is again some useful uh
functions from U from net and now we
stop with
cl uh we move into Visual Studio let me
see who has never done anything in
Visual
Studio okay a few of you so that makes
my job easier because I don't have to
explain far to much so I assume most of
you know how to create uh
assemblies uh the reason why we use
Visual Studio even though we could
obviously do most of the things from
Pure CL and I really mean that there is
very small portion of net which is not
really accessible to you uh from Pure
CL uh the reason why we would still want
to go into Visual Studio is when you
need to use some of those features which
are unavailable for example delegates if
you need to use them the only way is to
create your own assemblies and then use
them from
there uh there are other ones for
example
Performance net code when written as C
executes faster than net code which
results from you writing Cal and then
that being converted to C and compiled
take a look at the code of any any CL
converted to C and you will immediately
understand why for those of you who are
beyond the mere mortal level basically
those who did not raise their hand it's
uh the reflection because it's all over
essentially uh no single Cal line of
code that uses net really calls those
objects and those methods or accesses
those properties that you think you are
accessing it actually uses reflection to
do everything and it makes it slower
because it always needs the first check
can I do this uh it needs to locate the
method by name for example it needs to
construct U arrays of parameters
essentially it has a lot of overhead
probably you will not feel it but this
overhead will still be there it will
still slow things down so if performance
is really important then it might make
more sense to Simply go into visual
studio and write your
assembly so uh let me just create a
quick assembly so I'm going to visual
studio I'm creating a new
project so here in the projects list
depending on your language choice you
will select that language and then you
will select windows and then class
Library uh class libraries are compiling
into dll files in uh net jargon we call
them uh assemblies so I will just create
a tech days20
the 2014. mere
portals so this is the name of my
assembly when I compile this I will get
techday 2014. morals.
dll so uh when you create a new class
Library you get a c or vb.net file which
is called class one so here you can
write your class so I'm just going to do
a simple class here so I'm not going to
explain the the objectoriented uh
development in C or what classes are I'm
going just to assume that you know
enough to be able to follow this code so
uh I'm creating very simple class I will
start with calling this
class person and then person has public
string name actually first
name then public string last name these
are now my uh first and last and let let
me add one more public date time
birthday okay there is no date in net so
when I build
this what I get
is a DL file so I'm opening this file so
right
click then open folder in file explorer
and then bin debug and here I have my
tech dayme
morals. before I can use this from
nav uh I need to deploy it first
deployment is simple so I can I need to
take this file so I'm copying that and
then I'm I need to move it into actually
copy it to C program
files then Microsoft Dynamics
NV then 80 then service
then
addins so I will paste the file
here at this
stage I will create a new
so demo
8 if I go
to uh my globals and declare person of
type. net if I go to subtype
here in the server tab in
2015 I will see that I have do Tech Days
2014 M
Mortals so I select that and here I can
see okay I don't see the class I didn't
expect that I expected something
else let me see why not is this class
not
public it is public
no definitely not definitely
not so I
will let me see without the zoom it's
easier for
me it's not there I will
close I will close
my development environment because once
you load a dll and once development
environment locks it you cannot access
it anymore so I will uh just save this
and I will close this so public class
person it's in here build rebuild
solution
succeeded I'm going back
to my folder so it has just been
compiled I'm taking it again
and here I have addin
server I will pass it paste it here
actually I I think I have an explanation
for this I will paste it also in the
client folder because that's where uh
the client folder is where the add-ins
reside uh for uh for the development
environment so it seems to be the Mal
functioning autod deployment feature of
uh net sorry uh nav 2015 so let me go
again into my demo number eight so
here's this person. net
and now I I'm going to Dynamics NV
Dynamics NV is essentially my client
folder so here yes I see it here I
assume that it is it has to do with
autod deployment feature it doesn't
always work so I've heard that for auto
have you heard of autod deployment of
dlls in in 2015 sometimes it works
sometimes it doesn't not I've heard that
if it starts with Microsoft Dynamics
then it automatically upgrades even
though documentation doesn't say so here
I assume this was the reason why I
didn't see this class so now I see this
class here and I can start using it I
will immediately notice that even though
I have declared those first name last
name and birthday I don't see them here
they are not properties they're actually
Fields so I don't see them there and
we'll get to that pretty quickly so
this was just how to create an
assembly now some best practices that
I'm going to give to you I'm not going
to teach you today how to create or how
to develop in C or how to develop your
assemblies I will assume that you know
enough of net or C to just go there and
write some code that you need to uh to
have uh execute uh from within CL I'm
going to talk about deploying assemblies
to Global assembly cache and the
benefits of them of that approach uh I'm
going to talk about how to declare
properties as opposed to fields which is
what I've just done also I will teach
explain you to you how to make classes
serializable what it actually means and
why it is necessary and also I'm uh
going to just mention interfaces and
then I will invite you to the PRS
session just after lunch in uh in the
big room where I will demonstrate how to
actually uh make use of those interfaces
so let's talk about those best practi
IES first Global assembly cach or gak
this is a machine-wide repository of
assemblies uh and it essentially solves
several problems with deployment of dlls
that were commonly called dlll hell in
the old days of uh of automation uh and
win32 uh so to put an assembly into
Global assembly cache you need to sign
it with a strong name so essentially uh
it it has to have a qualified and a
unique unque name that only you can
guarantee that you can change or assign
so essentially once you assign a name to
to to an assembly a strong name to an
assembly it's only you who can change it
or who can guarantee that it is that
assembly so it has a very strong
security um effect because nobody can
actually temper with your assemblies
like for example in the old days of
win32 you have a dll like automation dll
which exposes 15 objects and these 15
objects have each five functions so what
you could do is essentially develop your
own dll which has the same 15 objects
with the same functions for each of
those objects and simply exchange put
your DL in place of their DL and
suddenly your code executes because the
application has no way to know whether
it's your code or their code or
whichever code executing it is basically
the back door for all sorts of viruses
Trojans Etc in net it's not really
possible possible it's it would be very
difficult to uh to do similar thing with
assemblies deployed into Global assembly
cache so uh it is always a good practice
even though for for Global assembly cach
it is a prerequisite to sign the
assemblies with a strong name uh for
regular assemblies this is not a
prerequisite you can just write an
assembly just as I did and not deploy it
to Global assembly cash not strongly
sign it and then anybody can temper with
it so it is a good practice to sign them
always even though if you don't attempt
intend to put them into Global assembly
cach so if you always deploy our
assemblies to Global assembly cash it
will force you to not forget that you
didn't sign it so that's one of the
reasons uh why deploying into Global
assembly cache is good the other one is
it simplifies development so for example
here I have first deployed it to the
server folder then it didn't quite work
then I deployed it in the client folder
and then it worked but had to restart uh
the client sometimes you might need to
to restart the service tier with the
global assembly cache it's simpler so
yes you will still have to uh to restart
uh the service tier sometimes
development environment almost always
but for most situations you don't have
to copy it into multiple places and also
it's it's very easy to deploy to Global
assembly cache so let me demonstrate how
I can put this assembly into Global
assembly cache and what what happens
then so to put something into Global
assembly cache you need to to run this
uh development environment and here you
have a utility called gak util so gak
util actually takes your dll and stores
it into Global assembly cach if it's
possible so what I want to do is I want
to call this gak Ule from my visual
studio so here I will take a look at
properties and then I have build events
so I use post build events to actually
deploy my assembly into Global assembly
cache so here I have to write gak
util minus I which stands for
install and then I need to put the name
of the assembly which is essentially the
dll I'm not hardcoding it I'm simply
using a macro command which is Target
path I can check those macros here if I
click edit post
build then this target path it's
essentially the dll full name so it's
the the name of the dll plus path so
when I uh when I put it into Global
assembly cache like that it essentially
just takes this DL and stores it there I
will also use minus F which means uh it
means Force the reinstallation even
though the assembly is already in there
uh I cannot just call that so before I
can call that I have to do at least one
thing first is I need to reference the
path of this gak util so uh the easiest
way to reference the path to gak util is
essentially to just take this shortcut
so I'm opening the file location then
right clicking here properties and then
taking this target box and just pasting
it in
here so I need to clean it up a bit so I
will expand this so that you can see
what I'm
doing so I will zoom in zoom in once
more and since this is not a command
prompt I need to take this out and I
just need to put call and I need to take
this last quotation mark out and then I
will click okay so when I
build this
solution okay I I got an error so it has
failed the yeah uh there are two things
I need to do first is I need to fine so
it if I take a look at this output it
will tell me that failure adding
assembly to the cache because
administrator permissions are needed so
it's not the prence problem it's
actually another one so to do that you
need to run Visual Studio as an
administrator so that's the first thing
I will do so I will close visual studio
and then run it as admin
then when it starts it will fail again
because of the other problem
so here I'm opening my uh M Mortals
demo and I will build the solution and
now it will again fail and it will tell
me that it fails because assembly is uh
requires a strong name so this is if you
remember my slide essentially if you do
this like that you will never forget to
assign a strong name it's always a good
practice for assemblies to have a strong
name assigning a strong name is simple
you just again go to Project
properties select the signing tab click
sign the assembly and then either use an
existing file that you use for example
to sign all of your assemblies or you
create a new file I'll call it Tech
Days 2014 M Mortals I will not protect
it with a
password and then I will rebuild my
assembly my solution and it tells me
that assembly was successfully added to
the cache if I take a look in my
development environment I will declare
person
2.net and then if I take a look at this
list I don't need to go to Dynamics nav
I need to go to net tab this is the
contents of the global assembly cache
and here I will
find Tech Days
2014 Mir Mortals
so it's there if I click that it has
this person
class one caveat these two are not the
same class anymore so they are two
different classes these are two
different DLS actually
so it's best that you first sign then
use so I will delete this first
one okay
so this still didn't expose my first
name and last name and birthday so I
need to do something else so this is the
first best practice that I have for
you the second best practice is just
declare everything as properties it's
easy because CL understands
properties uh CL does not understand
Fields what are Fields fields are simply
variables declared directly on a
class whereas properties are not
variables there are in essence they are
methods so when you have a property
called first name you will have
accessors or access methods if you want
a get access method and a set access
method so when you assign a value to a
property the set method is called and
when you read a value from a property
the get method is called so properties
are essentially methods uh this does not
explain though why nav doesn't expose
them why you don't see them that's
really strange decision by Microsoft
they probably fix that because I don't
think there is any U drawback to that um
yesterday at my session at my precom
session I have shown how to access
fields from clal though and the example
is on my blog so if you want to access
field it's possible it's just a little
bit tricky you need to to call some
reflection but let's see how to do it
the the right way how to fix it and how
to
actually expose those first name last
name and birthday as property
the old schooled way would be this for
each of the properties you would have to
have a private member or a private field
so private string first name for example
so this would be used to store my first
name and then I would have get access
method and I would say return first name
and I will have I would have a set
access method which would be first name
equals value so this is the old school
way to declare properties and it's also
the right way to declare properties if
your access methods do something else
other than just assigning a value or
reading a value so properties are nice
because you can easily take and access
method out and make it a readon property
or you can take get method out and make
it a write only property if you want so
this this is how to implement a simple
property however there is an even
simpler way there are Auto implemented
properties that's a feature of C not
quite sure which version three or two so
instead of just writing the access
method you can just say Get
Set so you're telling which accessors
you are exposing and the compiler does
essentially
this for you in the background so when
you compile that this is what you get so
these are just Auto implemented you
don't need to write anything code so
essentially I don't need
this uh this I will just say public
string first name and then get and
set and also the
birthday I will add get and
set so I will now rebuild my
solution so it is again added to the
cache it doesn't show immediately
because my development environment has
already loaded an instance from a global
assembly cache it does not check if a
new one is deployed and then rereads it
so I need to close
it and restart
it good uh let me go back into here and
here I have my person and now if I take
a look at properties I have birthday
first name and last name and if you ever
Wonder like why it's uh why you don't
see properties that you expect to add
it's probably because you just declare
them as as Fields if you want to use
something from nav if it's public then
just make it a practice whenever you
declare a variable just add this get set
and you're good to go so from CL uh
sorry from C you have no problems
accessing fields fromet from CL you will
so it's easier if you simply just
declare them as uh as properties right
away
okay now serialization this is an
important process serialization is a
process which allows you to have one
class then essentially store its current
state to be able to restore it later so
uh you might think like why do I need
that typical example is just going to uh
to come right now so I'm going to
immediately start with them we are short
on time so I want to show the problem
with this so here I have person and I
will instantiate this person and then I
will
assign first name
John last name do so this is running on
the server side
okay now I will declare a person to
which is going to be net but I will say
that it runs on client
okay it's going to be the same
type
so if I do
this which is perfectly
legal and I attempt to run
that my client gives me an error message
which says it failed to
serialize what is happening here I have
service here on one box and then I have
client on another box I cannot just
assign a variable which lives here to a
value or a reference in this case which
lives there so before I can do that
because semantically my Cal code should
continue executing it doesn't care which
domains these variables exist in so what
it needs to do is it needs to take this
instance from the service server box and
somehow transfer it here so that I have
the same context in there as well so to
do that server needs to realize that it
means turn it into XML or binary or Json
or something
else ship that content over the network
to the client and then deserialize it
and essentially have a clone of the
original one but allows me to get the
same context that the original one had
so how do I fix this error it's very
easy in fact so here I will just stop my
service deer and stop stop my client
so I have have one more minute to go
which is exactly as much time as I
need so I'm restarting this and I'm
going to restart this as well back in
my C I just need to add the attribute
called
serializable that's all
so I now rebuild this
go back to development
environment and here I will do message
person
sorry person 2. first name plus space
plus person to
do last
name and I run that
okay my time is
up let's uh let's wait this uh client to
wake
up so it shows me this John do okay so
uh my point here
is routinely just add this serializable
it costs nothing absolutely nothing it
doesn't make a class slower it just
allows it to be serialized when
necessary when not necessary it doesn't
have any effect whatsoever okay and I
have one more topic to cover which is
not that important that's why I left it
for the last which is
interfaces interfaces enable like real
polymorphism it enables your class to
take any necessary shape of a behavior
that you need for example this
serializable here I have by adding the
serializable attribute in fact I have
implemented the I serial I serializable
interface which allows this class to be
serialized so whoever needs to serialize
can observe this class only as the
interface so uh I'm going to show the
real power of that uh today in the PRS
session so if you want to see that
please join us that's not the reason to
be there there are many many more
reasons uh to join that session but
among other things you would see how
interfaces allow you a real flexibility
with handling uh uh with handling net
interrupt and
objects so thank you for uh attending
this session I hope it was
useful are there any questions no thank
you yeah we have a question here there
should be person yeah
so the question was are there any
dependencies when using net interrupt
with other client types such as web
client tablet client possibly Etc in the
future if you're using servers side.net
which is everything I have done so far
until I had declared this person to
variable no dependen is required so this
works equally well on all all uh client
types because this is hand happening on
the server however once you declare
client type uh client side yes then it
only runs in the windows client so you
cannot even make it run in in the tablet
client or or or the web client so you
should actually not
use uh clients side.net interrupt you
should avoid it at if at all
possible okay uh actually there is a
shirt for you
so I I'll just try to throw it strongly
there okay good
catch there are more shirts so please
ask questions otherwise I will have to
wear them
all yep
um yes another
question um so the question was about
exception handling like there there is
problem in C how to handle exceptions
because net is really allows you a lot
of exception handling I will I will get
back back to that that question just
just immediately so uh in fact there is
a workaround I've also blogged about
that my I think last or one before blog
post has a trick how to use exception
handling uh which is limited to you
being able to handle exceptions that
happen in net it requires an external
dll but it covers all of exception
handling scenarios
then in essence in 2015 you get get last
error object so if you have if code unit
run and then it fails you can get U last
object which is system do exception or
whichever descending class it is so it
means that you could at least you could
not have try catch stuff in uh in CL but
at least you could analyze the exception
and see what exactly happened and you
can get the context of the exception but
the answer really to your question is no
we don't have any kind of exception
handling any real exception handling in
in net interrup and if you expect
exceptions then you really need to write
your wrap your stuff in your dlls and
deploy them there was a question
somewhere over there yes here uh usually
you do not develop on on server I guess
so uh when you deploy your dll to the
GSC uh do you also have to do this on
the server side and with the same GSC
youtil or exactly you have to so uh here
I was working on a single machine and on
a single machine deploy deploying to gak
solves those scenarios I don't have to
deploy it twice this is one of added
benefits of adding it to gak When
developing uh when deploying uh when
deploying dlls in production
environments you do not get any
significant benefit from adding them to
gak but you would have to add them
separately on the server end and on all
of the clients this uh Auto deployment
feature does not work if the assembly is
in Gag so if you put the assembly to gag
then autod deployment will not work even
though it doesn't obviously seem to work
in all other scenarios as advertised but
I'm pretty sure that the next cumulative
update will take care of
that or I
hope uh any more
questions yeah yes I have one um is it
possible to um debar the C sharp code um
when we start uh the program uh in
dynamic a so that we can hop to okay yes
it's possible essentially uh what you
need to do is you need to start Visual
Studio as administrator then you go to
debug attach to
process then you need to make sure that
show processes from all users is
selected and then you need to find
Microsoft Dynamics server. exit there is
the shirt for you it will arrive shortly
uh if you're uh debugging client side
then you essentially need to attach the
debugger to the client okay and you can
attach to both simultaneously so and
then you can set break points and it
will just stop when it hits the
breakpoint and you can access your um C
code of your net
dlls yep okay do you have any solutions
for casting for type casting actually no
typ casting works completely fun not
possible um here's your shirt that's
that's an excellent question so uh there
are a lot of issues with tight casting
because what like uh C or net allows you
to upcast variables like you have a
descending class which you can assign to
an upper class variable in CL you can
downcast you can crosscast you can do
what I don't even have a term for like
you can cast completely off the the
hierarchies so essentially Cal has tons
of problems with that and essentially
you cannot directly cast you depend on
the
runtime to to resolve those issues or to
pinpoint those issues so there is no way
that Cal can help you at compile time
detect typ casting uh errors
exactly so if there are problems with
typ casting you would have to write an
assembly I mean normally you would test
your program you would figure out if
there is any type casting issues also
what you could do is you could use
reflection and system. type class to
actually verify if the the types are of
correct types before assigning uh
variables however there is a bug there
which uh again it's it lives in my to-do
list for my blog essentially you you
cannot call on system do type there are
methods which allow you to check the
hierarchies to see if something descends
from something else or if something
implements an interface they do not work
well they they always return false so
it's funny but yes if you really depend
on casting heavily then just wrap it in
your C and deploy it as
dlll I think I have more
shirts these are PRS shirts though but
they are equally as as good I promise
you
so blame look he only gave me five
shirts for so okay can we use Visual
Basic or C++ as well to create these
Dees Visual Basic C++ F whichever is on
the net yeah
delnet whichever language that compiles
into valid net assembly you can use it
and is there any like visual studio
version as well like we can use 2005
2008 uh essentially it doesn't matter
which Visual Studio you use it matters
which uh version of net interrupt you
produce oh sorry NET Framework you
target so with nav 2009 you have to
Target version 3.5 with 2013 and upwards
you can Target 3.5 and up so it's there
is a there is a shirt for you let me
just throw it again let's see who is
better me okay
sorry uh just one uh one disclaimer
about PRS shirts they come in different
sizes so if size doesn't match like
contact us the PRS folks especially Mark
bruml he is here in the front
row yeah so he can give you a matching
shirt yeah uh any more
questions yeah there is a question over
there uh I didn't quite hear it it
was how best way to consume web services
so if you ask me actually uh come to PRS
session today it will explain the best
way there are several ways one way is to
go to net declare actually reference
your web service get the proxy
classes actually this is the easiest way
and then just deploy this dll and call
them from na you will have problems
there the best way would be to actually
wrap them into wrapper classes which
allow you to call web services okay so
it's a much better way because then you
do not depend on whoever is on other
side you actually have your rapper which
exposes an an expected set of properties
and methods to your consumer which is CL
in this case so that if something
changes on the other end you don't have
to change a CAL code so that would be
the uh the best way
but I also have on my blog a demo how to
consume web services from Pure Cal which
essent actually constructs the proxy
classes compiles them in memory loads
the assembly and then allows you to call
into it through reflection I don't
recommend that way it's there just as a
pure trick I don't recommend that
because it will have you will be able to
do exactly the same as with just exposed
proxy classes so all of the problems
that you would get would still persist
so the best way would be to to actually
wrap it away in um in a dll and then use
it as essentially Define your own
interface to the web service and then
call into that
interface okay did you get a shirt
okay I have more
shirts lunch yeah I know it's lunch but
this is so
interesting okay oh there is a question
yeah yeah
cool is there a way to to use the DLS
you have in the addins folder to use
them in reports from
LLC oo can you can you repeat the
question if I have a D in in the addin
soer MH can I use it from an RC report
or do I have G I think you need to use G
for that technically you know I'm not
really rdlc guy I don't know what are
the limitations of this language
whatever it's called in rdlc the
scripting language which which can
access net technically I would say you
can load this assembly dynamically and
call types in that
assembly however I never tried that I
wouldn't say it was supported but maybe
you should ask Claus Lor about that
yeah why are you running away there are
more
shirts okay uh I know that I I see that
I'm 30 minutes overtime
so just like this and then nobody
catches great yeah thanks thanks again
and enjoy the conference yeah
