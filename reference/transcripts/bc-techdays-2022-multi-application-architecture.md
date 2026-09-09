# BC TechDays 2022 - Multi Application Architecture

- **Source:** https://www.youtube.com/watch?v=31WfYBdOMjY
- **Video ID:** 31WfYBdOMjY
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 94m06s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

I know
foreign
welcome back to our last session of the
day in room nine uh the session will be
multi-application architecture presented
by Camille sashek and Jeremy visca thank
you
[Applause]
hi everyone I welcome you on our session
I hope that you enjoyed this uh this
conference as we are already because we
are after two days of workshops which
are very very uh good thing how to find
new information and meet people and
my name is Camille sachik I'm working as
a software developer but right now I'm
managing our product development in
company invertica from Czech Republic
I'm MVP since long ago I will not bother
you with the date and I'm here not alone
because I have my friend here Jeremy hi
everyone I've been working with nav and
BC since year 2000 as well
and the ink is still drying on the MVP
so don't touch it too much
it means yeah Jeremy already told that
that's uh it's meeting uh of someone a
lot like me or MVP with the young MVP
but so yeah we were not continuing that
part okay we will talk about the
multi-application architecture uh since
today I think there was no session
focused on the architecture itself it
means maybe the session is somehow
different than you already had to today
about the tools you can use and how you
can produce code in the best way without
nearly touching the keyboard just
looking at the display and it will type
everything for you
that's nice but
producing code just without any
architecture without any any patterns or
or Target we want to hit with that code
it will lead to something we don't want
to use anymore and we can't support and
we can't upgrade and nobody will pay for
that anymore
but first the question is what does it
mean architecture architecture we we
know that word from what are around us
we see building and we see that that's
the architecture of 18
century or something like that uh
there is few quotes about the
architecture in software development
first one architecture represents the
significant design decisions that shape
a system where significant is measured
by cost of change
you know that name I think for example
from University because Grundy Butch is
behind many things in software
development
and we can see that architecture is
set of decisions decisions you are doing
during the development itself
these decisions are leading you
somewhere
and you can measure if the decision was
good or bad
for example based on the cost of change
but not cost of change now but cost of
change in future
because if you have
good architecture the cost of change of
for example adding one new field and you
know that it's every time it's only one
New Field the customer wants to add
there yeah and then there is another one
field I need I don't need anything more
just add that field and that field and
that field
the cost will be constant for you
um
I will let it grow up
uh if we have a good architecture
sorry
that's working uh we are on the on the
constant line and even in 10 years or 20
years the cost will be safe same
if I want to do the same change
if I have a wrong architecture
and you know these cases when the
architecture is wrong the cost is going
up linearly or or exponentially it
doesn't matter yeah
those are the monoliths on nav
which are still on version 2.6 or 3.6 or
4 and 5 and any other version and they
are not able to upgrade anymore they are
not able to extend the system anymore
they are not able to change anything
anymore because if someone asks someone
please can you change that no no I will
not touch that yeah because something
else will break there I I don't want to
to break your posting because I added a
new field in that
an important stable and additionally on
top of that you also get into the
challenge of try to find information
about 2009 setting up a new web service
and getting the spns just right the
documentation keeps up with the version
so there's a higher and higher cost of
just supporting those older customers
it means don't forget about cost of
change we will speak that about that
mostly
another quote
when software is done right it requires
fraction of the human resources to
create and maintain
changes are simple and rapid
and defects are few and far between
effort is minimized functionality is and
flexibility are maximized yeah
that's from book green architecture from
Robert C Martin you can know him as an
Uncle Bob for example on Twitter
and again we are talking about some
measurements and some some values which
are affected by the architecture
if I put it to some chart it looks like
that
the blue one is maybe something like
current state of your system I don't
know that's just example
uh we have some Human Resources we need
to do some change
if we are doing good architecture
we don't need so much human resources it
means one developer can
do more work in that system with good
architecture
and I I think that everyone knows that
it's hard to find developer for for Al
yeah every partner is struggling with
that we are searching for developers
anywhere
yeah we are taking anyone who is able to
write the code
just applying correct architecture could
save your
capacity on the people
the second things cost of change will be
all over uh
it means we are saving money of our
customer
because if they need something to be
changed it will not cost them
higher money in 10 years for example
defects there's there are few defects if
the architecture is good and you change
one pipe P somewhere
it will not break something which is not
connected with that part
if you have wrong architecture and you
touch something something else will
break yeah and even that part will save
you capacity of the developers and
Consultants because they don't need to
spend hours and hours
to solve different problems of the
customers just because someone changed
the layout of the report
and customer is going hey we can't post
now
why we changed only the the report
layout and who knows why it is not
working anymore
another part effort of course if you
have a good architecture you don't need
to put so much effort into the changes
and so on and with good architecture you
will have better functionality and
better flexibility
and those are two things which the
customers will understand
because customers need flexibility and
they need functionality
the covet
proved that
because the companies which were not
flexible enough
they didn't make it
if you just just imagine a restaurant on
beginning of the covet
who was flexible switch switched to to
deliveries make the eshops to send their
meals or sorts they meals to their
customers and so on it was really fast
change for them and if they were
flexible they are still working who was
not flexible
they they've gone from from the market
another quote
sorry
the goal of software architecture is to
minimize the human resources required to
build build and maintain
the required system yeah it means again
we are talking about the human resources
architecture have impact on that and you
need to be sure that really you are
doing good architecture because
elsewhere you are you are spending your
your capacities on something which is
not producing product productive for you
one more quad the the only way to go
fast is to go well
again on kebab
yes if you have good architecture
you are faster to implement the changes
because it's ready for you to
change the system
doing system in a way which is
preventing me from any changes is is
that end yeah if you hit something like
that yeah you just run away from that uh
decisions which will lead you to that
that uh that end
if you think good architecture is
expensive try bad architecture that's
very nice
sentence because
I think many partners went this this way
already and everyone who implemented nav
or a navigation before and maybe
those were bad architecture
which leads to things which I was
already talking about there the
monoliths which are not upgradable and
you need to throw them away and
Implement everything again from scratch
and again the the price the cost of of
the change we need to think about that
making passes and clean them is slower
always slower than stay clean
I don't know who says that but I know
that Waldo approves that yeah just ask
him and he will tell you yeah you need
to be to stay clean and do everything in
correct way because elsewhere you you
are throwing out the work of your people
from the window or and you are losing
your capacities on something you don't
need
if you want to know more don't forget to
to go tomorrow on his session about bad
habits of ir Developers
and
last thing no codes anymore but last
thing
we are creating software
software that's the part soft means it's
easy to change and software was created
to be able to change behavior of
Hardware which is hard to change
yeah don't forget about that we are
creating software it means really we
should be uh in a way uh that we can
change it easily and don't produce
Hardware
in in your code
okay
now prepare your phones for a short and
small pool we prepared for you
I want to know uh
[Music]
how you will see those two questions I
will show you
just scan the code and you can you can
vote on the pool
sorry Paul not pool
I you can
vote on the poll in your in your pool if
you want but yep the question is what is
better
software which perfectly works but it's
impossible to change
or software which doesn't work but is
easy to change
it means I have something it works it
have all the features I I need but I can
change it
or software doesn't work
but I easily change it
and there is one one quote that's you
know that's a software could be reduced
to one line of code which is wrong
yeah that's that's the software and we
can we can do that uh yeah
but I hope that that you are not
producing this line of code which is
wrong
I hope that you already
are pulling uh pulling sorry still
tablet is not working with me okay I
switch on the pool
ball
yeah I need to to duplicate that
that's pretty good I think it's very
good yeah
that's
okay it's not narrative moving anymore
we have over 150 people for the second
choice 23 for the software which
perfectly works
a good one
and I will go back to the presentation
which I closed accidentally
okay
the result of course yes
the software which is which doesn't work
but is easy to change
is better
yeah because we can change it easily to
work correctly
yeah
it's it sounds
I don't know first time when I I heard
that that's oh it's it's it's
interesting that something which doesn't
work is better
but yes we need the flexibility we need
to be able to change it easily even in
future and now if something doesn't work
it's just
question of few minutes or hour or
something to fix it and it will work and
you can add new features yeah I don't
know how many of you played Sports when
you're young I was taught by a bowling
coach I want you to bowl terribly your
very first thing you should do is learn
how to do it wrong the same way every
single time and I thought that was one
of the weirdest ranges of strangest
pieces of advice I had ever gotten but
the difference was is that if you are
consistently doing the same things they
are adjustably consistent so if you're
using the right techniques the right
patterns the right designs even if
you're not getting all those happy
little green Tech check marks for all
the tests you're all writing right then
at least you've got the pattern and the
structure in place
yeah and if you are doing some
architecture of course on on beginning
it is slower until you get the that into
your fingers when you're typing the code
and then it's faster faster faster and
and it starts to be part of of your
thinking and everything okay
okay it means cost of change matter
matters and design matters
don't forget about that short
intermission who knows what Eisenhower
Matrix is
hands up
few people okay that's good something
new for you yeah if nothing about the
design we will give you something else
hey it's good then at least Eisenhower
metrics and you will see you will know
how to manage your time
now uh Eisenhower Matrix is about
important versus
urgent things in your life during your
work or during your your everyday uh
schedule
it looks like that those are the three
variants of of the same thing uh
one axis here is
not working one axis is important things
that's the top line of
[Music]
the chart
not important things are on the button
urgent things are on the left and not
urgent on the right
and what is telling us that Matrix if I
have
urgent and important thing
I should do it that's the high priority
task I need to to do
if I I have important but not urgent
thing it means it is not urgent now
maybe it will be urgent in few days yeah
but it is important
I need to think about it and maybe
schedule it for later
but I will need to do it I just plan
when I will do it it is not urgent it
can wait for a while
urgent but not important things
that's I need to do that now but who
cares about if it's not important but we
tend to do these things
yeah because we like the urgent things
they are pressure there's pressure on us
and we are just trying to do that but
but then someone will
just say why you did that nobody wanted
to to do that it's not important the
downside the team's Integrations yeah
it means not an important and Urgent and
not important and not urgent things
those are the things which we like to do
because they pleasure us
but you are just losing time on that
don't do these things if you want to use
your time productively yeah not
important things and not urgent things
just just delete them from your your
life
and it have One impact because important
yeah we need to think about it again
sorry uh just the example
there is a fire
and of course it's urgent thing yes you
need to call the fire department it's
urgent
because you need to call it now not
tomorrow or something then you will
write an email far far yeah help me
that's a call for the help of Fire
Department
but important
yes it is important if you are in danger
then you will run or use the fire
extinguisher and and so on if it is not
important because the fire is over the
street there and who cares if the car
will just uh
be totally destroyed by the the fire uh
it's not important for you then you have
delegated it already to the fire
department and you can continue with
your work and that's the difference
between features
and architecture
because features are
urgent things mostly because
customer and managers wants them now
or at the best yesterday
yeah
but architecture is important thing
architecture is important because it
have impact to the Future things to the
Future costs of changes and and so on
and because one is urgent and one is
important there is a tension between
these two things
and if you know about that it will be
easier for you to solve these things
because features are urgent
architecture is important
managers and customers want the feature
but we tend to prioritize the urgent
things it means the features
and we are forgetting about the
important things
and this is architecture and that's the
reason why we are producing features and
we are not thinking about the
architecture or we are pushing the
architecture uh somewhere okay we will
think about that next week not not today
we don't have time for that right now I
need two features because the customer
is going live tomorrow
no
architecture is important
and mostly the features are urgent but
not important it means you can delegate
them to someone else if you have someone
like that yeah me as a manager I will
delegate that features to my uh young
developer and I will just focus on the
architecture I will tell him how it
should looks like the rules for the
architecture and he will implement the
future I don't need to implement it I
will just think about the architecture
for him because he don't know all the
things around for example
but architecture is
important for everyone in the team
it's not problem of just architect or
consultant
it is things for everyone in the team
developer consultant architect of course
not manageable because manager just just
hired developers and Consultants to do
that work because we don't need to
understand the architecture
um it means the development team is
responsible for for the the architecture
don't ask your manager if you do should
do it in that way or or that way it's
your responsibility to decide the
architecture because you are thinking
about the cost of change in future and
that it will save your work in the
future
manager needs to know that it will be
cheaper in future for the customer or or
even for your company to do that these
changes and so on but we will talk about
that later
Again The Matrix don't forget
architecture is important features are
are only urgent
we will talk about some principles and
these principles are in Upper you can
apply these principles uh on
different levels of your code about you
can Implement them on a level of
functions objects
source files or modules applications or
or some Component Solutions which are
composed from multiple applications for
example together it doesn't matter we
will mostly focus on the application
Level but you can apply them everywhere
in in during the the development
so one of the challenges whenever you're
thinking through principles design rules
architecture is it's hard to hang those
ideals without there being some sort of
story to connect that to especially
since most of you are going to be going
back and trying to explain some of these
different principles to people so what
we're going to do as we go through each
of the principles is we're going to
follow along with a company that we've
invented that is a monolith they've gone
through the traditional process of you
make a big giant solution it's one big
pte they had initially exactly what they
needed they could book little bouncy
castles for children or fun adults for
the day and they've expanded to add some
new lines of businesses but they know
that they're growing and growing and
there are many different booking systems
so they know that they need to break up
that monolith all of the stuff is
Tangled together with that booking
system so there needs to be a plan and
the principles we're going to go through
is how how do we break that up for that
company and it reflects a lot of
different projects that we've worked on
over the years taking that Journey
version by version
to getting a good solution
it means yeah let's so I miss you amuse
you company
okay
and now we will talk about the
principles we want to to to show them
and to introduce these principles to you
and we want
to to offer these principles to to think
about every decision you will make
during the development and think about
these principles how they are impacting
my decision now what will be a fact if I
will break that principle or if I will
apply that principle
these principles are part of a solid
framework or solid principles which were
described for example in the book clean
architecture from Robert C Martin
and the solid are the first letters of
these principles we will talk about
single responsibility principle open
close principle a list of substitution
principle interface segregation
principle and dependency inversion
principle
okay begin with the first one single
responsibility principle
what you can imagine under that
I will try to demonstrate on the car
that's the single responsibility
principle which is not used in that car
yeah
can you imagine that this principle was
not implemented in your car
that there is only one driver
responsible for driving the car
oh it will be very very big boom I think
after you you start the engine and start
your trip yeah it means that's the
responsibility principle in in reality
in car uh if we break that and we are
doing that in a software development
every day
yeah we are breaking that that principle
and then solving the effect of that
what is telling us a module should be
responsible to one and only one reason
to change reason to change is I'm
changing it because for example
that process needs to be changed
I don't change it because another
process needs to be changed in this case
I can have a conflict
and it means I will change it because
that process changed and then I will
break the second process because it's
using the same part of my system
the part was responsible to two masters
if I tell it in that way you can't serve
two masters you don't you you know that
that's the responsible single
responsibility principle different
definition is targeting that module
should not be responsive should be
responsible one to one and only one user
or stakeholder it means if you have one
end user who is responsible for some
some process
there should not be any other user
telling you please change that app for
me because I want something to be
changed there
same for actor if you if you identify
some actor in in your app for example
some doctor for which you are doing
something or or uh
the one who is doing the reservation of
your e-card tracks or something like
that or banza castles there should be
only one person responsible for some
part in your software
what is module in our case module is
unit of deployment mostly it's app it
have own version and you are deploying
separate app that's the module but again
you can Implement that on any level and
for example function could or should be
responsible only for one thing too yeah
if you break that you can have possible
problems
uh so if we take our example and we look
at the company that we were talking
about if we start looking at their
organizational chart they've got four
managers we know that they have all
these different needs that are all being
served by one monolith so right now when
we have to ask the question of what
should change we have to ask all four of
these people so our first pass on the
solid principles is to go what are the
individual extensions as far as who's
responsible for them when I at the end
of the day have to pick one person to
say yes or no to a feature change who is
it so we break it down by organizational
structure and then we start with that as
our first pass to create initially the
framework of what are all the different
parts of the system that we need to pull
out of that monolith
yeah and that gives us
maybe a better plan than monolith I
suspect a number of people have built
something along these lines where he
said okay well we've got these five
different lines of business and all of
them need to make use of this booking
system so we'll make the booking
the Baseline app that all of these other
apps are dependent on that's going to
work out right
uh remember that they want to remove
bookings later so that's not quite going
to be the plan we need yet yeah
it means
if we are thinking about single
responsibility principle uh
you can Implement everywhere
standard example of breaking that rule
where reservation table
what is responsibility of reservation
table
reservations and item tracking yeah and
why
that was not changed until now because
it's hard to do something with that
because there are two responsibilities
and if you change one you will break the
second yeah that's that's hard thing of
course monolithic applications again who
is responsible for the monolithic
application
if you want to ask someone if you want
to change something
who you will ask you will need to ask
everyone if it is okay for them also
yeah because there is or or no one and
you will do it and someone after that
will tell oh something was broken for me
yeah you didn't tell me that you want to
change that and yeah
that's the single responsibility
principle
and what can help you ask what is the
responsibility of the app or function or
component or object if you are thinking
to modify it you need to know that what
is the responsibility who is responsible
for that part
is he accepting that change yeah or have
some some additional info for example
for that ask the questions
you can add this information to your
user stories in devops for example to
see that who who is responsible maybe
it's responsible the one who is assigned
on that user story and then if you
detect that you are implementing two
user stories on one app and each user
story is have different uh responsible
person then ask these persons if it is
okay or there is some conflict or
because there is possible problem for
you
and don't create multi-purpose objects
table and apps definitely not the tables
which are having multiple fields and
based on some options some Fields is
used for that record something is used
for that record because you need to save
three ID tables because the customer
will not buy any other
package of 10 tables into your the
license I just helped the customer
upgrade a monolith application where
they had a table literally called the
multi-function table which had a primary
key of just two codes and a description
and they used it for 50 different
settings Pages yeah I know most of us
knows these cases yeah when when the
architecture was sacrificed just because
some money must be saved somewhere
but you will pay it multiple times later
another principle open close principle
what does it mean open close okay we
have a
truck which is uh
components of two things yeah there is a
tractor and semi-track a semi-trailer
sorry the semi-trial is is the second
part of the track first is the tractor
and open close principle is saying I can
change the semi-track without need to
change the tractor in this case I don't
need to change anything on the tractor
to be able to connect another trailer to
that tractor because there is something
prepared for that yeah and I don't need
to to change anything in in the closed
system of the tractor itself software
artifacts should not should be open for
extension but closed for modifications
and if you think about that that's IL
that's what we have we have core app
which we can't modify but we can extend
it
yeah that's the core principle of Al
changing by adding not changing existing
and we need to to use that uh principle
but you are using that principle already
you didn't know that it have name and
now you know that it have name and it's
open close principle and of course there
are some tools which are helping us with
that for example valdo's generic method
pattern here who is implementing that
you know that you are implementing that
to be open for extensions
yeah because you are closed and you
don't want others to change your app but
you want to extend them by some ways
even think interfaces standard way how
to extend your application without
changing it that's the open close
principle separate the functionality
based on how when and why it's changed
and organized the separated function
into hierarchy of components it means
you have multiple applications which are
depending in some ways on each other and
doing that that hierarchy
and there are some some rules we will
talk about them and it's based on how
and when these applications are changed
and so on
and that's another one yeah uh if we are
doing that that hierarchy we are doing
that high level policies
Central concern business rules
and peripheral concerns which are
specific implementation somewhere or low
level access for example to to some
printers
the apps are depending in some specific
Direction yeah and this these are the
rules we can apply and we will talk
about them later low level is mostly
depending on the high level application
it means core application
from Microsoft that's the central
business rule application of the
solution
those are the rules which are applied
through the system how the sales order
is changed to sales invoice and sales
invoices posted to GL entries those are
the basics rules and you can't change
them that's why you are depending on the
core app not core app on you
because
that's the the highest level and lower
level is some process doing something
which is okay if it is not working it
will not break the functionality of the
rest and Company for example could still
work
okay so taking that open close printable
example which we're doing better than
the workshop most of you folks are still
awake we lose a lot of people by the O
uh in the open close principle example
the partner implementing the booking
system they're doing what they should be
they're creating a whole lot of events
that makes that component extensible
they can do that many of you are already
doing that today so that seems to make
sense in this plan that we had built
we're going to create events for on
booking canceled on booking confirmed
all sorts of different things so we're
keeping that open to the possibility of
change a quick aside I'm going to steal
a little bit of Waldo's performance
information
if you are publishing events and nothing
subscribed to it there is no cost to
Performance he did lots of testing on
that there is no harm for performance to
open this application up so make the
application very very open to those
possibilities but as we went through in
detail in the workshop also verify if
you pass off information to events you
don't know what you're going to get back
so be open but don't necessarily allow
people to make the changes directly in
things yeah don't expect that the
subscriber will play nicely for with you
or rather validate everything you what
you are getting from that subscriber
back to your code yeah that's on you and
you are responsible that you will not
fail if something wrong is returned to
you or you will react nicely for that
for example with nice error message
someone give me something I don't know
what is it yeah that's on you how you
will handle that that situation but be
nice and if you are consuming you are
extending another application be nice
and play nice with that application and
keep their rules uh how to extend their
applications and of course everything
like like that is helping us as a
Partners if we are Partners to con
interconnect our Solutions together and
of course if I'm partner responsible and
I have single responsibility in my IPL
because no other partners is responsible
for my ad
I'm responsible for adding additional
even if someone wants to extend my app I
will put that even there without no
problems I don't have any problem with
adding that event why not I'm happy that
someone else will use my app yeah that's
yeah use it I will put it everything
what you want not everything please yeah
but what you think that is good for you
of course and if someone wants something
which is against your your design don't
put it there solve it in in a way to
keep your design nice and clean and and
simple be careful with is handled yeah
and you know that it's it's really
a good
good habit to be able to say no
we are mostly saying too much yes to my
to our customers for example and then
the customer is saying why you allows us
to do that
you are the expert which should say no
to to that okay you will try once and
they say but we want that yeah okay but
we taught you no not to do that
open close to municipal use the known
patterns to open your app for
dependencies
of course uh I think you you already
heard about the website which is uh
created just to to describe different
patterns we can use in business Central
uh just open that that that website go
through the patterns uh let your other
developers know these patterns and apply
these patterns of course think about
that if you are not over thinking some
things and you are not doing things too
much complicated but they are really
good patterns to follow
that might be a good in the room poll do
does everyone here know about the
patterns website he's referring to that
show of hands
so that was pretty good conversations
okay for the folks in the room who don't
know alguidelines.dev
bunch of best practices it's all GitHub
populated anyone can contribute best
practice and patterns yeah and if you
have good practice then just describe it
there share it with others because it
everyone will will gain something on
that
do not change the existing code if the
kind of the of the change is different
that the original code it means don't do
anything in the code if the change is
totally doing something else because you
are introducing another responsibility
for that that function and there will be
conflict in the future for example a
rather extend that application with new
application and you will not break that
one until you will add new functionality
through through new app which will play
nicely in your in your system
check if the dependency is incorrect
directions
the low too high yeah it means
application which is not so important is
depending on the important one
things which are just low level access
to some external system
for example integrating you with
external Warehouse system
these applications should depend on
other applications in your in your in
your solution which are implementing
business rules
yeah
specific to generic it means specific
implementation of something for example
protocol for sending sms or emails or
something like that should depend on
generic applications which are just for
example implementing some interface for
sending some notifications those are
generic things and specific things
oops
uh not stable to stable what is stable
application stable application is
application you are changing maybe once
per month
because you are just doing some some
cleanup
that's stable one because for example
it's implementing business critical
things and the business critical things
are not changing every week
but maybe you have something else some
up you are changing every week because
every week some customers or the
customer claims and say okay can you add
this field here and this field here and
you you edit this field last time but we
don't need it here but it should be
there this is unstable application
um doing that unstable application
depending on the stable one
you are
protecting the stable one from the
changes in that unstable because the
dependency know nothing about the
depending app yeah if low level depends
on High level high level up know nothing
about the low level it means if you
change low level it will not have effect
to a high level or should not have
if everything is okay and design is okay
next principle substitution principle
if we have a truck
we can change the trailer on the track
without changing anything on the tractor
yeah it means we can just Substitute
part of the system for something else
and the rest of the system will not
notice anything about that change it
will still work it have no effect on the
tractor okay maybe he needs to hire a
performance or something to to to keep
the speed with the same with more heavy
uh semi-trialer but yeah it will work
you can substitute part of the system
without effect to the sub to the
functionality
introduced by Barbara lishkov in 1988
that's a principle from 88.
we don't know about that now we are part
of the of the world of developers and
they are knowing that principle already
so long yeah why we are not not
implementing that we can
you can replace one part without
something with something else without
need to change on the pending part
without change of behavior and if you
implement that it allows you to
for example totally change one part of
the system how it is programmed or how
it is working just take it away put
something new there
it will not have effect to the system it
will not break anything it will still
work
for example now from my head
what is good example of holishkov
substitution in principle
the thing which we are now going through
since Microsoft bought nav
Microsoft totally changed the framework
behind an AV and uh and business Central
it's still work
mostly
it's still work same code which was
there 20 years ago it still work
yeah it have no effect on the function
of course we needed to change it on the
ways with many things but in general
it's changed part of the system without
effect on the rest of one yeah nice
example I think it's of course if you
just forgot the details
originally about support super classes
and subclasses but could be applied on
Al and the solution for risk of
substitution principle is interfaces and
events
because we have them we can do that
because we can do the
dependencies in different directions and
then it allows us to take something from
the system and put something else there
violation of substitutability cause
pollution with a significant amount of
extra mechanisms it means if you see the
code if then else if then else if then
else or if something is something else
then do something and if it is something
else a case and so on
those are
marks that you break that principle
so to apply that example when we talked
about we came up with this first plan we
said okay we're going to break up all
these applications they're going to
depend on the booking system when it
comes time that the company is going to
replace it with a web-based one instead
of a BC based one
uh we pull that out
oh
so often as a partner you go okay well
forget that we can't break it up in that
way that's obviously not going to work
for us so we'll build a big common like
shared application and for older
versions for performance reasons we're
going to stuff everything in there
that's data related we'll put tables and
extensions in there but all the
functionality is now nicely separated so
later on when I'm going to pull the
booking system out
in theory as far as the dependency tree
is concerned we're not going to have a
problem right should be fine
unfortunately they've just moved the
problem to somewhere else we'll see
so
when we move things down to the common
we try to be smart about it we say okay
we'll make in the common layer some sort
of management code unit already a danger
word for those of you who haven't heard
the term Swiss Army code unit
uh yeah management code units are a sign
of that so in that case we have a
function in here that the bounce units
will call to say okay I know about
bounce and when that event gets called
by the Bounce app
it will fire an event and bookings is
listening for that event so I've now
decoupled those two extensions they
don't know about each other this should
solve the problem right
should now when the booking goes away
bounce is still calling that function
the event is still firing but we don't
have a problem anymore
we don't have a booking system connected
to BC because we haven't replaced it but
we don't have errors so now that we've
broken at least one of the dependency
hooks that's in here that prevents us
from easily changing an individual part
of the system
and that massively reduces
one of the big costs
regarding substitution principle if you
tend to put new if then else or case to
make something different in some num
options yeah if my enum is that do
something else
consider using interfaces yeah
classical example sales line type and um
and the code which is connected to that
sales line type if you are posting item
or posting GL entry or resource or car
or bike
you will see in the code many if then
else or cases which are solving that if
posting for items should be posted
during the posting or something else if
there is implemented interface you will
not have these cases it means yeah if
you tend to put the case like that then
consider interface use interface
whenever it's possible that
implementation of the specific process
function
could be different for different cases
I had a case with my colleague he
analyzed one customer's needs a customer
told us that he need six processes to be
implemented
okay so six processes it will be so long
that to implement that we don't have
capacity for that and my colleagues
analyzed them and found out that these
six processes are in reality one process
for six different things
it means same steps same tasks were done
with six different things once it was
fixed assets once it was item once it
was some job it once it was some task
somewhere else yeah it means we import
we can Implement one process
with some interface and Implement six in
specific implementations for this
process
do not depend on the specific
implementation if you are doing
something like that develop the process
for unknown
yeah if you take sales order and you
will uh create the process of posting
sales order for unknown sales line yeah
I don't know what will be sold if it
will be item car or car or something
else I will do it in generic way
and then I will implement the specific
implementation of the interface for
items for resources for something else
try to think about unknown things
replace these specific things for with
unknown and you will be more generic
if something should be interchangeable
of course the inputs cannot be stricter
if it means
if there is some implementation which
allows only uh minus 1000 to 1000 the
new replacement cannot accept only 100
to from minus 100 to 100 because it will
error out if my generic process sends
500 there it will fail it means it
cannot
stricter the inputs and outputs can be
wider because the rest of the system is
accepting some values and now you you
you send back something which is out of
the bounce that's will fail
next principle and we are going to
narrow it to the end there is only one
principle of
in front of us after the interface
segregation principle interface
segregation principle I was thinking
hardly how to explain that on on cars
but I I came with that example we are
working on something what should work
with cars in generic cars yeah any car
on the world
I will create some interface working for
cars having some functionality for cars
and now I have truck and now I have a
personal car
I need new functionality which is
available only for the trucks
I should not put that functionality into
the same interface which is for all the
uh the cars
because
interface segregation principle is
telling us that the the client should
not be forced to depend upon interfaces
that that they don't use it means if I
put some specific functionality for
tracks and I will Implement that for
personal car I will need to implement
even that function for the trucks which
have no meaning for personal car
I'm polluting the interface with
something what is not used with all the
clients
and it
the same principle works for the
dependencies yeah we don't want to
pollute application with dependencies on
other application if the application
needs that only for one small part for
example
yeah so to bring us back to this example
you know we had the bounce units calling
this little management function and that
threw an event and the event tells the
booking engine okay we have some info
this unit that is going to be booked
it's no longer available well you know
the VP of the paintball fields has
decided we should also have the ability
when we fire this event to include the
list of all the players that are coming
that day so I want you to add to the
interface a list that I can then
theoretically in the event of bookings
read that out send off information to
lots of different people well that's
really cool and all but if you remember
correctly our bounce management also
uses that same interface and so now
we're having to provide an empty list
for something that doesn't matter it's
not relevant to that so the idea of this
one is that if you are creating generic
interfaces they should not be polluted
by functionality that is specific to a
particular regular module or part of the
system
yeah that's the case when you extend
such an interface you are forcing all
who Implement that interface to
implement this new function even when it
is it have no meaning for them and they
will implement it in a way that maybe it
will break your your processes yeah
that's the pollution and you don't want
to do that Roger you will create new
interface
which is only for the the paintball
fields and have this new functionality
and then if you have some specific
paintball fields because for example you
have outdoor paintball fields and indoor
pavement Fields they will have this
functionality implemented and will use
it but no others which don't need that
functionality
if applications are Loosely coupled and
now I'm talking more about the
dependencies than just pollution in the
interface if applications are Loosely
Loosely coupled don't make them
dependent it means
if I have application oh sorry I will go
to the
I don't have let's picture that okay
sorry uh
if I have a application A and B
and I want to have them dependent a
depending on B
and
when I remove B
H still should work
because they are not not tightly coupled
or they are Loosely coupled the
dependency cannot be there
think about that uh each time when you
are adding dependency think what will uh
be effect of removing that dependency
because maybe in future you will not
have the bookings and you want to remove
the booking what else must be removed to
be able to remove the booking if you
need to remove even something which
should stayed in the system the
dependency cannot be there between these
two applications because you are
polluting
these dependencies with something which
is not uh needed for that use dependency
only if the functionality is tightly
coupled you yeah only when
the beach don't have meaning without a
if only part of the app is tightly
coupled because for example you have
application and only one report needs
some some field from another application
and the rest of the application don't
need that don't put that dependency for
all up because as I thought if I remove
B I will need to remove for all a
but I won't just remove maybe the report
which is depending on that yeah just
split that app remove that report from
that app put it to separate one that
separate app will be depending on on the
application with with the field and
connect these two applications in some
some way which will not prevent you to
from removing uh these parts when needed
keep interface minimal now we are going
back to the interface keep it minimal
don't pollute it with unnecessary things
for specific things create new interface
that's just uh repeating what I already
said
and last principle
dependency inversion principle
I think you already
you are using that principle but maybe
you even don't know about it but
we will see later I think definitely
at least most of you are using that
principle
how to describe that on the car you have
fuel tank
and fuel tank wants to notice you that
there is no fuel inside
knows nothing about the dashboard you
are using in your car
yeah
and he need to somehow say to that
dashboard that there is no fuel because
you can have that dashboard or that
dashboard you can have Tesla or you have
something else okay Tesla don't have
filter in Korean
we have batteries for example in that
case Okay uh knows nothing about the
dashboard it means the dashboard is
mostly depending on the fuel tank
but the fuel tank is signaling us
something it means the dependence is in
opposite than the the flow of the
control
and that's the dependency inversion
principle you are changing the direction
of dependency
normal is to have dependence in same
direction as flow of control a call B
then a is depending on B and call the
function from the B that's the standard
situation
but dependency inversion is changing
that that that directions and it is tool
which help us to implement previous
principles open close principles risk of
substitutional principles and this this
kind of things and solution for us is
events and interfaces again
yeah at the end you see that we are
talking mostly about events and
interfaces nothing more
but
it's more complex things to think and
use them correctly yeah that's the
example a call B A depends on B that's
standard situation opposite a COS B but
B is depending on a how it's possible
because a call just events a publisher
and know nothing about the B which is
subscribing that event and answering to
that event when it is fired it means a
is protected from changes in b
in first example B is protected from a
because B know nothing about a
but because there are some rules we were
talking about that that high level and
low level applications business rules
versus peripheral things and these kind
of things we need sometimes to to switch
that dependency Direction and dependency
inversion principle is just about that
so
maybe you've gone down a different Road
and you said okay well we're not going
to make all of these extensions
dependent on a common app we're going to
try to keep these all separate very
interchangeable it's very easy to
accidentally go let's make bounce depend
on the bookings well as we talked about
that will break things we know that it's
still fragile that way we remove
bookings things go terribly wrong so to
fix that this last piece which I think
is the part that's a little bit new to
people I hope that most everyone else so
far has been going yep that's all
familiar what's the new stuff here the
difference here is this dependency
injection means that we create an
extension that makes the connection
between two disseparate modules
by being able to use enums and their
ability to implement interfaces we can
tell the lower level applications that
we depend on information about other
parts of the system
so what does that mean for us as
developers this means that in the
bookings application we would create an
enum that says what kind of type of
amusement is it and we create an
interface that has all those different
event calls that we might want to be
able to implement all those functions up
in the bookings bounce module that sits
dependent on those two things we can
then inject into the bookings module a
new enum value where we say okay there's
Now a type field that knows about the
bounce we can update the table
relationships we can update and
Implement new code units so that way
when things happen in either of those
modules they're able to call the generic
implementation of an interface object
and fire an event on that just quick
check of the room because there's a lot
of people in our workshops that had not
done enums and interfaces who has
written one of those yet
oh thank goodness for those watching the
recording later that was actually a
pretty good number of people so the
advantage of this is that by creating a
little micro extension on top of two
disconnected modules neither of these
applications have ever heard of the
other one
that means that later on if we decide we
want to replace the booking system with
something else
the cost of the change is to click
uninstall
bounce no longer cares it's never heard
of it we click uninstall both of those
extensions go away our system is done
it's ready
no problem we pop in a new extension
that connects to a new system
so we created a little extra
infrastructure up front to create
separate booking system create separate
bounce and we created a third little
extension which by the way in our
Workshop it was five objects total
it's a very small extension very easy to
manage
that little thing saved us the effort of
later on we don't have to worry about
our 60 customers in the wild of how do
we update all of those customers because
now we've changed the dependency tree
they don't have to know about each other
they don't ever have to meet each other
by investing that time in creating the
Loosely coupled injected dependencies
we save costs in a very big way past
year one
yeah it means the dependency inversion
principle is for us I think uh the most
used principle from all that and now you
will know that you are using that if you
are implementing interface or events and
so on and you you will know if someone
wants to add dependency in your solution
in Direction which is not correct you
will say okay no no no no
and he was like but I need that because
I need to call that function from that
that application yeah but dependency
inversion is allowing me to make the
dependency in opposite direction and I
will just Implement some event and some
subscriber and I will solve that problem
and keep the architecture nice and
simple
okay maybe if on the first side it will
not be so simple but it will be simple
for maintenance
if you find out that dependency should
goes opposite USE events and interfaces
to invert it specific to depends on
generic specific application
depends on the generic thing it means
the the bridge is specific thing it's
solving specific connection between the
two apps but the bouncy app is generic
thing that's why the bridge was
depending on the bounce bouncy
application low level depends on High
level low level for example integration
with external system that's low level
application high level is some business
process unstable unstable already we are
talking about that if you change
something really often
put it at the end of all the
dependencies it should depend on others
but nothing should depends on that
application which is unstable because if
something depends on unstable app it
will be unstable too and you should
check each time you change that unstable
app you need to check again that you
didn't broke something on that depending
application
if we want to protect a from changes in
b b must depend on a that's the core of
the problem here yeah
dependency could allow us to protect
some app
from changes in another app
the bridge was something there
and because we were we had no
dependencies between bookings and and
bonds
they were protected
and the bounce and booking was protected
from change in the bridge app because
Bridge depends on them it means if I
break something in the in the bridge app
it will have no effect or should not
have effect on the booking and on the
bounds and they should work okay maybe
some process will not work because they
can't post something about the bouncy
but for example posting about the the
paintball fields will still works
remember the open close principle it's
it's uh connected because in open close
principle we were talking about
dependencies too
and don't be afraid of that
don't be so be solid try to implement
this this these principles in into your
work yeah
if somebody tells you no no we don't
have time for that
you will never have time for that
until you start to implement it and you
save your time because you will have
correct architecture in your Solution
that's a circle you need to to to stop
some someone yeah nobody have time for
architecture until the architecture is
in place and you save time on that and
you you can do that but you need to
start some but you can start
step by step so if you don't need to
start with everything now step by step
try to think first about the single
responsibility things don't don't
introduce multiple responsibilities on
different ways then start with some
something else and step by step make the
architecture better yeah
one of the questions that we got a lot
in the workshop is okay this is
interesting it's novel it's kind of cool
there are some parts I like about it as
an aside all of the code that we created
as part of that Workshop including the
bounce application all of that uh the
completed code will be on my GitHub next
week you can crawl through it have fun
with it play with it but the question we
got from Workshop attendees is okay I
like the ideas of this but I have to go
back to a job
um I they're not really that interested
to hear about the cool new plan I have
to break up this monolith they don't
have the time we don't have the interest
we don't have the resources so for the
folks who are going back to report to a
product manager or a department manager
they ask a question of how can I
convince that person that architecture
matters because that was the point the
architecture matters we have to Champion
it because no one else will well start
small
and start from the outside moving the
way in just like testability where you
can start small by targeting support
cases first start little make those
little changes so uh clients that are
working with printers web shops
Integrations these are your first
targets because they're that outermost
layer they're the they might be Core
Business application but they're
connecting different things so work your
way out to in what are the advantages
you can tell one of those folks in
charge is that those small changes those
little Bridge apps they're tiny they're
half a dozen objects those are much much
easier to delegate to people
and you can delegate them to Juniors you
can delegate them to external it helps
you bring people that are new to the
product and say let me teach you all
about building Bridge apps and you're
going to be my bridge App Guy
I don't have to ever think about it
again wonderful and they're reusable
they're often very very simple patterns
that you can just rename the fields
rename the tables move on with your day
we have talked with a couple of
different partners in the channel for
example that are isvs offering Solutions
on appsource that because they followed
this careful architecture around making
their code open making it possible to
inject these dependencies they were able
to create scenarios where they built
between them those connection Bridges
between their disseparate products and
as a result when they go to do demos to
customers of their product they usually
show The Other Guys stuff
because the customer sees this is a
complete solution I don't have to spend
the time and effort to go okay I didn't
have ship it they work with tasklet
Factory I don't have to wonder how does
my warehouse guy scanning this code get
to the shipping organization it's just
built in
it comes pre-installed so that makes a
real strong case of if you architect
things you potentially can sell more
well that's nice and all but then also
there's the uh okay lots of us have
clients who's going to pay for this
clients aren't going to want to who's
had luck with getting clients to pay for
testing automation
I I saw one quiet embarrassed person in
the back
so when it comes to selling solid you're
going to pay for it just like testing
later you might pay for it later and if
you're working with a client
organization where they have lots of
turnover they might go great I'd love to
pay for it later thanks here's the
credit card
but if you invest in that architecture
up front you pay less overall that bar
stays flat that whole time you don't
have those huge jumps
uh I'm working with a customer right now
that's breaking up a monolith we've done
the cost projection of all of the
different things that we've done over
the past three years to their monolith
the time spent on defects the time spent
on figuring out different changes the
time spent in team status meetings get
three different managers to approve each
change we've done that cost analysis and
it's going to actually cost them less
money to have us spend all the time to
break up that monolith into the apps
because they were willing to look at the
three or even five-year Roi of does that
time actually get me anything yes later
it gets you a bigger budget that you can
put into let's do some new good stuff
let's not just spend money to keep the
lights on so it's easier to do big
changes it's less time that you're going
to spend on defects because customers
spend time on defects too the trucks
here I can't print I need to ship
and then of course we also get into the
fun wonderful world of some of you folks
are going to go back on Monday
yeah we're not ticking along here
and some of you are Junior devs and
you're going to go back to the senior
developer and go I've got this cool plan
and they're an old nav fossil like we
are and they go I don't have time for
that nav was better whatever I don't
want to hear it
we hear it too
um the segregation principle keeps you
from having to fix the fixes I don't
know how many hours I've spent going I
fix it and then more hours fixing what
just got fixed
it also becomes much easier for senior
developers who are a little resistant to
working with some of the new ways to say
okay well tell you what you don't have
to worry about building these connectors
to an API you don't have to worry about
oauth we just taught this new guy all
about building the micro application
necessary the Eventing structure
necessary to build the bridges to talk
to external apis you don't have to worry
about that you just worry about posting
code units
cool
so for those it's easier to break up the
projects and smaller becomes faster
because it becomes repeatable you're
able to be cheeky you can copy and paste
code from different projects and just
rename the tables you're pointing at and
it's also a heck of a lot easier I don't
know how many times I've debugged a
monolith and I got the wonderful
debugging messages where it would say oh
sure no problem the problem is on
function line 932 in this 3000 line code
unit
trying to find that is much much harder
and if you're building pipelines you're
going to be able to pinpoint exactly
where in the pipeline things are failing
much much faster so you can make the
case to some of these different people
with some of those different theories
and yes this slide deck is going to be
available later you don't have to have
taken notes on those so all of these
costs do build up someone is going to be
paying for those costs and it's if
you're not paying it intentionally with
good design you're going to pay for it
unintentionally with bad design
yeah remember the principles
single responsibility principle open
close principle holistic of substitution
principle interface segregation
principle and dependency inversion
principle
solid yeah don't uh forgo them
try to implement them try to think about
them and I hope that your designer
architecture will be going better and
better and and we will go forward with
same price for each change you will need
to implement in your system we have
seven minutes four questions I see
already some hands up for for the
question there okay
um just uh
to the topic about our state
um pollution of the apps because
um in in this example uh you showed us
it was one company so you developed
several apps for one company
so if you de-install an app it's not
relevant anymore for anyone exactly but
if you're working on products and you
say okay this customer don't need this
app anymore then it's not relevant
for uh it is relevant because another
customer maybe uses it
so in this case because you also
mentioned then
um the strategy that you say okay if two
apps are connected together just making
a third app
um and the third app just uses a
collector for
same procedures for example date
management or I don't know posting in
the same way
um
this is not the pollution then when I
just say okay I just move
functionality and in some customers
there's only one app existing this
doesn't count as pollution one of the
recommendations that we have on
pollution of interfaces if you haven't
used it yet or heard of it uh folks in
the room still the argument table
pattern is a fantastic way of giving a
consistent signature that is extensible
so that way you can consume only the
data you need and we recommend it a lot
in our Workshop that when you're
building a lot of those interfaces those
the pattern of handing specifically an
argument table that has all the
different values you need makes it easy
for depending apps to say I need 10
extra bits of info and they can inject
into that argument table via table
extension those new fields and the
application that depends on those 10
Fields can see that those are present
you'll find that there's cases in base
app where they do things like that where
they go if field number exists us then
we're going to do these things to make
it Loosely coupled so you can say it's
it's like a design pattern in the app
like a readme for example definitely
there are multiple solutions for each
case here the the dependency could
be in different directions or maybe it
doesn't need to be there and you can
replace that with some other other
functionality light using record draft
or using API and calling API of the
second app and making them Loosely
coupled without a dependency there are
multiple Solutions and the question is
you need to think about what will be
easier for you measured in the cost of
change in the future yeah that's the
main thing and the decision is on us
architect
if it is better for your company because
you are used to that maybe it's better
than someone else will use other way
because they are used to that way yeah
it means
architecture is not not uh exact thing
and you can see it everywhere that
architecture of buildings even when it
is same architecture is totally
different building yeah because
the the the one who made that
architecture made own decisions measured
by some some measurements and uh the
result is different it's really like
painting the uh the picture some some
picture or something if you have two two
people doing same
style of painting the result will be
different yeah even there are same rules
for example applied to that it means
maybe you have some ways which are good
for you and it's okay yeah if it fits
into these principles and I think it
will fit
why not
yeah the the thing with the um
designing pattern that looks good yeah
to think like a readme of it yeah
exactly okay there's another question
here
well thanks for the session first
um so we are a dinosaur company so we
have our solution as a monolithic thing
since 20 years and also being on our
journey so it's really nice to see these
patterns we right now have one funny
little case and I really wonder if the
bridge apps will help on that is
something like we have a cyclomatic
dependency between two partners
so while the one says I have something
for you you can get it the other one
says yeah we have something for you as
well you get it from us so um how to
apply a pattern on top of this one will
it be one bridge for both will it be two
Bridges which are going vice versa so
what would be your preferred way here
and who's responsible for it I I that's
I think the first question who will be
responsible for that yes yeah if each
one wants something what they are
responsible for then there will be two
apps and they were responsible for these
two apps and if there is conflict
between the functionality of these two
Bridges then they need to communicate
somehow yes yeah and say okay it's your
your thing or no It's Your Thing
yeah there is no other solution than
that but definitely yeah the the cycle
could be solved by the bridge or
something else uh but
first thing is the responsibility yeah
there can can't be at for which both
partners are responsible no it will not
work and that's the general idea of the
bridge app is you're injecting into it
uh whether you want input to go into it
uh which you can do via Eventing in the
receiving app or if you want to
potentially expose functionality that
then you can actively call and that
becomes those enums and the interfaces
so it depends a little bit the direction
of information flow and that sort of
thing but of course events can pass vars
back and forth so sometimes events are
their own little procedures and while we
have the last 30 seconds I do want to
catch one more question
our microphone cubes
um let's imagine I have a solution which
is kinda monolith and yeah I it's
difficult to extend and so on so which
way is
to move which way is better uh is it
like refactor this step by step until
it's I know a better architecture or
should I create a new one with the good
architecture and somehow migrate to it
great question and the short answer to
that is it depends of course
um but you can take both approaches it
depends on their willingness to invest
in the refactor before they move to a
new version I've done both
implementations where we wrote a whole
new extension framework and migrated
into that as a clean brand new start
because architecture is the reflection
of decisions passed if those decisions
passed aren't relevant anymore that's an
opportunity to do a whole cleanup
project and that's an opportunity to
make things a little bit better if all
of those decisions of the past are still
relevant then it's a great opportunity
to say let's migrate to BC let's migrate
to the monolith and then start breaking
pieces at a time based on those
different work our way out into the
middle of it so you can take a slower
process where you can take a monolith
over the next three to five years and
just break off parts and parts and
slowly work your way in and it's it's
what Microsoft is doing now we have to
modulate that now they are starting from
or started from the the system level and
put all the system things out of the
moon on it to separate apps and now the
new new things are already implemented
in as a apps it means new things you can
or should Implement in the new way and
in between start pulling other parts out
of the monoliths to break it but all
depends on the capacities and all that
things around but yeah that's more
thanks but thank you out of time so
thank you everyone thank you very much
hopeful that it was something positive
for everyone you will use it thanks
