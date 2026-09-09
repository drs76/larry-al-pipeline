# Transcript — Getting started with Agent testing: Test setup and structuring (part 3/3)

- **Source:** https://youtu.be/V4zCPAsYi_Y
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[music]
Quin, can you show us how we can
structure the tests and how we can get
the test set up automatically done?
>> Yep. So, we we've seen from your
presentation uh Nicolola on how to write
the AL test and how to create the
datadriven uh structure from from the
YAML files. But we actually need to
register all these tests and make sure
that they do get executed in business
central. Um if you're moving to the next
slide, um we we've seen those two
categories. So we do have AL tests, we
do have the data set here. Um the AL
test is what ends looping through the
turn verifying their outcome. So the
data sets are defining the input in the
form of queries and the expected output.
But we also have an extra um one um and
this is the sweet config and that sweet
config is what is actually wiring
together both the data sets and the code
units and they're also taking uh an
important role in registering those
tests with the evaluation tools so that
you get them available in business
central. So those three components are
the components you'd have in in your app
in business central. Um and in order to
leverage all of this uh you would need
to take a dependency. So if you click a
bit further um we you need to depend on
this new app this AI development toolkit
evaluation which is uh the app uh we
recommend using and it propagates
dependency to everything you need and
among those you have the AI test
toolkits that defining the core
integration with uh all the UI within
business central with the agent test
library which is what Nicolola just
showed you with all the nice utility
methods that you can use to handle your
tests and also all the other test
libraries uh that allow you to create
your data uh when you need to create
customers when you need to create
document records and so on. Um you have
here an example of how it looks like.
This is the uh configuration file that
corresponds to what I showed you earlier
in UI. Um and you can see here that it
has this AI tu declaration with the code
and the description. It's also defining
the test the test type as being an agent
type. Um and it has the four lines that
we've seen. So we do have the P 0P path,
the attachments and then the advance
scenarios that were marked as P1. You
can also see from there that the data
sets and the code units are referenced
on each lines. And in this case, we're
actually reusing one code unit with
multiple data sets, which so which
highlights also how easy it is now to to
create new tests and um extend them
through this data driven approach. So
how would you uh be structuring those?
Um so how would you first of all like be
registering those? So we we do need to
have some install code unit added as
part of our test app. that install code
unit is loading from resources all the
different YAML files for the data driven
uh for the data and uh the configuration
files in the form of XML and then it
will be calling methods from the AI um
test suite management and this one will
be taking care of importing those files
into your environment. So you do need to
have an installed code unit and you do
need to use some of the methods that
we're making available out of this
modules.
So
how would you structure your tests? Um,
as we've seen shortly a bit uh before,
we usually define a set of P 0 tests.
Those are the ones that you should
expect to to pass pretty often. Uh, they
are the happy path. They must succeed
most of the time and they're usually
small focused and you want them to be
running fast and pretty often. And then
you might have another category of tests
you might want to look into specific
scenarios or specific edge cases, some
bugs you've learned over time and that
you want to capture into tests. And
they're also allowing you to iterate
quickly on some specific part of your
app. So if there's one part of the
scenario on the sales return agent here
that doesn't work, you might define
specific uh test suit for it and
specifically run that one uh and not run
all the other ones. And then the last
category would be all the load and
variation tests. So the load test is
something that we started introducing in
order to test the limits of the runtime
and the limits of your agent. You would
be defining here tests that have a lot
more data than than your agent is
usually dealing with and you would run
them more sparely because uh they would
take longer to run, but they also give
you a good overview of uh what your
agent actually can do. And then we also
recommend having a set of variation
tests which are specific to the other
test categories we've seen but with new
variations so that you can test your
agent in slightly different context and
assess how well it adapts to those. And
I have here now an example of how it
could look like for the sales return
agent. So if I was to introduce those
specific scenario tests and those uh
variations it could look like this. I
would have my P 0. I would have some P1
taking some specific scenarios and then
I would have additional test testing
variations.
All right, thanks Quinton. So for the
next topic which is going to be brief is
about PowerShell support for running
tests. So if you would like to set up
the CI/CD pipelines and to run your
tests in the automated way is supported.
So you can use this test runner for AL
test PowerShell module and you can point
this PowerShell to run the tests against
the sandbox. Currently it's only
possible to run these tests in the
sandboxes. Unfortunately, it's not
possible to run them on prem for the
algo images. This is following is
similar approach as BCPT or the AL test
runner. The way how you would
authenticate is by using a token which
is the same as token as for APIs and
then you can point it and kick off the
run and collect the results
automatically from the sandbox instance.
It is shipped on the PC image. You can
find it in the folder which is called
applications. Then test framework testr
runner. So this is the place where you
can find this partial file and use it
for your own tests.
We have shipped samples. So you can find
a sample test which is called the sales
validation agent test at the BCT. So
everything that we have been presenting
today you can go to the BCT and find one
of the examples. And currently we are
working on shipping the second sample
which is the sales returns agent. We
have shown you some of the things from
the sales return agent. However, this
one is not on BCT. If you need it, reach
out to us and we can provide the codes
to you so you can see how this run. But
I do believe that the sales validation
sample is quite sufficient for getting
started.
All right. So for the future plans
briefly we are planning to introduce LLM
as a judge and this one is to verify the
user intervention if it is containing
the text as you would expect it and also
to gener to review the generated message
text for example an email that is
generated or anything any other text
that the agent is able to generate. Then
we are looking into enabling running
these tests from the visual studio code.
So you will be able to kick off the ai
eval suit from visual studio code. As I
said, we want to ship you more. We want
to ship more samples. And one of the
items that we are looking into is making
this fully possible for the agents to
implement. So the idea is that you can
take your development agent, point it to
your code, and then get the agent to
implement a BC agent together with
writing tests and running and improving
the agent that it builds in the loop.
So call to actions, try it out. You can
try out the sample that we have shipped
and please give us the feedback. Keep in
mind this is the first version. We are
really looking forward to your feedback.
Now you are able to write the accuracy
tests. So if you find anything
problematic that you're missing the
tools that something is not intuitive
enough or not documented, let us know
and we are going to improve it.