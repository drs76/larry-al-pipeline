# BC TechDays 2023 - Feature Management for Continuous Delivery

- **Source:** https://www.youtube.com/watch?v=WAuCfS-vYZ8
- **Video ID:** WAuCfS-vYZ8
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 88m16s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

yeah thank you for coming I'm quite
excited that a lot of people are
interested in this topic
um because it's kind of widely used
around in in other Technologies texts in
digital and web development
and
I really want to with this session to
bring this over into AO world as well
so we had two presenters here planned
only one on stage unfortunately second
one didn't gonna make it
so we will see him virtually
so uh as you're in a cinema be ready
that there will be part of the session
where you guys will see it as a film
hello everyone
sorry for not being able to
be there in person to deliver the
session and enjoy and connect with
everyone
I tried my best
next year I will be there for sure
let me introduce myself
lead technical consultant at data
did I said one of the largest PC
Partners in the ancient region
I'm also a Microsoft MVP I got my first
award 2016 while I was back in Sri Lanka
I specialized in air development and
extending and integrating business
Central with use of azure integration
services
I am originally from Sri Lanka but have
lived in Oakland New Zealand for past
seven years with my loving daughter and
wife
I hope you will enjoy our session
it's audio blood thank you
thanks
my name is what I'm working with strong
guy in in Titan New Zealand we are quite
a large partner as strong girls already
mentioned in our practice we had like 45
people in BC world
um
I'm originally from Ukraine we actually
had two speakers in this session from
Ukraine and we kind of competing he's in
another room talking
so be free to reach me out on GitHub or
Twitter
so the topic for today would be kind of
trying to introduce BC Community into
what the feature flag approaches
you might heard about this as with
another names like feature toggles
features features release switches
release struggles so and actually
sometimes they're referring as a strong
based development
as for this kind of approach as well
what it is in a nutshell it's just a way
for you to enable or disable your
features without modifying the source
code or without redeployment and the key
word here is kind of this redeployment
phase we usually are talking about
deployment and release as
kind of synonyms sometimes like let's
just release to this environment just
deploy to this environment is kind of
the same thing for us
but it is actually two completely
different processes
where
when we talk about deployment it's
actually packaging your code in a in a
in-app file and moving this around to
some other environment in or into the
artifact storage
where where we're talking about release
is where you're actually taking your
feature and presenting this feature to
your users
I'm kind of like this technology
thinking that deployment is your Amazon
that the sky deliver guide dropped in
the back to your door where the release
is your Christmas dinner where you
unpacking this kind of Christmas
presents and show to your family
so what the feature flag approach allows
you to do is actually decouple this to
process and control them in separation
uh
we had a few use cases where we can use
this approach and one of my favorite one
is the continuous integration process
continuous integration is actually hard
to do and
you're always trying to balance between
some of your key goals when you're doing
this
so you're kind of prioritizing do I want
to get my feature as fast as possible
but I'm kind of doing it's my lead time
of my future delivery should be fast
enough or should I have availability
defined correctly so then if anything
crashing I can just take my Branch mind
branch and ship it to my customer
anytime
or I wanted to make sure that my quality
is defined correctly so my test
resolution is valid so there are no
features that overlapping or crashing my
test environments
and in common pipelines you're kind of
balancing trying to find what the right
approach with the right balance for you
and so with this in mind let's look into
typical pipeline that kind of
trying to implement this balance
so we start coding with our two new
features
we have two developers working on
feature a feature B it's kind of two
days for each features to be delivered
to be coded sorry
we are doing development and separation
in two separate feature branches
feature a completed first we kind of can
integrate it into our main branch and so
good and it can already go into our
testing phase
because we prioritize the test
oscillation
in as an hour definition file pipeline
this is where feature B is blocked right
now we cannot integrate it to the main
branch because potentially
we wanted to make sure that our test
environment is clear for anything else
so this is where feature B should be
blocked for whole time when feature a is
going through the testing process
it might be bugley we can decide to
say okay
we can roll it back but
team can just sit and said no we wanted
to just have a quick fix to it so let's
just work for a quick fix and integrate
it quickly where the feature B is still
blocked
we get our fix integrated finally it's
arrived in our test environment
we did our testing
and we move it to uat so this is we
finally able to unlock the feature B
and integrate it into our main branch
and then move it to testing process so
you've seen that the feature B was kind
of blocked for more time than it was
originally developed
then
feature a is quite a bugly and our users
didn't accept it they said okay we sort
of mean a little bit different from what
your Consultants understand
it happened
so please rework it and make it uh
completely different
so this is where we actually need to
roll back
and because it's a change into our
current main branch
we again put in a feature blade feature
Beyond a blocking face
we kind of cannot proceed with testing
we need to make sure that they're all
back successful before we can proceed
with testing for feature B
we'll wait for all back
and now we can get back
finally to start testing for feature B
um
yep
and then we can pass it to to a uat
state
so
this was a typical Pipeline and you can
see that like we feature we kind of
stuck in in a blocking phase from the
same time as it was spent for
development for it
and of course it's delayed our release
for feature B and this is not what we
want to do
so let's try to look how this pipeline
can be transformed with pitchflex
similar way we have two features we're
developing them in parallel on specific
feature branches
you can see this kind of marks
I'm trying to identify
where the feature flagging for them is
enabled or disabled
so for both of them they're enabled and
developers working in the isolated
feature branches they're doing some
testing unit testing so on
when they're happy with it and similar
as a previous time
we can integrate feature a
we integrate in it without feature flag
enabled so it's not affecting our
runtime it's not affecting any other
processes that currently happening
without without main branch
and we can move it to a test routine as
well and this is where
we kind of can enable this flag only for
subset of our users
who is taking care of the functional
testing for our extension for for our
feature
this is where our feature B can be
integrated as well because as it's
coming with in this kind of disabled
state
we are not affecting any other
environment so our test isolation
requirement is still compiled
and this is where we can even pass a
feature b in a testing environment to be
tested in parallel we can just identify
that this feature is enabled for another
subset of functional Consultants who is
taking care of testing our feature
and we're doing our testing
feature a fail we just instantly
disabling it it's not affecting app p2b
which is going right now on a uat
and we can wait for a fix to come in
because technically it's not affecting
any runtime right now
feature B was successful we moved
feature B into a wife already
so there was no booking time we managed
to do it in time as expected as it was
promised
to our customers
we finally get our fix integrated we did
our
regression testing for VGA it's moved to
uat
and so on and so on
ah
so you can see that
in our case with the feature flagging
approach we can stop compromising
between these aspects of our delivery
Pipeline and actually achieve all the
three
aspects of it without any trade-offs
so there are other use cases where you
can use the feature plugin approach
through the previous slides you guys
already seen the controlled draw out
process or Progressive delivery
this is where you're rolling out your
feature
to a bigger subsets of users in a first
phase on a testing environment it was
just our functional consultant our next
phase it can be just the key users
on next phase you can actually deliver
if it's an app store shops you can
probably get it to some some to some
countries
and then maybe roll it out globally
and with the feature flag approach you
can actually have like the same
environment for it so we might have
single sandbox where we are running our
internal testing with functional
consultant as well as the same sandbox
for uat
uh another good use case is a kill
switch
again we've seen it before on previous
slides wherever your feature is broken
wherever there are some complaints about
it you can instantly hear it you don't
need to spend time on rolling back this
change and actually stressing your team
about it and this is where
is probably my second favorite one
another one it's actually something
completely outside of our Erp world
we kind of don't like the idea to do an
experiments with our users but it might
have certain cases in Theta we are
building a monetization solution for our
partner and we always debating about
what should be a sign up for
and this is kind of our key
UI process
and in some point in time we were
we come to the point that we kind of
cannot make it this decision
what if we all wrap
two different flows
into feature flag and actually release
it globally and said that 50 of our
customer will get one flow another 50
will get another one
we plug in some Telemetry to this
process and see which one would actually
work and then as soon as we come up with
an idea which one will work we actually
put it as a globally available for
everyone
another one is use a charter Street
this is where we're talking about more
permanent Flags where we're saying okay
now our features
should be permanently available in a in
an environment
but the good use cases for it uh your
app you wanted to deliver one app into
appsource but you wanted to break this
app into two different pricing plans for
your user you might have like essential
pricing plan within your app and more
advanced one and you wanted to have this
limited set of users available for
essential one and add the business plan
would have all your features enabled
and you can use a feature flagging
approach for this as well
in other use cases launching time on
time this is actually the first use case
which we use in Theta for feature Flags
what we did is
um
we develop as part of our key extension
we had a dynamic announcement feature
idea is that it's a notification behind
a feature flag
and the content of the simplification
sits in another keyboard
so in case if for example we need to
announce something to our users we can
go to key vote
configure what kind of announcement we
wanted to do like what message what
action they need to do they might like
our backend service is down so they need
to wait for two hours while we're fixing
it so we're going to key vote we're
correcting what we wanted to show to the
users and then we go into our feature
flagging system
and actually defining right now we
wanted to show this notification to
everyone in the world who have a it
manager role or admin role so then the
right users are notified about our
downtime
in one other nice use case
is the Early Access
what is this about is
let's say the way how you're doing
changes into your application and
upsource is you kind of come up with a
design you think that this would be a
better user experience for your users
and you package it you pass to observe
for validation and boom your customers
get it they might use the previous UI
they might like you previously more
but in most cases they don't and they
are not ready for your new UI
and this is where Early Access has its
value so idea is that you push in your
changes
with your new UI changes behind a
feature flag
and then you allowing users to decide
when they wanted to enable this feature
so then kind of can schedule their
training with the user schedule any
processes and it's kind of decoupled
from the moment when you are
actually do the deployment
this is actually a use case which
Microsoft using for their feature
management
this was the original driver
you've seen that for SAS environment
Microsoft had this kind of moment of we
are deploying a new release
and they identify that it's actually a
challenge for most of the users in the
world so they decide that any kind of
dramatic UI changes should go through
this early access approach
now over to taranga to kind of talk to
you about this
thank you for the introduction to Future
class
it sounds very promising and should be
able to resolve many of the development
and deployment challenges we face as
partners
saying that does Microsoft use the
feature flag Approach at all
or do they use a different approach
let's try to find it out in next few
minutes
in fact
Microsoft does use feature flag approach
quite heavily with the business and
releases
in the past when there was a new version
of nav or a business Central
users or Partners had no option to
enable these functionalities of reaches
manually
as soon as the tenant or database
upgraded all these new features
functionalities are enabled whether you
like them or not
but with the new feature management
module
users and partners get to select which
new features should be activated first
why does Microsoft go ahead and
Implement such functionalities into PC
they could have implemented all the new
features and then let the user
experience it
all of them together as in all days
it's simply because Microsoft recognized
that most users will not be able to
accept dramatic changes in use
experience
which Microsoft going to deliver within
is Major release
the idea is to wrap all future dramatic
user experience changes into switchable
feature flag and gradually release them
with the next two release Cycles
this approach enables Microsoft to like
disconnect environment upgrades from
worrying about any client and partner
pushback they will do features
using Facebook lag dramatically improves
SAS platform's stability
it enables Microsoft to keep all the
tenant with the latest version without
breaking user experience
let's imagine a world without which flag
for a moment
Microsoft upgrade all the tenants in a
single day
from the next day onwards there will be
many complaints from the users and
partners
Partners will also have a very hard time
since users and Consultants are
unfamiliar with the new features
they would not be able to carry out
day-to-day activities without training
on new functionalities and processes
sometimes even the existing
functionalities will not provide the end
result that they used to provide prior
to the upgrade
with the feature flag all these
limitations are and barriers are handled
now we know that why Microsoft use
feature flag approach to release new
features
let's see how we can find out these
upcoming latest features before they end
up in BC
as a partner or a user
it's very vital to be on top of these
new changes
there are a couple of ways to find out
this information before those features
end up in BC
one of the most efficient way to work is
work with Insider bits
Microsoft release inside the build very
often and partners can download this
Insider build and explore them to
understand the latest changes
another option is release plans and
roadmaps
Microsoft released these documents way
ahead of actual releases
and with that partners and end users can
get to know the confirmed upcoming
changes and plan for that
that's also another option
that is just wait for the upgrade
and then check them on your tenant with
the sandboxes
let's see how we can do that
in order for me to show that I need to
go to business Central so I'll open my
browser
and I will refresh that and I will log
in
so this is my Docker container and if I
search for
feature Management in here
it lists all the available features and
their current status
by using this page
you can try some features by yourself
without affecting other users
but there are some features you cannot
Try by yourself
this means it will be for the entire
organization once you enable it
also some of the features cannot be
turned off once you turn them on
especially if it's something related to
data upgrades
if you look closely it shows when these
features will be automatically enabled
as well in the other word forcefully
enabled by Microsoft
we will talk about that later
let's take example that I want to try
this model action by myself
so if I want to try it by myself I would
what I do is I'll click this try it out
function
it will open a new
browsing window and it's asked me to log
in again
and once I log in it will give me the
new experience of modern action bar in
this browser page
so let's go to the sales orders
and see whether it's actually working
yeah it's it does work
now I can see the modern action bind
here
let's say that I'm happy with this
experience and I think yeah it looks
good I would like to enable it for all
the users
so all I have to do is I go back to this
uh feature management page and then
enable it for all users
and let's say I need to read more about
that before I enable it so I can
actually click learn more
and it will take me to the modern action
bar Microsoft learn page and I can read
it through and I can understand what are
the impact of each of these features
let's go back to the PowerPoint slide
we discussed why Microsoft used freezer
flag then we discuss where you can find
the upcoming releases upcoming features
and lastly we discuss how to enable and
disable features within BC
next I want to take your focus to talk
about
Microsoft release Cycles briefly
how long can company hold off without
enabling these new features
and how does Microsoft release these
features
Microsoft Implement these new features
as a part of its release process so with
the major and minor releases
Microsoft released new features into
business Central
you can read about them in Microsoft
release plans
let's take an example
let's take example of a feature released
into BC on November release
till the next major release which will
be in April
that newly added feature will be
optional to use
but after six months of initial release
Microsoft will enable it
whether you like it or not
that means as a partner or a user
you get six months to try it out train
your users and consultant and also to
adjust your business processors
enabling a feature ahead of time allows
users to explore and benefit
from new functionality before it becomes
widely available
it also allows users to be part of the
testing and bug identification process
as well
by reporting issues early user can
contribute to improve the future
and also stability and performance
having said all of that
one of the major benefit
is that user can learn and develop new
skills associated with the feature
before it goes to production
this applies to the partners as well
Partners will get enough time to train
their staff so that staff will be well
equipped to support the users if
necessary
as a partner how would you know
which of your customers are actually
using these new features and who need
more support
that's where the Telemetry comes into
play
let me quickly show you uh
quick example of
how you can use the television to
identify
who's using these new features and who
are not
so if you have seen uh
or if you are being active on LinkedIn
Twitter or any social media
into that matter you might have noticed
these heaps of posts from Kenny about
business Central Parliament rapid power
bi
it's a free app you can install and
configure
let me quickly show how it works and how
it looks
if you go to
feature usage
in here
it lists most of the available feature
flag in Visa Central and some
alternative data
also it shows
which customers use each of these new
features
it gives a better view to the partners
to make themselves ready
and also to make customers ready for the
upcoming updates let's take example of a
modern action bar
so I find One Direction Mark in the
feature usage statistics and I click
that
and now it shows me
all of the all of the customer tenant
IDs that
actually use the modern action bar it
even shows like on which environment
they are using it
so with that information I will be able
to decide that okay these are the users
who actually actually actively using it
so if you think that they would need a
training and that would actually help
them you can contact them and
proposed that we can we can do a
training on you about this but if there
are customers who are actually not using
it you can talk to them and you can
actually make them ready for the next
version upgrade of Visa Central
you can install this app by going into
analyze and monetize helmetry with power
bi and if you scroll further down in
here
you will have the uh this link and once
you go there you will be asked to
install it and once you install you will
get the sample data so you can
how you can get a better understanding
and once you are ready you can configure
it with your telemetries
and then that report will actually help
quite a lot
let's go back to the purple slide
as an isv
handling a newly added feature by
Microsoft can sometimes be very
challenging
for example if that new feature is going
to cross path with one of the modules
that the partner has developed
then the partner needs to take necessary
action to ensure that once the feature
is enabled user will have us both
experience
so that that's where the feature aware
apps comes into play
feature app is a App Partners developed
but it execute different logic or
Implement changes to user experience
based on the feature flag
let's see the benefit from the partners
perspective
based on newly added features
regardless of whether they are enabled
or not
a partner or isv developed solution
should work
because it should cover both the options
of which enabled or feature disabled
if this if if that covers that the user
will have a smooth experience using your
developed solution
and your internal support team will have
a fewer worrying phone calls or emails
to deal with
let me show you how it works it's a
simple way to handle the changes but a
very effective way to keep the customers
and your support team happy
that we've got to business Central first
in my solution what I want to achieve is
when I enable the convert User Group
feature in BC
my new page accent should pop up a
message saying that modern permission
provider enabled or else it should prop
up a message saying that Legacy
permission provide enabled
let me go to my new page and my new page
called get user function
so if I go and click get user permission
it says that Legacy permission provider
enabled
now if I go back and then I said okay I
want to enable it for all the users
and I go to
web page
user permission
and then I click get user permission in
here it says modern permission provider
enabled so that means my app can
understand with the feature is enabled
or not based on that I can make
decisions on my app on how to run my
logic
let me go to visual studio open my
interface
I have interface called user permission
provider
and within that interface I have get
user permission as the procedure
signature
and I have two implementation of this
interface
the first implementation is Legacy
permission provider
which Returns the Legacy permission
provider label
and the other implementation is modern
permission provider which retains the
modern permission provider label
and then I have a code unit
in that one I have I use set user
permission provider function no
procedure
in here I have defined two variables one
is the feature management fazard
according as a variable and then the
other one is a feature flag for the User
Group
you might be wondering how did I get
this High Legacy usage groups value
it's quite simple
if you go to business Central and go to
feature management page
and go to the feature that you are
interested in and then go Ctrl alt F1
or the page inspect View and then you
can copy that value from the ID field
and with that value what I'm doing is
I'm using is enabled function in feature
management facade code unit and pass
that
and the feature benefit
will will take that value and it will do
all the checks and give me the
information about whether the feature is
enabled or not
with that information my program will
understand and decide
which implementation of the permission
provider should be used
and then I have a page
within this page what I do is I have
page action
I actually
call that
procedure that I showed you quite a
little bit earlier and then
it assign the interface and then I'm
using that interface to get the message
about which interface actually being
implemented
so it's quite simple
but it's also quite powerful as well
with this kind of simple approach
partners and isvs can provide very
smooth use experience to the end user as
the solution will work with newly
enabled feature or even without it
if you want to access the code I showed
you
can access the URL below or it will take
you to my GitHub or you can scan the QR
code as well it will take you to GitHub
as well
to recap
you can use the future management facade
code you need to understand whether the
feature is enabled it is simple as
passing the feature key to function
once you pass the feature key to the
feature management facade it checks if
there's any data upgrades running or
have been completed after all those
checks it Returns the details about
whether the features has been enabled or
not
if you are 100 not catering to both the
possibilities of feature being on and
off
I hope I can miss you a little bit to
change that approach and handle both
possibilities within your app
with that I will hand over to Vlad to
continue with the rest of the session
thank you taranga virtually
so I hope we can understand what this
approach is about and how Microsoft is
using this and this is where I wanted to
kind of help you and probably guide you
on
how on our experiences Theta how we
start this and what kind of
practices we build up to be able to
implement it into your organization
so I break this into two kind of areas
where you look into processes and the
tools
so from a process perspective
I strongly recommend to start from the
understanding of where are and what is
my features
we strongly not recommend to have your
features on the back level or a story
level task is out of scope
so this should be on a kite kind of high
level within your back walk it's either
on an epic site or a feature
then
you've seen that we are doing
in the example for the future flag we're
doing this kind of integration this is
part of your pull request review within
your pipeline so what are you
introducing as part of your pull request
review is this isolation check
so the reviewer should be able to go
through
all the scope of the change
and see how this functionality is
properly wrapped into the your feature
flag
um so basically what he should be
checking is all the subscribers all the
interfaces that you are changes
implementing
um any kind of UI that it's introducing
actions pages and Page extensions
another one is
we wanted to make sure that we're
defining what is the lifespan of your
feature
there will be absolute Mass if you are
don't have a proper culture of defining
how long my feature would live in my
environment if it's a a shortly feature
I would recommend you to link it to
wherever your release Cycles are it's
probably let's say you're doing some
agile on your iterations is two weeks
you can probably Target that your future
will leave
within iteration plus another two
iterations so you wanted to keep it in
your life environment for another two
iterations to make sure that wherever
you rolled it out to all your users you
are sure that there's no complaints you
probably check the data there is no some
performance gaps or anything like this
so you need to build up this kind of
policies in advance it helps your team
to be able to manage your features as
well as build up this customer
expectations properly
uh
when we're talking about the duration
one more thing is they usually treating
two types of features they're permanent
features and a short-lived one so again
depends on your use case you might have
a permanent feature but you need to
clearly Define that this feature is
permanent I'm not expecting to clean
this up after features goes out
depends on your scenarios
and this is where if you
some of the use cases for feature
flagging is actually provide your users
with your future early allow them to
test it and we strongly recommend you to
Define this feedback loop in my
organization when we start using the
feature flagging approach in the parable
we actually provide our users with a
portal where everyone in the world can
actually report the box to us and they
can kind of see publicly over our issues
and see how we actually prioritizing
them and moving them into the release
phases
and that's it's an interesting one
um we are in therapy we cannot don't
have customers who wants to have changes
and
you probably will see some kind of a
negative feedback on this approach from
your Consultants I had a case actually
this was in Malta
when we were kind of rolling this out to
our team I had a frustrated functional
consultant comes to me and said so you
guys will drop some rubbish feature in
our list
to our customers and my only answer was
yeah
kind of I'm safe to do this I can safely
push it to production and show this to
someone even like if it's two key users
and allow them to try it in a different
company within their manufacturing
process
yeah this can be unfinished feature
so um
yeah in terms of tooling
that's actually interesting one as well
Microsoft feature management is closed
from other partners to contribute within
their own features it's mainly done
because the feature key table it's a
system table you cannot modify it it's
invisible kind of to you you cannot
insert your new feature
before this session we actually had an
interview with Microsoft and we were
asking them what kind of plans for them
what they have in mind for a feature
management
and what we discovered they actually had
two plans one is
they do want to enhance it and we didn't
see this in a roadmap today where
Vincent was showing but we had some
dates where in April 2024 releases they
plan to enhance it there was a recent
enhancement for feature management they
introduced an option to build up
dependencies
that's the scary part of it
and it looks like that Microsoft will
have challenges to build up some
dependencies between their features
we don't have a plans for Microsoft in
terms of releasing this to be used for
partners
hopefully someday this would be possible
as well
you can do it by yourself it's probably
some of you already did it without
knowing that you're using feature
flagging approach
you might have a
kind of Boolean field in some setup
saying
this is a functionality that I wanted to
work with
it's probably the Boolean valid for the
whole organization for a whole company
and then you hiding number of your
functionalities behind this Boolean
field
it's probably not the best option
and this is where and within this
session we want us to show you the tool
that
we built in Theta to handle our feature
flagging
we call it open pitch for real and you
can use this link to go to GitHub it's
full open source and we are taking care
of publishing each of the releases into
appsource
so the way how it works and the whole
goal of this project was I'm done as
I was trying to
kind of bring this approach to business
Central Community by providing the
workable tool to manage it
and it's actually rewind on
the two or
um capabilities of business Central that
are already there that allow us to
conditionally hide or
and and show some of the actions some of
the user experience
depends on the user you probably kind of
guess what I'm talking about
and this is application areas
it's a little bit hacky but on an
interview we had with Microsoft they
actually said that they wish their
feature management solution would
actually work with application areas
because it's actually nice too for this
we finally kind of find a use case for
application errors properly
um
so the way hell open feature works is
it's calculating what feature based on
your condition you wanted to enable for
your users and then it
populates your application error effort
it's pretty much simple is it
so if you wanted to identify any of your
visible controls to a
build up it and like make sure that the
visibility of this control is controlled
by your feature flag you just Define an
application area to be equal to your
feature identifier
the same you can do with actions pages
so if you would put it on your pages
that you introduced within your feature
user will not be able to even find this
in the menu
comparing to for example Microsoft
solution where even if the feature is
disabled the users will still be able to
go to this page and be confused on what
is it about
when we come into the code isolation
you've seen in taranga's example he was
showing how you can use for a feature
for Microsoft feature where apps the
facade for Microsoft we kind of had a
similar facet that you can use
within their open feature for a year
we're actually enhancing this condition
into bringing even some Telemetry for
you so we are reporting Telemetry for a
feature management if your features
right now on board or not
and
we actually can do more I probably can
show you a little bit more on further
slides how we using this
because we are
eventually calculating the application
area you can skip it
and you can just do the check if your
feature ID is within the application
error this will be one less dependency
for Europe
um so it's kind of cool if you need it
um
cool with this in mind what I wanted to
show you that
why we call it the open feature and this
is actually coming a little bit from a
digital world
um
there are there was many services that
was providing feature management
capabilities
and there was no kind of single
structure if for example I build up
some.net application and I wanted to
introduce feature flagging into it and I
deal in with Once Darkly as my service
for future Flag Management I kind of
need to hold with a Alan starkly SDK to
be able to do this
and there is there was this kind of
initiative to build up Mark and SDK that
provides only
um like a client guideline
and client side of it and then you can
plug in the service which is in the back
end that handles your feature flag and
they call this open feature and the way
how we develop it in open source in our
report is sort of trying to follow their
SDK guidelines
so make it provider agnostic
so then and if you guys will start using
this you can contribute and actually
build up your own feature provider to
add to deal with this app
as for current version We will we build
two providers one we call conditional
provider
and this is a
to be able to cover use cases for our
pertainant extensions
so ideas that you have your application
and within this application you're
introduce a new feature so on stock code
unit you will be able to use conditional
provider API to say this is my new shiny
feature this is a description of it
that's probably some kind of Link
that the user can navigate to get some
more information about my feature
so then open feature will kind of
understand this is what it is we had a
similar UI as for our feature management
so users can go there see
what is it about
and in the condition provider you can
build up certain condition when you want
this feature to be enabled
you can do it through code
where's my next one
yep so you can say I want this feature
to be enabled only for evaluation
companies
please add and maintain this condition
and then I wanted to make sure that
my feature flag which is my customer
reward and feature is controlled by this
condition
so let me show you how this looks like
for one of the apps that we did oh thank
you very much it's bright enough
hopefully
um so what you see it's an extension
that Microsoft built at customer rewards
you might seen it in a Microsoft
documentation it's used to demo you how
you can do Advanced testing
um so what we did we actually kind of
take it with us
we were not comfortable to say that we
are Microsoft Publisher so it's
Microsoft
the mocking Microsoft
um so I'm not sure if you're familiar
with it it has a certain page extension
code units and so on
but what I wanted to show you is what
kind of changes you need to introduce
into this extension to be able to wrap
it within your feature flag using the
open feature foil
so
of course for any new
Pages the only thing that you need to do
is to change an application error from
your all
your favorite all
to where your future identifiers
similar pretty much for all other pages
that you're adding in case if you had a
page extension
you're defining any of your user
experience
and you changing again your o to your
feature ID
and when in case if you had a subscriber
this is where you need to use a code
wrapper to again wrap your code base
into if enabled condition
similarly if you had a subscriber
somewhere in your code which subscribes
to a
some standard code unit or wherever if
you depend on another SV solution
you can do this as well to make sure
that your code is not running if it's
not enabled
the bigger change actually coming to
installation logic
you can see here that in a previous
version
we had an install code unit where only
installed per company
we did some data setup we said okay set
up some kind of default data somewhere
to be able to transform this into the
wrapped approach with the feature Flex
this is where you need to move it to
some point where you can check if your
feature is enabled or not so this is
where we decoupling deployment from
release so this is where at the moment
where are you check in if your features
enables probably not in the installation
cabinet it's somewhere on login or on um
we are probably in in most cases what
we're using is a road Center on open and
subscribers sorry events
so this is where I have my role Center
notification in my feature is enabled
this is where I'm doing my data setup
we actually plan to enhance this to give
you much richer capabilities to handle
it and we will provide our own event so
you can subscribe and actually be
immediately notified when your feature
become enabled or not
and
this is where you need to head as well
some code to actually introduce your
feature into environment and as I showed
on a screenshot before
you can use uninstall app for database
we are handling
your features and conditions for the
features are data per company Falls so
it's like we can build up rules for
companies as well
it's like on top of it
so you can introduce a feature
customer rewards and you can build up
some
default conditions
actually this is where I didn't show you
one slide in previous one let's deploy
this one
let me show you how this works
you better be ready
so one of the features that customer
Warrior extension is adding it's adding
an action to customer list
to the home menu
we just deployed so we run on our
uninstall code unit
and I'm in a container in the Chronos
this is a relation company so my
condition is valid
so I can see that here I have my action
rewards level
I even can search Rewards
if I spell it correctly
or
re
Wards yes
that's it
so we have it in a menu
now I can go to
features
oh really
so this URI is provided by open feature
foil
you can see it's a similar list as a
feature management
we had an idea of our feature you have a
description that allows user to kind of
click on it and navigate to some help
materials for your feature
we show in the state and which provider
actually provide this feature for you
and because we tackling this for the
pertainant extension scenarios
this is where we wanted to handle
scenarios where you're doing your
continuous delivery
so we allowing users to actually modify
those conditions come up and say now
okay this actually should not be related
to valiation or you actually can skip
the the part where you're defining
condition and code at all
and say okay right now I do want to add
a condition
where
I don't want to show this to an admin
so I said my condition based on user
filter
it's not equal to an admin
good so we instantly showing you that
right now this condition is not active
I'm an admin
so you can see how this condition we
ever laid them for your for your
environment
I said cool please add this condition as
part of your condition to enable your
feature you can build up like certain
set of rules when you wanted this to be
enabled
and again here it's disabled
I'm going back to feature my feature
become disabled as well
I'm going back to my UI
refreshing the page
no actions anymore
for my customers
and similarly if I'm trying to search
spelling write Rewards
nothing
so it's all right now hidden from users
but we didn't do any deployment change
we didn't do app any kind of code change
it's just there
so let me go back to the slides please
cool and this is the one that I was
missing before
the conditions you have a UI in open
fish for Al to Define your conditions
as I mentioned we actually doing two
providers
um currently
and second one is a post-hoc provider
postcard is one of these services that
are available there to manage your
features
and for us what is the requirement is
weisb providers as well as a partner
we shipping
hopefully quite popular apps to an app
source and we do wanted to control our
effects not per environment but outside
of it so this is where we start using
this third-party service
so we're defining and defining
conditions for our flags externally and
allowing open feature for Al actually
communicate to the service read the
flags validate the conditions and apply
them to your application area
um
yep
now
in terms of defining
features in the post Hub environment
you can't not defining them anymore and
URL because all it's defined within a
third-party service so but what you
should do is you need to tell open fish
for Al to
can you please connect to this service
and this is where on your install code
unit you need to make sure that you
provide
you use the postcard provider API to
actually
pass some information about how to
connect to your backend service
yep and then
all the magic in terms of defining
features and defining your conditions
for your feature then going in the post
hoc
they had a quite
um strong instrumentation where you can
build up these conditions
and can we move to
My Demo
so I can show you how you can do this
what open
feature for you I was doing
um in terms of handling this provider
when we installing open feature is
actually going and streaming some
information about your users
to the post Hub so this allows you to
build up the rules based on some of
these used properties
um
any information about these users are
anonymized so you will not be able to
mention any of these identifiers back to
your customers the only let's call it
sort of a sensitive information that
we're sharing is the domain of their
email
oh that's good that I clicked this one
because sometimes I kind of
show some random one
so open feature for El stream in some
context
about your user so we are
pushing like what localization they use
with the email domain the environment it
is production it's sandbox is it sandbox
environment means like
sorry if it's a SAS environment or it's
a Docker environment
what user licenses
what version and what profile they use
this model is extensible so in case if
for your features you wanted to build up
this condition based on something else
you can extend this context
so we will stream some more information
so then based on these conditions you
can they have this kind of concept of
words I'm not sure this word I'm not
English speaking natively but basically
what you do is you build up rules based
on this property so for example we had a
rule for what is the docker environment
so everywhere where the property of the
user is environment equal to false this
is going into this group
similar we had a group of I.T managers
or admins so this is everyone who had a
profile
I.T manager or admin
and you actually can see we had a good
customer base
in a group of
SAS environment right now
this is where you can Define your
your feature Flags so I mentioned
already this Dynamic announcement
feature that we had
now it's pretty easy to add a new
feature you just defining the identifier
your feature and the description of it
and then you build up what conditions
you wanted to use for this and this is
where you can Define
to what percentage of your users you are
streaming this so this is where you
actually can say I wanted to to do it
just for 50 of the users
the open feature for here will handle
this consistency meaning if we are
streamed this for one user it will be
consistent that we've always streaming
back at the same enable state for your
feature for him going forward
you can ask why I'm showing you this
it's not a bit Central but in reality
all these Services done in the same way
you will find list of features you will
find certain user properties and certain
groups and conditions how you can do
this it's just one of them
I mentioned one of the
um features that open feature is doing
we actually
had a we built up this provider as an
interface with certain functionality and
then we implementing two of them
and one of this capabilities of it is
actually capture events
so we can capture event when the user
checking the flag if the user getting
disabled flag and when the user clicking
on the link about your feature so then
you can capture this kind of event
and this provider they actually able to
receive these events and visualize it
for you to say how many of your
validations of your flag was
calculated as valid and how much is not
so then you kind of can get daily how
many times we are checking if your
feature is disabled and you see that my
current rules is only for Docker
environment
so I can go here and said roll this out
right now for everyone in the world and
this will start getting truce so
everyone in the world start getting our
announcements
I don't need to really deploy I don't
need to pass another validation with
appsource with Microsoft team I just can
plug it in
um so I mentioned that we built this on
a open feature specification and I don't
have a links in the presentation for it
but you just can Google open feature and
you can read a little bit more about
this initiative
so now let me show you how this work in
code
yeah am I assuring yeah
so that's an example app that's
basically responding
and me back on the same flag
um that's my notification
you can see that I have a subscriber
uh sorry here is it
um on before show notification for a
roll center
I'm checking if my feature is enabled
if it's enabled
then I'm enabling my notification and if
it's valid as well
and then I'm showing the notification to
my customers
in this case I do have my install
coordinate
and as I mentioned before
I'm adding
using post Hub API to Define
what is API Keys how it should
communicate with a service
so let's try to deploy this
hopefully this will work
um
if you've seen if hopefully you remember
I showed you that their Dynamic
announcement right now enabled
for all the docker environment I am a
Docker environment so you actually see
notification
and
my notification is showing can you
please go and review our app in
appsource so the user can go and like
put some
sensitive review for us
if I go to features
this is where I can see that
I have a new Dynamic announcement
feature it's now an enabled State the
provider is my third party post Hub
provider
and I don't actually have any
option to
Define my own condition for it because
this is where we controlling this
remotely
not um the the user
comparing to the conditional one where
you do have these conditions defined
ah cool so can we get back to slides
please
awesome I'm kind of controlling someone
else
uh
so
that's our providers now there are
things to consider wherever you are
going to implement the feature flagging
approach for your organization
um I'm not native English speaker
and actually ask Chad GPT can you come
up with a proper wording for what I'm
trying to explain and
I do find this in some organizations
that are experimenting with fish
flagging and I call it decomposition
overwhelms
you probably had this conversation
within your organization when you have a
big monolith extension and you come to
your Dev team and saying you know guys I
just been on a nice workshop for
evolving Your solution and now I
actually had a great idea that I need to
break it down into small layers and
build up a dependency firm
and this is a reaction that you will get
from your team they will be confused
and not because they don't like it or
they're not comfortable with it it's
just they need to they would understand
that there will be more bits and pieces
that need to control they need to
maintain they need to deploy and so on
and similar feedback I'm getting
regarding the feature flag approach it's
actually adding another dimension into
your management kind of process into
your delivery pipeline
you can imagine that in case if you had
an extension one monolith that you break
down into multiple Wares you might have
this feature
primarily introduced in one layer but
then you might have in in other layers
some components or dependency or some
functionality that's required for this
feature so the feature flag will
introduce this kind of vertical
Dimension to your extension layers
comparing to server to horizontal yeah
where the verticals your layers
horizontal is your feature flag which
are kind of cross all your apps
what my recommendation for this to be is
to start on boarding some in some let's
code easy to sell
scenarios so as I showed you before in
my organization we start with lunch and
time scenario this can be a requirement
for monetization that you're saying like
Okay for our price implant let's build
this it's so cool we can wrap it but as
soon as this functionality is part of
your deployment pipeline is part of your
delivery pipeline that's much easier
become to actually start trying some and
other use cases
and other things to consider
we might have a schema change
we kind of start living in a world where
all our schema changes are incremental
and because we talked in SAS in most
cases
so it kind of already
more comfortable with it
but
to handle this properly I would
recommend to put a little bit more
effort into your planning phase where
you actually plan your schema change
with a new feature
and hopefully you make the types and
fills not limited like don't do maybe
Boolean in cases start with anom
right away so then it can be more
flexible
and you need as an example as I showed
before you need to move all your schema
and your data migration into your when
the feature is enabled subscriber
so then it's actually
um you are executing your
data schema changes within the flag
taranga showed you a little bit how
Microsoft is handling this actually some
of the Microsoft feature required the
data migration
so when you from the UI you enabling
this feature they actually scheduling
the background task
that is executed to migrate the data and
trying to show you the code where when
you're running is enabled it's actually
going and checking if this job is
completed and only when it's completed
it's actually allowing you to identify
the flag as enabled
one more thing because the schema change
you cannot like said ah sorry man I
wanted to do this data migration just
for this user we don't know what the
data this user will work so in this case
please avoid
any kind of user-specific condition it
should be the company or the whole
organization
uh I mentioned already the feature flag
life cycle
what I didn't mention that this process
actually introduced you another face
into your delivery pipeline which we
call a cleanup
and the idea of cleanup is
you go and you get in rid of the Legacy
code that was there as well as the
conditions that you had within your code
base
with openfeature file it's actually
quite easy to do
you can open your vs code and just run
replace in all files from your fish
identifier to all
and cleanup is done
but of course you would need to get rid
of some Legacy code that was as off
condition for your code base
one more topic is feature flag
dependencies
that's a complicated and because of the
composition overwhelms we don't want to
have the dependencies with our feature
to the matter to Provo the way how to
mitigate this risk to have these
dependencies is first of all within the
planning phase
clearly Define this separation what is
my feature is what is affecting
and the future life cycle definition
will help you to make sure that you're
getting rid of this condition so your
feature is permanently enabled
so there will be no subsequent
dependencies within the next few
releases but that's possible
and
things to consider
key takeaways for this session that we
had is feature flag approach
the couple released from deployment
hopefully we need as a community start
to separating these two words and use
them
in the right places
it's improved safe safeness of your
delivery if you start using the
continuous integration continuous
delivery use cases with the fish flag
and it can be handled with some open
source tools we are inviting you to
contribute
uh hopefully our code is not messy we're
not Microsoft but still following some
best practices
with this in mind I really wanted to
switch to
question inside
um before we start we I actually had a
very good two questions in a hob up
can we share my screen please
if it's still possible
yeah please
no
they had a h
smoking break again
oh okay there was two nice questions
that addressed in an app
and that's for Marco wind sir if I spoke
correctly and Stefan Morrow
we had actually some presents from New
Zealand to keep you hydrated if you can
come up here I can pass it to you
because they're actually heavy
okay you probably can come up to me oh
okay
you're here
good
and uh yeah so
you know the guy looks like he asked a
good question and didn't show up but if
you're somewhere there please go and and
ask your question
can we get back to spice please
um
I don't have taranga online so I will be
able to answer any questions
from his part of presentation as well
uh yeah so yeah I need to train my
throwing skills and we actually had a
present for first three uh questions so
if you have any just raise your hand
I'll get it addressed
oh I know you by name it's not cheating
just simple question the short-lived
features you mean like you had the
Legacy code and you have some new shiny
feature and you just want to implement
the one by one and then switch it off at
some point or is it something else yeah
so certainly features
um we're talking about the use case for
continuous integration you implement
your change you decouple this change
from your release pipeline
you push it you define when it's enabled
you're doing Progressive throw out of
your feature as soon as you're happy
with it this is where you clean this up
um is it an answering a question
permission management for to manage this
this kind of stuff yeah I'm happy you
guys can reach out to us through the
social network and we can try to help
you wherever you are trying to
experiment with this future flagging
uh let's go back and I will try to throw
you the T-shirt If you don't like it I
can take it
yes sure I know that's right
oh thank you guys that you are in the
first rolls because I'm probably will
not be able to handle the third one yes
so
um you mentioned that we should worry
about upgrading when enabling features
right
so does that mean we should worry about
downgrading when disabling features and
how exactly would we go about that
that's actually a good question do you
ever write any downgrade data script
yeah because I mean breaking changes are
not even possible to downgrade in BC
right yeah
yes so as I said this is a challenge
um we right now we're not addressing
this Challenge and we kind of doing this
in a similar way as Microsoft is doing
this and if you try to want if you want
to try with a new feature using
Microsoft feature management what you're
doing is creating a Sandbox environment
you go there you try a feature doesn't
work
you kill the sandbox and you kind of
going back to Microsoft so similar way
in case if you
include this as part of your continuous
delivery and you wanted to try some new
features this would be in a separate
environment you're doing this trialing
testing and so on and this is where in
some point when you're switching to
production you're sure that this is
something that you're comfortable to
move only forward and not going
backwards you might have a kill switch
scenario and this is where uh
you consider this as an emergency case
yeah so the kill switch is we suddenly
breaking business processes and the
ideas I wanted to get an instant
feedback in terms of killing this
bringing back users to a working state
and then I can incrementally deliver the
fix for them and yeah that potentially
would be this kind of date immigration
thing
and uh in case if you're handling this
hopefully you're the way you're doing
the data migration you're keeping the
data in the previous tables it's just a
matter of this moment when you start
using this feature there might be that
you start using new Fields you can have
populate in the old one and yeah this
might be a chunk but again this extreme
case which allows you to kind of
minimize the risk of your roll back and
not like oh wait I will spend a day to
roll this back so we had these cases
before thank you sure
any other questions
I'm Not Jesus one it's a last t-shirt
if you need to upgrade any feature
uh how you can manage that
what do you mean upgrade sorry new
feature
same feature oh delete that very small
thing you don't need to remove it you
don't eat disabled
yeah so uh I mean in I was showing
Independence right
so first of all
and if I understand your case correctly
the the slide that I was shown for
continuous integration where you had
like your broken feature or wherever
your user doesn't like it and you might
still keep it there enabled but then
you're delivering some enhancements for
this feature this is a scenario that
you're talking about
all right
yeah so this is I mean pretty simple
this is just a piece of code you will
have another pull request review
wherever enhancement you're doing use a
similar way you check in if this kind of
changes to your feature is wrapped into
a feature flag to make sure that they
are not like spoiled and then you
continuously delivering this for your
uat environment it become part of your
feature
so you don't need to wrap it into
another dependent feature to kind of
conditionally try this or try this this
become your one single feature
I doubt that you will need to kind of
separately
um
wrap it in in a sub 1 but probably we
need to talk more or fine and you can
kind of describe a little bit more your
use case
because it might be interesting if you
want to break it down but in most cases
you just enhancing your feature and
you're testing this as a whole feature
in the back
it might answer my question thank you
yeah your last t-shirt
no too short but more questions ah that
would be row number four uh I will try
my best yeah uh can you then pass to the
next one please
um I'm running automatic test each night
with the scripts for Freddy with PC
container helper
and could I run the tests with and
without features with a simple trick or
yeah of course I mean depends on a
tooling that you use that's a part of
your installation for your desktop unit
you can have luck okay I must program it
by Porsche or something like that sorry
what I must program it by Powershell or
something like that to enable the
feature or not
oh it depends on the tooling that you
use Microsoft actually allows you to run
the certain code units like your test
code unit with certain feature enabled
I'm not sure if it's actually a separate
comment or it's part of your container
creation process I need to validate this
and probably can get back to you with it
it's definitely a part of the creation
of your container process where you can
Define what Microsoft feature is enabled
but in case if you're using any other
app it's part of your initialization for
your test code unit so you can say now I
wanted to enable this feature please run
my test with enabled one then you can
have another code unit that actually
have a certain test for disabled feature
if you need this kind of validation
does it make sense
yeah maybe I send an email I mean again
we can go offline and actually can show
me this case please
oh okay cool you kind of had some hours
to do you have any more questions
oh okay
no
foreign
depending on on your programming
throughput you're potentially putting
into the court lots of application areas
depending I mean always depending on how
many features you introduce
was your approach to basically removing
them
especially in consideration often maybe
in an automated way have you had any
experience with that or are you
basically keeping in the
I mean 100 application areas
indefinitely
no uh so as I mentioned uh you have you
should have this feature life cycle
defined so you should have a clear date
when your feature should be clean up
when this date is coming you had a
review process there might be certain
conditions that preventing you from
disabling this it might be that
some of the key users went on holiday
and you need to wait for another two
weeks to come back to actually test it
and as you have this date and this day
comes we need to make sure that you are
removing this feature condition from
your code base so you actually deleting
this if is enabled from your code you
deleting the the old Legacy code base
and this is this cleanup phase in most
cases it's kind of short
um and you probably can Outsource it to
to the con to some of your juniors in
the team but my recommendation is first
document this process properly
and actually doing this not on the
um like a final code base just not go
through all the condition actually do
the cleanup based on change sets that
you introduce within this feature so
then you actually confirm comfortable to
say that yes I kind of clean up
everything from my future
yeah so you're basically doing it
um with a manual labor yeah I mean
introduction no automation no automation
uh you as I said if in case if you use
an open fish for Yale you probably can
write a small Powershell to replace all
but you still wanted to clean up the
conditions
replace all will still keep in code this
kind of if enabled but this would be all
and we know that all enabled always this
like your features always enable but
yeah so that's part of the kind of menu
work
thank you sure
no
good anyway if you have any more
questions you can reach out to me
through the conference day
and thank you very much for coming
please
