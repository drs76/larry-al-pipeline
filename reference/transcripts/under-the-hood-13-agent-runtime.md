# Transcript — Business Central Under the Hood 13: Inside the Agent Runtime

- **Source:** https://youtu.be/nPF84Ufkn4k
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[music]
>> Welcome to this new episode of under the
hood. So today we are going to go really
under the hood. And we are going to talk
about our agent runtime. So as you know,
we we have a few agents already in
Business Central, the sales order agent
and
and the the payable agent. And they all
build on what we call the agent runtime.
So today with me I have Esteban. Hello
Esteban. Hello Vincent.
>> Esteban, you have been working on the
agent runtime for a while now. So you
kind of it's fair to say you were there
you were there in from since the
beginning of it and there was in the
inception of it. So just
we talked about it earlier but just as a
quick reminder what what is the agent
runtime? What does it do?
Um right. So
the agent runtime is is the term that we
use for what is essentially the
foundation
of agents in BC.
Uh and it's what everything else builds
uh on top of. Um
so there would be three parts to it I
would say. One of them is the underlying
data model.
Um so all the tables
for storing your agents tasks, keeping
track of what agents are doing. Then
there is the agent task execution engine
which is really the
the heart of it.
>> main part of of the agent runtime and
why we call it agent runtime. And then
there are some
you know, supporting or auxiliary roles
the the agent runtime assists in for
example, when you are using agents in
the product and you use the the timeline
view. Mhm.
Uh the underlying data model
and preparing the data for the timeline
is also something that the agent runtime
is responsible for. Mhm. Okay,
[clears throat] that also and so both
both our agents, both the sales order
agent for example and uh
and the the payable agent they are both
built on top of that, right?
Uh right. So there is I would say maybe
another layer which is you know, the
agent SDK that allows you to then sort
of build your agent apps. And then the
SDK is using the the runtime components
underneath.
So what's the what's the principle of
it? What's the heart of it?
We we talked a little bit about that in
some earlier videos but maybe it's good
with a with a refresher.
So the the way agents work is
for example when when anyone signs in to
BC on on the web browser, right? Usually
you sign in and you see the role center
and you can click around and new pages
open.
Um [snorts] what is happening there is
that your web browser is issuing
requests to the BC web server.
But the BC web server is is not actually
responding with with that HTML and and
CSS and and JavaScript. Instead it it
has this JSON based API
uh that we call the the logical client
API that provides all the information
necessary to then display it to users.
So it it has all the information about
your current page, the fields, the
actions, the tooltips and then there is
a component on the client side that
converts that into into the final HTML.
>> So that's the kind of the logical layer
logical representation of the page.
>> of of the page and then you have the
>> have had that for a long time. It's
prior to AI and all these things. That's
a that's an old
framework so to speak we have had for
for a very long time. Right. Right.
>> Actually in the old days when we still
had the Windows client, we had these we
still had that and and we we had the
ability to
to transform this logical page into
either the Windows client which we like
the you know, the old days Windows
control or the browser. Uh actually
today the mobile client is also based on
that technology where we transform the
logical layer into a more mobile
friendly pages. But that has nothing to
do with the other that existed for a
long time, right? Yes and and we we
didn't really need to reinvent the
wheel. Right.
>> Right because we had this API that
allows us to interact with the product
and that gives us all the information we
could need, right? Everything that a
user needs to work in BC
it's the same information
an agent or or an AI would need.
So so the way agents work is they use
this API
and they are also similar to how a user
is presented on the web browser or the
app. They are also presented with some
representation of say the current page
and the controls on the page, right? The
fields, the actions.
Um and then
there is
um
some additional you know, guidelines on
how to interact and there are some some
tools that represent various
interactions.
So a tool for example to set some field
to some value or to invoke one of the
actions available on the page or close
the current page etc.
And the AI
or the the LLM in this case is
internally then deciding okay, based on
the page I'm on and what my instructions
are
as whichever agent is running, what am I
going to do next? Right? Do I need to
edit some fields? Do I need to navigate
somewhere or invoke some action? And so
that is the
That is the heart of the agent.
>> Yeah, basically the the heart of how it
works. Now
there is of course a lot more around
that. Agents
or these prompts to be more specific,
they do need some additional context.
The the agents need to be able to also
remember certain things. For example,
when you're on the product and you're on
the customer card page and you can see
information about the customer. But once
you close that page you can't see that
information anymore, right? And
>> But a human would maybe remember some
information.
>> might remember it, might copy it
somewhere, might write it down. Yeah.
Yeah. Um and so agents need to also be
able to do something like that, right?
So they need to be able to to remember
to say oh I I should actually write some
of these things down because I need them
uh later on. I I know what my
instructions are. I know I'm going to
need this. So they need to be able to to
remember some information
um similarly
>> summarize what you're saying so far,
right? Just so everybody can you know,
follow. So we the at the heart of the
agent runtime, what we do is that we
take a page and in in a logical
representation but still it's a page
pretty much like a you know, almost like
a user would see we show it to the to
the AI, right? And we this and and then
we ask the AI here is a set of tools and
these tools can be you know, as you
mentioned click on an action, fill out a
fields,
things like that. And we ask the AI
okay, what what what's next? Yes.
>> typically in a in a in a task execution
say for example in a sales order agent
you would start maybe on the role
center.
And then so that's what the agent sees.
And the agent has and I'm just you know,
kind of you know, trying to go through a
a an exa- an example of a workflow of a
flow, right? And the instruction be
create a sales quote, right? for a
certain number of items. So maybe the
first thing with the the agent would see
is okay, I'm going to go and search for
these items. See if they are available.
So they would click on that page. Mhm.
And that's it. That's the first step.
And then next next step would be here's
the page new page which is the item
search, right?
Uh and then it would go okay, what do
you do now, right? And so forth, right?
Right. And and you mentioned something
also important that
it is it it is doing one thing at a time
and so it is also important
um
to for it to know okay, what it has it
already done
>> Yeah. because depending on instructions,
right? It it might currently be on some
page.
>> Yeah. Yeah. Maybe even a page it it
doesn't necessarily expect to be on. So
it has to understand well, how did I how
did I get here? What what was I doing so
I can Yeah, so maybe what's important to
to point out actually is that I don't
know if many people know that but when
if you do a pure call to LLM LLM it's
it's it's completely stateless. Like
every time you do a call to an LLM you
get a an answer
but then the next next time you're going
to call an LLM it doesn't remember what
you uh what you actually asked before
unless you provide you know, the the the
history of the conversation. So so what
I think fools people sometimes is that
when they use things like ChatGPT or
Copilot, there is on top of LLMs there
is actually an application that does you
know, some of the things you mentioned
actually where that builds a memory of
the conversation and for every call you
get the whole history you know, together
with you. So we've built something
similar. We built some kind of a memory.
That's what you're saying, right? Right.
So so when you're using one of these
like chat based systems for example and
you send a new message, it's not just
sending that message somewhere, right?
It has to send
the entire chat history or
some ver- some version of that yeah,
yeah. So that an LLM can know what to
do.
Uh and we well, yes we do something very
similar to that. So you mentioned yeah,
you for example we have some memory in
that sense that um
the agent runtime remembers for example
where you have been, which page you come
from, right? Yes.
>> What else?
Uh well, it remembers search results for
example. So in in your example if you go
to the item list and search for some
items, those results will be
automatically remembered. It can also
just decide to, so the LLM is given a
tool
where it can basically just write
something down. Um
and it then has access to that
information.
>> Like say, you can if you really need to
make make some notes, just you know, put
them there. Yes. And that and that will
that means we will put that in the next
prompts.
Right. So, the next iteration of this,
what is essentially a loop,
would then have
still have this information. Um to to to
some extent.
Um and and yeah, so that's that's
in the end how agents perform their
work. Now, of course,
an agent can like an LLM can just say,
"Oh, I I would like to set this field."
Right? So, then of course the there are
components in the runtime that now have
to go and set the field and translate
this into actual Yeah. All right. But
that's just kind of the mechanics of it,
right? Yes.
So, okay. So, that's the that's the
heart of that's that was our basic you
know, our ground idea on how to do this
to implement this
this agent work. That's the
ground design of it, you you could say
in in a sense. But but that and that's
that's what we call execute task. This
particular
uh state
>> That particular prompt or But there are
but there are other it's it's not the
only thing that's going on in the agent
runtime. There are other So, this is one
this is one prompt essentially for that,
right? Uh but there are other prompts
and other things that are going on. Can
you tell us a little bit about that?
Yeah, sure. Um so, if we're talking
about prompts, um there's a lot of um
auxiliary work going on as well. So, for
example, you when you're working with an
agent, you have tasks and those tasks
have input messages. Kind of like a chat
or if you think about the sales order
agent, a new email coming in. So, one of
the things we need to do is analyze the
contents of that email and determine
does it have anything that is is
harmful. Mhm. Right? Harmful could be
specific type of language being used. Is
it violent? But it's also things like is
it trying to to to bypass
you know, what the agent is supposed to
do?
>> Like get access maybe to data they
shouldn't have access to.
>> Exactly. So, we have to do this type of
analysis and so we have various analysis
prompts, not just on input messages, but
in various other situations. Similarly,
um an agent might decide to create an
output message. So, think about uh
replying to an email. Mhm. And there we
also have to perform some some checks.
Uh something maybe as basic as is is it
in the correct language? Uh but is it
using the right formatting for for the
numbers and is it using correct dates?
And also very important is if if it
contains data, is that data actually
grounded in something the agent has
seen? Mhm. So,
back to the item list example, if the if
the agent were to go and search for some
items and then reply with a completely
different set of items, that wouldn't be
very good, right? And LLMs can at times
hallucinate. So, there's various
validations at different points that we
perform to to ensure that we minimize
So, what what you're talking about I I
believe is called grounding.
Uh can you can you maybe elaborate a
little bit on this because that's a
that's a very important technique when
you when you develop AI application, uh
grounding, right? So, we do some of
these grounding. Can Can you elaborate a
bit and maybe even give some examples?
Right. So, well, grounding basically um
when when an LLM generates content, um
you you want that content uh especially
if it contains data to to be grounded
Mhm. on the data. So, so usually what
you can do is um
separate from the prompt that is
generating this content, have a
like an evaluator, right? A a different
[clears throat] LLM prompt um
that is now taking this content and it
is not tasked with generating that
content.
>> Its job is to you give it the data, you
give it the content and it has to
figure out whether the content that was
produced actually matches the data. And
they're pretty good at it. So, they
actually So, instead of running one call
to the LLM, you actually do two, right?
So, you do first you do generate that
content. Say for example, generate a
mail, right? And there's some in your
example, there might be some data in it.
And then you have a second call with a
different prompt that say, "Hey,
>> Right. take that mail and here's some
data, make sure that mail contains
this data, which is a second prompt,
which is a basically the grounding
prompt, right? Is that is that how it
works? Yeah, I I mean, you can say it
contains this data or you can say it if
if it contains data, that data can only
be something that is here. Yeah.
So, this is what's called grounding
because you make sure it's grounded in
the in the data. Okay. Yeah, that's a
very common technique actually. And and
it is very very important, especially if
you're thinking about an ERP system and
Yeah. something that handles, you know,
sales orders. Yeah. We must make sure
that
>> Absolutely.
things are grounded. So, what are the
prompts is there
we talked about three or four and then I
think by now. Is there other other
prompts going on? Are there other things
going on in the agent runtime?
Um sure. For example, um
some something else that can happen with
this process of I'm doing one step, now
I'm doing one step, is it an agent can
get into some loop where [clears throat]
due to maybe some token repetition in
your prompt or something, the LLM is now
constantly either replying with the same
tool call every time or or bouncing
between two or three things in in a loop
that are not expected. And so, we also
have to run things like loop detection.
Uh which is is is not that
straightforward because you might have
agents that are doing things in a loop
and are supposed to do things in a loop.
>> repeatedly. Right? Things that look very
much like, "Ooh, it's doing a loop." But
that's expected. So, [clears throat]
there we we also use prompts um
to to detect if it really is a loop.
And and then we try to give the agent a
chance to get out of it on its own.
Right? We don't want to immediately fail
or or something because often times you
can just give a hint. Uh you know, nudge
and and
>> "Hey, are you sure you're not stuck in a
loop? Maybe you should try something
else." Yeah, and and people who have
worked with maybe other agentic tools,
etc. might have seen this. Right? You
sometimes you just provide a bit of
feedback and it continues, but we we
want to avoid that
a user having to do that. So, in some
cases we act as the user in the runtime
and say like, "Hey, I think you're in a
loop.
>> Mhm. This this doesn't, you know, look
like you're progressing. Try to get out
of it." And so then the agent has a
chance to get out of it and if it is
unable to, then we ultimately have to go
and ask a user to to intervene, yeah. to
intervene and and look at what's going
on. Mhm. Uh and it's a very similar
technique that we follow, for example,
with validation errors. So, the agent
might be setting fields and it might
have used a a wrong format or something
that was unexpected and
you can get validation errors, right? On
pages. Um and so the agent always has
the opportunity to also fix things. So,
might make a mistake setting some field,
gets an error, then Yeah, then try again
with some different inputs or something,
yeah. Yeah. But actually that's not too
far what from what a human would do in a
sense. Yeah, exactly.
>> Both in the loop thing or even in the in
the in a in a mediation or type of
scenario, right?
Yes, and and since you were asking about
prompts, then I guess one final area is
is the the timeline that I mentioned
earlier. So, when you are using the the
timeline in the product and you have an
agent that, for example, has to create a
sales quote, um creating the sales quote
might involve setting various fields,
adding sales lines, and these are many
different steps, right? Cuz the agent is
doing one step at a time.
Uh but to display this in a nicer or
friendlier way, we have these grouping
uh of of various steps into some
logical operation that makes sense like
create sales quote. And so, preparing
these, grouping these steps for
uh display in in the timeline is also
something that the runtime does. As it's
executing a task, it there's a
combination of, you know, some
deterministic rules plus some prompting
to determine how how we group these
steps in a way that
makes sense to Yeah, so we don't want we
don't want to display all the single
clicks that the and and and fill
that that the agent has filled out
because that would be much too
much too much information and and not
very useful for you. So, we're kind of
summarizing these into uh into some
more, you know, coarse type of
operations like say, you know, we we
created a sales order, we sent a mail or
something like that, right? Yes. So, you
you can always see these steps. This is
all logged and you have access to the
agent task logs in the product. If you
want to, you can go through every step
the agent did, but it is not the default
experience. Yes, it's not what we show
you. It will be too much to to show you.
We just show a condensed view of what's
going on. But still the user can see the
progression of what the user has been
doing at the this or the agent has been
doing well. Yes, that's right. So, I
believe we have all in all, correct me
if I'm wrong, but the I think we have
something like 11 prompts. So, is that
true or or maybe we have more?
Uh, I think
nowadays maybe it's more like 20. Okay,
really? Some of them that aren't used
very frequently, but that are there for
All right, so yeah, just to say
there there are many prompts and many
different ways we use the No, it's not
only as we as we
talked about before, there's the heart
of it, which is really
acting on the UI and clicking around and
filling out fields, but then there's all
these prompts around and and things we
want to to have all these things, you
know, do what what it's supposed to do.
Yes, and of course, all these prompts
vary in complexity, right? Sometimes we
just have a very simple small prompt
that is is used for simple tasks that
are still tasks that an LLM is better
suited than
deterministic groups. some deterministic
code, uh, but overall we have about 20,
I believe, right now. Is that Is that
fair to say that the execute task prompt
we
talked about before, that's the more
complex That's the most complex of them
all. By far. Yes. Yes, that is the the
most complex and
it's the
biggest one. It It's quite dynamic,
right? Because it grows as the agent
does more steps, etc. So, the size of it
is is very different depending on what
you're doing, but it is the most complex
prompt we have.
So, what about models? Let's talk a
little bit about models.
We We are using We're not using only one
model.
Uh, the runtime is using more than one
model.
Um,
yes, so
we some of these prompts, especially the
simpler ones, we usually use the
sort of mini Mhm. uh, version of the of
the model family, and then prompts like
the execute task prompt, which are more
complex, uh, use the full Mhm. uh, you
know, uh,
maybe slower, but better, uh, model. All
right, so the small Using small language
model is actually, uh, you know, a great
thing to do because it's, um, you know,
not all tasks require the full power of
a, you know, an edge model or
a big model like, uh, a 5.2 or
even the, you know, four models. Uh, so
so simple things like, uh, summarizing
or
even maybe some of the grounding, uh,
things can be done on smaller models.
This was faster and cheaper, right?
Yes. Yes, they are They can be
considerably faster and and they are
cheaper, of course.
Um,
so yes, we we have, you know, all these
prompts have various tests with various
scenarios where we expect them to work,
and we we always
evaluate um, you know, does does the
mini version of of this sort of model
family
uh, do a good job? Then it's fine, then
we'll just use the mini version for that
prompt.
So, you did some experiment with, uh,
various models, especially on the
execute task. Uh, we we did try some of
the
Uh, tell us a little bit about it. You
did talk You tried some of the reasoning
models, some of the, you know, bigger
models, smaller models.
So Yeah, so in general, we have been,
updating which model we use, um, or
models we use in the runtime ever since
we started. I
Honestly, I think the very first
prototype of what could possibly become
the agent runtime, I think was still
using GPT-3.5 or something.
Very shortly after we moved to four, and
and that's where we started, then we
upgraded everything to 4.0 and now 4.1,
and 4.1 is where we currently are.
Um,
but it is also something we are always
reassessing, and we do evaluations. So,
when,
uh, 0.1, I believe it was, came out, um,
with reasoning, um,
we we tried it. Uh, we were very
interested to see
how much things would improve if if we
had a model that could reason.
Um, what we found, uh, back then was
there was a significant increase in in
latency.
Yeah, so it's a lot slower. Reasoning
models, especially if you want them to
reason more, they are considerably
slower. And when you think about a
system where an agent is performing many
many many steps,
this That
really increases the overall task
execution time, and we didn't
Like in our experience, and for our
particular use case, um, in the execute
task prompt, for example, we didn't find
that it was much better Mhm. at doing
things. Um,
we did a similar evaluation then with
GPT-5 with reasoning, also with tweaking
the the reasoning effort, right? You can
make it reason less, and it will be a
bit faster.
Um,
so far we have not found, uh, any
immediate benefit. benefit for our use
case, but we are constantly evaluating
and thinking, um,
when it makes sense to to switch to a
newer model. I think people can get a a
sense of that if they are using ChatGPT
or Copilot that, you know, you can in
ChatGPT, for example, you can enable the
thinking mode, and then you'll you'll
see for the same question, it takes a
lot longer uh,
to to get an answer. So, that's, you
know, exactly the same we are
experiencing. We It's the the way you
you tell the model, now you you need to
think a little longer on
on this question. And and for our
application and for the agent runner,
that might not be as you say, that might
not be If you don't get any benefit from
it
in terms of better accuracy uh, or
better results, then there's no point.
We can just as well use a smaller,
faster, and cheaper model, right? Yes,
and and and the
we
especially in the runtime where we
control the the LLM requests and every
step, um,
we might have a combination
eventually, you know, where every once
in a while we reason, Mhm. um, and then
we continue with a smaller model, and
then we reason again. Mhm. Or things
like that. But this is all
Everything around the LLM space moves
really fast. Mhm. Yeah.
>> And we are also constantly, um,
evaluating and adjusting and updating.
So, So, when when we when we we talk We
can talk a little bit about the how we
evaluate these models,
uh, about a little bit about accuracy.
You know, when when we, you know, you
were mentioning uh, you know, we tried
this model, and we we can see it's not
better. So, how do we know?
Can talk a little bit about that.
Yes, uh, we we have, uh, various tests,
um,
for agents,
uh, where
we
in the case of the agent runtime
specifically, we what we do is we
basically
spin up an agent, we create an agent
with some instructions based on the
scenario we are testing, and then we
just run the agent, we have some test
data, and we have some expectation on
how the agent on what the agent is
supposed to do, what the outcome is
supposed to be.
And we have many of these many of these
tests.
And the more important thing, first of
all, is is making sure that the tests
don't break when we switch to a new
model, which,
uh, you know, one one would think that
switching to the new better model is
like it's just going to be better.
That's not always the case. Sometimes
you you have to make some tweaks, and
otherwise things that were working don't
work anymore with again with our
specific
prompt and how we use it. So, some
tweaks,
uh, where?
It It depends on where it's failing, um,
somewhere maybe in in in our execute
task, or maybe now some validation
prompt is not
working anymore in some situation with
the mini version of the new model.
>> you go and tweak the prompts actually,
or sometimes also?
When we are moving like working on
evaluating moving to a new model, yes,
because we we have all these tests that
we we know are working, and we expect
them to keep working. And if those tests
fail, that's an indication that
we have to tweak something, uh, if we
want to move to that model.
Um, but anyway, so these these tests
that we have, they they're split into
categories like accuracy and and and
challenge. So, accuracy, uh, would be
the regular tests
that most systems have of these things
are working, something breaks here,
something is wrong, right? And challenge
tests can be more more complex scenarios
and situations where we know that the
runtime can currently struggle. There
can be various
more complicated interactions, longer,
uh, processes, uh, that we know we have
some work to do, and of course, our goal
is to always make more of those tests
pass and and pass reliably.
Um, and
>> Another Another way to look at it is
maybe to say, okay, these we have these,
uh, tests which we which cover the
scenarios we we support, all right? We
know that the agent can do that, and
that's also what what we document to
some extent for for the agents we ship.
So, we have tests for these, and then we
we are aware of, as you mentioned, we
are aware of certain more complex
scenarios which we know that the agents
are struggling with. So, we are
measuring on that as well, because if we
only measured on the the one which have
the higher accuracy, we would we
wouldn't we wouldn't know if it the
model gets better, uh,
because because for Let's say you have a
98% accuracy, and we we get a new model,
you know,
and then we just still get 98% accuracy,
you don't know if you get better if you
are at the top, right? So so that's
where these more challenging
uh, evaluation makes sense, because if
you have, you know, some some things
that only show you, let's say, 40%,
uh, then you would expect to see an
increase here if there's really
something you know happening uh, that
positively affecting the the runtime,
right? Yes, exactly. So, um
you know, if if if you have uh 98%
accuracy and you still have 98%
accuracy, it doesn't You might be
better, but you don't just don't know.
>> You don't you don't really know, right?
So, so that's where they these challenge
uh
scenarios are. And of course,
as we work on the runtime, uh
these challenge scenarios eventually
become accuracy scenarios and And then
we discover new challenge
>> scenarios
come up. So, it's an area that Yeah.
that is moving all the time. I think you
mentioned to me earlier that every time
we have upgraded to a new model, there's
always been some some tweak we had to do
in somewhere in the prompt or so. Pretty
much every time there were some things
we needed to to adjust, right?
Yes, yes. The
maybe it's it's some wording on somebody
validation prompt. It's not necessarily
the the execute task that that suddenly
[clears throat] doesn't work, but
the validation prompts, if if they don't
work correctly, they can also block
something while the task is running and
cause an, you know, an uh
unsuccessful outcome. So,
it's usually not not a big not big work.
Uh
we we don't have to redo prompts or or
something like that. Usually, we we are
able to just find we can make some small
adjustments.
But still
we have not so far necessarily been able
to do like an in-place update
um
without modifying anything, which uh
well,
models are always improving, right? We
the next model we update to might not
have But it seems to have been so far it
actually seems to indicate there is
there is a dependency and correlation
between your prompt and your model,
right? Uh if you want to be, you know,
sure that you get, you know, the proper
outcome, right? Yeah, there there's also
been some some fan funny anecdotes like
I believe it was when we trying GPT-5
reasoning, some of our tests, uh for
example, had a test email saying, "Hey,
I I need it by uh
you know, 1st of January next year. I I
need the item by that date." Um and
those tests were fine and then we used
the reasoning model and suddenly they
started failing because the agent would
just say, "Sorry, that's a holiday. I we
we can't deliver on that date." You
[laughter] know,
So, maybe we need to change the dates on
our tests slightly or something. Um
but these things also sometimes happen
when we're trying
>> And that's all that's all come
back to the non-deterministic nature of
of LLMs, right? You might, you know,
especially from one model to the other,
you can't expect for the same for the
same prompt same request, you can't
always expect the exact same answer,
right?
No, right. Well, we we certainly try uh
that to to have the same outcome.
Um but but it is true also for for these
tests we have for agents, it's not
necessarily about us testing that it has
performed the exact same steps in the
exact same order. It's more that it has
reached the the goal. Mhm. Actually,
it's the same for for for human, right?
You might you might, you know, go into
BC and create a sales quote, but there
there might be different ways to go
about it. You know, it's not maybe like
one single path to create that that
sales quote. You might be navigating to
different pages and in the end if you
produce the what's important is that you
produce the right quote, right?
Yeah, exactly. And and as a as a human,
maybe more than LLM, right? You you you
have a typo sometimes, right? You you're
typing something, make a mistake, you
correct it.
The LLM
might not make that exact mistake, but
similar. It it
>> [clears throat]
>> might
do something, realize actually that's
not what I should do. Back to your
example earlier where you said there
might be a validation error and they can
the LLM can go back and fix that, right?
Yes. It's kind of, you know,
kind of the similar thing.
Okay, so that's very cool. So, what's
what are you working on now? What what
what new improvement are we working on
in in this agent runtime? So, we already
have a pretty good runtime that is
pretty, you know, pretty cool. It can
and we have, you know, real applicate
real agents running on it with real
business scenarios, but we are still
constantly working on improving them
runtime. So, you you're working on that
right now. Can you tell us a little bit
about that?
Yeah, so so first of all, we're always
working on accuracy. Going back to
the challenge scenarios, how do we get
these to work more reliably or
so so that is an area we
are always working on
uh under the hood. Mhm. And um then
there's functionalities. So, some things
we're looking at are, for example, the
ability to give the agent some tools
like as as an agent developer, for
example, using MCP
which is the the common standard
nowadays, um
probably. So, just when you're building
your agent, maybe you can give it some
extra tools
if necessary. Um then another area is we
we talked about memory and and context
and
the agent can write down and remember
things, but it's only ever for the
current task today. So, it will remember
things and you can also give it feedback
if it asks for help, but all of that
feedback is also only captured and used
Mhm. while running that task. And so So,
it's like having a
a new employee and you instruct them to
do something and then the next task they
do, they forgot all They don't remember
that you have Are you going to explain
again?
>> Exactly. So, so what we are looking into
is sort of this this we call it
cross-task memory. You could consider it
teaching or something as well, where we
can
remember certain things
across tasks. So, so that if you do have
some situation where the agent
might have made a mistake or needed help
on something, it doesn't need to ask
every time. Um so
>> So, does does this memory include some
things that the you know, the human in
the loop, the the user has
might have
done in an earlier task like you know,
so that the agent gets stuck on
something and requires human
intervention, a human intervenes and
say, "Hey, you should do that." So, we
will remember that
for the next time and the expectation is
that the agent wouldn't get stuck at the
same place. Is that what we're talking
about here? Yes.
Now, the the mechanism for when to
remember, whether it will ultimately be
that you have a checkbox and say
remember this when you're providing the
feedback or we just decide for for
ourselves like some other systems
sometimes do, we
it's it's still I would say TBD. We're
still looking into it, but in general,
this idea that yes, the feedback you
provided to the agent
will be something it can remember for
for future tasks. Mhm. So, that is an
area that we are looking into. We have
the tools as well.
Knowledge is another one. So, the agent
being able to consult some knowledge
base like Microsoft Learn. Yeah, outside
BC. Right, outside of the product. So,
if if you've ever used the the Copilot
chat, you can actually ask, "Oh, how do
I, you know, post
sales order in BC or something?" And it
can actually query some knowledge bases
and and give you some textual
representation, right? And some
instruction or something.
>> online and look at the BC documentation
and things like that.
>> Yes, and and having the agent be be able
to also do similar querying
so that it if it doesn't know
how to do something in BC, it can just
ask the system as opposed to going to
the user. But again, we
that's that's something we'll need to
maybe verify whether that helps or not,
right? We probably wouldn't wouldn't
want to run you know, back to these uh
challenging sets we had we were talking
about before, challenging tests, right?
I suppose the expectation is, okay, we
add we give more tools to the agent,
say, "Okay, for example, you have the
Now you have the ability to to look up
the documentation." We would expect our
challenging set to show a higher
accuracy, right? Is that correct? You
know, as I saw
the example. Yes, we we we we we would
expect that the the accuracy to increase
for the or the pass rate to increase for
the for the challenge tests. Um
Definitely, otherwise there's not much
of a But then but then there's also
interesting discovery because then we
know uh
conclusively, well, we can say, "Okay,
this tool doesn't help, so we don't need
to add these tools, right?" And and that
is also something that is, you know, a
bit different from other types of
development that we we have these ideas
and and we can experiment on them, but
we don't really know from the start
whether it [clears throat] will
necessarily improve something. We we can
have uh
uh you know, we can be optimistic about
it,
but there we still have to experiment a
lot, not only in improving, but also not
regressing elsewhere because remember,
every tool we give, every prompt change
we make might lead to some other
scenarios now the LLM making a different
decision in that case and then that
scenario suddenly doesn't work very
well. And so we also have to always be
very careful with
with our existing accuracy and tests and
thankfully we have
quite a few tests and we have also built
two agents that have lots of test cases
that we can always be running and making
sure that
are
still as accurate as before or more.
>> these improvements you're working on can
you if we should try to translate them
to you know what what you know how our
partners and customers
are going to be affected by are they
going to see some of it or is it all
under the hood?
Will they see would it be visible for
them? Is it is there going to be an
effect for them in the you know when
they use some of our agent or their own
agent for that matter?
Um well the usually changes that only
impact accuracy is are are changes that
are not necessarily visible. You might
notice it because sometimes now the
agent is is not asking for help in some
situations or
>> that's also something if you were
developing an agent and and you had you
were working on one and you knew ah it
doesn't work really well you might
notice well now it's working a lot
better. Ah but
>> might be some scenario that all of a
sudden were better or some task you
couldn't fulfill before that that now
can be fulfilled. Yes and and with then
there's other types of features for
example the
tool integration where surely there
would be some UI for that and release
notes etc. and it would be something you
could definitely see.
But it it depends on on the change that
we're making.
All right. Well thank you for you know
talking about working us through these
these agent drone up that was really a
under the hood session
but thank you for watching I hope you'll
find this interesting.
Thank you.