# Microsoft Presents: Exploring the Future of AL Development: Testing Copilot Features

- **Source:** https://www.youtube.com/watch?v=q8sHtAROKTY
- **Video ID:** q8sHtAROKTY
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 46m44s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

we're both software Engineers on
business Central and today we'll
continue the co-pilot theme and talk
about like how we see the future of Al
development in terms of testing all
these co-pilot features so it's a a very
light topic to finish Tech days
on um so for the agenda today uh we'll
start by explaining some of the
challenges and like reasons why you
actually want to bring uh automation to
your uh llm features for testing and uh
you know why why it's important then
we'll cover some like different test
strategies um on how you can uh tackle
these scenarios um and then we'll
actually dive into how we went and
tested chat with
co-pilot um and just in case like you're
watching this online later we do
recommend watching the talk that was
before this one which is like building
trust in Ai and how we built chat with
copilot and so once uh you understand
how we tested chat with copal we'll take
a look at how uh we can actually apply
this to your llm scenarios today in Al
and kind of like in the tech day spirit
it's all in like work in progress um so
you know it's all subject to change and
uh we' love to hear your feedback on all
of this and uh after showing you our
thoughts here uh we'll wrap up by um
letting you know where you can get
started today and uh be sure that your
features are already uh to be testable
and um have confidence in their safety
and
reliability so why do we want to test
really so obviously there's all the like
classical test reasons uh but in the llm
world there are a few new um conditions
like to be aware of so first like how uh
do we measure the accuracy of the
feature you know uh you might have tried
out the prompt a few times in say Azure
as Studio or like co-pilot and it seems
to work but like do you have any kind of
confidence in it working if you uh if
you scale it out um likewise if you you
have a prompt already and you go and
change like a word or two or even add a
sentence how do you know if that's going
to break other things um good reason to
add
tests um and then on on the flip side uh
you also want to make sure that you
handle all the bad cases so like you
want to make sure that your prompt
tackles all these harm mitigations that
we were talking about before you know
like asking about your manager's salary
and worse and these are kind of like the
responsible AI like fundamentals that uh
we uh deem very important for all your
all your features um and so like to the
extreme like we we call this like red
teaming uh which could be a whole talk
in itself but essentially it's like
where you are playing as the bad actor
and uh you're trying to like break the
prompts or get it to do things that are
not expected uh so that you can ensure
that you know your prompts behave well
and uh you do not expose your end users
to actual
harms so one of the first obvious
challenges to actually writing these
tests is where do you get all the data
to build out these test data sets and um
kind of the first thing you want to do
is uh when when um you want to get the
accuracy uh you need to build a a set of
inputs and you need to be careful here
already because like it shouldn't be
just yourself coming up with the inputs
because then you start getting kind of
biases into like how you are asking
questions so you want to get it from at
least a few different people um but on
once you have that you can go ahead and
take that data set to an llm and then
produce a ton more examples uh but then
you also need to go ahead and do like
some manual validation to make sure that
uh like the samples that we generated
are actually good because obviously the
llm doesn't
know and um just like your normal test
if you have some bad examples of inputs
that's also good because you want to
test all the all the edge
cases and then again for the red teaming
side of things you do need like a large
data set here uh like a pick a number at
least 600 samples uh so you can go ahead
and try and build one yourself uh of
course uh but we also have some tools
available to kind of automate uh the
simulation of like a redeeming exercise
against your prompts uh within Azure AI
studio um or if you are building your
own um output of um these data sets you
can actually get them graded within
Azure AI Studio as well uh for example
like this is what we do with marketing
Tech suggestions uh we we get these data
sets and then we evaluate like if they
are contained harms or not and we'll
we'll demonstrate that a little bit
later the next challenge uh that you'll
come across is like keeping current with
all these models because they're being
updated all the time with you know new
features or they they become cheaper so
there's like strong incentive to move to
them um so the the way kind of we think
about it is that there are like these
model families so we have a GPT 3.5
turbo GPT 4 and then each of these
families have like minor versions uh
underneath them so like with turbo we
have a model that was released uh last
year in June uh and uh one this year in
January GPT 4 same last year in June
there was one and we just recently had
40 released as well and so we just see
that as an incremental upgrade to to
gp4 and um you know these these models
May behave differently um between
versions so uh how do you keep current
with the latest one how do you know
what's going on so I thought it would be
interesting to kind of start with uh
some examples that we have seen uh with
like model new models bringing in
regressions so this first one here um
you see we had a prompt that was around
drafting uh an email that was confirming
some booking information and so on the
first model or the original model I
should say uh it would always say like
dear customer I'm writing to confirm the
time you booking here is all the
information blah blah blah um and then
when we upgraded the model we actually
saw that it changed the perspective of
the email right because the prompts kind
of ambiguous so it would say hi I just
wanted to confirm like is this the time
for my booking you know and obviously
that's not completely broken the
scenario so uh yeah that's that's not a
good case and uh like within business
Central as well we saw with the
marketing tax suggestions you know uh
you can describe say the Athens desk get
a request a tagline and a paragraph of
text marketing text and so in the the
original model that we shipped with it
would produce a nice tagline and then H
create a new paragraph saying like
introducing the athens's desk or
whatever and then when we moved to the
new model um actually what it still
produced like a tagline and a paragraph
of text but there was a subtle
difference that it started to rather
than giving like a double new line it
would only do one new line and as part
of our like grounding checks that happen
after uh generating a completion from
the model um we actually rejected these
suggestions because it's not a new
paragraph technically so uh you know
that upgrade kind of broke the feature
as well um so you know I I I hope this
kind of illustrates some of the
challenges with the model upgrades and
why you would start wanting to build
like some kind of test Matrix to um to
to validate these these
things so how are we kind of taking care
of this uh on our side um we we for each
kind of model family um we have like a a
concept of a latest model and a preview
model so for the feature that is shipped
um we refer to the using the latest
model of the particular family and then
when whenever there's a new model uh
coming out and we want to uh upgrade to
the newer one uh we point the preview as
like an alias to the newer model and
that gives Engineers time to test with
the new model um and then once
everyone's kind of happy we update the
latest to point to the the same preview
version and then we just wait till the
next one comes along and repeat the
cycle and uh this is kind of interesting
um because uh there's like this whole
machine learning Ops uh which previously
we had nothing to do with that was all
ml engineers and data scientists and you
know they did their own thing now we're
seeing the shift to llm Ops or like even
you know your your companies might be
starting this now uh and you'll see that
we are now famous uh app developers as
part of the the target audience and that
means we need to become aware of a lot
of new things like a lot of new metrics
and evaluations and you know as part of
this like testing stuff for Al uh we're
really hoping that you know we can help
as a platform here to make make this all
easier uh for for for
everyone so how do we actually test chat
with co-pilot so this is a a simplified
diagram of what you just saw in the
previous talk um and you can see here
that we have many different interactions
with the the llm going on here um so you
can kind of just you know put arrows
everywhere and say yes this is where we
need tests uh so for example the the
very first thing of you know rewriting
the conversation as a single message you
probably want to test that uh then once
you have this Rewritten message is it is
it off topic you probably want to add
test for that um and then once we are
invoking a particular capability say
it's looking for documentation or record
we probably want to a test for that uh
or if it's something like the maybe
business related but we don't support it
right now we also want test for that and
uh lastly of course we should also test
the actual generated chat chat message
uh that we send so tests everywhere but
actually there are there different types
of tests that uh you should be doing so
um we think of these the first is like
accuracy tests and you can think of
these as like your your unit tests
conventional unit tests but for um the
llm stuff and you can kind of break
these down even further into like your
absolute tests which is where you're
being very explicit about what you're
asserting uh so for example you have a
conversation uh that's you're asking
about your manager salary um that should
result in an off-topic uh result uh and
then uh the more complex example is uh
grounding tests so ensuring the say the
final chat message that you see um you
want to make sure that the output there
is grounded on the data that was given
to it so for example um if you uh look
for a record um and the final chat
message has a record you want to make
sure that record maps to what was
returned from the skill and it hasn't
just made up a new item or customer or
whatever and then secondly um you have
your quality tests and you can think of
those as like your your higher level
like endtoend integration type tests and
this is where you do all your like red
teaming and HS and other responsible AI
checks and they they are normally quite
a bit bigger and lengthy and so so the
idea is that for a given scenario so for
example chat with co-pilot you do want
both types of tests right so you want
the accuracy tests which are fairly
quick and you can run during your
development and during model updates to
give you like the granular checkpoints
on the different parts of the system and
then once you're kind of happy with all
the changes there you can run your
quality tests for the endtoend like
feature set validation and yeah go
through all your responsible AI uh
checks so if I go back to this diagram
we can actually classify all these tests
so you can see that like the Rewritten
conversation as a message uh feature
um that is just an an accuracy test
right because here we are taking a um a
conversation and generating a single
chat message and it doesn't really
matter if this is producing harmful
comment content or not because this is
passed further Downstream to say the off
topic uh detection and it's it's it's
the off toopics uh detection problem to
make sure that it deals with all the
harms right so that's where you would
then do the quality
checks uh
yeah so we can jump into maybe a
concrete example here um
so this uh this this is covering the re
Rewritten conversation as a message kind
of feature and uh you can think of the
setup of your test as the test context
so here you have like a multi-turn
conversation uh which is saying like you
know the bot opens the conversation with
hello how can I help uh user then asks
uh what open orders are there and then
the bot would reply with uh there are
open orders uh uh for sales order so1 Z1
and then uh the user finally asks what
is the amount right so it's already
quite a complex scenario here because
you can't just say like uh the user
message is the Rewritten
conversation um so we we take this whole
conversation and then we uh put it into
the product code and that will give us
the prompt result so again we don't want
to include the prompt within the tests
um it's like kind of like separation of
concerns right you don't put test code
in prod code and prod code in test code
um so yeah you you run the product code
and get the prompt output and here I've
put two examples so let's say the
product gives or the prompt gives uh
what is the amount of the open sales
order uh as one example or the other
example could be what is the amount of
the open sales order s o 1
z01 um and then finally you you want to
define a question which is basically
your test assertion um which in this
case would be that the the message
contains all the relevant intent and
identifies um from the the conversation
right so in this case the first one
would fail because although it captured
the intent it doesn't contain the
identifiers so it doesn't have enough
information to actually perform the
query whereas the second one passes
because that has the intent and the
identifier and so now that we have this
we can um build some um level of
accuracy and confidence within the this
uh feature and that means like the
capabilities that consume the Rewritten
conversation as a message or the the
user intent um can uh take like take
that with confidence and safely kind of
depend on
that so uh frankman do we have anything
like that in Al yeah so thanks uh for
explaining why we need to test and why
it is important to test so let's look at
an example of the sales line suggestion
which has been mentioned in the keynote
before uh so in this uh in this context
so we are talking about sales L
suggestion with the scenario of finding
the document by reference so here the
user can ask for something like okay I
need some items from the last sales
invoice so this is the scenario which we
would like to test so I will show you
how we did it traditionally uh in Al
like before uh with without the tools
what we have now or what we are building
so idea is okay all my user input
becomes a single uh label for example
and each of the label goes into a
separate test so that when I run the
test in the AL test tool I get which
tests are failing or passing you can
imagine how quickly uh it will uh the
code will CH because you will have to
keep adding new test and keep adding new
inputs and in a way that uh the code
will become unmanageable really quickly
but uh can we have something uh which
can save us here let's look at data
driven test so uh that's what we are
thinking uh the all the scenarios for Al
tests can we use data driven tests what
are they so they are basically uh a set
of data uh colle containing the test
inputs which we could use to run the
test repeatedly so you have only one
test and you can Define hundreds of
input and you will run the same test 100
number of times so rather than writing
100 different tests you could just have
one test now now this enables
reusability which in turns improves uh
uh the test coverage because now what
happens is you can reuse the same test
but just vary the input a bit and you
can have cover a lot more
scenario and also improves some
maintainability because now your test
logic is different or separated from the
test data itself and in context of
generative AI uh so llms are very
sensitive to different input variation
as Sam showed in his examples the slight
change in the input or could completely
uh like change the output so we need to
test against various inputs uh and
sometimes as we saw in the previous
talks how safety and evaluating safety
is important so we would like to eval
evaluate the safety metrics sometimes
the performance metrics like how fast
does the prompt or the feature Works
what's the quality and in case of cost
like how many tokens do we consume so we
would like to measure all these and we
were thinking of building a tool or we
are try are in process of building that
Tool uh to help in this
situation yeah so I will show you the
demo of the Tool uh however this a big
disclaimer this everything is work in
progress we will like your input in
designing the tool or right now I guess
the pr is out you will explain later but
we would definitely need your input to
uh design this uh experience and and get
some input from you guys and so for
example uh I showed you the some example
tests uh from the uh sales line
suggestions this is the actual test from
the GitHub repo you can see there are so
many labels for just one scenario and I
can just keep scrolling down there are
so many tests for each
input what if I tell you I can condense
them into one so uh let's look at the
tool first so I'll go to the business
Central I have the extension deployed
already so I look for AI at s suet
that's what we are naming it right now
and I can go ahead I can import a suite
uh so I've exported this one so let's do
that so I got the suite here named Tech
days uh 24 and over here you can see you
can Define the description give a
description to the suite you have the
code and then it it is asking me for a
data set so what would be the data set
in case of sales line suggestions uh so
let's start by looking at the data set
first
yeah so what we did uh so in the data
set we are supporting Json uh lines as a
file type and Json so in this case this
is a Json line type which become which
means every line is a Json um object and
in this case our question is all the
user input um so in this uh one of the
example is need all items from previous
sales invoice okay but we would like to
validate some some fields in our test so
for example uh in the case of when we
are asking for a specific sales invoice
we would like to validate if the
document number is correct and in other
cases we also want to validate uh about
the date so you can see need all items
uh from sales invoice from last week to
today so in this case we expect the
start date to be last week and the
expected date to be end uh expected
expected end date to be today uh these
are constant because we would like to
derive them uh in runtime because they
are dependent on the system time so we
we don't want to break your test when
you run it uh next year uh but yeah so
let's upload this data set so we can go
to the input data set where you we can
upload all the data set at once uh so
let's upload one of them so the data set
has been uh uploaded you can see there
are 28 entries in this and uh what we do
is we generate the description and code
for you if you don't Define it in the
data set so that you can refer to
specific input with the code and
description and so my data set is here
all the lines were passed and inserted
into each individual lines I can go back
to the suite and now I can assign that
data set uh here I can assign it to the
header which means all the lines uh
would use the same data set here and
then we have something called AO AI
model version in this case it's the
latest uh you can choose between latest
and preview at this point we do not
support it as in in a way that we do not
override that as as a Al developer you
would have access to this and in the
test you can decide which procedure you
want to call or you can parameter
parameterize it but hopefully if you are
using AI module from uh Microsoft we
should you should be able to get this
for free and then we have the test
Runner you can specify what kind of
isolation or which test Runner you are
using so we are using the isolation mode
in this at this point which means all
the test uh would be rolled back so none
of the transaction would be committed
and you can also give a tag to identify
the run of the test because we store
every run um of the test Suite we will
store it and we'll log it that way you
would be able to compare it so for
example now we are looking at the code
unit sales line accuracy test which is
inside the lines uh you can give a
description and let's see what's inside
the test first before executing it so
over here you can see uh we have one
test uh what we are doing is we want to
access the data set the way we do it now
is uh we have we are creating this AI
test context code unit we will provide
some helpers there which would allow you
to interact with the data set uh and we
are uh trying to standardize some of the
properties in the Json which you could
Define for example question would be a
standard property so in that case you
could just use the helper method to get
the question directly rather than having
to pass the Json uh and the next one
let's say the expected data document
number which is uh which won't be the
standard one one but you can still use
the get test input which gives you the
entire line and since it's ajacent
format we are providing some helpers to
go through the path using dot element
and you can get it as text and other
properties so similarly uh for date as I
mentioned that uh we are extracting the
date but we are passing it through a
function in the function we evaluate uh
based on the system date what what does
last week what does yesterday mean so
you can do that in your test
so once we have the uh expected date and
the expected results and the question
which is the user input we pass the user
input to the procedure uh which will
actually call the llm or the co-pilot
feature and in this case it's the sales
line suggestion feature just want to uh
note that none of the problems would be
exposed in the test it is just we are
just calling the procedure underneath
from the base up so or from the the
sales line suggestion app so you you
don't have to expose The Prompt
themselves just the end point or you can
even use test pages to access the prompt
dialog properties so you just uh do user
test that way so so this is just like a
Al test underne right exactly so I
forgot to mention that it's a regular
test with a subtype test so there is
nothing special about this and you have
the test property on the uh start of the
procedure and you can have similar
experience of writing the regular Al
test uh so what we are doing doing is uh
we get the response from the function
call or the from the sales line
suggestion feature and what we want to
do is we are just asserting certain
properties that that response should
contain the response is in adjacent
format so we can then use the same
helper method to see okay what was the
document type what was the document
number start date end date and we can do
the
assertion all right having said that uh
now we can go back to the suite and
let's start running the test so did the
bit little bit of cheating here because
I'm not calling the actual uh feature
because I mocked the responses because
it would take time of course to run all
the test uh so what you see here uh the
test has been run you can see all the
numbers here how many tests passed how
many failed and I will show you what
happens behind the scene so if I go to
the AL test tool so what we have here
is uh so the a suit would be created a
suite would be created for you uh by us
so depending uh we'll try to find the
right Suite so we don't have to create
multiple Suite so we'll find it and once
you have that uh you will see all the
tests uh so there was only there was
only one code unit and one procedure in
it however we have data input now we
have extended this tool as well using
the data or added the data driven test
properties here uh so all the lines have
has been uh expanded with different
inputs so if I just expand this so you
can can see the all test has different
inputs and you can even run the test
right from here right here and you can
also come to Al test tool you can input
the data uh you can assign the data set
here expand the test line manually but
if you use the tool everything happens
automatically and I can what I can do
now I can go to the log entries in the
log entries you will see uh all the
details so we have the tag to identify
and each version indicates the run so we
are storing this in information and on
the right you would be able to see the
test
input uh and the duration how much time
it took and and if there were any error
message we can also log we log the error
message so in this case yeah the
expected document date uh document
number was 1 2 3 4 5 but we got 1 2 3
that's why it failed so I probably need
to go back and inspect my
prompt so this is an example of uh sales
line suggestions uh how we tested it and
how we plan now move to data driven
testing to to make it easier for us to
maintain the code
yeah yeah no that's that's cool because
so so this is like a very nice example
of the the accuracy tests and you're
doing like an absolute assertion here
right um have you thought about what we
could do if there are more complex
scenarios uh let's say yeah marketing
teex suggestions yeah yeah that's a good
question so uh the first one was okay
accuracy do what about the marketing
text scenario so the marketing text is
generating marketing text from product
description attributes how do we test
whether it's safe whether the generated
text is grounded enough is it accurate
so that kind of test is little bit
difficult to do it in Al so what we will
do is we'll take the output of the
generated marketing text put it to an
external evaluator and get the results
so I'll show that in a
moment so before before going into the
test itself I would like to talk about
the uh Azure AI studio uh it it's it's a
great way to start uh building llm apps
like to it's a good playground where you
can play play with different models you
can play with uh prompts uh so it's a
good place if outside business Central
if you want to test it out and there we
have a tool called evaluation which
helps us evaluate the responses
generated from llm applications so in
this case let's start by creating an
evaluation
um so you can give it give it a name uh
and then you can U choose what kind of
evaluation you want to do so let's do
stick with question and answer and with
context so once we do next uh so it it
is asking me for a test data or a data
set okay what what is this so this is uh
this would be all the responses
generated by the marketing text that's
what this would be how do we get it so I
have a suite uh created for marketing
text which is like quality test and uh I
have the data set so let's look at the
data set first so I have only three
inputs uh in this case so we are using
again using some standard properties
like test setup which would contain the
setup required for running the test so
in this case our test setup contains the
information about the product which we
will use to generate the marketing
text so let's look at that code unit uh
test code unit for the marketing text so
here we have two tests so first one uh
is about generating par tagline
paragraph with inspiring tone so uh so
again the helper method what we are
providing we will need your feedback
like the kind of helper method you would
need or is it even a good practice to
have this we'll we'll probably have to
discuss those things um so in the we can
use the test context again to get the
setup uh which would be used uh to
generate the marketing text and in the
format I'm specifying okay I need a
tagline and a paragraph and the tone I
want it to be
inspiring and the facts uh is basically
converting the test setup uh I'm
converting the properties of the Json
into a dictionary because that's I want
to reuse the function which we Ed for
marketing text and again this one is
there is no prompts inside the generate
marketing text function it's just it
would make an call uh through the
exposed procedures and that would
generate an answer in this case the
answer is the marketing text you would
ask why am I formatting question
question answer context in a particular
format we are doing that because our
external tool the Azure AI Studio
evaluator requires the data set to be in
a certain format that's the only reason
why we are sticking to this which is
which is being
standardized so the context uh so here
the context will become uh the facts
about the product so because that's what
will govern is your response grounded or
no and the question since this feature
does not have a dialog there is no place
where user can go and input something so
we have to build this question so the
question here is a task which we are
artificially making uh and saying okay
create marketing text for an item with
inspiring tone and uh with tagline and
paragraph we are just creating a very
simplified task and that is what we'll
use for evaluation and yeah finally how
do we output the data from the test Tool
uh so we will use some procedures again
uh like helper which in this case it's
set test output and you can pass
question context question and answer in
that format and what will happen is uh
okay so we'll do that but let me show
you the second test in the second test
everything is almost the same only thing
what I'm changing here is the tone
because I want to also test whether if I
used formal or if I use inspiring uh my
evaluation should be the same like it
should be safe it should be grounded it
should not have impact that uh so let's
look at the site uh so we have the test
here uh let me run this so I have
assigned the input data set already and
once I started so yeah before that let
me hide this I have a question for you
yeah how many tests would you think has
run behind the scene yeah yeah yes so
just so I understand what's going going
on here right we're trying to use the
test tool within the AR test tool within
business Central to generate a data set
as the test output that we can then
input to to the Azure Studio to run the
evaluation MH um and so you've written
two tests MH and your data set has three
um entries correct so uh because it's a
data driven test now that would be three
* two exactly so we have six that's
perfect answer yeah so yeah now you can
see we have run six test uh we can go
inside this and have a look uh so you
can see all the procedure names uh so
there are two procedure per code unit
and on the right we can see the input uh
you can see the code that it has run for
same input was run against two different
procedure that's why yeah as you said we
have six test but now we also have a
field called test output uh so in this
case the test output is what we sent out
from the test which has the context
question and the answer um so let me
just download the test output from here
uh so here the the file which gets
downloaded is the entire uh list of uh
test output in the view and let's go
back to the uh evaluation tool in the
Azure AI studio so there we will add our
data set let me upload the data set that
we just
generated and let it PA so you can see
here you get the context you get the
question you get the answer and let's
try to run the Tool uh okay so before
running the tool of course you would
have to configure which metrics you are
interested in so you can choose from
evaluating ground groundedness relevance
coherence so I I we won't go into
details about each of the metrics but
definitely you would have the option to
read into it and understand the
different metrics uh other thing to
point out is you would need uh an open
AI uh model deployment uh for this uh
for now and then the other one is you
can choose the risk and safety M Matrix
you would like to evaluate um yeah so
you can choose whatever you want in your
case and then yeah you can submit the
job so this takes a bit usually because
it schedules a job in the background it
takes some time to run as well uh so
before so instead of showing the result
from that I already have evaluated the
same output before so I've have just
done the evaluation for groundedness so
in this case it says okay all of the
responses were grounded so it gives a
score between 1 to five so this looks
good we can also manually verify those
and the risk and safety part is was was
the output generated safe enough and and
in different context so you can can uh
go there and have a look uh so that's
the good part so but again we won't
usually run the safety and risk and
safety metrics for normal inputs usually
we do that when we are doing red theming
because when when we when we are forcing
the system to do something wrong that's
when we use it and uh for example uh so
if I go to the input data
set so I would imagine like the harmful
data set can contain as big as like
thousand inputs so and it would be it
would be painful to write individual
test for each of them so that's why we
think this is the future for testing
hopefully and you can of course give us
feedback uh and we have this sensitive
flag which you can turn on so that you
don't expose user and user with
this yeah so we also have a comparison
metrix you can compare different things
right now we give out of the works how
many tests failed and what was the
duration but in future if you're using
the AI module from business Central we
would be able to hopefully be able to
give you token consumption and response
time so that you can compare your
prompts and play around while building
the application and of course uh we are
also thinking about integrating the
external metrics and provide some of
them out of the box but this would be in
the future even further
future yeah yeah yeah yeah so um yeah
now uh where can you guys all get
started so the very first thing we want
to call out is we have the the pull
request for the the AI test toolkit on
the first AKA Ms link definitely check
it out uh we yeah really Keen to get
feedback on all the test helpers that we
have available there like get input get
user query set output if you need more
but also like the general design
discussion like that we're building on
top of uh the test tool and all all that
kind of thing um secondly I know this
has been shared a few times s already
but I've got the link here again U if
you want to give the the private preview
of the business Central managed AI
access ago um there's the AK Ms link
there for uh the signup form um and uh
for trying out the Azure AI Studio you
just saw uh you can get that at ai.
azure.com um and then just some general
guidelines here is that you should think
about when you're writing your llm
scenarios to write code uh that wraps
around the prompts quite nice ly and
you'll be able to get to from an Al test
and then you know that should be able to
integrate nicely into the the test tool
later on and also uh generally for all
the co-pilot stuff uh ensure your Al
metadata with all your objects like the
tool tips captions uh that they're clear
clear and easy to understand uh with
like limited context because obviously
this is good for your users uh but it
also helps out co-pilot like finding
records and that kind of thing so I'll
uh share some more Mings um again yeah
you have the test tool kit uh definitely
talk to us as well on Via engage um if
you want to learn more about all the
co-pilot features it's BC aai uh if you
want to start developing with the the um
co-pilot developer tools and you don't
know where to start we've got the BC
start coding with AI learn a very short
link um and if that's too many links
just remember AK msbc all and that's
like the link of links um so you'll
you'll hopefully find what you're
looking for there and kind of to wrap up
I think I'll I'll finish with a video
which kind of showcases all the co-pilot
features that we have in the product
today and hopefully you can see why it
brings us a lot of value to have test
automation here but also like why it
would be good to have test automation as
you introduce your llm features on top
um and yeah hopefully it's a bit
inspirational of kind of what can be
done with these uh generative AI
Technologies keeping up with the pace of
work can be challenging especially when
your business is adapting and growing
transform the way work gets done with
Microsoft co-pilot in Dynamics 365
business Central your everyday AI
companion save time by asking questions
to find what you
need and onboard quickly with co-pilot
to guide you as you develop new
skills accelerate sales and Spark
creativity with marketing teex
suggestions tailor to your unique brand
using details already in business
Central like color color size and
material use co-pilot to create sales
quotes orders and invoices faster and
easier than ever before so you can
invest time in relationships instead of
paperwork simplify your day-to-day by
automating business processes with power
automate
flows and reclaim time for your most
impactful work by using co-pilot to keep
your finances organized from reconciling
bank statements to matching purchase
orders with e invoices all while using
analysis views to make data driven
decisions that Propel your business
forward to new levels of
success work smarter adapt faster and
perform better with Microsoft co-pilot
in business
Central cool yeah thanks that's like
everything if you got any questions let
us
know yeah I'll let you
yeah uh so with the AI test tool kit do
you guys Envision that as for purely
like manually running it or do you guys
think maybe there'd be a use case for
running it in like cicd pipelines if say
these files for this feature were
modified yes definitely we are thinking
about that like we would be eventually
we'll start with the tool first being
bing then the next step would be to
integrating in the cicd pipeline so we
have not thought about how it will work
work uh with GitHub and everything so
we'll we'll have to discuss that but we
need to first test it out also
internally so yeah but that's the goal
okay thank you ultimate all the things
right yeah because even the small model
change requires a lot of testing from
our end yeah it's all the risk and
safety mitigation yeah so we would like
to automate
that Sam I have a question oh maybe for
you um in one of the MOS um for the
sales marketing test uh test uh you
showed that uh in
the test you had a label yeah so uh
please generate for me marketing test
for these items however in
the uh in the B app yeah this is part of
the prompt so you have this in the
prompt as
well uh
not exactly because this is the user
input what the user would type but there
is no gener but there is no input mode
there is a generation mode out of the
box no there is a promt dialogue you see
uh so if you uh it's on your it's on the
slides
uh ah okay yeah so no so this one so
this is the sales suggestions where user
would input here in the prompt box yeah
no no another one uh with the the marke
marketing text yes so the marketing text
yeah uh uh so you don't have any user
cannot input anything there yes user
controls that like this attribute goes
in so that's why as I showed you uh we
built a context and we built a question
so the question what we built was a very
basic one like create marketing text
yeah that's that that would have a part
of the problem but not the entire
problem yeah this was the question so I
mean that uh for this copilot yeah uh
you generate this uh user message as
well in the in the copilot yes so it
means that uh you have this in the
copilot and you have the same in the
test yes we will have to give some task
uh like we are creating a task like what
is the because the external evaluation
tool requires a task to be able to judge
like did it do the task uh like did it
perform uh generate the response
correctly or no so for that we somehow
have to give a small uh action like
what's the task this llm app is doing so
that's the thing we had to expose or
give it give it a small because what
happens behind the scene it's a lot more
than what we just gave we are not giving
the entire like meta prom and system
prompt but but uh how how do you pass
the system prompts to the uh
test uh so yeah yeah maybe yes so the
the user input for the marketing text
suggestions tests that's not quite the
prompt right it's it's a list of item
attributes um and these item attributes
they get converted to a dictionary which
is what the product code expects to
receive to generate the user message in
the final prompt that gets sent to the
AL yeah right and I forgot the second
bit Yeah so so the system promt right
now I don't think we have helpers to so
uh get that in the test maybe you could
expose it internally like when you are
writing test so if you want you can
expose that as a procedure like okay get
me the system prompt if you want to do
that but normally we are what happens in
the market index there's a lot more than
just the item attributes there's a lot
of other prompts but we are not exposing
those the question was so okay so the
question is if I built my own test for
myop pilot in myop Pilot I have this
line of code add system message yeah and
then add user message I want to make a
test for that so um I didn't see in uh
in in your examples where I uh pass my
system message to the test so again so
we are so so depends on the test you
want to do let's say you want to
evaluate everything in Al so the sales
line suggestion so what we are doing is
we are just directly calling so we can
pass the user input using even test
Pages like if you have a promp dialogue
if you you have that kind of feature so
you can call test page do set input and
then do the generate action and once the
generate action is done whatever you get
in the content box you can read that and
do the evaluation there so in that case
you're not exposing any prompts in the
test you are just interacting with the
test page MH that's one scenario the
other scenario in the marketing text
where we are generating some content
which we cannot evaluate like okay you
want to check the grammar of the
sentence you can't do that it's not easy
in Al you would have to call some
external service so in this case is if
your external evaluator tool whatever
you write requires you to expose the
promt then you would have to if it
doesn't if it can work without exposing
the problem then you don't have to so
it's up to you in our marketing text
what we are exposing is the task as in
what's the basic task okay I want to
create a marketing text with this tone
and with this uh features but not not
more than that it's like the the
assertion that you're doing right so if
you if maybe I go back to the slide uh
can I go back I'll just do this um but
we can also discuss more in those
absolutely yeah is it here yeah this one
right so the in the bottom right you see
here the question which is that the
output is asking for the open sales
order amount and references the
identifier right so so yes that is a
prompt but it's it's not your system
prompt it's not the user input it's the
it's the test assertion MH it's just
it's called the question which I guess
that gets a bit confusing with the
nameing yeah yeah yeah we're over time
so uh if you want to go so if you have
any more questions we are here so you
can yeah feel free to come come here and
yeah thank you so much for attending the
session yeah thanks
