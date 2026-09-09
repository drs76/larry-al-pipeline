# Microsoft Presents: Autonomous agents in Business Central

- **Source:** https://www.youtube.com/watch?v=nCD-CC8TrCs
- **Video ID:** nCD-CC8TrCs
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 92m01s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Ladies and gentlemen, please welcome our
three speakers, Christian, Erida, and
Estban for the autonomous agents in
Business Central.
Ah, it's exciting to be here. We have
Henerita and I'm Christian and we are
going to talk about autonomous agents in
Business Central or AI agents or
autonomous AI agents or just agents. We
call them different things but they are
the same.
So we are going to cover a few things.
Uh we're going to talk about what are
agents really to give you an intuition
about what they are and what they can
do. We will of course demo our first two
agents sales agent and pays agent uh in
more detail than in the keynote today.
And then we will go a lot under the hood
to show you how they really work. Again,
we hope you will leave the session with
an understanding of what they are, what
they can do, where Business Central is
headed with agents.
Okay, let's start with talking about or
reflecting over what is an AI agent. And
here I'm going to draw upon a concept
from philosophy. I have a link from WD
Wikipedia uh because I'm going to show
you a couple of quotes. Let's start with
the first one.
Human agency entails the claim that
humans make decisions and enact them on
the world. So there's this claim that
humans
have a free will. They have options.
They can choose for themselves what they
want to do and when they make a decision
they enact them on the world. So I think
what this means is more the physical
enactment taking action taking real
action which is more than just
information exchange. It's more than
just chat. It's actually doing something
that has a lasting impact in the world.
Another quote, an agent typically has
awareness of their physical activity and
the goal that the activity is aimed at
realizing. So agents know what they're
doing. They can see they can reflect on
themselves. They can sense the
environment. They can see what impact
they're having on the environment.
There's also this idea of a goal. So the
agent is pursuing a goal and is taking
actions to get closer and closer to that
goal.
As humans, we all have agency.
Imagine I wanted to leave this room. Now
what would I do? I would sense my
environment. I would see there's a room
exit there. There's an exit here. I
would then use my intelligence, my free
will to make a decision. Let's say I
wanted to go out that exit. Now that
becomes a more tangible goal that I
would try to pursue. And so I start to
do activity that gets me closer and
closer to that goal. But if something
gets in my way, I'm free to change my
mind. I have a free will. I can choose
to go out one of the other exits.
That's for human agency. How do we
translate that to AI? Well, AI agents
can sense the environment in the digital
world. They can make decisions. We
actually empower them. We make we give
them flexibility to make their own
decisions quite a lot as you will see
and they have intelligence through LMS
which is important because the decisions
that they make would probably not be as
good unless if they didn't have
intelligence.
So what do they do with these agents?
They pursue goals and the goals are set
by humans. How do they achieve those
goals? As I said before, it's actually
up to the agent. The agent decides on
its own, uses its free will to decide on
how it gets closer and closer to that
goal. It might look like this. It might
also look like this. So if you remember
one thing from this slide, it should be
that AI agents are goal oriented, goal
seeking. They have options and they try
to use their do the best they can to get
closer and closer to the goal.
How do we support AI agents in business
central? We think agents are actually
very much like humans in many ways. One
of the consequences of that has been
that we have decided to represent them
as users in the system. So they are
users in the records in the user table
and as any other user they have display
name, username, permissions, profile.
They also have a job description. Agents
have a job. We all have jobs, right? We
all have job descriptions. The
difference is that our job descriptions
are not written down. They're more a
mutual understanding like we know what's
our job. We know what's not our job. But
for AI agents, we write it down. We
write down dear agent, this is your job.
You're supposed to do this and this.
Once we have an agent, we can delegate a
task to it. Now that the agent has a
goal, it will try to pursue that goal.
How does it do it? What options do we
make available to these agents? What
resources do we make available? We make
the whole Business Central user
interface available to these agents.
They will actually log into Business
Central and navigate the UI, operate the
UI, open pages, fill out fields, close
the page. Again, all of that same as
what humans are doing. Let's drill a
little bit deeper into the last point
here. Here's an illustration of Susan
who is a Business Central user. She uses
the browser to connect to Business
Central. When she presses a button, a
web service call will be made to the
Business Central online service where it
will reach an API that we call the
logical UI API. This is an API like many
others using JSON,
but it is designed in a way to power a
UI. So it has everything that is needed
to render the UI in the browser. It has
operations for all the things that Susan
can do, press buttons, set field values,
etc., etc. So when Susan press the
button, the web service call goes to the
web server, response comes back and then
on the browser, it is converted to HTML.
So it renders nicely for Susan.
This is how Susan operates the Business
Central user interface. How do agents
operate the business central user
interface? Well, they call the same API.
What this means is agents can see and do
everything that Susan can see and do.
It will actually log in to the business
central UI and it will actually press
buttons and navigate just like a human
would just not using HTML, using JSON.
That's just the technicality.
So you can see the AI agent is not
inside of Susan's session. It's
separated just like a colleague. So it's
really more like a colleague. They work
side by side asynchronously
from each other. So when the agent lo in
logs in it will see the role center. It
has a goal. Remember it has a task. So
it has a goal that it wants to pursue.
And maybe we'll look at that ro and say
hm I think the next thing I want to do
is click that button that is called
sales orders. So it does and the
response comes back from the web server
with a list of sales orders from the
sales order list page
and then what what will it do? It might
think I need to press the first link
there to open the first sales order and
it does that and the response comes back
and with all the details about the sales
order etc etc. So this is this is how it
works. It's really like a user in many
ways.
But enough talk. Let's have a look at
our first agent, the sales order agent
to see how it looks in real life.
Yep. Thank you, Christian. Um, so we're
talking about the sales order agent.
Let's first start with a scenario of how
sales orders work. Typically, many of
them will come in as an order to your
mailbox. So, a customer will write in
sometimes with a very explicit specific
request listing all the items they need.
Sometimes they just come in with a query
like, "Do you have any chairs?" And then
a person in your team will be the one
that is keeping an eye out on that
mailbox and then checking if some email
is coming in, picking up those emails as
soon as possible, and then looking at
the email, checking all those items that
are requested, if they're available or
not. uh making a draft quote out of that
and then preparing a response for the
customer, sending that quote over,
waiting for the customer to confirm and
at the very end when that happens, we
create a sales order. So, it's a long
manual process and it's bound for
automation, but not just any automation.
And what we need in here is exactly that
intelligent delegation as Christian
described agents. And that's exactly
where the sales order agent comes in in
Business Central. It can be set up to
monitor a shared mailbox for all those
incoming sales inquiries. And then when
a mail comes in, just based on that
email, it can identify the right
customer that is sending you this
inquiry. It can check for item
availability.
Based on that, you draft a quote. It
even prepares a response for the
customer, attaching that quote as a PDF
to the response. sends it over to the
customer with your confirmation if
that's how you set it up. And then when
you receive the confirmation, it
converts it to a sales order.
And of of course um above all this, it
can also handle multi-turn conversation.
So what that means is a customer change
their changes their mind, they want to
add an item to the quote, remove an
item, change quantity or something else.
The agent can handle that and go back
and forth with the customers and change
the quote and the sales order as needed.
It also can ask qu uh clarifying
questions for those vague inquiries as
we said where if you just ask, hey, do
you have any chairs? It can go and find
the chairs that you have available if
that's how you set it up and then
prepare a response with all that
information and send it to the customer.
At the very end, what is also very
important to us at Microsoft is keeping
the human in the loop and making sure
that if you set it up like that, you
will review any responses that are sent
to the customer or you will review the
sales quote before they're sent over.
So, the sales order agent doesn't just
do small tasks here and there. It
understands the goal that was set to it
and it can handle that whole flow. It's
your new teammate that is ready to act
tireless. It knows when to act, when to
wait, when to ask for help. So, that's a
long intro and a long infomercial. Let's
go and check it out in the product.
So, we start in Business Central. How do
I set up an agent? Well, it's very, very
simple. As soon as you log in right into
your RO center, at the very top in here,
you'll see that the avatar has been
added. I hope it's big enough that you
can see. And this agent is not yet
activated or configured. So it's
represented by this dash line in the
avatar and that plus sign right next to
it. So if I want to activate it, what
I'll do is I just press activate over
here and then it will open this
configuration dialogue. So, we started
the whole process of the sales order
agent with the fact that it can monitor
a shared mailbox. And we can very easily
do that here where it says monitor
incoming information. I'll just pick a
mailbox that I've already set up in this
environment. So, that looks about good.
And as you see, it's ready to activate.
I can just update it and activate it. If
you want to be a bit more granular with
your setup, there's of course more
things that you can have a look at, such
as if I go to the next page, you can set
up if you want to review, for example,
all incoming messages or just the first
one or no review at all from your
senders or think about item availability
as you prepare those quotes. And what's
next is we also talked about the agent
as a team member, right? It's not a
co-pilot that you are using alone. Of
course, if you want to, you can do that.
But you really win in these situations
when you allow your whole team to help
when you delegate tasks to them. And you
can do that right here in the
configuration dialogue by managing user
access. And right now, I'm the only one
that has access to this agent because
I'm the one configuring it. But of
course, I can add Christian over here or
Estabban to also be able to work with
the agents and look at its tasks and
help it if needed.
So, as it is now, they can just look at
the tasks and help there. But if I want
them to be able to also configure the
agent with the things that I'm doing
right now, like setting up the mailbox
or those granular uh properties, I can
give them permission to also configure
it. And it's really that simple. Now,
the agent will be running and checking
my mailbox and just doing all of those
processes in the background. So, agent
setup done and dusted. I have another
environment where the agent has already
been configured and I think some emails
have come in. So let's just go and
switch and have a look at that. So yet
again you see this is the new
environment. There's a couple more
avatars right here as we said before.
And the one that has the initials so
which is the sales order agent has this
red dot with a number on it which is
quite a familiar um UX um scenario for
all of us with all the apps on our
phones. When they need our attention,
when there's any notifications,
there's just that little dot telling
you, "Hey, come have a look. I need your
help."
So, what you need to do now is just
click on that avatar and the task pane
will open up. And you'll see some
information, of course, about what agent
you're looking at the tasks of and then
that list of tasks. And you'll see that
the tasks are also grouped. At the very
top, you have the things that need your
attention. Um, so matched by those red
dots, as we saw the red dot on the
avatar. And then at the bottom is all
the recent things like things that your
agent has worked on, tests that are
completed, tests that have been stopped,
tests that are running, and a lot more.
So if it needs your attention, it will
be right there at the very top waiting
for you. So let's get to the first task.
There's an email from Alan Steiner.
Let's have a look. So once I click on
that task, what happens is we go to this
timeline view where we can see
everything that happened since the task
was created and anything that the agent
did after that.
So I can see all of the steps as I said
if I expand that group and it all
started with a message that was sent
from Allen's. Let's click on that and
have a look what the message is. So what
you see is once I click on that page on
that step that's related to the incoming
email the page for the incoming email
immediately shows up on the left and
that allows me to very quickly review
all of the changes all of the things
happening with the task. So in this case
the incoming email is as we said from
Allen and the agent has already been
able to identify the right contact based
on that email and identify the right
customer that's that that contact is
related to. So that's all good. Then if
we have a little read through um of the
email, we'll see that Allan is looking
to refernish their office um asking for
two Anverb conference tables and 20
Berlin chairs and asking if they can be
delivered on June 12th.
So that all looks good. Let's go back to
the timeline and see what the agent did
after this. So you can see a bunch of
steps that are already completed as
shown by the tick on the left where it
went to look for the items if they're
available. Then it created a sales quote
and it even populated that sales quote.
If I click on that, what happens? As
before I am able to review things very
easily because the right page just opens
up immediately on the left and I can see
that this is the sales quote that was
created for a DATM corporation.
uh and a couple of the details that the
agent put in. So, it's that same
customer that we talked about in the
same contact. And we have the requested
delivery date that the agent did pick up
from that email that we read and filled
it in the right field. And also, we have
made a couple changes to the lines where
we see those items that were requested
are right here in the right quantities.
So, everything is looking great so far
and the agent did all of that without
our help. What it needs our help for is
reviewing this email that's be that is
ready to be sent. So if I click on that
I will see that we have a message that
will be sent to Allen's once we confirm
it. And the message body is beautifully
written thanking them for their request
listing the items that they asked for
listing the total amount and even
reconfirming that request delivery date
over here as they specified it in the
email.
What we're saying is also that the sales
quote that we have prepared is attached
for their reference and we can even view
that right here. So if I show
attachments, there's one, the sales
quote. I open it up and as we saw
before, we can just preview this PDF
right in business central and see all of
those items that we mentioned before.
So all of this is looking great. I think
the agent did an excellent job. I didn't
even have to move a finger besides click
confirm. That's it. My contribution to
this task is done. So let's go and have
a look at the other one. We have two
remaining tasks. If we have a look at
this one from Diane Prescott maybe. So
what's happening here is similarly to
the previous one. The task starts with
an incoming email. Familiar concept. So,
she's writing that her sister is opening
up a cafe that she be she's been
dreaming about for years and she'd like
to order some coffee beans for the
opening day. And a few more details like
three packs of beans from Ethi Ethiopia,
some from Brazil, some from Colombia.
All looking good. And again, the right
customer and contact have been selected
just from that incoming email. And it
all looks great. And then the next steps
are we have created the sales quote for
that contact and added the items to the
quote.
Just a quick check on the quote not that
it's necessary but yes all the right
items are there and it's the right
customer. So, while this all looks good
and the agent is now ready to send the
message to Diane, I can see that there's
also a step coming up in the future in
the timeline, which is another message
that is coming from Diane for the same
task. And in the step that I have now,
well, I've already the the agent has
already drafted the response for Diane.
But there's also a warning on this step.
So, if I click on it, you can see that
the agent knows that a new message
related to this task was received while
this step was pending my review. And
it's telling me that it's a good idea to
maybe just review that other message
that's coming in before I decide to
confirm or discard this one. So, that
sounds good. Let's just go to the next
step and have a look at that message
that Diane sent to us. So, it looks like
Diane ch changed her mind. she would
like to add some more items to the
order. So, two packs of the decaf beans
from Colombia because she just forgot
about it. Understandable. And also,
she's saying that she heard that we
offer gift wrapping. It would be very
sweet for the grand opening and that we
should add that if possible. Sounds
legit. Why not do it for Diane? So, what
I need to do now is this email that was
drafted doesn't really match the latest
uh information that we have about this
task. So I'll just discard this step
because the agent needs to process that
information that is coming in. So once I
have discarded that I have Dian's
message that I read before which I can
just confirm because it is legit and
I'll tell the agent to just resume with
a task. So it updates all of that flow
with the latest information that we h
that we have from that later incoming
email. And you saw how this was the
multi-turn conversation, right? because
as long as Diane replied to the same
email thread as the one that she used
for her initial inquiry, that message
will go into the same task and not
create a new one. Pretty neat. So, while
the agent is running this task and I can
see that here and I don't need to work
on it because the agent is working on
it, I have one last task that needs my
attention and that is this one. Oh, and
that was quick from Diane.
So, maybe we'll look at Dian's.
Um, I can see that the agent was very
quick to draft another message for
Diane. And let's just go and have a look
at what that was. So, actually, we see
that we're thanking Diane for the
update. So, we have acknowledged that
that new email came from her. We did add
those two packs of decaf beans from
Colombia as she requested and also the
gift wrapping. And you can see also that
the sales quote PDF has been updated
with these decaf beans. can even zoom in
a little and make it very clear that all
the items I want are there. Um, and then
let's look at that gift wrapping because
I don't think that's a standard piece of
information in a sales quote, right? So,
let's go and have a look at the sales
quote. What did the agent do? Well, you
can see that there's this field called
gift wrap required and it set it to yes,
and it's highlighting this field that is
right here. So what this is, it's
actually a field coming from an
extension, not part of the sales quote
page initially, just my extension. But
the agent doesn't care where the field
is coming from as long as it has
permission to that field. So it's just
reading that JSON of the logical UI as
Christian mentioned and it's able to
interact with anything on the page just
as I would if I would be handling this
task. We also have those changes to the
lines as we saw with the Colombia beans
and it's all looking pretty great. So I
think the message looks good. The quote
uh that was prepared and updated looks
good as well. I'll just confirm. And
that's also done and dusted. So the last
task that I have is this email from
Alicia Thumber. Let's go and have a
look. Well, this one also has a warning,
but it's a different one, right? If I
click on it to have a look, then I can
see that this is a message from Alicia
who's not a registered sender. And the
warning from the agent is that this
appears not to be related to the agent
because it's a personal note does not
pertain to the agents responsibilities.
And that is actually correct. The email
says, "Hey, heard you're in Denver
presenting at BC Tech Days. Break a leg.
Haven't broken it yet. Want to catch up
over lunch on Friday while you still in
town?" Well, the agent doesn't need to
worry about this. I'll talk to Alicia
later. And I'll just stop that task and
all is done. So, it was all very quick
compared to having it done manually. And
you can really have a look at all that
by looking into the summary that we have
for the agent, which you can either see
here from this info icon, or if you
hover on the sales order avatar, you see
the same content with a little overview
of what agent you're looking at, those
initials, um, the state, and then a few
crucial KPIs for the agent. So, we have
the number of received emails. I have
activated my agent just a while ago, so
there's not many of them, but it's 13.
And just with these 13 emails that it
received and processed, it saved me 1.1
hours. Um, and this is an estimation
based on the assumption that uh it uses
it saves up 3 minutes per email. And
then from all of those emails, it has
created four quotes maybe because some
of them we haven't heard back from the
customers, some of them were unrelated
as the one I just stopped. And from just
those four quotes, we have saved 24
minutes. Again, an estimation based on
the assumption that we would use say uh
six minutes per quote. You know, filling
in all those details, the right
customer, the right items, the right
quantities and so on. So, it's pretty
great. And out of those uh quotes, I
still haven't heard back from my
customers. So, I have no orders, but
they would be here if uh I had any. And
also we would know what amount including
tax the agent helps us make with all of
these orders that it handles by itself
so to say.
So that's all about the sales order
agent. Let's hear how it works behind
the scenes with uh estab.
All right. Thank you.
Yes. So, so you just saw this whole new
sort of pain and timeline experience for
uh people using agents that we've built.
Um, but a lot uh revolving around agents
is is also just good old business
central. Um, so as you might expect um
we do have agents as you know uh a list
page and a table. So if we go to the
agents list page here, we can see all
the agents. Uh you'll also notice for
example this one is disabled and it
shows up as as uh the paused icon uh in
the avatar. Uh and let's have a look at
the at the sales order agent for
example.
So what Christian mentioned earlier and
what you might be able to see here is
that this agent cart page sort of
resembles the user card page and that's
because um every agent record is
directly tied to also an underlying user
record. So every agent in BC is actually
a user of a special agent type but
nevertheless it's still a user and
therefore permission sets and everything
else you have with users apply. also the
profiles. Um, and there are some
additional uh things that agents have
that regular BC users don't have like
this user access that Arita uh showed
you before when she was setting up the
agent where you define okay which users
have access uh to which agents
and this is very important because every
agent registered in the system and all
these tasks they they don't have their
own separate tables. Um so the user
access here works as a role level
security um for this data. This means
that for example if Arida uh is given
access to this sales order agent but not
some other agent in the system then she
cannot see that agent. So if she opens
the agents list page even though it's
reading from the same table she cannot
see the other agents uh or if if there's
some alco trying to do a a fine set or
similar. This is all kind of restricted
internally by the platform based on this
user access which makes it uh slightly
different let's say than than other
traditional business central tables and
the permission sets and the profile are
actually very important when when you're
creating an agent because they are
really responsible for the the security
and to to a very large extent the
accuracy of whatever agent you might
build. uh why don't we have a look at
the sales order agent profile for
example. So uh I will just go to my user
settings and I'll just change my role
here
and
let's go into that new profile.
So something you might notice is this is
actually very empty. Um a lot emptier
than my own RO center. And that's on
purpose. So one way to really help um
the the agent be very reliable at what
it is tked to do it is to is to make
sure that it mainly just has access to
the relevant pages and fields that that
agent may need. Because as Christian
said, the agent will just see the UI
like any other user and it will make
decisions and it will figure out how to
get the job done and you can assist it a
lot by restricting what it can see and
making it less likely that maybe it goes
into places that it shouldn't. It also
makes sense for example permission wise
that uh maybe this agent has access to
create quotes but not delete customer
records for example. Right? So if we
open a sales quote, you'll also notice
um it is actually quite simplified here.
So this is all controlled by the
profile. You'll see that the the agent
actually sees quite a few uh less
actions and fields than a human would.
And it's again it's just trying to steer
it, you know, into the right direction
and making sure it really just has
access to what it needs to. uh but of
course when you are building an agent
you are uh very welcome to uh play
around with the profiles and ro centers
that that fit your needs. So let's go
back to the role center
now. Agents are sort of the starting
point, right? Um agents also have
instructions. Uh unfortunately
instructions are not something I can
show you in the cart page for the sales
order agent, but you're going to have to
trust me that they're there. um they're
stored as part of the agent record and
they describe what the agent should do
and with all of that the user access the
you know regular BC user setup profile
permissions and the instructions you
have an agent um however an agent on its
own uh doesn't do anything right you
have to ask it to do something and how
you ask it to do something is by
creating agent tasks so this is also
just a table And an agent task is
basically the unit of work of an agent.
You create a new task, the agent will do
something. Um, now tasks can have inputs
and outputs of course like you saw in
the sales order agent. But they don't
have to. Um, you could create an agent
where the instructions are go to the
customer list page, open the first
customer, and set some field to some
value, right? And it doesn't need any
additional input. The instructions are
pretty clear. uh it's not going to
produce any output because well there's
no conversation going on there. So
that's also a completely valid task. Um
but usually the interesting part about
tasks is is the multi-turn
conversational aspect where not only can
it have an input and an output but it
can have a sequence of inputs and
outputs. can can really be a
conversation. Um, like you just saw with
the sales order agent where you might
get an initial inquiry for some items
and then it replies and and you reply
back to it and and you end up with
multiple inputs and outputs.
And that is where um task messages come
in. So these tasks you're seeing here
are the the exact same uh records
basically that are displayed in the task
pane view. We're just viewing them in
the list page. And each of these have
messages. And me messages are what we
use for input and output. So if we click
on view messages, for example, um you'll
see that they have a type. There can be
an input message or output message. Who
created this message? For example, some
of them the output ones are always
created by by the agent and the input
ones are created by a yell code and they
also have a status. For example, here
you can still trace this discarded
message that Arita had uh back when she
received uh a new email and she kind of
had to have the quote updated.
So um it is very important though when
thinking about multi-turn to think about
the task because the only way the
multi-turn works is by making sure
you're using the same task. And so
whenever you want to build an agent that
is uh conversational in nature, you have
to make sure that you're also being able
to find the task that already exists for
a certain conversation and just add to
that task because uh all the other
records uh outside of the agent itself
are are usually tied to a specific task
and all the context and memory that the
agent has about what has happened here
um are part of individual tasks.
There's a a bit more of information here
um than what you might be able to see on
the timeline. For example, we have log
entries. Uh and log entries are a more
detailed um let's say view of everything
that that the agent has done. So there's
different types of um let's say
operations an agent can perform. Uh page
operation is what we refer to every UI
interaction. Um there's also the
creation of output messages. The whole
story around user interventions like if
the agent asks you to review something
for example or it needs help and and in
log entries you can really see a lot
more detail. For example uh that it was
on the item availability page and in
invoked search with a particular set of
keywords. Uh it invoked a specific
action on some specific page. Uh, and so
this can be very useful uh for for
troubleshooting or or auditing purposes
because it gives you a lot more detail
uh than the than the timeline view.
Though usually users that are just
regularly interacting with an agent will
probably just tend to stick to the
timeline view.
And to to kind of just um bring home the
point that everything is just a task, um
we have a a special uh extension here
that adds a few more actions. Uh and
I'll just create a task for this sales
order agent. I'm not sending an actual
email right now, but I will just uh say,
yeah, put some message text here. and
I'll pretend it's from Robert Towns and
give it a title. Um, and I'll just
create a task. This this action
literally just inserts a task record and
the message record via al um and so
you'll notice if I go back to my row
center and
refresh perhaps. Yes, you see the task
is this this this test task is now
actually running and the whole timeline
experience is the exact same because
everything you're seeing in the timeline
is just really based on on these agents,
tasks, messages and so everything else
uh you get basically for free. Um
so one thing that is also important to
note here around agent permissions is
that the agent does have permissions
assigned to it. However, when a task is
running, it will actually run with an
intersection of permissions of the user
who created the task or who last
assisted with the task and the agents
permissions. Um, this is to prevent any
kind of uh elevation of privilege. So,
for example, I might create an agent
that can create quotes. Um, and then
some user that isn't actually allowed to
create quotes might somehow, you know,
be added to the list of users for this
agent. Um, and and we want to avoid
these situations where users get the
agent to do things for them that they
themselves don't have permissions to do.
So, uh, whenever the agent runs, uh, it
will always intersect its permissions
with whichever user uh, kind of last uh,
handled that task and and run with both
of those. Well, with the intersection of
those um yeah, so you can see everything
here otherwise shows up the exact same.
Um you can see the same sort of summary
of the message and the fact that another
message was created um etc.
And now maybe let's have a look at some
slides.
So we just talked about agent and and
tasks and messages. And at the end of
the day this is all data, right? These
are records in the database. We know an
agent has permissions in the profile.
Well, the agent user record has that. We
have the instructions. And so
creating an agent could boil down to
going to an agent list page, clicking
the new action,
putting some data in, and then creating
tasks just like I did uh manually via
the UI. But um of course that's not
really the expectation if someone wants
to ship agents and being able to uh
control their life cycle, update them,
update the instructions periodically.
And so the way to deliver agents is as
many of you might just guess is by
creating an agent application. Uh the
sales order agent is an app and every
other agent is also an app. And there's
actually quite a bit that the agent
applications are responsible for. Um,
this whole setup experience that Arita
showed you, having a setup page, uh,
keeping track of that setup data,
preparing your instructions based on the
setup, maybe some some of the options
for configuring your agents influence
that agents instructions. All of this is
kind of something that has to be handled
by the agent application. uh we will of
course provide various utilities to make
it very easy to work with these agent
records and tasks and various other you
know commonly used things but at the end
of the day there is there is quite you
know some thought that has to go into
creating an agent application
and uh let's have a bit of a look at the
difference between what the agent
application does and what the agent
platform does uh when it comes to
running a task. And we'll go with email
as the example because that's what you
already saw with the order taker and
it's a fairly simple uh interaction.
So we have two sides. We have uh the
agent application and then we have the
agent platform. And so when a new mail
comes in the expectation is that the
email integration part is is actually
handled by the application. The agent
platform doesn't know how to read or
send emails or or use any other channel.
It works with tasks and it creates uh
output messages and reads input
messages. Right? So here you probably
would have some background task, some
scheduled task running periodically
checking a mailbox perhaps or you you
have a different system that just goes
into BC. Um that's really up to the
implementation. But let's say uh a new
email has arrived. And so the first
thing that the application has to do is
to determine well is this a continuation
of a conversation or is this a new task,
right? And for example, there's fields
you can use on the agent task record uh
that allow you to uh link uh that task
to any external ID you want. It's a text
field. So you can use that for example
to to to check whether you have
something for uh this outlook
conversation ID or or any other system
you're working with and to find some
correlation there. But it's very
important again to make sure that you
are trying to find an existing task.
When you have the task or you've created
a new task, the agent application code
just needs to insert the message with in
this case the contents of the email. And
then the final step really is just
setting the task status to ready. Right?
It's just a field. Uh and when the
application does this, the task is more
or less handed over to the agent
platform. So it just indicates to the
agent platform that there's a task that
is now ready to run. And so the agent
platform will take care of uhuling that
task in the background and running it as
soon as it can. Uh it also means you
don't need to dispatch anything from the
AL code. uh it doesn't block anything to
set the task status to ready. Like you
can do it in a UI session as well. It's
fine. Um and the platform will just pick
this up. Um it will do some checks like
that how many tasks are already running
for your environment. Uh what's your
quotota and other things but then as
soon as it can it will actually start uh
executing the task. And executing the
task is actually many different steps
that happen. Um we can see some examples
here. So the first thing that the Asian
platform will do is always analyze any
new input messages that haven't been
analyzed before for harmful content. Um
so the platform will automatically
analyze any input for harmful content
and if any harmful content is ever
detected the task is blocked and it
stops and that's it and the agent will
make that very clear in the timeline. um
and it will not proceed with that task
after it analyzes the input messages. Um
well, it starts interacting with the UI
via the logical uh API uh that Christian
mentioned before. And what is it that is
it that it's doing when it's interacting
with the UI? Well, it's processing the
instructions, right? It it has it knows
what it's done already as part of this
task. it it knows what it sees on the
page and it will just make decisions
about what the next step is and it will
always record that. So uh it knows also
what to do next and this is purely based
on on the agents instructions in in the
agent record. The agent platform also
automatically will handle user
interventions. So user interventions is
um what we commonly refer to any
situation where a user needs to go and
and click on something in the timeline.
uh for example, reviewing an incoming or
outgoing mail is an intervention. Uh you
could also in the instructions say, "Oh,
in in this speci specific situation, you
should ask for help." Uh and then it
will just also just create a user
intervention request. Um something that
could also happen, especially depending
on the extensions you have installed and
your permissions, it it might run into a
permission issue, right? It might try to
do something on a sales quote and but
because there's some extension in maybe
some new field and it doesn't have
permissions to that field, it might not
be able to proceed and it will surface
that as well and ask for help and then
some user can go and and kind of fix
that. And this is all just handled
automatically. There's no involvement
necessary here from the application
side. Finally, uh well depending on your
agent, but this is an email example. uh
it will produce an output message and it
will also handle the review process of
that message. Making sure to ask someone
to review if if that is the way this
agent is set up uh and making sure the
message is reviewed and and that's where
the task execution kind of ends on the
platform side and then we go back to the
application.
So just like the application checks for
incoming mails, uh it would also need to
check for reviewed output messages that
are ready to be sent. And so when the
application finds one of these uh it is
then back to the application uh you know
to run some logic and actually send the
email because uh as I mentioned before
the agent platform does not handle the
communication aspect and then the email
is sent and finally for good measure uh
messages do have a status field that you
can set uh from review to sent. So you
can also make sure that you don't send
the same output message twice. Um, and
yeah, this is a very maybe simplified
view, but hopefully it gives you kind of
an idea of what is expected uh from an
agent application when developing one
versus what the platform just handles
automatically.
And so to recap the responsibilities
uh on the application side, we have the
whole agent configuration story. So
creating your own profile, deciding you
know what what makes sense for the agent
to see or not to see for if you're
creating one uh and your permission sets
providing a setup page and this whole
setup experience uh and probably the
most important thing the instructions
right the instructions are like the core
of of an agent um and then it is also up
to the application to decide well when
do I create a task maybe you create an
agent where people just create a task
manually that's totally fine maybe you
want to have email integration or some
other integration. Uh that is completely
up to up to each application and then
processing any output messages whether
these are then sent by email or you know
placed somewhere else in a share or
something. Um and the agent platform on
the other hand uh provides first of all
this whole agent task pane timeline user
experience with the interventions and
everything else and it handles all the
execution of of of an agent task
detecting harmful content interacting
with the UI handling intervention
requests and creating all the output
messages.
So hopefully this this has given you a a
an initial idea of of uh how these
things work
and um actually before we go there one
last quick demonstration
um
yeah let's look at some AL code just
just uh to uh exemplify what I've spoken
about um this is some code from our
sales order agent
Um
please keep in mind this is uh still all
changing. Um we are still in the process
of refactoring certain things. Some of
these methods, interfaces, etc. that you
see here uh are probably going to be a
bit different by the time this is
public. Um but still it it should still
give you an idea of how things work. So,
one thing we didn't touch on is what
happens before you create the agent
record. Because when you saw Arida um
uh set up the agent, it started with
this sort of dash line and a plus icon,
right? And when that happens, you don't
actually have an agent record. No one
has created this agent record yet. No
one has set it up. And so the way you
get that to show up for example is is
any app that provides an agent uh has to
extend this agent metadata provider enum
with you know your own value and you
give it a name and the important part is
that it expects you to implement certain
interfaces. So there's like the agent
factory and agent met data and agent
validation though agent validation has a
default uh implementation
but so the first thing to do is to
actually uh extend this enum and
implement these interfaces. Again these
interfaces are subject to change but we
can have a look. So in this in this
example we we have just one code unit
that implements both of these interfaces
and here is where you provide some of
the information. For example, you can
decide what initials does your agent
have. There's also the distinction you
can provide initials that show up only
when an agent can be set up versus the
initials used for an agent that has been
set up. Uh this can be useful if you
want to allow multiple instances of the
same agent in the same company so that
you can distinguish them, right? For
example, you could say SO1 and SO2 as
your different initials. uh similar to
the initials you provide whatever page
is supposed to be opened when the agent
is going to be set up. And here we can
also distinguish between a first time
setup and maybe a subsequent setup of an
existing agent. Uh in this case we're
using the same initials and same setup
page for both situations but it's
flexible. And you also have the summary
page ID which in the case of the sales
order agent shows the KPIs that you saw
earlier that area showed you about the
time saved etc. This is also something
that you would implement in your own
agent application and you know find some
meaningful KPIs
and you can also decide whether you want
to actually show this uh sort of agent
avatar with the plus sign. So for
example it might be very common that you
check well do I already have an agent of
my type in this company and if I do I'm
not going to show you the plus sign
because I only want you to create one.
uh otherwise you can you know
potentially allow them to create
multiple instances uh if it makes sense
for your use case and then uh agents are
also always tied to a copilot capability
meaning that if that copilot capability
is disabled in the product in the
environment by an admin or someone then
all the agents with that capability are
automatically disabled as well. So, an
agent is is tied to uh a capability. And
there's a few other things like, for
example, being able to overwrite the uh
agent task message page that shows up
when you want to review a message. You
can create your own page that maybe is
more meaningful to the type of uh
messages that your agent handles.
And here just as uh some final examples
uh we discussed uh the fact that the
agent application has to create tasks
and then also uh mark them as sent and
and actually send them. And for example,
the the sales order agent task uh sales
order agent app um creates a uh
background task when you activate the
agent that periodically um is uh
checking a mailbox and is also checking
for new output messages that are ready.
And uh here's for example an uh the
code. So uh as I mentioned before it
will check whether we have uh a task
based on the conversation ID uh of this
uh email inbox. Uh if we do it will just
add this email as a new message to an
existing task otherwise it will create a
new task. Um and finally
we can see for example here uh it's it's
really very basic right uh you filter
the uh agent task messages of type
reviewed um and then if you manage to
send it you just uh finally update the
status to send and and that's kind of
it. Um so yeah there is um you know
quite a bit to think about and implement
if you are want to create your own agent
application. Uh actually this is not all
you know if we look at all these files
there's uh quite a bit going on in this
agent and quite a bit of customization
and the setup experience building the
instructions. So um it it can take a
while uh to create an agent application
and of course sometimes someone just
wants to write some instructions uh try
it out see if your idea even works. you
don't particularly care about that
there's an email or not an email just
want to create a task an agent try
things out um and I'll hand it over to
Christian to talk about that yes thank
you estan yes so as explained there's
like two parts to it and and you all
know very well how to write al code
which is the big blue box here there are
some nuances about how you register an
agent as as been explained and delegate
task to it but the heart of an agent
really is in the green talks mainly I
would say in the in the instructions. So
you might be wondering how do
instructions look and how do you develop
them and uh to show you that I'm also
going to introduce you to the agent
playground
uh which is a an experience inside the
app where you can change instructions
and try and create a task and just
iterate really quickly. You actually saw
it estan showed it once and I'm going to
show it multiple times. But because this
is just data at the end of the day, we
don't need to redeploy apps. We can just
iterate uh very fast.
So let's have a look at that.
Okay. So let me go to the agents
this page again and and I'm going to
create a new agent on the fly here. So
we see we have this uh menu called
playground. This is not for regular
users. It's more for developers at this
point. I can create an agent and I give
it a name like this would be the
username. So let's say well the scenario
I'm going to use is the policy checker
that you also saw in the keynote. So an
agent that is supposed to research a
little bit like see look through all
sales orders and see if they comply with
the policy. So I call it policy checker
and I already have one. So I'm going to
call it policy checker 2. Policy
checker. And it says type no code agent.
It's going to be called playground
agent. This is code we're running here
is from Friday and it's already been
changed. So if I was to run it against
the latest, it would say playground
agent. Okay. So create one. And so now
we have a new agent. Now we have four
agents. Um and like this is a like a
user, right? So I need to give it some
permission sets otherwise it can't do
anything. And normally I wouldn't. But
for playing with it, it's okay to give
it super. Similarly, I need to assign a
profile to it. What should it see when
it locks in again? I would probably
design a special purpose rose in the for
so it can see, you know, doesn't see a
lot of things that might confuse it. But
for playing with, I'm just going to give
it business manager, which is the same
profile that I'm using. And so it will
see a lot of things on the road center.
You can navigate to purchase orders,
sales orders, customers, vendors, items
and many many more things.
Okay, so now let's enable it
and it takes me to this page. And then
the initials, those are the two three
letters that it will show in that
hexagon avatar. So let me call that
PC2.
Okay, good. I will activate it. And now
I have an active agent. But what should
it do? This is where the instructions
come into play. And so let's give it
some instructions. And I have a notepad
here with some snippets.
So the first one, can you read? Okay.
Yeah.
I'm telling the agent, select a random
sales order. Draft a message with some
details about that sales order. Okay. So
now I have an agent has it knows what to
do. How do I start it? Assistant and
explained an agent will not do anything
until it has a task. So I need to create
a task.
So this is a brand new agent. So it
hasn't done anything yet. But under the
playground I can actually create a task.
And in my particular scenario I don't
need to give it an input message. It I
just need to poke it and then it knows
what it what it should do. But I need to
give the task a title. Let's say I'm
going to call it hello world task
because this is really a kind of a hello
world scenario.
Good. So now
let's look at PC2
and see we have now a running task for
this brand new agent. And so I'm just
going to press F5 a few times here
because it'll save me some time
otherwise it will yeah it will come
eventually.
Let's see what it Okay, now it finished
already. And so what it did was find a
random sales order and write some
details about it just like I asked it
to. Great. Thank you, agent.
So let's go back to I have a shortcut
here to make a little bit faster. Let's
go back to my policy. I
spelling mistake. Bet you saw that.
I'm going to give it some more detail
instructions here just to make it a
little bit more realistic. So what I'm
say telling it is please iterate all the
sales orders. Select each row while on
the sales order page, you know, the cart
page, check if the data on that page
complies with the policies below, and if
it doesn't, request a review of the user
and describe, you know, how it violates
one of the policies and then close the
page and move to the next row. And then
the policies are total amounts including
VAT higher than 10,000 are not allowed
and we don't sell to art schools which
are of course ridiculous policies but
it'll be clear in a moment why I chose
those. So um let's give it a task just
to start it
under playground and let's say um what
should we call it? Check policies
task.
Okay. So while we're waiting for it to
kind of start, let's go to the sales
orders page. And it'll be clear why I
chose those policies because we have
nine sales orders. The first one
has a very high amount including VAT or
tax is US and
second one is fine but the third one the
customer's school of fine art which is
arguably as
an art school. So what we would expect
is that it would stop on the first one
here and say hey here's a sales order
that does not comply with policy and
let's see what it says. Yes. So this
sales order does not comply with policy
because the amount of 17,000
exceeds 10,000
as expected. Thank you agent. Let's uh
I'll let you move on. So now um yeah, it
will go on and pro hopefully skip the
next one and then any moment from now it
will stop on this one.
Let's just give it a moment.
Any
moment now. Elevator music. What?
Elevator music. Elevator music. Yes. All
right. So, it stopped on this one, which
is indeed the one for the school of fine
art. Thank you, Aiden. I'll let you
continue and it will go through the rest
and it will not flag anymore. Great.
Okay. So um that's a little bit more
realistic
but so the first two examples um the
agent was just researching reviewing you
know reading read only it didn't change
anything in our database in our
environment
so to illustrate how it might do that
let's give it some different
instructions
so I'm going to Replace number three
here, bullet three with a new. I'll
delete the first one in a moment just so
you can compare the two. So here,
instead of requesting a review,
I'm saying please set this field, which
is a new field I added on the sales
order table
um to violation plus what policy it
violated. And if there were no policy
violations, just set this value to none.
And then I don't want you to stop and
request a review from me anymore. So I'm
going to delete this line.
Oops. And now let's start that one.
So let's say we call that set field
task.
So and while that runs, let me go back
to the sales orders page. What you
probably didn't notice was this new
field that I added to the sales order
table. So if I press F5 now I should see
I press F5 repeatedly which you cannot
see but I am and you can see that it's
actually iterating through all the sales
orders checking whether they comply with
the policy and if they don't or if they
do they will it will write the
appropriate thing in that field. So
while it's running still has four four
left I think I can make it. So if you go
to this task what a what also showed was
you can actually see the steps as they
take place. So I'm I'm I'm continuously
pressing F5 now. So you can see
everything that the agent does. So it's
really doing it live in a separate
session that it is locked into. So let's
see it's very close to finish. So now it
finished.
So stepping through those
nine sales orders, opening each one,
setting the field value, closing it
again. So three at minimum for each for
each um sales order. That's 27 plus a
little bit more to start and stop makes
33 steps. So the agent did 33 steps to
do this this piece of work.
All right.
So um great. So it's doing everything I
told it to do.
But remember in the beginning I said uh
agents are goal seeking. You tell it
what to you want it to do not how it
should do it. We want to give the agent
uh the flexibility the empowerment to do
it like it wants it to do it. But you
can see in the instructions here they
are a little bit mixed bag. I would say
the first line is fine. I'm just telling
it to iterate all sales orders, which
I'm not telling it to open the sales
orders page. That would be very direct,
just relatively abstract. Iterate all
the sales orders. But then I go into
much more detailed instructions. Select
a row, close the page, move to the next
row. Very directed.
Like, can we do better than that?
So let's try instead of those
instructions, let's try with
shorter instructions.
So now I'm saying policy checker, I
trust you. I want you to ensure that all
sales orders comply with the policies.
You should inform the user when a policy
is violated. So I'm not being very
specific about how we should do things.
Let's um let's u start it.
And let's call that um or abstract task
don't need an input message and we start
it.
So now actually don't know what it will
do. I mean it might request review each
one by one as I as the first scenario.
It might produce an output message as in
the hello world example.
It might.
Yeah. What might it do? We'll see. I
don't know what it will do.
But it's actually already finished.
Let's see what it did.
Okay. So, it chose to
just summarize all the violations in one
message, which is fine.
Did what I told it to do. So what you
can imagine I think the way the where we
are headed with this but it's not
implemented yet is that we give
relatively abstract instructions to an
agent and then when it does something it
actually tries we give it feedback. So
in this case we might say thank you
agent next time I would like it in a
table format and then maybe it will do
it right or if it doesn't do it right
next time I will again give it feedback
kind of reinforce uh this is good this I
want it to be slightly different kind of
when you train a a colleague at work
where you to some extent let them lose
but you give continuous feedback on how
they're doing.
So
maybe you noticed I think
remember 33 that was how many steps it
took to iterate through all sales orders
in the previous task. But in this
abstract task it only took three steps.
How can that be? Well, it's very easy to
see what the agent did. So we can just
open the log entries and we can see that
it started on the business manager ro
sensor
and then it
clicked sales orders
and that's when it decided to create
this output message with the violations.
How can it do that? Well, it's because
if you navigate to that page,
all the things it needed were on this
list page. So the names so it will
identify art schools and the total
amounts you can also see those. So it
realized on its own that it doesn't need
to go into every single card. So it's
actually clever than I was.
Yeah. So I hope that gives you an
intuition of you know how they really
really work and what they what they can
do. So at this point let's uh move on to
uh look at the
other agent that Microsoft is shipping
which is the payables agent.
Yep. Let's go into our last agent of the
day. So for payables agent we know that
every company has expenses. You need to
pay your rent, pay your phone bill, pay
your utilities and so on. Oftentimes
those expenses arrive into your mailbox
as PDF invoices. And yet again, we start
that manual t uh tedious process
similarly to how it was for the sales
order agent when someone in your team
has to go in and check that and download
that PDF, open that side by side with
Business Central. Um try to get all the
right data from the PDF, put it into the
fields that it needs to be, get the
right accounts, match them up, make sure
not to miss any data, not to mix any
data, and all of that could be improved
a lot. And that's exactly what the
payables agent does. It monitors again a
designated mailbox for those incoming
invoices. And once an email comes in, it
can read the PDF. It can extract all the
data that it needs from it by using Asia
document intelligence and then create a
draft purchase in Business Central and
even map everything to the right
accounts based on your company's
accounting policies or the purchase
history. And all of this happens
automatically. uh a draft is ready for
you to review unless it needs a little
bit of help finding the right account.
In some cases, it might. So, let's go
and see how that works within Business
Central. So, I have this environment
which is
polluted with so many agents because um
agents do a lot and it's great to have a
lot of them. Thanks to the initials that
Estaban mentioned, I can tell all of
them apart. And PA is my payables agent.
So if I click on it, the task pane shows
again and I can see the tasks that the
payables agent has been working on. We
can also have a look at the
configuration. Of course, I
pre-activated this one. It's kind of
similar to the sales order agent where
we have set it up to monitor an email
account. And that's it really for the
payables agent. So let's go and have a
look at the last task that it worked on.
It has already completed it, but it's
good to just see what happened. So,
similarly to the sales order agent, we
started with an email. What was
different here though was that we're not
interested in the content in the body of
that email as much as we are in the PDF
that's included in it. And I have to
play some elevator music while it opens
up. Okay, you didn't hear me sing.
That's good. Um, so we see that the
buddy is just something very generic
where we have received this email that
says, "Thank you for purchasing from
graphic design institute. Please find
the invoice attached to this email." And
as we know, we can preview PDFs right in
business central. So I can have a look
at the PDF right here and see what is it
really. So it's an invoice. Again, if I
zoom in a little from graphic design
institute and I can see um that it
includes logo design, a mouse pad,
prepaid vendor managed inventory lease,
shipping fee, all good. Um so what did
the agent do with this email that came
in and with this PDF? I can have a look
at the next step where it actually
finalized the drafty document. But if I
want to have a look at that draft e
document instead of the purchase
invoice, of course, I can do that right
here in the action bar. open that e
document draft. So if I have a look at
the e document draft, I want a little
bit more space. So I'll just collapse
this pane and give myself some more
space. What I can see in the page over
here in the draft is that I have all the
changes in here and I have a preview of
the PDF on the side and I can make my
fact box as wide or as narrow as I need
it to be and I can really have a look at
them side by side where it's logo design
as we have it on the left on the right
mouse pad prepaid vendor managed
inventory. If I scroll a bit
horizontally we can see that the quality
the quantities sorry also match up. And
what's more important of course as we
said before that for the sales order
agent it was able to map everything to
the right customer. In this case
similarly we're a able just from that
email message to uh map it to the right
vendor based on the contacts. What's
more important for the payables agent
though is that it was able to find the
right account to put everything into. So
I can have a look at those one by one.
For example, the logo design went into
advertisement development which is fair.
mouse pad went into office supplies.
Also, fair enough. And the prepaid
vendor managed inventory lease for 12
months went into rent and leases. So,
it's really good at finding where things
need to be. Shipping fee went into
fright fees for goods. And I really
didn't need to do anything because the
agent figured all of this out by itself.
And I can have a look and see that it's
already done with this task and all that
it needed to do um is is finished. And
similarly for another task that it
worked on, I can see this email from
Eric who is saying that um they're
pleased to have offered their
consultancy services and for the impact
our collaboration has had. Also finding
the invoice attached to the email and
yet again I can see that right here. Can
zoom in a little and look at all those
lines. pair consultancy service travels
cost technology infrastructure updates
all listed all with their prices and I
can see how did the agent do with these?
Well, just go to the next step right
here and I can have a look at the e
document and I can see again all of
those are listed. If I want I can view
the PDF right on this page on the
purchase invoice just to remind myself
what was it actually that was in the
PDF. Well, consultancy services, travel
costs, miles traveled, all of those are
in here as well. And yet again, the
agent has done an excellent job at
finding all the right accounts to put
everything into. And I didn't even need
to help it this time. So, that's about
it for the agent.
Thank you, Arita.
Yeah. So, what you've seen is the first
two agents that we provide. the sales
order agent which is in public preview
in mostly English-sp speakaking
countries. What we're doing now is
making it available in more and more
countries that that will come with every
minor more and more countries. So for
example for Germany we need to test that
it works that it can kind of converse in
German and that it can work with the
German localization. So it's mainly our
job is mainly to to test and when we're
confident it works we will release it
and you can use it. that will come.
We'll also be adding more capabilities,
for example, ability to handle PDF
attachments in emails.
For the payables agent, it is currently
in private preview with around 20
partners who are providing feedback on
it. Here it's a little bit more early
days. We are adding more capabilities.
One of the big ones we'll be adding soon
is um ability to match with purchase
orders which is a a way you know way
many companies operate. They create a
purchase order first
and then we plan to have it in a public
preview very very soon in select
countries meaning probably English
speaking countries because of the test
effort to to to roll it out to more
countries. So stay tuned for that and
we'll of course also add more agents
over time. But what you might be
wondering is when can you create your
own agents? And I just want to say we
working really really hard to enable you
to do that. We will have a private
preview of the agent playground what I
showed you
very soon in in July and this will be
for a very small group of partners
because we want to control it. But then
October is when we expect to have it in
public preview so that you can all play
with it. So have a bit of patience still
here. I want to end with some reflection
on why we think AI agents are such a big
deal. And of course it has to do with
automation. All the tasks that are
relatively repetitive that humans spend
their time on today.
Uh can we can we automate them? And it's
not like automation is a new thing.
We've been automating for years mainly
with by writing AL code. But as we know
that is both expensive and time
consuming. You need developers who write
the A code. They need to think about all
conceivable situations that can happen
like what if the address format is
slightly off? What if there are no items
available on stock or whatever. They
have to think about all these things and
write code to handle them. And it also
means that it can become fragile because
what if something unexpected happens
which is where agents
are better. But as a result of this what
we've done in the past many years is
automate simple processes like linear
processes where it's kind of mechanic
what needs to happen. We can automate
those. But what AI agents is going to do
is is really dramatically change this.
So as we've seen agents are intelligent.
We give them the whole UI of Business
Central and then we just tell it what we
want and it figures out how to do it. So
it can overcome situations much more uh
easily than if you were to write a code
for it. And so what we think will happen
not in the very short term but
eventually is that we will be able to
delegate whole areas of responsibility
to AI agents like handling all customer
communications like handling all invoice
processing etc etc. So this is this is
the direction we are going and it's
pretty exciting.
And with that we have 15 minutes for Q&A
and there are t-shirts for the first
ones as well. Can you throw that over
AJ?
I don't want to throw it. Yeah. Oh, you
need the microphone. You Who's first? We
have the queue. Okay. Okay. You don't
want to fine. One question. So, you hear
me? Okay. Um, you have the purchase
order and you give the general ledger
account number and then you can match
it. When will it be like that? You don't
give the agent this knowledge that the
that the agent understand really the
general ledgers and then you don't have
to give them the information in the
purchase order that he can only matches
and make it I'm not sure I follow. So
what what the reader showed is we get an
invoice in and we create a brand new
purchase invoice for it and so we
transfer all the lines that were on the
PDF and we also determine the right
accounts. Yeah. But you in a purchase
order you already give him the accounts
and you only have to match it and then
he knows the accounts. My question is
when do the agents really under
understand the bookkeeping and know this
will be their account. This will be the
account. So the really understanding of
the financial process. Thank you. Yeah.
Um so we can talk a lot about that but
it's also going to get a little bit
detailed but I will give you one minute
summary of what our thinking is around
the payables agent. So basically we will
use what you saw here was we use the LLM
to come up with the right accounts what
we think are the right accounts. What is
coming very soon is some indicating in
the UI that sells the user how confident
we are that this is the right account.
The mentality we have here, the way of
thinking we have here is you know how to
uh let's imagine this scenario. You get
dropped into a company that has existed
for years and you are asked to handle
the next invoice that comes in. Can you
do it? Yes, you can do it because you
can look in the history. How have
invoices previously been handled in this
company? It takes you a lot of work to
do it but you can do it. You don't want
to do those kinds of things. Agents
don't mind. they will actually be able
to you know scan earlier invoices that
look similar and there this is where we
get the essence from and so basically in
a way you can think of it as the users
are training it they're saying this is
the right account next time it will
notice
AJ now it's your turn
all right so a couple of questions I'll
ask one maybe ask you know give it away
and then come back for another one from
a visibility perspective and from From a
performance perspective, at some point
the penalty of having too many of those
agents is overflow. So from an interface
perspective, are you thinking about
creating some kind of a scroll bar if
you have too many? Then the other part
of it is from a performance perspective,
how does that impact is there have you
kind of done any testing at scale that
says after so many agents we're
expecting performance degradation or is
it really just like another user session
and it's really not impacting anything
significantly? you answer to yourself.
So it is really just a user session and
you know we have customers with
thousands of users and so having 10
agents is fine. It's not going to be
fun.
On the on the first question is about
the user experience. Do you want Yeah.
The first part we initially designed the
task pane using only our first agent and
of course as we get more agents you see
more avatars popping up. Of course we
work with accessibility. it all will
either reflow nicely, but of course
we'll also add the ability in the
copilot pane itself to choose which
agent you're looking at. So you don't
always need to go back to the RO center
and click on those avatars even from the
task pane which you can just open um
from the bar on top which opens the
copilot pane. You can switch between
chats and agents and then when you're in
the agents part of that pane you can
switch in the future between the
different agents that you have running.
So, so let me also give another
perspective on that because
the way this is going is
users will do less of the grunt work.
They will be more like managers of
agents. We're talking a little bit into
the future now, a couple years. And so
what we are playing with, what we
imagining is a UI. How would a UI look
if you were kind of a manager of agents?
So what we have now is will do just fine
in the short term but we're also
thinking about how it might look longer
term. Yes. A question about spam emails
and sales order agents. U can sales
order agents have any mechanism how
exclude spam emails from process? Yeah.
So, so the way it works today, uh, okay,
I'll say how it works today and what you
can imagine us adding later. So, the way
it works today is the sales agent will
read every single email that comes into
your mailbox so that you don't have to
manually swip flip back and forth
between Outlook and and business. So,
everything will be brought in and you
will then get this warning that the
reader showed that says this is probably
not relevant and you could dismiss it.
So what one thing we have discussed is
you know in Outlook you can have
indications of spam of like they might
end in your junk folder but they might
actually not um and we can actually use
that information. So what we might do is
have a setting that says uh don't
include those but it comes at a risk
because what if you miss it like it's
the same with your junk folder right
sometimes a valid emails ends up there
so it's a trade-off.
Okay. Yeah. So there's a lot of
questions, a lot of aims.
Um, so you we have seen a little bit of
AL code. We have seen a little bit of
prompting in the client. But when you
think about outside of business central
when you want to create an agent, you go
to copilot studio. Uh why the business
central agents are created directly in
the client.
I had a feeling that question would
come. So you can create agents in
copilot studio and you can create agents
in business central and it's not like
one excludes the other. I mean Kofi
Studio has a lot of flexibility. You can
integrate with I think there more than a
thousand connectors they have. So you
can do a lot there. But the there's also
benefits in having an integrated
experience like for example the delivery
mechanism of extension an app store app
source and the timeline that you see
which is fully integrated has some
benefits too. So what what we will do
though is you if you you're following
this space there's a new protocol called
A2A agent to agent. So you can imagine
and this is what we will pursue that a
copilot studio agent can interact with a
business central agent. So you can get
the best of both worlds.
All right.
I have question of a little bit under
the hood. I'm curious. Uh can you hear
me? Yes. Uh I'm curious how exactly
agent interacts with data. Do we need to
create function for each table? How does
it interact with custom tables? If you
want to build custom agent for our
solution,
it interacts directly with with with the
UI. So if anything you might want to
create pages that that show all the
relevant data. So which is also it can
also be you know beneficial uh if you
have an if you're building an agent that
actually needs data from many different
places. It can also help if you can
maybe create some pages that kind of
bring this data together um potentially
um but but I mean it it interacts with
it via pages and via the UI.
But for example, was shown that it can
select random sales order. How would it
know random from the UI? I think
it's an LLM. I I guess it just it's the
same as if you ask chat GBT. Here's a
list of things. Pick a random one.
That's essentially what it does at the
end of the day. Okay. You catch
[Laughter]
no just a simple question. I wanted to
know if he gets if he does any
integration with uh any approval
workflows or potential external ISVS
of approval workflows of external ISVS.
I mean so we have some built-in workflow
you know approval workflows in business
central already in the base app and so
what it might do but not in our scenario
but what what it might do is prevent the
agent from pressing the button like
pressing the post button let's say
because like any a user would also not
be able to and an agent is just a user
and so it would have to it would get
stuck there until somebody actually
approves and then it would be able to
continue as uh with respect to
integrating with third party solutions
ions. Um, that's a bigger question, but
I mean we saw we saw what extensions
like if extensions add fields and
buttons to some extent it can just use
those if it understands what they are
for. But there's a limit to how much you
can integrate at this point
to the left.
Okay. Sorry to the people in the back.
So, uh, this looks wonderful. uh and I
can imagine all kinds of different
scenarios where uh this would really
help a lot. Uh but I can also see that
uh the performance of this probably also
narrows that down a lot. Uh do you have
any like are you going to work on making
this faster um because that really
limits the the use cases for my
particular point of view. Yeah. Do you
want to ask or I've talked a lot answer?
Uh um well in terms of the the agent
runtime uh I mean we are restricted by
you know the LLM response times for
example um we do have work planned to
you know compact the the history of the
things that have happened as part of a
task periodically but you know of course
um if if you have large pages with large
numbers of fields and many steps uh the
the ultimately the prompts that get sent
are are going to be you know pretty
heavy uh in terms of tokens and uh it
could be slightly slow. So right now
we're also really thinking mainly about
the agents as something that runs just
in the background and you know whenever
you're needed it will ask you but it's
not currently uh at least not with the
two agents we have currently meant as a
situation where you click something and
you just stare and wait and then you
click on something again. Um because yes
it it it can definitely happen that is
is not only slow but uh like I mentioned
earlier uh there are going to be
restrictions in place also uh because
performance we will not be running you
know a thousand agent tasks in parallel
for an environment. So if you have a lot
of tasks uh a few of them might run at
the same time. Uh there's also the whole
quotota uh around you know AI usage and
so sometimes maybe you run out of daily
quota or something um TPD um but it's
more like of a background experience at
this point um for sure. Good.
So from what we've seen, I'm just going
to a conclusion that basically you
you're going to have custom RO centers
with custom pages that are provided to
the agents to have them have the ability
to improvise.
But for anything that um concerns bigger
amounts of data, you expect us to um
supply it with like custom actions that
it can take to actually work through it.
Because in your example, it was going
through the orders and you were telling
it basically telling it open this page
and then go through them, which works
fine when you have 10 orders, but you
know, we've got customers with like
50,000 orders and you can't expect it to
cycle through page and work through it.
So, at that point, you probably want us
to then implement actions like um check
orders for availability or whatever.
It's it's a really um interesting
question. How much should you change the
app for the agents? And how much should
the agencies do like a human would do?
If you have a process today where you
need to do something with 50,000
customers, what do what do users do?
What do humans do?
I bet the alien could do the same. It
would probably search or filter and so
on. But that doesn't exclude of course
that you can make custom pages that
would actually what we did what's what
we didn't show but for safe solder agent
we did create at least one page for item
availability which is the way you know
for a given item for given time how much
will I have on hand at this point and
that's can be achieved by clicking a lot
around in the UI but we actually ended
up creating a custom page for that
because it was more efficient and more
reliable. Just just a small followup.
Does that mean that the agent actually
can interact with the filters of a page?
Yep.
How is the licensing going to be? Are
there special agent licenses or full
users or Yeah. So, so the agents uh
don't require licenses.
So, there's no license requirements. But
the way way we will use a licenses Yes.
And any user can interact with them. So
there will be a a charge
but that is based on how much they do
not how not on licenses
how we are going to measure how much
they do. So there's it's all documented
but every incoming mail
the the unit of the currency here is is
messages h and every message currently
is one cent. So an incoming mail, I
think it's two cents. Correct me if I'm
wrong. Every outgoing, you know, mail
two cents. Every quote created five
cents. Every order created five cents.
So if you, you know, super like two
rounds will amount to
14 or whatever. I cannot do the 28.
Yeah. Yep.
Yeah. It has been defined. So you can
just go to the website to Microsoft
learn and see the price model. How are
we doing on time? One minute left. Under
one minute left.
One question.
Hello. Nice. Um for example um are the
instructions from the Microsoft standard
agents extensible or adjustable? I mean
for example handling individual new
fields in a different way. Sorry, I
didn't catch the second part.
Um the instructions from the Microsoft
standard agents um are those extensible
or adjustable? So, so uh they are today
they are not uh extensible or adjustable
but we want to do that. We want to
enable that so that you can actually
provide your own snippet second you know
separate that will also guide how the
agent does some you know does it work.
Okay. Thank you. All right. I think
that's it. Thank you very much. We're on
time. Thank you.
