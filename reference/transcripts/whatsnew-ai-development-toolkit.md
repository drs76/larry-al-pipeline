# Transcript — What's new: AI development toolkit

- **Source:** https://youtu.be/juUBVPfIp8A
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[music]
>> Welcome to this session on the AI
development toolkit. My name is Peter.
And I'm Steen.
So, you might not have heard about the
AI development toolkit, but hopefully
you heard about the development toolkit
for extending copilot in Business
Central. Or just copilot development
toolkit.
The AI development toolkit
is the new name we're using now.
We decided to change the name because
the toolkit now does not just support
the ability to use Azure Open AI to use
LLMs from AL code, for instance when you
build prompt dialogues and evaluate or
test these. But it now also supports
designing and coding agents in Business
Central.
The latter has actually been in public
preview since the beginning of February.
We've already seen almost 1,500
agents being built by the community so
far.
Just in the last month. So, if you
haven't already tried,
you know, we really suggest that you get
started.
I will talk a bit more about agents at
the end of this session because we have
a whole lot of sessions just dedicated
to the agent preview.
However, in this session we're going to
focus on the other news in the AI
development toolkit. Namely updates to
BC AI resources, Azure Open AI policies,
and how you can evaluate your AI
features.
>> [snorts]
>> If you want to stop and know more about
the AI development toolkit, you can go
to ak.ms/bcstartcodingwithailearn.
That will bring you to a landing page
where we have links to
everything we have for the toolkit, how
to develop in AL,
samples, videos, etc.
So, let's start talking about the
building AI resources. They are key
feature of the AI development toolkit.
Publishers can use large language models
via the Microsoft managed
Open AI resources. And that basically
eliminates the need for publishers to
independently procure and manage Azure
Open AI subscriptions for their
customers.
We had a session going deep on how you
can do this last year. I provided a link
here. We're going to have the link in
the description as well. But if you
haven't heard about BC AI resources, you
can jump to that one and and understand
what it's all about.
But the change we did for BC AI
resources is that typically you would
use your own subscription while
developing. And then for production use,
you can use the BC AI resources that are
part of the toolkit.
And when you were using the latter,
you would previously have to
authenticate to the BC AI resources
providing your own partner subscription.
It was not something we were using. We
were not billing your partner
subscription, but we were using it to
verify that you had already
signed up for an Azure Open AI
subscription yourself and following sort
of the licensing and EULA
requirements there.
But we have now removed that
requirement. So, when you authenticate
or authorize in code using the set
managed resource authorization we now
have a new
signature for that method that omits
passing in your subscription details. We
still have the old
method because, you know, we are
obsoleting it and we have to keep it a
little bit. But if you already have
built code using this, you can change
and adopt the new method signature. And
if you haven't started yet, you should
only use this new signature.
We also have a sample on the BC Tech
GitHub repo where you can see how you
can actually um
authorize and use the BC AI resources in
your features using the Azure Open AI
calls from AL.
Then we have another improvement when
you are working with Azure Open AI and
that is supporting some more granularity
for policies.
And the first policy that we're going to
talk about is
content filtering. So, content filtering
is basically a capability in Azure Open
AI where the LLM guardrails against
harmful content.
And so, the Azure Open AI works with a
number of levels from basically none
over low to medium to high harmful
content. And you can set up a limit as
to how much harmful content you want to
tolerate in your feature. You know,
should you block any kind of attempt to
generate having the LLM to reply to or
generate harmful content.
And this is a feature that is available
when extending copilot in Business
Central via the prompt dialogues or
using our Azure Open AI methods. It's
specifically the Azure Open
AI.GenerateChatCompletion
method.
We have added support for only low and
medium content filtering policies. Where
low is the default and actually the the
setup that will
allow the least amount of harmful
content. And we recommend that you only
change for your feature if you see that
supported
scenarios, scenarios that you would like
to see supported are flagged out for
harmful content on the default low
session.
We do not support the high setting,
basically passing the most harmful
content. That is something that you can
have if you're using your own Azure Open
AI subscription for the production
scenarios for your customers.
That requires an approval from Azure
Open AI though. It's a form you have to
submit. And in general, we just
discourage um
going with the the high setting. But of
course, it depends on what your scenario
is. Maybe you're supplying to industries
that could be selling items that fall
into sort of harmful categories and you
might, for instance, need to have that
capability when you're working with
LLMs.
But the default is low.
Um
If we look at how you do this from
source code, there's an example here.
It's actually also in the documentation
for this feature. We have a new Azure
Open AI policy
parameters code unit.
And you can then input this enum value.
Again, you have low and medium
supported. And you then pass these
parameters as part of
your call to the LLM.
Then we have another
setting that you can modify as part of
the Azure Open AI policies and that's
how you basically
manage prompt guardrails or cross prompt
injection attacks, protect against that.
It is part of the Azure AI content
prompt shields feature.
And it's a way to identify and also
blocking malicious attempts to inject
instructions
through external data that gets passed
into
the input for the LLM. So, you know
um
if if anybody tries to trick the LLM
feature that you are building or the AI
feature that you are building.
And you can learn more about it in the
link that I provided here for the prompt
shields. We'll put that in the
description as well.
And just with the
previous feature, you can set or modify
this level
when you are building features in AL
that calls out to the LLMs through the
Azure Open AI APIs that we have provided
for you.
If you are using this
to basically detect
XPI in your input prompts, then for
these untrusted prompts, you need to
remember to also call detecting tags in
in the input. So again, you're using the
Azure Open AI policy parameter code
unit. You are calling to add tags to the
input and then you can set the XPI
detection to true and then the platform
will,
you know, add additional detection or
and flag or block against any kind of
prompt injection. So, that's it for me.
A big part of the AI development toolkit
is also the ability to after you created
AI features to actually go and test and
evaluate whether those features have the
right accuracy. So, Steen, can you talk
about that? Yes, thank you, Peter. So,
let's talk about what's new in
evaluations.
So, the first thing you'll probably
notice is the terminology change from
evaluation or from tests to evaluations.
And this is also represented throughout
the product or in the toolkit.
Additionally, we're introducing new
configuration parameters.
That
that you'll be able to configure and
then use in APIs.
Also, we're adding language support
built-in to the tool that you'll be able
to use and test or evaluate AI features
in different languages.
Additionally, we're adding insights into
Copilot credit usage in evaluations.
And lastly,
we're also adding some agent support and
there'll be more about that as well
later on.
So, the AI test tool is now referred to
as the AI development tool kit
evaluation. And this is because the
evaluation capabilities are now part of
the broader development tool kit.
So, you're still getting the same
data-driven AI evaluations or testing
that you're used to, but you're also
getting new capabilities as part of
this.
It's built for Copilot and agent
development and evaluation. Um
So, it's it's the same tool with new
capabilities part of a larger AI
development tool kit.
So, the first thing we're introducing is
evaluation suite configurations. And
this helps you or this is the first step
towards managing AI quality at scale.
Um so,
it will allow you to define capability,
test type, and execution frequency of
your evaluation suite. And then you can
use those in APIs. So, these are
standardized evaluation configurations
that you can get through the API and use
in your pipelines to automate this
process.
So, if we take a look at how this is
exposed in the product, you'll be able
to see here that you can now set the
capability of a specific
test suite or evaluation suite.
So, in this case we set it to sales
order agent and these capabilities are
the capabilities that you also register
in order to create a Copilot or agent
feature.
Additionally, you can set the run
frequency to daily or weekly or manual.
And this is an extensible enum, so you
can extend with your own frequencies.
Um but it's not automatically running
just because you set this. This is just
a configuration parameter that you can
uptake in your own pipelines.
And just to take a look at how this
looks in code, you can see here that I
set the capability, frequency, and test
type. So, capability again is the
Copilot capability that you are
evaluating, then the frequency, and
lastly there's test type which is sort
of a broader
um
broader categorization of the type of
test because you might need different
setups depending on what type of test
you're doing.
Next, we have built-in language support.
This allows you to evaluate agent and
Copilot experiences globally because
Business Central solutions are global
and so should your evaluation suite be.
Now, the tool kit supports suites and
data sets with languages. So, you can
have multi-language data sets and suites
and execute them in the language that
you want.
This allows you to evaluate the same
scenario across multiple languages.
So again, going into the tool, you'll be
able to see here at the very top that
you can configure languages for a
specific evaluation suite.
And down here, you're able to select the
run language. So, this is the specific
instance or the specific language that
you run want to run this suite in. And
you can also set this on the command
line runner.
Similarly, if you go to the test inputs,
you can now see that they are
categorized by languages.
So, if we take a look at this, this all
represents one multi-language data set.
So, we have the very top multi-lang data
set and then we have specific instances
of language that you want to test.
And similarly, we have the same one
below.
In order to uptake this in your apps,
you need to specify the name and
language in your data sets. And this is
all you need to do for the tool to
recognize that this
this is the language of the test or of
the data set.
And the name needs to be common across
data sets. So, if you have an
English and another language, then you
need the same name for the tool to be
able to recognize that it's the same
data set.
Then in your evaluation suite, what you
can do is you can refer to this data
set. So, here I'm referring to the data
set you just saw before.
And the tool will automatically be able
to run this in these languages that you
then specify on the suite as well.
And that's everything you need to do in
order to uptake the language support and
run evaluations in different languages.
Next, we're also adding Copilot credit
insights to help you understand AI
consumptions for evaluations.
So, developers will be able to see how
many credits were used per run, per
line, and per data set entry.
And this is also visible directly in the
results of a run.
So again, if you go back into the tool,
you'll be able to see at the very bottom
the Copilot credits used for the entire
run.
And on the line level, you can see how
many Copilot credits were used for each
line.
And additionally, if you go into the log
entries, you'll be able to see the
Copilot credits used per individual data
set entry. So, you can really get
insights into how many Copilot credits
were used.
Lastly, we're also adding agent
evaluation support. This is still in the
early stages, but now you can build and
validate AI agents in BC.
So, you can select which agent you want
to run in your evaluations. And you can
inspect the agent tasks per run and per
line and per data set entry just as we
saw with the Copilot credits.
And lastly, you can use that agent in
your evaluations.
And very soon we'll have an agent
library coming giving you even more
capabilities to test agents.
But for now, you're actually able to to
get started.
So, on the AI evaluation suite,
you can select the agent that you want
for the specific suite. And that will
make it available in your test to get
this agent and set tasks on the agent.
Then you can also see the agent tasks
after run. You'll be able to see which
tasks were created during this run.
And you can also see for each line what
tasks were created. And additionally,
you can see for each
data entry which tasks were created.
So, in order to use this in your
evaluations, you can define a function
like this, get agent during test, which
takes an agent security ID.
And then you can use the agent test test
context code unit.
And you can get the agent user security
ID. And that will get you the specific
instance of an agent that you defined in
your evaluation suite. And you can then
use that and you can also use the test
context to set specific tasks that you
want to run. And and then you can do
your evaluations and and the test will
run with that agent.
And that's it for news in evaluations.
So, Peter, do you want to give a
summary?
Yeah, and let me just say that you know,
whenever you are building
or extending Copilot Business Central or
if you are building these agents that we
just introduced in public preview, test
are really important when you work with
with AI or evaluating, right? So,
hopefully you will be using also this
evaluation part of the tool kit to go
and assess the accuracy and and monitor
for that and also help you actually
improve prompts and agent instructions
based on those insights.
But for the summary, as I said in the
beginning, we now have changed the name
of what was before the development tools
for extending Copilot Business Central
or just a Copilot tool kit to the AI
development tool kit. We talked about
how for the built-in AI resources, you
no longer have to pass the your partner
as your OpenAI subscription when you are
using the built-in AI resources. We
talked a bit about some of the
flexibility you have for setting the
Azure OpenAI policies specifically for
content filtering on harmful content as
well as um
the
X P I A or prompt injection attacks.
And Steve talked about how with the
evaluation tool, you can now
have better support for configurations
for pipelines, etc. Test multiple
languages, see how much credits your
Copilot features are actually using. And
also um how we are now beginning to see
support for evaluating agents.
And speaking about the agents, we have a
whole series of videos just dedicated to
designing and coding agents in Business
Central. The features that went in
public preview
just a little over a month ago. You can
find all these videos by using the short
link aka.ms/BCDesignAgents
or just find the playlist in our YouTube
channel. As I said in the beginning, we
have
many in the community already started
trying out building agents. So, if you
haven't already done that, I suggest you
go and start playing with with agents.
As usual, we have a number of different
resources. The aka.ms/BCAll
is a good starting point to to see all
of the other sort of short links. You
can join our community. We we have moved
from Yammer to Viva Engage. You can ask
there. We have lots of different office
hours on different themes. As I
mentioned, YouTube. And as always, you
can give us a feedback.
Uh
and also monitor LinkedIn for any social
media news.
Um and I mentioned YouTube. So, thank
you for joining us. Yeah, thank you.