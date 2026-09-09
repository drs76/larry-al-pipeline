# Transcript — Business Central Under the Hood 14: Building agents in Business Central

- **Source:** https://youtu.be/Vq9Nk6_uxmQ
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[music]
>> Welcome to this new episode of under the
hood. So in the previous episode, if you
recall, we we talked about the agent
runtime and how we have this platform
that allows us to
to implement agents in Business Central.
So today we are going to talk about
something that is also
around agents, right? And
we're talking about custom agents, which
you'll see something we've built on top
of this agent runtime platform. And with
me I have Nikolai today. Hello Nikolai,
welcome. Hi Vincent. Hi.
So let's let's start by
just setting the stage and if you can
tell me a little bit what what are
custom agents. You know, people might
have seen this other video. We'll put a
We'll put the link in the comments
for this other video where we talk about
the runtime, but
what what are custom agent? Tell me a
little bit what what what that is. So
the custom agents are the agents that
you can build in sandboxes
out of the box without writing any code.
Basically, you can log into the sandbox,
go to the agent list or use the avatar
from the role center itself.
Then you click it, you get a very simple
dialogue and you have a no-code
experience where you can define the
instructions, profile, and permissions,
and then the agent is ready to take the
tasks and you can use this tool to
quickly prototype and to try out the
ideas when you're building the agent. So
no code required at all. It is no code
required at all. The primary audience
that we are targeting are the
consultants, but this is also a
developer tool. So for all of the
developers that are listening,
you can share this video with the
consultants because I believe most
likely you will be using this tooling
together.
Building the agents in the future.
>> So we have we have some web already in
we have shipped already in in Business
Central. We have the sales order agent
and and we have the payable agent,
right? You've been working on some of
these agents, so you you know a lot
about it already. And and you've also
been working on the on these custom
agents. So So what is there any Tell
Tell Tell Tell us is there any relation
between these agents or are they related
somehow?
Yes, they are related because when we
were building the sales order agent
payable agent at the same time, we
needed to build the tooling to help us
to quickly iterate, to test, and to
build these agents.
And now because we want to enable also
the partner channel to build their own
agents, we believe that they will need
the same tooling that we needed
ourselves.
So the main goal of this project was not
only that you can specify a custom
agent, but that you can also quickly
iterate and test and troubleshoot. So we
see that this tooling will be used for
both quick prototyping, but also when
you're ready to build your own agent and
package it as an app, you will be able
to use this tooling to quickly test it
and to see if it works. So what Okay, so
what's what does it take to to do a
custom agent? You know, you said you you
just enabled it and but what's the you
know, what's
what's involved exactly? So the first
thing that the people will be doing is
that they will create an agent and in
reality, from technical point of view,
an agent is a user.
So the first item is to provide the
instructions, describe to the agent what
the agent should do. The second item is
to provide a profile because
profile will drive
the role center that the agent is
starting in. It will also drive how the
UI is looking like, which actions and
which fields are available to the agent.
And the third item is the permission set
that the agent will have assigned.
In the beginning, most of the people
will most likely use the super
permission set to quickly prototype and
test. Just to make sure every everything
is you know, the agent has access to
everything. Correct. We are doing this
ourselves as well. And it's
I would strongly recommend as well
before shipping
to take time to reduce the permission
set. Okay, I think we'll get back to
that. But so just to
Just to recap, you say so there's three
things
What are you saying that there's three
things required to create a custom
agent? Instructions,
profile, and instruction set. Sorry. Um
Permission set. Permission set. Yes. So
so
let's start with the instructions. So
these are the three things required,
right? Let's start with the
instructions. So what Isn't that so that
I think the instructions are
pretty much the the heart of the agent
because that's That's where you describe
what the agent is supposed to do.
So tell us a little bit about the
What does it take to
to create these instructions and how do
how do you create these instructions in
practice?
So creating an instructions a good
instruction set is an art in itself and
it has been changing a lot recently.
To give you one example, when we were
writing the sales order agent, the
instructions that we have written
I think in the minimum instruction set
contained three or four pages of words
text.
So with previous models, it was
necessary to write a lot of instructions
to specify each step individually, to
tell the agent to come back and check
the things. Well, the sales order agent
is also quite complex agent. It can do a
lot of things.
>> Yes. Right. But with the new models,
Yeah. it requires way less instructions.
So the recommendations that we have to
anybody starting with this
is to write as little instructions as
possible.
To give you an example, I was testing
and playing around with
samples
and I wanted to create an agent which is
handling returns and creating credit
memos.
The agent is able to create a full
credit memo
without any instructions on the full not
reduced UI.
I gave it instructions to create the
credit memo for a given customer, which
items it should return, and it was able
to do it without
>> simple like a few lines instruction.
Just the message that I sent it. Okay.
>> It was able to go and create a credit
memo. Mhm.
Now,
you cannot ship with this, right? So
people don't get the wrong assumptions
because in half of the cases, it will
post the credit memo
and in half of the cases, it will remain
in the draft state.
And the reason why this is happening is
because I didn't tell it what to do. Do
I want it to post the credit memo or do
I want the agent to ask me for the
review before posting?
>> [clears throat]
>> So then, you know, when I'm building
instructions, I say to the agent, do not
post anything.
Ask me for the review.
I can give the instructions generically
across all the tasks.
For example, I can say to the agents,
never ever post anything, always ask the
user for the review.
Or I can be specific about the processes
that it can do and specific points where
I want it to ask the user for the
review.
So it's a little bit like instructing
a new employee actually, isn't it?
Precisely. Because it's it's like you
know, you have to describe the tasks to
because that's what our agent agent
runtime or agent platform does. It It
acts as as a user as you mentioned
before. So So writing instruction is is
a little bit like instructing a new
employee, isn't it? Precisely, yes. So
the same things that you would say to
the employee,
you will say to the agent as well. So we
recommend that you start with minimum
possible instruction set and then you
start outlining the most important parts
of the step, test it, and then slowly
grow your instruction sets.
They should also be using the natural
language because from our experience,
natural language works the best.
So it's a it's a little bit like Is it
Is it fair to say that this this part is
is actually prompt engineering? Mhm.
It is no way,
but one thing that the
people that are watching this video that
I want to highlight is that
the instructions that they are writing
are going to be a part of a bigger
prompt. The platform is wrapping the
instructions that they write within a
much larger prompt.
Thus, the instructions that they provide
will get additional handling by the
platform.
>> [snorts]
>> One of the good practices that we say is
do not tell to the agent to use a
specific tool.
You can do this if you really want to
or if you see that the agent is confused
which tool to pick.
But for example, to pick a tool to
filter a list, it's sufficient to sell
to the to tell to the agent, go to the
sales invoice list and find all of the
orders that are open.
And it will go there, it will pick the
correct tool to filter the list, and it
will set the filter.
So I
Yeah, so you mentioned that
the instruction they they they end up
being part of a larger prompt. Correct.
So these larger prompts are usually
called system prompt or meta prompt
sometimes. And And I think it's
important to realize that most
AI
applications today, that's the way they
work, right? Like for example, things
like ChatGPT or
Copilot, when you when you ask question
to ChatGPT, there is actually there is
not just go just like we, you know, wrap
our instruction in in in in some other
prompt before we send it to the model,
ChatGPT for example does exactly the
same. You write You write my little
question, but then there's some system
prompt and meta prompt that you don't
see,
which wrap what whatever you write
and and and send it to the model. So
this is the way This is the way most AI
feature are actually
engineered, right? These days, right?
Correct. And one of the things that I
believe people using this framework will
really appreciate is that the security
is handled by us. So we will protect
against the
the prompt injections and other most
common security attacks that can happen
to the agent. Also, we will wrap these
interactions with the UI within the
Business Central and we will shield our
users from the prompt changes.
So, agent is going to navigate the UI
the same way as the user is able to.
It also has some additional tools that
it can use
which is making
which is enabling the people to easy
automate the scenarios in a rather
robust way. Yeah, so you make it a lot
easier than if you had to build this
from from scratch with some other kind
of tool. Or using your own models and
the outside tools. So, so that was So,
we talked a little bit about instruction
there. So, you mentioned also that for
for a a custom agent you need to create
a profile. What what is that What is
that required? Why do you need a
profile? So, the profile is needed so
you can limit the agent's UI.
Currently, the agent when it logs in
because it is completely mimicking the
user, it is going to log in, it's going
to get the user session,
from profile assigned permissions
assigned at the same time. It's going to
start from the role center. So, you're
deciding the starting point for the
agent.
Then the second thing is that you want
to limit the functionality that it can
access because this will give you some
additional stability, accuracy, also
safety.
And it will enable you to troubleshoot
in a much easier way. Yeah, so if you
recall from the from the other video
where we talked about the agent runtime,
the way the agent
or agent runtime works is that we show
the page to the to to the model and ask
you know what's the next step, you know,
what's what the next action the agent
should be taking. And if I understand
what you're saying, by having a profile
where you simplify the pages
to the task that the agent is supposed
to perform, you increase the
decrease the complexity
so the agent sees, you know, more much
simpler pages, right? So, and in a sense
it's also like we were just saying
before, it's like having a new employee.
If you just show them the full UI with
all the bells and whistles, they might
be confused.
But if you show them a simplified
version of it, they have a better chance
to kind of perform the task properly,
right? Exactly. And I'm very happy that
you used this new employee example
because one design rule that we are
following, which I would like to share
with the partners as well
is that anything that the agent is able
to do, the end user should be able to do
as well. Yeah, so actually Yeah, so when
you create these profiles, they are just
they are not they are just regular
It did exist before AI, right? Uh so, we
are following our mantra here. When we
were deciding how to limit the agent's
UI,
we know that the partners wanted to use
this functionality to limit the UI for
the new employees as you can mention
them.
And they had a problem that each time
when we release a new version, we are
adding additional UI. You can install a
new extension and a PTE and these
profiles were extremely hard to
maintain.
And for this reason, we added three
properties that are going to clear the
action
all of the actions that you have in the
UI, all of the fields, all of the saved
views, and you're going to get a blank
page.
And then through code, you can add the
fields and the actions back to the page
ensuring that this page is going to stay
fixed
forever, basically. So, so that wasn't
quite accurate that you say no code was
required. A little bit of code is A
little bit of code is required. Well, we
are also considering to enable this
thing through through the UI.
And possibly also to have some agentic
help to help you to generate these
pages.
You can also do this one easily by
exporting the existing profiles, seeing
which syntax is used there.
>> [clears throat]
>> And then you can use it as the example
to write your own page. It's quite
simple.
Yeah, so it's mostly declarative, right?
You don't need to write algorithm or
something like that. You don't need to
write a lot of code. It's mostly
declaring how the profile looks like,
right? It's possible to write code it.
And the important thing to mention to
people is that the code is supporting
more things than you can do in UI.
So, you're able to change more
properties through the code than you
would be able to do through the UI
itself.
So, this is a nice example of the
feature that we built for agents, but
also for the regular users that can be
used across multiple scenarios. So,
actually Yeah, so when you create that
profile for for for your agent, for your
custom agent, you can actually log on
with that profile if you want. Yes. And
see So, what what it would do is that
you would see then the pages
the same way that the agent sees the
pages, right? Exactly. And it can it can
even be a way to test that you have
enabled the right things and then you
didn't you know remove too much or
something like that, right? Yes, we do
this a lot of time when we are building
these profiles.
Another cool thing that is possible is
if there is an additional field that you
want to expose to the agent that is
coming from a third-party extension or
you want an additional field,
you can simply do it through
configuration.
So, even if the profile is reducing it,
it's possible to return the fields and
the actions back to the page through
configuration. So, that means even
though for example, you are consultant
and you ship a
custom agent
to to a customer, even though this
customer uses a third-party extension of
some kind that adds new fields, you can
still have the agent working and do
perform the task it's supposed to work
and even act on that field and all
whatever customization there is. That's
what you're saying, right? Exactly. So,
the agent is going to react on the
errors.
For example, if this extension is adding
a mandatory field, agent will react and
try to set the field. If it can't, then
it asks the user for the user
intervention.
In one of the demos we had for the sales
order agent, we added a small field on
the sales order. I wanted to gift wrap,
yeah.
And then
a user would send a mail and say I want
a gift wrapping. An agent would simply
pick up this field without any
additional That's the beauty of of AI
and LLM that they can deal with
ambiguity uh Correctly. As as as opposed
if you had, you know, if you had some
code running, you would have to change
the code and do something to kind of
take take care of this gift wrap thing.
Whereas LLMs, they can, you know, they
can reason on on these things, right?
So, so that was So, we covered we
covered instruction. We covered profile.
Is there something you wanted to add?
One additional thing that I wanted to
say on profiles. If you look at the BC
pages, to explain to people why it is
needed.
On the items page, there is 120 actions.
Pure vanilla W1.
And sales order has together with lines,
it has around close to 100 fields and
120 actions.
And you don't know what it is going to
be running on the target. So, in order
to you know, minimize its world,
it's best to trim the UI and then people
can return
Precisely. And people can return the
fields back through configuration.
>> with that number of actions, it's not I
mean, even a human would be confused,
right? Precisely. But agent is
surprisingly able to do most of the
tasks correctly.
By again, what? By reducing the the
complexity of these pages, you increase
the likelihood that the agent will do
the right thing and and and don't go and
and get you know, get lost in in in
various pages. We've seen We've seen
actually agents sometimes, some of the
agents we've been you know, trying to
develop, sometimes they get a little bit
lost. They go and and click around and
go to that page and they go, "Oh, no."
And then they go back and and you know,
and finally do the task right, but
that's not what you want. You want the
the agent to be as, you know, as
efficient as possible, right? Yes, and
coming back to our mantra, agent is a
user, is able to do everything that the
user can.
Think also of the agents as your
ultimate usability testers because if
the agent finds something confusing,
an end user will most likely find it
confusing as well.
When we were building the sales order
agent,
one of the task that was incredibly
difficult is finding if the items are
available
because before how it was being done in
the product is that you needed to
navigate through a lot of pages,
memorize the things in different places,
and then go back to the order and fill
out the items that are available.
And we would usually try you know, to
build an agent. In this case, we didn't
even try it because we could see that
it's not going to work.
And the solution is simple. We created a
single page where user can quickly enter
the name of the item. We will find all
of the similar items.
>> So, that's part of the profile of the
custom profile. No, this is not part of
the profile. We added a completely new
page.
>> Okay, you added a completely new page.
And we got the platform support for
smarter search.
And now when the user is typing a name
of the item, we are going to search all
of the available items. And on this
page, you will be able to see quickly is
it available or not.
And this gave us both high accuracy for
agents and we simplified one of the
common scenarios that was difficult to
do in the app. Okay, so what you're
saying is that
again, you know, you started by saying
no code is required, but but you can
also write a little bit of code and
create new object, new pages
if if necessary to help the agent a
little bit along the way, right? It's
the excellent opportunity to fix the
usability problems and bugs that we have
in the product.
Okay, so instructions, profiles, and
these profiles as you say now may may
contain possibly some new pages if if
required. It's not necessary, but
it might help you in some sort of
>> your product and this is the thing that
we would recommend to you. Mhm. To give
you another example, it was confused by
having two actions that had a similar or
the same name in the UI. Mhm. But the
end user would be confused as well.
>> Mhm. Because you wouldn't know which one
>> Good opportunity to rename this. So it's
a good opportunity to rename or remove
through profile, so you leave a single
action and then both agents and the
users And everybody is happy
Everybody's happy Machines and people.
Correct. So so the third thing uh the
third the third component of a of a
custom agent you mentioned was uh
permission set. Correct. So
why do you need a a special permission
set for for the agent? Uh it's a very
smart idea to limit the permission sets
and we recommend people not to use
super.
Uh this is a a strong security
recommendation because permission set is
the thing that is limiting your access
in the end.
Now, this permission set is usually a
task that you would do at the end and
then you would trim. When you have all
of the scenarios defined, you would trim
the permission set to bare minimum. Mhm.
Why this is important? Before I
explained why this is important as well,
I want to highlight one thing that
people miss. When agent is running, it's
going to run as the intersection of the
permission sets
of the user that gave it the task and
the permission set it has assigned. Mhm.
So it can never do more than the user
that gave it the task. So this is this
additional security measure.
So even if the agent has a super
permission set and I give it a task and
I don't have a super, it will be limited
by my permission set.
Now, why it is a good idea to limit the
permission sets?
I'll give you an example from the sales
order agent.
We have
written the negative test case where we
were expecting the agent to ask for the
user intervention. There was no customer
and we asked it to create a sales order.
Mhm.
And the test failed. It created a sales
order, which is impossible. Mhm.
And now the question is how did it do
it? It managed to navigate through
lookups to the customer.
It renamed the existing customers. It
changed its shipping addresses
>> Okay. and it repurposed the existing
customer to a new Okay.
Now [snorts] if you think about it, this
is something that the new employee can
do as well.
>> Yeah. Yeah, exactly. That's again back
to your
uh mantra about, you know, it's thinking
of the agent as a new employee. That's
exactly the same thing. A new employee
could actually do the same thing. They
do not know what is a consequence of
renaming a customer. Yeah. Which is
something that you shouldn't do in the
product. Yeah.
Now, if you limit its permission sets,
you are reducing the possibility of
these things to happen significantly.
They are quite unlikely to happen, but
it is good to be as safe out of the box
as you can.
Because if the agent should not edit the
things, remove the edit permissions,
also delete permissions from it.
And we are also have started working on
changing the way how we are writing
instructions permissions and how we are
handling permissions in the product. We
are moving more to these indirect
inherited permissions and also elevating
in them through the attributes as the
code is running.
So the main idea is that you would
control few objects
and then based on the flow that it's
running, you're getting your permissions
as you would need to complete this
specific flow. Mhm. Okay. Yeah, so
that'd be a yeah, a good addition to
to this whole agent framework, but also
for you know, to in general creating
creating permission set would be a lot
easier this way. Yes.
So let's talk a little bit about So now
we we covered, you know, the three three
components of the of the custom agent.
Let's talk a little bit about it because
people are often wondering about models
and you might when models do it actually
choose, does it matter what model do
they have? Can they control Can can the
the consultant or partner who who are
going to make to to make custom agent,
can they control which model the they'll
be using? Is that important?
So they cannot control which model they
will be using. The models are decided by
us and we are the ones that are updating
the models as we go. We are following
the rest of the Microsoft because
Microsoft is operating the models and
slowly moving away from the old models.
So there will be a notification to the
partner community when we decide to
switch the model. There will be some
time to test and to prepare.
But our goal is to make this completely
irrelevant to the partners. So you
should not be thinking about the model
change if your instructions are going to
continue working.
The
platform should shield you from these
these changes. So we know from
experience that
you know, we have as you mentioned
before, we have this meta prompt or the
system prompt and when we change model,
we actually have had to do a little bit
of tweaks to these, right? I believe we
mentioned that in a previous video.
Correct. Uh so so so it's like any
third-party kind of library you're
using, you know, it's
you change it, sometimes there might be
some changes in the API.
Well, the same goes for model. The the
equivalent of it being the prompt,
right? The prompt might need to be
adjusted a little bit and our our
intention is to try to shield uh you
know, the the the people who will author
this custom agent from these changes. So
as we will
upgrade to better models
uh we'll do necessary changes in the
prompt so they don't have to worry about
it and they can focus on the
instruction, which is basically where
the business logic is,
the business value is, right? So they
don't have to worry about
some intricacy in the prompt engineering
or specificity of models, right? Yeah,
it shouldn't be necessary to optimize
the prompt for the given model.
Now with this said, we are also having
our own
nice tools that were added to the
instructions.
So if you're writing instructions, check
the official documentation because we
have added additional features that you
can use.
For example, if you have a complicated
page and you would like to add some
page-specific instructions, there is a
syntax that these instructions will be
only included when this page is open.
Okay. Also, you can structure your
instructions in a way that it reflects
the timeline. So when the user is
reviewing the things, they can see these
reflected in the timeline. So there are
some product-specific things that we
have added. But it's still natural
language, right? It is still a natural
language.
>> There's something you would put in
instruction, but that would trigger a
certain behavior of the agent runtime,
right? These are not really natural
language ones because it's a specific
syntax. Okay. So for page-specific
instructions, it is something like curly
braces percentage if page equals this
Got it. curly braces and then end if.
Okay. So but the but these these are
still just plain text you put in the
instructions, right? Correct.
>> Yeah. So it's this still not coding.
It's still not coding. Yeah. So so it's
just a a special syntax that instruct
the agent runtime to do something very
specific. But we document all that,
right? Correct. Yeah. So check out the
official documentation.
We will have the examples and samples
for these specific things that we have
added to the instructions framework.
Okay. So
what So
um for the people who are watching this
video, they they maybe they want to get
started and and let's try try it out and
and try to to author custom agent. So
what what should they start?
So to get started, get a sandbox and
when you log into the sandbox, you will
see a small icon with a plus that helps
you to create a custom agent. It will
open a simple wizard
that you can use to define instructions,
set the permissions and profile.
You don't need to spend much time on the
permission because there is a dedicated
UI that can help you to write the
instructions and run the tasks at the
same time.
It requires you to set at least some
permissions to allow you to continue,
but there is a dedicated UI where you
can change the instructions and run the
tasks at the same time. So very simple
to get started.
>> Precisely. And you can also access it
from the agents list. There is an action
to create a custom agent, which will
open the same setup dialog, which you
can use and get started. Do we have any
samples that
that our partners and and consultant can
look at? Yes, we shipped one sample. It
is called sales validator. Mhm. It is
basically checking for the open sales
orders if they are ready to release and
then it releases them.
And you can check out this sample to see
how we've written the instructions and
profile
and everything. We are working to ship
more samples.
And one of the samples that I'm looking
at at the moment is writing these sales
return agent, which is quite an
interesting scenario.
Which brings to a very important topic
which we are discussing a lot with
partners. What is a good agentic
scenario?
So
what is a a good agentic scenario? When
when is it When when should partners or
consultant go and say, "Okay, I'm going
to create a custom agent." What what is,
you know, can you give me examples or
yeah?
As opposed to just write code, write an
extension as they as they do today,
right? Yes, this is one of the questions
that we are getting a lot and we are
also discussing this a lot internally
within the teams.
Because you have many tooling available.
You can write AL code, you can use the
co-pilot, you can maybe use the co-pilot
studio and integrate with the R APIs and
you can also write the agents.
So the question is when should you use
what?
And my recommendation to all of you is
to use the best tool for the job, right?
Which I know it's not helping much,
right?
But to define what is a good agentic
scenario, it's a scenario which has a
lot of variability, where you need the
agent to go and to do a specific task
potentially in different ways.
It can also be something that you're
doing less frequently and you it is an
ad hoc task that you would give to a
colleague because you don't want to
spend time on it.
And to give you a perfect example of a
good scenario that we are looking at, as
I mentioned this returns agent.
Out of the box, the platform is enabling
me to analyze the attached PDF
documents.
If the customer has attached any images,
we can read the text from them.
And with only instructions, I'm able to
create an agent which is creating credit
memos, fills the work description, and
puts all of the things that customer
wants to return.
One of the example is that the customer
has ordered 15 items and they want
chairs and lamps
to return them because chairs were
damaged.
It's the agent is able to tell which
item is a chair and which item is not.
And which item is a lamp and it does a
good job with really high accuracy
and it creates a credit memo in a good
way.
>> Yeah, so what what what you mentioned
earlier that there's some variability
that's you know I get that that agent
are able to you know as opposed to if
you write code the algorithm is usually
pretty
fixed pretty static and even you can
have some you know if this then that but
but you know
at a certain level of complexity there's
maybe too many you know branching so
which that's where agent are really good
because they can handle that kind of you
know variability as you mentioned but
another thing that the
that is worth mentioning
is that LLMs are really good with
anything with language. I mean they are
called large language model, right? So,
for example you mentioned you know
looking at a PDF and and extracting some
information from that or sales order
agent receive mails and is able to
transform what the what the what the
customer is writing into actually
actions in the product and and even
author replies to the customer. So,
these things are it would be extremely
difficult to do these things or if if if
possible at all and
to do this in code. So, Exactly. So, in
your scenario if you if you spot things
like that these are also good indicators
that
you have a potential agentic scenario.
Exactly.
One of the things I grow this scenario
even further, I said to the agent we are
in Denmark and I would like you to
follow the Danish laws when doing the
returns.
>> Yeah. And then I created a invoice which
has food items in it together with other
articles
and I use the local brand names like Dan
Bowl or something.
It's able to tell you which product is a
food and it's also able to tell you that
by the Danish law this is a perishable
goods
that you do not need to return if you
don't want to, right? Because food
returns can be rejected.
>> Yeah, that's a good point. It's also
also something you can leverage from
LLMs. They do have a lot of knowledge
about you [snorts] know a lot of things
you know that you you don't want to code
that either you know
because that's like they have you know
so much knowledge
just readily available so you can ask as
you example what what kind of food is it
you know what what is a law around this
and thing like that.
>> It knows the local products which many
people don't know
and it's also brilliant working with
languages.
Sales order agent is able to take and
understand the emails in different
languages and reply [snorts] in the
user's language. So, there are many
scenarios that you can use where it can
combine both the data within the PC
and the data that is coming from the
outside because it has the outside
knowledge that would be hard for the
user to
look up and understand in many cases.
The second set of good agentic scenarios
which many people overlook are these
scenarios that you do once in a blue.
So, for example issuing reminders and
chasing people that did not pay you.
It's very difficult from AI point of
view to code reports that you can run in
multiple ways
especially if you need to chain up
multiple processing reports.
We have written this UI in the past.
It's a bit difficult to write and it's
difficult to use. With agentic scenarios
this is a brilliant use case because
agent is able to do this with high
reliability.
You can ask the user to review the work
before proceeding and running next
report
and it's going to cost only few dollars
a month to run.
So, it does not need to be something
that is very expensive out of the box.
The company can make a small investment
of 20-30 dollars a month and get their
scenarios up and running. Oh, pretty
cool.
So, what what is the what are the future
of
of the custom agents? What what what are
you working on? What what's next with
with the customer custom agent? So, for
what's next, we have not mentioned this
a lot during this talk. We are also
releasing the SDK and the SDK will allow
partners to build and ship their own
agents. You can build some really nice
user experiences with review setup where
you define instructions and you can
release your agents.
Then the second item that we are going
to be looking into is giving you the
ability to test your agents
which we will be releasing quite soon.
So, this is the work that we are
starting now.
But that's maybe a little more advanced
than than just writing you know
instructions. That's maybe that's that's
for you know that kind of the advanced
type of agents, right?
>> This is why this video is for both
consultants and developers. Consultants
will start with prototyping and
developers will take on the task by
packaging it, testing it and releasing
and maintaining these agents.
The second thing that I wanted to say is
that we have a lot of items on the
backlog and we are really looking
forward for your feedback what to
prioritize because we are going to use
the feedback that you have to prioritize
the items that we will be working on.
All right, thanks Nikolai. I hope you
enjoyed this video and yeah, go and try
it out. Go and play around with your
custom agent and
you know I'm sure you'll find
you'll find it useful and and and as
Nikolai mentioned give us some feedback.
We look forward to it, right? Thank you
for watching.
Thank you for watching as well.