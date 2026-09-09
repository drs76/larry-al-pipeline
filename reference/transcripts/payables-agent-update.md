# Transcript — What's new: Payables Agent update

- **Source:** https://youtu.be/Xc3ISQ7NAaQ
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[Music]
Hello and welcome to this update on the
payables agent. My name is Saurin. I'm a
product manager in the business central
team.
>> Hi, my name is Hos Antonio and I'm one
of the software engineers that have
worked on this payables agent update.
>> So accounts payables is the backbone of
quality financial data. What does that
mean? Well, it means that if you make a
mistake in your accounts payable when
you register vento invoices, you will
see that trickle up downstream and
become errors and it will impact your
financial statements, your P&L and all
kinds of other things and you'll spend a
lot of time cleaning that up. That's why
we have the payables agent to help you
streamline your accounts payable
processes. There's a lot of business
value in the payables agent. First of
all, it's an AI powered end-to-end
invoice processing. It covers the entire
process. That's the idea. You don't need
anything else to handle your vendor
invoice processing.
The key thing is that the agent empowers
your AP teams to provide quality
financial data to the organization so
you can trust your financial statements
and trust your P&L and so on.
We also think that the agent will be
able to improve the throughput of your
accounts payable teams because now the
agent does a lot of the heavy work for
your teams. No data entry and so on. And
it helps ensure that data is registered
correctly in your accounts payable.
And one of the important things is the
way that the agent works is it learns
over time. The more you use it, the
better it will become. The more it will
learn how you do things in your company.
So right now the payables agent is in
preview and we call it the first line of
defense against the poor quality data
and accounts payable. So the agent is in
preview in four countries United States,
United Kingdom, Australia and New
Zealand and it has a lot of great
functionality already that you can see
here on screen. One of the key things is
that there will be no more data entry
and the agent will interpret an invoice
and be able to present its reasoning of
why do we register an invoice in a
certain way to the user. It's all about
trust and transparency.
So let's just jump right into a demo.
Jose, do you mind showing us a demo of
the agent?
>> Yes, let's go for a demo. Here we are in
business central and the only thing that
we need to do to start working with a
payable agent is go to this hexagon and
on settings we have different uh
parameters. The agent works on a email.
I know that here I will have one
configure from my company that I will be
listening my invoices PDFs from it.
>> So you're saying Jose that we monitor
specific email address for incoming
invoices. So let's just clarify that. So
whether or not you expose that email
account, that email address to your
vendors so they can send invoices to
that account is up to you. You can also
use it in a scenario where you you you
don't expose that uh email account, but
your employees, your AP team will
forward invoices to this email account.
So that way you can minimize some of the
noise that comes in to this email
account. The one key things to know is
that you don't need to and you shouldn't
monitor this email account in Outlook as
well. The agent will take care of any uh
any PDF attachment that comes into this
uh to this email account.
>> Yeah, exactly. Once we can we enable the
agent, it will be monitoring any new
incoming email that you will have uh
received on that account. Like for
example, this demo invoice that we're
sending to the target account with a PDF
that we'll be analyzing.
There is no need to actively monitor
what the payable agent is doing. It will
be picked up on its own time and it will
be showing on this side panel here on
the right as a new task.
Now the the agent is done we will get a
notification both in BC and also on the
side panel that there is a task for
review. Here we will be able to see that
uh the content of the email and also
view the PDF that we will be analyzing.
It all looks good to me. So when I go
for the review, here is the draft
information that was uh suggested. For
example, we found different lines that
they basically align to what we
expected. We found some proposals for
deferrals. Uh all of this content has
been AI generated. So a human needs to
review as there can be errors. It all
looks good to me. So I will just confirm
and the agent will take the last steps
to create a final purchase invoice.
However, this is a basic scenario. Let's
move forward a couple of months and look
at what a company could be actually uh
doing part of their uh accountant job.
Let's say that we jump into uh weekly
rotations and then on Monday morning
it's time to review a new list of tasks.
So now let's look at this other company
that had the agent running for a while.
We will see that there is multiple tasks
that there were already addressed and
let's assume that a new content comes by
on Monday. There is a bunch of work
items for them to look at. First we will
look at this one. There is some review.
There is some information draft ready.
Same as before. Everything looks fine.
Uh I can view the PDF itself to get an
idea of what exactly is it that I'm
dealing with. Okay. So I'm working with
Fabrican. Okay. I know that there is a
bunch of uh information that we have
already set up like item references. So
I just want to double check that the
information here looks according to what
I expect. Everything looks good. Same as
before. We can confirm and move forward.
No pain, no almost no time required for
my part into reviewing this invoice.
Let's look into another scenario. Uh on
this one I can see that the agent didn't
actually find a vendor originally. So it
suggests me to create a new one. I
already accepted to move forward. And at
this point I will just review what is
the information that is populated into
this agent. This is on this right side.
We will have the information extracted
from the invoice and the fields were
populated. It all looks good for me. And
when we speak about uh creating vendors,
so when the agent uh is asked by the
user, instructed by the user to create a
new vendor, it's important to know that
that the blocked field on the vendor
will be set to all. And that's because
we want to respect any due diligence or
processes you have for approving a
vendor. Uh you need to maybe check the
vendor's bank account and onboard the
vendor in various ways. So the agent is
not able to process with the invoice
until you unblock the vendor. That's
important to know.
>> Exactly. So if even if we confirm here
that the content is valid, the agent
will not overwrite existing behavior on
Business Central. Uh there are many more
scenarios that we could cover, but I
think this is a good enough uh
experience. Just go and try out the
payable agents for yourself. Going back
to you, Sorin,
>> that's great. Thank you for a great
demo, Jose. Now you started by showing
us a little bit of the setup experience.
Could you add a few more words to what
does it mean to set up the agent?
>> Yeah, actually there is not much setup
uh required. The idea was that the agent
will be a one uh oneclick stop for
configuration. So out of the box, the
agents will work with your system
business central. However, for those of
you that are interested in tweaking some
of the parameters, like for example, the
reviewing that initial email, you can
skip that step for the agent to analyze
directly the PDF and come down for a
human in the loop moment uh down the
line when it's more necessary. Uh there
is also other configurations for the
algorithms that we use for suggesting
what each line uh should be matched to
but uh we will explain more those in the
documentation.
That's really cool. So I can basically
get started with the agent in very very
little time. There's nothing I need to
set up basically nothing I need to map
to my existing items or accounts and
things of that nature. Very very cool.
Thank you Jose. So let's talk about
customer feedback for a second. So when
when we build AI features, it's crucial
that we get customer feedback as early
in the process as possible. So the
payables agent as we saw is in preview
right now. And one of the key piece of
feedback that we got for through the
preview was that a customer said, well,
they want to they want the payables
agent to be able to increase the invoice
throughput and they also want the agent
to be able to improve the accuracy of
their vendor invoice processing because
they had errors in the process today.
And they want to make sure that controls
and compliance is easy. And that's
exactly that's actually spot on what we
intend the agent to help you with.
Speaking of feedback,
we can argue that in the past software
was done when it met a certain set of
fixed requirements. But with AI, there's
a change in this perspective because AI
improves as it's being used. It kind of
depends on real world real world use. So
in that sense you could say that
software with AI is sort of co-created
with customers and we really want you to
try out the agent use it will become
better it will learn from from from your
use from the historic uh invoices that
you have. So key message from here is
start using the agent so you can get
familiar with it and provide us with the
feedback both the feedback that the
system will will give by itself that we
will learn from but also feedback in
terms of what is missing what do you
think the agent should be able to
handle. What we're doing next and coming
up in this wave is we want to make the
agent available to as many customers as
possible. That means worldwide
availability what we call general
availability of the agent. There might
still be some language and geographical
restrictions even if we go general
availability but stand by for more
information on that. But we want the
agent to be uh available to any of you
out there as soon as possible. At the
same time, we want to expand the
functional capabilities of the agent. We
want to improve the matching of vendors.
As we saw before the scenario where we
didn't recognize the vendor, we want to
get better at that. We also want to
handle one of those crucial uh processes
which is matching with purchase orders
in the system. Whether those purchase
orders are from actual products or with
services and things you buy on G
accounts, for example, we want to be
able to do both sort of two-way and
three-way matching of of purchase
orders.
Let's talk about what we want the agent
to become a bit more long-term. So the
vision of the agent is that it's all you
need to handle your vendor invoice
processing from start to finish.
Basically we want to transform back
office and accounts payables with AI.
And one of these things is we want to be
able to source any invoice whether it's
an electronic invoice like the e
invoices we have a lot of here in Europe
or it's a PDF as you just saw in this
example in the in the demo. We want to
help with identifying fraudulent
invoices in different anti-fraud
scenarios. We want the as I said before
we want this to be an end toend invoice
processing with purge order matching
approvals posting what have you
according to how comfortable you are
with dialing up the autonomy level.
End of the day accounts payable team
should be able to provide quality data
to the organization and the payables
agent will help with that.
And that also means that by streamlining
the entire operations, these account
payable teams will be able to spend time
on other things that may be creating
more value in the organization.
As we saw before, this is a turnkey
solution. No setup required. This is a
non-implementation. You point andclick
and activate and that's basically it.
A key thing here is this is all about
trust and transparency. You saw some of
the configuration options that allowed
you to dial up the autonomy level by
skipping the uh the uh review of the
email. We'll probably add more of these
configurations over time so that the
agent is supervised by subject matter
experts, but can be unattended where you
so desire.
As I also mentioned, we want to do a
three-way matching and of course also
two-way matching if you have non
products. And this is a crucial thing.
It should be as easy as you saw Jose do
before when you review that draft to
see, oh, it's matched with my purchase
orders. Maybe there's a price
discrepancy or and something like that.
It should be easily handled by the
agent.
And then a key thing which you didn't
see here because we haven't gotten to
that part yet. What we saw now was that
the invoice the the draft becomes a
purchase invoice document and now at the
current state of the agent you take it
from there do whatever approval process
and whatever you want to do before
posting the invoice but we also want to
handle approvals basically we want you
to be able to approve an invoice from
from anywhere that's the goal
and we might also go as far as to say
once it's done once the invoice has been
approved and it's been through the
proper process
Maybe you decide to post it. Maybe the
agent can post it for you if you so
choose. And maybe the agent could go as
far as to create the optimal payment
suggestion. Let's see. But these are
part of the thoughts of where we want to
take the agent. So with that, we want to
thank you for watching this update of
the payables agent. For more information
about anything Business Central, if
there's one link you should take away
from this slide is the ak.ms/bcall.
You probably know many of the rest of
these links, but note them down anyway.
And of course, follow our LinkedIn page
and make sure to follow all of the new
content that we post there and learn
from the from a great community out
there of Business Central professionals.
Thank you for watching. Thank you for
watching.