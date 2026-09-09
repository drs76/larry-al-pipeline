# BC TechDays 2023 - Testability - The Hammer and the Nail

- **Source:** https://www.youtube.com/watch?v=T68OQ_Yd-S0
- **Video ID:** T68OQ_Yd-S0
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 81m22s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Hello everybody.
Good afternoon. I hope everyone's
enjoyed their day one at Tech Days so
far this year.
Uh for those of you who do not know me,
uh I am an American who relocated to
Sweden. Uh I became a MVP.
Uh so I oddly enough for a year had the
track record of the only Nordic BC MVP.
Little odd thing.
But during that time, I wrote a book,
Your First 20 Hours with Business
Central. Great little getting started
guide. Uh still proud of that one. Uh
number of people have reported it helped
them pass the MB-800. So enjoy that. And
earlier this year, uh good friend of
mine, AJ Kaufman, uh we wrote the API
reference guide together. So if you need
to work with the Business Central APIs,
super helpful.
I have also participated in the project
of ALGuidelines.dev.
I hope you guys have seen that, have
visited that, taken a look at some of
the rules and design patterns. There's
lots of good info there.
I also released for free a licensing
application that partners can monetize
their AppSource apps, including little
indie dev shops with just one guy. So if
you have a cool little idea, use it.
It's free and it's open source. Uh and
if you just want to show your BC love,
there's wallpapers you can grab for free
as well. And last little about me thing,
uh there's also a community newsletter
you can sign up to. Uh this does a
roundup of all the blogs of the
community. Well north of 100,
approaching 200 sources. If there's new
posts, you can go grab the info from
that. It will send emails weekly and
just give you what you need to know.
So
let's get to the good stuff.
First of all, one of the things that I
like to do is I like to cook. But one of
the best practices when it comes to
cooking is you get everything together,
get everything prepared. And so what
we're applying that philosophy today of
I'm making sure that we have the right
foundational knowledge to move forward.
So, we're going to go back a little bit
to a couple of design principles because
we're going to get weird
and it helps to start with a shared
foundation when we go a little weird.
So, originally, once upon a time, a VAR
would demonstrate the product to a
customer. A salesperson would show what
they needed to do, maybe what the gaps
were.
A project manager would come along with
their consultant and they try to figure
out what all do we need to do for an
implementation and they might write rope
in a developer to say, "Okay, we need to
customize this to be able to implement
it."
Okay, not too bad. And after go live, we
hand it to a support person who's
generally horrified by the job of the
previous team.
Uh
some of you are going, "Oh, you have
support people. How nice for you."
That's me.
Okay, fair enough. And then there are
other people who work for ISVs who
create products. And that flow is you
gather requirements, hopefully. They
might be from a live customer, but you
gather requirements from users, you grab
the requirements from the stakeholders,
and then, of course, you put together
the solution with a product manager and
development effort.
Pretty straightforward. And then
historically, the delivery was you would
install that for the end user.
Good old FOBs.
Way back long ago.
Some of you might not even know FOBs
anymore.
That's fine. So, not to horrify anyone
and bring up some history
and open scars, but in the before times,
back in the financial days,
there was one development environment.
There was a single IDE. It was one
language and we had one way of
presenting things on the screen, forms.
They weren't even pages yet. So, if you
don't know forms, welcome to the history
times. There was everything you needed
to develop was just on the CD with the
exception of the license file, which was
on a floppy.
Well, if you are one of those folks who
grew up in these times, you're probably
feeling like woo woo.
The modern world is great, but there's
an awful lot of stuff.
You are not wrong. You are not wrong at
all. And you are probably challenged
with the fact that as a technical person
in your organization,
the project manager, the consultative
people, they're not taking on a lot of
these new technologies. They're not
hiring all lot of the times a whole new
department to take on these
technologies. So, guess what you get to
do.
You get to learn.
And learn.
And keep up with all of these things. I
ran out of room on the slide.
These are all things and all
technologies I've had to use, work with,
understand, and implement best practices
in the past week.
Most of the development companies I know
call this an IT department.
So, if you're a developer in the room
and you're going, "I don't know how to
keep up with all this." That's why,
because you're being a department. So.
The challenge here is many of these
things take organizational effort to
really implement correctly.
And that brings us to what we're going
to be talking about today. One of the
elements that we're going to look at
implementing as an organization is the
test framework.
The test framework
lets us do a bunch of things. But,
before I go too much further, because
we've come a long way with testability.
Those of you remember 10 years ago, we
didn't have all the tools to run the
tests that we do we do today.
There's a whole bunch of stuff that we
have now, pipelines and testability. And
it feels like extra effort, but it's
not. It's good stuff.
And so I wanted to just at least salute
with this very delightfully ancient
quote that's been paraphrased
paraphrased and attributed over and over
again in different ways, but the
original source of this is we are
standing on the shoulders of giants and
so I just want to give a small nod to
Luke in the audience.
Uh if you haven't read his book on
testability, you should be.
Uh and if you know Luke, you also would
know that I am also slightly making a
height joke.
Sorry.
Um
but when I'm talking about testability
today,
this is a cultivated process
to take a set of preconditions, your
starting data.
You are going to apply a set of
processes,
verify that the process worked,
and then you want to be able to
repeatably do things. You want to be
able to have those changes rolled back.
Now if you're using the AL testing
tools, most of this is handled for you
uh at least on the rollback side by the
test runners themselves. Pretty
straightforward.
And it's good stuff.
Um so we're going to look at you can
change how you use testability code when
you change the ingredients of this list.
When you build a test app, you're
bringing knowledge, you're bringing your
generation of preconditions, you're
running processes, and you're verifying
results, and then theoretically the AL
framework is doing the rollback for you.
That's good. That's pretty awesome
stuff. I hope most of the people in the
audience have at least experimented with
writing test applications, if not
embraced the beginning of doing that uh
in their organization.
So in theory, what we're hearing is that
the modern development experience is
that you're going to create solutions,
whether they be for a specific customer
or for AppSource, whatever have you, you
theoretically are gathering your users,
your stakeholders, your project team,
and you're analyzing things, you're
working through creating the testability
requirements.
Because testability requirements is just
a short list of what will I do as a
person trying this application to
confirm that it works.
That's a really good thing to do. And
then theoretically, if you're doing
ATDD, you then code to pass those
requirements. I know a lot of people are
hesitant to start down that path, but
it's pretty useful. And then in the
perfect world, you're also using
pipelines to maintain, run those tests,
to do deployments, all that stuff,
whether it be to AppSource or directly
to customer environments, whatever have
you.
So this is the modern process that I
hope a lot of people, even if they're
not doing yet, they're at least familiar
with, that would be some of the good
stuff.
So,
now we have a shared foundation that we
can jump off of. That's where we started
from, that's what we're hearing about.
There are great sessions here. I'm
looking greatly forward to Wiebe and
Waldo tomorrow talking about interfaces
and how they help testability. That's
going to be fun.
So, let's talk about the overall
implementation process.
Again, using this older framework,
we have our traditional test use that
there's some sort of customization that
needs to happen for our internal
stakeholders, for our customer, for our
product. Well, we're going to assess
those needs. We're going to create a set
of tests that for that functionality
that we are making, we are going to
confirm that it works.
That's good, absolutely. That makes
sense.
I like
to do what is called smoke tests that
test critical mission business processes
from end to finish for my customers.
Uh one of the easiest ways that I have
started getting customers to appreciate
testability is I sit with them and I
say, "Okay, you have five departments.
Each of those departments give me your
top 10 list tomorrow that if BC made
that process die,
so would your business."
Well, that that kind of wakes people up
a little and you can look at that and
say, "All right, I just want to make
tests that
take your sales quote, make a sales
order, ship, pick, and make sure things
can go out the door." Because you never
want to find out that oh, over the
weekend the next minor added a new
feature
and now we can't ship.
That's a bad Monday morning. I don't
like those Monday mornings. Smoke tests
help me do that. They confirm the
mission critical processes are working.
So, I hope there are some folks in the
audience going, "I do that." Uh I hope
so.
It's a really great thing to do.
Another scenario that is an easy place
to start is in the support workflow.
I like to make for a lot of my customers
who have support cases a special testing
app that all it does is test old
tickets.
Because if you've ever worked support,
I'm sorry, but also you would have to uh
have collected what was the expected
results and what are the steps to
reproduce.
That's a test case right there.
So, you can very easily take any support
tickets and go, "This is a test. It's an
opportunity to create some tests." Um
I'm a married man. Uh I don't know how
many folks in the audience are also
married to someone or someone's. I
whatever. The uh
But if you make a mistake at home,
you say, "I'm sorry." You make it
better.
Make that same mistake the second time,
boy, that I'm sorry better be a lot more
sincere.
Customers are people, too.
They I know.
Oh,
sorry. Take a moment to take that in.
Customers are people, too.
If you
apologize for something and then do it
again 2 weeks later, how much angrier
are they?
Support apps that do testability against
old tickets means that you never
reintroduce the same bug. And boy, is
that a nice easy thing to not make a
customer angry. It doesn't make anyone
excited if you're sitting in a team
meeting going, "I would like to make
sure we don't make our customers
furious." They go,
"Could you go get the water?"
It's not exciting, but exciting is also
being yelled at on the phone.
But, there's also scenarios that some of
my customers who are ISVs love to do.
And I love this so much. I've helped a
few customers uh
architect these solutions. Make an app
that diagnoses
all of the setup information in a
customer's live environment.
Are they missing number fields?
Are they missing critical setup?
Make a toolkit that you can say, "Okay,
we added some critical mandatory field
on the customer card that has to be
filled in or you can't do sales
operations." Well, you can make a
diagnostic app that goes through all of
their customers in a sandbox and says,
"Are all of those filled in?" No, I see
there there's a potential risk and a
potential problem. You can build
diagnostic apps using testability to
say, "Where are the potential problems?"
And my favorite part about that is if
you do that and you put that in
AppSource
along with the solution itself, that
means that customers who are the kind of
customers who like to be able to
self-solve can run this before they call
you.
In your first emails to people, it can
be an auto response of, "Have you tried
running the diagnostic apps to kind find
common solutions. And by putting this
into AppSource with all of these common
FAQ style problems,
well, you can grow that over time just
as you do your main app. Every time you
get new problems that you've seen time
and time again,
add a diagnostic to it. Why not? You can
do lots of fun stuff with that. You can
create JSONs of logs and all sorts of
things.
And then, of course, we get into all the
fun and exciting stuff about pipelines.
I talk about them all the time. I'm not
going to do it too much today, but
please tell me most people here are
using pipelines.
Uh okay.
A few people humored me. Thank you.
So, the other bright side to
adding pipelines to the mix is all of
those different proactive, reactive
tests, the smoke tests, you can run them
in advance. You can run them on a
scheduled basis. You can set it up so
that they run on a weekly against the
next minor, next major. You can go, I
know there's a new major version of BC
around the corner. I would like to find
out
via an automated email out of DevOps
that there is a problem coming.
I do not want to find out that there is
a problem with my solution via the
warehouse manager going, I can't get the
shipment to go through and the truck is
leaving in 5 minutes.
You don't want to get the email from
Microsoft saying the environment
couldn't be upgraded.
Or worse, your application was
uninstalled.
Those are bad days.
So, looking at this older style
framework,
we just helped a whole bunch with the
customized process. We are able to
validate that the customizations work.
That's good. We potentially have helped
solve support cases and make them stay
solved. That second part is real
important, stay solved. And we found a
way to even do some preventative things.
We can test in advance. Hopefully, some
of those are at least not news to people
here.
Uh the bad news
we we did make analysis worse.
Uh sorry about that.
The the small good news is that analysis
is something you do as a team. That
shouldn't necessarily be a developer
only job. It should not be. It should be
things that consultants, project
managers, both client side, internal
stakeholders, all these different people
should be helping with the analysis. But
I will admit what we're doing is making
analysis take a little more effort. So,
I put a red X on that because we didn't
make it easier. We didn't make it
gentler. We made it better, but we did
make it more work.
However, one of Luke's great things that
he talks about is the money you spend on
analysis and testing and making sure
things are right.
Later on, if you spend the time and
effort to do that as support cases, it's
a lot a lot higher.
We were talking in our workshops earlier
this week, if you do not architect your
solutions in good way, you're building
technical debt. And the metaphor I use
for that is you are putting your
development effort on a credit card.
And boy are the interest rates rough on
that.
And each and every month when there's a
new major and a new minor, you take that
credit card statement and you throw it
away.
We don't need it.
Okay. Eventually, when you hit a big
roadblock, the technical debt interest
is going to be more significant. So,
bear that in mind.
But we haven't touched sales.
And I know
I know we're mostly a technical
conference here. I'm sorry for those of
you I'm going to be scary and say we
should help sales people.
Sorry.
Um
but sales people need to demonstrate
complex processes and features.
Hopefully, you guys are out there
building cool stuff.
Well, the sales people
need to know how to show off that cool
stuff. Trainers who are working with the
sales people need to show people how to
use that cool stuff.
But sales people also have an
interesting challenge. Uh I don't know
how many of you have been in the field
doing demonstrations. I have.
Uh have you ever met with, say, a fish
company and tried to show them Cronus?
It doesn't really relate for them. It
takes a lot of mental effort for them to
go, "I see how selling units of
furniture relates to my business that at
4:00 in the morning I'm getting up with
my crew and we're filleting salmon."
It's a bit of a reach to ask customers
to do during a sales process.
So,
it is TechDays, we do need to do some
demonstrations, right? So, let's do a
demo.
I have built, and this is going to be
available on GitHub, and it is right now
uh on the GitHub for Spare Brand Ideas
sales demo helper.
And you are welcome to use this as
inspiration for your own solutions.
And what this is
is using the ideas of testability.
We're
we're wanting to remember testability is
generate baseline, apply process,
validate the process, roll things back.
Well, in a sales operation,
wouldn't it be really cool if you had
better baselines to do demonstrations
on?
So, for example, one of the ones I made
here in this little demo helper is a
toolkit here for sales people to say,
"What do you want to demonstrate to an
end user today?"
Well,
I don't know about you, but if you try
to build a Power BI against Cronus data
to show sales trends,
those five orders don't help.
So,
I got asked the question, could we,
theoretically using the tools of
testability, say, we would like more
orders? And the zoom on this is pretty
intense. Let's uh let's zoom that up a
little bit.
It's a big screen. I think folks can go.
So, what we've said is we would like to
be able to create 30 orders per month,
but we also need some historical data.
We need some posted transactions. So,
let's make 20 invoices per month, and
we're going to be doing some
demonstration for the first half of the
year, so let's make the
date range there. And what is some of
the variability we would like to have on
the item quantity? Cuz after all, if
every single month we're doing
transactions where we sell 10 items, 10
items, 10 items, that's not a very
interesting Power BI. That's not a very
interesting and analysis tool.
And we can say, I would like to grab
these three different customers because
domestic, foreign, EU, we want to see
some transactions against different
posting groups.
And we can also come on down here and
say, well, which items do we want to
have involved? I would like to have all
five of these on these different orders.
Okay.
And we hit run helper, and those of you
who are used to doing some of the
operations in BC can already guess a
little bit at what's going on right now
because of all the nice little pop-ups
that we're getting. I didn't suppress
them because I think it's fun to see it.
But what this does is it takes all those
parameters, and that quickly, now we've
got some rich test data.
So, if I'm going to go show my customer,
what does it look like when you've got a
good volume of sales orders? Well,
here's a bunch.
And I want to potentially see some sales
invoice to see the history data. Well,
here's a bunch scattered across time.
And if we look into the details of just
one of these,
we'll see that it grabbed all those
different items, and it threw some
different amounts, just randomly,
grabbed some different things.
And that's not too complicated to
accomplish if you think about what's
actually happening behind the scenes
here.
In the customer data generation,
we can make use of some of the testing
libraries to make this nice and easy
code for us to run.
So, looking at the logic that we're
doing here, we have some things where
we're loading up the settings values.
You can crawl through the code later.
I'm not going to give a line-by-line
analysis of this, but the key idea here
is for each customer,
we're going to look to see for each
month, we want to
generate sales orders if that's been
asked for, and we'd like to generate
sales orders if that's been asked for.
And all the generate sales orders is
doing is it's taking a significant
advantage of this library right here,
library sales. Library sales has some
functions on it, create header, create
sales line.
Because we don't really care too much
about the data that's on it. We need
there to be some data. We just need
there to be some data. Okay. Well, I
don't know about you, but I really do
get tired of creating the sales header
line by line. It's about 12 lines to
make a good sales header. It's about
another eight or 10 lines to create a
sales line. Here it's one.
Nice and easy.
The same is true for our posted sales
invoices. We just do the same exact
logic except at the end,
we also
just call a little post function.
There are a bunch of libraries in the
testing framework that allow us to take
advantage of the testability suite to
run things.
But you might ask the question of, well,
if you're using all these test
libraries, how come the data is still
present in the database?
Well, for those of you who caught on,
you're ahead of the game a little bit,
but
if you look at the AL test tool and what
it does when it's running things,
hopefully most of you have seen this,
but some of you might have glossed over
one of the key fields here is
up in the header for each of these
sections,
we define what test runner is running
all of the tests for us.
This is the default setting.
It's called isolated codeunit. Hopefully
most people know what the isolation
options are and what they mean, but in
short, test runners run test code.
And at the end of the codeunit, hence
the name, at the end of the codeunit,
it's going to roll back the
transactions.
So, in our sales demo helper, we create
our own little tiny test runner,
which is a rarely used in the field uh
subtype here,
test test runner,
and most importantly, we flag a little
property that is only valid on test
runners
that I'm aware of,
uh
test isolation equals disabled.
What this means is that when we're all
done, don't do the rollback.
I'd like that data to live. So,
obviously, you not want to do this in
production.
But,
this allows you to generate lots and
lots of data using the testability
scripts, using the test tools, and don't
roll it back at the end. That's fine.
I'm perfectly content with polluting the
database. Cuz traditionally, if a test
doesn't roll back, that's polluting your
tests. It's making the next run dirty
because your data is no longer the same.
Well, in this case, we want that dirty
data. We're making it on purpose. That
is the whole point.
And you can do some other fun stuff
because I did mention that one of the
challenges when you're showing a fish
company, for example, that
uh BC is relatable for them.
Well, what can you do to make things
more relatable? I've worked with sales
people in the past to create demo
scripts and all that sort of thing. And
what they've done is they typically will
follow some sort of script, but they
will follow a set up script and they're
sitting there working with a BC
container these days. Back in the day
they would work with a
uh installation on their local machine
and they would painstakingly sit down
and create all the items that would be
more relatable for their customer. So,
they for our given fish company, they
would make a whole bunch of new items,
salmon, cod, shrimp, all those different
things. So, at least there's something
in the database that they can put on a
sales order that will make more sense to
the customer.
Well, go figure. We could go ahead and
do some more with that.
So, I took this example
where I wanted to create some new item
numbers in my system
and this little setup configuration
says, "Okay, well, we want to name we
want this number. We want the name. We
want these different units of measure.
They want to show off some of the
different unit of measure functionality.
And we want some standard settings
across all those. They use FIFO in this
environment. Or we want to be able to
demonstrate effectively the difference
between standard costing on one fish
versus FIFO. Uh and for some ungodly
reason we really want to show them
average costing."
Um
There there are some horrors there.
But creating the items quickly is nice
and all, but when you go to add them to
a sales order, how are you going to show
them item availability?
By period, by location, any of those
things. How are you going to show what's
available on the item card?
You can't do that. That's just creating
This is just going to create the items.
Well, we can add some additional
settings and I did so as part of this
demonstration toolkit where we can say,
"You know what? I want you to go back in
time and create some stock settings for
this as well. I want you between the 1st
and the 6th of June. Every 2 weeks, I
want you to create some noise. I want
you to add some positive adjustments
that bring in that data.
And additionally, on top of that, we're
going to want to demonstrate order
promising maybe against some purchase
orders coming in. So, I also say, "All
right, let's also add on here all of
these different purchase settings." We
can say that every 3 weeks we want to
order some various amount from this
vendor.
Okay.
No problem.
We run the helper.
It goes ahead and it creates all the
items first.
And then, as you can guess by the pop-up
that's happening right now, we're doing
some posting. It's posting some item
journal lines.
Okay. Well, now if we head off to our
item list, we can see
da da da
slowly but surely
We can see those now exist and it has
inventory.
This is a lot easier of a technique that
if your sales people are needing to spin
up a new sandbox to demonstrate to a
partner in 5 minutes, "Oh no, they're
here. Can I make this make more sense?
They're a car company."
Whatever have you. Whatever you need to
do to make this more relatable, you can
speed that along.
And you can have lots more info. We can
see that this item not only is there a
bunch more in stock, but there's a whole
bunch of purchase orders created for
that. So, you can see over time that
there is incoming quantities of
different amounts.
This allows you to build a lot more data
to show a customer. What does it really
look like? Not what does it look like
when there are five purchase orders in
the system.
That's hard to relate to for a lot of
customers, I find.
So,
uh the logic to that again not very far
off from what we've done before. If we
look at the item generation logic and we
won't need to spend too much time on
this. Uh we're making use of the library
inventory.
And what we'll do,
let me make that a little bigger here.
What we'll do is we generate the item.
And if we have some past stock settings,
we'll go ahead and create an item
journal entry, and we'll post the item
journal.
And if they have some purchase settings
that are valid, cuz after all, it is a
salesperson using this tool, maybe they
messed something up.
Um we go ahead and create some purchase
settings, and we create the purchase
documents. And these rely on standard
libraries, and you do see I do have some
assignment stuff, cuz we do want to
validate some of the different fields
and check all the work and everything
like that. But if we look at our create
purchase document, again, same thing. We
have one nice easy line where we create
the purchase order, we assign a few
extra fields based on our settings, and
then we create a purchase line with that
item.
No big deal.
You don't have to do the work. You don't
have to rely, even with Copilot's help,
since we've been hearing a lot about
that.
Even with Copilot's help, we can do
stuff in one line here.
It's a lot easier.
So, using the testability tools, you can
create demonstration starters that make
it easier for sales people to relate
that information to their customers.
You can also make the system make more
sense to a different audience. I I
appreciate Cronus for what it is, but it
is better to speak to the customer where
they live.
Uh many of you in the room are creating
solutions that are specific to you.
There's no way in the world that Cronus
can help demonstrate the cool stuff
you've just added to Business Central.
So, make your own. Make your own cool
stuff. Uh just to give an example,
because, you know, it's nice to have
some real-world examples, and I'll
bravely wander off to the internet. If
you look at Contoso Coffee,
If we look at Contoso Coffee Business
Central,
you may have heard of this already. You
may not have.
Microsoft's doing that exact same thing.
Here on the Docs website, we have this
introduction to Contoso Coffee demo
data.
If you look, there are walkthroughs of I
need to learn the basics of if you set
up the basic warehousing module, what
does it actually look like to receive
and ship inventory.
What's involved in that? There is a
companion app to this documentation that
generates all of the data that this
documentation relies on.
It affectionately has been referred to
as part of the bloatware ecosystem.
But, if you create sandboxes, you will
often find there is a Contoso Coffee
application installed in your sandbox.
That's what that is.
It's an app that goes along with these
documentations that you can go in here
following this documentation
step-by-step, and this bin exists. This
item exists. There are values for these
things. So, Microsoft is an example of
the kind of company that is going, "You
should be able to take documentation and
have your data match it. You should be
able to move forward with that."
Additionally, uh besides the fact that
as I said, we are taking the starting
data, we're applying the process, we're
we don't need to verify the results. The
results are the results, whatever they
are. And we don't need to roll back the
changes.
That's cool.
But, we can do training off of this.
This is a really fantastic way to prep
classroom environments. For those of you
who are doing online training, you're
doing workshops, you're doing seminars
over and over again to teach people how
to use this product, well, wouldn't it
be great to just have an app that sets
all of that environment up in one go?
Wouldn't it be better that the
initialization process of preparing that
environment for the environment was
something that was part of a pipeline or
an app that you can just run?
It's fantastic, and you can make the
documentation make sense.
Additionally, those of you who are
creating product, your product,
odds are pretty good that there are
partners out there that you're hoping
are selling your solution.
You're hoping that their sales people
know how to demonstrate your cool stuff.
Uh
that's a lot of hope.
I I I don't like relying on hope. It's
great. I like holding hope, but I don't
like building my plans on hope.
So, by building these testability
demonstration toolkits, the
documentation to go along with it, you
can even do things like I did here in
the demonstration toolkit where in the
uh sales, you can give links to your
website
to open the demo script, open the slide
deck to go with it. You can help the
people who are trying to demonstrate
this that maybe because you're on
AppSource, you don't even know who the
partners are.
So, give them this.
So, that way they have something to go
on. Make them able to see some of the
best stuff.
And then, of course, there are plenty of
folks who are customers, who are savvy,
who are smart folks.
I suspect there are a few of you here
today. That makes you very savvy
customers if you're here today.
But, those folks are able to install
stuff from AppSource and figure it out
themselves.
Well,
do you think if you're making a product
for AppSource that a customer right now
today, they can hit try it now, are they
going to get the best experience they
can?
Maybe.
But, wouldn't it be cool if they can
install a companion app that you you
recommend that says, "Would you like me
to initialize your sandbox so you can
see how it all looks?"
Um a place where you will find Microsoft
doing that. I love it a whole bunch for
those of you who have been to some of
the telemetry sessions, uh looking at
the Power BI BI app for telemetry, one
of the great things Kenny did, he did
the same thing. He creates sample data
in the app that even before you hook up
the Power BI app to your telemetry
environment, you can see what it would
look like.
That's pretty powerful. So, make it
simple.
So,
we've now helped
the sales people out,
which I know that's not exciting for
some folks here. I'm I'm sorry.
But,
we also
popped a little bit of an extra bonus
check mark into training.
So, that's pretty cool.
But, what about the implementation part?
Well, implementation
uh
I don't know how many developers have
also done implementations by themselves,
but hopefully at least some of you have
participated in implementations and seen
how it goes.
The person in charge of implementing for
a customer
has to manage lots and lots of setup
information. I love Business Central, I
do.
It has a lot of settings. You can go
wrong very easily with a lot of
settings. This is why a lot of times you
will hear people say you should set up
controls, permissions, change log on
setups because one check box can throw
off your whole business.
And then of course, if you're migrating
from an old system into Business
Central, you're managing a whole bunch
of new data coming into the system. Who
knows how right it is?
You hope it's pretty good,
especially if you're dealing with
customers, vendors, items, critical
master data. You potentially you're
dealing with thousands and thousands of
records. I've absolutely migrated
someone from another system that had
6,000 customers, 9,000 vendors, and well
north of 10,000 items that they all
transact. All of those are real and
valid transactionable master data
records.
That's a lot of information to check.
You also have to test dozens and
hundreds of operations and permutations
of operations. I'm going to ship with
this. I'm going to ship partial. I'm
going to receive partial. Oh, and now we
also have some over shipping
functionality, under receiving. There's
many different permutations. Uh we've
got three different warehouses and they
have different levels of warehousing set
to them.
That's a lot of testing for your
customer to do, never mind your
implementation team.
So,
let's help them out a little bit.
Let's take a different way of thinking
about things
cuz after all, we talked about how
testability
is taking a set of preconditions,
applying a process,
validating results, and rolling back.
Well,
we
are trying to build our test database
where we're migrating information into
that test database. Guess what? That's
our baseline data.
So, if we look at what I've built here
as a go live checklist example, there's
a lot of
Scotch tape holding this together.
Um if we look at this,
here's a really basic set of examples.
We want to make sure that some of the
different posting setups are populated.
We want to make sure
a real simple one, common sort of thing
with new people who are using Business
Central, you have all of your income
statement accounts, you have all your
balance sheet accounts, or vice versa,
depending on your country.
Um
well, it's real easy when you insert a
new one in the middle of all your
expenses to forget to swap that from
balance sheet to income statement, and
things go a little nutty.
So, how do you know for sure that all of
your GL accounts are set to the right
thing? That's a really easy thing for us
to check, but
let's take a look at what we could do
to check that.
Well, we can
have a little testability code in that
says, "All right, you know, it's
hard-coded here, but we could absolutely
do this with some cool parameter
tricks." And I'm going to be updating
this demonstration to show how uh as
part of the fall updates to these
things. But, in my customer environment,
everything up to 599 should be balance
sheet, everything after 6,000 should be
income statement. So, I want to run my
selected tests here,
and it will go through and check all of
that data and go, "Okay.
Well, there are 270 GL accounts, 266 of
them are set correctly, four of them are
not."
Whoops.
Well, that's cool. So, here what we're
doing is we are verifying the data using
the testability. Just as we did before,
we have a code runner test runner here,
but we are leaving that test isolation
on its default setting, which is we
definitely want to roll back anything we
change.
The reason we're doing this with a
custom test runner for the people who
really love the whys and everything
behind the scenes, uh we run our own
test runner so we can capture the errors
and present them.
So, that's a really basic example, sure,
like just check we could effectively do
this with a filter. It's not very
exciting example,
but here's where we start to get a
little bit more exciting.
Uh when you're migrating customer data,
you theoretically know how many
customers should be blocked or
unblocked, for example, coming from an
old system. We want to have 6,000
customers, we know 100 of them are
presently blocked. Well, did those
migrate incorrectly? Not yet. Okay.
We can see that in this particular case,
we can run this selected test. It will
go through the operations and again,
we're doing something a little bit
simple here that we're making sure that
the
data is valid. This could be done with a
filter. Sure, we could do some basic
counting and all that sort of thing.
But we can also do operations where
theoretically as part of this, for each
and every customer, we can check, are
the posting groups right? Are they
within expectations? And importantly, as
part of using testability, you can run
test transactions. So we could say for
each of these customers, can we ship
them items?
I personally, if we're importing 6,000
customers,
would really like to know
that we can transact on each and every
one of those 6,000 customers.
Because otherwise,
you're hoping.
And again,
I don't really like hope to be in the
mortar of the foundation of the project.
I think there's a lot more that we can
do with validating these things. So
these are example tests where we can for
each and every customer of the system,
we write up a sales order, we ship them
items. We want to receive cash from
them. We want to make sure we can issue
credit memos to them. Make sure that
these are all working correctly.
And additionally,
this is based off of real-world
examples.
Item journal positive of adjustments. I
mentioned a customer that had over
10,000 items and they were bringing in
lots of stuff. When you're first getting
a system started,
you need to create all the beginning
balances. Well, that means that you've
got a whole bunch of item journals that
have to be created to bring in those
beginning balances, of course.
Well,
the day before the go-live, one of the
location managers went,
"We label all of our shelves.
Those seem like bins to me.
And he went to the location card and
went, "Ah, there's a really cool option
on here called bin mandatory."
Uh-oh.
There are at least a few people in the
room who realized what went wrong real
fast because no longer could any of
those item journals post. All the bin
codes were blank.
So, what we can do here is as part of
our item tests, we can run a positive
adjustment in a testing scenario for
every single item in the system, for
every location in the system. And that's
not too hard. It's It's really basic
code when you think about it. It's just
the idea is a little bit different. So,
if we look at our positive adjustment
test here,
we say for each location,
we go through each item, and we create
an item journal line.
And if that goes correctly, then let's
also try to post it.
And so, this will catch cool stuff, too,
like can we create the journal line for
that item? Cuz if we can't, I really
want to know that, too. So, we'll
capture that information, and we add
that to our list of errors.
Now, the advantage to all of this
is that this is all an app file,
which means that guess what? You can set
all of these tests to run as part of a
scheduled pipeline.
So, as you are getting closer and closer
to your go live,
guess what you can do.
You can check the data. You can use
those pipelines to revalidate, but
importantly, you can answer with
certainty,
"How close are we to actually ready?"
You can check every day to go, "Did some
guy turn on bin mandatory? Did someone
delete the sales order numbers field in
sales and receivables setup.
Absolutely, you can turn on change log
setup and find out those things after
the fact. That's great for diagnostics
afterwards.
But if you create tools like this and
you run tools like this as part of your
implementation,
hope isn't one of the critical points in
your foundation.
So, as mentioned, we're dropping the
starting data and we just apply the
process, verify the results, and roll
back the changes.
So, now
we've helped the implementation process.
Cool.
That's a lot of fun.
There's a bunch of different good news,
bad news off of this.
The good news
on this
is that right from the get-go, you even
in the sales part of the process, the
first time the customer is ever
interacting with you, testability has
been brought to the table in some small
way.
The earliest point of contact with a
business life cycle in your organization
now understands that automation, which
is what testability is built on,
automation has value to them.
And if you are building testability to
test the data to validate an
implementation, that means that you are
validating the data every step along the
way.
And customers are seeing how careful you
are about their business operations.
Because after all, you're the doctor
operating on the patient, the patient is
their business.
If the patient doesn't make it, it's a
bad day for everyone.
So, it's much, much easier to make the
case that when they ask for a
customization,
guess what? We should do just like we
did during the implementation and make
sure.
Hope should not be part of the equation.
We should make sure.
The the bad news now,
unfortunately,
you get more to do.
So, the challenge with adding, okay, in
the sales process, in the implementation
process, we want to write all this cool
new code. Most of you in the room, I'm
guessing are already going, I already
have to write a lot of code. You already
showed us a slide of how much I'm not
even getting to write the code anymore.
So, I feel bad about that. So,
to make things a little bit better, as
an apology,
I am introducing a project that is going
to be released
uh
by fall, tentatively,
and is another open-source tool that I
hope will help people out a little bit
with testability.
So, let's take a look at
something a little bit fun. I haven't
shown this off anywhere to anyone yet.
So, you guys are seeing it for the first
time.
I have a little tool that is starting to
be put together. This is going to be an
open-source project that I am roping
Stefan Marrone into helping me with cuz
he had some cool ideas to make this
better.
So, what this does
is let's take the default settings.
It'll take a second just to initialize
the database.
I create
these little packages.
For those of you who have worked with
config packages, this should look pretty
similar.
Here's a whole bunch of tables.
Here's some of the different fields we
want to have.
And maybe we want to do some filters on
things. Maybe we want to do some
anonymization on these fields.
Okay, but what does it do?
Well, what we are able to do with this
is I can click generate.
Open this up.
Look what we've got in this zip file for
you.
I heard some very quiet chuckling on
that, and good.
First of all, we get our wall of
permission of all the different tables
that are involved.
But what we also get in this monstrous
pile that we're looking at in Notepad
for delightful reasons, but sure.
We get a function called called create
item that is going to initialize based
on all those different fields that we
want to have,
all sorts of different parameters. But
if we scroll on down to the very bottom
here,
what we get is this wonderful little
thing. Let's turn off word wrap and make
that a little more visible.
We get
a wonderful world where we're creating
items.
Creating item, creating item.
This little toolkit lets you
for all of those different things that
we've just talked about, for creating
demonstration data, for creating
testability solutions,
this allows you to configure what is
some of the information that you
potentially would want to extract from
an existing system.
And it takes that information, and it
makes a code unit.
And everything about this is handled,
written for you,
and just all you have to do is call run.
So you take this little package, you
drop this into your existing testability
pipelines, your sales demonstration
helpers, whatever have you. You check
this into source control, which is why
we anonymize.
And now you can go ahead and run these
initialization routines.
You can just march right through
creating the data.
Because after all, I like Copilot. I do.
But I have customers that they need a
customization that says, "Okay, over 5
years history, we needed the ability to
identify spikes in demand." And that's
the customization is where identifying
spikes. Well, you can't do that
off of 5 years of ledger entries using
Cronus.
You can't even generate 5 years of
ledger entries very easily using config
packages.
But you sure can through code units.
Absolutely can.
So, the idea behind this is very simple.
Is let's take some information.
Let's choose how to configure it. Let's
capture it.
And you can add all sorts of different
things just like any config package
would. You could have a custom uh
package. Uh as part of our workshops, we
had a gift box solution that we had
configured some
uh demonstration company to build a good
solution architecture around.
I believe it was 70 6,000. No, 70,000
maybe.
Uh do do do do do. Let me grab our gift
box. If we browse this just like config
packages,
you can just grab anything that's in the
system. Any tenant data, it doesn't
matter.
So, we'll say, "Okay. We'll rename
that." Sure, no problem.
I thought that worked. Okay.
Validation issues.
Not quite ready for prime time, but
ready for preview.
So, we'll grab some related tables.
And by default,
we'll bring some of those fields in. If
we look, we can choose. We can say we
want to anonymize. We want to filter on
things. You can do different filters on
all sorts of stuff. So, for example, as
part of like the sales area where you're
creating initialization routines, uh we
might No, not what's this. Uh we might
want to filter on the uh blocked field
to say we don't want
Yep.
I guess we're not searching on that. Um
we can go ahead and say we want to
filter on a specific language code or
different currency codes, whatever have
you. Those filters will be applied. So,
we can say that this should be filtering
on blocked.
Single quotes. Uh validates the filters,
of course.
No problem. And now we're going to
filter the result set. So, now this gift
box package, if we want to generate just
that one,
um
we might have uh messed myself up with
creating that uh 76,000 line first.
Sure.
So, we'll grab those fields. We'll make
sure they're in here.
Great. Now we just generate that single
code unit.
Open it up.
And there we go.
It's that fast and easy. And now this
can potentially be part of my source
control.
So,
you know, I'm very much one of those
people of if I'm going to give you
presents, I'm going to explain how they
work. Uh so, I'm sure there are some
folks who are a little bit curious about
what's going on here. And again, the
code behind this is very simple.
Um we have some basic packaging where we
choose what tables are involved. We
choose what fields are involved and all
that sort of thing. And then, as messy
as this code is, it's also not very hard
to read. It's meant to be very simple to
read at first and foremost.
We're going to create a zip archive.
Which I hope most folks are familiar
with this uh utility library if you're a
developer in the room and someone's
asking you, I want to have three PDF
files downloaded at the same time. This
is how you do that. Um you create zip
archives and stuff things in it. So, in
our our zip archive, we're going to add
an entry. And what we're adding is a
created code unit.
And for each of these create code unit
calls, we add
some basic code unit header.
Those create functions. We create the
actual collection data and we create the
footer as a result of that.
The header is a very straightforward and
I kept it simple text builder so you
could read it looking through this and
go, "Ah, for my organization, I'm going
to make a fork off this project. I want
there to always be some extra stuff at
the beginning." Okay, fork it, add some
stuff here. It's super easy to adjust,
to modify, all that fun stuff.
The create functions will go through and
say, "Okay, well, we're going to create
something for each table name."
And again, we're just doing a pen line
and we're generating these little
procedure names.
And then we're passing in the parameters
of all the different fields that are
involved.
That's all.
Nothing too complicated, I would hope. I
hope most people are going, "Oh, yeah,
that that's straightforward. That I Why
didn't I think of that?"
I hope.
Um and then we're doing some basic
answer calls. And then finally, at the
very end, we're doing some routines
where we're creating the collection.
And so this routine
iterates through each of the tables and
based on the field settings, it creates
a detailed line and it says, "Okay,
there are some different filters here.
We'll apply those real quick." And
running through each of the records, we
want to
go ahead and say, "Let's grab the field
values."
And it depends a little bit on currently
a sort of if statement. I want to Next
up will be turning this into an
interface, so that way we can have a
wide array array of implementations
around what we want to replace the data
with. But for given code, text, date
time, all that sort of stuff, let's
append that. Because after all, in AL
code, you know that date formats have to
be written differently. GUIDs have to be
interpreted and evaluated, all that fun
stuff.
Uh if it's uh, not an if it is
anonymized, let's go ahead and run that
through some scrambler. Uh, the way that
this behaves in its default form, uh, if
we are running it through an
anonymization process for a whole bunch
of different packages,
uh, let's say for example, once again,
our sales area.
The way the anonymization works at the
moment, and will be the default
implementation, is we actually create a
whole bunch of noise.
You probably saw it as I scrolled past
it.
I love doing this.
And the reason I love doing this is you
get a free little code review of, "Did
anyone forget to set description to
100?"
You get to find out a real quick way of,
"Ah, I missed one."
Most of the time, I hope that your code
cops and your pipeline are already
warning you about these sort of things.
But again,
now, no hope.
Hope is not a baseline object to work
off of. So, we'll be fiddling with this.
We'll add some more anonymization
routines to it. Um, I was showing uh,
Freddy over break, there's a great
service for making mock data.
Um, and I would love for there there be
more methodologies for these different
mocks. So, this tool is something that
we are going to be releasing pretty
soon. Um, and hopefully, these create
some different scenarios for you to look
at, to work through. Uh, as mentioned,
the code data helpers that we were
looking at before, uh, sales demo
helper, uh, go live check listing, these
are public repositories.
I'm going to continuously uh, keep
improving them.
Uh, right now, each of them has three or
four
example implementations.
Uh, if you look at the source behind
this, you'll see that uh, they're
relatively organized into different
checklists that we might be working
with, uh, and implementations. So, if we
look at item, we have items blocked,
item positive adjustment.
Um so, there's some basic ones to get
started. I want to add lots of these.
And I'm hopeful that over the upcoming
year or so, more and more of you will
start seeing that there is value to
this, and you might throw some pull
requests in here. Go for it. Uh please
do. Um I'm going to continue to expand
this. I am working to do a second
edition of Your First 20 Hours. I am
going to expand this Go Live Checklist
thing to be a companion to that and
cover as many of those scenarios as I
possibly can.
And additionally, we have, of course,
the sales demo helper. Um there are lots
of different things. Sorry about that.
I'm trying to go too many tabs.
Brain too many tabs.
Um the sales demo helper is also just
public. So, you can go ahead and work
with this. I'm going to be expanding
this, improving it, rewriting it, adding
lots more things to it,
uh
as part of architecture design.
You'll notice at the moment these are
all just code units that are installing
themselves into records and then are
call uh called. Uh we're going to try to
change that up and make it be more
interface extension and that sort of
thing.
So,
hopefully, that's a bit of an apology
for creating the more work.
So, to recap some of the critical parts
of this,
what we're going for is think of about
all of the discrete parts of
testability. You're generating
baselines, you're validating processes,
you're
uh applying processes, you're validating
the process, and then you're rolling
back the results. How can you put those
togethers in new way new ways?
It's a little bit like LEGOs. Yeah, it's
a car kit, but that doesn't mean it has
to be a car.
So, think of some different ways that
you can play with that in your
organization.
What this does is it begins to involve
more of your teammates in helping you
build those test applications. Because
if a salesperson understands that I can
make better demos if I give you useful
information about how to show the
product at its best,
well, then it becomes a lot easier in
that product meeting in a month talking
about how can we help our customers
onboard.
You've already been having conversations
now with your salesperson about how do
we demonstrate the product in a good
way. You're already developing the
language, the habits, the integration
between the different teams to get those
different use cases.
And it understanding culture of
automation because one of the number one
things I hear about testability is
I can't get anyone to authorize this
because who's going to pay for it?
Or I hear all the time I don't have the
time to implement these sort of things.
Well, if these become part of the
deliverable package that you're creating
for AppSource,
it's a lot easier to sit with a product
manager and say, I need to spend time on
testability. I need to grow my abilities
with this toolkit. I need to develop
those strengths.
And it
empowers your uh partners and customers,
which is a fancy way of saying it
involves them and makes them understand
you guys are actually doing good work.
So, hopefully that makes a little bit
more ease when you're starting to say
uh Sorry. Uh
yep.
Link for the GitHub. Uh you guys saw
that.
Um
And then additionally,
um
yeah, I thought I actually had one more
slide, but it has disappeared on me. So,
I guess the question is uh are there
questions? I'm I'm between you guys and
beer. So, there's a little bit of
interest in keeping the
talk shorter for sure. And I saw the
first hand go up here.
Yeah.
You said you will
the app for your organization because
you want to add some things at the
start. Why are there any events used?
Let me come a little closer cuz I didn't
quite catch that.
I'm just wondering why you didn't use
any events and just subscribe to your
functions and then add your stuff
beforehand. So,
Absolutely. Because it's a first draft.
One of the things that I encourage a lot
of my developers of
you can't edit an empty page.
You can't make a great second version
until you've made a first version.
Your first 20 hours, I wrote that in 30
days.
It was less than a month from beginning
to end and it's about 500 pages.
And that is because I needed to get a
first edition to exist. I needed to find
out how does it help people? How does it
improve people? So, those right now are
proof of concepts.
They're inspirational pieces. They're
not something that I could sit with a
customer today and put this into their
environment and start using. Because
there's a lot of things that need to be
tailored to it. But they're you're
absolutely correct that they they need
more events. They need interfaces. They
need enums. They need some love. But
what I'm hoping is that between now and
next year's Tech Days,
there will be a significant number of
improvements to make there be a whole
bunch of stuff that you can just use it
right out of the box.
Because it's free,
it does get to go into the spare time
category, of which many of you know, we
all have copious spare time.
So, short throw.
Um have you have a chance to uh look
into generative AI to um generate this
data instead to have a
more rich experience with what kind of
fish, for example, I have. So, if I tell
the AI I need uh demo data for
for the fishing company and please pick
five fish and
generate it for me?
Ah, that is a fantastic question. Uh so,
if anyone didn't catch that, I'm just
making it clear for the recording and
everything. Uh the question was uh did I
think about potentially making use of AI
to help do some of these generation
pieces. So, for example, in our sales
demo helper, you know, we've got some
basic mechanics in here that say uh we
want to create something relatable data.
Uh well, what if your sales guy doesn't
know the relatable data?
Uh what if you are going to uh demo to
someone and you don't know what would
make sense? Or you would just like to be
efficient with your time and say, "Make
fishes for this." Um not at present, uh
but that's mostly just been the tempo of
AI.
Um I was discussing that with someone
upstairs. January 1, most of us have not
considered AI as part of our daily life.
That's a really intense tempo
for us to keep up with, for sure. Um
however, uh one of the areas where we do
see significant value uh from AI at the
moment, uh since we're talking
testability, my junior developers that I
hand testability scripts to and I hand a
first functional test to,
testability is extremely repeatable
code. It's very repetitious in that
you're trying many different
permutations. AI is phenomenal for
writing testable code. I had a junior
dev who over the course of a day might
write 10 tests from scratch based on the
scripts I handed him.
On one day, he went from 10 tests, I
gave him GitHub Copilot as a try this
for me. The second day, he wrote 100.
And they were all good.
Because there was already a baseline of
testable code. So, where I would love to
go is in some of these tools that
potentially we might want to create
relatable service items, we want to
create relatable items and stories and
data to support those narratives. I
think this is a phenomenal place to hook
up to Azure Open AI and say, I would
like you to populate a toolkit like this
for me with a whole bunch of
demonstration settings.
Run those tools against that setting.
And that would be fairly easy to
populate
by passing just functions as a
parameter. And then
Copilot could certainly help with that.
I think the Open AI ecosystem will be a
little bit better for generating those
story data than Copilot since Copilot
knows code. But I absolutely want to go
in that direction.
For those of you who haven't made AI
part of your life
as developers, little ways that helps. I
had a workshop earlier this week where I
needed create 15, 20 different
extensions to demonstrate
multi-application architecture.
Well, if you did that one by one with AL
Go,
I'd be there all morning. It takes a
while.
I'd be opening and closing workspaces
left, right, and center. So, I created a
little CSV that said, okay, for this
application name, for this prefix, for
this start object ID, end object ID. I I
that CSV file, went to chat GPT
equivalent. I'm not going to say which
one, but I went to a chat GPT equivalent
and I said, "I need a PowerShell that
reads a CSV file structured like this. I
need it to copy an app JSON, a
settings.json.
I need it to create the folders for me.
I need it to update those JSON files
with the values from the CSV. Go." It
gave me a PowerShell script within 5
minutes of me being done creating the
CSV. I then had a multi-application
framework of all these different apps
all set up
probably about 5-10 minutes later.
So, there are great opportunities,
whether it be testability stuff and
demonstration data and all those sort of
things or even just normal operation,
there are great opportunities to make
use of AI in that space. Um I
often will make comparisons of uh many
of you've seen different sci-fi movies
like Edge of Tomorrow and whatnot where
soldiers are wearing mechanized suits of
armor.
AI is like that. They're the mech suits
of armor right now. If you're a
moderately good or very good soldier,
you can do so much more because you're
so much faster, stronger, etc. But, if
you're a complete novice, you might do
faster, better, stronger or you might
end up at really high speeds upside down
in a ditch.
So, it's a little 50/50. You need to be
thoughtful if you're working with junior
developers about how they're embracing
it
because of that safety check. So, to
bring it all back to that question, I
absolutely think this would be a
wonderful opportunity to do AI level
demo data generation. So, I will be
looking at that
to be able to say, you know, some of
these different demonstration scenarios
that I have listed here,
I know what stuff needs to be populated.
I provide lots of defaults. It's just
missing a a bits of information.
Go ask for those few bits of
information.
I think that would be a super cool way
to do things.
Closer.
Thank you.
Um do your tools rely on specific
Chronos data, especially localized and
language related data?
Ah.
An excellent question. Um this comes up
an awful lot when it comes to
demonstration and testability.
Uh does this rely on localizations? Does
this rely on Chronos? Any of those sort
of fun things? Um the toolkits that I
have been showing today, the sales demo
helper, um the sales demo helper relies
on whatever settings are your in your
environment. Uh for example here, this
relied on whatever customers are
present.
It doesn't care how those are set up.
This is built against worldwide one. It
doesn't care what customers are present.
It just asks you as a user to select
them.
And it's going to use them. If your
database is blank, there won't be
anything present to select. So some of
these tools rely on a Chronos or an
existing set of data to work with.
Uh for the sales uh for the sales demo
helper. For the go-live checklist, um
the entire point of that one is that you
want to check the data that the customer
has. So this relies not on any of the
settings that come from Chronos or
worldwide one or any of the things. It
relies entirely on whatever data is
present at the time.
So that is a much easier sort of
infrastructure. Um it can rely on
anything. And then the baseline
generator, the the gift present here,
this is harvesting data from whatever is
present in the system. It does not care
about what localizations. It does not
care about what data is present. It
could be an empty database. You you
create a couple of settings in
does not matter.
Um because uh this question comes up a
lot in testability, when I'm creating
tests, should I build tests against a
blank database, or should I build tests
against Cronus?
Um and as my frequent co-host Camel has
talked about, if you build against
Cronus, now you're dealing with all
sorts of localization problems. You're
going to have to build tests for each of
the different regions that your Cronus
is operating in.
So, if you want to make it very region
safe solution to do demonstrations, to
do implementations, to do testability
using the generation toolkits, in a
perfect world
in a perfect world, you're building
against an empty database. And that's a
big part of why I wanted to make the
baseline generator is because building
against an empty database is a lot of
work. I've done it, it's not fun. Um I
don't know how many developers in the
room go, "Oh, good. I get to set up 250
GL accounts just so I can validate that
I can ship."
Uh that's not my favorite.
So, part of this is because I'm lazy.
One of the ways that you can be lazy is
by being more efficient. And any
opportunity I have to be more efficient
and I can give that efficiency to
everyone else
let's do that. And that's one of the
reasons that I really love making tools
like this that just help me do my job.
There's no IP involved in this. This
isn't a product. There's no way in the
world I could sell this as a product,
but it's a toolkit that allows me to do
to my job faster. And it's a toolkit
that I think will help other people do
their job faster. And those sort of
things, the more we can create open
source repositories like that on GitHub,
the more we can create that, and the
more we can convince our managers to let
us have the time to work on those tools,
the more we can get done. The more we
can help each other get done.
We We had a great question in my
workshop that ties into that question of
how do you estimate things?
Which is a challenging question. Lots of
people ask that. And I told them, well,
one of the things I do is I write down
discrete operations.
I'm making a setup table and a setup
page. That's a discrete operation. I'm
making a document. Okay, that's a header
line table. I'm making a list. I'm
making a card. I'm making a subpage. I'm
maybe making a couple of fact boxes.
That's a discrete operation. I write all
those down.
How long it takes me to do those things.
And now I know what my baseline is.
Well, when you're sitting down with your
product manager and you go, I found a
cool tool that 20% of my discrete
operations that take me 4-6 hours,
if I start using this tool, those 20% go
down to 1 hour,
you can do the math real easy. Over a
year, how much time do tools like this
save me? Oh, this would save me every
year 72 hours.
Well, isn't it worth giving me
16 hours for a couple days, maybe in a
couple weeks? Trick for you if you're
asking for things, if you ask beyond a
couple of weeks, it's beyond the 2-week
horizon, people are more likely to say
yes.
Uh, I would like a couple of days in 3
weeks. So that if I spend 16 hours, I
will be 72 hours a year less doing the
same work.
That's a fun thing to say. So, it
becomes much easier to go, ah, if I
spend a little bit of time, I can shave
off some time. I can make open source
tools or there's an open source tool
like the baseline generator that almost
does what we need.
If I can spend a day just adding a
couple things to it, it changes
everything we can do today in our
organization. We can make much cooler
apps on AppSource. We can make it easier
for our customers onboard. We can make a
diagnostic tool so that instead of me
spending 24 hours per quarter on
"Did you click this setting in setup?"
Instead of spending 24 hours per quarter
asking that question, I would like to
spend 4 hours in 3 weeks.
I would like to spend 4 hours in 3 weeks
making a little diagnostic app that just
checks, "Is this set?" And if it's not
set, goes, "Would you like that to be
set?"
You can make a lot of these noisy little
bad uses of your time start to shrink
down. So, hopefully, uh that was a very
yammering down the corridor uh answer to
your question of, "Does this rely on any
baseline?" But, uh no, it does not.
I think last round he had this, so I'll
ask here, here, and then let everyone go
to get beer.
Do we just use PC to generate data and
call the API, or is there a better way
to do it?
Um I will actually decline to answer
this question during this session
because there is a phenomenal answer to
that question in a session tomorrow. And
I would hate to go on record and be
recorded answering question Vieko and
Walder are about to take on.
Okay.
That feels like uh inviting some strong
heckling, and I'm just glad they're busy
prepping for tomorrow and not here to
sass me for it.
Um what's the the main use for the the
extraction of the data? Is it so you can
input it in your docker with the
automated testing specific for
a customer or
how is it used?
Ah, an excellent question. So, the
question, just to make absolutely sure
that was caught, is what is the main
purpose of the data extraction tool? Is
this meant for developers to work with
docker environments? Is it meant to be
used in pipelines? And the answer to
that is both.
Um, in a perfect world of development,
you're having a production environment,
you might have a sandbox environment
where the users are doing their testing
and acceptance, you might have
development environments where you're
doing the integration of all the
different changes that you're making,
but also hopefully you have your own
little private space that you're doing
your development work in.
Well, sometimes the change requests that
you're getting,
you can't develop that in a vacuum. You
know, uh, I gave the example earlier of
one of my customer's customization
relies on five years of ledger entry
history so that they can do
year-over-year comparisons and basic
trend graphing and all that sort of
thing. Well, testing that in a docker
without some sort of baseline
information would be near impossible.
So, by using a data extraction tool like
this and choosing to pull all of their
information out of that key ledger that
they're trying to bring information out
of,
uh, I'm able to then put that into a
code unit that it runs automatically on
install. Uh, the on install trigger
actually calls all of these data
generation code units. So, the minute I
hit, uh, publish on my test app to go
alongside that application that I'm
developing for them, it generates all
the test data and now I can either run
tests against that test data or I can
manually go into the product and do all
the different settings. I can see that
the visuals are coming up correctly,
that maybe the charts are displaying
correctly in my docker environment. And
then hopefully, if you've gotten to that
level of sophistication that you're
working with Dockers with all this
generated data on your local machine,
you hopefully also have pipelines that
because I have that scenario where I
need this complex pile of data to test
against. I would want to generate all
that data. Um and I talked to a few
folks uh in industry about that
including Microsoft folks uh here at the
conference and there was a lot of
excitement at the potential use of this
in pipelines. So, we might see some fun
collaboration stuff on this since it is
open source, people can do whatever they
want to help this along. Um
just as a again, caveat emptor, this is
a data extraction tool just like config
packages. Uh be thoughtful in how you're
using that. You are mass exporting data
and you are creating code units that are
checked into repositories. So, do be
careful with checking that you're not
exporting customer secret information,
you're not doing GDPR violations. One of
the to-do items before I even make this
live is to look at the field
classifications to anonymize the data uh
if it is set to GDPR flagged so that the
default behavior is always safe and you
have to go out of your way to choose
wrongly. Um but hopefully that answers
the good question of, you know, what is
your goal out of this? And the goal out
of this is you should be able to take a
customer environment and with a Docker
take an empty database, install this
initialization app, and now you have a
fully functional environment with all
your posting setups, you've got all your
ancillary supporting data, you've got
all your master data, and now you can
just transact.
And the important part for me on that,
I've written app after app over the past
year, 2 years that did that sort of
testing against an empty database. And
you spend a lot of time generating all
the underlying data.
That That's even with Copilot's help,
that's not a good use of my time. That's
not a good use of whether it's the
customer paying for it or me paying for
it. That time is being consumed. It's
not a good use. So, the hope was that we
should be able to do development the
right way against an empty database
without having to sit there.
Okay, create the gen posting setup.
Create the currency. Create the
location. All that stuff.
All right. Well, I think that would be a
good stopping point for today. We're
only a few minutes short, but this does
give you a head start that if you want
to make it downstairs into some lines
before all the other rooms, I gave you a
head start.
So, thank you everyone.
