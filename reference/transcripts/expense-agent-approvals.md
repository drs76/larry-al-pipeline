# Transcript — Introducing: Approvals for the Expense Agent

- **Source:** https://youtu.be/qZALauRY_So
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[music]
>> Welcome. My name is Blazej Kotelko. I
work as a program manager at Microsoft.
And my name is Enrico Csimitan and I'm a
senior software engineer working also in
Business Central and with Blazej on this
great new feature which is approvals for
the expense agent.
Exactly. And today in this session we'll
be talking about approvals in the
expense agent.
You hopefully have seen already
introduction to expense agent by our
colleagues Alexander and Monika. If you
haven't seen that session yet, please
stop watching this recording and switch
to the introduction first.
That session gives you great overview
over the
expense agent all up. In this particular
recording we'll we'll focus on the
approvals which is part of course of the
expense agent process.
When we started working on approvals for
for the expense agent, we had two
important things in our mind. First is
that users of the expense agent are
quite often outside of Business Central.
They will be working on mobile devices.
They will be using
email to send receipts and communicate
with the agent in different way even
through copilot chat.
So they don't have they don't they they
are not in Business Central and they are
also sometimes don't even have a
Business Central license. So we we'll
talk about that later. And the second is
that the whole project has been done in
model model first or AI first approach
where AI is helping us
guide the user and and execute the the
business process and that also includes
approvals. And the other thing is I
I need to mention we also wanted to
refresh the user interface provide with
a my nicer and and more modern approach
to how approvals will look in this in
this whole
system of of expense agent.
So as you can see on screen here we have
a very simple
process for for approval
presented on screen. But I have a little
bit more like animated slides so let's
go through that and then you will show
that in a demo that that Enrico will
will show you in a moment. So when you
are starting with expense agent, you are
sourcing your receipt in different ways
through as I said email and so on.
And those are processed by the agent.
They are extracted, itemized, and so on
and so forth. And then there is a
process of of pre-approval with where
the AI model is already
making some decision decisions or
suggestions as as to whether a given
receipt is
follows the policy or not.
When that report is ready for submit for
the submission,
the user of course will be able to go
and edit and and maybe tweak the report
a little bit
and send it to to approve. And that all
can be happening outside of Business
Central and and we have sessions talking
about that in detail.
When that expense report is sent to
approval, the approver will receive a
notification through
email or copilot chat and the
approval can happen. And of course the
approval the approval can be also
rejected or the report can be rejected
in some cases that makes sense
where some data is is missing.
The report needs to go back to the
submitter
to provide some additional
clarification.
And then of course at the end the
approval will be registered of course in
Business Central. Everything that we do
here might be happening outside of
Business Central but the fact of the
approval is of course registered in
Business Central and all the financial
consequences
that need to happen for the expense
approval
posting and so on so forth
are happening in Business Central.
So the best way to show that is in a
demo.
Enrico, take it away. Thank you.
Yes. So now we switched to my screen and
we are seeing the expense agent
dashboard also called web app.
I am logged in with my user and I have
already uploaded earlier today some
expense expenses that the AI has
processed and added some expense
reports. As you saw in the previous
videos, these are all saved in Business
Central of course.
But I'm just going to go ahead and
review that everything looks fine and
the AI has
done already
the
right things.
So I'm going to
submit this one. It looks good.
And this is now going to be processed by
AI and set in a pending approval state
and going to be sent to my approver.
And I'm going to have a look at the
second one as well. This also looks
fine. So I'm going to submit this one as
well.
So now you see that my
reports are now submitted so they appear
in my submitted tab. I can go ahead and
have a look at the details but I cannot
edit them anymore because of course now
they are pending
the approval from Blazej.
So now I'm going to put on my Blazej hat
and become Blazej for a few seconds and
I'm going to switch to the view that
Blazej will have in the web application.
So now I switched to my
my
view with Blazej as a user as you can
see from the header here.
And Blazej might be a submitter himself
of expenses. So as you can see he has
some expenses that he is going to submit
to his approver.
But most importantly Blazej is my
approver. So you can see that there is a
tab here called for my approval. This
did not show up earlier because I cannot
approve for anyone. But Blazej can. So
the moment he goes here, he can see a
list of expense reports that have been
submitted by persons he can approve for.
So in this case you see the one down
here is the one that I just submitted
from the previous view. And Blazej can
just go in and have a look at the
expense
or like multiple expenses potentially
that are added to the expense report,
check that everything looks fine.
And in this case Blazej is just going to
say that he approves because of course
he trusts me and he also sees that
everything looks compliant to the
policies.
So the previous expense is now approved
in the system and this is also of course
synced with the state in Business
Central. So Business Central also will
know that this is in a approval state.
But
Blazej also will review the second
expense that I have submitted a few
minutes ago.
And Blazej can see that this also looks
compliant from the AI point of view. AI
checked potentially the policies that I
have added to my system. But in this
case let's say that Blazej
knows that I've done more expenses in my
trip
in this Kontos Hotel hotel. For example
I've had a breakfast or I've had meals.
And Blazej wants everything in one
expense report. So Blazej can just send
back the report and basically you can
say reject or send back and say
"Please include all expenses for the
trip
in the same report."
And the moment Blazej sends this back,
this is also going to be saved in
Business Central, processed, and then
sent back to me and I can then review
Blazej's comment and act on it and
basically
um
make it
make it compliant again and make things
work again.
So
now that I'm done with my approval and
my send back as Blazej, I also want to
mention how this is set up in practice.
So I wanted to show as little Business
Central UI as possible because
technically as submitter or as an
approver
using the expense agent, you don't
really need to go into Business Central.
But you do need to have some setup that
your admin needs to set up for you in
the Business Central UI.
So I will switch to Business Central
now.
And we have a new page which I have
pinned just to make it more accessible
for me which is the expense users page.
And here you can see that the users of
the system need to be
defined as expense users. But also more
importantly
our expense users have a can approve
flag which needs to be turned on for
them to be able to be set as approvers.
I have to make a small note here. The UI
is not fully final so we might tweak a
few things around. But the idea behind
it is that basically a person can be
marked as approver as Blazej is.
And as you can see Blazej can approve
for me and for Jim.
And let's take for example another user
which is Robin.
As you can see Robin is not an approver.
So in the case of Robin, we don't really
see like people he can approve for. But
the moment I set Robin as an approver,
then I can of course decide who he can
approve for.
I also want to mention that we support
also approver through setting up teams.
So you can actually set up your teams
expense teams in the system. In my case
I don't have that. But in that case you
can have a more
structured approval approach where
basically your team manager can approve
for the team that that they manage.
All right. Thank you very much Enrico.
Amazing demo.
As you have seen you you have full
control over your expenses and the
approval system outside of Business
Central and that is also why this this
slide might be quite important. Because
we don't require users of the expense
agent, users who are submitting
expenses, submitting reports
to actually have a Business Central
license.
You can just do it outside of Business
Central and everything will be billed
using our standard agent billing system.
So it all follows the same
agent billing billing system that you
know from sales order agent or payables
agent.
For approvals though, that is slightly
different story because when you are
approving the report, there is some
there are some financial
consequences in Business Central data,
and that includes also posting data to
GL reports and so on. And for that
reason,
uh users who are approving expense
reports, even if they are doing that
from outside of Business Central, just
just as you have seen in the demo, they
are required to have a Business Central
license.
Uh so, that's a very simple but
important uh story here, important
slide.
Please have a look at other sessions in
the in the series when we are talking
about the expense agent. As I mentioned,
the introduction to the expense agent by
Alexander and Monica is probably the
most important session for you to
understand
the end-to-end scenario and the whole
story about our expense agent. And then
we have separate sessions uh talking
about different aspects of the of this
project, including the one that you just
uh have seen. Of course, please look at
all the normal resources we have for
partners and customers. Follow us on
uh YouTube and LinkedIn. And if you are
a partner,
uh get in touch on Viva Engage. All
right. Thank you very much. That was it
from this session.
Thank you, and enjoy Expense Agent.