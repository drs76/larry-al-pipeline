# Transcript — Getting started with Agent testing: Why are evaluations important? (part 1/3)

- **Source:** https://youtu.be/xB9kszf93hE
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

Working with AI is actually doesn't
matter that much what it do. It does
matter, right? But the important part is
not necessarily how good your prompt is
or your instructions, but how good your
evaluations are.
Uh so basically, will the AI do what you
intended to do and get an understanding
of that so that you can maybe modify
your product or that you can set
expectations, etc.
And it is, you know, it's always been
important to do traditional testing. Uh
most of you know that. Uh probably many
are not doing that, especially in the
more customer-specific implementations,
but we as ISVs do more tests, hopefully.
But very often customers have never
wanted to to pay or there's not been
anyone interested in in paying for that.
So it's always probably been manual
testing,
uh often done by customers.
But in the this traditional testing uh
sphere,
you would normally do
uh deterministic
uh testing of the testing deterministic
behavior. So you put in some input and
you expect some certain output.
And so you always check if the results
are right or wrong with some exact
assertions. They will always, you know,
be true or false.
Uh
and also, if you ran this 100 times, the
behavior is repeatable.
You know, you can And And that's 100
times on the same code, that is.
And the behavior is repeatable and you
can do this pass-fail.
Uh AI is different in that AI has
non-deterministic behavior.
The uh the inputs will vary.
Uh users will use AI differently. They
will come in with different prompts.
Emails from different people will be
different. Uh you know, questions from
different people will be different.
There will be differences in biasing,
words used, et cetera.
But also the outputs will likely vary
based on whatever context was available.
Sometimes even
just due to to randomness.
And so you need to evaluate these and
measure them the quality and safety in
this.
How does the feature behave when trying
to sort of fool it or do do do false
things? But also how how great is the
accuracy?
And the behavior isn't repeatable, and
the quality is subjective, and the
metrics actually matter more than just a
pass-fail compared to traditional
testing.
And that's why we we use evaluations.
And so um
in in this most of the rest, if you
switch to the next one, uh Nikola.
>> Mhm.
>> In most, you know, in in when we look at
the types of evaluations that you can
do, then of course you can do the human
evaluation. Where you actually try this
feature out, and you try different uh
variations of input, and you see how it
goes. But it's super hard to scale this.
So you need something more uh
deterministic.
And I said that it wasn't deterministic
with AI, but you need to program the
tests in a deterministic way.
You can have
variation in the input. You can have
different biases. It can be data-driven.
Uh but building it in AI AIL and using
um data-driven via YAML gives you a
framework for basically testing in a
deterministic way to do the evaluations
in in a first deterministic way.
And that is what we're going to focus
most of today's office hour how you can
build your own evaluations for your AI
features here.
Then you can also
use LLM to actually help you judge the
output. So,
you could use things like Foundry has
functionality for things that you
generate. So, maybe you generate
an outbound communication like an email
response or something like that or text
that you want to put in on a product
description or things like that, project
descriptions, etc. And those can be
super hard to again
evaluate using a deterministic approach.
There you can use LLMs
to try to judge, okay, I asked for this,
does the answer reflect what I asked
for? And they can help you provide a
score.
And then you even have a more advanced
scenarios where you want to do
benchmarks
potentially across
um
you know, specific setups for for all of
the different agents.
And also observe things like agency,
cost of this, error rates, etc. But
we're not really going to cover that
today. The main focus is on the on the
second part.