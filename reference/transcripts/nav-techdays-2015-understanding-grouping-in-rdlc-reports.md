# NAV TechDays 2015 - Understanding Grouping in RDLC Reports

- **Source:** https://www.youtube.com/watch?v=-aXQPuCISzI
- **Video ID:** -aXQPuCISzI
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 83m00s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

so I'm on perfect uh I'm just going to
take a small picture of you guys so
could you please
smile
thanks perfect okay so I'm going to tell
you a little bit about reports uh I'm
Claus um lunch time and the people have
been in my session know that I love to
do a lot of slides so of course I have
around 800 slides that we have to go
through uh but the first one is this one
here is actually my second slide I have
eight slides so uh that's the only thing
I have uh I'm Claus uh I um yeah this is
I know a little bit about the reports
I'm an MVP uh I used to work for
Microsoft a million years ago I stopped
there about three years ago uh and I was
actually one of the guys that was
killing the classic
reports okay so um
yes I was not really uh yeah um it was
not really the decision I was really
happy about uh and but on the other hand
uh we we needed to move on and it was a
decision from high over that we had to
use RCV ports and CV ports of course
supports
everything yes um so we in 2009 of
course created the possibility to run
classic vorts in 2009 okay summercloud I
know a lot about reports now I said it
uh and I've done uh a lot of uh
trainings and I've actually think I've
been training over 900 people in the
channel now so if you're sitting here in
in the audience and you've been at my
training you probably shouldn't be
sitting here you should probably go to
the other session but that's up to you
if you want to have a repeat uh I from
continia so I'm not going to do any
advertisement about this but these are
the products that we uh that we are
going International with and enough
about that so next
slide you
ready as I don't like slides I want to
show the product so so let's do that so
just want to he uh just one just to get
some a feeling on where you are so
uh so how many people are still on nav2
the classic
reports
okay and out of you guys are still on
classic vorts have you done any
investigation in the into the adlc port
B ports or is this your first session if
this is your first session hands up you
know about corts okay so if one person
okay okay you're going to be busy uh so
you need to know these reports um um
okay who is on
2016 okay great so a lot of advanced
people also great perfect okay so let's
uh let's do a small demo about these
reports and I'd like to show tell you
about groupings oops let's get out this
PowerPoint get
away so what I'm going to do I'm going
to jump right into it and I'm going to
jump into the object designer which
we're all up I'm not going to do all
that much development on stage probably
I will but let's see so I've done one
little report here and it's not that
exciting report but it uh it creates a
it's a data item and it has a few uh FS
on this on this data item so I have the
customer and uh what I want to uh for
this report I actually just want to run
this report
here what I always teach in my class
this is a three days class uh some some
people think they can do it in one day
that's a little bit optimistic uh but uh
two days then then your hair would be
like this uh and so usually 3 days is a
good is a good time for doing uh getting
your hands uh dirty and understanding
the re all the ADC uh issues that we
have because we have a lot of issues
unfortunately Visual Studio is not a bug
free program
unfortunately and I have gone through
some of the box and tried to get them
fixed but uh none of them are getting
fixed so there's always a workaround
okay so that's what I probably said this
last year also if you ever come with a
service request to Microsoft
don't ever tell them there a workaround
let them figure that one out themselves
because if they see workaround where
they're going through all these box uh
they will uh they will just say you
that's a work will not fix this okay so
never tell them that and you won't get
your box
fixed so that's just a small tip for you
so uh what I uh what's important when
you when you work with C reports I I see
a lot of people just open up the reports
and open up Vis Studio I also see people
using reot Builder well don't use reot
Builder is a a very uh minimum tool that
we really can't can't use for for
nothing other than changing colors and
and and and deleting stuff but um so I
don't use Reaper Builder if anybody
calls me and they Cloud can we do a team
viewer uh i' like to have some help with
this report here and I'm ring up the
team viewer and they present report
builder for me I go on the top and the
right cor corner I click and I say yeah
call me when you're serious okay so
repop Builder is not something that we
work with
okay so what's important for these
reports here is that we need to
understand the data set so people go
into the visual studio and they start
attacking the report from there and that
think that they can then solve the
report and maybe sometimes they're lucky
that they solve the report and if they
do they sometimes end up with this
situation that ah it's working don't
touch it don't touch it anymore and they
walk away from this vort don't touch it
anymore anybody in that situation
yeah a few people yeah so you have a lot
of orts in your system that you don't
touch anymore because you don't dare uh
yes so I suggest that the first thing
you do is you go through look at your
data set so to do this we're going to go
preview and we I see this report is
completely blank I don't have anything
in this because it's not it's not the
layout that's important right now it's
this a data set so I'm going to open up
the data set this page is running model
so I'm going to close it immediately and
I'm going to go go to excel here in
Excel I can see my columns that I have
created in my data set in any in the
object Center so go back to the update
Center here you see they have two
columns see customer number the customer
name go back and here in Excel I have a
customer number and customer
name pretty simple you probably all know
this uh but I'm going to make it a
little bit more advanced so now what I
have here is it's just a customer uh
it's just yeah just can don't want to
see this in the more let's go away if we
go and open up the uh designer for this
open up this studio I am working in this
scenario I thought of should I do this
on uh 2016 and 2015 and I was like yeah
I could do that but why uh there nothing
has happened to the IDLC since or ID
since SQL show 2008
R2 okay nothing nothing absolutely
nothing okay so we have uh we have a
product that has been created by
Microsoft it's nobody is doing anything
with it right now so I might be very
unpopular saying this but nobody is
doing anything but they released it in
secet show 2008 out2 seet show 2008 out2
so that's 2010 they released that and
nothing has happened then nothing okay
so there no wonder why when you come
with a with a box to them they have no
idea how to solve this because they
don't have anybody working on it so uh
that's really great so this is a uh so
so I can live long on this uh because I
know a lot about this people I I can I
don't have to to to get into any new new
things around this because I can teach
this for years so Microsoft will not go
away without the CV ports they will not
do that okay it's been a lot of hassle
for them upgrading uh to the V ports
here and if they changed it uh I think
all Partners will kill them okay so it's
not going to
change and RLC of course has some
limitations but it also has a lot of
great things um so so let's just I have
a look at this report here so what I do
now is I insert a table and in this
table here what I do is that I put in a
few colors I always use
colors
always of course not when I hand this
and I uh I'm final with my report I
don't do this okay so of course I'm when
to hand it to the customer I don't I
remove all the colors because if I did
not do the colors so let's just do it
without the colors so like this save go
back save and
compile we
run and I look at my report hopefully
it's coming up ah it's running M so it's
open up another session this I'm
sometimes doing that don't want that go
away run it again control R so
preview and now I'm looking at the
report now I have borders on the report
but I did if I did not have borders on
the report I really couldn't see that I
had anything on this
report unless of course I put something
there but
let's have a look uh go back to the to
the reort designer here and we'll take
the uh color so we line this and let's
take actually we going to do this so
just undo the things and I that's it and
save and go
back and I know this is a very simple
scenario it will be harder later I
promise
you preview so do you see what happened
there I did much change and I was really
fast when I ran the vort so when that
happens uh I could sit and scratch my
head I don't understand why I actually
fixed the vort it's not working I don't
understand that so I go back to visual
studio and then I change it change it
and and I actually break it and then
when I come back uh to NV I do really
fast again and then actually I'm running
the the old version of the vort which
actually fixed and if I now run the vort
uh then I say I'm not happy it's now
fixed but I actually broke it okay so be
careful when you run your V just wait a
couple of seconds before you run it
because if I run this again it will be
the correct
version so preview and I have colors
okay so be hold your horses uh just for
a couple of seconds before you run so
now I can see that I have a table header
I can see that I have a uh and all my
detail rows and all the the hot pink
ones here is is going through my uh my
data set and here in my data set I have
68 customers in my database which is1 de
database we all know this I
assume so this was a very very simple
scenario so let's go and close down this
one here I want to go a look
at this
report and this is a little bit more
complicated
so yeah I don't really like cameras but
the
okay that's okay so so please take a
picture of me when I'm not looking
because okay so here I have a um I have
a data item uh the customer data item
and then I have a uh the sales lines uh
indented underneath here so really uh
also very simple and this is where it
gets interesting to create a report
because I'm using multiple tables if I
had if I done a a report on the other uh
the the other table with the customer
list I could have really just created
the page I really didn't need to do a
report unless of course you wanted you
wanted some uh hot pink colors so but
that's that's of course up to you if you
do that okay so let's have a look at
this data set so I've run this data set
again and now it's opening up and and if
I then go and preview and again this
report is completely empty and then I go
to help I go about this report and I go
to
excelon I close down this one running
model so it's taking complete control of
my sessions so I don't want that so here
I have
the uh the data set I have here um from
uh from the report so I have my customer
which is apparent for the sales lines
and here I see that I don't have any uh
sales lines for the first couple of
customers uh and the customers right
after the uh New Concept Furniture so
I'm going to get rid of that so let's
just clean that up in the data set so I
don't see that I do that by going to the
customer and we should should all know
this also I hope going to print only
detail you say to yes and when you have
done
this uh it would only show uh the
customer if it has sales lines so pretty
basic
en so run it again I'm just going to
take something to
drink so I'm going to
preview and in here I'm going to go into
help about this report and again I'm
going to have a look at the data set and
now I've cleaned up so I don't get any
customers that don't have any uh any
sales lines so the interesting here is
that my data set is now being
flattened uh and what does what does
that mean well that means if you notice
here the customer here these uh these
customers here is uh now shown here
three times but actually over here you
can see that there's actually three
different sales lines that I have here
so on the uh on the uh left side here I
have the the customer columns and I have
the uh sales line comments I also have a
format column over here uh that uh that
I really didn't create and this is
coming automatically if you put a
decimal in your data set then this
decimal will be uh uh you will get the
format uh transferred over in your data
set you have no way of getting rid of
that that's just there okay so this is
our data Cent great so now we know that
every time that it runs through the the
customer and it goes through the sales
lines for this customer the customer is
being
repeated
okay so we also see this here so for for
sale and going the customer 20,000 it's
being repeated 13 times because there's
13 lines in the uh sales lines uh table
that is related to this
customer okay so what I'm going to do
now is I'm going to go and look at the
grouping now because how is that how's
am I going to group that over in visual
studio so let's go back here go to the
designer and uh I'm going to put in a uh
a table and going what I want here is
that I want to have uh my uh customer
shown and then the customer underneath
the customer I want to see uh each of
the sales lines so what I'm going to do
now is just going to insert a uh just a
table and uh then I want to uh start
doing some grouping here the grouping
window is down
here this window here when you do
groupings I always work in this area so
it's really best practice to work in
this area you want to do row groups then
there uh the uh this part here if you
want to do column groups in on it's on
the right side column groups we don't do
that often uh if you are in this
scenario if you want to do column groups
you are more probably in a bi scenario
and you probably want to do some bi
stuff instead of doing a static a CV
Port so from myone point of view IDC
reports is really something that we use
for document
reports while it's a little bit strange
that Microsoft then is releasing a a
docum report as a word uh which in my
eyes we really can't use for anything
because we cannot do any conditional
things so let's fix that we can do that
well then we can start using word uh so
for a partner's point of view word is
not really an option uh as I see it for
an end user uh maybe but not for our
partner because we always want to do
something da we want to have a report
that can work for this and this and this
and this customer we don't want to
create a report for each of these people
so word reports in my eyes uh if you
completely disagree disagree with me
come down afterwards uh and then we can
talk about
this okay so I'm going to put this in
and I'm going to put um the go to groups
here going to details and I'm going to
add a group and here I have a the
possibility to do a parent a child and a
before and adjacent after everybody
knows what adjacent
means hands up who knows what adjacent
means okay there's only a few people so
adjacent means that when things are
completely on top of each other okay
right after each other so it's
adjacent so let's do a parent group here
I'm going to do now is I'm going to
group on the uh on the customer number
so right now I won't see anything here
and the reason for this is that this uh
table here has or ta has not been U has
not been uh linked to the data set so
data set name is not filled in here I
could go and fill it in here if I wanted
to but I could also if I wanted to I
could also go here and just type the
number of customer and then I see the
property of the T the TL again and then
I get it okay but I really I don't want
to put anything in my report here so
let's get rid of
this and I want to go down to the to the
details add group parent group and I
click here now it is linked to the data
set so it knows what what what we can we
can use
here about the data set is that we only
have one data set so we don't have the
possibility of doing multiple data set
would be great feature if we could have
that so Microsoft lening be
great you put in number customer and if
you uh then you uh decide if you want to
do a group head or group footer if you
don't understand what this is all about
you always check mark these okay we can
always get rid of them afterwards so
let's just check mark this say
okay and then uh this tool is is
creating uh a vertical text box here to
the left uh and uh from a bi point of
view that's really nice uh maybe for for
a docum report that's not something
really might want to use you could use
it but uh let's just delete this in this
case here I'm not going to use it so
delete go away so now I have a repo I'm
looking at uh and that's uh uh and I
actually have uh now completed the
report okay this is where people are
struggling so let's save
and let's run the
V and go back go back
and
run yes preview so now the report is
done can you all see it's
done no exactly you cannot because I've
have not been using any colors so you're
just looking at a blank page with a lot
of lot of rows here and you don't know
that that is actually this is actually
working so again help yourself do some
colors so let's go in here let's uh this
row here we don't need so let's just Del
this and actually we could use it later
so let's just keep it in um so I'm just
going to do some colors here so let's
take uh green
and uh let's take this blue here and
then we'll take some orange maybe
there's an orange yes
and I always have to have hot pink I
can't stop that I'm sorry hot pink I
don't know why it's called hot pink but
it's uh in Excel it's a Magneta but in
here in our tool it's hot pink so it's
really great uh so we have a hot pink in
the end
great yeah I didn't say that out loud
but
okay uh we now will go back and now uh
notice that I did not put any any data
on this repon here I'm just working on
the groups on the data set building up
my
report so if you're struggling with a
report and you sit there oh my God this
grouping I don't really understand this
why how is this happening so what is
your best
friend colors yeah hot pink
exactly exactly hot pink is your friend
yes you might want to use other colors
also but uh yes thanks for that one uh
who said that there a t-shirt for that
one yeah who yeah yeah okay so I'll I'll
run up so do this really fast I'm old
man
all here you
go so I can I can do like Steve bommer
run around and I can Dev devop us
develop us and they standing in 10
minutes
like I can't speak have you seen this
video
I'm not going to show you that video uh
so okay so let's uh let's go and have a
look at the
Von uh I did it again
sorry just I don't want two sessions
running let's run
it so now I can see that I just added
colors to my report now so now I can see
that at the top row that I have the
green one that was my table
header
if I click here and see the table header
then I can see this line that I have
here starting and ending and in the
middle here I have the detail Row the
detail row will go through your data
set if you it's outside of a group just
a detail row it will go through your
whole data set whole data set if it's
inside a group it will run in your group
what you have all the lines that you
have in that group and I have now
grouped it on the customer
number and if we go back let's see let's
see we put this to the left and we're
going to take this one and put it to the
right this one to the right Ah that's a
little bit too optimistic I'm not going
to do that small
screen so just just switch between so
this is a this is a group header this is
a dil row and this is a group uh group
footer so for every group I get a group
header then I get all the lines and now
then I get a group foter if we look in
the Excel I can see that for customer
10,000 I have three
lines these three lines and if I go and
look at my report just maximize this
this is group number three so start it
here group header all my lines and the
group footer so my report is working now
it's just a matter of me adding in the
information that needs to go
there people people get confused about
this and start thinking that Visual
Studio would automatically find out the
groupings of what the data that you put
up there up in the in the body section
it's does not work like
that so what I could I could for example
here I would put in the number of
customer or the name of the customer but
I could also put the name of the
customer here for example that will be
that would be wrong for me to do but
probably when you been playing around
with this these reports here this is a
scenario you've been in and you're
wondering why it's working like this
but the refa is really working you're
just placing it
incorrectly so preview so now I go just
get all my customers shown there because
that's what's in my data set for these
rows that is being created there so you
need to put in the right data of
course you all understand this somebody
say
no okay nobody dare to say no okay
should be quite simple I I hope you you
you follow me so what I'll do now is of
course I'll go back to visual studio and
I do this of course the correct way so I
put in here the uh the customer number
put in the customer name and here I put
in the uh just put in the sales number
and here I want to put in the
description and here I want to put in
the
amount I really don't want these caption
right now so let's get rid of
these so save go back save and compile
1,000 2,000 3,000 run
and then I'll preview my report and now
my report is
done so the foundation of my report was
done down in the
group is this too
basic yes yes okay what do you want to
hear
about more groups
yes
do you want me to tell you about how you
should create your document reports and
not the way that the standard reports
are
done yes okay let me do that
then we have about an hour left I have a
plane at 5:00 from Brussel so I might
leave five minutes
before uh the session ends so just aware
of that if you have any questions I
would like to have the questions during
the session and not after which because
I will be running out the door at 3:00
okay so uh let's let's have a look at it
so let's close down
this uh by the way I actually wanted to
show something also here before we
actually do that do you want to see uh
how I do sums of the the amounts and how
do I I use the these amounts uh from the
from the group itself and from the
tablets and the overall data set and and
show these groups inside the groups and
all that you want to see that you want
to see see that okay so let's finish
that then I'll just do that then
first just takes a few minutes to do
it's really easy because I'm going to go
down here and it's in the group I'll put
in the amount and really I'm just going
to go summarize by Sum boom and let's
just Bol this one here this bold boom
save and compile and go back to in yeah
was both in but this is the development
environment compile 1,000 2,000 3,000
run
and so now preview now I have the amount
there uh of the of the group so really
not that interesting for the third part
here first groups but more interesting
for this one here because there's not
more numbers here so that's a group I
could also also do that let's say put
that in the top so I could go here and I
say this to the sum also here uh boom
boom and then just uh let's select it
boom summarize by Sum boom then I also
have the uh the group sum here but what
about adding a new new row here so
insert row to the right and what I want
to do now is actually want to have the
sum of
everything can I do
that people are almost quiet so yes you
can you could just go into the
expression and in the expression here
you have the possibility to give a scope
okay so what I soorry I have do a sum
first of
course so sumar by some boom and then in
the expression boom and in here I want
to give this a um a a scope so I have to
define the scope here so I say comma and
then I say do dot not like that sorry
like this two quotes and then I give it
to scope right now I have the scope it's
all written down here for me data set
results I'll put that in data set
results and you have to be very specific
otherwise this will not work so data set
result put that in so now I have that
youve probably been wondering about
these expressions and everybody loves
these Expressions that you don't have
you have the possibility to see what's
in there right do you know how to fix
this you just double click give it a
name and you write here and then say
overall
tool so you help your fellow colleagues
it's coming after you so now it's this
overall to of expression um okay so let
uh let's just have a look at that that's
the overall total so save and compile go
back to NV to do I need to speed up
because you wanted to see the other part
also so now I have the the overall total
this is uh this part here the total of
the group in the top and the total of
the group in the bottom
also oh so could I have uh what if I uh
wanted to have the uh total of the group
inside the row also could I also have
that well you could also do that so you
can always look up but not down of
course so we're going to go here let's
put in the
amount and here I'm going to go H click
the field again boom boom summarize by
Sum I'm going to go into the expression
and here in the expression I'm going to
give it a scope so what's the scope I'm
going to give it
here this the scope of the group and the
group is called no customer or number
customer
so you say yes to this again we get this
nice little expression double click it
get into the placeholder properties put
a label and then we just call this group
Total yes and then we click
okay so we have group Total here save
and compile let's have a look at what
we're
done
yes so let's have a preview so now we
have uh we have the group Total in see i
r too fast
again let's be a little bit more
patient so now we have the group to to
yeah actually was working sorry uh we
have the group tot here on the lines so
the lines are the uh are the orange uh
orange on I usually make the lines hot
pink that's why I got
confused so yes so the group Total is
here on the lines the group Total here
Group total here and then the overall
total here so that's what you can do uh
but what if I then have a uh a group or
a uh um or taets that's filtered so
let's see if I have this filtered so I'm
going to go back to this and going to
look at this table here boom I'm going
to go to the visibility sorry filters
I'm going to add a filter and I'm going
to say I want to do this on a customer
number I want to do between boom and
let's say 10 10,000 to
20,000 so okay and save and
compile so now I really haven't done any
total on the on the taets yet but let's
just see what's what's going on here so
now I only should only have uh did I not
do it
right did I do something
wrong filter yes yes
Save oh I didn't get back okay sorry
about that
yes and
preview uh and now I only see the
customers uh 10,000 and 20,000 that's
the only thing I see now uh and if I
then want to unless I want to see the
total of that I could also say I
actually want to see the total of that
scope so I can set a column to the right
so I want to put here let's just take a
copy of this one here contrl C and
control V and you go in here and you say
check expression and instead of data set
result what do you what do you do well
what you do is that you take the uh
scope of the table and if you have the
document outline if you are working with
this studio you have the document
outline open over here to the left and
you can see uh the hierarchy of how your
report is being built up you can see you
now this is called TX one so you write
TX one here and then say okay and this
is not the overall total anymore this is
the
overall uh TX
total
so yes okay save and and back and save
compile one two three four hopefully
it's okay
now and we run preview and now we have
the total for the for the tapic we have
the total for the data set we have the
total for the group and you can of
course play with all these so you can
get get from you can always go from
inside the group or go to the level
higher and higher and higher you can do
that but of course you cannot go in uh
and do this okay
Let's uh let's pack this one now unless
there have some
questions uh so the question was if we
could do totals per month
per multiple multiple tables you could
do some for that uh
yes you could do that so uh but then let
me actually answer that question by
going to the next exercise because and
then I can I can show it to you uh so
there's a little trick to this so uh let
me just close this one
down and I'm going to go in here and
let's just close down Vis studio also if
anybody have read my blog I really
encourage you when you're sitting and
designing reports I really encourage you
not to close down Vis Studio because you
can always undo always undo and if you
close down to the studio you're shooing
yourself in the foot I think I've said
this many many times I also said last
year at this session here so but please
keep this studio open as much as
possible because you can always undo the
things you have done and on doing things
and on developing things well you uh
make the call of what is
fastest so let me answer that question
first that you had because in this uh in
this designer here I don't have a data
item that in in need uh the customer
here I have two tables that are
completely uh uh independent of each
other so they're same level that's kind
of the scenario you're thinking about
correct I can see you nodding
yes uh let's not do any sums here uh but
let's do something else uh let's do
um let's go in here and put in a text
constant I'll just SC this cost
and I call this
customer and I want here I call the
vendor and then
vendor yes
so compile uh actually I wanted to have
it in here so let's uh put up the
customer here and just give it a name so
I can use it own Vis studio and then
here vendor here open up the simple menu
and vendor here so save and compile and
then we're going to go open up the
visual studio and in here with
then I'm looking for something to drink
here uh we have our data set uh actually
we need to look at the data set first
yeah exactly let's not uh get too
carried away here because this is
important and going to
preview and then we're going to go to
the help and we're going to B this
report and we're going to go to Excel
and let's get rid of this one running
modal
and
Excel okay so now I have uh two uh two
tables that they are completely
independent of each other so I have a
table that's running here so going
through all my customers and then when
the customers are done all my my my
vendors are here so I have in the uh in
the object designer I have two tables
that are on top of each other but then
in Excel it's completely separate from
each other so you're actually trying to
do a sum of some things that are
completely separated from each other yes
but let me show you a
trick you could of course do this in a
in N uh but that's uh Did anyone say
anything
yes so if you wanted to use labels
instead of text constants uh yes I could
have done that also
yes you're saying the purple ones are
infect are we talking hot pink now or
what the perform performance yeah yeah
of course uh but then we talking about
the captions okay so let me answer that
question also and I'll get back to you
okay so the captions is when you're
saying include caption is include
caption is is is a label that's coming
over it's a parameter it's actually
misusing a little bit parameters uh when
we did this uh actually was part of the
group that did that at Microsoft we
misused it a little bit because we know
it's not really supposed to be a
parameters as such but since nobody is
changing this we could do this uh so uh
there was a risk that somebody would
change it but nobody's changing this for
the next 25 years so so we okay uh so uh
if you do it with a parameter the
caption that comes in is a caption the
language of the client that you're
running okay so if you want to do this
these captions you can do this on
internal
reports but you cannot do this on docum
reports because you might want to have
this report going to Spain to Germany
and UK and maybe also to Denmark don't
send invoices to Denmark but but uh you
and you would have to have uh these
these caption SS and the and then you
would have to go and add these as a
column and you will have to have the
captions on each row of your data set
and that is of course a little
performance heavy yes did I answer your
question yes okay so back to
you so what I'll do now is that I have a
look at my vort and if I if I run my
vort
now uh let's just add
insert here a
table and uh let's just for the fun of
it just instead of mov and colors we're
going to go into the expression here and
expression and here we're going to take
the common function and we're going to
take miscellaneous we're take the row
number so I can actually get the r
number also it gives me a scope what is
the scope that I want to run this well
this is on the tapx one that I want to
do this on tapx
one bom R number yes so now I get the r
number let's just give it a name so roll
number so oh so and then we run the
vort and back to the development
environment wait a couple of seconds
run and
preview and now it's running through my
whole data set so I have all my the all
the the rows that I have and I have one
36 so really I've created a a table
that's just that's running through whole
data set so I've not grouped this yet uh
so let's uh think that now we have the
whole data set in this this table let's
go and uh and play with this so if I I
don't have a decimal in this uh in this
uh scenario here but I'll give you a
clue of how you do this or tip so go to
the expression and what you put in here
in your data set let's not let's
actually get this this report or this
table related to the data set good so
I'm going to going to go into the
expression boom and then we're going to
go to the fs I'm going to take the
customer number here uh yeah let's just
do the customer number that's fine uh
and what I'll do now is a little trick
so I put plus here and then I take the
the vendor
number so what is am man doing here is
going this is going through my whole
data set and no matter what happens it
will never be able to have the customer
and the vendor at the same time never
they because they completely separated
from each other so I could do a sum here
also on these things if there was a
number I had there uh so I could put a
sum around here yes so let's say okay
here so that's just a I don't want to
put the names anymore so just go the
expression and here I put in the field
put in the name of the customer and now
I put in the uh name of the vendor boom
and then just uh do this also so it's
visible what we're doing
computer please work thank
you
expression going to go here and then I'm
going to take this uh
customer and plus and
vender and let's do some interactive
sting on this report here then so say
Okay boom and I'm going to go up in this
field here I'm going to go to text
properties in the text properties you're
going to go to the interactive sorting
enable sorting and I'm going to sort by
the same expression that I just had down
there so okay
boom and if I save and apply my report
please work computer
please thank
you so preview and now I have uh my uh I
have my customers shown and if I go down
I have my uh my vendors come coming also
so they're coming down here so I don't
have any blank rows in this uh in this
uh uh table now and if I go to the
top I can now do a filtering here so I
can sort on the customer and the vendor
and if I actually did an interactive
sorting on here let's do that also here
so take this on and do it on the name so
copy this expression
here boom boom
boom here text box interactive salting
enable inter salt
expression and come on computer work for
me thank
you say
Okay
save
and save and compile wait for a couple
of seconds and then run the
report then I go
preview and then now I can now sort here
and now I can I can mix things together
so uh so now I've alphabetic the
alphabetic order the customers and
vendors uh
so as I said the other day you now have
your list of the Christmas cards
so so do you understand do you
understand you could do some like this
do you
understand yes okay
yes
perfect okay so so that's one way to you
could do it in other ways also um so
what I want to now show you the way that
you actually should create document
reports because document reports is I
have to say it's a bit bit of struggle
uh it's probably also why you're all
sitting here
um the way that are CV ports work or
actually the report viewer is working
actually it is CV report is that
first first of all the nav team is a
little bit or actually also was part of
that team uh so uh sometimes when you
point you have three fingers pointing at
your yourself sometimes you know that uh
so what we actually did was we uh we
created one big data set it's not really
nice uh because the way that Vis Studio
or actually it was actually the SQL
Server team that created this RDL not
the VIS Studio team the VIS Studio team
came afterwards and then created the
rdlc so we could embed our reports ins
inside our
application but we did was we created
one huge data set so if I have let's say
300 invoices then I want to I want to
print I have all these 300 invoices in
one big data set and that's not really
what uh the guys from the SSS team had
thought that this is something that
people would do uh why would you do
something like crazy something like that
well that's what we did in the na team
uh so um if anybody from Microsoft is
listening to here or here it would
really nice if we could get a print
engine so we could do it on groups
instead so we don't have to have a huge
data set okay and call me if you want to
have that elaborated because that would
solve so many things for us without the
CB Force but we have this huge data set
and the way that is working is that it
goes through all of the uh the body of
these reports and when it go through the
body of the report then it will do the
page set up for all of them the page
foot for all of them you would think as
a human will say ah it's taking Page
Body
page no that's not how
working unfortunately it's working like
that because it needs to know how many
page number there is it has to calculate
all the page numbers first and then it
does a page set on page page uh footer
afterwards and one of the reasons and we
also only can do the page number on the
page set and the page pH kind of one of
the things that that I hate most about
icvs but I can't do and put the page
number where I want to have it in the
body but I can I have to have it in the
page page header or page footer so
when we do it like this so we run
through the body uh the page Setter
doesn't necessarily know are you can
always uh you can always get to the
first and you can get to the last but
you can as not iterate you cannot do a
table in the page Setter and you cannot
do a table in the uh page footer either
it's you can do text box and you can do
a rectangle uh and I think also you can
do a line that's about it so you can
only get to the first and the last in
your data set in your pay Setter but you
have
400 uh invoices or 300 invoices in your
in your data set so you can get to the
first and you get to the last so we have
to do some logic to get the uh to to get
the uh each of these uh um information
the customer address for example on each
of these
uh uh each of these uh bodies uh sorry
of each of these invoices that we have
for example so we take the uh we go to
page number two well that's another
customer from what we had on on page
number one and then this customer we
need to to we need to uh create a
variable and store that and then we have
all this crazy code get data and set
data uh so really what I do is I don't
use any pay heads in my
reports uh I and people say oh can you
do that yeah you can do that U is it
complicated no it's actually easy easy
to do uh can you show me how it works
yes of course I can do that so here I
have a Reon where I have done this
so I'm previewing this report and I've
done some other things to this report
also uh and this is just a report that's
being grouped on the uh um everything's
done in the in the uh T in one tax and
then I have some groups inside this in
this
tapings if I do this way and avoid doing
a Petter because I know the Petter is
something that is running very late in
the game and I can't do I can't work
with the with this this is just too
complicated when I do do my uh my
document report so I rather want to do
that uh I just want when I create my
report was like this is the part I want
to have repeated on all pages uh this
part actually I don't want to have this
on all pages and this one here I want to
have repeated on all pages so you have
suddenly you could do Dynamic things on
your pay
sets does anyone of your customers
request
this
no yes yeah exactly they're always
requesting this and then you're saying
to them well I see has a pet and it's 10
cm in in in in height and I cannot
change this because this is dynamic not
not not that this is this hard not
hardcoded but it's like fixed size I
canot change this it is 10 cm and 10 cm
on all your
bases that's
crazy so and
the the result of this why do we get
into this situation well we get into the
situation because we are adding multiple
taxes to our page so we create a TX TX
has a header it has a a detail row we
place another TX we place another TX and
we place another
TX and we then uh work with our report
and then we say I actually want to have
something repeated okay so you put on
the first tablets on the top you put uh
that this row should be repeated and
then you run your report ah it's working
great but then suddenly you go down and
and the next tablet starts and VOD
viewer is now okay the next the the
first tablet is is is uh is done
rendering so uh let's throw that away
and then move to the top again for the
next tet and then you and then it's not
repeating this that I had on my first T
no because you're doing multiple TS
you're forcing yourself to create a page
Setter when you do this so if you see a
report that has a list and has well
basically it has a list you're doing it
wrong
in my eyes okay so at list no don't do
it because if you do this you will get
into you are forcing yourself to create
a PID Setter and when you create a PID
Setter you get into this scenario where
you have to to set variables uh in a box
that is hidden in a corner and you have
to have 55 fields that you have to go
and and and look at and in the uh in the
top of the report it says code get data
one comma one and the code get data six
comma one and so forth and it's just a
waste of time if you ask
me there's a problem with my
design page
number because the customer will say I
would like to have the page number here
okay yes but you will not have that you
can have it in the top and the top left
top right uh the bottom
right bottom left or bottom bottom right
that's where you can have it you get it
for free yeah but I actually have it
here yeah no problem for each 1 centimet
we go down there's € 100,000 okay okay
then we then we do that because you're
ruining my design and I don't really
don't to talk about this page page
number okay just get rid of
it just put it in in these Corners page
number is not important and if you put
that is it how important how much money
do you want to pay for this page number
come on it's a page number it just have
to be somewhere on the
page so yes it's breaking uh this is not
working because see so I have the page
number down here this is where I have my
page page number
so I don't want to discuss that um and
that's of course would be nice if I
could put it into the put it into the
body of the report I could put in the
body of the report but then I start need
to count the rows in the report and then
it gets really really ugly uh but of
course if you're in this situation this
is an option that you you can do and
then you spend a lot of time with that
okay so what do I do let's just delete
this part here um because we did this so
I'm going to go in and put a table here
and now I'm going to build up my my
report the way uh that uh that I
suggested you do this I think I created
a video actually on YouTube that you can
find this also so we have a uh we have a
group here you go to uh a add group and
now I'm not going to go parent or child
I'm actually going to go adjacent
after and then next going to group on
anything I just going to put C1 here so
this is a child and I'm going to go AK
and I'm going to delete this part up
here this is not something I need right
now so now I just have a group that I
have called group one let's just rename
this and then so we get this as a CH one
and say okay so now I have this CH so
what I'll do now is come on thank you so
now I'm going to create a parent for
this so let's create a parents and then
I just click this group head and pooter
I like that H and then let's go into the
group properties here and then SC this
parent also boom uh boom
so then you go in here and the for the
child group and you add another child
group which is on the same level so you
go adjacent after and let's just put C2
here and what you then do is you go to
group properties
here
and C2 and you say okay so this is your
structure of the Reon say uh what about
the details yes let's put in details
also so add group you say TR group and
you show show detailed data actually I'm
going to before I do that I'm going to
click this and delete this column I
don't need it so go into the ad group go
chart group and notice that I click show
detail data I'm not going to put
anything here click okay now I get this
bloody column again let's get rid of
that say just to Del the column only yes
fine so now I have my group here which
is this group here this is my child one
and this is my child two so let's get
the detail data also there and let's get
rid of this F column that Visual Studio
keeps doing for us uh if anybody finds a
way for to disable that so it's not
doing that by by default please tell me
and I I'll invite you to a nice dinner
in Denmark because I really hate that so
now actually what you have in front of
you is the skeleton for a doc
report because you do everything inside
this group and what you do here instead
of doing taxes You Do child
groups and then you can fill these child
groups and say this is the subset of the
data set this group can see this is the
subset of the data set that this group
can
see just like we're doing on TX syst
because what we're doing is that we have
this humongous data set that we don't
necessarily want to show in all the
areas of our
report okay
so let's uh work a little bit with this
so actually what I
want I want to go and make some colors
surprise sorry about
that come on Mr Studio I I don't know
what's going on here but they I don't
know how they did this so no matter what
I do when I'm standing over to the left
side of my repost I'm standing over here
and I need a property over here it's
never the property that I need that is
visible I don't know how they did this
but it's really great this good logic uh
this is just amazing I don't know how
that's how they did this but uh now I
made a little bit bigger so let's uh
take
green and let's go here and we go let's
go with the blue and then we take detail
row and yes hot pink surprise uh we get
the group header here for this uh child
group now let's take yellow and then we
have the detail row uh we can't do
yellow again let's do gray and then we
have
here uh the bottom group uh footer and
then let's take this one here so now we
have a lot of nice colors so let's go
and save this
report and get the data set or get the
XML into the report itself and say okay
and then we run the
bort so preview so this report is not
working yet
uh so what we have now is that I haven't
done any rows here let's go to the print
lay out so we can see that I have a lot
of hot pinks and we go go down if I put
in the row numbers here actually what I
would have I would have 130 was it 134
rows that I have my data set so I have
134 uh hot pinks here and 134 of these
so I want to filter these so what I do
is I go to the group
and what I then do is I go into the uh
to the group here I say group properties
and then I go filter I add a filter the
way I'm doing filters uh yeah
um I've written a Blog about this but
it's just a very shortly uh so I always
convert a string uh so then I do a uh
length and then I put in the field that
I need ah still this needs to be linked
to the this the data set name thank than
Q so I'm going into the group again
group properties going to the filter
going add am I going to
slow okay
good uh then go to the
expression come on thank you
computer and we take the data set so we
take the customer number and we'll do it
like this so why do I I convert it to a
string well I convert it to a string
because then I can I don't have to
bother about this one over here if you
want to bother about that one this fine
uh but if you do this in visual studio
2013 which is sorry Visual Studio 2010
which is a version that supported in
2013 be careful because there's a Bo
there uh so uh and it will if you have
put integer and you will look go into
the expression it automatically Chang it
to text if somebody goes in and looks at
what you have done so be careful with
that then uh I would say just ler than
zero and I like to use the
length uh so um I've done that so now I
filter that so let's just put in the row
number on this one come on
computer don't do this to
me come
on so short break for this little
computer here uh
let's go to the expression and it's just
going to put in the row number here so
common function misell laneous uh row
number and we're going to put in the
scope so let's just put in uh should we
put in the scope of the group let's just
do that so that's uh
C1 so let's just put that in go away so
C1 it's always the name that we do this
on scope one so let's see this works
save
compile and we
run and we then uh preview the re so I
go and look at my data sets let's just
go make this a little bit bigger so
let's do not 500% but 200% and we go to
the next page next page next page and
you notice that I now have
136 uh rows here in my data Cent so my
fill is not
working so if you ask me what we're
looking at right now is a
buck uh unless somebody can explain me
why uh this is not working uh then then
it's fine uh but I don't have anybody
can can explain me that uh so what uh
what is what is the problem is that I
actually filter this this group and I in
this group I only wanted to see
customers because I was filtering on
the filtering on the customer number
okay so only want to see the customers
there so filter not working so what's
going on so some of these things that
you you you spending time on inste
thinking what what's going on here uh uh
so it will take you some time to figure
out if unless simp tells you well the
filter on the group is not working
because before you have a valid group so
you cannot just put a text there which I
which I just
did so it has to be a valid
group so what I'll do is I'm going to go
into the just just text I could have
written anything here anything it's not
being grouped by anything so let's go go
to here to the expression and I don't
know why my computer is slowing down
come
on time to drink something and
wait okay
so click here delete boom so I want to
put in a group exre here and what I
always do is I do the following so I put
in the length
and I then put in the field itself
where you customer number and I then do
different from
zero so now I've done a value group this
is in the scope of what what I want to
show so I say okay to this and I then
save go back to n wait a couple of
seconds
run and now the repo is
running and now if I just let's go back
to this layout let's go back to 200%
and then we'll go to the next page next
page oops so that's what's actually was
it was actually working so now I only
have 68 rows in this child group so I
have now specifically told this group
that you can now see this part of the
data set so I'm going to do exactly the
same on the next uh on the next uh group
also and then this can see the specific
rows also
there this way you can do you can mimic
what uh is done in the uh in the
standard reports with a list uh which is
forcing yourself to do a uh a pay Setter
and you can have everything uh inside a
one tax and you have full control of the
of what's going on in top and you can
have one row that's shown one row is not
shown and one row that's shown and one
row that's not shown and so forth it's
just a matter of your imagination and
the customer's imagination of what you
want to have there so uh let me uh show
you let me just finish this one here so
let's go down to this one this group
here this is the vendor group Let's uh
just put in the row number let's take a
copy of this one here and then go here
uh let's make this uh light gray also it
is light gray why is it saying
that
okay so let's say like we so this one
and when you do a copy notice that be
careful with that Vis Studio finds it
very funny to delete what you actually
had in your
expression
I I don't know why that's happening uh
but it's a oh this is too complicated
just just delete
things okay thanks uh so we want to put
in the uh the RO the the the RO number
here the scope again so in this case
here let's put just
C2 so yes uh and another thing is
actually if I let's show you something
if I go here and you uh let's say I put
some R visibility here so say this is uh
based on let's what just put whatever
just put true here whatever and then
we'll say okay and then you say okay you
go into this uh line
here if and you wait again for the
computer to wake
up this is a very well tested uh
scenario a lot of people in Microsoft is
testing this yes um so I'm going to go
in here and I'm going to uh now also do
a row visability here for this one here
so no row visability that's fair enough
you remember I do the row visibility on
this one right you remember that yeah
okay so let's have a look row
visibility gone okay so be careful with
that also uh so this is a little bit
tricky also so um yeah you have to hold
your horses uh another thing is also is
if you have this expression just take
take expression and I already did this
and I paste it over here so yeah that's
possible but let's imagine there's some
custom code in this one one here there's
already some custom code in the vport
that that Microsoft is coming with they
have some public function here theun
blank zero and so forth so we could just
take this blank zero for example
and it's not really very the case but
let's go in here expression and I think
all of you probably know this but let's
if you don't this is a small trick so I
put here a code and then I put in the uh
blank zero and then parentheses end here
so I put a uh actually where was it
blank here it is sorry uh here
and sorry about that so now I have that
so I say okay to this and now this text
box I want to copy and I want to copy
over here and I get this but get this
one here repo Builders unable to
successfully copy this text box okay
thank you for nothing why is it not
possible well uh if you if you think the
logical reason for not being able to
copy this is that you actually need to
have a comment here okay so you put a
comment here and then you take the text
box and then you can copy it
okay it's really strange
so yes you like that
one yes really strange uh so uh and this
is uh if you go and look at Ms connect
uh there probably about 250 people
saying oh this is a problem and you know
why we can't copy things and I was like
yeah and then there's a guy or girl or
whatever on on this m yeah we we could
have build we solve this in the next
version okay which
version there is no
version so stop promising something
you're not doing so okay uh what I want
to show you a little bit here also
because I also run into another Buck
here and the problem I have here is
that uh I'm ring into an issue because I
want to have let's say I want to have
this row here repeated and I want to
have this row
repeated unfortunately when I deleted
the columns that I actually didn't want
Visual Studio to to to create in the in
the first place well it that actually
did not clean up after itself
unfortunately so if I go into advanced
mode this is a really Advanced thing so
if I go into the uh to this uh row here
I have to go advanced mode and I can see
down here that I have a problem
experienced people of course but you
might not be able to see this if you're
not playing around with this but I have
a problem here so have a look at the
static row here and notice that I have
now it's actually very helpful so I
clicked this group here and I have on
the First Column I can have a this is
marked so I can see this is the uh the
group that that this is in this is a
parent group and I click on the child
group well this is this area here and I
look at the click on the other child
group and this is this area here so it's
kind of this to this kind of helping you
right uh quite a lot here it's very nice
actually uh I like that so go to the
static row well this is the static row
uh static row is of course not a row
that's iterating through your data set
it's just uh shows what you have printed
in there the static rows can get uh the
first and the last part of your of the
scope that you're in right now but it
cannot do any iterations of course if
it's in a group it
can okay so we have um the this static
row here here so I can see that this
static fine but when I click this static
rule it's going down to my detail Ru so
what's going on here well this is a
problem and you need to solve this and
there's an easy solution for this it's
really easy to do you open up uh the uh
the uh designer here you open it up in
XML view uh so you go and open with you
just save first and you open up tml ex
and then you locate the place where you
need to solve this okay so this quite
easy to do so let's go and uh I hope you
understand the ironic I have here so
delete
me so put this delete me so we're going
to go save going to go to the I also
wrot a block about this by the way so go
to XML text editor and I'm going to
search for the
me I didn't do a so just do it do it
like this delete me so here I have it
and then then uh what I have I also had
some P to great so this is um even more
easy to know exactly what I need to
delete so this is a I need TX member the
TX members the visibility property on
this one also and the data element name
so let's get rid of that one and I'm
going to get rid of these two also boom
so quite easy to do everybody can do
this and know exactly what they do if
you start playing around with this you
can in the designer undo things so you
go back to the uh to the IDC designer
here and what do you notice here now the
properties are
gone so what do you do to my properties
well actually CLA what you need to do
you have to go back to the reort IDE see
and you have to go back to the design
and then the properties will come
sometimes so I see no what's going on oh
now they probably still there are okay
thank you very much okay so uh so now
what I've done is and also gone out of
the advanc mode so everything is that
kind of reset so let's go back to Advan
mode and I can now see that the static
row is correct static row here and I can
uh I still have the problem down here so
this static row is still
wrong so be careful with this if you
don't care about repeating any of these
rows if the customer say I would like to
have when this group is running I would
actually have to like to have the the
caption being repeated on all pages
which a valid quests and you can spend
hours and hours and hours and hours and
hours trying to figure out what what the
hell is wrong here if you don't
understand that Visual Studio created a
static row it didn't leave took away the
static row when I deleted the
column
okay so what is a problem when I don't
remove the line I the problem or I can
try to do it I could put in the let's
say I want to repeat this Ro so uh let's
say I want to repeat this R so I go to
static and I go to the tabl member here
and I go and say keep a group uh and I
say actually don't yeah keep group
that's fine uh I'll said this several
times I don't know all have heard this
but uh uh keep group before uh don't
play with this because it's not working
um so I always use the keepy group after
keep Group after I have not found any
box in it's working all the time so if
you find a box please tell me I have not
found any box here so but keep it with
before it's not working so keep your
hands away from that uh if it's working
in your scenario beautiful uh but there
might be some Corner cases that you have
not tested in your report so be careful
before is is a it's a very buggy area uh
so that's small little warning so what
I've done here is I just stand static
rule here so I want to repeat this this
uh repeat on new page so I say yes and
let's do the same thing on this one up
here so go keybard group and keyb group
after and then I repeat on new page so
what we'll do now this this row here the
uh light blue here or whatever color it
is is will this will be repeated but the
yellow here will not be
repeated you will think it repeated
because you did exactly the same thing
but you have this little problem here
that's that's just blocking you from
doing it so let's uh save and uh compile
and then
run and then you go here and then you go
preview and let's have a look so I'm
expecting the not the green one I
expecting to go away because I didn't
ask this to be repeated I could actually
I've been have repeated this on all
pages because it's a uh above this as I
remember no it's actually if I created
another above that I could repeat this
on all pages let's just do that for a
second give me a second
uh how much time do I have
left 10
minutes 15 minutes yeah you remember I
have to catch a plane right so is that
including me running out of the door a
come on just the right color
close
so and now I'm going to set this static
row here I'm going to set this to also
to repeat on all
pages
so
yes
run run preview Bo and then we're going
to go here boom and then I'm going to go
to the uh next page I'm actually
expecting the uh the kind of the purple
one in top I want that to repeated the
green one will disappear and the light
blue here will keep on going so as I
said expected now I'm getting to the
next page here so I'm expecting the
yellow here not to be repeated so I'm
going here and it's not working okay
then you can start uh you know sit there
and you try to put it in and you get
errors and say let's say let's let's put
this static R here you say keep recoup
after you say ah why and you say I
should actually do that here also you
say true and you go here and you build
and it is now saying you you have a
grouping member uh that is uh yeah you
cannot do keep a group on the properties
you have to set it to none but I don't
want to set it to none I want to keep it
I want want to have it there and then
you're struggling with this one here so
you just have to get rid of it for this
to
work okay so uh any final questions
because I am I'm out of here soon guys
but I want to just uh want to give you a
little hint because if you want to know
more uh there is I'm doing some training
uh in these reports I'm doing it next
week Monday Tuesday and Wednesday next
week I will also do training in in
Belgium and in December and I'll do
training in in Holland also so if you
want to uh if you want to go there uh I
think it's good idea for you to uh to go
there if you want to beer experts in
orts if you attend my three days
training I always give people uh free
support for
things that I did not tell you in these
three days okay I know what I told you
so if you come back and you ask me uh
you can always uh you can always come
back to me and say oh CL you didn't tell
tell me about this no I didn't tell me
okay let me help you okay uh and
magically what happens is that if
somebody comes me with this request my
next training of course I'm going to
tell you about this okay yes so uh I as
I said been training around 900 people
in the channel there are other tools
available for you you probably seen this
on the uh on here in this conference
there's a tool from Iden and there's a
tool from fun app people coming up to me
oh what do you think about these tools
it looks very
promising
okay I suggest you check these tools out
it looks very
promising unfortunately it's not
something Microsoft is doing but
Microsoft is not doing anything so kind
this is the other the CB Force we have
so I really suggest you have a look at
the these tools uh the guys from Iden
what they did was they created the
designer uh so a great designer and then
uh they attacked the up upgrade uh while
far started with the upgrade and is
doing a 100% upgrade or at least that's
what they're claiming they're doing a
100% uh from classic to uh not the IDC
part but their reports uh the uh Island
guys are also claiming this uh and I've
not been in the uh in the position where
I have the possibility to go in and
claim other uh than what they're
saying uh so uh for AVU is working hard
on the designer uh so uh so the designer
in Iden uh from my point of view looks a
little bit better right now uh but on
the other hand for nav the upgrade of
the reports well might be a little bit
better also so and then they have a
different price Model so where iten is
uh As I understood it is uh it's more
cost on the partner and where for now
there's more cost on the on on the
customer so this different P model so
I'm not going to go and recommend any of
these tools even though people are
requesting me to do do this all the time
uh I'm not doing that uh but uh uh yeah
so go look at these two this is one I
recommend this is my recommendation
there's other tools in the market also
uh but these are kind of the Rising
Stars uh that we you might want to look
at okay so any questions that I missed
uh one question actually for me did you
get anything out of this session hands
up okay thanks guys
okay any questions I have two T-shirts
if no questions I'll keep them
myself so you already ask a question so
you don't count yes
yes so do we have a microphone I can
also repeat the question but yes when
you have a when you at a group you've
got the um include
head see I cannot hear you all all of us
can hear you but I cannot hear you so
when you add a group um you've got the
boxes for add header and footer lines if
you forget to tick them is there any way
to get those headers back on yes uh
yes especially if you have uh if you
have not removed your the column that
the kind of the vertical text box that
you have you're going to right click on
the detail row and you're going to click
at Group total so Group total and then
you get it I can very shortly show you a
T-shirt and then I'm out of here so show
you in a second and
then so what you do
is you are in this situation let's go
back on this report here go away go
away
so uh we're here here here here go back
go back go
Back come on go back go back go back go
back I I closed just don't know what's
going on here let's just delete
everything and we go here we're going to
insert a table boom we're going to go to
the row group and I going to go to the
details add group parent group group
this on whatever just uh just whatever
just this and you don't check mark this
for said you check mark this but you did
not check mark this for example so now
you're in the situation you want to have
that you then right click you set inser
above it will not do this this is your
problem right so what you actually do is
you go here and I believe it is where is
it uh it's actually on the group down
here here you go to add tot and you say
it
before ah come
on
here add total before and then you get
it okay so at all that's how you get it
in one more t-shirt and then I need to
catch a plane
you what's your name Dom okay hello
Dominic I'm CLA
is it possible to uh put trans Footers
yes in group Footers to the bottom yes
the page yes I love transitors and
transs this is a favorite topic of mine
I've written four blocks about this
topic so uh and they have reports uh on
the
uh on my one drive where you can find
these things uh you're probably asking
where's your one drive let's me show you
that
so my
block is
meoo actually they they Meo decided not
to have blocks anymore so I have a lot
of work to do now unfortunately
Soo uh
do
blocks uh
cloud and it should go to ah I'm not on
the internet give give me a second okay
mibuso.com
uh blogs clel this is my blog and when
you go into this block then you search
for One Drive in one drive you have
access
to actually there let's see come on yes
so here it is you search for one drive
one drive because I like to do give
examples switch for one
drive
come
on uh and then click here surprise is a
transitor transo uh scenario you go on
my one drive here and then in here you
can navigate up you go to the R2 you go
to public and you have huge amount of of
uh examples that I put in here I've not
blocked about all these things here
there just a lot of a lot of reports
there you can you can find and you can
play with so I need to catch play so
really thank you very go thank you very
much for being here thanks
guys
