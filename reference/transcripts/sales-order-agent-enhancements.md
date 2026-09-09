# Transcript — What's new: Sales Order Agent enhancements

- **Source:** https://youtu.be/4nFViDASGhg
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[Music]
Hello everyone and welcome to the
session about what's new in the sales
order agent. My name is Kasim Mikram and
I'm a senior software engineer working
in the development of sales order agent.
>> And my name is Dimmitri and I'm here to
help Kazim to demonstrate some of these
cool capabilities that we added to this
story.
Over the last several months, we've been
doing a research with all of you trying
to understand what else can we add to
the sales agent story and capabilities
to make it much more useful for all of
you. And you see this list of fantastic
improvements and changes to the sales
order agent capabilities which are now
available based specifically on your
feedback. So these are the features that
we Kazim and I going to introduce in the
next few minutes and hopefully get you
excited and get you to use this sales
order agent to ease your daily life.
Thanks Ditri. So now let's look at some
of these features in action. So right
now I'm inside business central uh and I
have the role center open up and on the
top right corner you can already see the
sales order agent is already configured
is and activated and we have one
notification that requires our
attention. So let's see what it is.
So it looks like uh a new incoming uh
email from our customer uh at DATM
corporation. And if you look at the
email itself, it's basically a request
for a sales code within the email body,
they are referencing to the attachment
for the details of item that they would
like to purchase along with the other
information that they would like it to
be delivered in 2 weeks and the shipping
address that it needs to be shipped. If
I go further down, we can see all the
attachments with this email as well. And
while we are reviewing this email, the
agent has already reviewed each and
every attachment to identify which of
the document is relevant, which of the
document is not relevant and which are
the documents which are not supported.
Over here you can see we have the
privacy and terms and condition
documents which are valid formats that
the agent supports but there's no
relevant content inside these. So the
agent will ignore these files when uh
processing this request. And lastly, we
have a purchase order attached with the
email which is categorized as reviewed,
meaning it has some relevant
information. If I open the purchase
order, I can see a purchase order that
was received by our customer at the ATM
corporation. And within this purchase
order, you can see a lot of items that
they uh are willing to buy uh which
contains a lot of uh office furniture.
they are uh asking for tables, chairs,
stool, lamps, desk and a lot of uh
different office furniture in different
quantities.
So the agent has categorized this as a
valid uh document and it will be
processed in combination with the email
itself. So everything looks good uh
within this email and the attachment. So
let's confirm this request.
And now the agent will be processing the
email along with the attachment only the
relevant documents that were attached to
the email.
After analyzing the customer request the
uh there is a user intervention on check
item availability and when we and we can
see one of the items tool in quantity 4
is not currently available. So let's go
into this step and try to investigate
further.
This open ups the item availability
page. This page can be used to see if
any of the items are available uh for a
particular customer. And we have bunch
of filters that you can apply to see if
a particular item is available or not
for a particular customer. So how I
would pro probably use this page is to
first apply the filter on the customer
itself. This will basically set all the
required filters
specific to this customer. For example,
it could be the location uh that this
customer is uh based. So the when the
item availability is calculated, all the
filters are considered. So as we saw
from the message, they were looking for
force tools and as we know these tools
are currently not available. But as a
business owner, we know we have some
alternate items that could be used in
place of stools.
So I know those items are called chairs
inside my uh system. And the two closest
items are the Munich chair and the
Berlin chair. As I can see the Munich
chair is currently out of stock. So this
is not something I can replace the stool
with. So what else I can do? There's
also this Berlin chair which is also
very similar to the stool that the
customer is asking for. So I will try to
use this as an alternate item in place
of these stool. So how I can do that? So
I will go down to the bottom. You can
see I already have a predefined
suggestion which says I have made this
item available or I can give some custom
instructions. So this is again a new
feature that we have added where you can
basically specify a custom instruction
to the agent. So you can guide if a
agent is stuck or it needs your help. So
what I will do over here is give this
extra instruction which says use Berlin
chair instead of stools and I press
confirm.
Now the agent is proceeding uh with this
custom instruction and let's see what
the agent will end up doing.
Now the agent has basically processed
the request created a sales code and it
requires our attention for the outgoing
email. Before going to the outgoing uh
message itself, I would like to open the
sales code itself.
And you can see the requested delivery
date that was specified inside the email
body was considered and added to the
document itself. The alternate shipping
address was correctly identified by the
agent and set inside the uh document
itself and it made all the changes to
the lines itself. You can see the
document was a bit extensive with seven
lines and as we can see the Berlin chair
is there in place of stool with the
right quantity.
So everything looks as expected. So now
I will go and review the outgoing
messages.
Over here we can see the attachment
itself. The email is very well
structured with all the summary of the
sales code itself. And if I go to the
bottom and there's one interesting thing
that you will notice there is this
custom signature. This again is a new
feature that we have introduced which
allow
uh the end users to specify a custom
signature. So that will be used whenever
an email is generated by the agent. So
you can use any custom signature based
on your business communication.
So everything looks perfect and I will
confirm this uh outgoing message.
Uh before going further I would like to
show how exactly you can set this custom
signature. So I will go to the agent
setting itself and I will go to the very
last card over here. You can see we have
this nice option where you can specify a
custom signature and I can click on edit
signature and it will pop up this rich
text editor. Over here you can either
copy paste your existing signature that
you already use for your business
communication or you can use this rich
text editor to design the signature
within the product itself. You can of
course add all the links uh the images
as well. There is a limit of some
characters but in most cases all the
signatures will be able to fit inside
this rich text editor. If I go back you
will now see there are even more
configuration that you can choose from.
One is to analyze the attachment. So we
have given you the option to choose if
you want to analyze any attachments that
are coming with uh the email. The
formats that we currently support is the
PDF and the images.
And you can also set the limit how many
emails that needs to be processed per
day. Right now the default is 100. Any
more emails will be processed the
following day.
So that's how uh the attachments and the
custom signature looks like. I hope you
find these feature useful. That
concludes our first demo. Back to you
Dimmitri. Fantastic capabilities. Thank
you very much Kasim. Um the yeah
recognition of uh document attachments
is is one of the top requests that we
heard from you. But let me go and show
you a few extra capabilities that we
added to the sales order agent. And I
will also start from the setup page and
navigate to the second part of it of
this experience. One of the asks that we
heard from you is that we with some time
as we learn to trust the sales or the
agent, we wanted to become much more
autonomous. And here you can see some of
the settings which help the agent to
become more autonomous. Assume you're
working with two types of category two
two categories of customers. Some of
these are registered senders, the
customers and contacts which are
registered in your business central
environment or unregistered senders. So
somebody out there who send an email
with a request to you but they're
currently not specified and not found in
your uh business central uh environment.
Now you can set up the agent to
um to either review the messages or
proceed with processing these messages
automatically for both categories of
these senders. So let me open up this
configuration and show you that there
are three levels that you can choose
from. U so you can either keep reviewing
every single email message that comes
from your registered senders. That's the
default safest option. You can also
change the setting to review only the
first message in the conversation,
meaning that every followup on that same
thread will be processed automatically
by the agent. Or you can choose to to
trust the the agent to pick up the
message from your register customer and
start generating the response fully
automatically without you having to
review that input. So our general
recommendation would be for you to maybe
use this second or third option for your
registered senders, the customers that
you work with the most and keep it to
review all for all of your unregistered
senders because you do want to get a
better control of of these types of
messages are they relevant or irrelevant
for your business. Another option which
I wanted to show you here is the new
capability that we added to the agent
based on your feedback as well. ability
to include items uh which we are capable
to promise. This is one of the existing
business central capabilities that many
businesses rely on when they serve the
quotes to their customers. Quite often
it may happen that the items that the
customers request are not necessarily
available on the date which they request
these items on. However, the business
central engine the the capable to
promise feature can calculate when we
are capable to ship these items to the
customers. So now this feature is also
made known to the agent and the agent
will use it in action. So let's see how
it works. Now when I reconfigure this
experience, I will update the
configuration. The agent configuration
now has changed and I will wait
patiently for the new email to arrive
from one of my customers.
And here it is. So the email from my
trusted customer is now coming in. Uh
and I see that the agent picked it up
and is now running with this task
without me having to review this
incoming message. So, so Kasim is a
registered customer in my system and
based on my settings the the agent does
not need my attention to review messages
from Kasim. So it it goes ahead and
checking the content of the email it uh
extracts the details and starts to
generate either the response reply with
the item availability information or the
quote document. So let's give it a
little bit of time to to go through this
request.
All right, it looks like the message is
ready for my review. So, let's take a
look at what the agent uh did in this in
this period of time. Again, every single
step is still listed uh in in the
co-pilot pane for you to review every
single step. Even though you instructed
the agent not to bring your attention to
these actions, you can still
retrospectively review every single step
of the agent. So, I'm going back to
review the message that Kazim sent to
me. So here's the message from AdSome
Corporation with a couple of attachments
and let's see what is what is asking
here. So Kasim is asking that I would
like to purchase the same items I
ordered last month. This is an
interesting request. Uh and please see
attached invoice uh details. So let let
I'm curious to see what was attached to
this um to this request. And I see that
the privacy policy is attached which is
great. So Kazim is very mindful of of
privacy. and his organization is at the
top of the privacy requirements, but it
is not relevant for for me for the agent
to create the quote. However, there
isn't there appears to be a PDF
attached. So, let's open it up and see
what's included here. Um, yes, this is
the invoice included with this email
that lists some of the items that this
organization wants to ask. All right,
perfect. So I I don't need to do
anything else because uh I can see that
the agent already took action on this.
So let me review the quote which was
created by the agent. I open it up
and uh let's see all of the details
already populated. The items are added
to the list. So and and here I see the
shipment date. And what you might notice
on these lines is that there are a
couple of items which we are shipping on
17th uh of this month. and there is
another my item which is shipped two
days later. So that's exactly the the
capability of the agent which is using
the capable to promise feature to
calculate that shipment date. So the way
if you want to you don't have to
validate the what agent does but if
you're super curious and you want to
validate what what's actually happening
be behind the scenes you can do that as
well. Let me quickly navigate to
availability
uh item availability page.
And uh what I'm going to do, I'm going
to search for the Munich chair.
There it is. And I see that it is indeed
out of stock and not available on the
current date. But when I engage this
capability to cap to calculate the
possible uh earliest shipment date, you
see the line is recalculated based on
all of the logic and the setup which is
configured in business central and it it
does allow me to to see on which date uh
earliest we can ship this item. That's
exactly the capability which the agent
uses to identify this shipping date for
the items which are not available on the
specific date required by the customer.
So fantastic work. Lots of time saved
for me having to try different options
and can configure this manually. So it
looks like the agent did all the job for
me. And what I'm going to do, I will
just u review the outgoing email.
Again, it is composed beautifully. So
there is a fantastic signature included
by the agent in the end. There is a
sales quote included as well which I can
review. It has all of the right items
and it's ready to send to to be sent to
the customer. All the job is done.
>> Yeah. So, how we envision this sales
order agent is to make it more
autonomous uh going forward. So, we have
even have even more options or
configuration for you to make the
process even more autonomous. So let's
go to the agent settings again and I go
to this particular card which says
create sales document. Here you have a
bunch of options throughout the process
of the creation of sales code and an
order at what point you will require a
user to review. You can choose if you
want to review when the code is created
or you can review when the confirmation
for the sales code is being sent.
Similarly, you can also review once the
sales order is created. What we can do
now is to uncheck this option of
reviewing the sales code. What it will
do is basically for any request that
comes from a register user and for the
items that the user is requesting is
available, it will go directly to the
step uh of creating the sales order by
not asking any reviews in between. So
let's see this in action. So now I've
unchecked this box and I will update the
configuration.
And now we are waiting for any future
requests that we might receive from our
customer.
Here it is. We have received a new um
email from uh myself in this case but
from our customer. And now since there
is no review for registered customers
inside BC and if the item is available
there will be no reviews and we have
unchecked the box which says we need a
review for the sales code. The agent
will follow all the steps but they will
it will not ask for any reviews until it
reach the sales order and will ask for
confirmation then.
So now the agent is done with this
particular task and asked for my review.
As you can see from the steps the agent
has performed each and every steps but
it didn't ask the user for the review.
It looks for it did look for the item
availability. Uh it created the sales
code and converted the uh the code to
the order and the only confirmation that
is required from our side is to review
the outgoing message for the sales code
created. But let's first review the
incoming message itself.
So it looks like a quite similar uh
email that we just saw. It is a repeat
order where the user is asking to
purchase an item that it ordered last
month. But what's interesting is the
attachment this time is an image. Let's
try to download this image and see how
it looks like.
As you can see, this image uh is yet
another format of input as an attachment
that the agent can process quite well.
And over here you can see all the three
items that were mentioned inside this
invoice. And it looks like a a very
standard invoice that you can take a
picture from your mobile and attach to a
particular email. And it looks like a
standard any standard uh invoice. And if
I go back and review the order that was
created, you can see all the three items
from the invoice were added correctly.
And since the order promising was turned
on, you can see the right uh shipment
date were also entered
and everything looks good. uh when we
review the outgoing message with the
right structured email and with the
right attachment the only thing I have
to do for this particular task was to
confirm the final message and and once I
do that that's was the only human
intervention that I needed for this
particular task.
So that concludes some of the cool
features that we wanted to show for our
sales order agent. Thank you very much
Kazim. In these demos, we demonstrated
some of the key capabilities that many
of you asked us to add to the sales
order agent to make it more capable,
make it more autonomous, and more
tailored to your business. You've seen
how the sales order agent can now
process email attachments of different
kinds. It can use the very powerful
feature of capable to promise to set the
expected shipping date for your items.
It can create sales orders directly from
the email request skipping the
unnecessary uh steps of going through
the quote if that is required by your
business. You can even interact with it
using natural language instructions. All
of these capabilities should help your
business become much more efficient with
the sales order agent. We do hope that
you will find these capabilities useful
and start using sales or agent to help
scale your business. Thank you so much.
>> Thank you for watching.