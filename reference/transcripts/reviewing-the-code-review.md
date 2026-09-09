# Reviewing the Code Review

- **Source:** https://www.youtube.com/watch?v=v-EaIJ0f9tU
- **Video ID:** v-EaIJ0f9tU
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 91m12s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

I can tell you how how happy I am to to
be here because um I've done a couple of
conferences last year and I've done
quite a couple this year but I've never
had opportunity to speak at TAG days and
tag days was also my first conference
that I ever attended it was the first
conference that made me realize that
we're not just building some Erp
products but that there's more there's
the whole Community behind it
Soo I'm happy to be here and to all of
you welcome to reviewing the code review
I always like to start my presentations
by explaining a little bit where did the
idea come from why do I love talking
about code review so much and to
understand why I like code review we
have to take a quick tour through my
career so
far so far I've worked for three
different organizations I've worked for
a really small VAR partner it was like a
garage firm where we developed directly
in production database is right it was
the c times and honestly who in Cal
times did code
review yeah exactly only I'm proud of
all of you who did it but we didn't no
nobody did code review in those times
but then at some point I switched to a
different company I switched to the
biggest isv in Slovenia at that time and
in the beginning we were doing code
review my code was being reviewed and I
thought W this is cool but but in about
6 months code review just became another
green check mark on a on a pool
request and then I switched again to my
current organization where I think we
actually have quite good code review
practices we still we still have room to
improve right
but um I think we're we're doing a good
job and when I was looking through my
own experiences three different
organizations with three completely
different approaches to code review I
was thinking to myself well you know
what about all the other partners I
think we're all we have all adopted
various practices in the five years
since we got code review and I think
right now it's a good moment to just
stop and take a look at what are good
practices what are bad practices how can
we be better at code
review now before I go any further I'll
just take a quick minute to introduce
myself my name is Tina starich and I'm
originally from Slovenia though for the
past couple of years I've been flying
under the Lithuanian flag because I went
on a little career adventure of sorts I
work at compel where I work as an
architect which just means I don't only
deal with Al code day in they out I also
think a lot about the quality of
solutions we create I think a lot about
the quality of products we develop with
our partners or or or for our
partners and code review is like a tool
tool that I can use to oversee what our
development themes are doing what kind
of quality code we're
producing I've also just recently became
uh an MVP it was actually exactly 44
days ago 7 hours and 26 minutes I timed
it since uh I got the
email it's it's a really cool time for
me right now I love being part of this
group of individuals that that love the
product are enthusiastic about the
product and love to share the knowledge
with with all of you so yeah really a
fun period for me right now but back to
our topic what are we going to talk
about today we're going to go through
Five Points first why do we do the code
review I think all of us we have our own
interpretation of why do we like code
review why why it is important but this
is just for us to kind of establish a
baseline or that we all see oh these are
the points why we should do the code
review and then we're going to jump into
the process how can we make the review
process better less boring less annoying
how can we speed it up and we're going
to talk about the roles so how can I be
better when I review code and on the
other side of things how can I be better
when my code is being reviewed and then
finally I also needed to include the are
co-pilots going to help because anything
Microsoft touches added adds a co-pilot
somewhere
and honestly I hope you didn't come to
this presentation for that bullet point
because long story short it's kind of
boring right now but still I just want
to show you what what is there and how
co-pilots should help with with code
review but let's get to it first
question why do we do the code review
now I could talk about we do the code
review to ensure code quality we do the
code review because we want to follow
coding guidelines we do the code review
because we want to find bugs and edge
cases but I found a quote on Reddit a
couple of months ago that summarizes it
much better than these bullet
points what the quote said is ask
yourself if I had to support this in
production tomorrow with no previous
knowledge of it how tempted would I be
to send a glitter bump to the developer
who wrote it when you think like that it
really cleans up a lot of your code
right so why do we do the code review
because we don't want to find glitter
bump worthy moments in production with
code review we can catch all of these
glitterbomb moments before code ever
reaches the main
branch on top of trying to prevent
glitter bump moments another reason
that's close to me why why I like code
review is because it helps us avoid the
lottery factor of
one now you might have heard
it under a different expression we
usually say the buzz factor of one which
for those of you who don't know means
how many people have to get hit by a bus
before we have a problem but now people
getting hit by a bus that's a bit morbid
so I found a different expression how
many developers need to win the lottery
before we have a problem and now what
what I mean by this is I think a lot of
us we have experienced situations where
part of the code base let's call it
payments are owned by just one developer
and then each additional feature each
additional change request each
additional bug ticket goes to that one
developer because that one developer
architected it that one developer
developed everything and it's the most
efficient way how we can add a feature
to payments yeah it is the most
efficient way
but you know what's going to happen if
that developer wins the lottery or even
if they just want to go on vacation for
3 or 4 weeks who's going to take the
next urgent bug fix somebody's going to
have to but they won't really enjoy it
because they have no clue of the context
what what was happening with
payments but if we do the code review at
least one additional person will see how
the feature has been evolving what kind
of features have we added what kind of
bugs were we solving and then at least
one additional person will have a bit
more context and they will be able to
work with within this this isolated part
of the code base so why do we want to do
the code review well because we want to
avoid situations where we're completely
dependent on just one
person an additional Point why do we
want to do the code review is knowledge
transfer now you could say that
knowledge transfer kind of relates back
to my previous point right we we are
transferring Knowledge from the person
who developed payments to the code
reviewers but in reality what I meant by
knowledge
transfer is hm let me let me put it this
way who usually reviews code it's the
senior developers right senior
developers review everyone else's code
now this is something that I would like
our organization to improve we're not
there yet but I would like to include
Junior developers to be the reviewers as
well now not necessarily for the juniors
to question or challenge well not to
challenge senior developers decisions
they can if they think they found
something but more to just question why
have you done something right why have
you used a query object here when
normally we just use find sets and gets
and finds and that works most most of
the time just for the the junior people
to be more exposed to different
development practices to to best
practices to different development
paradigms so this is let's say a quite
important point for for me personally
why to do the code review well because
we can share the knowledge from more
experienced people to everyone
else so if we just summarize why do we
want to do the code review we don't like
glitter bumps we want to avoid
situations where only one person knows
the code base and we would like to share
the knowledge across all experience
levels now let's move on into oh sorry
let's not move on to the process yet I
have a disclaimer I want to share with
you I normally don't include memes into
my presentations but for this one When I
Was preparing a couple of months ago
every time that I found something
interesting I said I'm going to put that
in and this is the the first one there's
a couple more to follow but why do we do
the code review because we would like to
avoid void a situation like this where
the same person opens the ticket defines
the ticket implements the code reviews
the code merges the code and closes the
ticket yeah no with code review we split
those tasks a little bit
apart okay and now we come to reviewing
the process in this part we're going to
talk about how can we make code review
better more efficient take less time
now I do kind of expect that we all know
what gear is and that we all know that
pool requests are the place where we do
the code review so we're going to take
it the steps further from there and
first what we're going to talk about are
policies now with
policies it's the perfect way how we can
ensure that every code change that would
reach our main branch first has to go
through code review and I have a couple
of policy set up in my examples
today I know a lot of you already know
policies I know a lot of you are already
using policies so we can just use this
opportunity to talk a little bit well
why do we set this or that policy
up most of my examples are going to be
on Asia devops that's just because well
our organization uses aure devops but in
reality any every point that we're going
to be making today it's fully applicable
to GitHub to gitlab to just about any
Source control tool you're
using but let's go to our policies
now with policies we set them up on
branches that we would like to protect
from from those changes usually that's
that's main but it could be just about
any branch and we go to options and
Branch
policies and let's talk a little bit
about what kind of policies I usually
set up the first one being require a
minimum number of
reviewers I personally would like for
each pool request to go through at least
two code reviewers but I also do realize
that sometimes the projects are just not
big enough so One reviewer is okay but
at least one person needs to review
code I don't like the idea that
requesters would approve their own
changes I don't think anyone should have
the power to directly merge code into
the main branch even with with smaller
projects for example let's say my my
brother he has a separate BC practice
and he works for one End customer he's
the sole developer the only person there
and still he opens pool requests and he
tags me I don't have context of that
project I will never find a bug there
but even then I can still give him
comments like I think this could be more
readable I think you could structure
this better there's a new language
feature in al13 that I think you could
use here so I really don't believe that
we don't need code review there's always
a need for for a code
review I also uh always set up that when
new changes are pushed we reset all code
reviewer votes because even if I have
already accepted a pool request and a
developer decides I'm just going to push
one small change up
I want my vote to be reset and I want to
see what kind of change they have made
so whenever a new change is pushed my
vote gets reset I get a new email and I
can take a look at the the new
changes check for Linked work items now
this is this is something we're going to
talk a bit more later but the point that
I'll be making is we don't want to only
review the syntax we want to review the
change does the code actually solve the
problem it's trying to solve and we can
only be sure of that if we know what the
problem was and if we have a work item
attached to the pull request well then I
can go and take a look at oh this is the
problem you were trying to solve yeah it
solves it or it
doesn't check for comment
resolution always even if I leave
comments that I don't want the developer
to to address I just say hey this was
good I want the developer to see that
comment before we move uh merge the pool
request
in with merge types I'm not dogmatic
about merge types use whatever merge
types you would like to use but we have
agreed internally that we would like to
use squash merge because with squash
merge you end up with just one commit at
the top of git history which means
you're going to have quite a linear G
history and it's going to be easy to
follow now with all of the other merge
types you end up in situations where
some changes come from here some changes
come from here some changes come from
here and that's when it becomes really
difficult to to see what's happening in
our git history but like I said I'm not
dogmatic about it use whatever merge
type you would like to
use build validation this is where you
set up your pipelines we won't be
talking too much about pipelines today
because there were sessions on pipelines
and there are blog posts on pipelines
and there are books on pip lines and I
think all of that knowledge covers it to
a degree that we don't have to dive any
deeper today but what I would like to
show here is that whenever we do set up
pipeline
checks we ensure that builds expire
immediately when the main branch is
updated because if I have two pool
requests both of them have already pass
the the pipeline check and the first one
gets merged in I would like the the
pipeline check on the second pull
request to expire because maybe now
these changes are not compatible with
the changes on on this pool
request so the builds should they expire
immediately when the main branch is
updated status checks I personally I've
never used status checks has anyone here
used status
checks one and you're a bit too far
otherwise I would ask you how do you use
them now I I did Google this I still
wanted to share with you what are status
checks uh but um I was hoping somebody
closer would share their their
experience with with status checks uh
status checks are used when we have some
external process that our pool request
should depend on right we we know for
example if we build pipelines we want
the pipelines to pass before a pool
request can be merged and if we have our
pipelines in Asia devops we set them up
here but if we would be using some
external tool like Jenkins right for our
cicd that would be an external process
and when that external process finishes
only then can we merge all our pool
request and that's what status checks
are that an external service can say hey
yes this is okay you can merge this pool
request or no you
cannot finally we have the automatically
included reviewers so for for every
project that we have in asure devops we
create this group called code reviewers
we add all the people that should review
code into this group we add it here and
then whenever there's a new pool request
opened these people get notified of oh
there's something else that I should
review and that's as far as I want to go
with uh with policies I can just briefly
show you that once we have policies in
place we can see that I'm still on my
main branch here I added a workspace
file if I would like to commit this
workspace
file I can still do that but when I
would try to push this update
up this is when I would get an error
saying pushes to this Branch are not
permitted you must use a pull request to
update this
Branch but that's policies so once we
have policies in place we can be sure
that any Cod change that would try to
reach our main branch has to go through
code review
first now the next thing I want to talk
about our pipelines I said I won't go
deep into pipelines but I still want to
mention why are pipelines so important
for the code
review it's because they help us avoid
questions like does it build right as a
code review Vier I don't want to care
about does the application still compile
after this pool request now you could
say well the least the developer could
do is just check if it still compiles or
not and I agree but I'll feel much more
confident if there's a pipeline that
simply compiles the app and then I can
be sure yeah it compiles or it doesn't
compile same with tests as a code
reviewer I don't care if all the tests
pass because the pipeline is going to
check for if all the tests pass the
pipeline is going to execute all of our
tests and it's going to say some of them
failed address that
first translations same thing I worked
on a project where we had to do
translations on a pool request basis as
a code reviewer I didn't care if it was
translated we added a step in our
pipelines that just checked are the
translations done if they're not fail
fix that
first so why are Pipelines so important
because they help us as code reviewers
to avoid questions that we shouldn't be
thinking about when we're doing the code
review and on top of these let's call
them technical checks we can also
automate checks for if the coding
guidelines are being followed this is
where linters come into
play I think you know all of you know
linters but under a different name you
know them as code cops appsource cup
perant extension cup UI cop so those are
the kind of cops that ensure that we
follow the guidelines from Microsoft
that all of the page Fields need to have
a tool tip all of the page actions need
to have an
image so do I as a code reviewer care if
an action has an image or not I do not
there's a warning for that and the
pipeline will fail if that warning is
shown but you can take it even further
you have your own guidelines in your
organizations that you can automate as
well with custom linters with custom
code cups so this next part I want to
try to inspire you that custom code cops
are
awesome one of the projects that I was
working on was for this German German
partner that
had I would say a bit weird requirements
in how they want us to write code they
wanted to have Global variables prefixed
with a G they wanted to have exit
statements capitalized and now I'm not
here to argue with you should we prefix
Global variables or should we not the
thing was partner wanted to have them
prefixed and that meant that I as a code
reviewer I had to go through all of the
global variables and just leave a bunch
of comments hey you missed a g here hey
you missed the G here oh you forgot an
exit oh you forgot another exit that's
when I found out that we can have custom
code cups and we can create our own
warnings and now we have a warning if a
global variable doesn't have a a prefix
and the pipeline will fail if we forgot
that so as a code reviewer I no longer
have to care
about variables or exit
statements now this is these examples
are a bit specific to that one partner
so I also included a couple other
examples that are a bit more applicable
to to all of of
us one of it is a commit statement
commits are powerful and sometimes we
need them but the problem with commits
is that six months later when you come
back to that commit you won't really
remember why is that commit there so we
decided that every commit should have a
comment but that would again mean that I
as a code reviewer I have to find each
commit and say you didn't put a comment
here put a comment here not anymore
there's a warning for
that same goes for this example really
simple procedure create new customer
initialize a record assign a number
assign a name and insert it if I come to
this code six months
later did the developer want to skip the
insert Trigger or did they just forget
to specify the
parameter I don't know probably they
don't know either and that's why we
decided that all internal uh methods
must be invoked with explicit parameters
so inserts modifies deletes all of that
now needs an explicit parameter and we
have a warning so I as a code reviewer
don't have to check
that and I have one more example of of a
linting use case which was super
powerful we added it a couple of months
ago and here actually I want to include
all of you as well um let me ask you
let's say you have a code uh you have a
pool request where somebody added four
fields on the customer table it's just
that what's the problem here does any
and Arthur you cannot answer uh but does
anyone else know uh what what could be
the issue
here
no let me yeah I I hear it some of you
already know but let me show you what
happens when you deploy such an
extension
let me just connect
again oh fun fact this morning my CDX
environments the environments where I
created these examples they all got
deleted so we almost didn't have a a
demo here but you know I got another one
running okay so we merged a
simple extension to the customer table
QA said it's fine but then the customers
they went to
contacts and they find a contact that
they like I'm going to find this contact
and they just want to create a customer
out of this
contact okay I select a template and
there's an
error that the following Fields must
have the same type what's the issue
here yes our our pool request only had
four additional fields to the customer
table what we don't know as code
reviewers that a month ago somebody
added a bunch of fields to the contact
table on different IDs and when you try
to create a customer out of a
contact transfer Fields is
executed which means all of the fields
from the contact table on the same IDs
are going to be jammed into the customer
if if there's a conflict on any of the
Fields you're going to have a runtime
error right so that means that as a code
reviewer every time I'm looking at a
customer table customer extension table
I have to keep in mind oh we should
actually check the contact table as well
now let me ask you do you know any any
other tables that are paired the same
way customer and contact
are yeah there's there's for example
vendor and contact there's sales header
sales header archive sales line sales
line archive so let let's talk numbers
how many tables in the basab do you
think are paired the way customer and
contact are paired together any any
numbers what would be
a
100 no well the last time we went
through
it2 there's 192 tables that are in the
basap coupled with transfer Fields now
just imagine if I as a code reviewer I
have to keep the context of 192 table
pairs in my head whenever I'm looking at
a table
extension impossible I have no clue how
we have done this so far but what we
created internally is a rule that is
going to go through all of these 192
table Pairs and if it finds that there's
a field on the customer table and a
field on the contact table that would
Clash we throw a warning that the ID
name and the type need to be exactly the
same otherwise we just end up with a
runtime error and now I would like to
show you where all of you can get the
benefits of that so I'm going to switch
to
a GitHub project over
here um we know the the appsource cops
from Microsoft uh code cops from
Microsoft oft appsource pendant
extension cop all of the cops this is
the let's call it the fifth cop that all
of you can really easily enable it's
business central. linter cop owned by by
Stefan
and Arthur was a heavy contributor to to
to this project when I found this
project about let's say what two two
years ago it had something like eight
eight rules one of them we we already
saw today commit needs a comment to
justify its
existence once Arthur got on board this
became big we now have close to 60
different warnings that can that can be
triggered and the one that I was just
explaining to
you tables coupled with transfer Fields
must have a matching
Fields right you you can read on the the
info page here
how how do you set it up how do you set
it up in Visual Studio code how do you
set up in your pipelines and you don't
have to use all of the 57 rules just
enables the enable the ones that do help
you write more maintainable codes that
will help you be better code reviewers
so really this is a great project but if
you enable lter cop you like all of the
additional rules but you still have your
own coding guidelines in your
organizations that you would like to
let's say
automate then I would invite you to
check out a webinar I did with Luke a
couple of weeks ago on aropa webinars if
you don't know aropa webinars Awesome
YouTube channel because you can find all
sorts of topics here from AI to
interfaces to I don't know all sorts of
different topics but the one I was
aiming at is this one automating code
quality a guide to using custom code
analysis this is where I went a bit
deeper into how do you create your own
warnings and your own
rules so feel free to to check that
out okay so that's what I wanted to to
share about custom linting and
linters in the end once we have our
policies in place no code changes can
reach the the main branch once we have
pipelines in place and linters we don't
have to worry about questions like does
it build do all the tests pass are
translations done is it following coding
guidelines not the question for the code
reviewer let the pipeline answer that
and let we can focus on the actual
changes now let's talk a little bit
about the softer side of the review
process I think you can already tell
from the slides that I want us to keep
pool request small like really I don't
have a problem with reviewing five small
pool requests I have a problem with
reviewing one big pool
request I've never rejected a pool
request because it was too small I have
rejected pool requests because they were
too big and I have another quote here
that's going to try to lead you in the
direction of Let's Make pool requests
small from Swiss he's a us-based blogger
he's not from the BC world but he talks
a lot about the engineering mindset so I
really like reading his things and what
he wrote in a recent post was but when
cod's finished it's too late for deep
feedback any push back breathes
resentment what do you mean you don't
like my beautiful baby right where does
that come from it comes from the fact
that the developer just spent three
weeks
developing and now they're afraid to
open a PO request because there's going
to be a ton of comments there and we're
going to have to fix it for the next two
weeks how do we fix that by not
developing for 3 weeks by opening a pool
request after two to three
days if you open a pool request after
two to three days I guarantee you that
you won't be you won't get comments that
you'll have to work on for the next two
weeks yeah another thing that SS said
was you know what's worse than a meeting
building the wrong thing for AEK week so
let's try to build the wrong thing for
two to three days at
best personally for me the ideal
workspan is up to three days up to five
it's okay but two weeks I think two
weeks is no longer okay because after
two weeks if you've been developing for
two weeks the pool request is going to
be
big but the second problem is that
estimates no longer work work at the
twoe period because if a developer says
this is going to take two weeks it's
just as likely to take one week as it is
to take three weeks but if a developer
says this is going to take two to three
days well then it's most likely going to
take two to three
days uh I know that well to get to
smaller pool requests we need to have
small work items so if we put more
effort into breaking the user stories
down breaking the use cases down it's
going to be much easier for us to
actually have smaller pool
requests but I also understand that just
because I want us to have small small
work items doesn't mean that on Monday
morning you can work with smaller work
items I was working for that same
partner I mentioned earlier the one that
wanted to have exit statements
capitalized and they simply dropped a 70
page PDF on my table saying go develop
this but instead of me developing in my
little cave for the next month I agreed
with the developers and the reviewers
that I'm going to create intermediate
pool requests I didn't make a pool
request to the main branch I made a pool
request to the the feature Branch every
two to three days and that allowed the
reviewers to actually review code they
were able to follow along how the
feature is evolving and I was able to
get feedback that I can work on on I
didn't wait till the pool request grew
to a 100 files and then trying to change
something is kind of
difficult now I know
that intermediate pool requests you
might go for it you might not but I
would say the very least thing we should
do with code review is plan time for it
because let's say we do we do Sprints
right at the beginning of the Sprint
plan
we're really good at estimating the time
needed for
development and we're really good at
estimating time for testing but code
review nah you you'll find the 10 15
minutes and and you're going to review
it yeah you'll you'll figure it out but
now imagine this situation it's Thursday
afternoon I'm a bit behind on my tasks
but I think I can I'll figure it out I
can make it even though tomorrow is the
end of the Sprint and now somebody opens
a pool request with 70 files
changed how much of a good job am I
going to do there as a
reviewer I'll let this graph answer for
me the bigger the pool request the
quicker I'm just going to scroll through
it right I won't I won't actually be
paying attention to the details and
that's how we're going to end up with
with bugs in the the production
I have another slide that that
emphasizes that we should keep request
small ask an engineer to review 15 lines
of code they'll find plenty of issues as
them to review thousand
lines looks good to
me so yeah if there's one thing I want
you to take away from from this session
today is let's keep pool requests
small okay now we're going to talk about
the roles and the reviewers let me ask
you this who has never reviewed code
before no one one person everyone else
has been a reviewer before so let's take
a look at how can we be better when we
have to review
code and the first point for me is that
as code reviewers we need to be timely
because when does code review come it
comes at the end of the phase right
somebody has been developing for 3 weeks
and now they're waiting on our input
before they can merge the code close the
ticket and move on so they're
essentially blocked by by Me by by my
input and I think we should actually
prioritize code review higher than my
own development
tasks the way I do this is that I have
like two mental blockers one in the
morning after I had my coffee and one in
the afternoon after lunch where I go go
through open pool requests and what this
gives to the developers is
predictability they know exactly when
they can expect the next batch of input
right so if I left a bunch of comments
they resolve them and they know oh okay
in the afternoon it's either going to be
more comments or a success and we can
merge things through so as reviewers
let's be timely when it comes to code
review and for the other two points
reviewing the changes not just the
syntax and sticking to scope I have a
couple of examples ready for
that so let's jump back into Asia
devops and let's go to one of the pull
requests we're going to start with the
ad location Loop to sync inventory now I
mentioned this during policies if we
require work items to be attached well
then they have to be attached and that
means how can I focus on the not just
the syntax by understanding what the
developer tried to solve what the
problem was and if I have a work item
attached I can simply navigate to it now
it doesn't really matter what it says up
here but what matters is that I as a
code reviewer I can understand what the
problem was and once I understand the
ticket that's when I can go back to to
the pool request and start reviewing the
code and now I'll be able to review the
change not just the syntax
a quick side note if you're using Asia
devops there's an extension that you
really really really should install to
make life of code reviewers easier it
has a really long name Al language
syntax highlights for Microsoft Dynamics
365 business Essential by Microsoft it's
a free extension and I'll show you in a
moment what what it brings uh but it's
really useful for for code review
because if you don't have this extension
installed all of your code is going to
look like this boring plain
white but if you do install the
extension once you navigate to
individual files you can see that the
reserved keywords are now blue and
hardcoded strings are now this orangey
brownie color hardcoded integers are are
green and the rest is still white but
even this helps so much with readability
of code it makes it much easier for us
to review code like
that okay so we already talked about the
first point where we want to review the
change not just the syntax now the
second one I was making is let's stick
to scope and what I mean by that is we
saw in the work item that they were
working on something related to sync
inventory we can also see that from the
name of the pool request over here here
now does that mean I cannot leave a
comment saying hey there's a typo in
order
sync I think we can typos are fine
because they're they're a quick fix but
what we shouldn't do as code reviewers
is go completely outside to something
like company sync functionality and
leave a comment saying yeah could you
while while you're added could you
refactor this so that it only syncs for
European
companies yeah that's that's a bit out
of scope that's a completely separate
work item and now it's easy to point
that out here because the pool request
is small and there's only one work item
attached to it but when we have those
pool requests where there's three user
stories attached to it and maybe two bug
tickets as well that's when the lines
get blurry and we don't really know
what's in scope and what isn't and
that's how we end up with those pool
requests that just seem to grow and grow
and grow and grow and we never seem to
merge
in so as code
reviewers let's be timely let's focus on
the changes not just the names of
procedures and variables and let's stick
to the
scope okay now this next slide for the
reviewers is about coding guidelines
I've recently learned that not a lot of
organizations have their own coding
guidelines documented so let me ask you
who has their coding guidelines
documented oh a bit more than I was
expecting still not all of you so I'll
try to use this slide to to motivate the
rest of you why it's a good idea to have
the guidelines
documented even we we didn't have them
two years or so ago but then we had a
couple of scenarios happen that made
them quite invaluable to
us the first one was different reviewers
different rules let me let me tell you
what happened and it was oh frustrating
I open a pool
request and a reviewer joins in and they
go through my code and they see oh um I
see you're using validate in a lot of
your procedure names I don't think you
should use validate because you know
validate has a lot of meaning in
bcn we validate Fields I think you
should be using verify
instead yeah okay Fair Point why not I
change the code I make the update we
merge the code in everything's fine a
week later I open a new pool request a
different code reviewer joins in they go
through my code and they go H I see
you're using verify in a lot of your
procedure names I think you should be
using validate because you know validate
has a lot of meaning in BC and Al we
validate all of the
fields that's so frustrating when when
you have two reviewers requesting to
completely
opposing things and that's where coding
guidelines really shine because if you
have your guidelines documented it
doesn't matter verify or validate what
we agree on once we put it in this
document well the guidelines become the
ultimate Arbiter in this agreements it
doesn't matter what the reviewer thinks
it doesn't matter what the developer
thinks if it's in the guidelines that's
how we write code at the end of the
day and I have another example Le that
happened to me a couple of months ago
let me jump into a different pull
request for
that let me find
one pull
requests this
one let me just jump into the changes
that I want to show
you okay so the developer had to do a
small thing just add a gatekeeper to the
inq job entry function nothing big but
when I was going over this I saw that in
Q job entry actually has quite a lot of
parameters so I left a comment hey I
think we should break those parameters
down because horizontal scrolling is not
not really something we we would like to
do and I was already getting push back
from the developer why why would I break
procedures Microsoft never breaks their
procedures why why should we well
Microsoft doesn't have all the the best
guidelines in in the way they write code
but still over time I was able to
convince him that horizontal scrolling
is not good and they said yeah okay I'll
I'll fix it this is how they fixed
it they took half of the parameters and
moved it to to a new line and to me
that's even more confusing actually
because now I don't know what is the
fourth parameter over here I have to
count everything and I was like yeah
well I want you to change it again but
instead of us going back and forward on
how we should break parameters if we
should break
parameters instead we added a section to
our guidelines you don't have to read
this block of text essentially what it's
saying is if a line goes over 120
characters we're going to break
procedures
if we break uh definitions we break them
like this if we break invocations we
break them like that and now again
doesn't matter what I think as a
reviewer doesn't matter what the
developer
thinks this is how we break
procedures now
hopefully come
on my clicker
stopped I have to click in the
presentation I think yeah so hopefully
you got a bit inspired that you would
like to have your own guidelines
documented as well and the question is
where do you
start well I would say check out ALG
guidelines. deev now I'm going to show
you how ALG guidelines. Dev look like
but this is a community initiative where
people from the community have
contributed their own guidelines and
best practices up there and you can go
to this website you can see those
guidelines you don't have to obey all of
them you can just choose whatever works
for you and let that be the Baseline for
your guidelines and then document
whatever else
you're uh however you write code in your
organizations and add it and let that be
your document and if you document some
of the guidelines that you have that you
think hey I think more of the community
could benefit from a guideline like that
I would really invite you to contribute
back to this
initiative now let's check it out just
how it
looks when you click the link this is
where you come to guidelines and
patterns for development for Microsoft
Dynamics 365 business
cenal so I don't want to go to through
too many details here but once you go to
the docs this is where you can find and
read about design patterns right what is
a facade or what is a generic method I
know Waldo loves the generic method I
didn't even know what a generic method
is but here I could go and read about
when do you use a generic method why do
you use a generic method what kind of
problems does it solve so this is the
the design patterns
section you also have best practices
over here
these are like I said we don't need all
of them just choose the ones that you
are already using for example there's
one that I actually disagree with
there's the unnecessary else else should
not be used when the last action in the
then part is an exit break skip quit
error this is supposed to be bad code
and this is supposed to be good code my
personal opinion is that the bad code is
actually clearer because it indicates
that there's only two possible outcomes
here while the good
code but again you know maybe you think
differently choose the the best
practices that you would like to use and
let that be the basis of your of your
coding
guidelines the last page that I want to
show you from the guidelines is the
contribution page like I said if you do
go and document things in your own
organizations that you think are
applicable to a wider
audience really go here open a pool
request everybody's going to love it and
I think it's only good for the whole
Community if we write the same code more
or
less uh I have two more examples about
guidelines first one a couple of months
ago I was tasked with reviewing a code
base of a product that we adopted and I
was supposed to say how much Tech depb
do we have
this was the kind of code that I found
there now the first problem is I don't
speak Dutch I have no clue what's
happening
here and I hope that at this point we're
all writing code in English now but what
I was trying to Showcase here is we all
have coding guidelines we don't just
write whatever we want to write because
otherwise we end up with procedures like
these where we have a prefix on the
parameter f which is what for parameter
I don't know so yeah we all have
guidelines so there is something to
document and another another thing that
we will have to do with with guidelines
in a couple of months is discuss what
are we going to do with this we all saw
this during the the keynote uh when
Vincent showed it but well I love the
idea of this not only because you can
pass now the instance of a code unit but
also you can have your Global variables
prefixed with this do Global variable or
this do local
procedure I like the idea of prefixing
global variable I don't I'm not sure I
like the idea of using it on local
procedures so internally we're just
going to agree on how do we use this
we're going to add it to the to the
guidelines and that's how we're all
going to use this it's not going to be I
use it this way you use it that way we
agree on how we're going to use this new
functionality okay and
now we have this last part of reviewing
the reviewer which is clear
communication is
key we talked about before of one type
of fear like why do I not want to open a
pool request well because I'm afraid
that there's going to be a bunch of
comments that I will have to solve now
for the next two weeks yeah that that's
one reason another reason why I wouldn't
want to open a pool request is because
there's that one developer who's going
to join in and he's just going to
complain oh I would do this differently
and this is poorly named and this is
poorly
named yeah nobody likes to open a pool
request and then get a lot of complaints
on it so I think that clear
communication really is key and the way
I approach this is that I look for five
types of code and I change the way I
communicate based on these five types of
code I look for good code code that
solves the problem code that's readable
code that's maintainable good code
doesn't really need a a
comment I look for could be better code
code that still solves the problem but
could be better maybe better structured
maybe better named this code usually
gets a
comment there's bad code bad code never
gets merged in an example of bad code is
let's say uh something that's an obvious
performance hit or something that could
potentially lead to data loss that's the
last thing we want for our applications
to cause data loss code is temporary
data is
forever there's also me code that's the
kind of code where I would do things
differently but am I going to block a
pool request because of that I won't and
with me code is where I use the power of
nit and I'll talk about that a little
bit later when I show you the examples
of these types of of code now the last
one that I look for is amazing code now
amazing code of course comes from the
developers who develop the algorithms
that
I could never think of yeah that is
amazing code but amazing code can also
come from a junior that just takes the
next step that delivers more than I sort
of expect of them for example let's say
I task a junior with creating a field in
one table creating a field in another
table and then they need to write a line
of code in a code unit somewhere to
transfer the field from one table to the
other that would be good
code but if the junior also sees that
this procedure where they had to add a
line of code is actually getting kind of
big so they split it down to different
procedures they documented it well
that's amazing code to me because maybe
I would expect this out of a senior
developer I did not expect it from a
junior and this is actually the area
where I want to improve myself more that
I don't only tear the pool requests
apart but that I also try to look for
the good parts you know this is good
thank you I like the the contribution
that you made and now I have a couple of
examples of just how these types of code
look
like so let's jump into the next pull
request okay let's
see now we're going into the add address
three let me just fill filter down the
changes there we
go I'll make it full screen close the
comment okay so this this was the
example I was talking about somebody
needs to add a field to the customer
table and they need to add a field to
the custom customer address table and
then they need to add a line of code in
a code unit somewhere that transfers the
address three from one table to to the
other and this would be good code solves
the problem no problem here so let's
move
on the next
request that developer had was to add
some validation loog logic so if address
3 is the same as address 2 then clear
address 3 and clear it in the connected
table as well because we don't want to
have duplicate data in in two Fields now
this is actually could be better code
because it does solve the problem but
the name process address is a bit too
wague we know exactly what this
procedure does so could be better code
gets a comment and this is where I try
to explain yeah hey what you did was
okay but I think you could rename it to
a clearer name not just because of you
when you get back to this code but for
anyone trying to finding this Pro
process address function and not really
understanding what does it process so
this would be an example of could be
better
code now the next example I have is of
amazing
code right remember from before this was
the line that they wrote so moving
address three from one table to the
other table however the developer also
noticed that this create customer front
template procedure is kind of big it's
doing a lot of things because it creates
a customer from template but then it
also assigns a bunch of fields to the
customer record and down here it it's
also modifying the customer address
table so they realized this could be
better if I extract this to a separate
code unit to a separate procedure and
like I said to me that's amazing code
it's a bit difficult to be enthusiastic
about this example that I fabricated
just just for today but I think you get
the point right we don't want to only
look for the bad parts of pool requests
we should also sometimes look for what's
good what was done
well finally I have an example of me
code for that I'm going to switch into
the file and we have to switch to the
modified content View
okay this is how the code looks after
everything was
extracted good I like it it's nice but
in reality I would want to have a line
break under this modify so it's a bit
clearer what kind of changes are done on
the custom record and what are other
changes right but will I ever block a
pool request for something like that I
won't but these are the types of
comments that I prefix with nit
this is the power of nit that I was
talking about nit stands for nit peing
and what it brings is it gives all of
the power to the developer the developer
can decide do I care about this comment
do I want to add a line or not and they
can decide yes I will add a line or no I
won't and they just mark it as won't fix
it right and not only does it give all
the power to to the developer it also
gives me as a reviewer a lot of power
because a lot of the times I have been
in a situation where I already leave
like 20 comments and then I think to
myself do I really want to comment on
something as meaningless as this I don't
know well with neat I can because it's
up to them they will decide do they want
to do something with this or do they not
and at the same time this nit is also
really useful for juniors because with
Juniors I would like to tell them more
often that hey what you did was okay
here's how I would have done it not
because anything's wrong with your your
approach just that you're exposed to hey
there's an alternative way and that's
when I prefix it with nit and they
decide do they care about the comment or
do they
not so really use the power of nit it's
useful both for the reviewers and the
reviewees so clear communication
I think is the the most important part
because if we clearly communicate our
intentions we build trust with the
developers the developers become less
defensive and they will be more willing
to receive
feedback okay now we come to to the last
section which is reviewing the reviewy
so when when my code is being reviewed
and again here I could ask you who has
never had their code
reviewed yeah we all had our own code
reviewed so what can we do to be better
in this
part and the first point is let's focus
on design before code because we we
talked about a situation where I'm
developing for three weeks and I get a
bunch of comments on my pool request I
can avoid that if I bring all of the the
reviewers and the Developers with me to
the design phase and if we agree at the
beginning how are we going to implement
this feature how are we going to solve
that problem well then there's not going
to be any surprises 3 weeks later once
we do open up a pool
request but I know that's kind of
difficult because thinking before coding
nah coding before thinking that's what
we like we like to just jump into the to
the feature and I'm guilty of of that
myself right I I like to solve the
problem as I kind of work through it but
there's just so many benefits if we do
that ahead of time that we
should the next two points are let's
review ourselves first and let's be
proactive in clarifying unclear parts
and for that I again have a couple of
examples ready so let's jump into our
pool request
uh this time which one I'm going for
this
one when you open a new pool request you
can first open it in draft mode and in
draft mode there's no
reviewers and there's no
pipelines it's just you and your changes
and you can use this opportunity to go
through the code from the same same way
as the reviewers will have to go through
it right you you view it from a
different perspective because we're used
to looking at our code in vs code
because that's where we developed it but
this is how the reviewers are going to
see it so it's beneficial if we first go
through our pool
request and we see oh wait a minute I
actually didn't want to comment this out
this was just for testing purposes right
I can catch my own mistakes before
somebody else has to because I just get
a view from a different perspective by
by reviewing it through Asia
devops now the second point was let's
clarify unclear Parts ahead of time with
this I'm primarily targeting places
where we already know that maybe
somebody's going to have questions in
this part of the pool request well why
not leave an answer ahead of time for
example our amazing code over here if I
see this kind of pull request from a
junior where a bunch of lines are
deleted red flags are going to go up
what's happening over here right but if
the developer leaves a comment ahead of
time that hey don't worry I just move
this to to a separate procedure to make
it clearer to make it more readable then
the flags go down again and I'll be fine
I'll understand that yeah we didn't just
delete a bunch of code because tests
were failing we actually wanted to to
refactor and improve
code so as review
is let's review ourselves first and
let's be proactive in clarifying unclear
parts and then there's one last point be
open to
feedback When I Was preparing for this
session I tried to pay attention
internally on our pool requests if I'll
ever get an example that I can use for
be open to
feedback and I did couple of months ago
there were these two comments I need to
push this pool request fast I don't have
time to argue and I get where the
developer was coming from they had a
deadline for tomorrow they needed to to
merge things in but the only response
that this kind of comment can get is
okay let's hop on a call let's go
through it together let me help you
merge this faster but urgency and
deadlines cannot be an excuse for us to
merge bad code in because we're just
going to end up in a situation where we
have glitter bump worthy code in our
production so the kind of code review
requests that I don't
like are these
ones that's review the code not only
approve and rubber
stamp okay now we're coming to to the
age of AI to to the last slides about
GitHub
co-pilot Has anyone used GitHub co-pilot
and let me be clear I'm not talking
about the wonders of GitHub co-pilot in
Visual Studio code that one I love
GitHub co-pilot in GitHub so the
Enterprise
one no one I know why I'll I'll show you
why we're not using it uh but I was
hoping that somebody's going to share
their experience because I haven't used
it either but that Enterprise co-pilot
what it's supposed to bring for the code
review is
this it's going to help us write pull
request
descriptions we didn't even talk about
pool request descriptions today because
not that they're not important they have
their place but they're just not that
important and the reason why I cannot
really endorse the Enterprise version of
co-pilot is the
price I love GitHub copilot in Visual
Studio code I can argue for every let's
say experienced developer that they
should have a license to the GitHub
co-pilot in Visual Studio code but the
Enterprise one it costs twice as much
and not only does it cost twice as much
you need to have the GitHub Enterprise
license so instead of me arguing for
this developer needs to have a license
for $25 I would need to argue for $60 so
our pool request descriptions can be
generated automatically now the
Enterprise co-pilot has additional
features but I just wanted to point out
that for for code
review we didn't get much yet but I did
when again when I Was preparing for this
session I was on a lookout if there are
other AI tools and what do they bring in
the sphere of code review and how are
they going to
help again I'm not trying to endorse any
products because I've only kind of
played around with them but this is just
to show
you what maybe one day co-pilot will do
for
us uh I
have something called code rabbit uh
before I show you what's happening here
this is essentially a pool request that
adds this code unit to to the code base
just to briefly explain what's happening
here a couple of months ago I was trying
to build a tool kit that would help us
um evaluate and test AI features so it's
a toolkit that
sends a lot of requests to open AI in
parallel so I can send 100 requests to
open AI get 100 responses and then see
are those responses okay or not right
and what this specific code unit here
was doing when all of those 100 test
cases went
through it calculated
the total number of of test runs right
all of the 100 runs that I've executed
and then it's going to calculate the
successful ones and it's going to
calculate the pass rate the rest we
don't really have to care too much about
but that's that's essentially the
calculation that's happening here and
when I created this pool request this
code rabbit tool again of course it
creates the the description for for us
okay fine but it also actually starts
performing the code review and you get a
comment it understands that well you're
doing some calculations here you're
trying to divide with total runs that
can be zero so consider handling the
case where total runs is
zero not really groundbreaking stuff but
what I'm trying to highlight here is
right now
co-pilots in GitHub they don't do much
for code review but I think in a few
months in a few iterations we might we
might actually get co-pilots that will
help us perform the code review because
they will catch catch things like this
for
us
okay
so now we come to the last part which is
a couple of key takeways that I want you
to remember as you exit this room and
the first one is just do the code
review policies don't matter pipelines
don't matter co-pilots don't matter if
we don't do the code review so let's
let's start there let's just do the code
review the next one is let's focus on
design before code right we we talked
about it let's take our development team
let's bring it with us to the beginning
let's agree how we're going to solve the
feature how we're going to to build it
out because otherwise we're going in the
wrong
direction right so let's let's focus on
design before code so that we don't go
in the in the wrong
direction this third point I think I was
making it quite a lot today let's keep
pool requests
small the next one is about adopting
process improvements to make reviews
faster once we're doing code
review that's when we should think about
pipelines and that's when we should
think about linters because there's all
sorts of questions that I as a code
reviewer don't have to think about I
shouldn't think about those questions
let that be the the work of the
automation
tools and then finally let's clearly
communicate our intentions because if we
clearly communicate what we want from
the developer we build the trust we
lower the defense expensiveness and the
developer is going to be more willing to
receive the
feedback so those are the five key
takeaways for for today and I want to
leave you with one final quote that a
friend of mine from UK uh said after I
did this session in in Birmingham at the
beginning of the
year what he said was we need to
understand that pool requests aren't an
obstacle that we need to overcome but a
tool to ctively have better
code and with that we come to the last
part which is this was all from my side
and now if you have any questions I have
T-shirts and I have uh the catch
boxes
so O
Okay so uh thank for the presentation uh
when we see the the uh things we do with
poll request I think it's mostly in the
context of distributed teams and
asynchronous uh communication or
something like that um so I was
wondering what your thoughts are about
when we have a setting where all the
developers are in the same room they can
talk to each other and something like
that um if we could skip pull request
and do pair programming instead because
they can talk to each other about the
issues in the code because they are
looking at the same screen and make the
fixes right away yeah uh so with pair
programming uh um the thing is I've
never done pair programming so I don't I
don't really have experience with it but
I do agree that if two people are
building the codes together it's already
a code review at the same time so I
could oh here's the T-shirt
uh yeah I mean I would agree with the
idea that code review is not as
important if we're already doing code
review while we're building everything
out well sorry there was there was a
question uh behind you as well um yeah
so I I have a question about the build
validation does it make sense also to
run all of the automated tests uh every
P request and I don't know you update P
request uh other are merging to master
so every time run uh automated test and
um what if they run like I don't know an
hour
then that's the problem you need to
solve I know we had this situation where
our tests were running for four hours
and then it makes I won't say it makes
no sense but it's really difficult to
argue run all of the tests on each pool
request but we fixed the tests and once
we got them to one hour that was
acceptable enough for us uh that we now
run tests on every pool request on every
change because no pool request should be
able to break something we want to catch
it immediately right so yeah run tests
uh on every pool request thanks um I'll
here's the t-shirt and you get the
mic okay so I have mostly a couple
comments yeah uh the first one I didn't
raise my hand before because I am
actually uh right now implementing them
I am using status checks at GitHub um
because with GitHub actions they
actually end up being status checks uh
my main developers asked me to check
that some branches don't end up being
merged uh to the main for example so po
request for from certain branches uh get
rejected automatically and that's a
status check okay in that case thank you
and the other comment was about the
extension you showed that highlights the
Syntax for Al yeah um do you know if it
can change the colors on that because I
noticed the comments are still green but
obviously if you remove the lines you
have have a red background I have a lot
of color blind develop developers so
that's a really a big issue I don't know
and I think we need to to ask Microsoft
uh can we do that I I never I never
played with it yeah but thank
you
what thank you um my question is um we
just recently started with pull request
reviews yeah we are very late on that
that and um I'm
afraid uh the developers will not be too
happy to have the poll request declined
at first and um do you have any
suggestions how to improve acceptability
on that one thing I would say is uh we
never really reject a pool request in
our internal teams all of us right if a
product owner decided that a feature
needs to go in then a feature will need
to go in so we don't really reject the
pool request we simply wait for the
input to be to be kind of resolved right
but I think what what you're asking is
not about rejecting a pool request but
how to tell people hey you might have to
do more more work right
um it is going to be a people issue in
the end so the best you can do is just
have some people who are eager to do
this and make it make it a slow change I
know it's it's always difficult to to
introduce a new process so I think this
is more of a change management question
and I don't really have an answer for
that for us it was always easy to
convince one additional person compared
to trying to convince a full team of
people of now you need need to do this
this way right it's much easier if the
team already agrees we want to do it in
a in a better way so yeah I I don't
really have any good good suggestions
for thank you anyway yeah start with a
few projects and see how it goes some
proactive person your
team and
then evangelize the others that that's
some for example not with pool requests
but uh we did that with automated
testing in a non-bc related Department
uh they were pushing back we don't want
to do automated testing how did we get
them to do automated testing we got an
experienced person in who already did
tests and knew the value of tests
and slowly they convinced one additional
person and one additional person and in
six months the whole team was doing
automated tests because slowly they
understood where the value is and that
there's not that much complexity to it
so I would assume that the same could
work with with pool
requests thank
you
yeah yes thank you tin great
presentation uh uh in practice uh how
much time uh uh we spend to to to this
section uh to perform the code review
yes uh when it's big pool requests it's
a lot of time uh on that German project
I was
spending two hours easily on on a pool
request and that was just one iteration
it had to go through many iterations
because there was so much code when you
come with uh with smaller pool requests
when it actually is two to three days
worth of work 15 minutes is completely
fine for me uh because there's not it's
not so many changes that I need to keep
in in my head so with smaller pool
requests 10 15 with big ones we're
talking
hours okay okay thank
you anyone else
yeah so um what what about uh if you
have like typo mistakes and so on you
comment on that poor request or
uh you fix it and and let the developer
know there's two things if if it's a
really simple typo I think maybe I can
show that uh there's the suggestions
directly in Asia
devops right you can you
can uh try to leave a comment and
there's uh I won't find it
now think I need to go here
maybe
suggest oh insert a suggestion here I
could already fix a typo and immediately
accept it and commit it so that the
developer doesn't really have to go
through
um U updating it but normally I I would
comment on a um on a typo as well I
would do do it with nit and they can
then see yeah I'm going to update any
something else anyway right it's up to
them it's their power of decision all
right thank
you here and then there's behind you two
more okay so you said that we have to
keep the PO simple small to get the easy
review so what's the algorithm to split
bit functionality that makes work from
couple weeks or something like that and
have to manage I know that we can
prepare
uh how to indirect feature Branch we can
make the pro request but sometimes
the uh you can't split because now we
we we had those where a user story is
either just too big or we don't want to
invest time into splitting it up yeah um
we did intermediate pull request where's
the limit it was up to the developer the
developer decided okay I think these are
the changes that a reviewer can handle
you know that that can be two days it
can be one week if it was it if it was
wasn't that many changes and that was a
pull request so there there's no hard
limit on how we break a huge feature
down thises to the planning call yeah
it's more just when the developer feels
that that's enough uh let's make a pool
request but you need to have proactive
Developers for that okay thank
you H so um how is your um whole process
on the uh developer um makes the P
request um in draft mode then looks over
it yeah and then um publish the PO
request yes um then you don't uh reject
it so you uh only make comments no no no
um okay so the word reject you uh don't
mean rejec yeah yeah okay so you you
reject it and when um the process of uh
overdevelopment should be three days and
perhaps two commits then it stays in
published mode or is it um the developer
sets it then in draft mode again back no
no no so once draft mode is just that
small period for the developer to to to
go through it and then it's published
once it's published it's published and
what I meant with the the rejects right
we have all of these different statuses
wait for author and reject for our
internal teams are exactly the same
because we're never going to reject
functionality because that's the
decision of the product owner not not me
as a code reviewer but then you have a
published request um that um is um there
for maybe one week and the developers
not working on it no so the thing is
with small pool requests and when I
review code twice per day the pool
request is open for one day and then
it's when the developer has time for it
maybe it's uh working after this um for
another customer so um this PR request
doesn't care him about
yeah so so this is in the um it's yeah
uh we are coming more from the product
oriented development and there it it I
see I see what you're aiming at if you
have different projects then here I do
the work and I don't have time to return
to this pool request until a week
later yeah that's that's more of an more
of an issue so I think um we have the um
solution that uh the developer uh
himself approves the PO request but the
number of Po request approvers is um
added by one so um there are at least
two U peras approvers yeah and when the
weg's over and the developer says okay
I'm fine with it then he he again
approve it so that uh when you look at
it you see ah it's it's approved so he's
fine with it
and okay
no um yeah we don't we don't do that for
me it's more like when the developer
does their changes they push them up my
votes get reset and that's my signal
that I need to now uh go through it
again so until they're done with their
changes they just don't push things up
and that means the pool request is going
to stay in the wait for author State
okay
yeah thank you thank you for the um
session it was very interesting I wonder
how do you decide who exactly does this
specific pool request As I understood
you have a team of people but who will
Who will do it yeah if nobody have time
at this at this
moment um we usually have development
like on a project we have a leading
developer that's always kind of the main
go-to person it's their main
responsibility now when when I was
talking about knowledge transfer and
that I would like to include more Junior
people I don't really have a a way for
that just yet um but I would I would
still have somebody who has
responsibility for a pool request and
everyone else is being rotated you know
you
um or they can even all be tagged I I'm
not sure I don't have a clear way of how
to rotate people who are who should be
rotated I don't know how to how to put
it in our team we have a week change who
is uh who approves the requests uh when
nobody has time and it's seniority is
more or
less the same so works for us that's
good but uh what we were struggling with
is what if you don't have enough
experienced people on a project to
rotate and but yeah no that's that's a
good good
point you mentioned that stick to scope
is very important uh I'm doing C very
often and yeah we have some very
motivated developers that yeah they add
new procedures and see a typo one
procedure above or below and then they
yeah I fix this while I see it and my
problem sometimes after they fix a typo
in a not related code I see an error or
something else
and yeah normally I at least at a common
then we need to decide but how how would
you do deal with this situation that
they you could also just say that you're
stricter with sticking to scope and um
open a separate pool request right uh to
for for all of those smaller things
which
are causing to to bigger issues because
like I said typos to me are okay but I
can also see that a typo can be a rename
which can break other things in in other
parts so it's yeah okay it's a it's a
slippery slope maybe I should go back to
just say no stick to scope don't go
outside of scope and out of scope should
just be a separate a separate fool
request
yeah anyone
else uh there's one and yeah we have two
minutes
left oh I didn't even see you there yeah
so uh if you have have to think before
you develop you have to think before you
uh do the code review because if you
would not reink the solution uh you
could not judge judge in correct way I
mean should you think about the solution
before the code review my take is yes I
know that's not always possible but
whenever you can have the context of the
problem you should but especially when
you have multiple projects and you want
you want to pull a pull a reviewer from
a different project they won't
understand this project so it is going
to happen that we don't always have the
the context to review the change and
sometimes we do just review the syntax
but my take is we should always know
what the what the ticket is
about okay last question uh have you
ever tried to um to not uh include
translations D directly in featur
branches and handle them in different
process and you found it better to
pipeline
validate uh so our Pro like our or
original approach was just merge
features in and then before the release
we're going to do translations but that
meant uh people didn't have any context
of what this word is supposed to be
because you just get that huge
translation file and now you have to
translate individual words instead of uh
like features with meaning right that's
when we moved to to the pool request
needs to be fully translated because
then when you see a certain action name
you know exactly what this action name
refers to if it has a more more generic
name so that that's why this was the
better solution for
us I'm not sure if that that uh yeah I'm
aiming more towards uh not handling
translations directly in uh Exel F files
but making it more friendly oh okay for
Consultants to do it so we never we
never edit them directly in the file we
had poedit uh the tool that that was
more friendly for actually translating
stuff
um but yeah uh the the second benefit
that we got from fully translating
everything on a pool request basis is we
didn't have any merge conflicts on the
translation files anymore because each
pool request introduced strings which
were also fully translated and they were
never again Modified by by someone else
that would that a different pool request
would Clash with with the
translations yeah um okay that's that's
all the time we we had for today so
thank you
