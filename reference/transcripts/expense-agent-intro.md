# Transcript — Introducing: Expense Agent in Business Central

- **Source:** https://youtu.be/egE6UdOfar0
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[music]
>> Welcome to Business Central Launch
Edition 2026 release wave one and
welcome to our introduction to the
expense agent session. My name is
Alexander Totovic and I am principal
product manager and I have my colleague
today with me.
Hello and welcome everyone. My name is
Monica Ahuja and I'm a principal
software engineer in Business Central
team in Copenhagen and I'm very excited
to present the session introduction to
the expense agent.
Thank you, Monica.
Now, let's see why we started and how we
started with expense agent at all.
Our first goal is to fill a
long-standing product gap with
AI-powered solution. What does it mean?
We didn't have expense agent for the
early beginning, so in all our products,
in all our versions, we didn't have
expense expense management.
So, we wanted to add new feature, but
not only a new feature because new
feature just adding few tables is not a
future. So, we wanted to make a really
AI-powered solution. And this is
AI-powered solution. So, it can be used
outside of agent, but this is primarily
created to be used with the agent. And
if you want to get the full capabilities
of this powerful solution, you should
use as a agent.
So, basic concept is to automate
receipts to get extraction,
categorization, itemization, and
approvals automatically. Then, reduce
manual effort and accelerate
reimbursement process. This is probably
one of the most important because this
is on the end of this process, but we
want to accelerate this process, so it
will be just very simple process to
reimburse our employees. And of course,
on the end to ensure all these
compliance with internal policies, tax
regulations, so many other
enforced
rules we have and we need to follow.
So, what is the expense agent?
This is AI-driven assistant.
As I said in the introduction for
collecting, extracting, categorization,
itemization of all type of expenses. And
even more, you will see through demos
what does it mean more because we didn't
want to put everything in one row. So,
it can handle compliance rules and
policies. It can manage even expense
report creation, review, and submission.
So, this is something what will happen
in the background. Agent will lead you
to make not only to create expense, but
to create expense report automatically
based on your behavior. Provides new
dedicated approval mechanism, so we have
new approval process and enable
financial auditing within a Business
Central app. So, it can be used in a
Business Central, but primary place for
using is outside of BC.
So,
um when you look into
core capabilities, there are a lot of
things.
So,
first, you could see what was our first
idea and yes, to go to this idea, it
cannot be done done overnight. So, Rome
didn't build overnight and not in one
day, so we had to plan. So,
in this case, we made some
>> [sighs]
>> even maybe too optimistic ideas to build
so much in public preview because this
is just in few months, we created all of
these things. So, you will see
everything what is marked really clear
color, this is something what we will
have in our public preview. So, you can
scan all your receipts, you can forward
them to different channels, web app,
email,
you can chat with entry 65 co-pilot
chat. You can
review, extract
all your details automatically,
categorize out automatically, then we
can switch to itemization,
reconciliation. It will be itemized in
the case of per diem, system will
automatically calculate per diem and
based on your location. So, all of these
things are already planned for public
preview. So, we will continue to expense
report creation in this moment based on
specific period, but it will be
again, it will be we will continue to
invest into this direction to make as
more automation as possible. So,
everything what we see this is possible
to be done automatically with AI, this
is subject of our investment. And as I
said, we will have approving process,
reimbursement, and posting process on
the end. So, this is what we have
right now in the public preview. As I
said, some of these features are in our
agent, some of these features are in the
Business Central.
But now you can see what is planned
more.
So, for public preview and for 2026
wave release wave two,
plus, so
do not take a wrong my assumptions that
this is not everything what will come
very soon. We will continue to work on
that. So, probably much more things all
these stars you can see around and this
is something what we are planning to do
sooner.
So, from next release and after that,
but all these things should be
delivered before GA.
So,
it was about functionalities we are
covering with the and what what we are
covering in public preview and what will
come next, but now Monica will switch
and try to explain all these details
about architecture. Thanks, Alexander.
Yes,
so the concept that we wanted to adopt
for expense agent is that expense
users that will be interested in filing
expenses
do not have to be Business Central
licensed users and they should not be
disrupted in their flow of work for
filing expenses. So, we want expense
agent to be available where the users
already are. So, we are going to target
as many apps and channels as client
where expense agent from Business
Central can be used and you can see some
of the initial clients that we have
here. We have the Microsoft 365 co-pilot
chat, we have the shared mailbox, and we
also have a brand new web app which is a
modern web app designed specifically for
expense management task for users that
are not Business Central users. And
through all these clients, then the
communication will happen to Business
Central via this new expense agent
service that we have introduced. And
this expense agent will be responsible
for basically all the AI-related actions
that needs to be done in the expense
management process. And then at the end
via APIs, the data will be logged into
the expense app module inside Business
Central.
So, that's the overall architecture we
have, but let's see the demo now.
Let's imagine I did a business travel
recently and I would like to file
expenses for it. So, here I am in my
Outlook app and I could just send email
to this shared mailbox configured by the
administrator of my organization.
And let me just go ahead and attach the
files that I would like to expense.
So,
let's attach the copy of the hotel.
And I would actually also like to
do this invoice that I have gotten
as a hard copy
for my ground transportation. So, let me
just click this
and attach it to the email. I can keep
the original size.
And then I'll go ahead and click send.
And now you can imagine that I go ahead
and take some coffee and wait for the
expense agent to do the work.
And after some time, after my coffee is
finished, I come back and sit on my desk
and use the Outlook in desktop version.
And then I see that an email has arrived
from the expense agent that it has
processed the receipts that we sent. And
let's see what has been done. So, I can
see that a report has been created. The
total amount for both the receipts is
has been extracted. The time period has
been extracted and it's also saying that
all the all the receipts are within the
policies and it's compliant. So, I can
just go ahead and review the report and
then submit if needed.
So, let me just go ahead and click this.
So, when I click the review button on
the email sent by the agent, I'll ended
up in this fresh new web app dedicated
for the expense management experience
for non-Business Central users.
And I can see that the report that has
been created with the two receipts. Let
me just expand this and see if all the
data within the receipts is also
correct. And if I want, I could go ahead
and see
the details
of the data that is extracted
automatically by the agent. The merchant
name sounds right, amount, date,
everything looks good. It has not only
extracted the data, but also decided the
right category based on the receipt and
its context. And my organization needs
itemization for the hotel receipts, so
it also went ahead and did the
itemization based on the lines and the
totals are good. Everything looks good,
so I can just go ahead and submit and
that's it.
The expense is now submitted. And this
was about the users that are not
Business Central users, but if you are a
Business Central users and you are
interested in how the expense finance is
working inside Business Central, then
these reports are actually logged inside
the expense module in Business Central.
Let me show you how. So, as a Business
Central user, I can just go and start
with tell me search for expense reports.
And now there is a list for all the
filed expenses and you can see that
there is the expense data logged for the
same expenses that we filed via email.
So, that's the demo for
end-to-end flow. Let me just show you
what you really saw.
Whenever a user uploads a receipt, be it
via email, be it via web app, then the
expense agent does all the heavy lifting
of processing, extracting, categorizing,
itemizing, grouping the expenses into
the reports, and at the end, it calls
the Business Central API to load the
data in Business Central.
So, let's see how we can now enable this
agent inside Business Central.
To enable the agent inside Business
Central, all we have to do is go in the
tell me and find expense agent, and then
you can configure the email for expense
agent to be used, or you can and you can
also use the initial setup data that we
have that will give you the list of
categories,
posting groups, and so on,
and adjust the parameters according to
the need of your organization. Then,
make sure you import and select the
right expense users that should be
having access to the expense agent, and
voila, we have activated the expense
agent. So, that's how easy it is.
So, thank you, Monica. Thanks, Todor.
Let's go slowly to finish our session,
but before we finish,
I just wanted to show you something
because
through all these demos, you could maybe
find some rules, some policies exist.
You could see that in one moment,
expense reports were compliant against
rules, and so on. So, I just wanted to
explain what we have right now, what are
rules, and what policy is.
So, in this moment, we have implemented
rules. In this moment, we have
implemented what rules are. This is
about straightforward information about
amounts. So, amount can be maximum. For
example, you are not allowed to spend
more than 1,000 euros, or you can spend
more, but you need to provide
justification. Very simplified models.
This is about amounts, about mostly
about money, maximum minimum amounts,
daily rates, fixed amounts, so on. It's
required absolutely accuracy, so we
cannot say this is enough to have 99%
accuracy. They are strict rules and must
be 100% accurate all the time. So, this
setup is actually in a table in a
Business Central. On the other side, we
want to provide great experience, a
really full policy experience. What does
it mean? This is about approval process.
So, expected behavior related to a
language basic conditions.
Example, when you are allowed to travel
in the business class. This is not about
amount you will pay. This is allowed in
these conditions, you can use business
class or premium economy. In other
conditions, you can use
economy class. Or when you are allowed
to book hotels more than four stars. If
you are allowed to use alcohol on a
business
lounge, or if you have moral event, you
are allowed to use alcohol, but you
cannot order Dom Perignon or similar
exclusive alcohol
drinks. So, this is about something we
can explain by word, and this is
actually full knowledge, and this is
what will come on the end. Full approval
process where system can say that you
are compliant with the rules and with
the policies. So, in this moment, we
have these two options, rules already
implemented, policy in a process of
implementation.
And
Monica mentioned few times,
you do not need to be Business Central
user, and so on. And it opened the doors
about how anybody can use Business
Central if if this person is not
Business Central user.
And it was not possible earlier. It will
not be possible in the future as well,
but this is not about specific user. We
mentioned we want to be on a place where
expense actually happen. So, if person
is a truck driver, they do not have
enough time to go to Business Central.
They
This person is not Business Central.
This is not native Business Central user
because this person just need to submit
its own expense. So, what we decided, if
you are using agent, but this is only if
you are using expense agent, you are not
required to have Business Central
license.
You will be charged based on copilot
credits.
So, this is only this situation. It
doesn't mean you cannot use Business
Central. You can use it Business
Central, but in this case, you must have
minimum team member license. And with
team member [clears throat] license, you
can be in a situation to cover managing
expenses, submitting reports, so all
regular processes, so almost everything
is
related to team member. But yes, team
member is even if you want to approve
expense report. You can do it through
web app, you don't need to switch to
Business Central. You can choose where
you will do, but you must
have team member license in this moment
because you are active user in the
Business Central regardless from where
you are doing that. And if you want to
post expense report and post payments to
finish all these processes, this is
natural that you must have Business
Central essential or premium license
depends what you have inside. So, this
is for posting and for posting for any
of other solutions in the system.
So,
now we are at the end, and what I want
to say,
please watch all these sessions because
expense agent
Yes.
Okay, I'm switching from.
And at the end, what I want to send as a
message, as expense agent is a huge
investment from our side. This is a big,
really big investment, and we do not
want to cover everything in one session,
no way. You can see even this one
session strictly related specific topic
is big. We have much more sessions, so
please watch all of them. You have
introduction expense agent what you just
had a chance to watch. Then, you have
web app in
expense agent, and this is if I copilot
chat and space agent approval to expense
agent because we have new approval model
for expense agent, and on the end,
expense management purely Business
Central experience.
And now we can close. Please use some of
these things to get more knowledge, to
find interesting information. Of course,
you can subscribe directly to LinkedIn
to get all these the freshest
information directly from Microsoft, or
watch YouTube videos as well.
So, now on the end, I can say only thank
you for watching this session, and in
the future, in advance, thank you for
using expense agent because we are
really sure this is a great new
functionality in Business Central. And
thank you, Monica, for working together
with me today.
Thank you so much.