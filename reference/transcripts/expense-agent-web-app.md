# Transcript — Introducing: Web App for Expense Agent

- **Source:** https://youtu.be/q-udoJPGUKE
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

Welcome to Business Central launch
edition 2026 release wave one.
And welcome to introduction to our new
web app for expense agents. My name is
Alexander Totovic. I'm product manager
and I have my colleague with me today.
Yeah, so hello. My name is Michael Swink
and I'm a developer and architect in
Business Central.
Okay, let's see what is about and why we
have web app because for years
we learned that we are using Business
Central as a user experience and now I
think for the first time we are moving
outside of that. So now we have a web
app exclusively for expense agents.
So what will happen? You are not
Business Central user but still need to
submit expenses. This is very often a
scenario. So you have thousands of of
your customer thousands of your
employees and they are not all of them
Business Central users but they still
have expenses.
So
not everything should be done via chat,
email. So yes, we will have M265
co-pilot chat, email but sometimes you
need to see what you have and how to
submit. So this is necessary. Need for
transparency control, uh exception
handling, more details, easier to update
when you see what you need to uh to
submit and how to uh submit. So even
after submission there is approval
process. So it can just go straight
forward. So this is a native environment
for expenses. In the future this is
native environment.
So it doesn't mean you cannot use in
Business Central but this is first
uh native environment for expense
management.
So who the web app is for? Employees.
They can create, review, fix, or submit
their expenses
and expense reports. And for finance and
approvers, they can oversight expense
reports
uh once when they are submitted. Uh they
can make correction, approval. Sometimes
they just need to make some corrections
related to specific uh rules but on the
end as I said for approvals.
How it should go?
You need to submit physical receipt. So
idea is you will have physical receipt.
This physical receipt
will be probably scanned. You can get
another way. You can get PDFs or
whatever. You can take any type of
physical receipt.
Uh review extracted expenses. What does
it mean? One when you upload this
physical receipt into your uh web app
this is an automatically extracted
expenses. Then
you will fix all AI detected issues if
some of them exist.
Track expense status, manage exceptions,
all of them and if you're okay, if
you're if you're satisfied with all
these details, you just submit uh this
expense. It it will continue its own
life cycle. Submit for approval and on
the end it will be approved as expense
report. You could see shortly how it
works uh on these slides but definitely
demo will speak much better than any
word. So Michael, please show us how it
works in the practice. Yeah, thank you
Alexander.
So here I have just signed in to the new
web app for expense agent uh and and I
just signed in with my micro Microsoft
intro account.
All that had to happen before was that I
was registered this user was registered
as an employee in Business Central and
furthermore this has been allowed to use
the as an expense user to use the
expense agent.
Okay, as you can see there's not much
going on. It's clean and simple.
The main thing is really to get an
actual receipt that you have gotten
either in PDF or an image into the
expense agent.
So let me just uh choose one receipt I
have here.
As you can see it's now kind of been
uploaded. It will be uploaded to the
expense agent and the expense agent will
now use AI to extract the relevant
information from the receipt
and categorize it. Uh and furthermore if
it passes all the initial kind of test
for actual getting into Business Central
we will also create uh and add it to a
kind of default expense report. Um so
you actually don't need to go and create
an expense report later. The the the
expense uh being passed here will simply
be added to an expense report as you can
see has happened here.
I can go and open up this one. As you
can see it's in a hotel bill. We have
extracted that information.
If we expand uh to just briefly look at
it because it's kind of a simple
traditional expense
uh uh receipt from a hotel stay.
Uh and what has happened here is that
all the relevant numbers, dates, etc.
has been extracted and put in here.
It has been uh
categorized as a hotel bill. And
furthermore we have done all the
itemizations of all the different lines
and [snorts] kind of put them into
subcategories for for each of the lines.
Which you often will have to or will be
a requirement especially for stuff like
hotel bills.
Um and if I want to correct anything,
let's say the AI is not didn't get 100%
correct or it's just I want to actually
add a for instance a note that this was
a
customer meeting
uh
meeting.
I can just do that and and save it.
Um so so so that just means it's very
easily directed to go and do this and I
could do all of this kind of manually
but of course you really want the AI to
give you as much help.
But let me just add a few more
uh expenses. So let's say I take
for instance these ones. You can you can
drop a whole folder or copy paste a
folder and all these kind of easy ways
to get things in here.
Um the general idea is that here we will
show all the expense reports.
You can kind of see up here what state
they're in. Currently we only have draft
ones.
Uh and
uh the processing of course takes a
little while. It is an AI driven thing
but you can see quickly we start having
information on the different ones.
For instance we could take a look at
this particular one.
This is an interesting one. It's a
handwritten taxi receipt.
Um
which you know maybe traditional OCR
technology would have a problem with but
since this is all AI driven it actually
works really well.
Uh you can see we extracted all the the
correct information from it here and
again it's been categorized into ground
transport in this case.
Um
and
we can also see here there was actually
one that kind of was raised a small kind
of issue with.
So we can open that up and see
uh what it is. So here you kind of get a
summary of kind of okay there's
something details missing.
I can look through this. I can of course
expand it to to again see what it's
about. Okay, it's an itinerary for
travel.
Uh and we'll just look through here and
okay. So okay, actually this is a case
where
uh the location was not kind of
correctly uh couldn't be identified for
some reason.
Um but here I could for instance just go
and say okay, it's UK all and then you
can press save and continue.
So what will happen there is that the AI
will run again. The whole workflow
underneath will run again and eventually
it will be added to an expense report.
One thing you can also notice here is
that all the numbers we are showing is
in the UK currency even though most of
these receipts are foreign
uh and in different currencies. So we
kind of have automatic currency
management
and conversion here going on as well.
Um
and also I mean you can see the grouping
um still something in progress. It's
somewhat of a simple grouping.
If for instance you are sure uh that a
certain receipt will have to go to a
certain receipt to a certain expense
report
you can basically go here and add it or
you can also drop it drag and drop it
onto it, right? So I can take for
instance this DK
uh taxi receipt I have and also add that
and it will show now
uh the AI wouldn't try to group it. It
will just always go to this group.
When I'm all happy with a certain
receipt expense report and I'm happy
with all the data in it
I can basically go and submit it for
approval.
And uh
it will now go in here and you know the
approver will get notified and can go in
and look at all the same details also in
the web app
and and and go through that flow.
So uh yeah, that was the current web app
we are building here. I'm really looking
forward to see how you will receive this
and use this and uh
back to you, Alexander.
Thank you, Michael. So you could see
that this is a great new web app and we
will continue to invest into these
directions to make this much more smooth
whatever you uh
we can look into this direction. So this
is a future of expense agent.
Now before we close this session I would
like to invite you to watch another
session related to expense agent because
expense agent is uh big investment from
Microsoft side in this release. So we
have introduction expense agent this
session web app to expense agent and D65
chat with expense agent approvals to
expense agent and expense management. So
all of these sessions are connected. So
please watch all of these sessions
together to get a full knowledge about
this new investment.
Okay, uh we are on the edge uh we are on
the end of our session. So you can use
all of these links to find interesting
information.
Of course, subscribe on LinkedIn or go
to YouTube to find all these interesting
and inspiring videos.
So thank you for watching us and we
really hope you will start using this
agent as soon as possible because this
is a great opportunity to improve your
regular job process.