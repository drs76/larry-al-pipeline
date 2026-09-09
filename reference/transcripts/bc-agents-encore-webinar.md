# Transcript — Getting Started with AI Agents in Dynamics 365 Business Central

- **Source:** https://www.youtube.com/watch?v=6OQyl6iVNTA
- **Channel:** Encore Business Solutions (Microsoft Partner) — webinar, 41:06
- **Speakers:** Aaron (overview/slides), Brennan (live demos)
- **Ingested:** 2026-07-06 (creator captions, cleaned)
- **Distilled into:** `reference/AL-REFERENCE.md` §28 (AI Agents in Business Central)

---

And indeed, good morning, everyone. eh Let's
get right into what we're going to be showing
today.  So  Agenda is pretty succinct and direct.
It's all about agents and all about agents
within Business Central today. So we'll do a
very, very quick  overview of what's available
in general in Business Central from an agent's
perspective.  And then we'll get into some
of the specifics about the pre-built agents,
specific to the payables and the sales order
agent. And then finally,  some uh very recent
releases from uh Microsoft, we will dig into
the agent designer. So this isn't a general
AI discussion. This is very, very specifically
an agentic discussion related to Business Central.
hopefully everyone is coming to this uh session
understanding  in  general terms,  the rough
difference between uh Copilot, overall AI
and what agents do. I'll do a really, really
quick recap on sort of how we would define
an agent. But it in effect is a component of
artificial intelligence that operates and processes
a very, very specific business process. So you
could almost give it a role within the org
chart. It would be just a very, very distinct
and confined role to the specific business
processes. that it is trying to  optimize  or
enhance. Within Business Central, we've got
two different ways that  we deliver agents to
customers at the end of the day.  One is the
pre-built agents that we just mentioned, the
sales order agent and the payables agent.
And by the way, Microsoft is coming out with
more agents  that will be pre-built for the
general public to use.  And then the other side
of that is, of course, the build your own agent.
In the past, you were always able to build your
own agent, but you had to do so in Copilot
Studio or  the  much more,  I would say, uh
development heavy applications that lived outside
of Business Central. So the concept of bringing
that agent build or agent designer inside of
Business Central is uh rather compelling, but
we'll save that for a little bit later in the
presentation. So specifically the agents within
Business Central,  Sales Order Agent and Payables
Agent, we'll dig into these  in a couple of
minutes in a relatively decent amount of uh
detail, but largely that Sales Order Agent is
there to communicate directly with those customers,
try to interpret or understand what the customer
is asking for,  and then send back quotes to
customers as well as create sales orders within
Business Central. On the Payables Agent side,
it effectively is receiving invoices that are
emailed to it from ah vendors. uh It captures
by reading that invoice, the information on
screen, and then it registers those invoices
within Business Central  for ah ultimately posting
uh into the subledger. So let's dig in in a
little bit of detail. Specifically, we'll start
with the payables agent. So when they started
kind of looking at what problems they could
they could  solve with  agentic uh AI,  the
payables challenges kind of came up more uh
than oh other business processes. So they started
with  wanting to solve problems like uh time
consumption in and around entering invoices,
uh incorrect data being,  not maliciously obviously,
but just re-entry of information always has
a risk of being incorrectly entered. uh The
compliance or the predictability with which
invoices get entered into the system so that
the process is always compliant.  And then
of course, the impact of any of those not being
correct has uh ultimately an impact on  financial
data, which  the rest of the business often
uses to make important business decisions.
And so we see the payables agent really trying
to solve some of those problems  in regards
to  very consistently and quickly correcting
or correctly entering  those invoices,  as
well as uh being date sensitive so that  you
can do your payables aging in the most appropriate
way,  being compliant with all of the rules
that the organization has set up in terms of
of how invoices are collected and processed
within the system.  And then even being able
to properly take an invoice and match that with
any pre-existing purchase orders to ensure
that uh inventory and predicted inventory are
all lined up to reality. So how it works, like
I said, Brennan will kind of walk through this
in a little bit of a live demonstration.
Some uh OCR capabilities, optical character
recognition capabilities, in order to read
the invoice and it will create a draft document
in Business Central uh using  what it's read
and matching to data that's in Business Central.
uh either match with a vendor or create a vendor,
if that's  how you want it to operate. We have
some recommendations on that front that we'll
get to.  And then it really only processes the
information within the role that  it's been
given. So it will have its own permissions and
its own profile. And anything that  is outside
of that  would uh effectively initiate an interaction
with uh a human kind of result. It will process
and uh error check itself in order to  make
sure that the invoice is entered correctly.
And once it's done all of that work, it brings
an individual  into the loop in order to validate
the information that it has  entered. Or it
will maybe even ask a question of the human
if it doesn't know how to process something.
After that is uh ultimately reviewed, uh we
basically would send that to  a posted vendor
invoice.  And I think at that point, Brennan,
I've probably talked enough. I think you can
take it away  and show everybody how this payables
agent works, which by the way, I think um I
was only released  fairly recently over the
last month or so. So it's been previewed for
a while. Generally available over the last
30 days, for sure. Okay, let me share my screen.
Thank you, Aran. Hello, everyone. Okay. Okay,
so...  I'm going to trigger this Payables agent,
the one that I have in my demo environment.
uh And I'll mention, there's a couple of ways
you can do this.  So I have a dedicated email
address for my Payables agent. I can use,  we
can use it internally. So your finance department
can send invoices to be processed. So that would
be an internal use, or you can send it to select
vendors for them to send directly their invoices.
the agent for both.  I'm doing this internally,
let's say,  and it's  an invoice for yearly
licenses. So we're going go ahead and we're
going send this out. It's going to take a couple
of minutes, but there's a few things I can
talk about before we actually receive it. Here's
the different agents I have in my demo environment.
If I hover over the payables agent, right away
it's showing the KPI. So some of what Aaron
was talking about, it's actually determining
how much time I saved by using the payables
agents to actually process, in this case, three
invoices, I only had it on for a little while,
received seven emails and saved time on emails
by 21 minutes. You don't even have to monitor
these emails for the payables agent. Now, what
I do want to do is just quickly show and reiterate
what Aran was talking about in terms of some
of the light setup. for the agent and I'll
use the example of the payables agent but this
goes across all agents in Business Central.
You set them up essentially the same as you
set up a user. You set them up with as Aran
had mentioned,  its own profile or UI that it
has access to uh and a set of permissions so
that it only has access to do what it needs
to do for its work and it doesn't have access
to anything beyond uh what's available to them.
based on these permissions. And then of course,
the user access. So you'd want maybe for a payable
agent to have two or three people in your finance
department to have access, maybe dedicate one
of them to configure the system, which is very
light configuration. And even when we look at
the tasks that it does over time, everything's
right down to the consumption of copilot credits,
which Sharon might talk about later on. It's
very  specific for the Payables agent. You always
know  what the consumption is. So just clicked
on it. It's really pretty straightforward. It's
uh 50 copilot credits per document processed
plus another five copilot credit credits per
month. And a copilot credit  is one cent US
this time. Okay, let's kind of go back and.
I'm in as  actually an AP Administrator, Royal
Centre, and I have the payables agent details
here. I'm going show one here. There's a couple
that were processed.  Let's just show this one
here as an example.  I'll open this up a little
bit. We'll go and we'll specifically look at
it. This is the document that the agent processed,
received it by email. And you can see  worldwide
importers or wide world importers, sorry.
You can see the invoice number 246, the due
date, document date. This is the document that
was processed by the agent  with all of that
detail, perfectly processed, wide world importers.
uh And here's the two lines that I want to focus
on.  So if you see here, The two lines in the
invoice that was sent to the agent is SGH001
and PGH001. These are vendor  item references.
Now the system recognized that, payables agent,
uh singled them out. These are the item reference
numbers against our item number in Business
Central. Just to validate, whenever you see
these little i icons,  This is the suggestion
that the Payables agent in this case has uh proposed.
And just to validate, we'll go ahead and click
on it and sure enough, um the referenced SGH001
is GRH in our system. Same with the PGH, it's
GRH in our system and you can see that in the
second line as well. So really straightforward,
everything's matched up but you always validate.
We can scroll across, just make sure that the
quantities,  prices, the totals match up, and
they do. So this one was processed. That's one
example. Let's go back. And if you  look at
my payables agent icon, you can see here that
there's one that I have to pay attention to,
and that's the one that we just emailed to the
system. So I'm going to click on it. And this
is that human in the loop pane that you'll see
across all agents. And what this is telling
me is that I have something that I need to pay
attention to, and it's to review the one that
we just sent. So I'm going click on that. We're
going to review it. uh so just so you can see
here, this is the  PDF that I'd sent it. You
recall yearly license fees. There's a quantity
of six. Graphic Design Institute.  Again, if
we looked at the numbers,  the actual invoice
numbers, everything kind of matches up here,
including of course the vendor. And so of note,
this info suggestion, what the system has said
is, okay, we think that we should be posting
against the jail account 68210. So I want to
validate that. If I click on this, sure enough,
it's for license fees. It's exactly what we
want to.  post this against. If it made a mistake
or guessed wrong and you make the correction,
finalize the draft, it will remember the next
time what you decided upon  for that. So it
learns as you go. And all we have to do is
uh click continue if I'm happy with this, I'm
happy. ah It's gone ahead, processed that document
uh in the system to be later uh actually posted
and paid  off. So that's all that I wanted
to show on the Paybles agent, Aaron, and I hope
that I showed that it'll actually go in and
process the invoice details, classifies the
lines against that, and significantly allows
your existing finance team to scale with an
increasing headcount if there's increase in
activity.
Excellent. Thanks, Brennan.
me a second, I'll get the PowerPoint back on.
All right, let's shift gears and get into the
sales order agent now. So we saw it from a
payable side of things. Let's look at a sales
side. This one is a little bit more complex.
And so think it's got some new elements of AI
that'll be interesting to you as you kind of
walk through. The use case for this one specifically
is trying to resolve a few different things
when it comes to organizations that have a high
volume of sales order entry. Ultimately, that
high volume is  time consuming to  reenter invoices
or enter  orders based on uh customer  requests.
Obviously, you're doing a lot of that data entry,
just like you had on the Payables agent.  Anytime
you're reentering information, there's a chance
that uh you could make an error. So it's trying
to eliminate  those.  will also,  over and above
what Payables agent does, uh it  is an agent
that the customer interacts with using natural
language. So there is some back and forth that
we see this agent taking care of  in terms of
communication with the customer to confirm
and validate the information or the order that
they're ultimately asking for us to then deliver.
ah The agent will even engage with uh more complex
functionality within Business Central  like
uh capable and available to promise so that
we're setting the right expectation with the
customers, again, without having to involve
a human in the middle of that. And so a lot
of what we see in terms of benefit out of the
agents is that ability to take the workload
out of that sales order entry team so that it
is entered automatically. We eliminate all
errors that go into the data entry. We also
take care of the basic level of interactions
with the customer from the perspective of clarification.
We take all that work away from the individual.
And it's not just one email that creates a sales
order. There's a fair bit of back and forth
that the agent can conduct on your behalf with
that customer in order to kind of hone in the
right order.
At that point, kind of see how it  ultimately
takes this information and then processes it.
So ultimately receives an email typically from
a customer, which is just going to be in natural
language. It's not like uh an official document
coming in.  It's request. There's still  the
checking and security checks in and around
the validity of that email.  It will do some
initial checking for things like inventory levels,
Are we transacting in the right unit of measure?
Have we got the right attributes and variants
assigned for what the customer is ultimately
looking for?
We can trigger this agent just at any time.
So basically it triggers upon the receipt of
an email. They'll then go through that interaction
with the customer, ultimately resulting in
the creation of Typically, I think it starts
with a quote with specific pricing that's related
to that specific customer. So not blindly creating
stock  sales orders and quotes. It is actually
entering and coming up with a pricing that's
specific to the customer  that it is interacting
with. Just like the payables agent, it has a
predefined role with predefined permissions
that it's not allowed to go outside the boundaries
of.  One quick note is, and I think I mentioned
it later,  those permissions are also  limited
by the user that is the user internally that
is interacting with that agent as well. So there's
kind of multiple layers of permissions and
security on top of uh these agents. It will
draft and write emails  to send back to customers.
uh Depending on your configuration, it can bring
the individual, the human,  into the fold in
order to validate what it is coming up with
in terms of what it's sending back to customers,
both from a language perspective as well as
an accuracy perspective on the sales order
or the quote. And then it would ultimately convert
that quote into an order upon customer confirming
that the order is good to go. So, Brendan, I'll
send back to you to walk everybody through
this process here. All right.
Good here. Okay, perfect. Okay, so I'm hover
over my sales order agent icon.  Right off
the bat, you'll notice it's paused. You have
full control, you turn them on and off when
you want to, when there's peak periods, for
example. And so I paused this one, but even
so, it's showing me again, KPIs,  very specific
to sales.  it will determine when it receives
emails whether or not they are sales related
and then whether or not to act on that. So
that's kind of the, this is, you know, I've
created one order and one quotes through the
sales order agents with a few in the loop, but
it's even summing up the amount of order dollar
billing that it's done so far. So. I think what
I want to do is  kind of show a little bit
of what Aran was talking about with the setup
of this, because there's a few more options
here, not many, but there's a few more options
versus the Payables agent. Certainly there's
a shared email box that you can  assign it if
you will.  Manage user access,  just like with
the Payables agent, you can have multiple account
managers or sales people or sales managers
that... uh get to monitor  and not keep in the
loop task pane, if you will.  But here's some
interesting uh setups. As Aran mentioned, you
can set up uh how it responds to your existing
registered customers or in Business Central
in the system, whether it's all the emails
or a few,  or there's some other advanced options
there as well, and whether or not to even uh
respond to unregistered. senders, if you will.
And then Aran had mentioned, I think a cable
to promise,  you can select whether or not it
only provides quotes for in stock available
items, or in stock available items that may
be  not in stock, I'm sorry, now, but they
will be in a week because there's a purchase
coming in in a few days.  And then on the
level of autonomy, you can have it fully automate
the sales quote generation to these um customers
and prospects financially. um And the same on
the sales order side. And of course, depending
on your use case, you'll want to kind of monitor
this and see.  But for example, rather than
always validating against the quotes and the
orders,  you could autonomously let the sales
order agents respond and provide quotes. and
then validates that the orders are done properly
before they're sent out to the customer. And
then finally, you can limit, in terms of spam,
daily limit of 100 emails or whatever you want
to put in here.  It will analyze PDFs of purchase
orders, for example, or images, and you can
kind of personalize the email signature of
your sales order agent. So let's go and show
an example of this. So I'm just going to go
in here.  as uh one of my customers, Peter.
And so what Peter did, he's with the datum.
He's asked for a quote in the body of the email,
but it could have been a purchase order PDF
attached. I'd like a quote for five Athens desks
and 20 Berlin chairs. In the system, we're
an office furniture distributor. And so  with
or without validation, in this case I did validate.
but  with the click of a button, the reply with
a sales quote was, uh thank you for your interest.
Please find below a summary and it's created
that summary.  I didn't do anything here. The
sales order agent did all this uh in terms of
the content of the email, including a discount.
So I'll show you where that discount came from.
And what I think is kind of neat,  there's
a nice soft close here asking,  whether or not
to convert this to an order. Let me And if
you can see this, it's kind of small, but a
data corporation, when they purchase five or
more Athens desks, they get a 10 % discount.
So Business Central, it's set up in the system
and the order agent included this in the quote.
So I validated all this, it looks perfect.
And in fact, the customer replied and said,
yes, it looks good. I confirmed the order.
please send this to our main address on file.
Now in Business Central, there's three or four
different addresses that the datum has. So again,
I validated with one click that the order was
correct in terms of the order confirmation.
But my sales order agent replied, thank you
for confirmation, order's been processed and
will be shipped to your main address on file.
So it actually confirmed that. And that ends
the process of that. So essentially, you can
almost completely autonomize this, but it significantly
automates the quote and order intake process.
Drafts orders for rapid approval, one click
if you want to do that, which I suggest that
you would.  But a huge increase in, I'll say,
quote capacity and revenue lift with your existing
team, especially during peak periods when you
want to turn this on or
Excellent. switch back to PowerPoint. We'll
get to the last little bit  of  our presentation
today, which is, in my opinion, the most exciting
part of it. So the agent designer. So the payables
agent and sales order agent are, I think, uh
great agents to be able to use.  I  lost my
internet connection there, apologies. uh We're
seeing that the agent designer, think, is really
an interesting uh addition to the  agentic uh
offering from Microsoft. you're, well, the
sales or agent and the payables agent are great.
uh But let's go through the uh agent designer
sort of process and the feedback that we can
kind of give you in and around how you would
create your own agent. So the first thing  that
you would do  is ultimately when you're creating
a new agent, you  assign a profile to that agent.
We talked about that a little bit earlier in
that it's predefined. but we want to get up
into Business Central and we want to give it
effectively some security permission. Remembering
though that the individual that this agent
will be attached to  will ultimately also adopt
any permissions  that that user has as well.
so, but it's good, best practice ultimately
to give your agent its own specific um permissions
as well. ah When you're creating effectively
the instructions,  you can use natural language
to describe what it is you want your agent to
ultimately do. The  advice that Microsoft has
on this is  do so as concisely as possible
and continue to refine and refine and refine
that language  as you kind of go through the
process of building that agent.  So you can
always go back and update your instructions,
which is really the key to how it all works.
That's the natural language instruction. It
also recommends that when you build those instructions,
you use a hierarchy, like almost like indented
bullets, in order to make sure that the agent
has sort of a step-by-step instruction list.
It also recommends that you prompt your agent
with a role that it plays in the business so
that it knows how to act.  you describe your
agent in the instructions  as, know,  a  whatever
it may be. uh But it's basically a description
of the job that it's ultimately doing. uh Your
prompt that you're writing  ultimately is really
a subset of a larger Microsoft prompt that is
governing things like, you  know, compliance,
but you're not doing anything illegal.  It's
also uh protecting you from things like security
threats, prompt insertion attacks that could
be trying to take over your agent to do something.
So you've got your portion of  the build, ah
which is then supplemented behind the scenes
with what Microsoft is doing. uh Those instructions
that you write in ah the instructions for the
agent that then get converted to a list of tasks
and steps for the agent that you're allowed
to then step through, when you process or test
out your agent. Those  tasks and steps can
be then specifically  modified and refined in
order to uh fine tune how the agent ultimately
works. But if you were to ask  Microsoft or
us,  what is most important? The most important
is to get the instructions right. The tasks
and steps are really more for fine tuning what
you want that agent to do.  As you kind of walk
through examples that you feed your agent,
can  tweak those tasks and steps. ah And then
as you also walk through step by step, you
can see how Microsoft is consuming or your agent
is consuming credits. So Brendan mentioned
earlier, one credit equals roughly one US cent.
You can kind of see the cost of your agent
that is accumulating as it processes  a single
case. And so...  What you can do is you can
get more efficient in your instructions as well
as your steps in order to kind of minimize
those copilot credits that you are using or
that the system will use when it goes live.
ah It will also uh monitor with memory  the
actions that were performed or the agent performed
on a uh case-by-case basis as well as the searches
that it executed.  And then the interaction
tools that you've got available to you to engage
with  individuals outside of the agent, so
real humans in your business or outside of,
are user intervention uh interaction, which
is,  need the user to uh help me finish this
process, user review, which is, course, I've
done this, please make sure that it is okay,
and then the response action, which is  effectively
communication  with typically an outside party,
so creation of an email or a chat or whatever
it may be. And then finally, we would recommend
that as you train this agent, as you are also
testing it. So when it creates a document, whether
that's a sales order or a quote or a purchase
order, a requisition or an inventory update
or whatnot, it will denote, as Brendan showed,
I think in the Payables agent demo, with a little
eye and a circle around it, that that data
very specifically was created by  the agent.
And so you can hover over it. So it'll give
you the rationale for why it created what it
created.  But if you give that either the thumbs
up or the thumbs down, it doesn't have a lot
of feelings yet.  And so  it's rather important
to give it that positive reinforcement or tell
it that it is incorrect because that will then,
that feedback will then make its way into the
next iteration of that process. the more you
give it feedback,  the better the next process
ultimately is. um The last thing  I'll just
note is  that link at the very bottom of the
screen  is  to the Microsoft Learn site and
it's very actively being updated mostly in and
around the most important part of this entire
process if you're building your own agent, which
is getting these instructions correct. So I
would encourage you if you want to experiment
with creating your own agent, that uh you take
a look  at that link.  And before I lose connection
again, we better pass over to you, uh Brennan.
Apologies for that. All right. You only cut
out a little bit there.  Okay, very exciting.
We've got nine and a half minutes. That's just
enough time, I think. So let's see what we
can get to. Okay, so create or design your own
agent. Really exciting. For 10 days, might
have mentioned Aaron. I've got a couple of examples.
There's a template example that Microsoft has
shipped the agent designer with, and it's a
sales validation. So we're gonna look at this.
right away actually so that I can kind of walk
through a lot of what  Aran had already  spoken
about. We've shown some of this, including the
setting up a profile, managing permissions.
But in this case,  similar to Co-Pilot Studio,
if you're familiar with that, which has a few
more tools and tweaking of different LLMs that
you can kind of run,  there's specific instructions
that you  assign, set up. for your agent. And
you can see here, this is similar to what Aaron
was talking about in terms of how you set up
those instructions in natural language. And
if I kind of scroll down a little bit more here,
it's actually showing, you kind of select a
task, this is the last task and it's showing
in this case, 12 steps that it went through.
This sales validation, um agent when you put
an input  of a shipment date in it, maybe I'll
show that, um which I did this, you know, I've
got an old work date in my system, but  I said,
okay, process  reserved, it's going to take
these items that are ready to ship, that are
reserved and in stock and release those sales
orders  to the warehouse. on this date. So
this is what it did is it actually went and
managed that and then sent me a review of exactly
what it did. I only put one system in the one
order in the system for it to be able to release,
but that's what it did. So very specific. The
instructions, if we go back quickly to this
and I show you an example because we've got
a few minutes here. This is a little bit about
what Aaron was talking about. It's step by step.
What did the agent decide? What the agent saw,
just code, the tools the agent had access to.
I Aaron had mentioned some of those tools as
well. And even what was memorized so that it
could do its job, its task. So really quite
detailed. And as... Aaron had mentioned with
those instructions, you can go back  iteratively
to previous  history of instructions, tweak
it, go ahead send it again. The whole idea
is this is helping you create a group of concepts.
Okay. I'll show you an example ah that I created
to do a little testing.  It's a project assistant.
And what this  project assistant  is doing
by clicking on the input, and this is a timeline.
I'll go through this step by step. I've got
time. The input that I had to provide this,
it's going to go and create a project with
phases and tasks in Business Central based on
the previous history for this customer and
how we've set up projects before and the description
that I give. as well as a start date and then
the project manager should be. So the message
that I gave it, the input was to create a project
for the School of Fine Art to remodel their
number three board. Start date should be September
1st. Choose a project manager that makes sense.
So we'll go through step by step so I can show
you exactly the reasoning behind this agent.
There's those info suggestions.  Remodel number
three boardroom,  school of fine arts, that.
ah What's really of interest though is the
next step it actually created, if I scroll down,
uh phases and tasks against those phases. So
WBS for this project uh in business central
and it's giving you reasoning behind each of
those phases. It's taking into account  previous
projects  for the School of Fine Art. What
I found interesting was uh this particular task,
A-B-I-T installation,  that wasn't in a previous
project. So the agent just decided that might
be a good task to add, which I would agree.
But the whole idea is you validate the instance.
And then the next step was we set up the agents
to provide a summary, project number, it's now
in Business Central. at the start dates, the
project manager and the WBS they created. That's
one example around project services. It's all
very operational. I have another example that
I'll show here. We've got two minutes left.
I'm in a different demo environment here, but
I created this one here. It's a Consume Materials
distributor. I'll go through steps with this
one as well. The input for this was in this
example, when we have a sales order set up with
make to order finished goods that we send to
the shop floor. The shop floor, when they're
finished consuming and  creating those finished
goods, they send us a total list of, I'll say,
effort  and actual um raw materials that are
consumed. And so this is what happened. If I
show you the attachment... Our shop floor had
a total consumption of both effort as well as
bill materials that included  different units
of materials. But of course, the finished goods,
they all use the same one. So  in the instructions,
I uh provided them with a specific allocation
against these specific finished goods.  Just
to give you an idea, I'll quickly show sales
orders referring to. Um. which is 1092, there's
two different lines here, two different products,
a full panel and a half panel. And these are
make to order in this example, there is no bill
of materials, there's no assembly bar associated.
My agent's going to create that for me with
my validation. And so if we go to the next
step here, it created a wall panel, bill of
materials. assembly bomb with the resources
and the items, the bill of materials for the
full panel.  It did it for the half panel as
well.  And  it also gave me a summary of exactly
what it's consuming in each of those lines,
if you almost finished goods.  And  I decide
whether to go back, tweak those bills of materials
against those lines.  If I click continue, it
just finishes that and associates these bill
of materials with that sales order. So really
that's uh all that I was going to show. think
we've got a minute and half left, but I hope
what these examples show is even on operational,
not just back office, we can  really uh automate
full workflows uh with a human in the loop
to validate, make sure that we're happy with
the way things are going. And that would significantly
add and boost productivity with your existing
team of FTEs so they can add more value where
it makes sense.
Great examples, Brennan. So hopefully we've
given you guys some great ideas in and around
how you can use agents within your business.